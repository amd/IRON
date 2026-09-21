# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import dataclasses
from typing import NamedTuple

import numpy as np
import pytest
import torch
import aie.utils as aie_utils
from aie.utils.benchmark import run_iters
from aie.utils.verify import nearly_equal
from ml_dtypes import bfloat16

_TORCH_DTYPES = {
    bfloat16: torch.bfloat16,
    np.float32: torch.float32,
    np.int8: torch.int8,
    np.uint8: torch.uint8,
    np.int16: torch.int16,
    np.int32: torch.int32,
}


def torch_dtype(dtype) -> torch.dtype:
    """The torch dtype of a numpy scalar type (``ml_dtypes.bfloat16`` included)."""
    key = np.dtype(dtype).type
    if key not in _TORCH_DTYPES:
        raise TypeError(f"no torch dtype for {dtype!r}")
    return _TORCH_DTYPES[key]


@dataclasses.dataclass
class Golden:
    """Test vectors for one operator, keyed by its declared buffer names."""

    inputs: dict[str, torch.Tensor]
    outputs: dict[str, torch.Tensor]

    def __getitem__(self, name: str) -> torch.Tensor:
        return self.inputs[name] if name in self.inputs else self.outputs[name]


def golden(op, *, seed=42, scale=4.0, normal=(), centered=(), **given) -> Golden:
    """Random inputs for ``op``'s declared buffers, and its reference's outputs.

    Each ``In`` buffer, in declaration order, is ``torch.rand`` of its declared
    shape and dtype times ``scale`` (``torch.randn`` for the names in
    ``normal``, shifted to centre on zero for those in ``centered``; an
    integer buffer draws uniformly on ``[0, scale]``), or comes from
    ``given``: a tensor as it is, or a shape to draw in place of the declared
    one (an operand the sequence packs, such as flm GEMM's B). The outputs
    are ``op.reference(*inputs)`` under the declared output names.
    """
    unknown = set(given) - {b.name for b in op.inputs}
    if unknown:
        raise ValueError(f"{type(op).__name__} has no input {sorted(unknown)}")
    torch.manual_seed(seed)
    inputs = {}
    for b in op.inputs:
        value = given.get(b.name)
        if isinstance(value, torch.Tensor):
            inputs[b.name] = value
            continue
        shape = tuple(b.shape) if value is None else tuple(value)
        # A buffer whose dtype follows tuning (flm GEMM's packed B) has none
        # until tuned; the unpacked operand a shape override asks for is bf16.
        dtype = torch.bfloat16 if b.dtype is None else torch_dtype(b.dtype)
        if not dtype.is_floating_point:
            t = torch.randint(0, int(scale) + 1, shape, dtype=dtype)
        else:
            draw = torch.randn if b.name in normal else torch.rand
            t = draw(shape, dtype=dtype) * scale
            if b.name in centered:
                t = t - scale / 2
        inputs[b.name] = t
    out = op.reference(*inputs.values())
    outs = (out,) if isinstance(out, torch.Tensor) else tuple(out)
    names = [b.name for b in op.outputs]
    if len(outs) != len(names):
        raise ValueError(
            f"{type(op).__name__}.reference returned {len(outs)} outputs for {names}"
        )
    return Golden(inputs, dict(zip(names, outs)))


# TODO: Consider upstreaming generic buffer utilities to mlir-aie once operator abstractions stabilize.


def _to_numpy(x):
    if isinstance(x, torch.Tensor):
        t = x.detach().cpu().contiguous()
        if t.dtype == torch.bfloat16:
            return t.view(torch.uint16).numpy().view(np.dtype("bfloat16"))
        return t.numpy()
    return np.asarray(x)


