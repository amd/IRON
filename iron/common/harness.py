# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device test harness: draw vectors, run an operator, check and time it."""

from __future__ import annotations

import dataclasses
import inspect
from collections.abc import Mapping
from typing import Callable, NamedTuple

import aie.utils as aie_utils
import numpy as np
from aie.utils.benchmark import run_iters
from aie.utils.verify import Tolerance, Verdict, compare
from ml_dtypes import bfloat16

from .declare import Direction, Operator
from .image import OperatorImage


@dataclasses.dataclass
class Vectors:
    """One operator's test vectors, keyed by its declared buffer names."""

    inputs: dict[str, np.ndarray]
    outputs: dict[str, np.ndarray]

    def __getitem__(self, name: str) -> np.ndarray:
        return self.inputs[name] if name in self.inputs else self.outputs[name]


def vectors(op, *, seed=42, scale=4.0, normal=(), centered=(), **given) -> Vectors:
    """Random inputs for ``op``'s declared buffers, and ``op.reference()``'s outputs.

    Args:
        scale: A uniform draw's scale; an integer buffer draws on ``[0, scale]``.
        normal: Names drawn normal instead.
        centered: Names shifted to centre on zero.
        **given: An array as it is, or a shape to draw in place of the
            declared one (an operand the sequence packs).
    """
    unknown = set(given) - {b.name for b in op.inputs}
    if unknown:
        raise ValueError(f"{type(op).__name__} has no input {sorted(unknown)}")
    rng = np.random.default_rng(seed)
    inputs = {}
    for b in op.inputs:
        value = given.get(b.name)
        if isinstance(value, np.ndarray):
            inputs[b.name] = value
            continue
        shape = b.host_shape if value is None else tuple(value)
        # A dtype that follows tuning is None until tuned; the unpacked operand is bf16.
        dtype = np.dtype(bfloat16 if b.dtype is None else b.host_dtype)
        if dtype.kind not in "fc" and dtype != bfloat16:
            t = rng.integers(0, int(scale) + 1, shape).astype(dtype)
        else:
            draw = rng.standard_normal if b.name in normal else rng.random
            t = (draw(shape) * scale).astype(dtype)
            if b.name in centered:
                t = (t.astype(np.float32) - scale / 2).astype(dtype)
        inputs[b.name] = t
    return Vectors(inputs, expected(op, inputs))


def expected(
    op: Operator,
    inputs: Mapping[str, np.ndarray],
    values: Mapping[str, int] | None = None,
) -> dict[str, np.ndarray]:
    """``op.reference()``'s outputs on ``inputs``, by output name.

    Args:
        values: Per-call values; the reference is given those it names.

    Raises:
        ValueError: The reference returns another number of outputs than
            `op` declares.
    """
    named = inspect.signature(op.reference).parameters
    given = {k: v for k, v in (values or {}).items() if k in named}
    out = op.reference(*inputs.values(), **given)
    outs = (out,) if isinstance(out, np.ndarray) else tuple(out)
    names = [b.name for b in op.outputs]
    if len(outs) != len(names):
        raise ValueError(
            f"{type(op).__name__}.reference returned {len(outs)} outputs for {names}"
        )
    return dict(zip(names, outs))


def verify_buffer(
    output: np.ndarray,
    buf_name: str,
    reference: np.ndarray,
    tolerance: Tolerance,
    bound=None,
) -> Verdict:
    """Judge ``output``'s leading elements against ``reference`` with
    mlir-aie's ``compare``; ``bound`` is a bound tolerance's limit.
    """
    expected = np.asarray(reference).reshape(-1)
    got = np.asarray(output).reshape(-1)[: len(expected)]

    if tolerance.kind == "bound":
        if bound is None:
            raise ValueError(f"{buf_name}: a bound tolerance needs its bound=")
        bound = np.asarray(bound, np.float64)
        if bound.size != expected.size:  # a scalar, or one per row
            bound = np.broadcast_to(bound, np.shape(reference))
        bound = bound.reshape(-1)
    verdict = compare(got, expected, tolerance, bound=bound)
    allowed = tolerance.max_mismatch_frac
    if verdict.n_mismatch and allowed > 0.0:
        within = "within" if verdict else "exceeds"
        print(
            f"{buf_name}: {verdict.n_mismatch} errors "
            f"({verdict.n_mismatch / verdict.n_checked * 100:.2f}%) {within} allowed "
            f"rate of {allowed * 100:.2f}%"
        )
    if not verdict:
        print(f"{buf_name}: {verdict.detail}")
    return verdict


