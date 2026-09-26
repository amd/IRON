# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device test harness: draw vectors, run an operator, check and time it.

Everything is numpy, like an operator's ``reference``: a draw becomes the
device buffer it is handed to, and mlir-aie's ``compare`` judges what comes
back. How an operator declares the shapes it is tested at is in
:mod:`iron.common.testing`, which imports no pytest.
"""

from __future__ import annotations

import dataclasses
from typing import NamedTuple

import aie.utils as aie_utils
import numpy as np
from aie.utils.benchmark import run_iters
from aie.utils.verify import Tolerance, compare, nearly_equal
from ml_dtypes import bfloat16

from .declare import Operator


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


# TODO: Consider upstreaming generic buffer utilities to mlir-aie once operator abstractions stabilize.


def verify_buffer(
    output: np.ndarray,
    buf_name: str,
    reference: np.ndarray,
    rel_tol: float = 0.04,
    abs_tol: float = 1e-6,
    max_error_rate: float = 0.0,
    tolerance: Tolerance | None = None,
) -> list[int]:
    """The indices where ``output`` is outside tolerance of ``reference``.

    The judge is mlir-aie's ``aie.utils.verify.compare``, by default under a
    relative ``Tolerance``: an element passes at
    ``|a - b| < max(abs_tol, rel_tol * (|a| + |b|))``, so
    ``rel_tol = abs_tol = 0`` is an exact gate, and a NaN or infinity must meet
    the same value in the reference whatever ``max_error_rate`` allows.
    ``max_error_rate`` lets that fraction of the elements miss; a shorter
    output than reference counts the missing elements as errors.

    ``tolerance`` judges by that instead of the three numbers: typically the
    contract of the kernel the operator runs. It must be judgeable element by
    element: no ``range_frac`` and not a bound.
    """
    judge = (
        Tolerance.relative(rel_tol, abs_tol, max_mismatch_frac=max_error_rate)
        if tolerance is None
        else tolerance
    )
    if judge.kind == "bound" or judge.range_frac is not None:
        raise ValueError(
            f"{buf_name}: a {judge.kind} tolerance with range_frac="
            f"{judge.range_frac} depends on more than the element it judges"
        )
    expected = np.asarray(reference).reshape(-1)
    got = np.asarray(output).reshape(-1)
    if len(got) < len(expected):
        print(
            f"Buffer size mismatch for {buf_name}: expected {len(expected)}, got {len(got)}"
        )
        return list(range(len(got), len(expected)))
    got = got[: len(expected)]

    verdict = compare(got, expected, judge)
    allowed = judge.max_mismatch_frac
    if verdict.n_mismatch and allowed > 0.0:
        within = "within" if verdict else "exceeds"
        print(
            f"{buf_name}: {verdict.n_mismatch} errors "
            f"({verdict.n_mismatch / verdict.n_checked * 100:.2f}%) {within} allowed "
            f"rate of {allowed * 100:.2f}%"
        )
    if verdict:
        return []

    print(f"{buf_name}: {verdict.detail}")
    # compare() judges; it does not list the elements.
    both_nan = np.isnan(got.astype(np.float32)) & np.isnan(expected.astype(np.float32))
    if judge.kind == "relative":
        # nearly_equal is the same per-element test, except that it also
        # rejects a NaN that meets a NaN.
        bad = ~nearly_equal(got, expected, rtol=judge.rtol or 0.0, atol=judge.atol)
    elif judge.kind == "exact":
        bad = got != expected.astype(got.dtype)
    else:
        each = dataclasses.replace(judge, max_mismatch_frac=0.0)
        bad = np.array(
            [
                not compare(got[i : i + 1], expected[i : i + 1], each)
                for i in range(len(got))
            ],
            dtype=bool,
        )
    errors = np.flatnonzero(bad & ~both_nan).tolist()
    for i in errors[:10]:
        print(
            f"Mismatch in {buf_name}[{i}]: expected {float(expected[i]):.6f}, got {float(got[i]):.6f}"
        )
    return errors


# -- metrics ------------------------------------------------------------------
# A test reports its figures here; the root conftest takes them after each
# test and writes one CSV row per test (mean, median, min, max, stddev over
# the iterations).

_METRICS: list[tuple[str, float]] = []


def record_metric(name: str, value: float) -> None:
    """Report a figure ("Latency", "Bandwidth", "Throughput", ...) for the CSV."""
    _METRICS.append((name, float(value)))


def take_metrics() -> list[tuple[str, float]]:
    """The figures recorded since the last call, cleared."""
    out = list(_METRICS)
    _METRICS.clear()
    return out


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

    errors: dict[str, list[int]]  # output name -> mismatched indices
    latency_us: float
    bandwidth_gbps: float


def run_test(
    operator: Operator,
    inputs,
    outputs=None,
    *,
    rel_tol: float = 0.04,
    abs_tol: float = 1e-6,
    max_error_rate: float = 0.0,
    warmup_iters: int = 1,
    timed_iters: int = 1,
    tolerance: Tolerance | None = None,
) -> Run:
    """Compile ``operator``, run it on the device, time it, check its outputs.

    ``inputs`` is a :class:`Vectors`, or the inputs by name with ``outputs``
    the expected outputs by name (an expected value of ``None`` is not
    checked); both are consumed in the order of the operator's declared
    buffers. An ``inout`` buffer is given as an input and checked under that
    name. The outputs are judged as :func:`verify_buffer` judges them, by
    ``tolerance`` when given. Latency (the NPU's own time) and effective
    bandwidth are recorded for the CSV and returned.
    """
    if isinstance(inputs, Vectors):
        inputs, outputs = inputs.inputs, inputs.outputs
    if outputs is None:
        outputs = {}
    if not isinstance(operator, Operator):
        raise TypeError(f"run_test runs one declared Operator, not {operator!r}")
    operator.compile()
    fn = operator.get_callable()
    # The device tensor type of whichever host runtime is selected (IRON_RUNTIME):
    # XRTTensor under XRT, HRXTensor under HRX. Both implement the Tensor interface
    # this function uses, and the operator dispatches through DefaultNPURuntime, which
    # is the matching runtime.
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    ins, outs = iter(inputs.items()), iter(outputs.items())
    args, produced, total_bytes = [], {}, 0
    for b in operator.buffers:
        try:
            if b.direction == "out":
                name, _ = next(outs)
                buf = tensor_class(b.host_shape, dtype=b.host_dtype)
                produced[name] = buf
            else:
                name, data = next(ins)
                buf = tensor_class(data)
                if b.direction == "inout":
                    produced[name] = buf
        except StopIteration:
            raise ValueError(f"no {b.direction} given for buffer {b.name!r}") from None
        args.append(buf)
        total_bytes += _nbytes(buf)

    benchmark = run_iters(fn, *args, warmup=warmup_iters, iters=timed_iters)
    if benchmark.npu is None:
        raise RuntimeError("Operator callable did not report NPU execution time")
    latency_us = benchmark.npu.avg_us

    errors = {}
    for name, expected in outputs.items():
        if expected is None:
            continue
        if name not in produced:
            print(f"Warning: Output buffer {name} not found in operator arguments")
            continue
        bad = verify_buffer(
            produced[name].numpy(),
            name,
            expected,
            rel_tol,
            abs_tol,
            max_error_rate,
            tolerance=tolerance,
        )
        if bad:
            errors[name] = bad

    # NPU-side bandwidth (excludes host DMA transfer time)
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9
    record_metric("Latency", latency_us)
    record_metric("Bandwidth", bandwidth_gbps)
    print(
        f"\nLatency (us): {latency_us:.1f}  Effective Bandwidth: {bandwidth_gbps:.6e} GB/s"
    )
    return Run(errors, latency_us, bandwidth_gbps)
