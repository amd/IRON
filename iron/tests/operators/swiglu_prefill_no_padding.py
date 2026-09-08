#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SwiGLUPrefill does not pad: it raises for a seq_len its inner GEMM cannot
tile, and the *_aligned attributes just echo the input dims back.

The __init__ docstring used to claim "All operators (GEMM, SiLU,
ElementwiseMul) apply their own padding", but none of the three pad --
each raises ValueError from __post_init__ if its shape doesn't already
divide evenly (see iron/common/operator_bases.py and
iron/operators/gemm/op.py). So SwiGLUPrefill(seq_len=...) simply forwards
that raise for any seq_len that is not already a multiple of
tile_m * 4 (256 with GEMM's defaults).
"""

import aie.utils as aie_utils
import pytest
from aie.iron.device import NPU2

from iron.operators.swiglu_prefill.op import SwiGLUPrefill


def _construct(seq_len, embedding_dim=2048, hidden_dim=2048):
    aie_utils.set_current_device(NPU2())
    return SwiGLUPrefill(
        seq_len=seq_len, embedding_dim=embedding_dim, hidden_dim=hidden_dim
    )


def test_non_aligned_seq_len_raises_instead_of_being_padded():
    with pytest.raises(ValueError, match=r"M \(300\) must be a multiple of 256"):
        _construct(seq_len=300)


def test_aligned_seq_len_constructs_and_aligned_attrs_equal_the_input():
    op = _construct(seq_len=512)
    assert op.seq_len_aligned == 512 == op.seq_len
    assert op.embedding_dim_aligned == 2048 == op.embedding_dim
    assert op.hidden_dim_aligned == 2048 == op.hidden_dim
