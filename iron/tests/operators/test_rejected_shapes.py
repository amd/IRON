# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Shapes an operator must refuse rather than build.

Each of these lowers, builds and then hangs the device or computes the wrong
answer, with no diagnostic worth reading -- so the operator rejects it at
construction. Host-only: what is checked is the refusal, not a dispatch.
"""

import contextlib
import dataclasses
import functools

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.iron.kernels import FLM_GEMMA4_E2B_DECODE, flm_gemma4
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.common import Precision, Unresolvable
from iron.operators.clamp import Clamp
from iron.operators.copy import Copy, Gather
from iron.operators.depthwise_conv1d import DepthwiseConv1d
from iron.operators.emit import Emit
from iron.operators.flm.dequant.op import DequantBFP
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.operators.flm.layer.op import DecodeLayer
from iron.operators.flm.lm_head.op import LMHead
from iron.operators.flm.prefill_attn.op import (
    PrefillAttention,
    PrefillSlidingAttention,
)
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs
from iron.operators.magnitude import Magnitude
from iron.operators.merge import Merge
from iron.operators.mha import MHA
from iron.operators.resample.op import PatchPositions
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.sample import Sample
from iron.operators.selective_scan import SelectiveScan
from iron.operators.softmax import Softmax

pytestmark = pytest.mark.usefixtures("npu2")


@pytest.mark.parametrize("block", [0, -16, 1, 17, 32, 96])
@pytest.mark.parametrize("columns", [None, 1])
def test_selective_scan_rejects_invalid_blocks(block, columns):
    with pytest.raises(ValueError, match="block"):
        SelectiveScan(
            rows=5, heads=2, head_dim=16, state_size=16, columns=columns, block=block
        ).resolved()


@pytest.mark.parametrize("rows,block", [(5, 16), (5, 80), (8, 32), (8, 128)])
def test_selective_scan_accepts_blocks_dividing_rows(rows, block):
    op = SelectiveScan(
        rows=rows, heads=2, head_dim=16, state_size=16, columns=1, block=block
    )
    assert op.resolved().block == block


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


def test_transfer_size_not_dividing_a_bounded_row_is_rejected(npu2):
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
    assert copy().resolved(npu2).tile_size == G * D


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
    "name,feeds",
    [("npu1", 3), ("npu2", 5), ("npu2", 0)],
)
def test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused(
    name, feeds, request
):
    """Feed ``k`` streams from shim column ``2k`` into column ``2k + 1``."""
    gather = Gather(rows=512, table_rows=4096, row=512, feeds=feeds)
    with pytest.raises(Unresolvable, match="shim columns"):
        gather.resolved(request.getfixturevalue(name))


def test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused(npu2):
    """A feed streams whole pairs of batches, so 33 rows (five batches of
    eight, three pairs) keep three feeds busy and leave a fourth idle.
    """
    with pytest.raises(ValueError, match="leave 1 idle"):
        Gather(rows=33, table_rows=4096, row=512, feeds=4)
    gather = Gather(rows=33, table_rows=4096, row=512)
    assert gather.resolved(npu2).feeds == 3


class _BoundedGather(iron.Graph):
    def __init__(self, table):
        self.table = iron.weight(table)

    def body(self, ids, *, n: Scratchpad[np.int32]):
        return Copy.step(self.table[ids[:n]])


def test_a_bounded_gather_of_rows_not_whole_16_byte_units_is_refused(npu2):
    """A bounded feed drains a per-call length in 16-byte units, so a row of
    six bf16 (12 bytes) cannot be bounded, though it gathers whole.
    """
    table = np.zeros((64, 6), dtype=bfloat16)
    recording = _BoundedGather(table).record(ids=((16,), np.int32))
    (gather,) = [s.op for s in recording.steps if isinstance(s.op, Gather)]
    with pytest.raises(ValueError, match="16-byte units"):
        gather.resolved(npu2)
    Gather(rows=16, table_rows=64, row=6).resolved(npu2)


def test_a_tile_past_what_one_core_holds_is_refused_not_split(npu2):
    """A row an elementwise kernel cannot hold is an error at resolution; the
    library never halves it, since a norm's reference is the whole row.
    """
    with pytest.raises(Unresolvable, match="tile_size=16384 exceeds the 8192"):
        RMSNorm(rows=1, tile_size=16384).resolved(npu2)
    assert RMSNorm(rows=2, tile_size=8192).resolved(npu2).tile_size == 8192


def test_softmax_with_no_column_count_that_tiles_is_refused(npu2):
    """A tunable-free operator resolves to the widest column count its shape
    divides over; where even one column does not fit, compatible() names the
    rule rather than falling back to the whole shim budget.
    """
    with pytest.raises(ValueError, match=r"rows \(16\)"):
        Softmax(rows=16, cols=16, num_channels=3).resolved(npu2)


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(kv_len=1000), "kv_len"),
        (dict(kv_len=512), "kv_len"),
    ],
    ids=[
        "kv_len_not_whole_blocks",
        "kv_len_short_of_queries",
    ],
)
def test_mha_whose_blocks_do_not_line_up_is_refused(kwargs, why, npu2):
    """The queries are the keys' last rows, whole blocks of them, so the
    cache must hold them.
    """
    with pytest.raises(ValueError, match=why):
        MHA(num_heads=2, seq_len=1024, num_pipelines=8, **kwargs).resolved(npu2)


def test_mha_whose_pipelines_do_not_fill_the_rows_is_refused(npu2):
    """Q is split in rounds of 64 rows a pipeline, and 128 rows are a
    quarter of a round of eight.
    """
    with pytest.raises(ValueError, match="whole rounds"):
        MHA(num_heads=2, seq_len=100, num_pipelines=8).resolved(npu2)


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(d=96), "multiple of 64"),
        (dict(causal=False, window=0), r"window \(0\) must be positive"),
        (dict(scale=-1.0), "scale"),
        (dict(B_q=128), "divide 64"),
    ],
    ids=[
        "head_not_whole_64",
        "empty_window",
        "negative_scale",
        "block_past_the_padding",
    ],
)
def test_mha_band_and_head_that_do_not_tile_are_refused(kwargs, why, npu2):
    """A head is whole 64-column tiles, a window at least one key, the scale
    not negative, and a query block within the 64-row padding.
    """
    with pytest.raises(ValueError, match=why):
        MHA(num_heads=2, seq_len=1024, num_pipelines=8, **kwargs).resolved(npu2)


def test_mha_whose_head_fits_no_block_is_refused(npu2):
    """At d=768 even half the head's float32 O fills a P*V core at 16 rows."""
    with pytest.raises(Unresolvable, match="no block"):
        MHA(num_heads=2, seq_len=1024, d=768, num_pipelines=8).resolved(npu2)


