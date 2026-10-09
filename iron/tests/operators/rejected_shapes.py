#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Shapes an operator must refuse rather than build.

Each of these lowers, builds and then hangs the device or computes the wrong
answer, with no diagnostic worth reading -- so the operator rejects it at
construction. Host-only: what is checked is the refusal, not a dispatch.
"""

import functools

import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.iron.device import from_name
from ml_dtypes import bfloat16

from iron.common import Link, Unresolvable
from iron.operators.copy import Copy, Gather
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.limbs import Limbs
from iron.operators.magnitude import Magnitude
from iron.operators.merge import Merge
from iron.operators.mha import MHA
from iron.operators.repeat import Repeat
from iron.operators.resample.op import PatchPositions
from iron.operators.rms_norm import RMSNorm
from iron.operators.sample import Sample
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.operators.transpose import Transpose


@pytest.mark.parametrize(
    "cols,why",
    [
        (513, "odd: every divisor is odd, so no chunk is a whole 32-bit word"),
        (1031, "prime > 1023: the only divisors are 1 and cols, neither legal"),
        (2062, "2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count"),
    ],
)
def test_repeat_cols_without_a_legal_split_is_rejected(cols, why):
    """A split has to satisfy the innermost dim AND the dim holding the chunk
    count. Both land on a 10-bit wrap field, and the innermost is denominated
    in 32-bit words, so bounding the chunk length alone lets through taps the
    BD verifier then rejects with a much less legible error.

    Refused when resolved for a device, against its shim's descriptor
    limits, not when it is built.
    """
    with pytest.raises(Unresolvable, match="Cannot split cols"):
        Repeat(rows=8, cols=cols, repeat=4).resolved(from_name("npu2"))


def test_transfer_size_not_dividing_the_per_channel_share_is_rejected():
    """A BD shorter than the ObjectFifo object hangs the device.

    4 channels over 1024 elements is a 256-element BD; a 512-element object
    leaves the memtile's S2MM waiting for a second half that no channel
    sends, and the drain's dma_await_task returns ERT_CMD_STATE_TIMEOUT with
    no diagnostic.
    """
    with pytest.raises(ValueError, match="must divide the per-channel transfer"):
        Copy(
            input_buffer_size=1024, num_channels=4, tile_size=512
        )  # every tunable given


def test_transfer_size_not_dividing_a_bounded_row_is_rejected():
    """A bounded copy moves any whole number of rows, so its object divides
    one row: a prompt's 513 rows of (8, 64) keys into a cache are 256.5
    objects of 1024 elements, and the last half-object hangs the device.
    Left to itself the copy takes one row's 512.
    """
    rows, G, D = 2048, 8, 64
    copy = functools.partial(
        Copy,
        src=TensorAccessPattern((rows, G, D), 0, [G, rows, D], [D, G * D, 1]),
        dst=TensorAccessPattern.full((G, rows, D))[:, :rows],
        src_bound=1,
        dst_bound=1,
        input_buffer_size=rows * G * D,
    )
    with pytest.raises(ValueError, match="one row of the bounded axis"):
        copy(tile_size=1024)  # every tunable given
    assert copy().resolved(from_name("npu2")).tile_size == G * D


def test_channels_not_dividing_the_shared_run_are_rejected():
    """The channels split the run both sides' innermost axes hold a whole
    number of: 6-wide rows into a flat output share runs of 6, which 4
    channels cannot split alike.
    """
    with pytest.raises(ValueError, match="common run of 6"):
        Copy(
            src=TensorAccessPattern.full((8, 6)),
            dst=TensorAccessPattern.full((48,)),
            input_buffer_size=48,
            num_channels=4,
            tile_size=12,
        )  # every tunable given


@pytest.mark.parametrize(
    "name,cols,feeds",
    [("npu1", 4, 3), ("npu2", 8, 5), ("npu2", 8, 0)],
)
def test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused(
    name, cols, feeds
):
    """Feed ``k`` streams from shim column ``2k`` into column ``2k + 1``."""
    gather = Gather(rows=512, table_rows=4096, row=512, feeds=feeds)
    with pytest.raises(Unresolvable, match="shim columns"):
        gather.resolved(from_name(name, n_cols=cols))


def test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused():
    """A feed streams whole pairs of batches, so 33 rows (five batches of
    eight, three pairs) keep three feeds busy and leave a fourth idle.
    """
    with pytest.raises(ValueError, match="leave 1 idle"):
        Gather(rows=33, table_rows=4096, row=512, feeds=4)
    gather = Gather(rows=33, table_rows=4096, row=512)
    assert gather.resolved(from_name("npu2", n_cols=8)).feeds == 3


# Shapes whose M*N is divisible by every factor while one per-dimension quotient is not
# a whole number of tiles. Without the guard these reach the transfer as sizes
# [8, 0, 256, 32]. compatible() runs at resolved(), so that is where the refusal lands.
@pytest.mark.parametrize(
    "M,N,aie_columns,channels,m,n,bad",
    [
        (2048, 128, 8, 1, 256, 32, "num_aie_columns"),
        (256, 2048, 1, 2, 256, 32, "num_channels"),
    ],
)
def test_transpose_dimension_that_does_not_tile_is_refused_by_name(
    M, N, aie_columns, channels, m, n, bad
):
    with pytest.raises(ValueError, match=bad):  # every tunable given: at construction
        Transpose(
            M=M, N=N, num_aie_columns=aie_columns, num_channels=channels, m=m, n=n, s=8
        )


@pytest.mark.parametrize("aie_columns", [1, 2, 4])
def test_transpose_tiling_that_fits_is_still_accepted(aie_columns):
    """The guard must not narrow the accepted set: 1/2/4 columns all tile N=128 by n=32."""
    Transpose(
        M=2048, N=128, num_aie_columns=aie_columns, num_channels=1, m=256, n=32, s=8
    ).resolved(from_name("npu2", n_cols=8))


def test_a_tile_past_what_one_core_holds_is_refused_not_split():
    """A row an elementwise kernel cannot hold is an error at resolution; the
    library never halves it, since a norm's reference is the whole row.
    """
    dev = from_name("npu2", n_cols=8)
    with pytest.raises(Unresolvable, match="tile_size=16384 exceeds the 8192"):
        RMSNorm(rows=1, tile_size=16384).resolved(dev)
    assert RMSNorm(rows=2, tile_size=8192).resolved(dev).tile_size == 8192


def test_the_default_column_count_is_the_most_that_leave_whole_tiles():
    """A tunable-free operator resolves on either device to the widest count
    its shape divides over, rather than the whole shim budget and a refusal.
    """
    npu2, npu1 = from_name("npu2", n_cols=8), from_name("npu1", n_cols=4)
    assert GEMM(M=256, K=64, N=256).resolved(npu2).num_aie_columns == 4
    assert GEMM(M=256, K=64, N=512).resolved(npu1).num_aie_columns == 4
    assert Transpose(M=64, N=64).resolved(npu2).num_aie_columns == 1
    assert Transpose(M=64, N=256).resolved(npu2).num_aie_columns == 4
    # Nothing fits: one column, and compatible() names the rule.
    with pytest.raises(ValueError, match=r"rows \(16\) must be a multiple of the 3"):
        Softmax(rows=16, cols=16, num_channels=3).resolved(npu2)


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(B_q=64, B_kv=128), "B_q"),
        (dict(kv_len=1000), "kv_len"),
        (dict(kv_len=512), "kv_len"),
    ],
    ids=[
        "q_and_kv_blocks_differ",
        "kv_len_not_whole_blocks",
        "kv_len_short_of_queries",
    ],
)
def test_mha_whose_blocks_do_not_line_up_is_refused(kwargs, why):
    """mha.cc skips a KV block past a Q block by comparing their indices, so
    the two block sizes must match; and the queries are the keys' last rows,
    whole blocks of them, so the cache must hold them.
    """
    with pytest.raises(ValueError, match=why):
        MHA(num_heads=2, seq_len=1024, num_pipelines=8, **kwargs).resolved(
            from_name("npu2", n_cols=8)
        )


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(d=96), "multiple of 64"),
        (dict(causal=False, window=0), "window must be positive"),
        (dict(causal=False, window=500), "whole 64-row blocks"),
        (dict(d=256, causal=False, window=520), "whole 16-row blocks"),
        (dict(scale=-1.0), "scale"),
        (dict(B_q=128, B_kv=128), "divide 64"),
    ],
    ids=[
        "head_not_whole_64",
        "empty_window",
        "window_not_whole_blocks",
        "window_not_whole_small_blocks",
        "negative_scale",
        "block_past_the_padding",
    ],
)
def test_mha_band_and_head_that_do_not_tile_are_refused(kwargs, why):
    """mha.cc keeps or skips whole key blocks for a whole query block, so a
    window is whole blocks; d=256 resolves to 16-row blocks, the largest
    whose P*V core fits L1.
    """
    with pytest.raises(ValueError, match=why):
        MHA(num_heads=2, seq_len=1024, num_pipelines=8, **kwargs).resolved(
            from_name("npu2", n_cols=8)
        )


def test_mha_whose_head_fits_no_block_is_refused():
    """At d=768 even half the head's float32 O fills a P*V core at 16 rows."""
    with pytest.raises(Unresolvable, match="no block"):
        MHA(num_heads=2, seq_len=1024, d=768, num_pipelines=8).resolved(
            from_name("npu2", n_cols=8)
        )


