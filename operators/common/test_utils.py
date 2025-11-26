# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import numpy as np
from ml_dtypes import bfloat16
from .aie_base import AIEOperatorBase
from .utils import torch_to_numpy
import logging


def nearly_equal(a, b, rel_tol=128 * np.finfo(np.float32).eps, abs_tol=np.finfo(np.float32).tiny):
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


def verify_buffer(operator, buf_name, reference, rel_tol=0.04, abs_tol=1e-6):
    errors = 0
    expected_np = torch_to_numpy(reference)
    buf_size = operator.buffers[buf_name] // 2
    output = operator.read_buffer(buf_name, (buf_size, ))
    if len(output) != len(expected_np):
        print(f"Buffer size mismatch for {buf_name}: expected {len(expected_np)}, got {len(output)}")
        errors += abs(len(output) - len(expected_np))
    compare_len = min(len(output), len(expected_np))
    for i in range(compare_len):
        if not nearly_equal(float(output[i]), float(expected_np[i]), rel_tol, abs_tol):
            errors += 1
            if errors <= 10:
                print(f"Mismatch in {buf_name}[{i}]: expected {float(expected_np[i]):.6f}, got {float(output[i]):.6f}")
    return errors


def run_test(operator, input_buffers, output_buffers, intermediate_buffers=None, rel_tol=0.04, abs_tol=1e-6, warmup_iters=1, timed_iters=1):
    """
    Run operator test with specified input/output/intermediate buffers.
    
    Args:
        operator: AIE operator instance with registered buffers
        input_buffers: Dict mapping buffer names to input data arrays
        output_buffers: Dict mapping buffer names to reference output arrays
        intermediate_buffers: Optional dict mapping buffer names to reference arrays for validation
        rel_tol: Relative tolerance for comparison of output and intermediate buffers
        abs_tol: Absolute tolerance for comparison of output and intermediate buffers
    
    Returns:
        (passed: bool, latency_us: float, bandwidth_gbps: float)
    """
    if intermediate_buffers is None:
        intermediate_buffers = {}
    
    # Build operator and prepare runtime
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    AIEOperatorBase.compile_all_operators()
    AIEOperatorBase.prepare_runtime()
    
    # Write input buffers and zero outputs
    for buf_name, data in input_buffers.items():
        data_np = torch_to_numpy(data)
        operator.write_buffer(buf_name, data_np)
    for buf_name in output_buffers:
        buf_size = operator.buffers[buf_name]
        operator.write_buffer(buf_name, np.zeros(buf_size, dtype=np.uint8))
   
    # Run operator
    for _ in range(warmup_iters):
        operator.run_runlist()  # warmup run to configure
    elapsed_total = 0
    for _ in range(timed_iters):
        elapsed_total += operator.run_runlist()
    elapsed = elapsed_total / timed_iters
    latency_us = elapsed * 1e6

    # Verify outputs
    errors = 0
    for buf_name, expected in output_buffers.items():
        errors += verify_buffer(operator, buf_name, expected, rel_tol, abs_tol)
    
    for buf_name, expected in intermediate_buffers.items():
        errors += verify_buffer(operator, buf_name, expected, rel_tol, abs_tol)
    
    # Calculate bandwidth
    input_bytes = sum(operator.buffers[buf_name] for buf_name in input_buffers)
    output_bytes = sum(operator.buffers[buf_name] for buf_name in output_buffers)
    total_bytes = input_bytes + output_bytes
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9
    
    passed = (errors == 0)
    
    return passed, latency_us, bandwidth_gbps
