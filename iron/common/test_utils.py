# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import dataclasses

import numpy as np
import torch
import aie.utils as aie_utils
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16
from .base import AIEOperatorBase

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
    ``normal``, shifted to centre on zero for those in ``centered``), or comes
    from ``given``: a tensor as it is, or a shape to draw in place of the
    declared one (an operand the sequence packs, such as flm GEMM's B). The
    outputs are ``op.reference(*inputs)`` under the declared output names.
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
        draw = torch.randn if b.name in normal else torch.rand
        t = draw(shape, dtype=torch_dtype(b.dtype)) * scale
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


def nearly_equal(
    a: float,
    b: float,
    rel_tol: float = 128 * np.finfo(np.float32).eps,
    abs_tol: float = np.finfo(np.float32).tiny,
) -> bool:
    """
    Compare two floating point numbers for approximate equality.

    Adapted from Stack Overflow, License CC BY-SA 4.0
    Original author: P-Gn
    Source: https://stackoverflow.com/a/32334103
    """
    if np.finfo(np.float32).eps > rel_tol:
        raise ValueError(f"rel_tol {rel_tol!r} must be >= machine epsilon")
    if rel_tol >= 1.0:
        raise ValueError(f"rel_tol {rel_tol!r} must be < 1.0")

    if a == b:
        return True

    diff = abs(float(a) - float(b))
    norm = min(abs(float(a)) + abs(float(b)), np.finfo(np.float32).max)
    return diff < max(abs_tol, rel_tol * norm)


def verify_buffer(
    output: np.ndarray | torch.Tensor,
    buf_name: str,
    reference: np.ndarray | torch.Tensor,
    rel_tol: float = 0.04,
    abs_tol: float = 1e-6,
    max_error_rate: float = 0.0,
) -> list[int]:
    """
    Verify buffer contents match reference within tolerances.

    Args:
        output: Output buffer to verify
        buf_name: Name of buffer for error messages
        reference: Reference data to compare against
        rel_tol: Relative tolerance for comparison
        abs_tol: Absolute tolerance for comparison
        max_error_rate: Maximum fraction of elements allowed to exceed tolerances (0.0 to 1.0)
                       For example, 0.01 allows up to 1% of elements to fail

    Returns:
        List of error indices. Empty if verification passes.
    """
    errors = []

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
        errors.extend(i for i in range(abs(len(output) - len(expected_np))))
    compare_len = min(len(output), len(expected_np))
    diff = np.abs(
        output[:compare_len].astype(float) - expected_np[:compare_len].astype(float)
    )
    norm = np.minimum(
        np.abs(output[:compare_len].astype(float))
        + np.abs(expected_np[:compare_len].astype(float)),
        np.finfo(np.float32).max,
    )
    # Use `>`, not `>=`, here, so that a user can pass rel_tol=abs_tol=0
    # check exact equality.
    mask = diff > np.maximum(abs_tol, rel_tol * norm)
    error_indices = np.where(mask)[0].tolist()
    for i in error_indices[:10]:
        print(
            f"Mismatch in {buf_name}[{i}]: expected {float(expected_np[i]):.6f}, got {float(output[i]):.6f}"
        )
    errors.extend(error_indices)

    # Check if error rate is acceptable
    if max_error_rate > 0.0 and len(errors) > 0:
        error_rate = len(errors) / compare_len
        max_allowed_errors = int(compare_len * max_error_rate)
        if len(errors) <= max_allowed_errors:
            print(
                f"{buf_name}: {len(errors)} errors ({error_rate*100:.2f}%) within allowed rate of {max_error_rate*100:.2f}% ({max_allowed_errors} errors)"
            )
            return []  # Pass - within allowed error rate
        else:
            print(
                f"{buf_name}: {len(errors)} errors ({error_rate*100:.2f}%) exceeds allowed rate of {max_error_rate*100:.2f}% ({max_allowed_errors} errors)"
            )

    return errors


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
                output_torch, buf_name, expected, rel_tol, abs_tol, max_error_rate
            )
            if buf_errors:
                errors[buf_name] = buf_errors
        else:
            print(f"Warning: Output buffer {buf_name} not found in operator arguments")

    # inout buffers are in output_map and are verified above if present in output_buffers

    # NPU-side bandwidth (excludes host DMA transfer time)
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    return errors, latency_us, bandwidth_gbps


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