def test_mha_blocks_follow_the_head_size():
    npu2 = from_name("npu2", n_cols=8)
    for d, block, pv_cores in ((64, 64, 1), (128, 32, 1), (256, 16, 1), (512, 16, 2)):
        op = MHA(num_heads=2, seq_len=1024, d=d, num_pipelines=8).resolved(npu2)
        assert (op.B_q, op.B_kv, op.pv_cores) == (block, block, pv_cores)
        assert op.pv_width * pv_cores == d


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(seq_len=1024, d=512, pv_cores=3), "one core or two"),
        (dict(seq_len=1536, d=512, num_pipelines=6), "at most 4 pipelines"),
        (
            dict(seq_len=1, kv_len=512, num_KV_heads=1, num_pipelines=2, pv_cores=2),
            "P\\*V takes one core",
        ),
    ],
    ids=["three_ways", "six_pipelines_to_a_join", "one_query_packed"],
)
def test_mha_whose_pv_split_does_not_route_is_refused(kwargs, why):
    """Split, P*V's halves sit on the rows either side of the softmax core,
    and each memtile then forwards its pipeline's scores and P as well as
    its share of the O joins; one query packed has a shim's two channels
    for its K and V.
    """
    with pytest.raises(ValueError, match=why):
        MHA(**{"num_heads": 8, "num_pipelines": 8, **kwargs}).resolved(
            from_name("npu2", n_cols=8)
        )


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (
            dict(num_heads=8, num_KV_heads=2, num_pipelines=2, causal=False, window=64),
            "window",
        ),
        (dict(num_heads=24, num_KV_heads=8, num_pipelines=4), "packs"),
        (dict(num_heads=32, num_KV_heads=8, num_pipelines=8), "at most 4"),
        (dict(num_heads=24, num_KV_heads=6, num_pipelines=4), "dividing"),
    ],
    ids=[
        "windowed",
        "group_not_dividing_a_block",
        "more_than_four_pipelines",
        "uneven_groups",
    ],
)
def test_mha_of_one_query_that_does_not_pack_is_refused(kwargs, why):
    """One query packs each KV group's heads into a block's rows, past every
    key block, where a window would mask them; and each pipeline reads its own
    groups' K and V through its own column's memtile.
    """
    with pytest.raises(ValueError, match=why):
        MHA(seq_len=1, kv_len=512, **kwargs).resolved(from_name("npu2", n_cols=8))


