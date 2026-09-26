# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The derived sequence's access patterns, checked against what designs hand-write today.

Each case reproduces a tap from an existing design (channeled unary, binary
elementwise, GEMV) so the derivation is pinned to behaviour the hardware has
already run, not to a fresh reading of the descriptor format.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.tiling import (
    DMA_BD_MAX_WRAP,
    Access,
    Block,
    contiguous,
    encode,
    granule_elements,
    legalize,
    repeated,
    split,
    split_run,
    whole,
)


def test_granularity_per_dtype():
    assert granule_elements(bfloat16) == 2
    assert granule_elements(np.int32) == 1
    assert granule_elements(np.int8) == 4


def test_channeled_unary_taps_are_reproduced():
    # The channeled unary rule: chunk = size // cols // channels, fifo idx = i*ch + j,
    # tap = ((1,size), chunk*i*ch + chunk*j, [1,1,1,chunk], [0,0,0,1]).
    size, cols, ch = 4096, 4, 2
    chunk = size // cols // ch
    blocks = split((size,), cols * ch, axis=0)
    for i in range(cols):
        for j in range(ch):
            idx = i * ch + j
            (acc,) = encode(blocks[idx], size, bfloat16)
            assert acc == Access(
                size, chunk * i * ch + chunk * j, (1, 1, 1, chunk), (0, 0, 0, 1)
            )


def test_binary_elementwise_taps_are_reproduced():
    size, cols = 8192, 8
    chunk = size // cols
    for i, block in enumerate(split((size,), cols, axis=0)):
        (acc,) = encode(block, size, bfloat16)
        assert acc.offset == chunk * i and acc.sizes == (1, 1, 1, chunk)


def test_whole_buffer_is_one_linear_transfer():
    (acc,) = encode(whole((3, 64)), 192, bfloat16)
    assert acc == contiguous(192, 0, 192)