def test_mha_one_query_packed_takes_the_narrowest_block_and_64_keys(npu2):
    """Every row of a packed block is computed, so one query takes the
    narrowest block that holds its group, over 64-key blocks: mha.cc's
    vectorized softmax reads 64-key rows. (num_heads=32, num_KV_heads=8 is
    the llama_1b shape test_catalog.py already dispatches; group_of_32,
    kv_heads=1, is not, so that is the one worth a construction-time check.)
    """
    op = MHA(
        num_heads=32,
        num_KV_heads=1,
        d=64,
        seq_len=1,
        kv_len=32768,
        num_pipelines=1,
        heads_interleaved=True,
    ).resolved(npu2)
    assert (op.B_q, op.B_kv) == (32, 64)


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
def test_mha_whose_pv_split_does_not_route_is_refused(kwargs, why, npu2):
    """Split, P*V's halves sit on the rows either side of the softmax core,
    and each memtile then forwards its pipeline's scores and P as well as
    its share of the O joins; one query packed has a shim's two channels
    for its K and V.
    """
    with pytest.raises(ValueError, match=why):
        MHA(**{"num_heads": 8, "num_pipelines": 8, **kwargs}).resolved(npu2)


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(num_heads=24, num_KV_heads=1, num_pipelines=1, B_q=16), "hold"),
        (dict(num_heads=32, num_KV_heads=8, num_pipelines=8), "at most 4"),
        (dict(num_heads=24, num_KV_heads=6, num_pipelines=4), "dividing"),
    ],
    ids=[
        "group_past_a_block",
        "more_than_four_pipelines",
        "uneven_groups",
    ],
)
def test_mha_of_one_query_that_does_not_pack_is_refused(kwargs, why, npu2):
    """One query packs each KV group's heads into a block's rows, and each
    pipeline reads its own groups' K and V through its own column's memtile.
    """
    with pytest.raises(ValueError, match=why):
        MHA(seq_len=1, kv_len=512, **kwargs).resolved(npu2)