def test_sample_with_more_cores_than_a_memtile_joins_is_refused():
    """Each select core's summary is one input stream of the memtile they
    join in, which has six: eight cores fit NPU2's shim and fail to place.
    """
    dev = from_name("npu2", n_cols=8)
    with pytest.raises(Unresolvable, match="join in one memtile"):
        Sample(vocab=4096, cores=8).resolved(dev)
    assert Sample(vocab=4096, cores=4).resolved(dev).cores == 4


def test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused():
    """A streamed core unrolls its rows, each with its own state: past 48
    its program overflows the core's memory.
    """
    dev = from_name("npu2", n_cols=8)
    with pytest.raises(ValueError, match="at most 48 rows"):
        Softmax(rows=1024, cols=8192, num_aie_columns=1).resolved(dev)
    assert Softmax(rows=256, cols=8192, num_aie_columns=8).resolved(dev).streamed


@pytest.mark.parametrize(
    "device,emulate",
    [(("npu1", 4), None), (("npu2", 8), None), (("npu2", 8), False)],
)
def test_flm_gemm_reads_b_as_stored_in_bf16(device, emulate):
    op = FLMGEMM(
        M=256, K=512, N=256, b_col_maj=True, emulate_bf16_mmul_with_bfp16=emulate
    ).resolved(from_name(device[0], n_cols=device[1]))
    assert op.B.shape == (256, 512) and op.b_dtype is bfloat16
    assert not op.bfp16_b
    with pytest.raises(ValueError, match="reads B as stored"):
        op.pack_B(None)


