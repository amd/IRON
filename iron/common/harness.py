# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device test harness: draw vectors, run an operator, check and time it.

Everything is numpy, like an operator's ``reference``: a draw becomes the
device buffer it is handed to, and mlir-aie's ``compare`` judges what comes
back. How an operator declares the shapes it is tested at is in
``iron.common.testing``, which imports no pytest.
"""

from __future__ import annotations

import dataclasses
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
    """Random inputs for ``op``'s declared buffers, and its reference's outputs.

    The expected outputs are ``op.reference()`` on the inputs drawn here,
    not an independent oracle.

    Each ``In`` buffer, in declaration order, is a uniform draw of its declared
    shape and dtype times ``scale`` (a normal draw for the names in
    ``normal``, shifted to centre on zero for those in ``centered``; an
    integer buffer draws uniformly on ``[0, scale]``), or comes from
    ``given``: an array as it is, or a shape to draw in place of the declared
    one (an operand the sequence packs, such as flm GEMM's B). The outputs
    are ``op.reference(*inputs)`` under the declared output names.
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
        # A buffer whose dtype follows tuning (flm GEMM's packed B) has none
        # until tuned; the unpacked operand a shape override asks for is bf16.
        dtype = np.dtype(bfloat16 if b.dtype is None else b.host_dtype)
        # ml_dtypes' bfloat16 has no numpy kind of its own: a float, as here.
        if dtype.kind not in "fc" and dtype != bfloat16:
            t = rng.integers(0, int(scale) + 1, shape).astype(dtype)
        else:
            draw = rng.standard_normal if b.name in normal else rng.random
            t = (draw(shape) * scale).astype(dtype)
            if b.name in centered:
                t = (t.astype(np.float32) - scale / 2).astype(dtype)
        inputs[b.name] = t
    out = op.reference(*inputs.values())
    outs = (out,) if isinstance(out, np.ndarray) else tuple(out)
    names = [b.name for b in op.outputs]
    if len(outs) != len(names):
        raise ValueError(
            f"{type(op).__name__}.reference returned {len(outs)} outputs for {names}"
        )
    return Vectors(inputs, dict(zip(names, outs)))


def verify_buffer(
    output: np.ndarray,
    buf_name: str,
    reference: np.ndarray,
    tolerance: Tolerance,
    bound=None,
) -> Verdict:
    """Judge ``output`` against ``reference`` with mlir-aie's ``compare``.

    The tolerance is the contract of the kernel the operator runs or a
    ``Tolerance.relative``, say. An output longer than the reference is
    judged on its leading elements; a shorter one fails as a shape mismatch.
    A bound tolerance's limit is ``bound``, evaluated on the inputs as
    ``compare`` takes it, of the output's size or broadcast to its shape.

    Returns:
        The ``Verdict``: true when the output passes, otherwise carrying the
        mismatch count, the first bad index and a ``detail`` line.
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

    ``inputs`` is a ``Vectors``, or the inputs by name with ``outputs``
    the expected outputs by name (an expected value of ``None`` is not
    checked); both are consumed in the order of the operator's declared
    buffers. An ``inout`` buffer is given as an input and checked under that
    name. The outputs are judged as ``verify_buffer`` judges them, by
    ``tolerance``; a bound tolerance's limit is its bound on the
    inputs, which holds for an elementwise kernel's contract whatever shape
    the operator gives its operands. Latency (the NPU's own time) and effective
    bandwidth are returned, and handed to ``record`` (a test's pytest
    ``record_property``, which the root conftest writes to the CSV) with
    throughput from ``Operator.ops`` for an
    operator that computes.
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
    # An inout buffer's expected value is among the outputs, under its name,
    # but its tensor is the input given: the outputs a buffer is made for
    # are the others.
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
