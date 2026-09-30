# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Causal prefill attention, optionally over a sliding window, on the whole array.

Groups of columns each take one query head per pass. A round covers ROUND
query rows. The cores of a group split these rows. Each core receives every key
up to the round's last row, or every key inside the window. k and v come from
one shim tile and reach every core through one memtile. The runtime sequence
takes the token range and the KV cache's row count as dispatch parameters. One
build therefore serves every prompt.

The two kernels differ in geometry and in their L1 layout. A ``Variant``
holds what differs.
"""

from dataclasses import dataclass
from typing import Callable

import numpy as np
from ml_dtypes import bfloat16

from aie.dialects import arith
from aie.dialects.aie import DMAChannelDir
from aie.dialects.aiex import (
    _as_i32,
    dma_free_task,
    dma_start_task,
    set_lock_value,
    shim_dma_single_bd_task,
)
from aie.extras import types as T
from aie.ir import Attribute
from aie.iron import (
    Acquire,
    Bd,
    Buffer,
    DmaChannel,
    Lock,
    ObjectFifo,
    Program,
    Release,
    Runtime,
    TileDma,
    Worker,
)
from aie.iron import kernels
from aie.iron.controlflow import range_
from aie.iron.dataflow import Flow
from aie.iron.device import Tile

from iron.common.device_utils import call_factory
from iron.operators.flm.dataflow import grid, ping_pong

LK_MT = 128  # key rows per memtile buffer
# Query rows per round. For each variant, the cores per group times the query
# rows per core equal ROUND.
ROUND = 128

# The k/v DMA and the kernel's steps synchronize on these locks of each core.
IN_PROD_LOCK, IN_CONS_LOCK = 2, 3

bf16 = np.dtype[bfloat16]


def _dims(d):
    return dict(sizes=[x[0] for x in d], strides=[x[1] for x in d])


def _stage_kv_causal(rt, MT, v):
    """The k/v memtile takes k and v on two channels and sends them interleaved on one.

    The memtile to its left holds half of the buffers.
    """
    mt, mt_left = MT[v.kv_memtile], MT[v.kv_memtile - 1]
    in_mem_ty = np.ndarray[(LK_MT, v.dh), bf16]
    kvdims = [(LK_MT // v.lk, v.lk * v.dh), (v.lk, 8), (64, 64), (8, 1)]
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
    for lock in (left_prod, left_cons, own_prod, own_cons):
        rt.add_lock(lock)
    fill = dict(offset=0, length=LK_MT * v.dh, **_dims(kvdims))

    def out(b, cons, prod, nxt):
        return Bd(b, acquires=[Acquire(cons)], releases=[Release(prod)], next=nxt)

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
                        **fill,
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
                        **fill,
                    ),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    [
                        out(bufs[("left", 0)], left_cons, left_prod, 1),
                        out(bufs[("own", 0)], own_cons, own_prod, 2),
                        out(bufs[("left", 1)], left_cons, left_prod, 3),
                        out(bufs[("own", 1)], own_cons, own_prod, 0),
                    ],
                ),
            ],
        )
    )
    # The placer removes a memtile that has no DMA program. The empty program
    # retains mt_left and its buffers.
    rt.add_tile_dma(TileDma(mt_left, []))


def _stage_kv_sliding(rt, MT, v):
    """The k/v memtile stages k and v in one buffer pair: k in the first half, v in the second.

    Each S2MM channel releases one count per buffer. The MM2S channel acquires
    two counts. It therefore reads a buffer after both halves hold data.
    """
    in_mem_ty = np.ndarray[(LK_MT * 2, v.dh), bf16]
    indims = [(LK_MT // v.lk, v.lk * v.dh), (v.lk, 8), (32, 128), (8, 1)]
    outdims = [(2 * LK_MT // v.lk, v.lk * v.dh), (v.lk, v.dh), (v.dh, 1)]
    half = LK_MT * v.dh
    mt = MT[v.kv_memtile]
    in_0 = Buffer(type=in_mem_ty, name=f"in_0_0_{mt.col}", tile=mt)
    in_1 = Buffer(type=in_mem_ty, name=f"in_1_0_{mt.col}", tile=mt)
    prod = Lock(tile=mt, lock_id=0, init=4)
    cons = Lock(tile=mt, lock_id=1, init=0)
    rt.add_lock(prod)
    rt.add_lock(cons)
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
                        offset=offset,
                        length=half,
                        **_dims(indims),
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
                        offset=0,
                        length=2 * half,
                        **_dims(outdims),
                    ),
                ),
            ],
        )
    )


@dataclass(frozen=True)
class Variant:
    """What differs between the causal and the sliding-window kernel's designs."""

    name: str
    factory: str  # the aie.iron.kernels factory
    dh: int  # head dim
    lq: int  # query rows per core
    lk: int  # key rows per step
    num_cu: int  # column groups, one query head each per pass
    # The buffer addresses of the FastFlowLM overlay. The stack occupies the
    # addresses from 0 to in_1, the lowest buffer.
    l1: dict
    # The memtile that splits the q fifos of column pair p.
    q_memtile: Callable[[int], int]
    # The memtile that stages k and v, and its DMA program.
    kv_memtile: int
    stage_kv: Callable
    # True: the variant takes a window. attn_blocks then takes the window_size
    # RTP as an argument.
    windowed: bool
    release_q_before_epilogue: bool

    @property
    def lq_ct(self):
        """Query rows in a core's q object: the rows of both columns of a pair."""
        return 2 * self.lq

    @property
    def lq_mt(self):
        """Query rows per memtile fifo half."""
        return 4 * self.lq