def test_sample_with_more_cores_than_a_memtile_joins_is_refused(npu2):
    """Each select core's summary is one input stream of the memtile they
    join in, which has six: eight cores fit NPU2's shim and fail to place.
    """
    with pytest.raises(Unresolvable, match="join in one memtile"):
        Sample(vocab=4096, cores=8).resolved(npu2)
    assert Sample(vocab=4096, cores=4).resolved(npu2).cores == 4


def test_sample_over_an_odd_vocab_is_refused():
    """The logits move in 4-byte words, so a slice ends on an even index."""
    with pytest.raises(ValueError, match="must be even"):
        Sample(vocab=51865)


def test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused(npu2):
    """A streamed core unrolls its rows, each with its own state: past 48
    its program overflows the core's memory.
    """
    with pytest.raises(ValueError, match="at most 48 rows"):
        Softmax(rows=1024, cols=8192, num_aie_columns=1).resolved(npu2)
    assert Softmax(rows=256, cols=8192, num_aie_columns=8).resolved(npu2).streamed


def test_a_float32_softmax_under_a_per_call_bound_is_refused(npu2):
    """The float32 kernel takes its row length at build time, so a bound
    row would come out as the softmax of every element, stale ones too.
    """

    class Attend(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Softmax.step(x[:, :n], input_dtype=np.float32)

    (step,) = Attend().record(x=((32, 1024), np.float32)).steps
    with pytest.raises(ValueError, match="takes no per-call bound"):
        step.op.resolved()


def test_flm_gemm_reads_b_as_stored_in_bf16(npu2):
    """Packing is for a row-major B; ``b_col_maj`` reads B as the array
    already holds it, so packing it again is refused rather than silently
    reordered wrong. (The read-as-stored path itself is the device check in
    flm/gemm/test.py's test_gemm_b_col_maj.)
    """
    op = ProjectionGEMM(
        M=256, K=512, N=256, b_col_maj=True, precision=Precision.MEDIUM
    ).resolved(npu2)
    with pytest.raises(ValueError, match="reads B as stored"):
        op.pack_B(None)


@pytest.mark.parametrize(
    "make",
    [
        lambda: Limbs(rows=64, line=176),
        lambda: Magnitude(rows=64, width=608),
    ],
    ids=["limbs", "magnitude"],
)
def test_a_line_of_part_of_a_vector_is_refused(make, npu2):
    """Limbs and Magnitude load and store whole 32-lane vectors, so a line
    (or each half of a complex row) of part of one would read past it: their
    kernels' factories refuse it.
    """
    with pytest.raises(ValueError, match="32-element vector step"):
        make().resolved().tolerance()


@pytest.mark.parametrize(
    "kwargs,why",
    [
        (dict(rows=2560, out_height=64, out_width=912), "whole 48-pixel windows"),
        (dict(rows=1280, out_height=672, out_width=912), "at most 1280 patches"),
        (dict(rows=1000, out_height=48, out_width=48), "256-row blocks"),
    ],
    ids=["not_whole_windows", "more_patches_than_rows", "rows_not_whole_blocks"],
)
def test_patch_positions_that_do_not_tile_are_refused(kwargs, why, npu2):
    """The tower pools whole windows of patches, and the core writes whole
    blocks of rows: a short block would leave the last rows unwritten.
    """
    with pytest.raises(ValueError, match=why):
        PatchPositions(**kwargs).resolved(npu2)


def test_merge_of_part_of_a_block_is_refused(npu2):
    """The core reads whole blocks of ids: a short one would leave the last
    rows unwritten.
    """
    with pytest.raises(ValueError, match="64-row blocks"):
        Merge(rows=100, placeholders=((0, 0), (1, 0))).resolved(npu2)


@pytest.mark.parametrize("placeholders", [(), ((7, 0), (7, 64))])
def test_merge_of_no_or_repeated_placeholders_is_refused(placeholders):
    """A token is one placeholder's: a repeat would merge it twice."""
    with pytest.raises(ValueError, match="distinct tokens"):
        Merge(rows=128, placeholders=placeholders)


@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_gemm_on_columns_that_do_not_divide_its_rows_is_refused(device, request):
    """Each of a GEMM's first shims carries A to as many rows of cores as
    the others: three columns leave a fourth row without its A. Left open,
    the columns resolve to a count that divides the rows or covers them:
    two on npu1, six on npu2.
    """
    dev = request.getfixturevalue(device)
    shape = dict(M=256, K=128, N=384, b_col_maj=True, precision=Precision.MEDIUM)
    with pytest.raises(ValueError, match="do not divide the 4 rows"):
        GEMM(**shape, num_aie_columns=3).resolved(dev)
    assert GEMM(**shape).resolved(dev).num_aie_columns == {"npu1": 2, "npu2": 6}[device]


@pytest.mark.parametrize(
    "tile_m, tile_k, tile_n, precision, expectation",
    [
        (
            8,
            64,
            64,
            Precision.MEDIUM,
            pytest.raises(ValueError, match="tile_m .* multiple of 16"),
        ),
        (8, 64, 64, Precision.HIGH, contextlib.nullcontext()),
        (
            64,
            64,
            8,
            Precision.HIGH,
            pytest.raises(ValueError, match="tile_n .* multiple of 16"),
        ),
        # tile_k=4 still divides K=512 evenly (the outer K % tile_k check),
        # so this exercises the s-divisibility check rather than that one.
        (
            64,
            4,
            64,
            Precision.MEDIUM,
            pytest.raises(ValueError, match="tile_k .* multiple of 8"),
        ),
    ],
    ids=[
        "m8_emulated",
        "m8",
        "n8",
        "k4_emulated",
    ],
)
def test_gemm_tile_the_kernel_cannot_build_is_rejected(
    tile_m, tile_k, tile_n, precision, expectation
):
    """GEMM must reject tile sizes the kernel cannot build.

    aie_kernels/linalg/mm_aie2p.h's matmul_vectorized_*x*x*_bf16_* wrappers
    static_assert m % (2*r) == 0, k % s == 0 and n % (2*t) == 0 for the (r,
    s, t) triple MEDIUM's bfp16 macs select (r=t=8, the default; r=4, t=8
    otherwise). A tile size that meets a
    lower bound without dividing evenly would construct without error and
    then fail that static_assert at kernel compile time, from a file this
    class never names.
    """
    with expectation:
        GEMM(
            M=512,
            K=512,
            N=512,
            tile_m=tile_m,
            tile_k=tile_k,
            tile_n=tile_n,
            precision=precision,
        )


@pytest.mark.parametrize(
    "device, precision, M, tile_m",
    [
        ("npu2", Precision.MEDIUM, 2048, 64),
        ("npu2", Precision.MEDIUM, 128, 32),
        ("npu2", Precision.MEDIUM, 64, 16),
        ("npu2", Precision.HIGH, 32, 8),
        ("npu1", Precision.HIGH, 64, 16),
    ],
)
def test_an_open_tile_m_is_the_widest_that_splits_m(
    device, precision, M, tile_m, request
):
    """Four rows of cores each take tile_m of M's rows, so a short M takes a
    short tile rather than padding to 256 rows: down to the kernel's m block,
    16 under emulation (2 r, r=8) and on aie2 (4 r, r=4), else 8.
    """
    dev = request.getfixturevalue(device)
    op = GEMM(M=M, K=64, N=512, precision=precision)
    assert op.resolved(dev).tile_m == tile_m


@pytest.mark.parametrize(
    "device, precision, M, rows, tile_m",
    [
        ("npu2", Precision.MEDIUM, 32, 2, 16),
        ("npu2", Precision.HIGH, 16, 2, 8),
        ("npu1", Precision.HIGH, 32, 2, 16),
        ("npu1", Precision.HIGH, 16, 1, 16),
    ],
)
def test_a_short_m_takes_fewer_rows_of_cores(
    device, precision, M, rows, tile_m, request
):
    """An M shorter than every row of cores at the kernel's m block is split
    over half as many, down to one.
    """
    op = GEMM(M=M, K=64, N=512, precision=precision)
    resolved = op.resolved(request.getfixturevalue(device))
    assert (resolved.n_aie_rows, resolved.tile_m) == (rows, tile_m)


@pytest.mark.parametrize(
    "device, precision", [("npu2", Precision.MEDIUM), ("npu1", Precision.HIGH)]
)
def test_an_m_no_tile_splits_is_rejected(device, precision, request):
    """Refused when constructed for the bound device, which has no such tile."""
    request.getfixturevalue(device)
    with pytest.raises(ValueError, match=r"M \(8\) must be a multiple of 64"):
        GEMM(M=8, K=64, N=512, precision=precision)


# Extents the grid does not divide: refused once the grid is known.
@pytest.mark.parametrize(
    "K, N, match", [(1000, 128, r"K \(1000\)"), (1024, 100, r"N \(100\)")]
)
def test_flm_dequant_rejects_unservable_shapes(K, N, match, npu2):
    with pytest.raises(ValueError, match=match):
        DequantBFP(K=K, N=N).resolved(npu2)


@pytest.mark.parametrize(
    "cls, kwargs, match",
    [
        (PrefillAttention, dict(num_kv_heads=3), "multiple of"),
        (PrefillAttention, dict(num_kv_heads=0), "must be positive"),
        (PrefillAttention, dict(num_kv_heads=8), "query heads"),
        (
            PrefillSlidingAttention,
            dict(num_kv_heads=1, window=500),
            "multiple of 128",
        ),
    ],
)
@pytest.mark.skipif(
    "attn_qk_chunk" not in flm_gemma4._PrefillKernel.__annotations__,
    reason="needs mlir-aie's prefill kernel with attn_qk_chunk (Xilinx/mlir-aie#3940)",
)
def test_flm_prefill_attention_rejects_unservable_shapes(cls, kwargs, match, npu2):
    with pytest.raises(ValueError, match=match):
        cls(**{"max_context": 1024, "num_heads": 8, **kwargs})


@pytest.mark.parametrize(
    "dim, vocab, softcap, match",
    [
        (1000, 4096, 30.0, r"dim \(1000\) must be a multiple"),
        (1536, 1000, 30.0, r"vocab \(1000\) must be a multiple"),
        (1536, 4096, 0.0, "finite and positive"),
    ],
)
def test_flm_lm_head_rejects_unservable_shapes(dim, vocab, softcap, match, npu2):
    with pytest.raises(ValueError, match=match):
        LMHead(dim=dim, vocab=vocab, softcap=softcap).resolved(npu2)


@pytest.mark.parametrize(
    "kwargs, match",
    [
        (
            dict(
                geometry=dataclasses.replace(
                    FLM_GEMMA4_E2B_DECODE, model_dim=2048, name="gemma4_e8b"
                ),
                layer_type="global",
            ),
            r"geometry \(.*\) must be",
        ),
        (
            dict(geometry=FLM_GEMMA4_E2B_DECODE, layer_type="sliding"),
            r"layer_type \('sliding'\) must be one of",
        ),
    ],
    ids=["geometry", "layer_type"],
)
def test_flm_decode_layer_rejects_unknown_configurations(kwargs, match):
    with pytest.raises(ValueError, match=match):
        DecodeLayer(**kwargs)


@pytest.mark.parametrize(
    "make, match",
    [
        (lambda: DepthwiseConv1d(rows=64, channels=48), "32-lane vectors"),
        (
            lambda: DepthwiseConv1d(rows=6, channels=64, num_aie_columns=2),
            r"rows \(6\) must split into 2 runs",
        ),
        (lambda: Emit(slots=4, carried=2, rows=5), r"Emit: rows \(5\) must be 6"),
        (lambda: Clamp(size=2048, tile_size=2048, low=1.0, high=0.5), "exceeds high"),
        (lambda: RoPE(rows=64, cols=48), r"cols \(48\) must be a positive multiple"),
        (lambda: RoPE(rows=64, cols=64, angle_rows=48), "must divide rows"),
        (
            lambda: RoPE(rows=60, cols=64, angle_rows=4, num_aie_columns=8),
            r"rows \(60\) must be a multiple of num_aie_columns",
        ),
        (
            lambda: RoPE(rows=64, cols=64, angle_rows=4, num_aie_columns=8),
            r"angle_rows \(4\) must be a multiple of",
        ),
        (lambda: Softmax(rows=16, cols=64, soft_cap=30.0), "of the float32 input path"),
        (
            lambda: Softmax(rows=16, cols=64, input_dtype=np.float32, window=4),
            "given together",
        ),
        (
            lambda: Softmax(
                rows=16, cols=64, input_dtype=np.float32, window=4, period=8
            ),
            "pre-cap addend",
        ),
    ],
    ids=[
        "conv_channels",
        "conv_runs",
        "emit_rows",
        "clamp_bounds",
        "rope_cols",
        "rope_angle_rows",
        "rope_rows_split",
        "rope_angle_rows_split",
        "softmax_f32_option",
        "softmax_window_alone",
        "softmax_window_no_addend",
    ],
)
def test_a_validate_or_compatible_branch_refuses(make, match, npu2):
    with pytest.raises(ValueError, match=match):
        make().resolved(npu2)
