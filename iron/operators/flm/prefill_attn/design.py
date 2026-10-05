# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Causal prefill attention, optionally over a sliding window, on the whole array.

Groups of columns each take one query head per pass. A round covers ROUND
query rows. The cores of a group split these rows. Each core receives every key
up to the round's last row, or every key inside the window. k and v come from
one shim tile and reach every core through one memtile. The runtime sequence
takes the token range and the KV cache's row count as dispatch parameters. One
build therefore serves every prompt.

The two kernels differ in geometry and in their L1 layout. ``Geometry`` reads
the geometry from the kernel build. A ``Variant`` holds the rest of what
differs.
"""

from dataclasses import dataclass
from typing import Callable

import numpy as np
from ml_dtypes import bfloat16

from aie.dialects import arith
from aie.dialects.aie import DMAChannelDir
from aie.dialects.aiex import _as_i32
from aie.extras import types as T
from aie.helpers.npdtypes import np_ndarray_type_get_shape
from aie.helpers.taplib import TensorAccessPattern
from aie.ir import Attribute
from aie.iron import (
    Acquire,
    Bd,
    Buffer,
    DispatchTime,
    DmaChannel,
    ExternalFunction,
    Lock,
    ObjectFifo,
    Program,
    Release,
    Runtime,
    TileDma,
    Worker,
    require,
)
from aie.iron.controlflow import range_
from aie.iron.dataflow import Flow
from aie.iron.device import Tile
from aie.iron.kernels import flm_gemma4

from iron.operators.flm.dataflow import ping_pong

LK_MT = 128  # key rows per memtile buffer
# Query rows per round. For each variant, the cores per group times the query
# rows per core equal ROUND.
ROUND = 128

# The k/v DMA and the kernel's steps synchronize on these locks of each core.
IN_PROD_LOCK, IN_CONS_LOCK = 2, 3

bf16 = np.dtype[bfloat16]


@dataclass(frozen=True)
class Geometry:
    """The tile shapes that the kernel build fixes."""

    dh: int  # head dim
    lq: int  # query rows per core
    lk: int  # key rows per step

    @classmethod
    def of(cls, kernel):
        """Read the shapes from the argument types of the kernel's entry points."""
        lq, dh = np_ndarray_type_get_shape(kernel.attn_round_begin.arg_types()[4])
        lk, _ = np_ndarray_type_get_shape(kernel.attn_qk_step.arg_types()[2])
        return cls(dh=dh, lq=lq, lk=lk)


@dataclass(frozen=True)
class Variant:
    """What differs between the causal and the sliding-window kernel's designs."""

    name: str
    factory: Callable[..., ExternalFunction]
    num_cu: int  # column groups, one query head each per pass
    # The buffer addresses of the FastFlowLM overlay. The stack occupies the
    # addresses from 0 to in_1, the lowest buffer.
    l1: dict
    # The memtile that splits the q fifos of column pair p.
    q_memtile: Callable[[int], int]
    # The memtile that stages k and v.
    kv_memtile: int
    # True: the variant takes a window. attn_blocks then takes the window_size
    # RTP as an argument, and _stage_kv_sliding stages k and v.
    windowed: bool
    release_q_before_epilogue: bool


CAUSAL = Variant(
    name="causal",
    factory=flm_gemma4.flm_gemma4_attn_prefill,
    num_cu=2,
    l1={
        "in_0": 49152,
        "in_1": 3072,
        "s": 57344,
        "m": 11392,
        "y": 32768,
        "L_begin": 59520,
        "L_end": 11520,
        "window_size": 59552,
        "n_rounds": 11552,
    },
    q_memtile=lambda p: 2 * p + p % 2,
    kv_memtile=2,
    windowed=False,
    release_q_before_epilogue=False,
)

SLIDING = Variant(
    name="sliding",
    factory=flm_gemma4.flm_gemma4_swa_prefill,
    num_cu=4,
    l1={
        "L_begin": 61568,
        "L_end": 11904,
        "window_size": 61600,
        "in_0": 49152,
        "in_1": 3712,
        "s": 57344,
        "m": 61760,
        "y": 32768,
        "l_bf16": 61440,
        "n_rounds": 11936,
    },
    q_memtile=lambda p: 2 * p,
    kv_memtile=3,
    windowed=True,
    release_q_before_epilogue=True,
)

VARIANTS = {v.name: v for v in (CAUSAL, SLIDING)}