def _nbytes(buf) -> int:
    """Bytes of tensor data moved, for the effective-bandwidth figure.

    Reads the numpy view rather than the backend buffer handle: ``buffer_object()``
    returns a ``pyxrt.bo`` under XRT but an opaque handle under HRX, so ``.size()`` is
    not part of the Tensor interface. The view is also the payload size, not the
    page-rounded allocation.
    """
    return buf.data.nbytes


class Run(NamedTuple):
    """What a device run of one operator came back with."""

    errors: dict[str, Verdict]  # output name -> its failing verdict
    latency_us: float
    bandwidth_gbps: float


def run_test(
    operator: Operator,
    inputs,
    outputs=None,
    *,
    tolerance: Tolerance,
    warmup_iters: int = 1,
    timed_iters: int = 1,
    record: Callable[[str, float], object] | None = None,
) -> Run:
    """Compile ``operator``, run it on the device, time it, check its outputs.

    Args:
        inputs: A ``Vectors``, or the inputs by name in declaration order (an
            ``inout`` buffer among them).
        outputs: The expected outputs by name; None is not checked.
        record: A test's ``record_property``: latency, bandwidth and, from
            ``Operator.ops``, throughput.
    """
    if isinstance(inputs, Vectors):
        inputs, outputs = inputs.inputs, inputs.outputs
    if outputs is None:
        outputs = {}
    if not isinstance(operator, Operator):
        raise TypeError(f"run_test runs one declared Operator, not {operator!r}")
    fn = OperatorImage(operator).compile()
    # The device tensor type of whichever host runtime is selected (IRON_RUNTIME):
    # XRTTensor under XRT, HRXTensor under HRX. Both implement the Tensor interface
    # this function uses, and the operator dispatches through DefaultNPURuntime, which
    # is the matching runtime.
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    inout = {b.name for b in operator.buffers if b.direction is Direction.INOUT}
    ins = iter(inputs.items())
    outs = iter([(n, v) for n, v in outputs.items() if n not in inout])
    args, produced, total_bytes = [], {}, 0
    for b in operator.buffers:
        try:
            if b.direction is Direction.OUT:
                name, _ = next(outs)
                buf = tensor_class(b.host_shape, dtype=b.host_dtype)
                produced[name] = buf
            else:
                name, data = next(ins)
                buf = tensor_class(data)
                if b.direction is Direction.INOUT:
                    produced[name] = buf
        except StopIteration:
            raise ValueError(
                f"no {b.direction.value} given for buffer {b.name!r}"
            ) from None
        args.append(buf)
        total_bytes += _nbytes(buf)

    benchmark = run_iters(fn, *args, warmup=warmup_iters, iters=timed_iters)
    if benchmark.npu is None:
        raise RuntimeError("Operator callable did not report NPU execution time")
    latency_us = benchmark.npu.avg_us

    bound = None
    if tolerance.kind == "bound":
        assert tolerance.bound is not None
        bound = tolerance.bound(*inputs.values())
    errors = {}
    for name, expected in outputs.items():
        if expected is None:
            continue
        if name not in produced:
            print(f"Warning: Output buffer {name} not found in operator arguments")
            continue
        verdict = verify_buffer(
            produced[name].numpy(), name, expected, tolerance, bound=bound
        )
        if not verdict:
            errors[name] = verdict

    # NPU-side bandwidth (excludes host DMA transfer time)
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9
    if record is not None:
        record("Latency", latency_us)
        record("Bandwidth", bandwidth_gbps)
        ops = operator.resolved().ops()
        if ops:
            record("Throughput", ops / (latency_us * 1e-6) / 1e9)
    print(
        f"\nLatency (us): {latency_us:.1f}  Effective Bandwidth: {bandwidth_gbps:.6e} GB/s"
    )
    return Run(errors, latency_us, bandwidth_gbps)
