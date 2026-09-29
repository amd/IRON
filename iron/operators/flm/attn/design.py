# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Causal prefill attention with a head dim of 512, on the whole array.

Two column groups of four each take one query head per pass. A round covers
128 query rows: each of a group's 16 cores takes 8 of them and streams every
key up to the round's last row past them. k and v come from one shim tile and
reach every core through one memtile. The runtime sequence takes the token
range and the KV cache's row count at dispatch, so one build serves every
prompt.
"""

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
    Kernel,
    Lock,
    ObjectFifo,
    Program,
    Release,
    Runtime,
    TileDma,
    Worker,
)
from aie.iron.controlflow import range_
from aie.iron.dataflow import Flow
from aie.iron.device import AnyComputeTile, Tile

DH = 512  # head dim
LQ = 8  # query rows per core
LK = 8  # key rows per step
LK_MT = 128  # key rows per memtile buffer
LQ_MT = 32  # query rows per memtile fifo half
LQ_CT = 16  # query rows per core's q object, two cores' worth
NUM_CU = 2  # column groups
DATA_PER_ROUND = LK * 16  # query rows per round

KERNEL_OBJECT = "attn_prefill.o"

# The buffer addresses of the FastFlowLM overlay this design reproduces. The
# stack occupies [0, STACK_SIZE) and grows up, so in_1, the lowest buffer, caps
# it.
L1 = {
    "in_0": 49152,
    "in_1": 3072,
    "s": 57344,
    "m": 11392,
    "y": 32768,
    "L_begin": 59520,
    "L_end": 11520,
    "window_size": 59552,
    "n_rounds": 11552,
}
STACK_SIZE = 3 * 1024

# Locks 2 and 3 of each core guard k and v. The kernel names them by number.
IN_PROD_LOCK, IN_CONS_LOCK = 2, 3

_NO_UNROLL = "#llvm.loop_annotation<unroll = <disable = true>>"


def _no_unroll(iv):
    """Keep the scf.for that yields iv rolled through Peano's opt.

    Unrolled 16 times, the loop repeats the same buffer addresses as call
    arguments in every copy. MLIR drops a malformed annotation without an
    error: check the call count in the core's opted_*.ll.
    """
    iv.owner.owner.attributes["loop_annotation"] = Attribute.parse(_NO_UNROLL)


def grid(dev):
    """Columns and compute rows of the array."""
    rows = sum(
        dev.get_tile_type(0, r) == AnyComputeTile.tile_type for r in range(dev.rows)
    )
    return dev.cols, rows


def _ping_pong(b0, b1, acq, rel, **bd_args):
    """Two BDs that alternate between b0 and b1 behind one lock pair."""
    return [
        Bd(b, acquires=[Acquire(acq)], releases=[Release(rel)], next=nxt, **bd_args)
        for b, nxt in ((b0, 1), (b1, 0))
    ]


def attn(dev, max_context, num_heads, num_kv_heads, trace_size=0):
    """Prefill attention over a KV cache of up to max_context rows.

    O and Q hold one row of num_heads heads per query token, from token
    L_begin on. KV holds all K rows, then all V rows, max_l rows each; a row
    holds num_kv_heads heads. The sequence takes L_begin, L_end and max_l at
    dispatch. L_begin and L_end must be multiples of 128.
    """
    COLS, ROWS = grid(dev)
    HEADS = num_heads
    KV_D = num_kv_heads
    GQA = HEADS // KV_D

    bf16 = np.dtype[bfloat16]
    f32 = np.dtype[np.float32]

    q_ty = np.ndarray[(LQ_CT, DH), bf16]
    in_ty = np.ndarray[(LK, DH), bf16]
    in_mem_ty = np.ndarray[(LK_MT, DH), bf16]
    o_ty = np.ndarray[(64,), bf16]
    q_half_ty = np.ndarray[(LQ_MT, DH), bf16]
    o_col_ty = np.ndarray[(LQ * 4, DH), bf16]
    s_ty = np.ndarray[(LQ, LK_MT), bf16]
    m_ty = np.ndarray[(LQ, LK), bf16]
    y_ty = np.ndarray[(LQ, DH), f32]
    l_bf16_ty = np.ndarray[(LQ,), bf16]
    mv_ty = np.ndarray[(LQ,), bf16]
    cv_ty = np.ndarray[(LQ,), f32]
    L_ty = np.ndarray[(8,), np.dtype[np.int32]]

    qdims = [(LQ_CT // 8, 8 * DH), (DH // 8, 8), (8, DH), (8, 1)]
    odims = [(LQ // 8, 8 * DH), (DH // 8, 8), (8, DH), (8, 1)]
    kvdims = [(LK_MT // LK, LK * DH), (LK, 8), (64, 64), (8, 1)]

    def k(name, arg_types):
        return Kernel(name, KERNEL_OBJECT, arg_types)

    k_rounds = k("attn_rounds", [L_ty, L_ty, L_ty])
    k_round_begin = k("attn_round_begin", [mv_ty, mv_ty, cv_ty, cv_ty, y_ty])
    k_blocks = k("attn_blocks", [L_ty, np.int32, L_ty])
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

    # Shim row 0, memtile row 1, compute rows from 2. The memtiles need their
    # type: an untyped tile lowers its DMA to a core tile's aie.mem.
    IT = [Tile(j, 0, tile_type=dev.get_tile_type(j, 0)) for j in range(COLS)]
    MT = [Tile(j, 1, tile_type=dev.get_tile_type(j, 1)) for j in range(COLS)]
    CT = [
        [Tile(j, i + 2, tile_type=dev.get_tile_type(j, i + 2)) for j in range(COLS)]
        for i in range(ROWS)
    ]

    def sequence(o, q, kv, lb_arg, le_arg, max_l_arg, o_shim, q_shims, rtps):
        q_shim = dict(zip(q_keys, q_shims))
        max_l = _as_i32(max_l_arg)
        kv_cache_half = max_l * (DH * KV_D)
        L_begin = _as_i32(lb_arg)
        L_end = _as_i32(le_arg)
        rounds = arith.divsi(
            L_end - L_begin + (DATA_PER_ROUND - 1), _as_i32(DATA_PER_ROUND)
        )

        # Causal attention: the window reaches back to token 0.
        for lb, le, ws in rtps:
            lb[0] = L_begin
            le[0] = L_end
            ws[0] = L_end
        for lock in go.values():
            set_lock_value(lock.op, HEADS // NUM_CU)

        for head in range(HEADS // NUM_CU):
            for rnd in range_(rounds):
                r = arith.index_cast(T.i32(), rnd)
                kv_length = r * DATA_PER_ROUND + (L_begin + DATA_PER_ROUND)
                o_tasks, q_tasks, kv_tasks = [], [], []
                for cu in range(NUM_CU):
                    head_off = head * NUM_CU + cu
                    for col in range(4):
                        o_tasks.append(
                            o_shim[cu * 4 + col].drain(
                                o,
                                sizes=[1, 1, 4 * LK, DH],
                                strides=[0, 0, DH * HEADS, 1],
                                offset=r * (DATA_PER_ROUND * DH * HEADS)
                                + (head_off * DH + col * LK * 4 * DH * HEADS),
                                transfer_len=4 * LK * DH,
                                wait=True,
                                managed=False,
                            )
                        )
                    q_base = r * (DATA_PER_ROUND * DH * HEADS) + head_off * DH
                    for qi, key in enumerate(
                        ((cu * 4, 0), (cu * 4, 1), (cu * 4 + 3, 0), (cu * 4 + 3, 1))
                    ):
                        q_tasks.append(
                            q_shim[key].fill(
                                q,
                                sizes=[1, 1, LK * 4, DH],
                                strides=[0, 0, DH * HEADS, 1],
                                offset=q_base + qi * LK * 4 * DH * HEADS,
                                transfer_len=LK * 4 * DH,
                                wait=False,
                                managed=False,
                            )
                        )
                # An i32 transfer_len: derived from the i64 size product, it
                # does not fit dma_bd's operand.
                kv_rows = arith.extsi(T.i64(), arith.divsi(kv_length, _as_i32(128)))
                kv_head = head // (GQA // NUM_CU)
                k_base = max_l * ((kv_head // KV_D) * DH * KV_D) + (kv_head % KV_D) * DH
                for symbol, offset in (
                    ("k_in", k_base),
                    ("v_in", k_base + kv_cache_half),
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

    # RTPs, one set per core: the sequence writes the token range into them.
    rtp = {}
    for i in range(ROWS):
        for j in range(COLS):
            t = CT[i][j]
            rtp[(i, j)] = [
                Buffer(
                    type=L_ty,
                    name=f"{key}_attn_core_{t.row}_{t.col}",
                    tile=t,
                    use_write_rtp=True,
                    address=L1[key],
                )
                for key in ("L_begin", "L_end", "window_size")
            ]

    # A core that has finished one dispatch loops back and reads the RTPs at
    # once, before the next dispatch writes them. So the sequence sets go once
    # it has written them, to the number of passes a dispatch makes, and a core
    # takes one before each read.
    go = {
        (i, j): Lock(tile=CT[i][j], init=0, name=f"go_{CT[i][j].row}_{CT[i][j].col}")
        for i in range(ROWS)
        for j in range(COLS)
    }

    # o: one fifo per column, joined in memtile m from four cores. Memtile m
    # takes rows 0 and 1 when m is even and rows 2 and 3 when m is odd, over
    # columns 2*(m//2) and 2*(m//2)+1.
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

    # q: the mirror of o. Memtiles 4j and 4j+3 each take two halves on two
    # channels. Each half splits into two cores' slices, each broadcast to the
    # two columns the memtile serves. Half 0 feeds rows 0 and 1.
    q_shim, q_cons = {}, {}
    for j in range(COLS // 4):
        for mt_idx, cols in (
            (j * 4, (j * 4, j * 4 + 1)),
            (j * 4 + 3, (j * 4 + 2, j * 4 + 3)),
        ):
            for half, rows in ((0, (0, 1)), (1, (2, 3))):
                of_q = ObjectFifo(q_half_ty, name=f"q{mt_idx}_{half}", depth=2)
                q_shim[(mt_idx, half)] = of_q.prod(tile=IT[mt_idx], channel=half)
                slices = of_q.cons().split(
                    [LQ_CT * DH * t for t in range(2)],
                    obj_types=[q_ty] * 2,
                    names=[f"q{mt_idx}_{half}_{t}" for t in range(2)],
                    dims_to_stream=[qdims] * 2,
                    depths=[1, 1],
                    tile=MT[mt_idx],
                )
                for t, row in enumerate(rows):
                    for col in cols:
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
            [rtp[(i, j)] for i in range(ROWS) for j in range(COLS)],
        ],
    )

    def make_core_fn(row, col):
        def core_fn(
            o_h,
            q_h,
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
            nb,
            lb,
            le,
            ws,
            n_buf,
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
                blocks_k(lb, i, nb)
                for b in range_(nb[0]):
                    block_begin_k(m, prev_m)
                    for j in range_(16):
                        _no_unroll(j)
                        qk_k(s, q, in0, in1, m, lb, ws, row, col, i, b, j)
                    block_mid_k(s, m, new_m, prev_m, cbuf, lbuf, y)
                    for j in range_(16):
                        _no_unroll(j)
                        fv_k(y, s, in0, in1, j)
                    block_end_k(prev_m, new_m)
                finalize_k(lbuf, l_bf16)
                for c in range_(DH // 8):
                    o = o_h.acquire(1)
                    epilogue_k(o, l_bf16, y, c)
                    o_h.release(1)
                q_h.release(1)

        return core_fn

    workers = []
    for j in range(COLS):
        for i in range(ROWS):
            tile = CT[i][j]
            name = f"{tile.row}_{tile.col}"

            def buf(ty, key, **kw):
                return Buffer(type=ty, name=f"{key}_{name}", tile=tile, **kw)

            in_0 = buf(in_ty, "in_0", address=L1["in_0"])
            in_1 = buf(in_ty, "in_1", address=L1["in_1"])
            core_bufs = [
                in_0,
                in_1,
                buf(s_ty, "s", address=L1["s"]),
                buf(m_ty, "m", address=L1["m"]),
                buf(y_ty, "y", address=L1["y"]),
                buf(l_bf16_ty, "l_bf16"),
                buf(mv_ty, "prev_m"),
                buf(mv_ty, "new_m"),
                buf(cv_ty, "c"),
                buf(cv_ty, "l"),
                buf(L_ty, "n_blocks"),
            ]
            n_rounds = buf(L_ty, "n_rounds", address=L1["n_rounds"])
            in_prod = Lock(tile=tile, lock_id=IN_PROD_LOCK, init=2)
            in_cons = Lock(tile=tile, lock_id=IN_CONS_LOCK, init=0)
            rt.add_lock(in_prod)
            rt.add_lock(in_cons)
            rt.add_lock(go[(i, j)])
            workers.append(
                Worker(
                    make_core_fn(i, j & 0x3),
                    [o_prod[(i, j)].prod(), q_cons[(i, j)].cons()]
                    + core_bufs
                    + rtp[(i, j)]
                    + [
                        n_rounds,
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
                        go[(i, j)],
                    ],
                    tile=tile,
                    while_true=True,
                    stack_size=STACK_SIZE,
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
                            _ping_pong(in_0, in_1, in_prod, in_cons),
                        )
                    ],
                )
            )

    # Memtile 4j+2 takes k and v on two channels and sends them out
    # interleaved on one. Memtile 4j+1 holds half of the buffers.
    for j in range(COLS // 4):
        mt, mt_left = MT[j * 4 + 2], MT[j * 4 + 1]
        bufs = {
            (side, n): Buffer(type=in_mem_ty, name=f"in_{n}_0_{tile.col}", tile=tile)
            for side, tile in (("own", mt), ("left", mt_left))
            for n in (0, 1)
        }
        # The left pair's locks sit on mt too.
        left_prod = Lock(tile=mt, lock_id=0, init=2)
        left_cons = Lock(tile=mt, lock_id=1, init=0)
        own_prod = Lock(tile=mt, lock_id=7, init=2)
        own_cons = Lock(tile=mt, lock_id=8, init=0)
        for lock in (left_prod, left_cons, own_prod, own_cons):
            rt.add_lock(lock)
        fill = dict(
            offset=0,
            length=LK_MT * DH,
            sizes=[d[0] for d in kvdims],
            strides=[d[1] for d in kvdims],
        )

        def out(b, cons, prod, nxt):
            return Bd(b, acquires=[Acquire(cons)], releases=[Release(prod)], next=nxt)

        rt.add_tile_dma(
            TileDma(
                mt,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        0,
                        _ping_pong(
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
                        _ping_pong(
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
        # An empty program, so the placer keeps mt_left and its buffers.
        rt.add_tile_dma(TileDma(mt_left, []))

    rt.add_flow(Flow(IT[2], MT[2], src_channel=0, dst_channel=0, shim_symbol="k_in"))
    rt.add_flow(Flow(IT[2], MT[2], src_channel=1, dst_channel=1, shim_symbol="v_in"))
    for j in range(COLS):
        for i in range(ROWS):
            rt.add_flow(Flow(MT[2], CT[i][j], src_channel=0, dst_channel=1))

    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
