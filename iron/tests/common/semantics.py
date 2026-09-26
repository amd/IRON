# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an overlay computes: declared where only its kernel knows, derived
from its stream declarations everywhere else. Device-free."""

import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.declare import (
    Composite,
    Contraction,
    Local,
    Movement,
    Overlay,
    Undeclared,
)
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.flm.dequant.op import DequantBFP
from iron.operators.gemv.op import GEMV
from iron.operators.layer_norm import LayerNorm
from iron.operators.mem_copy import MemCopy
from iron.operators.mha.op import MHA
from iron.operators.relu import ReLU
from iron.operators.rms_norm import WeightedRMSNorm
from iron.operators.rope.op import RoPE
from iron.operators.softmax import Softmax
from iron.operators.strided_copy import StridedCopy


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    dev = from_name("npu2", n_cols=8)
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


def _derived(op) -> bool:
    return type(op.ov).semantics is Overlay.semantics


@pytest.mark.parametrize(
    "op, block",
    [
        (Softmax(rows=16, cols=256), 256),
        (RoPE(rows=32, cols=64), 64),
        (LayerNorm(size=4096, tile_size=1024, num_aie_columns=1), 1024),
        (WeightedRMSNorm(rows=4, tile_size=2048), 2048),
    ],
)
def test_a_row_op_derives_its_row_from_its_streams(op, block, npu2):
    # No class declares these: every stream carries one object shape over one
    # slot count (a weight row replicated at that shape included), so a core
    # maps object k to object k and the object is the block.
    tuned = op.tuned(npu2)
    assert _derived(tuned)
    assert tuned.ov.semantics() == Local(block)


def test_what_only_the_kernel_knows_is_declared(npu2):
    assert ReLU(size=1024, tile_size=256, num_aie_columns=1).tuned(
        npu2
    ).ov.semantics() == Local(1)
    assert ElementwiseAdd(size=1024, num_aie_columns=1).tuned(
        npu2
    ).ov.semantics() == Local(1)
    gemv = GEMV(M=256, K=128, num_aie_columns=2, tile_size_output=64).tuned(npu2)
    assert gemv.ov.semantics() == Contraction(final_at_release=True)
    mha = MHA(num_heads=8, seq_len=128, d=64, num_KV_heads=2).tuned(npu2)
    assert mha.ov.semantics() == Composite()
    copy = dict(size=1024, num_cores=2, num_channels=1, tile_size=512)
    assert MemCopy(**copy).tuned(npu2).ov.semantics() == Movement(has_cores=True)
    bypass = MemCopy(**copy, bypass=True).tuned(npu2)
    assert bypass.ov.semantics() == Movement(has_cores=False)
    strided = StridedCopy(
        input_sizes=[1024],
        input_strides=[1],
        input_offset=0,
        input_buffer_size=1024,
        output_sizes=[1024],
        output_strides=[1],
        output_offset=0,
        output_buffer_size=1024,
    ).tuned(npu2)
    assert strided.ov.semantics() == Movement(has_cores=False)


def test_streams_that_do_not_align_are_undeclared_not_guessed(npu2):
    # q4nx bytes in, packed bfp16 half-tiles out: nothing in the streams says
    # which output depends on which input, so the answer says why.
    sem = DequantBFP(K=1024, N=512).tuned(npu2).ov.semantics()
    assert isinstance(sem, Undeclared)
    assert "carry different objects" in sem.reason


def test_layer_norm_row_is_what_it_computes_not_a_tunable():
    # The row it normalises was a tunable defaulting to 256: an operator built
    # without it normalised 256-element pieces of whatever row it was given.
    with pytest.raises(TypeError, match="tile_size"):
        LayerNorm(size=4096)
    with pytest.raises(ValueError, match="normalised in pieces"):
        LayerNorm(size=16384, tile_size=16384)