def test_flm_gemm_bfp16_macs_are_aie2p_only():
    with pytest.raises(ValueError, match="bfp16 macs are AIE2P's"):
        FLMGEMM(M=256, K=512, N=256, emulate_bf16_mmul_with_bfp16=True).resolved(
            from_name("npu1", n_cols=4)
        )


def test_a_finish_input_past_the_cores_input_channels_is_refused():
    """A sum's cores read two streams, neither declared for a finish step's
    own input to ride; past them the design fails to place. A one-stream
    core takes it, and so does a matvec's, on its matrix.
    """
    dev = from_name("npu2", n_cols=8)
    finish = (Link(ElementwiseMul(size=2048), 1),)
    with pytest.raises(Unresolvable, match="input channels"):
        ElementwiseAdd(size=2048, num_aie_columns=4, finish=finish).resolved(dev)
    SiLU(size=2048, num_aie_columns=4, finish=finish).resolved(dev)
    fed = GEMV(M=2048, K=2048, finish=finish).resolved(dev)
    assert [b.streamed for b in fed.finish_inputs] == [False]


def test_a_step_that_needs_the_order_of_a_gemm_block_is_refused():
    """GEMM's cores hold their block of C in the matmul kernel's own layout:
    a step independent of that order finishes it; a norm over rows, or a
    product whose other input streams in row order, does not.
    """
    dev = from_name("npu2", n_cols=8)
    kwargs = dict(M=2048, K=2048, N=2048, b_col_maj=True)
    with pytest.raises(ValueError, match="reduces over rows"):
        GEMM(**kwargs, finish=(Link(RMSNorm(rows=1024, tile_size=4096)),)).resolved(dev)
    with pytest.raises(Unresolvable, match="order of their own"):
        GEMM(**kwargs, finish=(Link(ElementwiseMul(size=2048 * 2048), 1),)).resolved(
            dev
        )
    GEMM(**kwargs, finish=(Link(SiLU(size=2048 * 2048)),)).resolved(dev)


@pytest.mark.parametrize(
    "make",
    [
        lambda: Limbs(rows=64, line=176),
        lambda: Magnitude(rows=64, width=608),
    ],
    ids=["limbs", "magnitude"],
)
def test_a_line_of_part_of_a_vector_is_refused(make):
    """Limbs and Magnitude load and store whole 32-lane vectors, so a line
    (or each half of a complex row) of part of one would read past it.
    """
    with pytest.raises(ValueError, match="32-element vectors"):
        make()


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(rows=2560, out_height=64, out_width=912), "whole 48-pixel windows"),
        (dict(rows=1280, out_height=672, out_width=912), "at most 1280 patches"),
        (dict(rows=1000, out_height=48, out_width=48), "256-row blocks"),
    ],
    ids=["not_whole_windows", "more_patches_than_rows", "rows_not_whole_blocks"],
)
def test_patch_positions_that_do_not_tile_are_refused(kwargs, why):
    """The tower pools whole windows of patches, and the core writes whole
    blocks of rows: a short block would leave the last rows unwritten.
    """
    with pytest.raises(ValueError, match=why):
        PatchPositions(**kwargs).resolved(from_name("npu2", n_cols=8))


def test_merge_of_part_of_a_block_is_refused():
    """The core reads whole blocks of ids: a short one would leave the last
    rows unwritten.
    """
    with pytest.raises(ValueError, match="64-row blocks"):
        Merge(rows=100, audio_token=0, image_token=1, audio_at=0, vision_at=0).resolved(
            from_name("npu2", n_cols=8)
        )
