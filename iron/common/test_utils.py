# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import replace

import numpy as np
import torch
import aie.utils as aie_utils
from aie.utils.benchmark import run_iters
from aie.utils.verify import Tolerance, compare, nearly_equal
from ml_dtypes import bfloat16
from .base import AIEOperatorBase


def verify_buffer(
    output: np.ndarray | torch.Tensor,
    buf_name: str,
    reference: np.ndarray | torch.Tensor,
    rel_tol: float = 0.04,
    abs_tol: float = 1e-6,
    max_error_rate: float = 0.0,
    tolerance: Tolerance | None = None,
) -> list[int]:
    """
    Verify buffer contents match reference within tolerances.

    The comparison is mlir-aie's ``aie.utils.verify.compare``, by default under
    a relative ``Tolerance``: an element passes at ``|a - b| < max(abs_tol, rel_tol * (|a| + |b|))``,
    so ``rel_tol=abs_tol=0`` demands exact equality, and a NaN or infinity must
    meet the same value in the reference whatever ``max_error_rate`` allows.

    Args:
        output: Output buffer to verify
        buf_name: Name of buffer for error messages
        reference: Reference data to compare against
        rel_tol: Relative tolerance for comparison
        abs_tol: Absolute tolerance for comparison
        max_error_rate: Maximum fraction of elements allowed to exceed tolerances (0.0 to 1.0)
                       For example, 0.01 allows up to 1% of elements to fail
        tolerance: A ``Tolerance`` to judge by instead of ``rel_tol``, ``abs_tol``
                   and ``max_error_rate``; typically the contract of the kernel
                   the operator runs (``ExternalFunction.contract.tolerance``).
                   It must be judgeable element by element: no ``range_frac``
                   and not a bound.

    Returns:
        List of error indices. Empty if verification passes.
    """
    if tolerance is None:
        tolerance = Tolerance.relative(
            rel_tol, abs_tol, max_mismatch_frac=max_error_rate
        )
    elif tolerance.kind == "bound" or tolerance.range_frac is not None:
        raise ValueError(
            f"{buf_name}: a {tolerance.kind} tolerance with range_frac="
            f"{tolerance.range_frac} depends on more than the element it judges"
        )

    def _to_numpy(x):
        if isinstance(x, torch.Tensor):
            t = x.detach().cpu().contiguous()
            if t.dtype == torch.bfloat16:
                return t.view(torch.uint16).numpy().view(np.dtype("bfloat16"))
            return t.numpy()
        return np.asarray(x)

    expected_np = _to_numpy(reference).reshape((-1,))
    output = _to_numpy(output).reshape((-1,))

    if len(output) < len(expected_np):
        # Allow larger buffers - binning may have allocated more space than needed
        print(
            f"Buffer size mismatch for {buf_name}: expected {len(expected_np)}, got {len(output)}"
        )
        return list(range(len(output), len(expected_np)))
    output = output[: len(expected_np)]

    verdict = compare(output, expected_np, tolerance)
    allowed = tolerance.max_mismatch_frac
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
    both_nan = np.isnan(output.astype(np.float32)) & np.isnan(
        expected_np.astype(np.float32)
    )
    if tolerance.kind == "relative":
        # nearly_equal is the same per-element test, except that it also
        # rejects a NaN that meets a NaN.
        bad = ~nearly_equal(
            output, expected_np, rtol=tolerance.rtol or 0.0, atol=tolerance.atol
        )
        error_indices = np.flatnonzero(bad & ~both_nan).tolist()
    elif tolerance.kind == "exact":
        bad = output != expected_np.astype(output.dtype)
        error_indices = np.flatnonzero(bad & ~both_nan).tolist()
    else:
        each = replace(tolerance, max_mismatch_frac=0.0)
        error_indices = [
            i
            for i in range(len(output))
            if not compare(output[i : i + 1], expected_np[i : i + 1], each)
        ]
    for i in error_indices[:10]:
        print(
            f"Mismatch in {buf_name}[{i}]: expected {float(expected_np[i]):.6f}, got {float(output[i]):.6f}"
        )
    return error_indices


def _nbytes(buf) -> int:
    """Bytes of tensor data moved, for the effective-bandwidth figure.

    Reads the numpy view rather than the backend buffer handle: ``buffer_object()``
    returns a ``pyxrt.bo`` under XRT but an opaque handle under HRX, so ``.size()`` is
    not part of the Tensor interface. The view is also the more honest number -- it is
    the payload, not the (page-rounded) allocation.
    """
    return buf.data.nbytes


