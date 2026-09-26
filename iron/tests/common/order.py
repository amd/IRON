# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A buffer's declared order is what its sequence issues.

``Operator.order()`` is the one statement of which elements each slot of a
stream carries; the build checks that the sequence -- derived, an operator's
``design(rt)``, or an overlay's own -- issues exactly it. No NPU: every test
generates real MLIR in process.
"""

import numpy as np
import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.declare import Order, operator
from iron.common.declare.order import derived
from iron.common.design import generator_for
from iron.common.tiling import Access
from iron.operators.flm.dequant.op import DequantBFP
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.operators.flm.gemm.shipped import Shipped
from iron.operators.gemm.op import GEMM
from iron.operators.gemv.op import GEMV
from iron.operators.mem_copy import MemCopy
from iron.operators.mha.op import MHA
from iron.operators.repeat import Repeat
from iron.operators.strided_copy import StridedCopy
from iron.operators.transpose import Transpose


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    dev = from_name("npu2", n_cols=8)
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


def _kv_slot():
    return dict(
        input_sizes=[8, 64],
        input_strides=[64, 1],
        input_offset=0,
        input_buffer_size=8 * 64,
        output_sizes=[1, 8, 64],
        output_strides=[0, 128 * 64, 1],
        output_offset=5 * 64,
        output_buffer_size=8 * 128 * 64,
        num_aie_channels=2,
    )


# One construction per operator that writes its own sequence, at shapes that
# reach its irregular paths: GEMV's coalesced batches, GEMM's split C drain,
# a copy's padded remainder, flm.GEMM's split C and its shipped overlay.
OVERRIDES = [
    lambda: GEMV(M=256, K=128, num_aie_columns=2, tile_size_output=64, num_batches=4),
    lambda: GEMM(M=1024, K=2560, N=10240, tile_m=64, tile_k=64, tile_n=64),
    lambda: MHA(num_heads=8, seq_len=128, d=64, num_KV_heads=2, num_of_pipelines=1),
    lambda: Transpose(M=128, N=128, num_aie_columns=2, num_channels=1, num_batches=2),
    lambda: StridedCopy(**_kv_slot()),
    lambda: MemCopy(size=1000, num_cores=4, num_channels=1, tile_size=256),
    lambda: Repeat(rows=16, cols=64, repeat=4),
    lambda: DequantBFP(K=1024, N=512),
    lambda: FLMGEMM(M=512, K=1024, N=10240),
    lambda: FLMGEMM(Shipped(), M=256, K=512, N=1280),
]


@pytest.mark.parametrize(
    "make",
    OVERRIDES,
    ids=[
        "GEMV",
        "GEMM",
        "MHA",
        "Transpose",
        "StridedCopy",
        "MemCopy",
        "Repeat",
        "DequantBFP",
        "flm.GEMM",
        "flm.GEMM-Shipped",
    ],
)
def test_each_sequence_issues_its_declared_order(make, npu2):
    op = make().tuned(npu2)
    generator_for(op)()  # raises if a slot departs from op.order()
    for buf in op.buffers:
        order = op.order(buf)
        assert order.stream is buf.stream(op.ov)


def test_repeat_is_its_order_and_no_sequence():
    # Its override was the derived shape all along: one group, the fill,
    # then the waited drain.
    assert not Repeat.has_design_override()


def test_a_sequence_that_departs_from_its_order_fails_the_build(npu2):
    @operator
    class OneColumnB(GEMV):
        def design(self, rt):
            # B to column 0 only, where the order (replicate) says every column.
            ov = self.ov
            with rt.group():
                for tap in self.order(self.B)[0]:
                    rt.fill(ov.b[0], (self.B, tap))
                a, c = self.order(self.A), self.order(self.C)
                for col in range(ov.num_aie_columns):
                    rt.fill(ov.a[col], (self.A, a[col][0]))
                    rt.drain(ov.c[col], (self.C, c[col][0]), wait=True)

    op = OneColumnB(M=256, K=128, num_aie_columns=2, tile_size_output=64).tuned(npu2)
    with pytest.raises(ValueError, match=r"OneColumnB\.B: slot 1 of stream 'b'"):
        generator_for(op)()


def test_an_order_agrees_with_its_streams_replicate_flag(npu2):
    gemv = GEMV(M=256, K=128, num_aie_columns=2, tile_size_output=64).tuned(npu2)
    n = gemv.B.elements
    halves = (
        (Access(n, 0, (1, 1, 1, n // 2), (0, 0, 0, 1)),),
        (Access(n, n // 2, (1, 1, 1, n // 2), (0, 0, 0, 1)),),
    )
    with pytest.raises(ValueError, match="'b' is declared replicate=True"):
        Order(gemv.ov.b, halves)

    copy = MemCopy(size=512, num_cores=2, num_channels=1, tile_size=256).tuned(npu2)
    whole = (Access(512, 0, (1, 1, 1, 512), (0, 0, 0, 1)),)
    with pytest.raises(ValueError, match="'s' is not declared replicate=True"):
        Order(copy.ov.s, (whole, whole))


def test_gemv_encodes_the_derived_split_its_own_way(npu2):
    # GEMV keeps its own descriptor factoring so its instruction stream is
    # unchanged; the elements each column receives are still the library's
    # row-block split, which is what a fusion pass compares.
    op = GEMV(
        M=256, K=128, num_aie_columns=2, tile_size_output=64, num_batches=4
    ).tuned(npu2)
    for buf in (op.A, op.C):
        mine, library = op.order(buf), derived(buf, buf.stream(op.ov))
        for slot in range(2):
            assert np.array_equal(mine.indices(slot), library.indices(slot))
    b = op.order(op.B)
    assert b.replicated
    for slot in range(2):
        assert np.array_equal(b.indices(slot), np.arange(op.B.elements))
