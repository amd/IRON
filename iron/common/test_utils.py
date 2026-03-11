# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import numpy as np
from ml_dtypes import bfloat16
from .utils import torch_to_numpy
import logging
from .base import MLIROperator, CompositeOperator, AIEBuffer


def nearly_equal(
    a, b, rel_tol=128 * np.finfo(np.float32).eps, abs_tol=np.finfo(np.float32).tiny
):
    """
    Compare two floating point numbers for approximate equality.

    Adapted from Stack Overflow, License CC BY-SA 4.0
    Original author: P-Gn
    Source: https://stackoverflow.com/a/32334103
    """
    assert np.finfo(np.float32).eps <= rel_tol
    assert rel_tol < 1.0

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
    expected_np = torch_to_numpy(reference).reshape((-1,))
    output = output.reshape((-1,))

    if len(output) < len(expected_np):
        # Allow larger buffers - binning may have allocated more space than needed
        print(
            f"Buffer size mismatch for {buf_name}: expected {len(expected_np)}, got {len(output)}"
        )
        errors.extend(i for i in range(abs(len(output) - len(expected_np))))
    compare_len = min(len(output), len(expected_np))
    for i in range(compare_len):
        if not nearly_equal(float(output[i]), float(expected_np[i]), rel_tol, abs_tol):
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch in {buf_name}[{i}]: expected {float(expected_np[i]):.6f}, got {float(output[i]):.6f}"
                )

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
    Run operator test with specified input/output/intermediate buffers.

    Args:
        operator: AIE operator instance
        input_buffers: Dict mapping buffer names to input data arrays
        output_buffers: Dict mapping buffer names to reference output arrays
        intermediate_buffers: Optional dict mapping buffer names to reference arrays for validation
        rel_tol: Relative tolerance for comparison of output and intermediate buffers
        abs_tol: Absolute tolerance for comparison of output and intermediate buffers
        max_error_rate: Maximum fraction of elements allowed to exceed tolerances (0.0 to 1.0)

    Returns:
        (errors: list, latency_us: float, bandwidth_gbps: float)
    """
    if intermediate_buffers is None:
        intermediate_buffers = {}

    # Build operator and prepare runtime
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    if not isinstance(operator, (MLIROperator, CompositeOperator)):
        raise ValueError("run_test only supports MLIROperator or CompositeOperator")

    operator.compile()
    op_func = operator.get_callable()

    args = []
    arg_spec = operator.get_arg_spec()

    input_iter = iter(input_buffers.items())
    output_iter = iter(output_buffers.items())
    output_map = {}

    total_bytes = 0

    for spec in arg_spec:
        if spec.direction == "in":
            try:
                name, data = next(input_iter)
            except StopIteration:
                raise ValueError("Not enough input buffers provided for arg spec")
            data_np = torch_to_numpy(data)
            buf = AIEBuffer.from_np(data_np)
            args.append(buf)
            total_bytes += buf.bo.size()
        elif spec.direction == "out":
            try:
                name, expected = next(output_iter)
            except StopIteration:
                raise ValueError("Not enough output buffers provided for arg spec")
            buf = AIEBuffer(shape=spec.shape, dtype=spec.dtype)
            args.append(buf)
            output_map[name] = buf
            total_bytes += buf.bo.size()
        else:
            # Handle other directions if needed, or raise error
            raise ValueError(f"Unsupported direction: {spec.direction}")

    # Run warmup iterations
    for _ in range(warmup_iters):
        op_func(*args)

    # Run operator
    start_time = time.time()
    for _ in range(timed_iters):
        op_func(*args)
    end_time = time.time()

    elapsed = (end_time - start_time) / timed_iters
    latency_us = elapsed * 1e6

    # Verify outputs
    errors = {}
    for buf_name, expected in output_buffers.items():
        if expected is None:
            continue
        if buf_name in output_map:
            buf = output_map[buf_name]
            output_np = buf.view_as_np()
            buf_errors = verify_buffer(
                output_np, buf_name, expected, rel_tol, abs_tol, max_error_rate
            )
            if buf_errors:
                errors[buf_name] = buf_errors
        else:
            print(f"Warning: Output buffer {buf_name} not found in operator arguments")

    # Intermediate buffers are not supported in this generic run_test
    # unless we expose them somehow. For now, ignore or warn.
    if intermediate_buffers:
        print("Warning: intermediate_buffers verification is not supported in run_test")

    # Calculate bandwidth
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    return errors, latency_us, bandwidth_gbps