def _stage_kv_causal(rt, MT, v, g):
    """The k/v memtile takes k and v on two channels and sends them interleaved on one.

    The memtile to its left holds half of the buffers.
    """
    mt, mt_left = MT[v.kv_memtile], MT[v.kv_memtile - 1]
    in_mem_ty = np.ndarray[(LK_MT, g.dh), bf16]
    bufs = {
        (side, n): Buffer(type=in_mem_ty, name=f"in_{n}_0_{tile.col}", tile=tile)
        for side, tile in (("own", mt), ("left", mt_left))
        for n in (0, 1)
    }
    # The locks of the left pair sit on mt.
    left_prod = Lock(tile=mt, lock_id=0, init=2)
    left_cons = Lock(tile=mt, lock_id=1, init=0)
    own_prod = Lock(tile=mt, lock_id=7, init=2)
    own_cons = Lock(tile=mt, lock_id=8, init=0)
    fill = TensorAccessPattern(
        (LK_MT, g.dh), 0, [LK_MT // g.lk, g.lk, 64, 8], [g.lk * g.dh, 8, 64, 1]
    )
    rt.add_tile_dma(
        TileDma(
            mt,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    ping_pong(
                        bufs[("left", 0)],
                        bufs[("left", 1)],
                        left_prod,
                        left_cons,
                        tap=fill,
                    ),
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    ping_pong(
                        bufs[("own", 0)],
                        bufs[("own", 1)],
                        own_prod,
                        own_cons,
                        tap=fill,
                    ),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    [
                        Bd(
                            bufs[(side, n)],
                            acquires=[Acquire(cons)],
                            releases=[Release(prod)],
                        )
                        for n in (0, 1)
                        for side, cons, prod in (
                            ("left", left_cons, left_prod),
                            ("own", own_cons, own_prod),
                        )
                    ],
                ),
            ],
        )
    )


def _stage_kv_sliding(rt, MT, v, g):
    """The k/v memtile stages k and v in one buffer pair: k in the first half, v in the second.

    Each S2MM channel releases one count per buffer. The MM2S channel acquires
    two counts. It therefore reads a buffer after both halves hold data.
    """
    in_mem_ty = np.ndarray[(LK_MT * 2, g.dh), bf16]
    half = LK_MT * g.dh
    mt = MT[v.kv_memtile]
    in_0 = Buffer(type=in_mem_ty, name=f"in_0_0_{mt.col}", tile=mt)
    in_1 = Buffer(type=in_mem_ty, name=f"in_1_0_{mt.col}", tile=mt)
    prod = Lock(tile=mt, lock_id=0, init=4)
    cons = Lock(tile=mt, lock_id=1, init=0)
    rt.add_tile_dma(
        TileDma(
            mt,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    ch,
                    ping_pong(
                        in_0,
                        in_1,
                        prod,
                        cons,
                        tap=TensorAccessPattern(
                            (2 * LK_MT, g.dh),
                            offset,
                            [LK_MT // g.lk, g.lk, 32, 8],
                            [g.lk * g.dh, 8, 128, 1],
                        ),
                    ),
                )
                for ch, offset in ((0, 0), (1, half))
            ]
            + [
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    ping_pong(
                        in_0,
                        in_1,
                        cons,
                        prod,
                        acq_val=2,
                        rel_val=2,
                        tap=TensorAccessPattern.full((2 * LK_MT, g.dh)),
                    ),
                ),
            ],
        )
    )


def _no_unroll(iv):
    """Disable unrolling of the scf.for that yields iv in Peano's opt.

    Each unrolled copy recomputes the same buffer addresses as call arguments.
    The copies add instructions to every step. MLIR drops a malformed
    annotation without an error: check the call count in the core's opted_*.ll.
    """
    iv.owner.owner.attributes["loop_annotation"] = Attribute.parse(
        "#llvm.loop_annotation<unroll = <disable = true>>"
    )


