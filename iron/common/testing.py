# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How an operator declares the shapes it is tested at on a device, and the device
test harness: draw vectors, run it, judge and time it.
``iron/tests/operators/test_catalog.py`` runs every declaration against the
operator's ``reference()``. Nothing here imports pytest, so an operator module
stays importable without it.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, Iterable, Mapping

import aie.utils as aie_utils
import numpy as np
from aie.iron.device import Device
from aie.utils.benchmark import run_iters
from aie.utils.verify import Tolerance, Verdict
from ml_dtypes import bfloat16

if TYPE_CHECKING:
    from .declare import Operand, Operator

__all__ = ["Case", "Testing", "Vectors", "run_test", "time_call", "vectors"]

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Case:
    """One construction of an operator.

    Attributes:
        kwargs: The constructor's keywords.
        extensive: Keeps the case out of the default suite.
        id: Its name in test output, else the arguments.
        bench: CI tracks it over time (``pytest.mark.bench``).
        lower: The toolchain tests lower it to instructions on every
            device, as they do each operator's first default case.
    """

    kwargs: dict = field(default_factory=dict)
    extensive: bool = False
    id: str | None = None
    bench: bool = False
    lower: bool = False

    @property
    def label(self) -> str:
        return self.id or "-".join(f"{k}_{v}" for k, v in self.kwargs.items())


_Cases = Callable[[type, Device], Iterable[Case]]


@dataclass(frozen=True)
class Testing:
    """How an operator is checked against its reference on a device.

    Attributes:
        cases: ``Case``s, or callables of the class and the device returning
            them (a ``Sweep``).
        draw: A callable of the operator returning extra ``vectors`` arguments
            (``dict(normal=(op.A,))``), for inputs with preconditions.
    """

    __test__ = False  # pytest: a declaration, not a test class

    cases: Iterable[Case | _Cases] | _Cases
    draw: Callable[[Any], dict[str, Any]] | None = None

    def resolve(self, cls: type, dev: Device) -> list[Case]:
        """The cases for ``cls`` on ``dev``, so an inherited sweep reads the
        subclass's caps.
        """
        out = []
        for c in [self.cases] if callable(self.cases) else self.cases:
            out += list(c(cls, dev)) if callable(c) else [c]
        return out


@dataclass
class Vectors:
    """One operator's test vectors, keyed by its declared buffer names."""

    inputs: dict[str, np.ndarray]
    outputs: dict[str, np.ndarray]

    def __getitem__(self, name: str) -> np.ndarray:
        return self.inputs[name] if name in self.inputs else self.outputs[name]


def vectors(
    op,
    *,
    seed: int = 42,
    scale: float = 4.0,
    normal: Iterable[Operand] = (),
    centered: Iterable[Operand] = (),
    given: Mapping[Operand, np.ndarray | tuple[int, ...]] | None = None,
) -> Vectors:
    """Random inputs for ``op``'s declared buffers, and ``op.reference()``'s outputs.

    Args:
        scale: A uniform draw's scale; an integer buffer draws on ``[0, scale]``.
        normal: Inputs drawn normal instead (``op.A``).
        centered: Inputs shifted to centre on zero.
        given: Per input, an array as it is, or a shape to draw in place of
            the declared one (an operand the sequence packs).

    Raises:
        ValueError: An operand named is not one of ``op``'s inputs.
    """
    given = {o.name: v for o, v in (given or {}).items()}
    normal = {o.name for o in normal}
    centered = {o.name for o in centered}
    unknown = (given.keys() | normal | centered) - {b.name for b in op.inputs}
    if unknown:
        raise ValueError(f"{type(op).__name__} has no input {sorted(unknown)}")
    rng = np.random.default_rng(seed)
    inputs = {}
    for b in op.inputs:
        value = given.get(b.name)
        if isinstance(value, np.ndarray):
            inputs[b.name] = value
            continue
        # A coded operand is drawn as the logical tensor its reference reads.
        drawn = b.logical_shape if b.coded else b.host_shape
        shape = drawn if value is None else tuple(value)
        # A dtype that follows tuning is None until tuned; the unpacked operand is bf16.
        dtype = np.dtype(bfloat16 if b.dtype is None or b.coded else b.host_dtype)
        if dtype.kind not in "fc" and dtype != bfloat16:
            t = rng.integers(0, int(scale) + 1, shape).astype(dtype)
        else:
            draw = rng.standard_normal if b.name in normal else rng.random
            t = (draw(shape) * scale).astype(dtype)
            if b.name in centered:
                t = (t.astype(np.float32) - scale / 2).astype(dtype)
        inputs[b.name] = t
    return Vectors(inputs, op._call_reference(inputs))


