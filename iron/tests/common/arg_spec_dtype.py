#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``AIERuntimeArgSpec.dtype`` must describe the operator it belongs to.

``get_arg_spec()`` is the contract every buffer-sizing caller trusts:
``iron.common.test_utils.run_test`` sizes an "out" ``XRTTensor`` off
``spec.dtype`` (``XRTTensor(spec.shape, dtype=spec.dtype)``), and
``OperatorSequence.calculate_buffer_layout`` sizes every dispatch buffer off
``np.dtype(spec.dtype).itemsize``. An operator that declares its own dtype but
never passes it into ``AIERuntimeArgSpec`` silently hands both callers the
dataclass default (bfloat16) instead, so a non-default-dtype user under- or
over-allocates. These tests pin the arg spec to the operator's real dtype
directly, and pin the two callers' byte arithmetic against it -- entirely
device-free, no ``XRTTensor``/``pyxrt`` construction anywhere below.
"""

import numpy as np
from ml_dtypes import bfloat16
from aie.iron import str_to_dtype

from iron.common.sequence import OperatorSequence
from iron.operators.strided_copy.op import StridedCopy
from iron.operators.repeat.op import Repeat
from iron.operators.gemm.op import GEMM


def _bytes_for(shape, dtype):
    return int(np.prod(shape) * np.dtype(dtype).itemsize)


def test_strided_copy_arg_spec_reports_operator_dtype():
    op = StridedCopy(
        input_sizes=[1024],
        input_strides=[1],
        input_offset=0,
        output_sizes=[1024],
        output_strides=[1],
        output_offset=0,
        input_buffer_size=1024,
        output_buffer_size=1024,
        dtype=np.float32,
    )
    in_spec, out_spec = op.get_arg_spec()
    assert in_spec.dtype == np.float32
    assert out_spec.dtype == np.float32


def test_repeat_arg_spec_reports_operator_dtype():
    op = Repeat(rows=8, cols=64, repeat=4, dtype=np.int32)
    in_spec, out_spec = op.get_arg_spec()
    assert in_spec.dtype == np.int32
    assert out_spec.dtype == np.int32


def test_gemm_arg_spec_reports_operator_dtype():
    op = GEMM(
        M=256,
        K=64,
        N=64,
        tile_m=64,
        tile_k=64,
        tile_n=64,
        num_aie_columns=1,
        dtype_in="i8",
        dtype_out="i32",
    )
    a_spec, b_spec, c_spec = op.get_arg_spec()
    assert a_spec.dtype == str_to_dtype("i8")
    assert b_spec.dtype == str_to_dtype("i8")
    assert c_spec.dtype == str_to_dtype("i32")


def test_default_dtype_arg_spec_is_unaffected():
    """The bf16-default path every shipped caller uses today must not move."""
    op = StridedCopy(
        input_sizes=[64],
        input_strides=[1],
        input_offset=0,
        output_sizes=[64],
        output_strides=[1],
        output_offset=0,
        input_buffer_size=64,
        output_buffer_size=64,
    )
    in_spec, out_spec = op.get_arg_spec()
    assert in_spec.dtype == bfloat16
    assert out_spec.dtype == bfloat16


def test_sequence_calculate_buffer_layout_sizes_off_the_real_dtype():
    """``sequence.py``'s consumer (``sequence.py:399-401``): the byte length it
    computes for a dispatch buffer must match what the design actually DMAs,
    not a bf16-assumed width."""
    op = GEMM(
        M=256,
        K=64,
        N=64,
        tile_m=64,
        tile_k=64,
        tile_n=64,
        num_aie_columns=1,
        dtype_in="i8",
        dtype_out="i32",
    )
    seq = OperatorSequence(
        "argspec_probe",
        runlist=[(op, "A", "B", "C")],
        input_args=["A", "B"],
        output_args=["C"],
    )
    _, buffer_sizes, _ = seq.calculate_buffer_layout()
    _, output_buffer_size, _ = buffer_sizes
    assert output_buffer_size == _bytes_for((256, 64), str_to_dtype("i32"))


def test_test_utils_xrttensor_sizing_formula_matches_the_real_dtype():
    """``test_utils.py``'s consumer (``test_utils.py:188``,
    ``XRTTensor(spec.shape, dtype=spec.dtype)``): replicate the exact byte
    formula ``XRTTensor.__init__`` uses (``np.prod(shape) * itemsize(dtype)``)
    off the arg spec alone, so the assertion holds without opening a device."""
    op = Repeat(rows=8, cols=64, repeat=4, dtype=np.int32)
    _, out_spec = op.get_arg_spec()
    declared_bytes = _bytes_for(out_spec.shape, out_spec.dtype)
    actual_bytes = _bytes_for(out_spec.shape, op.dtype)
    assert declared_bytes == actual_bytes