def prefill_attn(
    dev,
    variant,
    max_context,
    num_heads,
    num_kv_heads,
    window=None,
    trace_size=0,
    *,
    kernel,
    L_begin: DispatchTime[np.int32],
    L_end: DispatchTime[np.int32],
    max_l: DispatchTime[np.int32],
):
    """Prefill attention over a KV cache of up to max_context rows.

    The README gives the layout of O, Q and KV and the meaning of the
    dispatch parameters ``L_begin``, ``L_end`` and ``max_l``. ``kernel`` is
    the variant's factory's build with the locks IN_PROD_LOCK and
    IN_CONS_LOCK.
    """
    v = VARIANTS[variant]
    if v.windowed != (window is not None):
        need = "needs a" if v.windowed else "takes no"
        raise ValueError(f"the {v.name} variant {need} window")
    g = Geometry.of(kernel)
    group_cols = dev.cols // v.num_cu
    gqa = num_heads // num_kv_heads
    # Elements per token in Q and O, and in each of k and v.
    qo_row = g.dh * num_heads
    kv_row = g.dh * num_kv_heads
    # Query rows in a core's q object: the rows of both columns of a pair.
    lq_ct = 2 * g.lq
    # Query rows per memtile fifo half.
    lq_mt = 4 * g.lq

    # The core's buffers take the kernel's argument types.
    s_ty, q_ty, in_ty, _, m_ty, L_ty = kernel.attn_qk_step.arg_types()[:6]
    mv_ty, _, cv_ty, _, y_ty = kernel.attn_round_begin.arg_types()
    o_ty, l_bf16_ty, _, _ = kernel.attn_epilogue.arg_types()
    q_half_ty = np.ndarray[(lq_mt, g.dh), bf16]
    o_col_ty = np.ndarray[(lq_mt, g.dh), bf16]

    # The memtiles move q and o in 8x8 blocks.
    q_walk = TensorAccessPattern.full((lq_ct, g.dh)).tile((8, 8))
    o_walk = TensorAccessPattern.full((g.lq, g.dh)).tile((8, 8))
    # Block b of Q and O: query rows b * lq_mt onwards, all heads.
    qo_blocks = TensorAccessPattern.full((max_context, num_heads, g.dh)).partition(
        max_context // lq_mt
    )
    blocks_per_round = ROUND // lq_mt

    # Shim row 0, memtile row 1. Each tile carries its type. A Worker stamps an
    # untyped tile with Tile.with_type(). That call returns a second CoreTile
    # at the coordinates of the first tile's buffers and locks.
    IT = [Tile(j, 0, tile_type=dev.get_tile_type(j, 0)) for j in range(dev.cols)]
    MT = [Tile(j, 1, tile_type=dev.get_tile_type(j, 1)) for j in range(dev.cols)]
    CT = {
        (j, r): Tile(j, r, tile_type=dev.get_tile_type(j, r))
        for j in range(dev.cols)
        for r in dev.core_rows
    }

    def sequence(o, q, kv, lb_arg, le_arg, max_l_arg, o_shim, q_shims):
        q_shim = dict(zip(q_keys, q_shims))
        kv_cache = TensorAccessPattern.full((2, _as_i32(max_l_arg), num_kv_heads, g.dh))
        L_begin = _as_i32(lb_arg)
        L_end = _as_i32(le_arg)
        require(L_begin >= 0, "L_begin must be >= 0")
        require(L_begin % ROUND == 0, f"L_begin must be a multiple of {ROUND}")
        require(L_end % ROUND == 0, f"L_end must be a multiple of {ROUND}")
        require(_as_i32(max_l_arg) <= max_context, "max_l exceeds max_context")
        rounds = arith.divsi(L_end - L_begin + (ROUND - 1), _as_i32(ROUND))

        for key in sorted(rtp):
            lb, le, ws = rtp[key]
            lb[0] = L_begin
            le[0] = L_end
            # A window of L_end covers every key from token 0.
            ws[0] = L_end if window is None else window
        for key in sorted(go):
            go[key].set(num_heads // v.num_cu)

        for head in range(num_heads // v.num_cu):
            for rnd in range_(rounds):
                r = arith.index_cast(T.i32(), rnd)
                if window is None:
                    kv_begin = 0
                    kv_length = r * ROUND + (L_begin + ROUND)
                else:
                    lq_current = L_begin + r * ROUND
                    x = lq_current - _as_i32(window)
                    # max(x, 0) without a branch: x & (x >> 31) is x when x < 0,
                    # else 0.
                    kv_begin = x - arith.andi(x, arith.shrsi(x, _as_i32(31)))
                    kv_length = lq_current - kv_begin + _as_i32(ROUND)
                o_tasks, q_tasks = [], []
                for cu in range(v.num_cu):
                    head_off = head * v.num_cu + cu
                    for col in range(group_cols):
                        o_tasks.append(
                            o_shim[cu * group_cols + col].drain(
                                o,
                                qo_blocks[r * blocks_per_round + col, :, head_off],
                                wait=True,
                                managed=False,
                            )
                        )
                    pairs = range(cu * group_cols // 2, (cu + 1) * group_cols // 2)
                    for qi, key in enumerate((p, h) for p in pairs for h in (0, 1)):
                        q_tasks.append(
                            q_shim[key].fill(
                                q,
                                qo_blocks[r * blocks_per_round + qi, :, head_off],
                                wait=False,
                                managed=False,
                            )
                        )
                # Rows of 128 keys: one row alone may exceed a BD dimension.
                kv_head = head // (gqa // v.num_cu)
                rows = slice(kv_begin, kv_begin + kv_length)
                kv_tasks = [
                    flow.fill(
                        kv,
                        tap=kv_cache[half, rows, kv_head].split(0, 128),
                        wait=False,
                        managed=False,
                    )
                    for half, flow in enumerate(kv_flows)
                ]
                # Every handle must retire inside the scf.for that created it.
                for t in o_tasks:
                    t.await_()
                    t.free()
                for t in q_tasks + kv_tasks:
                    t.free()

    # RTPs, one set per core, keyed by the tile's (row, col): the sequence
    # writes the token range and the window into them.
    rtp = {}
    # go orders each core's RTP read after the sequence's RTP write. A core
    # starts its next pass when a dispatch ends. The next dispatch writes the
    # RTPs later.
    #
    # The sequence sets go to the number of passes after it writes the RTPs.
    # A core acquires one count before each pass.
    go = {}
    # The shim flows of k, then v.
    kv_flows = []

    # o: one fifo per memtile m. Memtile m joins the output of four cores:
    # rows 0 and 1 for an even m, rows 2 and 3 for an odd m, in columns
    # 2*(m//2) and 2*(m//2)+1.
    o_shim, o_prod = [], {}
    for m in range(dev.cols):
        of_o = ObjectFifo(o_col_ty, name=f"o{m}", depth=2)
        o_shim.append(of_o.cons(tile=IT[m], channel=0))
        sub = of_o.prod().join(
            [g.lq * g.dh * i for i in range(4)],
            obj_types=[o_ty] * 4,
            names=[f"o{m}_{i}" for i in range(4)],
            from_stream=[o_walk] * 4,
            tile=MT[m],
        )
        base_row = 0 if m % 2 == 0 else 2
        for c in range(4):
            o_prod[(base_row + c // 2, 2 * (m // 2) + (c & 0x1))] = sub[c]

    # q: the mirror of o. The memtile of each column pair takes two halves on
    # two channels. Each half splits into two slices, one per row. The memtile
    # broadcasts each slice to both columns of the pair. Half 0 feeds rows 0
    # and 1.
    q_shim, q_cons = {}, {}
    for p in range(dev.cols // 2):
        mt_idx = v.q_memtile(p)
        for half, rows in ((0, (0, 1)), (1, (2, 3))):
            of_q = ObjectFifo(q_half_ty, name=f"q{mt_idx}_{half}", depth=2)
            q_shim[(p, half)] = of_q.prod(tile=IT[mt_idx], channel=half)
            slices = of_q.cons().split(
                [lq_ct * g.dh * t for t in range(2)],
                obj_types=[q_ty] * 2,
                names=[f"q{mt_idx}_{half}_{t}" for t in range(2)],
                to_stream=[q_walk] * 2,
                depths=[1, 1],
                tile=MT[mt_idx],
            )
            for t, row in enumerate(rows):
                for col in (2 * p, 2 * p + 1):
                    q_cons[(row, col)] = slices[t]
    q_keys = list(q_shim)

    o_l3_ty = np.ndarray[(max_context * qo_row,), bf16]
    kv_l3_ty = np.ndarray[(max_context * kv_row * 2,), bf16]
    rt = Runtime(
        sequence,
        [
            o_l3_ty,
            o_l3_ty,
            kv_l3_ty,
            L_begin,
            L_end,
            max_l,
            o_shim,
            list(q_shim.values()),
        ],
    )

    def make_core_fn(row, col):
        def core_fn(
            q_h,
            o_h,
            in0,
            in1,
            s,
            m,
            y,
            l_bf16,
            prev_m,
            new_m,
            cbuf,
            lbuf,
            lb,
            le,
            ws,
            n_buf,
            nb,
            rounds_k,
            round_begin_k,
            blocks_k,
            block_begin_k,
            qk_k,
            block_mid_k,
            fv_k,
            block_end_k,
            finalize_k,
            epilogue_k,
            go_lock,
        ):
            go_lock.acquire(1)
            rounds_k(lb, le, n_buf)
            for i in range_(n_buf[0]):
                q = q_h.acquire(1)
                round_begin_k(prev_m, new_m, cbuf, lbuf, y)
                blocks_k(*((lb, ws) if v.windowed else (lb,)), i, nb)
                for b in range_(nb[0]):
                    block_begin_k(m, prev_m)
                    for j in range_(LK_MT // g.lk):
                        _no_unroll(j)
                        qk_k(s, q, in0, in1, m, lb, ws, row, col, i, b, j)
                    block_mid_k(s, m, new_m, prev_m, cbuf, lbuf, y)
                    for j in range_(LK_MT // g.lk):
                        _no_unroll(j)
                        fv_k(y, s, in0, in1, j)
                    block_end_k(prev_m, new_m)
                finalize_k(lbuf, l_bf16)
                if v.release_q_before_epilogue:
                    q_h.release(1)
                for c in range_(g.lq * g.dh // 64):
                    o = o_h.acquire(1)
                    epilogue_k(o, l_bf16, y, c)
                    o_h.release(1)
                if not v.release_q_before_epilogue:
                    q_h.release(1)

        return core_fn

    workers = []
    for j in range(dev.cols):
        for i, r in enumerate(dev.core_rows):
            tile = CT[(j, r)]
            name = f"{tile.row}_{tile.col}"

            def buf(ty, key, **kw):
                return Buffer(type=ty, name=f"{key}_{name}", tile=tile, **kw)

            rtp[(tile.row, tile.col)] = [
                buf(L_ty, f"{key}_attn_core", use_write_rtp=True, address=v.l1[key])
                for key in ("L_begin", "L_end", "window_size")
            ]
            in_0 = buf(in_ty, "in_0", address=v.l1["in_0"])
            in_1 = buf(in_ty, "in_1", address=v.l1["in_1"])
            core_bufs = [
                in_0,
                in_1,
                buf(s_ty, "s", address=v.l1["s"]),
                buf(m_ty, "m", address=v.l1["m"]),
                buf(y_ty, "y", address=v.l1["y"]),
                buf(l_bf16_ty, "l_bf16", address=v.l1.get("l_bf16")),
                buf(mv_ty, "prev_m"),
                buf(mv_ty, "new_m"),
                buf(cv_ty, "c"),
                buf(cv_ty, "l"),
            ]
            n_rounds = buf(L_ty, "n_rounds", address=v.l1["n_rounds"])
            n_blocks = buf(L_ty, "n_blocks")
            in_prod = Lock(tile=tile, lock_id=IN_PROD_LOCK, init=2)
            in_cons = Lock(tile=tile, lock_id=IN_CONS_LOCK, init=0)
            go_lock = Lock(tile=tile, init=0, name=f"go_{name}")
            go[(tile.row, tile.col)] = go_lock
            workers.append(
                Worker(
                    make_core_fn(i, j % group_cols),
                    [q_cons[(i, j)].cons(), o_prod[(i, j)].prod()]
                    + core_bufs
                    + rtp[(tile.row, tile.col)]
                    + [
                        n_rounds,
                        n_blocks,
                        kernel.attn_rounds,
                        kernel.attn_round_begin,
                        kernel.attn_blocks,
                        kernel.attn_block_begin,
                        kernel.attn_qk_step,
                        kernel.attn_block_mid,
                        kernel.attn_fv_step,
                        kernel.attn_block_end,
                        kernel.attn_finalize,
                        kernel.attn_epilogue,
                        go_lock,
                    ],
                    tile=tile,
                    while_true=True,
                    stack_size=v.l1["in_1"],
                )
            )
            # k and v share S2MM channel 1; q takes channel 0.
            rt.add_tile_dma(
                TileDma(
                    tile,
                    [
                        DmaChannel(
                            DMAChannelDir.S2MM,
                            1,
                            ping_pong(in_0, in_1, in_prod, in_cons),
                        )
                    ],
                )
            )

    stage_kv = _stage_kv_sliding if v.windowed else _stage_kv_causal
    stage_kv(rt, MT, v, g)

    kv_mt = v.kv_memtile
    for ch, symbol in enumerate(("k_in", "v_in")):
        kv_flows.append(
            Flow(
                IT[kv_mt], MT[kv_mt], src_channel=ch, dst_channel=ch, shim_symbol=symbol
            )
        )
        rt.add_flow(kv_flows[-1])
    for tile in CT.values():
        rt.add_flow(Flow(MT[kv_mt], tile, src_channel=0, dst_channel=1))

    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