def verify_buffer(
    output: np.ndarray | torch.Tensor,
    buf_name: str,
    reference: np.ndarray | torch.Tensor,
    rel_tol: float = 0.04,
    abs_tol: float = 1e-6,
    max_error_rate: float = 0.0,
) -> list[int]:
    """The indices where ``output`` is outside tolerance of ``reference``.

    The comparator is mlir-aie's (``aie.utils.verify.nearly_equal``):
    ``|a - b| < max(abs_tol, rel_tol * (|a| + |b|))``, in float32, with a NaN
    on either side a mismatch. ``rel_tol = abs_tol = 0`` is an exact gate.
    ``max_error_rate`` lets that fraction of the elements miss; a shorter
    output than reference counts the missing elements as errors.
    """
    expected = _to_numpy(reference).reshape(-1)
    got = _to_numpy(output).reshape(-1)
    errors: list[int] = []
    if len(got) < len(expected):
        print(
            f"Buffer size mismatch for {buf_name}: expected {len(expected)}, got {len(got)}"
        )
        errors.extend(range(len(expected) - len(got)))
    n = min(len(got), len(expected))
    ok = nearly_equal(got[:n], expected[:n], rtol=rel_tol, atol=abs_tol)
    bad = np.flatnonzero(~ok).tolist()
    for i in bad[:10]:
        print(
            f"Mismatch in {buf_name}[{i}]: expected {float(expected[i]):.6f}, got {float(got[i]):.6f}"
        )
    errors.extend(bad)
    if errors and max_error_rate > 0.0:
        allowed = int(n * max_error_rate)
        verdict = "within" if len(errors) <= allowed else "exceeds"
        print(
            f"{buf_name}: {len(errors)} errors ({len(errors) / n * 100:.2f}%) {verdict} "
            f"allowed rate of {max_error_rate * 100:.2f}% ({allowed} errors)"
        )
        if len(errors) <= allowed:
            return []
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
    not part of the Tensor interface. The view is also the more honest number -- it is
    the payload, not the (page-rounded) allocation.
    """
    return buf.data.nbytes


class Run(NamedTuple):
    """What a device run of one operator came back with."""

    errors: dict[str, list[int]]  # output name -> mismatched indices
    latency_us: float
    bandwidth_gbps: float


def run_test(
    operator,
    inputs,
    outputs=None,
    *,
    rel_tol: float = 0.04,
    abs_tol: float = 1e-6,
    max_error_rate: float = 0.0,
    warmup_iters: int = 1,
    timed_iters: int = 1,
) -> Run:
    """Compile ``operator``, run it on the device, time it, check its outputs.

    ``inputs`` is a :class:`Golden`, or the inputs by name with ``outputs``
    the expected outputs by name (an expected value of ``None`` is not
    checked); both are consumed in the order of the operator's declared
    buffers. An ``inout`` buffer is given as an input and checked under that
    name. Latency (the NPU's own time) and effective bandwidth are recorded
    for the CSV and returned.
    """
    if isinstance(inputs, Golden):
        inputs, outputs = inputs.inputs, inputs.outputs
    if not hasattr(operator, "buffers"):
        raise ValueError("run_test runs one declared operator (see Operator.buffers)")
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
                buf = tensor_class(tuple(b.shape), dtype=b.dtype)
                produced[name] = buf
            else:
                name, data = next(ins)
                buf = tensor_class.from_torch(data)
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
            produced[name].to_torch(), name, expected, rel_tol, abs_tol, max_error_rate
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


# -- one test per operator ------------------------------------------------------


def _case_id(kwargs: dict) -> str:
    return "-".join(f"{k}_{v}" for k, v in kwargs.items())


def _mark(regular: bool) -> list:
    return [] if regular else [pytest.mark.extensive]


def operator_test(
    cls, cases, *, rel_tol=0.04, abs_tol=1e-6, max_error_rate=0.0, draw=None
):
    """A parametrized pytest function that runs ``cls`` against its reference.

    Each case is a dict of constructor keyword arguments, or a ``pytest.param``
    wrapping one (for marks or an id). The test constructs
    ``cls(**case, context=aie_context)``, draws its vectors with
    :func:`golden` (``draw``: extra ``golden()`` arguments, or a callable of
    the operator returning them), runs it through :func:`run_test` and asserts
    no output element is off. Case ids are the arguments, ``name_value``
    joined by ``-``. Assign the result to a ``test_*`` name.
    """
    params = []
    for case in cases:
        if hasattr(case, "values") and hasattr(case, "marks"):  # a pytest.param
            (kwargs,) = case.values
            params.append(
                pytest.param(kwargs, id=case.id or _case_id(kwargs), marks=case.marks)
            )
        else:
            params.append(pytest.param(case, id=_case_id(case)))

    @pytest.mark.parametrize("case", params)
    def test(case, aie_context):
        op = cls(**case, context=aie_context)
        extra = draw(op) if callable(draw) else (draw or {})
        run = run_test(
            op,
            golden(op, **extra),
            rel_tol=rel_tol,
            abs_tol=abs_tol,
            max_error_rate=max_error_rate,
        )
        assert not run.errors, f"{cls.__name__}({_case_id(case)}) failed: {run.errors}"

    return test


def channeled_unary_cases(
    input_lengths, tile_cap, channels=(1, 2), regular=2048, **extra
):
    """Cases for a channeled unary operator: every column count the device has
    by every channel count, at each length, with the tile capped; only the
    ``regular`` length is in the default suite. ``channels=None`` leaves the
    channel count out (an operator without one)."""
    cases = []
    for il, cols, ch, ts, _ in make_channeled_unary_params(
        input_lengths, tile_cap, [1] if channels is None else channels
    ):
        kwargs = dict(size=il, num_aie_columns=cols)
        if channels is not None:
            kwargs["num_channels"] = ch
        kwargs.update(tile_size=ts, **extra)
        cases.append(pytest.param(kwargs, marks=_mark(il == regular)))
    return cases


def binary_elementwise_cases(input_lengths, tile_cap=None, regular=2048, **extra):
    """Cases for a binary elementwise operator, as :func:`channeled_unary_cases`."""
    return [
        pytest.param(
            dict(size=il, num_aie_columns=cols, tile_size=ts, **extra),
            marks=_mark(il == regular),
        )
        for il, cols, ts, _ in make_binary_elementwise_params(input_lengths, tile_cap)
    ]


def make_channeled_unary_params(input_lengths, tile_size_cap, num_channels_choices):
    """Generate parameter tuples for channeled unary operator tests.

    Yields:
        (input_length, num_aie_columns, num_channels, tile_size, is_extensive)
    """
    max_aie_columns = aie_utils.get_current_device().cols
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            for num_channels in num_channels_choices:
                total_cores = num_aie_columns * num_channels
                tile_size = input_length // total_cores
                if tile_size > tile_size_cap:
                    tile_size = tile_size_cap
                if tile_size * total_cores != input_length:
                    continue
                is_extensive = input_length != 2048
                yield (
                    input_length,
                    num_aie_columns,
                    num_channels,
                    tile_size,
                    is_extensive,
                )


def make_binary_elementwise_params(input_lengths, tile_size_cap=None):
    """Generate parameter tuples for binary elementwise operator tests.

    Yields:
        (input_length, num_aie_columns, tile_size, is_extensive)
    """
    max_aie_columns = aie_utils.get_current_device().cols
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = input_length // num_aie_columns
            if tile_size_cap is not None and tile_size > tile_size_cap:
                tile_size = tile_size_cap
            if tile_size * num_aie_columns != input_length:
                continue
            is_extensive = input_length != 2048
            yield (input_length, num_aie_columns, tile_size, is_extensive)
