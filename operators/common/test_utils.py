# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import numpy as np
from ml_dtypes import bfloat16
from .aie_base import AIEOperatorBase
from .utils import torch_to_numpy


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


def run_test(operator, input_buffers, output_buffers, intermediate_buffers=None, rel_tol=0.04, abs_tol=1e-6):
    """
    Run operator test with specified input/output/intermediate buffers.
    
    Args:
        operator: AIE operator instance with registered buffers
        input_buffers: Dict mapping buffer names to input data arrays
        output_buffers: Dict mapping buffer names to reference output arrays
        intermediate_buffers: Optional dict mapping buffer names to reference arrays for validation
        rel_tol: Relative tolerance for comparison
        abs_tol: Absolute tolerance for comparison
    
    Returns:
        (passed: bool, latency_us: float, bandwidth_gbps: float)
    """
    if intermediate_buffers is None:
        intermediate_buffers = {}
    

    
    AIEOperatorBase.compile_all_operators()
    AIEOperatorBase.prepare_runtime()
    
    # Get all registered buffers from operator
    registered_buffers = set(operator.buffers)
    
    # Verify all specified buffers are registered
    all_specified = set(input_buffers) | set(output_buffers) | set(intermediate_buffers)
    unregistered = all_specified - registered_buffers
    if unregistered:
        raise ValueError(f"Buffers not registered in operator: {unregistered}")
    
    # Determine which buffers are not input/output (need to be zeroed)
    known_buffers = set(input_buffers) | set(output_buffers) | set(intermediate_buffers)
    buffers_to_zero = registered_buffers - known_buffers
    
    input_bytes = 0
    output_bytes = 0
    
    # Write input buffers
    for buf_name, data in input_buffers.items():
        # Convert torch tensors to numpy if needed
        data_np = torch_to_numpy(data)
        operator.write_buffer(buf_name, data_np)
        input_bytes += data_np.nbytes
    
    # Zero output buffers
    for buf_name in output_buffers:
        buf_size = operator.buffers[buf_name]
        operator.write_buffer(buf_name, np.zeros(buf_size, dtype=np.uint8))
    
    # Zero intermediate buffers (always zeroed before running)
    for buf_name in intermediate_buffers:
        buf_size = operator.buffers[buf_name]
        operator.write_buffer(buf_name, np.zeros(buf_size, dtype=np.uint8))
    
    # Zero any other registered buffers
    for buf_name in buffers_to_zero:
        buf_size = operator.buffers[buf_name]
        operator.write_buffer(buf_name, np.zeros(buf_size, dtype=np.uint8))
   
    # Run operator
    start = time.perf_counter()
    operator.run_runlist()
    end = time.perf_counter()
    
    latency_us = (end - start) * 1e6
    
    # Read and verify output buffers
    errors = 0
    
    for buf_name, expected in output_buffers.items():
        # Convert torch tensors to numpy if needed
        expected_np = torch_to_numpy(expected)
        
        buf_size = operator.buffers[buf_name] // 2
        output = operator.read_buffer(buf_name, (buf_size, ))
        output_bytes += output.nbytes
        
        # Compare only the relevant portion (handle potential padding)
        compare_len = min(len(output), len(expected_np))
        for i in range(compare_len):
            if not nearly_equal(float(output[i]), float(expected_np[i]), rel_tol, abs_tol):
                errors += 1
                if errors <= 10:
                    print(f"Mismatch in {buf_name}[{i}]: expected {float(expected_np[i]):.6f}, got {float(output[i]):.6f}")
    
    # Verify intermediate buffers if provided
    for buf_name, expected in intermediate_buffers.items():
        # Convert torch tensors to numpy if needed
        expected_np = torch_to_numpy(expected)
        
        buf_size = operator.buffers[buf_name]
        output = operator.read_buffer(buf_name, buf_size)
        
        compare_len = min(len(output), len(expected_np))
        for i in range(compare_len):
            if not nearly_equal(float(output[i]), float(expected_np[i]), rel_tol, abs_tol):
                errors += 1
                if errors <= 10:
                    print(f"Mismatch in intermediate {buf_name}[{i}]: expected {float(expected_np[i]):.6f}, got {float(output[i]):.6f}")
    
    # Calculate bandwidth
    total_bytes = input_bytes + output_bytes
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9
    
    passed = (errors == 0)
    
    return passed, latency_us, bandwidth_gbps
