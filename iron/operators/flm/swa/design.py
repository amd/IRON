# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sliding-window causal prefill attention with a head dim of 256, on the whole array.

Four pairs of columns each take one query head per pass. A round covers 128 query
rows: each of a pair's 8 cores takes 16 of them and streams past them every
key inside the window up to the round's last row. k and v come from one shim
tile and reach every core through one memtile. The runtime sequence takes the
token range and the KV cache's row count at dispatch, so one build serves
every prompt.
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
from aie.iron.device import AnyComputeTile, Tile

from iron.common.device_utils import call_factory

DH = 256  # head dim
LQ = 16  # query rows per core
LK = 16  # key rows per step
LK_MT = 128  # key rows per memtile buffer
LQ_MT = 64  # query rows per memtile fifo half
LQ_CT = 32  # query rows per core's q object, two cores' worth
NUM_CU = 4  # column pairs
DATA_PER_ROUND = LQ * 8  # query rows per round

# The buffer addresses of the FastFlowLM overlay. The stack grows up from 0 to
# in_1, the lowest buffer.
L1 = {
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
}
STACK_SIZE = L1["in_1"]

# The k/v DMA and the kernel's steps synchronize on these locks of each core.
IN_PROD_LOCK, IN_CONS_LOCK = 2, 3


def swa_kernel(device=None):
    """The flm_gemma4_swa_prefill build this design's cores link."""
    return call_factory(
        kernels.flm_gemma4_swa_prefill,
        device=device,
        in_prod_lock=IN_PROD_LOCK,
        in_cons_lock=IN_CONS_LOCK,
    )


def _no_unroll(iv):
    """Keep the scf.for that yields iv rolled through Peano's opt.

    Unrolled, the loop repeats the same buffer addresses as call arguments in
    every copy. MLIR drops a malformed annotation without an error: check the
    call count in the core's opted_*.ll.
    """
    iv.owner.owner.attributes["loop_annotation"] = Attribute.parse(
        "#llvm.loop_annotation<unroll = <disable = true>>"
    )


def grid(dev):
    """Columns and compute rows of the array."""
    rows = sum(
        dev.get_tile_type(0, r) == AnyComputeTile.tile_type for r in range(dev.rows)
    )
    return dev.cols, rows


def _ping_pong(b0, b1, acq, rel, acq_val=1, rel_val=1, **bd_args):
    """Two BDs that alternate between b0 and b1 behind one lock pair."""
    return [
        Bd(
            b,
            acquires=[Acquire(acq, value=acq_val)],
            releases=[Release(rel, value=rel_val)],
            next=nxt,
            **bd_args,
        )
        for b, nxt in ((b0, 1), (b1, 0))
    ]


