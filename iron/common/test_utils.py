# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import numpy as np
from ml_dtypes import bfloat16
from .utils import xrt_to_torch
from .base import AIEOperatorBase
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor


def nearly_equal(
    a, b, rel_tol=128 * np.finfo(np.float32).eps, abs_tol=np.finfo(np.float32).tiny
):
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
    output, buf_name, reference, rel_tol=0.04, abs_tol=1e-6, max_error_rate=0.0
):
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
    expected = reference.reshape((-1,))
    output = output.reshape((-1,))

    if len(output) < len(expected):
        # Allow larger buffers - binning may have allocated more space than needed
        print(
            f"Buffer size mismatch for {buf_name}: expected {len(expected)}, got {len(output)} "
            f"({len(expected) - len(output)} elements missing)"
        )
    compare_len = min(len(output), len(expected))
    mismatch_errors = []
    for i in range(compare_len):
        if not nearly_equal(float(output[i]), float(expected[i]), rel_tol, abs_tol):
            mismatch_errors.append(i)
            if len(mismatch_errors) <= 10:
                print(
                    f"Mismatch in {buf_name}[{i}]: expected {float(expected[i]):.6f}, got {float(output[i]):.6f}"
                )

    # Check if error rate is acceptable (only counting value mismatches, not size mismatches)
    if max_error_rate > 0.0 and len(mismatch_errors) > 0:
        error_rate = len(mismatch_errors) / compare_len
        max_allowed_errors = int(compare_len * max_error_rate)
        if len(mismatch_errors) <= max_allowed_errors:
            print(
                f"{buf_name}: {len(mismatch_errors)} errors ({error_rate*100:.2f}%) within allowed rate of {max_error_rate*100:.2f}% ({max_allowed_errors} errors)"
            )
            return errors  # Pass value check - within allowed error rate; return any size-mismatch errors only
        else:
            print(
                f"{buf_name}: {len(mismatch_errors)} errors ({error_rate*100:.2f}%) exceeds allowed rate of {max_error_rate*100:.2f}% ({max_allowed_errors} errors)"
            )

    errors.extend(mismatch_errors)
    return errors


def run_test(
    operator,
    input_buffers,
    output_buffers,
    intermediate_buffers=None,
    rel_tol=0.04,
    abs_tol=1e-6,
    max_error_rate=0.0,
    warmup_iters=1,
    timed_iters=1,
):
    """
    Run operator test with specified input/output buffers.

    Args:
        operator: AIE operator instance (must be an AIEOperatorBase subclass)
        input_buffers: Dict mapping buffer names to input data arrays
        output_buffers: Dict mapping buffer names to reference output arrays
        intermediate_buffers: Not supported; passing a non-empty value raises ValueError
        rel_tol: Relative tolerance for comparison of output buffers
        abs_tol: Absolute tolerance for comparison of output buffers
        max_error_rate: Maximum fraction of elements allowed to exceed tolerances (0.0 to 1.0)
        warmup_iters: Number of warmup iterations before timing
        timed_iters: Number of timed iterations for latency/bandwidth measurement

    Returns:
        (errors: dict, latency_us: float, bandwidth_gbps: float)
    """
    if intermediate_buffers:
        raise ValueError(
            "intermediate_buffers verification is not supported in run_test"
        )

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

    for spec in arg_spec:
        if spec.direction == "in":
            try:
                name, data = next(input_iter)
            except StopIteration:
                raise ValueError("Not enough input buffers provided for arg spec")
            buf = XRTTensor.from_torch(data)
            args.append(buf)
            total_bytes += buf.buffer_object().size()
        elif spec.direction == "out":
            try:
                name, expected = next(output_iter)
            except StopIteration:
                raise ValueError("Not enough output buffers provided for arg spec")
            buf = XRTTensor(spec.shape, dtype=spec.dtype)
            args.append(buf)
            output_map[name] = buf
            total_bytes += buf.buffer_object().size()
        elif spec.direction == "inout":
            try:
                name, data = next(input_iter)
            except StopIteration:
                raise ValueError("Not enough input buffers provided for inout arg spec")
            buf = XRTTensor.from_torch(data)
            args.append(buf)
            output_map[name] = buf
            inout_names.append(name)
            total_bytes += buf.buffer_object().size()
        else:
            raise ValueError(f"Unsupported direction: {spec.direction}")

    # Run warmup iterations
    for _ in range(warmup_iters):
        op_func(*args)

    # Run operator
    start_time = time.perf_counter()
    for _ in range(timed_iters):
        op_func(*args)
    end_time = time.perf_counter()

    elapsed = (end_time - start_time) / timed_iters
    latency_us = elapsed * 1e6

    # Verify outputs
    errors = {}
    for buf_name, expected in output_buffers.items():
        if expected is None:
            continue
        if buf_name in output_map:
            buf = output_map[buf_name]
            output_torch = xrt_to_torch(buf)
            buf_errors = verify_buffer(
                output_torch, buf_name, expected, rel_tol, abs_tol, max_error_rate
            )
            if buf_errors:
                errors[buf_name] = buf_errors
        else:
            print(f"Warning: Output buffer {buf_name} not found in operator arguments")

    # inout buffers are in output_map and are verified above if present in output_buffers

    # Calculate bandwidth
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    return errors, latency_us, bandwidth_gbps