def _report(buf_name: str, verdict: Verdict, tolerance: Tolerance) -> None:
    allowed = tolerance.max_mismatch_frac
    if verdict.n_mismatch and allowed > 0.0:
        within = "within" if verdict else "exceeds"
        logger.info(
            "%s: %d errors (%.2f%%) %s allowed rate of %.2f%%",
            buf_name,
            verdict.n_mismatch,
            verdict.n_mismatch / verdict.n_checked * 100,
            within,
            allowed * 100,
        )
    if not verdict:
        logger.warning("%s: %s", buf_name, verdict.detail)


def _nbytes(buf) -> int:
    """Bytes of tensor data moved, off the numpy view: the payload, not the
    page-rounded allocation, and ``buffer_object()`` has no ``.size()`` under HRX.
    """
    return buf.data.nbytes


def time_call(
    fn: Callable,
    *args,
    bytes_moved: int = 0,
    ops: float = 0.0,
    warmup: int = 0,
    iters: int = 20,
    record: Callable[[str, float], object] | None = None,
    **kwargs,
) -> None:
    """Time any compiled callable (an ``Operator``, a graph version, a shipped
    binary): the median NPU latency of ``iters`` runs of ``fn(*args, **kwargs)``.
    ``run_test`` is this plus the checked run and its judgement.

    Args:
        bytes_moved: Bytes moved a call, for the bandwidth figure; 0 records none.
        ops: Per call, for the throughput figure; 0 records none.
        warmup: Untimed runs before the ``iters`` timed ones.
        record: A test's ``record_property``: latency, its median absolute
            deviation over the timed runs, bandwidth and throughput.

    Raises:
        RuntimeError: ``fn`` did not report NPU execution time.
    """
    benchmark = run_iters(fn, *args, warmup=warmup, iters=iters, **kwargs)
    if benchmark.npu is None:
        raise RuntimeError("the callable did not report NPU execution time")
    latency_us = benchmark.npu.median_us
    if record is not None:
        record("Latency", latency_us)
        record("Latency MAD", benchmark.npu.mad_us)
        if bytes_moved:
            record("Bandwidth", bytes_moved / (latency_us * 1e-6) / 1e9)
        if ops:
            record("Throughput", ops / (latency_us * 1e-6) / 1e9)
    logger.info(
        "Latency (us): %.1f ± %.1f%s",
        latency_us,
        benchmark.npu.mad_us,
        (
            f"  Effective Bandwidth: {bytes_moved / (latency_us * 1e-6) / 1e9:.6e} GB/s"
            if bytes_moved
            else ""
        ),
    )


def run_test(
    operator: "Operator",
    inputs,
    outputs=None,
    *,
    tolerance: Tolerance,
    timed_iters: int = 20,
    record: Callable[[str, float], object] | None = None,
) -> dict[str, Verdict]:
    """Compile ``operator``, run it on the device, check its outputs, time it. The
    first run is the one checked, before a timed run rewrites an ``inout`` buffer.

    Args:
        inputs: A ``Vectors``, or every input by buffer name (an ``inout``
            buffer among them).
        outputs: Each buffer the operator writes, its expected result by
            name; ``operator.call_reference`` on ``inputs`` where None.
        record: ``time_call``'s.

    Returns:
        Each failing output's ``Verdict``, by name; empty where all passed.

    Raises:
        ValueError: ``inputs`` or ``outputs`` do not name the operator's
            buffers, or an expected result is None.
    """
    from .declare import Operator

    if isinstance(inputs, Vectors):
        inputs, outputs = inputs.inputs, inputs.outputs
    if not isinstance(operator, Operator):
        raise TypeError(f"run_test runs one declared Operator, not {operator!r}")
    declared = [b.name for b in operator.inputs]
    if sorted(inputs) != sorted(declared):
        raise ValueError(
            f"{type(operator).__name__} takes the inputs {declared}, "
            f"not {sorted(inputs)}"
        )
    operator.compile()
    # The device tensor type of whichever host runtime is selected (IRON_RUNTIME):
    # XRTTensor under XRT, HRXTensor under HRX. Both implement the Tensor interface
    # this function uses, and the operator dispatches through DefaultNPURuntime, which
    # is the matching runtime.
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    args, produced, total_bytes = [], {}, 0
    for b in operator.buffers:
        if b.fills:
            buf = tensor_class(b.device_form(inputs[b.name]))
        else:
            buf = tensor_class(b.host_shape, dtype=b.host_dtype)
        if b.drains:
            produced[b.name] = buf
        args.append(buf)
        total_bytes += _nbytes(buf)

    operator(*args)
    written = {name: buf.numpy() for name, buf in produced.items()}
    verdicts = operator.judge(inputs, written, tolerance, outputs)
    for name, verdict in verdicts.items():
        _report(name, verdict, tolerance)
    errors = {name: verdict for name, verdict in verdicts.items() if not verdict}

    ops = operator.resolved().ops()
    time_call(
        operator,
        *args,
        bytes_moved=total_bytes,
        ops=ops,
        iters=timed_iters,
        record=record,
    )
    return errors