CAUSAL = Variant(
    name="causal",
    factory="flm_gemma4_attn_prefill",
    dh=512,
    lq=8,
    lk=8,
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
    stage_kv=_stage_kv_causal,
    windowed=False,
    release_q_before_epilogue=False,
)

SLIDING = Variant(
    name="sliding",
    factory="flm_gemma4_swa_prefill",
    dh=256,
    lq=16,
    lk=16,
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
    stage_kv=_stage_kv_sliding,
    windowed=True,
    release_q_before_epilogue=True,
)

VARIANTS = {v.name: v for v in (CAUSAL, SLIDING)}


def kernel(variant, device=None):
    """The kernel build that the variant's cores link."""
    return call_factory(
        getattr(kernels, variant.factory),
        device=device,
        in_prod_lock=IN_PROD_LOCK,
        in_cons_lock=IN_CONS_LOCK,
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
    dev, variant, max_context, num_heads, num_kv_heads, window=None, trace_size=0
):
    """Prefill attention over a KV cache of up to max_context rows.

    The README gives the layout of O, Q and KV.
    """
    v = VARIANTS[variant]
    if v.windowed != (window is not None):
        need = "needs a" if v.windowed else "takes no"
        raise ValueError(f"the {v.name} variant {need} window")
    COLS, ROWS = grid(dev)
    DH, LQ, LK, NUM_CU, L1 = v.dh, v.lq, v.lk, v.num_cu, v.l1
    GROUP_COLS = COLS // NUM_CU
    HEADS = num_heads
    KV_D = num_kv_heads
    GQA = HEADS // KV_D

    f32 = np.dtype[np.float32]

    q_ty = np.ndarray[(v.lq_ct, DH), bf16]
    in_ty = np.ndarray[(LK, DH), bf16]
    o_ty = np.ndarray[(64,), bf16]
    q_half_ty = np.ndarray[(v.lq_mt, DH), bf16]
    o_col_ty = np.ndarray[(v.lq_mt, DH), bf16]
    s_ty = np.ndarray[(LQ, LK_MT), bf16]
    m_ty = np.ndarray[(LQ, LK), bf16]
    y_ty = np.ndarray[(LQ, DH), f32]
    l_bf16_ty = np.ndarray[(LQ,), bf16]
    mv_ty = np.ndarray[(LQ,), bf16]
    cv_ty = np.ndarray[(LQ,), f32]
    L_ty = np.ndarray[(8,), np.dtype[np.int32]]

    qdims = [(v.lq_ct // 8, 8 * DH), (DH // 8, 8), (8, DH), (8, 1)]
    odims = [(LQ // 8, 8 * DH), (DH // 8, 8), (8, DH), (8, 1)]

    k = kernel(v, dev).entry
    k_rounds = k("attn_rounds", [L_ty, L_ty, L_ty])
    k_round_begin = k("attn_round_begin", [mv_ty, mv_ty, cv_ty, cv_ty, y_ty])
    k_blocks = k("attn_blocks", [L_ty] * (1 + v.windowed) + [np.int32, L_ty])
    k_block_begin = k("attn_block_begin", [m_ty, mv_ty])
    k_qk = k(
        "attn_qk_step",
        [s_ty, q_ty, in_ty, in_ty, m_ty, L_ty, L_ty] + [np.int32] * 5,
    )
    k_block_mid = k("attn_block_mid", [s_ty, m_ty, mv_ty, mv_ty, cv_ty, cv_ty, y_ty])
    k_fv = k("attn_fv_step", [y_ty, s_ty, in_ty, in_ty, np.int32])
    k_block_end = k("attn_block_end", [mv_ty, mv_ty])
    k_finalize = k("attn_finalize", [cv_ty, l_bf16_ty])
    k_epilogue = k("attn_epilogue", [o_ty, l_bf16_ty, y_ty, np.int32])

    # Shim row 0, memtile row 1, compute rows from 2. Each tile needs its type.
    # The DMA of an untyped tile lowers to a core tile's aie.mem.
    IT = [Tile(j, 0, tile_type=dev.get_tile_type(j, 0)) for j in range(COLS)]
    MT = [Tile(j, 1, tile_type=dev.get_tile_type(j, 1)) for j in range(COLS)]
    CT = [
        [Tile(j, i + 2, tile_type=dev.get_tile_type(j, i + 2)) for j in range(COLS)]
        for i in range(ROWS)
    ]

    def sequence(o, q, kv, lb_arg, le_arg, max_l_arg, o_shim, q_shims):
        q_shim = dict(zip(q_keys, q_shims))
        max_l = _as_i32(max_l_arg)
        kv_cache_half = max_l * (DH * KV_D)
        L_begin = _as_i32(lb_arg)
        L_end = _as_i32(le_arg)
        rounds = arith.divsi(L_end - L_begin + (ROUND - 1), _as_i32(ROUND))

        for key in sorted(rtp):
            lb, le, ws = rtp[key]
            lb[0] = L_begin
            le[0] = L_end
            # A window of L_end covers every key from token 0.
            ws[0] = L_end if window is None else window
        for key in sorted(go):
            set_lock_value(go[key].op, HEADS // NUM_CU)

        def max0(x):
            # max(x, 0) without a branch: x & (x >> 31) is x when x < 0, else 0.
            return x - arith.andi(x, arith.shrsi(x, _as_i32(31)))

        for head in range(HEADS // NUM_CU):
            for rnd in range_(rounds):
                r = arith.index_cast(T.i32(), rnd)
                if window is None:
                    kv_length = r * ROUND + (L_begin + ROUND)
                else:
                    lq_current = L_begin + r * ROUND
                    kv_begin = max0(lq_current - _as_i32(window))
                    kv_length = lq_current - kv_begin + _as_i32(ROUND)
                o_tasks, q_tasks, kv_tasks = [], [], []
                for cu in range(NUM_CU):
                    head_off = head * NUM_CU + cu
                    for col in range(GROUP_COLS):
                        o_tasks.append(
                            o_shim[cu * GROUP_COLS + col].drain(
                                o,
                                sizes=[1, 1, v.lq_mt, DH],
                                strides=[0, 0, DH * HEADS, 1],
                                offset=r * (ROUND * DH * HEADS)
                                + (head_off * DH + col * v.lq_mt * DH * HEADS),
                                transfer_len=v.lq_mt * DH,
                                wait=True,
                                managed=False,
                            )
                        )
                    q_base = r * (ROUND * DH * HEADS) + head_off * DH
                    pairs = range(cu * GROUP_COLS // 2, (cu + 1) * GROUP_COLS // 2)
                    for qi, key in enumerate((p, h) for p in pairs for h in (0, 1)):
                        q_tasks.append(
                            q_shim[key].fill(
                                q,
                                sizes=[1, 1, v.lq_mt, DH],
                                strides=[0, 0, DH * HEADS, 1],
                                offset=(
                                    q_base + qi * v.lq_mt * DH * HEADS if qi else q_base
                                ),
                                transfer_len=v.lq_mt * DH,
                                wait=False,
                                managed=False,
                            )
                        )
                # dma_bd's length operand is an i32. The product of the i64
                # sizes does not fit in it. transfer_len sets the length.
                kv_rows = arith.extsi(T.i64(), arith.divsi(kv_length, _as_i32(128)))
                kv_head = head // (GQA // NUM_CU)
                k_off = max_l * ((kv_head // KV_D) * DH * KV_D) + (kv_head % KV_D) * DH
                if window is not None:
                    k_off = k_off + kv_begin * _as_i32(DH * KV_D)
                for symbol, offset in (
                    ("k_in", k_off),
                    ("v_in", k_off + kv_cache_half),
                ):
                    kv_tasks.append(
                        shim_dma_single_bd_task(
                            symbol,
                            kv.op,
                            offset=offset,
                            sizes=[1, kv_rows, 128, DH],
                            strides=[0, 128 * DH * KV_D, DH * KV_D, 1],
                            transfer_len=kv_length * DH,
                            issue_token=False,
                        )
                    )
                dma_start_task(*kv_tasks)
                # Every handle must retire inside the scf.for that created it.
                for t in o_tasks:
                    t.await_()
                    t.free()
                for t in q_tasks:
                    t.free()
                dma_free_task(*kv_tasks)

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

    # o: one fifo per memtile m. Memtile m joins the output of four cores:
    # rows 0 and 1 for an even m, rows 2 and 3 for an odd m, in columns
    # 2*(m//2) and 2*(m//2)+1.
    o_shim, o_prod = [], {}
    for m in range(COLS):
        of_o = ObjectFifo(o_col_ty, name=f"o{m}", depth=2)
        o_shim.append(of_o.cons(tile=IT[m], channel=0))
        sub = of_o.prod().join(
            [LQ * DH * i for i in range(4)],
            obj_types=[o_ty] * 4,
            names=[f"o{m}_{i}" for i in range(4)],
            dims_from_stream=[odims] * 4,
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
    for p in range(COLS // 2):
        mt_idx = v.q_memtile(p)
        for half, rows in ((0, (0, 1)), (1, (2, 3))):
            of_q = ObjectFifo(q_half_ty, name=f"q{mt_idx}_{half}", depth=2)
            q_shim[(p, half)] = of_q.prod(tile=IT[mt_idx], channel=half)
            slices = of_q.cons().split(
                [v.lq_ct * DH * t for t in range(2)],
                obj_types=[q_ty] * 2,
                names=[f"q{mt_idx}_{half}_{t}" for t in range(2)],
                dims_to_stream=[qdims] * 2,
                depths=[1, 1],
                tile=MT[mt_idx],
            )
            for t, row in enumerate(rows):
                for col in (2 * p, 2 * p + 1):
                    q_cons[(row, col)] = slices[t]
    q_keys = list(q_shim)

    o_l3_ty = np.ndarray[(max_context * DH * HEADS,), bf16]
    kv_l3_ty = np.ndarray[(max_context * DH * KV_D * 2,), bf16]
    rt = Runtime(
        sequence,
        [
            o_l3_ty,
            o_l3_ty,
            kv_l3_ty,
            np.int32,
            np.int32,
            np.int32,
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
                    for j in range_(LK_MT // LK):
                        _no_unroll(j)
                        qk_k(s, q, in0, in1, m, lb, ws, row, col, i, b, j)
                    block_mid_k(s, m, new_m, prev_m, cbuf, lbuf, y)
                    for j in range_(LK_MT // LK):
                        _no_unroll(j)
                        fv_k(y, s, in0, in1, j)
                    block_end_k(prev_m, new_m)
                finalize_k(lbuf, l_bf16)
                if v.release_q_before_epilogue:
                    q_h.release(1)
                for c in range_(LQ * DH // 64):
                    o = o_h.acquire(1)
                    epilogue_k(o, l_bf16, y, c)
                    o_h.release(1)
                if not v.release_q_before_epilogue:
                    q_h.release(1)

        return core_fn

    workers = []
    for j in range(COLS):
        for i in range(ROWS):
            tile = CT[i][j]
            name = f"{tile.row}_{tile.col}"

            def buf(ty, key, **kw):
                return Buffer(type=ty, name=f"{key}_{name}", tile=tile, **kw)

            rtp[(tile.row, tile.col)] = [
                buf(L_ty, f"{key}_attn_core", use_write_rtp=True, address=L1[key])
                for key in ("L_begin", "L_end", "window_size")
            ]
            in_0 = buf(in_ty, "in_0", address=L1["in_0"])
            in_1 = buf(in_ty, "in_1", address=L1["in_1"])
            core_bufs = [
                in_0,
                in_1,
                buf(s_ty, "s", address=L1["s"]),
                buf(m_ty, "m", address=L1["m"]),
                buf(y_ty, "y", address=L1["y"]),
                buf(l_bf16_ty, "l_bf16", address=L1.get("l_bf16")),
                buf(mv_ty, "prev_m"),
                buf(mv_ty, "new_m"),
                buf(cv_ty, "c"),
                buf(cv_ty, "l"),
            ]
            n_rounds = buf(L_ty, "n_rounds", address=L1["n_rounds"])
            n_blocks = buf(L_ty, "n_blocks")
            in_prod = Lock(tile=tile, lock_id=IN_PROD_LOCK, init=2)
            in_cons = Lock(tile=tile, lock_id=IN_CONS_LOCK, init=0)
            go_lock = Lock(tile=tile, init=0, name=f"go_{name}")
            go[(tile.row, tile.col)] = go_lock
            for lock in (in_prod, in_cons, go_lock):
                rt.add_lock(lock)
            workers.append(
                Worker(
                    make_core_fn(i, j % GROUP_COLS),
                    [q_cons[(i, j)].cons(), o_prod[(i, j)].prod()]
                    + core_bufs
                    + rtp[(tile.row, tile.col)]
                    + [
                        n_rounds,
                        n_blocks,
                        k_rounds,
                        k_round_begin,
                        k_blocks,
                        k_block_begin,
                        k_qk,
                        k_block_mid,
                        k_fv,
                        k_block_end,
                        k_finalize,
                        k_epilogue,
                        go_lock,
                    ],
                    tile=tile,
                    while_true=True,
                    stack_size=L1["in_1"],
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

    v.stage_kv(rt, MT, v)

    kv_mt = v.kv_memtile
    rt.add_flow(
        Flow(IT[kv_mt], MT[kv_mt], src_channel=0, dst_channel=0, shim_symbol="k_in")
    )
    rt.add_flow(
        Flow(IT[kv_mt], MT[kv_mt], src_channel=1, dst_channel=1, shim_symbol="v_in")
    )
    for j in range(COLS):
        for i in range(ROWS):
            rt.add_flow(Flow(MT[kv_mt], CT[i][j], src_channel=0, dst_channel=1))

    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
