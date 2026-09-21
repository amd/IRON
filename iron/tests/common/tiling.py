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
    Access,
    Block,
    contiguous,
    encode,
    granule_elements,
    repeated,
    split,
    split_run,
    whole,
)
from iron.common.utils import DMA_BD_MAX_WRAP


def test_granularity_per_dtype():
    assert granule_elements(bfloat16) == 2
    assert granule_elements(np.int32) == 1
    assert granule_elements(np.int8) == 4


def test_channeled_unary_taps_are_reproduced():
    # channeled_unary_design.py: chunk = size // cols // channels, fifo idx = i*ch + j,
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
    # gemv/op.py coalesced_tap: sizes [1, nb, run_hi, run_lo], strides [0, M*K, run_lo, 1]
    # with (run_hi, run_lo) = split_run((M//cols)*K).
    M, K, cols, nb = 256, 128, 8, 100
    run = (M // cols) * K  # 4096 > 1023: needs the hi/lo split
    blocks = split((nb, M, K), cols, axis=1)
    assert blocks[1].repeats == ((nb, M * K),)
    (acc,) = encode(blocks[1], nb * M * K, bfloat16)
    hi, lo = split_run(run, gran=2)
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
    # lo <= 1023, lo a multiple of the granule, lo maximal.
    assert split_run(512, gran=2) == (1, 512)
    assert (
        split_run(4096, gran=2) == (4, 1024)
        or split_run(4096, gran=2)[0] * split_run(4096, gran=2)[1] == 4096
    )
    hi, lo = split_run(4096, gran=2)
    assert hi * lo == 4096 and lo <= DMA_BD_MAX_WRAP and lo % 2 == 0
    # gemv case (1026, 64, 1, 1, 2, 2): an odd-looking run that needs an even split
    hi, lo = split_run(1026 * 64, gran=2)
    assert hi * lo == 1026 * 64 and lo % 2 == 0 and hi <= DMA_BD_MAX_WRAP


def test_repeated_rejects_what_the_descriptor_cannot_hold():
    assert repeated(1 << 24, 0, 1024, [(2000, 1024)], bfloat16) is None  # count > wrap
    assert repeated(4096, 1, 16, [(2, 32)], bfloat16) is None  # odd bf16 offset
    assert repeated(4096, 0, 16, [(2, 33)], bfloat16) is None  # odd bf16 stride
    assert (
        repeated(4096, 0, 16, [(2, 4), (2, 8), (2, 16)], bfloat16) is None
    )  # 3 outer dims
    assert repeated(4096, 0, 16, [(2, 32)], np.int32) is not None


def test_repeated_zero_stride_rereads_the_run():
    # repeat/op.py's input: the whole buffer re-read `repeat` times.
    acc = repeated(64, 0, 64, [(3, 0)], bfloat16)
    assert acc.sizes == (1, 1, 3, 64) and acc.strides == (0, 0, 0, 1)


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
    # mha's K_tiles case: a (2048, 64) tile is [1,1,2048,64]/[0,0,64,1]; 2048 > 1023.
    from iron.common.tiling import legalize

    (acc,) = legalize(2048 * 64, 0, [1, 1, 2048, 64], [0, 0, 64, 1], bfloat16)
    # 1024 is past the 10-bit wrap, so the largest legal factor is 512.
    assert acc.sizes == (1, 4, 512, 64) and acc.strides == (0, 512 * 64, 64, 1)
    assert acc.count == 2048 * 64


def test_legalize_unrolls_when_no_slot_is_free():
    from iron.common.tiling import legalize

    accs = legalize(1 << 21, 0, [2, 2048, 2, 64], [1 << 20, 128, 64, 1], bfloat16)
    assert len(accs) == 2
    assert [a.offset for a in accs] == [0, 1 << 20]
    assert all(a.sizes == (4, 512, 2, 64) for a in accs)


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