def swa(dev, max_context, num_heads, num_kv_heads, window, trace_size=0):
    """Sliding-window prefill attention over a KV cache of up to max_context rows.

    O and Q hold one row of num_heads heads per query token, from token
    L_begin on. KV holds all K rows, then all V rows, max_l rows each. A KV
    row holds num_kv_heads heads. A query sees the window keys up to itself.
    """
    COLS, ROWS = grid(dev)
    HEADS = num_heads
    KV_D = num_kv_heads
    GQA = HEADS // KV_D

    bf16 = np.dtype[bfloat16]
    f32 = np.dtype[np.float32]

    q_ty = np.ndarray[(LQ_CT, DH), bf16]
    in_ty = np.ndarray[(LK, DH), bf16]
    in_mem_ty = np.ndarray[(LK_MT * 2, DH), bf16]
    o_ty = np.ndarray[(64,), bf16]
    o_col_ty = np.ndarray[(LQ * 4 * DH,), bf16]
    s_ty = np.ndarray[(LQ, LK_MT), bf16]
    m_ty = np.ndarray[(LQ, LK), bf16]
    m_col_ty = np.ndarray[(LQ,), bf16]
    cl_ty = np.ndarray[(LQ,), f32]
    y_ty = np.ndarray[(LQ, DH), f32]
    l_bf16_ty = np.ndarray[(LQ,), bf16]
    L_ty = np.ndarray[(8,), np.dtype[np.int32]]
    q_half_ty = np.ndarray[(LQ_MT, DH), bf16]

    odims = [(LQ // 8, 8 * DH), (DH // 8, 8), (8, DH), (8, 1)]
    qdims = [(LQ_CT // 8, 8 * DH), (DH // 8, 8), (8, DH), (8, 1)]

    # Shim row 0, memtile row 1, compute rows from 2. The memtiles need their
    # type: an untyped tile lowers its DMA to a core tile's aie.mem.
    IT = [Tile(j, 0, tile_type=dev.get_tile_type(j, 0)) for j in range(COLS)]
    MT = [Tile(j, 1, tile_type=dev.get_tile_type(j, 1)) for j in range(COLS)]
    CT = [
        [Tile(j, i + 2, tile_type=dev.get_tile_type(j, i + 2)) for j in range(COLS)]
        for i in range(ROWS)
    ]

    k = swa_kernel(dev).entry

    k_blocks = k("attn_blocks", [L_ty, L_ty, np.int32, L_ty])
    k_round_begin = k("attn_round_begin", [m_col_ty, m_col_ty, cl_ty, cl_ty, y_ty])
    k_block_begin = k("attn_block_begin", [m_ty, m_col_ty])
    k_qk = k(
        "attn_qk_step",
        [s_ty, q_ty, in_ty, in_ty, m_ty, L_ty, L_ty] + [np.int32] * 5,
    )
    k_block_mid = k(
        "attn_block_mid", [s_ty, m_ty, m_col_ty, m_col_ty, cl_ty, cl_ty, y_ty]
    )
    k_fv = k("attn_fv_step", [y_ty, s_ty, in_ty, in_ty, np.int32])
    k_block_end = k("attn_block_end", [m_col_ty, m_col_ty])
    k_finalize = k("attn_finalize", [cl_ty, l_bf16_ty])
    k_epilogue = k("attn_epilogue", [o_ty, l_bf16_ty, y_ty, np.int32])
    k_rounds = k("attn_rounds", [L_ty, L_ty, L_ty])

    # RTPs, one set per core, keyed by the tile's (row, col): the sequence
    # writes the token range and the window into them.
    rtp = {}
    # go orders each core's RTP read after the sequence's RTP write. A core
    # starts its next pass as soon as a dispatch ends, before the next dispatch
    # writes the RTPs. The sequence sets go to the number of passes after it
    # writes the RTPs. A core takes one count before each pass.
    go = {}

    def sequence(o, q, kv, lb_arg, le_arg, max_l_arg, o_shim, q_shims):
        q_shim = dict(zip(q_keys, q_shims))
        max_l = _as_i32(max_l_arg)
        kv_cache_half = max_l * (DH * KV_D)
        L_begin = _as_i32(lb_arg)
        L_end = _as_i32(le_arg)
        rounds = arith.divsi(
            L_end - L_begin + (DATA_PER_ROUND - 1), _as_i32(DATA_PER_ROUND)
        )

        for key in sorted(rtp):
            lb, le, ws = rtp[key]
            lb[0] = L_begin
            le[0] = L_end
            ws[0] = window
        for key in sorted(go):
            set_lock_value(go[key].op, HEADS // NUM_CU)

        def max0(v):
            # max(v, 0) without a branch: v & (v >> 31) is v when v < 0, else 0.
            return v - arith.andi(v, arith.shrsi(v, _as_i32(31)))

        for head in range(HEADS // NUM_CU):
            for rnd in range_(rounds):
                r = arith.index_cast(T.i32(), rnd)
                lq_current = L_begin + r * DATA_PER_ROUND
                kv_begin = max0(lq_current - _as_i32(window))
                kv_length = lq_current - kv_begin + _as_i32(DATA_PER_ROUND)

                o_tasks, q_tasks = [], []
                for cu in range(NUM_CU):
                    head_off = head * NUM_CU + cu
                    for col in range(2):
                        o_tasks.append(
                            o_shim[cu * 2 + col].drain(
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
                    for half in range(2):
                        q_tasks.append(
                            q_shim[(cu, half)].fill(
                                q,
                                sizes=[1, 1, LK * 4, DH],
                                strides=[0, 0, DH * HEADS, 1],
                                offset=(
                                    q_base + LK * 4 * DH * HEADS if half else q_base
                                ),
                                transfer_len=LK * 4 * DH,
                                wait=False,
                                managed=False,
                            )
                        )

                # dma_bd's length operand is an i32. The product of the i64
                # sizes does not fit it, so transfer_len gives the length.
                kv_rows = arith.extsi(T.i64(), arith.divsi(kv_length, _as_i32(128)))
                kv_head = head // (GQA // NUM_CU)
                const_off = (
                    max_l * ((kv_head // KV_D) * DH * KV_D) + (kv_head % KV_D) * DH
                )
                k_off = const_off + kv_begin * _as_i32(DH * KV_D)

                kv_tasks = []
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

    # o: one fifo per column, joined in memtile j from four cores. Memtile j
    # takes rows 0 and 1 when j is even and rows 2 and 3 when j is odd, over
    # columns 2*(j//2) and 2*(j//2)+1.
    o_shim, o_prod = [], {}
    for j in range(COLS):
        of_o = ObjectFifo(o_col_ty, name=f"o{j}", depth=2)
        o_shim.append(of_o.cons(tile=IT[j], channel=0))
        sub = of_o.prod().join(
            [LQ * DH * i for i in range(4)],
            obj_types=[o_ty] * 4,
            names=[f"o{j}_{i}" for i in range(4)],
            dims_from_stream=[odims] * 4,
            tile=MT[j],
        )
        base_row = 0 if j & 0x1 == 0 else 2
        for c in range(4):
            o_prod[(base_row + c // 2, 2 * (j // 2) + (c & 0x1))] = sub[c]

    # q: the mirror of o. Even memtile 2p takes two 64-row halves on two
    # channels. Each half splits into two 32-row core slices, each broadcast
    # to both columns of the pair. Half 0 feeds rows 0 and 1.
    q_shim, q_cons = {}, {}
    for p in range(COLS // 2):
        mt = MT[2 * p]
        for half, rows in ((0, (0, 1)), (1, (2, 3))):
            of_q = ObjectFifo(q_half_ty, name=f"q{2 * p}_{half}", depth=2)
            q_shim[(p, half)] = of_q.prod(tile=IT[2 * p], channel=half)
            slices = of_q.cons().split(
                [LQ_CT * DH * s for s in range(2)],
                obj_types=[q_ty] * 2,
                names=[f"q{2 * p}_{half}_{s}" for s in range(2)],
                dims_to_stream=[qdims] * 2,
                depths=[1, 1],
                tile=mt,
            )
            for s, row in enumerate(rows):
                for col in (2 * p, 2 * p + 1):
                    q_cons[(row, col)] = slices[s]
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
            blocks_k,
            round_begin_k,
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
                blocks_k(lb, ws, i, nb)
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
                q_h.release(1)
                for c in range_(LQ * DH // 64):
                    o = o_h.acquire(1)
                    epilogue_k(o, l_bf16, y, c)
                    o_h.release(1)

        return core_fn

    workers = []
    for j in range(COLS):
        for i in range(ROWS):
            tile = CT[i][j]
            name = f"{tile.row}_{tile.col}"

            def buf(ty, key, **kw):
                return Buffer(type=ty, name=f"{key}_{name}", tile=tile, **kw)

            rtp_bufs = [
                buf(L_ty, f"{key}_attn_core", use_write_rtp=True, address=L1[key])
                for key in ("L_begin", "L_end", "window_size")
            ]
            rtp[(tile.row, tile.col)] = rtp_bufs
            in_0 = buf(in_ty, "in_0", address=L1["in_0"])
            in_1 = buf(in_ty, "in_1", address=L1["in_1"])
            pinned = [
                buf(s_ty, "s", address=L1["s"]),
                buf(m_ty, "m", address=L1["m"]),
                buf(y_ty, "y", address=L1["y"]),
                buf(l_bf16_ty, "l_bf16", address=L1["l_bf16"]),
            ]
            n_rounds = buf(L_ty, "n_rounds", address=L1["n_rounds"])
            in_prod = Lock(tile=tile, lock_id=IN_PROD_LOCK, init=2)
            in_cons = Lock(tile=tile, lock_id=IN_CONS_LOCK, init=0)
            rt.add_lock(in_prod)
            rt.add_lock(in_cons)
            state = [
                buf(m_col_ty, "prev_m"),
                buf(m_col_ty, "new_m"),
                buf(cl_ty, "c"),
                buf(cl_ty, "l"),
            ]
            n_blocks = buf(L_ty, "n_blocks")
            go_lock = Lock(tile=tile, init=0, name=f"go_{name}")
            go[(tile.row, tile.col)] = go_lock
            rt.add_lock(go_lock)
            workers.append(
                Worker(
                    make_core_fn(i, j & 0x1),
                    [q_cons[(i, j)].cons(), o_prod[(i, j)].prod(), in_0, in_1]
                    + pinned
                    + state
                    + rtp_bufs
                    + [
                        n_rounds,
                        n_blocks,
                        k_rounds,
                        k_blocks,
                        k_round_begin,
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

    # Odd memtiles stage k and v in one buffer pair: k in the first half, v in
    # the second. Each input channel releases one of two counts. The output
    # acquires both, so it reads a buffer once both halves hold data.
    for j in range(1, COLS, 2):
        mt = MT[j]
        in_0 = Buffer(type=in_mem_ty, name=f"in_0_0_{mt.col}", tile=mt)
        in_1 = Buffer(type=in_mem_ty, name=f"in_1_0_{mt.col}", tile=mt)
        prod = Lock(tile=mt, lock_id=0, init=4)
        cons = Lock(tile=mt, lock_id=1, init=0)
        rt.add_lock(prod)
        rt.add_lock(cons)
        indims = [(LK_MT // LK, LK * DH), (LK, 8), (32, 128), (8, 1)]
        outdims = [(2 * LK_MT // LK, LK * DH), (LK, DH), (DH, 1)]
        half = LK_MT * DH

        def dims(d):
            return dict(sizes=[x[0] for x in d], strides=[x[1] for x in d])

        rt.add_tile_dma(
            TileDma(
                mt,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        0,
                        _ping_pong(
                            in_0,
                            in_1,
                            prod,
                            cons,
                            offset=0,
                            length=half,
                            **dims(indims),
                        ),
                    ),
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        1,
                        _ping_pong(
                            in_0,
                            in_1,
                            prod,
                            cons,
                            offset=half,
                            length=half,
                            **dims(indims),
                        ),
                    ),
                    DmaChannel(
                        DMAChannelDir.MM2S,
                        0,
                        _ping_pong(
                            in_0,
                            in_1,
                            cons,
                            prod,
                            acq_val=2,
                            rel_val=2,
                            offset=0,
                            length=2 * half,
                            **dims(outdims),
                        ),
                    ),
                ],
            )
        )

    rt.add_flow(Flow(IT[3], MT[3], src_channel=0, dst_channel=0, shim_symbol="k_in"))
    rt.add_flow(Flow(IT[3], MT[3], src_channel=1, dst_channel=1, shim_symbol="v_in"))
    for j in range(COLS):
        for i in range(ROWS):
            rt.add_flow(Flow(MT[3], CT[i][j], src_channel=0, dst_channel=1))

    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