def run_test(
    operator: AIEOperatorBase,
    input_buffers: dict[str, torch.Tensor],
    output_buffers: dict[str, torch.Tensor | None],
    rel_tol: float = 0.04,
    abs_tol: float = 1e-6,
    max_error_rate: float = 0.0,
    warmup_iters: int = 1,
    timed_iters: int = 1,
    tolerance: Tolerance | None = None,
) -> tuple[dict[str, list[int]], float, float]:
    """
    Run operator test with specified input/output buffers.

    Args:
        operator: AIE operator instance (must be an AIEOperatorBase subclass)
        input_buffers: Dict mapping buffer names to input data arrays
        output_buffers: Dict mapping buffer names to reference output arrays
        rel_tol: Relative tolerance for comparison of output buffers
        abs_tol: Absolute tolerance for comparison of output buffers
        max_error_rate: Maximum fraction of elements allowed to exceed tolerances (0.0 to 1.0)
        warmup_iters: Number of warmup iterations before timing
        timed_iters: Number of timed iterations for latency/bandwidth measurement
        tolerance: Judge the outputs by this ``Tolerance`` instead; see
                   ``verify_buffer``

    Returns:
        (errors: dict, latency_us: float, bandwidth_gbps: float)
    """

    if not isinstance(operator, AIEOperatorBase):
        raise ValueError("run_test only supports AIEOperatorBase subclasses")

    operator.compile()
    op_func = operator.get_callable()

    args = []
    arg_spec = operator.get_arg_spec()

    input_iter = iter(input_buffers.items())
    output_iter = iter(output_buffers.items())
    output_map = {}
    inout_names = []

    total_bytes = 0

    # The device tensor type of whichever host runtime is selected (IRON_RUNTIME):
    # XRTTensor under XRT, HRXTensor under HRX. Both implement the Tensor interface
    # this function uses, and the operator dispatches through DefaultNPURuntime, which
    # is the matching runtime.
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    for spec in arg_spec:
        if spec.direction == "in":
            try:
                name, data = next(input_iter)
            except StopIteration:
                raise ValueError("Not enough input buffers provided for arg spec")
            buf = tensor_class.from_torch(data)
            args.append(buf)
            total_bytes += _nbytes(buf)
        elif spec.direction == "out":
            try:
                name, expected = next(output_iter)
            except StopIteration:
                raise ValueError("Not enough output buffers provided for arg spec")
            buf = tensor_class(spec.shape, dtype=spec.dtype)
            args.append(buf)
            output_map[name] = buf
            total_bytes += _nbytes(buf)
        elif spec.direction == "inout":
            try:
                name, data = next(input_iter)
            except StopIteration:
                raise ValueError("Not enough input buffers provided for inout arg spec")
            buf = tensor_class.from_torch(data)
            args.append(buf)
            output_map[name] = buf
            inout_names.append(name)
            total_bytes += _nbytes(buf)
        else:
            raise ValueError(f"Unsupported direction: {spec.direction}")

    benchmark = run_iters(op_func, *args, warmup=warmup_iters, iters=timed_iters)
    if benchmark.npu is None:
        raise RuntimeError("Operator callable did not report NPU execution time")
    latency_us = benchmark.npu.avg_us

    # Verify outputs
    errors = {}
    for buf_name, expected in output_buffers.items():
        if expected is None:
            continue
        if buf_name in output_map:
            buf = output_map[buf_name]
            output_torch = buf.to_torch()
            buf_errors = verify_buffer(
                output_torch,
                buf_name,
                expected,
                rel_tol,
                abs_tol,
                max_error_rate,
                tolerance=tolerance,
            )
            if buf_errors:
                errors[buf_name] = buf_errors
        else:
            print(f"Warning: Output buffer {buf_name} not found in operator arguments")

    # inout buffers are in output_map and are verified above if present in output_buffers

    # NPU-side bandwidth (excludes host DMA transfer time)
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    return errors, latency_us, bandwidth_gbps


def assert_matches_reference(
    operator: AIEOperatorBase,
    *inputs: torch.Tensor,
    tolerance: Tolerance | None = None,
) -> None:
    """Dispatch ``operator`` once and assert its output matches ``reference()``.

    The expected output is ``operator.reference(*inputs)``, each input shaped
    as its argument spec, so the test and a ``dispatch="compare"`` sequence
    hold the operator to the same reference. Latency and bandwidth are printed
    in the form the CI metrics parse.

    Args:
        operator: An operator with a single output and a ``reference()``
        inputs: Its ``"in"`` arguments, in argument-spec order
        tolerance: How close the output must come; defaults to
                   ``operator.reference_tolerance()``, the contract of the
                   kernel it runs
    """
    in_specs = [s for s in operator.get_arg_spec() if s.direction == "in"]
    if len(inputs) != len(in_specs):
        raise ValueError(
            f"{type(operator).__name__} takes {len(in_specs)} inputs, "
            f"got {len(inputs)}"
        )
    expected = operator.reference(
        *(x.reshape(spec.shape) for x, spec in zip(inputs, in_specs))
    )
    if tolerance is None:
        tolerance = operator.reference_tolerance()
    if tolerance is None:
        raise ValueError(
            f"{type(operator).__name__} declares no tolerance; pass tolerance="
        )

    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        {f"input{i}": x for i, x in enumerate(inputs)},
        {"output": expected},
        tolerance=tolerance,
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


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