def test_gemv_unbatched_taps_are_reproduced():
    # gemv/op.py A_taps for num_batches == 1: offset col*(M//cols)*K, sizes [1,1,1,(M//cols)*K].
    M, K, cols = 2048, 8192, 8
    blocks = split((M, K), cols, axis=0)
    for col, block in enumerate(blocks):
        (acc,) = encode(block, M * K, bfloat16)
        assert acc.offset == col * (M // cols) * K
        assert acc.sizes == (1, 1, 1, (M // cols) * K) and acc.strides == (0, 0, 0, 1)
    # C: offset col*(M//cols), run M//cols
    for col, block in enumerate(split((M,), cols, axis=0)):
        (acc,) = encode(block, M, bfloat16)
        assert (acc.offset, acc.sizes[3]) == (col * (M // cols), M // cols)


def test_gemv_batched_coalesces_into_one_iterated_descriptor():
    # GEMV's batched fill: sizes [1, nb, run_hi, run_lo], strides [0, M*K, run_lo, 1]
    # with (run_hi, run_lo) = split_run((M//cols)*K).
    M, K, cols, nb = 256, 128, 8, 100
    run = (M // cols) * K  # 4096 > 1023: needs the hi/lo split
    blocks = split((nb, M, K), cols, axis=1)
    assert blocks[1].repeats == ((nb, M * K),)
    (acc,) = encode(blocks[1], nb * M * K, bfloat16)
    hi_lo = split_run(run, gran=2)
    assert hi_lo is not None
    hi, lo = hi_lo
    assert acc.sizes == (1, nb, hi, lo) and acc.strides == (0, M * K, lo, 1)
    assert acc.offset == 1 * run
    assert acc.count == nb * run


def test_gemv_batched_falls_back_to_per_batch_when_stride_too_wide():
    # gemv test case (1024, 1024, 1, 1, 64, 2): batch stride M*K = 2**20 exceeds the
    # 20-bit granule field -> today's design unrolls one tap per batch.
    M, K, nb = 1024, 1024, 2
    (block,) = split((nb, M, K), 1, axis=1)
    accs = encode(block, nb * M * K, bfloat16)
    assert len(accs) == nb
    assert [a.offset for a in accs] == [0, M * K]
    assert all(a.sizes == (1, 1, 1, M * K) for a in accs)


def test_split_run_matches_gemv_rules():
    # lo is at most 1023 granules (2046 bf16 elements), a multiple of the
    # granule, and maximal; hi is at most 1023.
    assert split_run(512, gran=2) == (1, 512)
    assert split_run(4096, gran=2) == (4, 1024)  # 2048 would exceed 2046
    hi_lo = split_run(4096, gran=2)
    assert hi_lo is not None
    hi, lo = hi_lo
    assert hi * lo == 4096 and lo <= DMA_BD_MAX_WRAP * 2 and lo % 2 == 0
    # gemv case (1026, 64, 1, 1, 2, 2): an odd-looking run that needs an even split
    hi_lo = split_run(1026 * 64, gran=2)
    assert hi_lo is not None
    hi, lo = hi_lo
    assert hi * lo == 1026 * 64 and lo % 2 == 0 and hi <= DMA_BD_MAX_WRAP


def test_repeated_rejects_what_the_descriptor_cannot_hold():
    assert (
        repeated(1 << 24, 0, 1024, [(2000, 1024)], bfloat16) is not None
    )  # d2 is free
    # two repeats plus a split run fill all four slots, so iter > 64 cannot fit
    assert repeated(1 << 24, 0, 4096, [(65, 1 << 16), (2, 4096)], bfloat16) is None
    assert repeated(4096, 1, 16, [(2, 32)], bfloat16) is None  # odd bf16 offset
    assert repeated(4096, 0, 16, [(2, 33)], bfloat16) is None  # odd bf16 stride
    assert (
        repeated(4096, 0, 16, [(2, 4), (2, 8), (2, 16)], bfloat16) is None
    )  # 3 outer dims
    assert repeated(4096, 0, 16, [(2, 32)], np.int32) is not None


def test_repeated_zero_stride_rereads_the_run_from_the_iteration_slot():
    # repeat/op.py's input: the whole buffer re-read `repeat` times. Only the
    # iteration slot may carry a zero stride, and it holds at most 64.
    acc = repeated(64, 0, 64, [(3, 0)], bfloat16)
    assert acc is not None
    assert acc.sizes == (3, 1, 1, 64) and acc.strides == (0, 0, 0, 1)
    assert repeated(64, 0, 64, [(65, 0)], bfloat16) is None  # past the iteration wrap
    # a strided repeat goes in d2 instead, where there is no wrap limit
    acc = repeated(64 * 100, 0, 64, [(100, 64)], bfloat16)
    assert acc is not None
    assert acc.sizes == (1, 100, 1, 64) and acc.strides == (0, 64, 0, 1)


def test_legalize_keeps_a_leading_zero_stride_in_the_iteration_slot():
    # mha's K and V: one head's rows re-read once per (head, Q block) of its
    # group. The re-read stays outermost whatever the rest needs: a contiguous
    # head splits into d1/d0 under it, a strided one (heads interleaved per
    # token) factors its rows into d2/d1.
    (acc,) = legalize(8 * 2048 * 64, 0, (16, 2048 * 64), (0, 1), bfloat16)
    assert acc.sizes == (16, 1, 128, 1024) and acc.strides == (0, 0, 1024, 1)
    (acc,) = legalize(2048 * 8 * 64, 64, (16, 2048, 64), (0, 512, 1), bfloat16)
    assert acc.sizes == (16, 4, 512, 64) and acc.strides == (0, 512 * 512, 512, 1)
    # Past the iteration wrap the re-read factors (5 x 13, both re-reads) and
    # the outer factor unrolls: five descriptors of thirteen re-reads each.
    accs = legalize(8 * 2048 * 64, 0, (65, 2048 * 64), (0, 1), bfloat16)
    assert len(accs) == 5 and all(a.sizes == (13, 1, 128, 1024) for a in accs)
    assert all(a.offset == 0 for a in accs)


def test_legalize_merges_nesting_dimensions_only_when_that_helps():
    # Five dimensions, the outer two nesting contiguously: as given they do
    # not fit and would unroll; merged they are four and fit.
    (acc,) = legalize(
        1 << 22, 0, [2, 20, 8, 2, 64], [20 * 40000, 40000, 4096, 128, 1], bfloat16
    )
    assert acc.sizes == (40, 8, 2, 64) and acc.strides == (40000, 4096, 128, 1)
    # gemm's column-major B: as given it fits one descriptor; merged, its
    # middle dimensions grow past a wrap and factor onto a stride past the
    # field, unrolling into hundreds. The pattern that fits keeps its shape.
    (acc,) = legalize(
        8192 * 2048, 0, [16, 32, 64, 64], [512, 524288, 8192, 1], bfloat16
    )
    assert acc.sizes == (16, 32, 64, 64)


def test_split_validates_divisibility_and_axis():
    with pytest.raises(ValueError, match="cannot split 100 rows"):
        split((100, 8), 8, axis=0)
    with pytest.raises(ValueError, match="axis 2 out of range"):
        split((100, 8), 4, axis=2)


def test_block_unrolls_leading_axes_outermost_first():
    b = Block(slot=0, offset=5, run=2, repeats=((2, 100), (3, 10)))
    assert list(b.unrolled) == [(5, 2), (15, 2), (25, 2), (105, 2), (115, 2), (125, 2)]


def test_access_span_is_bounds_checked():
    with pytest.raises(ValueError, match="runs past"):
        contiguous(10, 8, 4)
    with pytest.raises(ValueError, match="spans"):
        repeated(100, 0, 16, [(8, 16)], bfloat16)


def test_legalize_factors_an_oversize_outer_dim_when_a_slot_is_free():
    from iron.common.tiling import legalize

    # mha's K_tiles case: a (2048, 64) tile of a 64-wide buffer is contiguous,
    # so it is one linear transfer.
    (acc,) = legalize(2048 * 64, 0, [1, 1, 2048, 64], [0, 0, 64, 1], bfloat16)
    assert acc == contiguous(2048 * 64, 0, 2048 * 64)
    # A non-contiguous tile with an oversize d1 is factored into the free d2;
    # 1024 exceeds d1's 1023, so the factor is 512.
    (acc,) = legalize(2048 * 128, 0, [1, 1, 2048, 64], [0, 0, 128, 1], bfloat16)
    assert acc.sizes == (1, 4, 512, 64) and acc.strides == (0, 512 * 128, 128, 1)
    assert acc.count == 2048 * 64


def test_legalize_unrolls_when_no_slot_is_free():
    from iron.common.tiling import legalize

    # All four slots used and the iteration count past 64: unroll it. (The
    # outer stride is not the next dimension's extent, or the two would
    # merge into one slot and the rest fit.)
    accs = legalize(1 << 22, 0, [100, 8, 2, 64], [40000, 4096, 128, 1], bfloat16)
    assert len(accs) == 100
    assert [a.offset for a in accs][:3] == [0, 40000, 80000]
    assert all(a.sizes == (1, 8, 2, 64) for a in accs)


def test_legalize_drops_unit_dims_and_keeps_legal_patterns():
    from iron.common.tiling import legalize

    (acc,) = legalize(4096, 8, [1, 1, 4, 32], [0, 0, 64, 1], bfloat16)
    assert acc == Access(4096, 8, (1, 1, 4, 32), (0, 0, 64, 1))


def test_legalize_rejects_granularity_violations():
    from iron.common.tiling import legalize

    with pytest.raises(ValueError, match="granule"):
        legalize(4096, 1, [1, 1, 4, 32], [0, 0, 64, 1], bfloat16)
    with pytest.raises(ValueError, match="granule"):
        legalize(4096, 0, [1, 1, 4, 32], [0, 0, 63, 1], bfloat16)


def test_view_of_whole_rows_is_one_linear_run():
    from iron.common.tiling import view

    # GEMV's sequence(rt): self.A[:, col*rows:(col+1)*rows, :] over (nb, M, K)
    nb, M, K, cols = 4, 256, 128, 8
    rows = M // cols
    off, sizes, strides = view(
        (nb, M, K), (slice(None), slice(rows, 2 * rows), slice(None))
    )
    assert off == rows * K
    assert sizes == [nb, rows * K] and strides == [M * K, 1]
    # unbatched: the leading axis is gone and the run is linear
    off, sizes, strides = view((M, K), (slice(rows, 2 * rows),))
    assert (off, sizes, strides) == (rows * K, [rows * K], [1])


def test_view_with_an_integer_index_drops_the_axis():
    from iron.common.tiling import view

    off, sizes, strides = view((3, 64, 8), (1, slice(16, 32)))
    assert off == 64 * 8 + 16 * 8 and sizes == [16 * 8] and strides == [1]


def test_view_rejects_steps_and_empty_slices():
    from iron.common.tiling import view

    with pytest.raises(ValueError, match="unit steps"):
        view((64,), (slice(0, 64, 2),))
    with pytest.raises(ValueError, match="empty"):
        view((64,), (slice(10, 10),))
    with pytest.raises(IndexError):
        view((64,), (0, 0))


def test_view_then_legalize_round_trips_a_batched_block():
    from iron.common.tiling import legalize, view

    nb, M, K = 100, 256, 128
    off, sizes, strides = view((nb, M, K), (slice(None), slice(0, 32), slice(None)))
    (acc,) = legalize(nb * M * K, off, sizes, strides, bfloat16)
    hi_lo = split_run(32 * K, gran=2)
    assert hi_lo is not None
    hi, lo = hi_lo
    assert acc.sizes == (1, nb, hi, lo) and acc.strides == (0, M * K, lo, 1)
