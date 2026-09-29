# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's fused decode layer on the whole array: one token through one layer.

One core per stage: RMS norm and residual, RoPE for the global and the
sliding-window layers, 16 q4nx projection cores, GLU, the per-layer-input
path, and one attention pair (qk and kv) for each attention kind. One xclbin
serves the four layer types. The runtime sequence writes the layer type into
RTPs, then streams the weights, the KV cache and the hidden state. The
layer's context length and the KV cache's row count are dispatch parameters.

The runtime sequence is FastFlowLM's gen_layer_seq. It writes the RTPs at
fixed addresses, ``RTP_ADDRESSES``.
"""

from enum import IntEnum

import numpy as np
from ml_dtypes import bfloat16

from aie.dialects import arith
from aie.dialects.aie import DMAChannelDir
from aie.dialects.aiex import (
    _as_i32,
    dma_await_task,
    dma_free_task,
    dma_start_task,
    npu_write32,
    shim_dma_single_bd_task,
)
from aie.extras import types as T
from aie.extras.dialects.arith import constant
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
from aie.iron.dataflow import Flow, PacketFlow
from aie.iron.device import Tile

from iron.common.device_utils import call_factory

LAYER_TYPES = ("global", "swa", "global_skip", "swa_skip")

# Rows of the KV cache the runtime sequence's buffer types allow for. The
# sequence takes the real row count, max_l, at dispatch.
MAX_CONTEXT = 32768
SLIDING_WINDOW = 512

# The L1 address of each RTP, per model: FastFlowLM's address book, which the
# runtime sequence writes. The design pins every RTP buffer at its address:
# the allocator places four of them elsewhere, and the sequence's writes to
# those addresses then land in other buffers.
RTP_ADDRESSES = {
    "GEMMA4_E2B": {
        "l_qk": 57344,
        "l_kv": 14976,
        "swa_l_qk": 9216,
        "swa_l_kv": 40960,
        "proj_swa": 33280,
        "proj_skip": 49664,
        "rms_swa": 52224,
        "rms_skip": 25600,
        "rope_skip_kv": 33792,
        "swa_rope_skip_kv": 33280,
        "glu_skip": 34816,
    },
    "GEMMA4_E4B": {
        "l_qk": 57344,
        "l_kv": 14976,
        "swa_l_qk": 53248,
        "swa_l_kv": 57664,
        "proj_swa": 33280,
        "proj_skip": 49664,
        "rms_swa": 55328,
        "rms_skip": 55392,
        "rope_skip_kv": 34816,
        "swa_rope_skip_kv": 33792,
        "glu_skip": 30720,
    },
}

# The symbol of each RTP buffer, by RTP_ADDRESSES key. Each projection core
# has its own pair, so proj_swa and proj_skip have none here.
RTP_SYMBOLS = {
    "rms_swa": "RTP_RMS_IS_SWA_BUFFER",
    "rms_skip": "RTP_RMS_SKIP_BUFFER",
    "rope_skip_kv": "RTP_RoPE_SKIP_KV_4_3",
    "swa_rope_skip_kv": "RTP_SWA_RoPE_SKIP_KV_5_3",
    "glu_skip": "RTP_GLU_IS_SKIP_3_3",
    "l_qk": "RTP_L_attn_qk_core_2_2",
    "l_kv": "RTP_L_attn_kv_core_3_2",
    "swa_l_qk": "RTP_L_swa_attn_qk_core_4_2",
    "swa_l_kv": "RTP_L_swa_attn_kv_core_5_2",
}

# One q4nx weight block: 32 rows by 256 columns at 5 bits a weight.
Q4_M, Q4_K = 32, 256
Q4_BLOCK_BYTES = Q4_M * Q4_K * 5 // 8
# The q4nx block in bf16 elements, the unit the weight buffers are typed in.
W_BLOCK = Q4_BLOCK_BYTES // 2
# One bf16 weight block of the per-layer-input projections.
BF16_W_BLOCK = 32 * 256
# The projections' input slice. Every projection's input dim is a multiple.
X_SLICE = 256
# Keys per attention round.
LK = 16
# Each KV head's query group rounds up to a multiple of this many heads.
Q_HEADS_PADDING = 4
# The padding in the engine's per-layer-input stream (gemma4e_npu_sequence.hpp).
MIN_BF16_PAD = 32
PROJ_COLS = (0, 1, 6, 7)

# Core locks, by the name of the factory argument that tells the kernel its id.
RMS_LOCKS = dict(
    w_prod_lock=0,
    w_cons_lock=1,
    y_prod_lock=2,
    y_cons_lock=3,
    x_prod_lock=4,
    x_cons_lock=5,
    rtp_available_lock=6,
    lm_head_out_prod_lock=7,
    lm_head_out_cons_lock=8,
)
ROPE_LOCKS = dict(
    qkv_prod_lock=0,
    qkv_cons_lock=1,
    k_prod_lock=4,
    k_cons_lock=5,
    v_prod_lock=6,
    v_cons_lock=7,
    rope_prod_lock=8,
    rope_cons_lock=9,
)
ROPE_Q_PASS_LOCK = 10
PLE_LOCKS = dict(
    norm_w_prod_lock=0,
    x0_per_layer_prod_lock=1,
    x0_prod_lock=2,
    xw_cons_lock=3,
    proj_w_prod_lock=4,
    proj_w_cons_lock=5,
    y_prod_lock=6,
    y_cons_lock=7,
)
# The DMA's second norm_w leg, which no kernel takes.
PLE_NORM_W_P2_LOCK = 8
# final_x_* are locks of the RMS tile, to the left of the gate tile.
GLE_LOCKS = dict(
    x_prod_lock=0,
    x_cons_lock=1,
    proj_w_prod_lock=2,
    proj_w_cons_lock=3,
    y_prod_lock=4,
    y_cons_lock=5,
    final_x_prod_lock=RMS_LOCKS["lm_head_out_prod_lock"],
    final_x_cons_lock=RMS_LOCKS["lm_head_out_cons_lock"],
)
PLU_LOCKS = dict(
    x_prod_lock=0,
    x_cons_lock=1,
    proj_w_prod_lock=2,
    proj_w_cons_lock=3,
    y_prod_lock=4,
    y_cons_lock=5,
)
GLU_LOCKS = dict(x_prod_lock=0, x_cons_lock=1, y_prod_lock=2, y_cons_lock=3, rtp_lock=6)
PROJ_LOCKS = dict(
    x_prod_lock=0,
    x_cons_lock=1,
    w_prod_lock=2,
    w_cons_lock=3,
    y_prod_ping_lock=4,
    y_prod_pong_lock=5,
    rtp_available_lock=6,
    y_cons_ping_lock=7,
    y_cons_pong_lock=8,
)
# The qk core's lock 8 orders the kv core's RTP read after the qk core's.
ATTN_HANDSHAKE_LOCK = 8
ATTN_KV_LOCKS = dict(
    o_prod_lock=0,
    o_cons_lock=1,
    v_prod_lock=2,
    v_cons_lock=3,
    l_cons_lock=ATTN_HANDSHAKE_LOCK,
)
ATTN_QK_LOCKS = dict(k_prod_lock=2, k_cons_lock=3)

# The lock the RMS, GLU and projection cores acquire before they read their
# RTPs. The sequence sets it once it has written them. A core tile's lock n
# sits at 0x1F000 + 16 * n.
RTP_SYNC_LOCK = PROJ_LOCKS["rtp_available_lock"]
assert RTP_SYNC_LOCK == RMS_LOCKS["rtp_available_lock"] == GLU_LOCKS["rtp_lock"]
RTP_SYNC_LOCK_ADDR = 0x1F000 + 16 * RTP_SYNC_LOCK


class _ShimPkt(IntEnum):
    """Packet ids of the shim streams into the RMS and RoPE tiles."""

    to_rms = 0
    to_rope = 1


class _ProjPkt(IntEnum):
    """Packet ids of the projection output, one per consumer."""

    to_rope = 1
    to_swa_rope = 2
    to_rms = 4
    to_glu = 8


# Packet ids into the projection engine's x input.
_X_FROM_RMS = 0
_X_FROM_ATTN = 0
_X_FROM_GLU = 22
# Packet ids of the KV cache streams into the attention memtile.
_KV_PKT_GLOBAL = 12
_KV_PKT_SWA = 13


def layer_kernels(geometry, device=None):
    """The flm_decode_* builds this design's cores link, by the kernel's symbol.

    The global attention kernels build for the geometry's KV head count.
    """
    two_kv = geometry.num_kv_heads == 2
    qk_handshake = "l_prod_lock" if two_kv else "l_cons_lock"

    def build(factory, locks):
        return call_factory(factory, device=device, geometry=geometry, **locks)

    attn_qk_locks = {**ATTN_QK_LOCKS, qk_handshake: ATTN_HANDSHAKE_LOCK}
    swa_qk_locks = {**ATTN_QK_LOCKS, "l_cons_lock": ATTN_HANDSHAKE_LOCK}
    return {
        "rms_residual": build(kernels.flm_decode_rms_residual, RMS_LOCKS),
        "rope": build(kernels.flm_decode_rope, ROPE_LOCKS),
        "swa_rope": build(kernels.flm_decode_swa_rope, ROPE_LOCKS),
        "proj_layer_embedding": build(
            kernels.flm_decode_proj_layer_embedding, PLE_LOCKS
        ),
        "gate_layer_embedding": build(
            kernels.flm_decode_gate_layer_embedding, GLE_LOCKS
        ),
        "per_layer_up": build(kernels.flm_decode_per_layer_up, PLU_LOCKS),
        "glu": build(kernels.flm_decode_glu, GLU_LOCKS),
        "proj_main": build(kernels.flm_decode_proj_main, PROJ_LOCKS),
        "attn_kv": build(
            (kernels.flm_decode_attn_kv_kvh2 if two_kv else kernels.flm_decode_attn_kv),
            ATTN_KV_LOCKS,
        ),
        "attn_qk": build(
            (kernels.flm_decode_attn_qk_kvh2 if two_kv else kernels.flm_decode_attn_qk),
            attn_qk_locks,
        ),
        "swa_attn_kv": build(kernels.flm_decode_swa_attn_kv, ATTN_KV_LOCKS),
        "swa_attn_qk": build(kernels.flm_decode_swa_attn_qk, swa_qk_locks),
    }


def q_heads_padded(geometry):
    """Query heads per attention core, each KV head's group padded."""
    groups = geometry.num_attn_heads // geometry.num_kv_heads
    pad = Q_HEADS_PADDING
    return (groups + pad - 1) // pad * pad * geometry.num_kv_heads


def arg_sizes(geometry):
    """Elements of the sequence's buffers: x, proj, rms, rope_rms and kv.

    The engine binds its own buffers. These sizes bound what the sequence
    reads and writes.
    """
    D, pli, inter = geometry.model_dim, geometry.pli_d, geometry.intermediate_size
    dq = geometry.num_attn_heads * geometry.dh
    dk = geometry.num_kv_heads * geometry.dh
    proj = (
        (dq + 2 * dk) * D * 5 // 8 // 2
        + dq * D * 5 // 8 // 2
        + 2 * inter * D * 5 // 8 // 2
        + 3 * pli * D
    )
    return {
        "x": 3 * D,
        "proj": proj,
        "rms": 4 * D,
        "rope_rms": 3 * geometry.dh + pli * 2 + D + 64,
        "kv": 2 * dk * MAX_CONTEXT,
    }


def _ping_pong(
    b0,
    b1,
    acq,
    rel,
    *,
    offset=0,
    length=None,
    dimensions=None,
    acq_val=1,
    rel_val=1,
    packet=None,
):
    """Two BDs that alternate between b0 and b1 behind one lock pair.

    ``dimensions`` is a list of (size, stride), outermost first.
    """
    sizes = [d[0] for d in dimensions] if dimensions else []
    strides = [d[1] for d in dimensions] if dimensions else []
    common = dict(
        offset=offset, length=length, sizes=sizes, strides=strides, packet=packet
    )
    return [
        Bd(
            b,
            **common,
            acquires=[Acquire(acq, value=acq_val)],
            releases=[Release(rel, value=rel_val)],
            next=nxt,
        )
        for b, nxt in ((b0, 1), (b1, 0))
    ]


def _connect(rt, src, src_ch, dst, dst_ch, pkt_id=-1, keep_pkt_header=False):
    """A circuit-switched flow, or a packet flow when pkt_id >= 0."""
    if pkt_id < 0:
        rt.add_flow(Flow(src, dst, src_channel=src_ch, dst_channel=dst_ch))
    else:
        rt.add_flow(
            PacketFlow(
                pkt_id,
                src,
                dst,
                src_channel=src_ch,
                dst_channel=dst_ch,
                keep_pkt_header=keep_pkt_header,
            )
        )


def decode_layer(dev, geometry, rtp, layer_type, sliding_window=SLIDING_WINDOW):
    """The decode layer of ``layer_type`` for ``geometry``.

    ``rtp`` maps each RTP_ADDRESSES key to the address the engine writes.
    ``layer_type`` sets what the sequence streams and writes into the RTPs;
    the device configuration is the same for every type. The sequence takes
    x, proj, rms, rope_rms and kv, then the context length and max_l, the
    KV cache's row count.
    """
    if layer_type not in LAYER_TYPES:
        raise ValueError(f"layer_type must be one of {LAYER_TYPES}")
    if sliding_window & (sliding_window - 1):
        raise ValueError(
            f"sliding_window ({sliding_window}) must be a power of two: the "
            "sequence takes the remainder by it with a mask"
        )
    g = geometry
    total_cols = dev.cols
    IS_SWA = layer_type in ("swa", "swa_skip")
    IS_SKIP = layer_type in ("global_skip", "swa_skip")
    D = g.model_dim
    NUM_KV = g.num_kv_heads
    G_DQ, G_DK = g.num_attn_heads * g.dh, NUM_KV * g.dh
    S_DQ, S_DK = g.num_attn_heads * g.swa_dh, NUM_KV * g.swa_dh
    PLI_D = g.pli_d
    NQ_PADDED = q_heads_padded(g)
    two_kv = NUM_KV == 2

    kernel_fns = layer_kernels(g, dev)

    def k(name, symbol, arg_types):
        return kernel_fns[name].object_file.bind(symbol, arg_types)

    def sequence(x_arg, proj_arg, rms_arg, rope_rms_arg, kv_arg, len_arg, max_l_arg):
        # The engine's gen_layer_seq: its RTP writes, then its shim DMA legs in
        # its order, in bf16 elements. The engine passes context_len; the
        # sequence works with the length after this token.
        L = _as_i32(len_arg) + 1
        MAX_L_v = _as_i32(max_l_arg)

        def _ceil_mul(v, chunk):
            # arith.divsi: `//` emits floordivsi, which the C++ generator
            # cannot lower.
            return arith.divsi(v + (chunk - 1), _as_i32(chunk)) * chunk

        DH = g.swa_dh if IS_SWA else g.dh
        DQ = S_DQ if IS_SWA else G_DQ
        DK = S_DK if IS_SWA else G_DK
        DV = DK
        INTERMEDIATE = (
            g.intermediate_size * 2
            if IS_SKIP and g.double_wide_mlp
            else g.intermediate_size
        )
        L_CHUNK = 16

        # The engine's weight blob, in bf16 elements. A skip layer shares
        # another layer's KV cache and has no k or v projection.
        def q4b(dout, din):
            return dout * din * 5 // 8

        w = 0
        qkv_off = w // 2
        w += q4b(DQ, D)
        if not IS_SKIP:
            w += q4b(DK, D) + q4b(DV, D)
        o_off = w // 2
        w += q4b(DQ, D)
        upgate_off = w // 2
        w += q4b(2 * INTERMEDIATE, D)
        down_off = w // 2
        w += q4b(INTERMEDIATE, D)
        pli_down_off = w // 2
        w += PLI_D * D * 2
        pli_gate_off = w // 2
        w += PLI_D * D * 2
        pli_up_off = w // 2

        # RTPs, then the sync lock that lets the proj, RMS and GLU cores read
        # them.
        for c in PROJ_COLS:
            for r in (2, 3, 4, 5):
                npu_write32(rtp["proj_swa"], int(IS_SWA), column=c, row=r)
                npu_write32(rtp["proj_skip"], int(IS_SKIP), column=c, row=r)
                npu_write32(RTP_SYNC_LOCK_ADDR, 1, column=c, row=r)
        _SW = sliding_window

        # The C++ generator has no arith.minsi, so min and the masks are
        # branchless.
        def _mask_ge(v, bound):
            """All ones if v >= bound, else 0."""
            return arith.shrsi(_as_i32(bound - 1) - v, _as_i32(31))

        def _min_const(v, bound):
            d = v - _as_i32(bound)
            return _as_i32(bound) + arith.andi(d, arith.shrsi(d, _as_i32(31)))

        L_local = _min_const(L, _SW) if IS_SWA else L
        npu_write32(rtp["l_qk"], L_local, column=2, row=2)
        npu_write32(rtp["l_kv"], L_local, column=2, row=3)
        npu_write32(rtp["swa_l_qk"], L_local, column=2, row=4)
        npu_write32(rtp["swa_l_kv"], L_local, column=2, row=5)
        npu_write32(rtp["rms_swa"], int(IS_SWA), column=3, row=2)
        npu_write32(rtp["rms_skip"], int(IS_SKIP), column=3, row=2)
        npu_write32(rtp["rope_skip_kv"], int(IS_SKIP), column=3, row=4)
        npu_write32(rtp["swa_rope_skip_kv"], int(IS_SKIP), column=3, row=5)
        npu_write32(
            rtp["glu_skip"],
            int(IS_SKIP and g.double_wide_mlp),
            column=3,
            row=3,
        )
        npu_write32(RTP_SYNC_LOCK_ADDR, 1, column=3, row=2)
        npu_write32(RTP_SYNC_LOCK_ADDR, 1, column=3, row=3)

        # Two rounds of legs in flight, as the engine's bd_offset double
        # buffer: at most 16 BDs a shim tile.
        DEPTH_ROUNDS = 2
        window = []

        def flush(force=False):
            while len(window) > (0 if force else DEPTH_ROUNDS):
                tasks = window.pop(0)
                for t in tasks:
                    if t[1]:
                        dma_await_task(t[0])
                dma_free_task(*[t[0] for t in tasks])

        def emit(round_tasks):
            """Start one round of (task, has_token) legs."""
            dma_start_task(*[t[0] for t in round_tasks])
            window.append(round_tasks)
            flush()

        def lin(symbol, mem, off, length, token, pkt=None):
            # dma_bd takes i64 sizes and an i32 transfer_len.
            size_len = (
                length if isinstance(length, int) else arith.extsi(T.i64(), length)
            )
            return shim_dma_single_bd_task(
                symbol,
                mem,
                offset=off,
                sizes=[1, 1, 1, size_len],
                strides=[0, 0, 0, 1],
                transfer_len=length,
                issue_token=token,
                packet=pkt,
            )

        emit([(lin("send_x", x_arg.op, 0, D, True, pkt=(0, _ShimPkt.to_rms)), True)])
        emit(
            [
                (
                    lin(
                        "send_rms", rms_arg.op, 0, 4 * D, True, pkt=(0, _ShimPkt.to_rms)
                    ),
                    True,
                )
            ]
        )
        # The RoPE weights go out on the channel whose flow reaches this
        # layer type's RoPE tile.
        rope_sym = "send_rms" if IS_SWA else "send_x"
        emit(
            [
                (
                    lin(
                        rope_sym,
                        rope_rms_arg.op,
                        0,
                        3 * DH,
                        True,
                        pkt=(0, _ShimPkt.to_rope),
                    ),
                    True,
                )
            ]
        )
        recv_y = lin("recv_y", x_arg.op, 0, D, True)
        dma_start_task(recv_y)

        def move_weights(Dout, Din, w_off):
            """The engine's _move_weights: a round is 2 legs to each proj column."""
            cols = 4
            bpr = Din // Q4_K
            cores = cols * 4
            rounds = Dout // Q4_M // cores
            for rnd in range(rounds):
                rt_tasks = []
                for ci in range(cols):
                    col = PROJ_COLS[ci]
                    off0 = (rnd * cores + ci * 4) * W_BLOCK * bpr + w_off
                    rt_tasks.append(
                        (
                            lin(
                                f"proj_w0_{col}",
                                proj_arg.op,
                                off0,
                                2 * bpr * W_BLOCK,
                                True,
                            ),
                            True,
                        )
                    )
                    off1 = (rnd * cores + ci * 4 + 2) * W_BLOCK * bpr + w_off
                    rt_tasks.append(
                        (
                            lin(
                                f"proj_w1_{col}",
                                proj_arg.op,
                                off1,
                                2 * bpr * W_BLOCK,
                                True,
                            ),
                            True,
                        )
                    )
                emit(rt_tasks)

        # The engine strides the sliding-window cache by the window and the
        # global cache by its runtime max_l. DK + DV is even, so the halving
        # folds into the constant.
        assert (DK + DV) % 2 == 0
        if IS_SWA:
            v_cache_off = (DK + DV) * _SW // 2
        else:
            v_cache_off = MAX_L_v * ((DK + DV) // 2)
        if IS_SKIP:
            move_weights(DQ, D, qkv_off)
        else:
            move_weights(DQ + DK + DV, D, qkv_off)
            # This token's K and V into the cache, at row L - 1, modulo the
            # window on sliding-window layers. Both legs go on the layer
            # type's receive channel.
            L_off = (arith.andi(L - 1, _as_i32(_SW - 1)) if IS_SWA else (L - 1)) * DK
            recv_sym = "recv_v" if IS_SWA else "recv_k"
            emit([(lin(recv_sym, kv_arg.op, L_off, DK, True), True)])
            emit([(lin(recv_sym, kv_arg.op, L_off + v_cache_off, DV, True), True)])
        emit(
            [
                (
                    lin(
                        "pli_rope_rms",
                        rope_rms_arg.op,
                        3 * DH,
                        PLI_D * 2 + D + MIN_BF16_PAD,
                        True,
                    ),
                    True,
                )
            ]
        )
        # x reuses pli_rope_rms's channel as a second BD.
        emit([(lin("pli_rope_rms", x_arg.op, 2 * D, D, False), False)])
        emit([(lin("pli_down", proj_arg.op, pli_down_off, PLI_D * D, True), True)])
        # The KV cache into the attention memtile: one phase on global layers.
        # The sliding-window cache is a ring, so its window can wrap into two.
        mv_pkt = _KV_PKT_SWA if IS_SWA else _KV_PKT_GLOBAL
        if not IS_SWA:
            d2m = _ceil_mul(L, L_CHUNK) * DK
            emit([(lin("move_k", kv_arg.op, 0, d2m, True, pkt=(0, mv_pkt)), True)])
            emit(
                [
                    (
                        lin(
                            "move_v", kv_arg.op, v_cache_off, d2m, True, pkt=(0, mv_pkt)
                        ),
                        True,
                    )
                ]
            )
        else:
            # Two phases when L >= SW, one when L < SW: a mask picks the
            # lengths, so the leg count is fixed.
            _m = _mask_ge(L, _SW)
            _nm = arith.xori(_m, _as_i32(-1))
            _lb = arith.andi(L, _as_i32(_SW - 1))
            _Lp = arith.andi(L + (L_CHUNK - 1), _as_i32(-L_CHUNK))
            p1_off = arith.andi(_m, _lb * DK)
            p1_len = arith.ori(
                arith.andi(_m, (_as_i32(_SW) - _lb) * DK), arith.andi(_nm, _Lp * DK)
            )
            p2_len = arith.andi(_m, _lb * DK)
            emit(
                [
                    (
                        lin("move_k", kv_arg.op, p1_off, p1_len, True, pkt=(0, mv_pkt)),
                        True,
                    )
                ]
            )
            emit(
                [
                    (
                        lin(
                            "move_v",
                            kv_arg.op,
                            p1_off + v_cache_off,
                            p1_len,
                            True,
                            pkt=(0, mv_pkt),
                        ),
                        True,
                    )
                ]
            )
            # A zero-length BD issues no token, so the second phase awaits
            # none.
            emit([(lin("move_k", kv_arg.op, 0, p2_len, False, pkt=(0, mv_pkt)), False)])
            emit(
                [
                    (
                        lin(
                            "move_v",
                            kv_arg.op,
                            v_cache_off,
                            p2_len,
                            False,
                            pkt=(0, mv_pkt),
                        ),
                        False,
                    )
                ]
            )
        move_weights(D, DQ, o_off)
        move_weights(2 * INTERMEDIATE, D, upgate_off)
        move_weights(D, INTERMEDIATE, down_off)
        emit([(lin("pli_gate", proj_arg.op, pli_gate_off, PLI_D * D, True), True)])
        emit([(lin("pli_up", proj_arg.op, pli_up_off, PLI_D * D, True), True)])
        flush(force=True)
        dma_await_task(recv_y)
        dma_free_task(recv_y)

    bf = np.dtype[bfloat16]
    sizes = arg_sizes(g)
    rt = Runtime(
        sequence,
        [
            np.ndarray[(sizes["x"],), bf],
            np.ndarray[(sizes["proj"],), bf],
            np.ndarray[(sizes["rms"],), bf],
            np.ndarray[(sizes["rope_rms"],), bf],
            np.ndarray[(sizes["kv"],), bf],
            np.int32,
            np.int32,
        ],
    )
    workers = []

    # Shim row 0, memtile row 1, compute rows 2 to 5. CT is [compute row][col].
    IT = [Tile(c, 0, tile_type=dev.get_tile_type(c, 0)) for c in range(total_cols)]
    MT = [Tile(c, 1, tile_type=dev.get_tile_type(c, 1)) for c in range(total_cols)]
    CT = [
        [
            Tile(c, r + 2, tile_type=dev.get_tile_type(c, r + 2))
            for c in range(total_cols)
        ]
        for r in range(4)
    ]

    RTP_ty = np.ndarray[(16,), np.dtype[np.int32]]

    def locks(tile, table, inits):
        """The tile's locks named in ``table``, with ``inits`` by name."""
        out = {}
        for name, init in inits.items():
            out[name] = Lock(tile=tile, lock_id=table[name], init=init)
            rt.add_lock(out[name])
        return out

    # --- RMS norm and residual. x in on S2MM 0, the norm weights on S2MM 1,
    # y out on MM2S 0 behind its packet header. y_out is the layer output the
    # gate tile reads.
    rms_tile = CT[0][3]
    rms_x_ty = np.ndarray[(D,), bf]
    rms_x_buf_ty = np.ndarray[(D, 2), bf]
    rms_w_ty = np.ndarray[(4, D), bf]
    rms_y_pkt_ty = np.ndarray[(D + 16,), bf]
    rms_name = f"{rms_tile.row}_{rms_tile.col}"
    rms_x_ping = Buffer(type=rms_x_ty, name=f"x_ping_{rms_name}", tile=rms_tile)
    rms_x_pong = Buffer(type=rms_x_ty, name=f"x_pong_{rms_name}", tile=rms_tile)
    rms_x_buf = Buffer(type=rms_x_buf_ty, name=f"x_buf_{rms_name}", tile=rms_tile)
    rms_w = Buffer(type=rms_w_ty, name=f"w_buffer_{rms_name}", tile=rms_tile)
    rms_y_out = Buffer(type=rms_x_ty, name=f"y_out_{rms_name}", tile=rms_tile)
    rms_y = Buffer(type=rms_y_pkt_ty, name=f"y_{rms_name}", tile=rms_tile)
    rms_is_swa = Buffer(
        type=RTP_ty,
        name=RTP_SYMBOLS["rms_swa"],
        tile=rms_tile,
        use_write_rtp=True,
        address=rtp["rms_swa"],
    )
    rms_skip = Buffer(
        type=RTP_ty,
        name=RTP_SYMBOLS["rms_skip"],
        tile=rms_tile,
        use_write_rtp=True,
        address=rtp["rms_skip"],
    )
    rl = locks(
        rms_tile,
        RMS_LOCKS,
        dict(
            w_prod_lock=1,
            w_cons_lock=0,
            y_prod_lock=0,
            y_cons_lock=0,
            x_prod_lock=2,
            x_cons_lock=0,
            # No DMA takes the rest. The sequence sets the first. The other
            # two hand y_out to the gate tile's kernel.
            rtp_available_lock=0,
            lm_head_out_prod_lock=1,
            lm_head_out_cons_lock=0,
        ),
    )
    rms_k = k(
        "rms_residual",
        "rms_residual",
        [
            rms_y_pkt_ty,
            rms_x_ty,
            rms_x_ty,
            rms_x_ty,
            rms_w_ty,
            rms_x_buf_ty,
            RTP_ty,
            RTP_ty,
        ],
    )

    def rms_body(y, xp, xq, yo, w, xb, is_swa, skip, kern):
        kern(y, xp, xq, yo, w, xb, is_swa, skip)

    workers.append(
        Worker(
            rms_body,
            [
                rms_y,
                rms_x_ping,
                rms_x_pong,
                rms_y_out,
                rms_w,
                rms_x_buf,
                rms_is_swa,
                rms_skip,
                rms_k,
            ],
            tile=rms_tile,
            while_true=True,
            stack_size=1024 * 4,
        )
    )
    rt.add_tile_dma(
        TileDma(
            rms_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    _ping_pong(
                        rms_x_ping,
                        rms_x_pong,
                        rl["x_prod_lock"],
                        rl["x_cons_lock"],
                        offset=0,
                        length=D,
                    ),
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    [
                        Bd(
                            rms_w,
                            offset=0,
                            length=4 * D,
                            acquires=[Acquire(rl["w_prod_lock"])],
                            releases=[Release(rl["w_cons_lock"])],
                        ),
                    ],
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    [
                        Bd(
                            rms_y,
                            offset=14,
                            length=D + 2,
                            acquires=[Acquire(rl["y_cons_lock"])],
                            releases=[Release(rl["y_prod_lock"])],
                        ),
                    ],
                ),
            ],
        )
    )

    # --- RoPE, global and sliding-window: qkv in on S2MM 0, the RoPE weights
    # on S2MM 1, q out through a fifo to the qk core, k and v out on MM2S 1.
    def build_rope(rope_tile, name, name_tag, dq, dk, dh, q_fifo, skip_addr):
        dq_padded = NQ_PADDED * dh
        qkv_ty = np.ndarray[(dh,), bf]
        q_ty = np.ndarray[(dq_padded,), bf]
        k_ty = np.ndarray[(dk,), bf]
        v_ty = np.ndarray[(dk,), bf]
        rope_ty = np.ndarray[(dh * 3 if g.qk_norm else dh,), bf]

        r, c = rope_tile.row, rope_tile.col
        qkv_0 = Buffer(type=qkv_ty, name=f"qkv_buffer_0_{r}_{c}", tile=rope_tile)
        qkv_1 = Buffer(type=qkv_ty, name=f"qkv_buffer_1_{r}_{c}", tile=rope_tile)
        k_buf = Buffer(type=k_ty, name=f"k_buffer_{r}_{c}", tile=rope_tile)
        v_buf = Buffer(type=v_ty, name=f"v_buffer_{r}_{c}", tile=rope_tile)
        rope_buf = Buffer(type=rope_ty, name=f"rope_buffer_{r}_{c}", tile=rope_tile)
        skip_kv = Buffer(
            type=RTP_ty,
            name=f"RTP_{name_tag}_SKIP_KV_{r}_{c}",
            tile=rope_tile,
            use_write_rtp=True,
            address=skip_addr,
        )
        lk = locks(
            rope_tile,
            ROPE_LOCKS,
            dict(
                qkv_prod_lock=2,
                qkv_cons_lock=0,
                k_prod_lock=1,
                k_cons_lock=0,
                v_prod_lock=1,
                v_cons_lock=0,
                rope_prod_lock=1,
                rope_cons_lock=0,
            ),
        )
        rt.add_lock(Lock(tile=rope_tile, lock_id=ROPE_Q_PASS_LOCK, init=0))
        kern = k(name, name, [q_ty, k_ty, v_ty, qkv_ty, qkv_ty, rope_ty, RTP_ty])

        def rope_body(q_h, kk, v, q0, q1, rope, skip, kern):
            q = q_h.acquire(1)
            kern(q, kk, v, q0, q1, rope, skip)
            q_h.release(1)

        workers.append(
            Worker(
                rope_body,
                [q_fifo.prod(), k_buf, v_buf, qkv_0, qkv_1, rope_buf, skip_kv, kern],
                tile=rope_tile,
                while_true=True,
                stack_size=1024 * 4,
            )
        )
        rt.add_tile_dma(
            TileDma(
                rope_tile,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        0,
                        _ping_pong(
                            qkv_0, qkv_1, lk["qkv_prod_lock"], lk["qkv_cons_lock"]
                        ),
                    ),
                    DmaChannel(
                        DMAChannelDir.MM2S,
                        1,
                        [
                            Bd(
                                k_buf,
                                acquires=[Acquire(lk["k_cons_lock"])],
                                releases=[Release(lk["k_prod_lock"])],
                                next=1,
                            ),
                            Bd(
                                v_buf,
                                acquires=[Acquire(lk["v_cons_lock"])],
                                releases=[Release(lk["v_prod_lock"])],
                                next=0,
                            ),
                        ],
                    ),
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        1,
                        [
                            Bd(
                                rope_buf,
                                acquires=[Acquire(lk["rope_prod_lock"])],
                                releases=[Release(lk["rope_cons_lock"])],
                            ),
                        ],
                    ),
                ],
            )
        )

    # q from RoPE to the qk core. The consumer reorders it on the way in.
    q_of_g = ObjectFifo(np.ndarray[(G_DQ,), bf], name="q_in", depth=2)
    q_of_swa = ObjectFifo(np.ndarray[(S_DQ,), bf], name="swa_q_in", depth=2)

    rope_tile = CT[2][3]
    build_rope(rope_tile, "rope", "RoPE", G_DQ, G_DK, g.dh, q_of_g, rtp["rope_skip_kv"])
    swa_rope_tile = CT[3][3]
    build_rope(
        swa_rope_tile,
        "swa_rope",
        "SWA_RoPE",
        S_DQ,
        S_DK,
        g.swa_dh,
        q_of_swa,
        rtp["swa_rope_skip_kv"],
    )

    w_blk_ty = np.ndarray[(BF16_W_BLOCK,), bf]

    # --- Per-layer-input embedding: x0_per_layer, the norm weights and x0 in
    # on S2MM 0 as a 4-BD cycle, weights on S2MM 1, y out on MM2S 1.
    ple_tile = CT[1][4]
    ple_name = f"{ple_tile.row}_{ple_tile.col}"
    ple_norm_w_ty = np.ndarray[(PLI_D + D + 32,), bf]
    ple_x0_pl_ty = np.ndarray[(PLI_D,), bf]
    ple_x0_ty = np.ndarray[(D,), bf]
    ple_y_ty = np.ndarray[(PLI_D + D + 32,), bf]
    ple_norm_w = Buffer(type=ple_norm_w_ty, name=f"norm_w_{ple_name}", tile=ple_tile)
    ple_x0_pl = Buffer(
        type=ple_x0_pl_ty, name=f"x0_per_layer_{ple_name}", tile=ple_tile
    )
    ple_x0 = Buffer(type=ple_x0_ty, name=f"x0_{ple_name}", tile=ple_tile)
    ple_x_proj = Buffer(type=ple_x0_pl_ty, name=f"x_proj_{ple_name}", tile=ple_tile)
    ple_y = Buffer(type=ple_y_ty, name=f"y_{ple_name}", tile=ple_tile)
    ple_w0 = Buffer(type=w_blk_ty, name=f"proj_w_0_{ple_name}", tile=ple_tile)
    ple_w1 = Buffer(type=w_blk_ty, name=f"proj_w_1_{ple_name}", tile=ple_tile)
    pl = locks(
        ple_tile,
        PLE_LOCKS,
        dict(
            norm_w_prod_lock=0,
            x0_per_layer_prod_lock=1,
            x0_prod_lock=0,
            xw_cons_lock=0,
            proj_w_prod_lock=2,
            proj_w_cons_lock=0,
            y_prod_lock=1,
            y_cons_lock=0,
        ),
    )
    ple_norm_w_p2 = Lock(tile=ple_tile, lock_id=PLE_NORM_W_P2_LOCK, init=0)
    rt.add_lock(ple_norm_w_p2)
    ple_k = k(
        "proj_layer_embedding",
        "proj_layer_embedding",
        [
            ple_norm_w_ty,
            ple_x0_pl_ty,
            ple_x0_ty,
            ple_x0_pl_ty,
            ple_y_ty,
            w_blk_ty,
            w_blk_ty,
        ],
    )

    def ple_body(nw, x0pl, x0, xproj, y, w0, w1, kern):
        kern(nw, x0pl, x0, xproj, y, w0, w1)

    workers.append(
        Worker(
            ple_body,
            [ple_norm_w, ple_x0_pl, ple_x0, ple_x_proj, ple_y, ple_w0, ple_w1, ple_k],
            tile=ple_tile,
            while_true=True,
            stack_size=1024 * 4,
        )
    )
    rt.add_tile_dma(
        TileDma(
            ple_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    [
                        Bd(
                            ple_x0_pl,
                            acquires=[Acquire(pl["x0_per_layer_prod_lock"])],
                            releases=[Release(pl["norm_w_prod_lock"])],
                            next=1,
                        ),
                        Bd(
                            ple_norm_w,
                            offset=0,
                            length=PLI_D,
                            acquires=[Acquire(pl["norm_w_prod_lock"])],
                            releases=[Release(ple_norm_w_p2)],
                            next=2,
                        ),
                        Bd(
                            ple_norm_w,
                            offset=PLI_D,
                            length=D + 32,
                            acquires=[Acquire(ple_norm_w_p2)],
                            releases=[Release(pl["x0_prod_lock"])],
                            next=3,
                        ),
                        Bd(
                            ple_x0,
                            acquires=[Acquire(pl["x0_prod_lock"])],
                            releases=[Release(pl["xw_cons_lock"])],
                            next=0,
                        ),
                    ],
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    _ping_pong(
                        ple_w0,
                        ple_w1,
                        pl["proj_w_prod_lock"],
                        pl["proj_w_cons_lock"],
                    ),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    1,
                    [
                        Bd(
                            ple_y,
                            acquires=[Acquire(pl["y_cons_lock"])],
                            releases=[Release(pl["y_prod_lock"])],
                        ),
                    ],
                ),
            ],
        )
    )

    # --- Per-layer-input gate: x is the RMS tile's y_out, weights on S2MM 1,
    # y out on MM2S 1. No core reads x_residual.
    gle_tile = CT[0][4]
    gle_name = f"{gle_tile.row}_{gle_tile.col}"
    gle_x_ty = np.ndarray[(D,), bf]
    gle_y_ty = np.ndarray[(D + PLI_D,), bf]
    gle_x_residual = Buffer(type=gle_x_ty, name=f"x_residual_{gle_name}", tile=gle_tile)
    gle_w0 = Buffer(type=w_blk_ty, name=f"proj_w_0_{gle_name}", tile=gle_tile)
    gle_w1 = Buffer(type=w_blk_ty, name=f"proj_w_1_{gle_name}", tile=gle_tile)
    gle_y = Buffer(type=gle_y_ty, name=f"y_{gle_name}", tile=gle_tile)
    gl = locks(
        gle_tile,
        GLE_LOCKS,
        dict(
            x_prod_lock=1,
            x_cons_lock=0,
            proj_w_prod_lock=2,
            proj_w_cons_lock=0,
            y_prod_lock=1,
            y_cons_lock=0,
        ),
    )
    gle_k = k(
        "gate_layer_embedding",
        "gate_layer_embedding",
        [gle_x_ty, w_blk_ty, w_blk_ty, gle_y_ty],
    )

    def gle_body(x, w0, w1, y, kern, _x_residual):
        kern(x, w0, w1, y)

    workers.append(
        Worker(
            gle_body,
            [rms_y_out, gle_w0, gle_w1, gle_y, gle_k, gle_x_residual],
            tile=gle_tile,
            while_true=True,
            stack_size=1024 * 4,
        )
    )
    rt.add_tile_dma(
        TileDma(
            gle_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    _ping_pong(
                        gle_w0,
                        gle_w1,
                        gl["proj_w_prod_lock"],
                        gl["proj_w_cons_lock"],
                    ),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    1,
                    [
                        Bd(
                            gle_y,
                            acquires=[Acquire(gl["y_cons_lock"])],
                            releases=[Release(gl["y_prod_lock"])],
                        ),
                    ],
                ),
            ],
        )
    )

    # --- Per-layer-input merge, a tile without a core: the embedding and the
    # gate outputs into one buffer, out to the up projection.
    plm_tile = CT[1][5]
    plm_dual_y_ty = np.ndarray[(2 * (PLI_D + D) + 32,), bf]
    plm_y = Buffer(
        type=plm_dual_y_ty, name=f"y_{plm_tile.row}_{plm_tile.col}", tile=plm_tile
    )
    plm_norm_i_prod = Lock(tile=plm_tile, lock_id=0, init=1)
    rt.add_lock(plm_norm_i_prod)
    plm_res_gate_prod = Lock(tile=plm_tile, lock_id=1, init=0)
    rt.add_lock(plm_res_gate_prod)
    plm_cons = Lock(tile=plm_tile, lock_id=2, init=0)
    rt.add_lock(plm_cons)
    rt.add_tile_dma(
        TileDma(
            plm_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    [
                        Bd(
                            plm_y,
                            offset=0,
                            length=D + PLI_D + 32,
                            acquires=[Acquire(plm_norm_i_prod)],
                            releases=[Release(plm_res_gate_prod)],
                        ),
                    ],
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    [
                        Bd(
                            plm_y,
                            offset=D + PLI_D + 32,
                            length=D + PLI_D,
                            acquires=[Acquire(plm_res_gate_prod)],
                            releases=[Release(plm_cons)],
                        ),
                    ],
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    [
                        Bd(
                            plm_y,
                            acquires=[Acquire(plm_cons)],
                            releases=[Release(plm_norm_i_prod)],
                        ),
                    ],
                ),
            ],
        )
    )

    # --- Per-layer-input up projection: x in on S2MM 0, weights on S2MM 1,
    # the layer output on MM2S 0.
    plu_tile = CT[0][5]
    plu_name = f"{plu_tile.row}_{plu_tile.col}"
    plu_dual_x_ty = np.ndarray[(2 * (PLI_D + D) + 32,), bf]
    plu_y_ty = np.ndarray[(D,), bf]
    plu_x = Buffer(type=plu_dual_x_ty, name=f"x_{plu_name}", tile=plu_tile)
    plu_y = Buffer(type=plu_y_ty, name=f"y_{plu_name}", tile=plu_tile)
    plu_w0 = Buffer(type=w_blk_ty, name=f"proj_w_0_{plu_name}", tile=plu_tile)
    plu_w1 = Buffer(type=w_blk_ty, name=f"proj_w_1_{plu_name}", tile=plu_tile)
    ul = locks(
        plu_tile,
        PLU_LOCKS,
        dict(
            x_prod_lock=1,
            x_cons_lock=0,
            proj_w_prod_lock=2,
            proj_w_cons_lock=0,
            y_prod_lock=1,
            y_cons_lock=0,
        ),
    )
    plu_k = k(
        "per_layer_up", "per_layer_up", [plu_dual_x_ty, w_blk_ty, w_blk_ty, plu_y_ty]
    )

    def plu_body(x, w0, w1, y, kern):
        kern(x, w0, w1, y)

    workers.append(
        Worker(
            plu_body,
            [plu_x, plu_w0, plu_w1, plu_y, plu_k],
            tile=plu_tile,
            while_true=True,
            stack_size=1024 * 4,
        )
    )
    rt.add_tile_dma(
        TileDma(
            plu_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    [
                        Bd(
                            plu_x,
                            acquires=[Acquire(ul["x_prod_lock"])],
                            releases=[Release(ul["x_cons_lock"])],
                        ),
                    ],
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    _ping_pong(
                        plu_w0,
                        plu_w1,
                        ul["proj_w_prod_lock"],
                        ul["proj_w_cons_lock"],
                    ),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    [
                        Bd(
                            plu_y,
                            acquires=[Acquire(ul["y_cons_lock"])],
                            releases=[Release(ul["y_prod_lock"])],
                        ),
                    ],
                ),
            ],
        )
    )

    # --- GLU: gate and up in on S2MM 0, the activations out on MM2S 0 with a
    # packet header to the projection engine.
    glu_tile = CT[1][3]
    glu_name = f"{glu_tile.row}_{glu_tile.col}"
    glu_up_gate_ty = np.ndarray[(g.glu_slice,), bf]
    glu_hid_ty = np.ndarray[
        (g.intermediate_size * (2 if g.double_wide_mlp else 1),), bf
    ]
    glu_y_ty = np.ndarray[(g.glu_slice // 2,), bf]
    glu_x_0 = Buffer(type=glu_up_gate_ty, name=f"x_0_{glu_name}", tile=glu_tile)
    glu_x_1 = Buffer(type=glu_up_gate_ty, name=f"x_1_{glu_name}", tile=glu_tile)
    glu_y_0 = Buffer(type=glu_y_ty, name=f"y_0_{glu_name}", tile=glu_tile)
    glu_y_1 = Buffer(type=glu_y_ty, name=f"y_1_{glu_name}", tile=glu_tile)
    glu_hid = Buffer(type=glu_hid_ty, name=f"hid_0_{glu_name}", tile=glu_tile)
    glu_is_skip = Buffer(
        type=RTP_ty,
        name=RTP_SYMBOLS["glu_skip"],
        tile=glu_tile,
        use_write_rtp=True,
        address=rtp["glu_skip"],
    )
    ll = locks(
        glu_tile,
        GLU_LOCKS,
        dict(x_prod_lock=2, x_cons_lock=0, y_prod_lock=2, y_cons_lock=0, rtp_lock=0),
    )
    glu_k = k(
        "glu",
        "glu",
        [glu_hid_ty, glu_up_gate_ty, glu_up_gate_ty, glu_y_ty, glu_y_ty, RTP_ty],
    )

    def glu_body(hid, x0, x1, y0, y1, is_skip, kern):
        kern(hid, x0, x1, y0, y1, is_skip)

    workers.append(
        Worker(
            glu_body,
            [glu_hid, glu_x_0, glu_x_1, glu_y_0, glu_y_1, glu_is_skip, glu_k],
            tile=glu_tile,
            while_true=True,
            stack_size=4 * 1024,
        )
    )
    rt.add_tile_dma(
        TileDma(
            glu_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    _ping_pong(glu_x_0, glu_x_1, ll["x_prod_lock"], ll["x_cons_lock"]),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    _ping_pong(
                        glu_y_0,
                        glu_y_1,
                        ll["y_cons_lock"],
                        ll["y_prod_lock"],
                        packet=(0, _X_FROM_GLU),
                    ),
                ),
            ],
        )
    )

    # --- The q4nx projection engine: 16 cores in columns 0, 1, 6 and 7. The
    # core of an even row sends; the core below it fills the second slot of
    # the sender's y buffers.
    x_slice_ty = np.ndarray[(X_SLICE,), bf]
    linear_w_ty = np.ndarray[(W_BLOCK,), bf]
    m_pkt_ty = np.ndarray[(2 * Q4_M + 16,), bf]
    proj_k = k(
        "proj_main",
        "proj_main",
        [
            m_pkt_ty,
            linear_w_ty,
            x_slice_ty,
            m_pkt_ty,
            linear_w_ty,
            x_slice_ty,
            RTP_ty,
            RTP_ty,
            np.int32,
        ],
    )

    def build_proj_main(pt, send_x_out, main_y0=None, main_y1=None):
        """Returns (y0, y1), which the paired core below borrows."""
        r, c = pt.row, pt.col
        is_swa = Buffer(
            type=RTP_ty,
            name=f"RTP_PROJ_IS_SWA_BUFFER_{r}_{c}",
            tile=pt,
            use_write_rtp=True,
            address=rtp["proj_swa"],
        )
        skip_kv = Buffer(
            type=RTP_ty,
            name=f"RTP_PROJ_SKIP_KV_BUFFER_{r}_{c}",
            tile=pt,
            use_write_rtp=True,
            address=rtp["proj_skip"],
        )
        x0 = Buffer(type=x_slice_ty, name=f"x_0_{r}_{c}", tile=pt)
        w0 = Buffer(type=linear_w_ty, name=f"w_0_{r}_{c}", tile=pt)
        x1 = Buffer(type=x_slice_ty, name=f"x_1_{r}_{c}", tile=pt)
        w1 = Buffer(type=linear_w_ty, name=f"w_1_{r}_{c}", tile=pt)
        if send_x_out:
            y0 = Buffer(type=m_pkt_ty, name=f"y_0_{r}_{c}", tile=pt)
            y1 = Buffer(type=m_pkt_ty, name=f"y_1_{r}_{c}", tile=pt)
        else:
            y0, y1 = main_y0, main_y1
        pk = locks(
            pt,
            PROJ_LOCKS,
            dict(
                x_prod_lock=2,
                x_cons_lock=0,
                w_prod_lock=2,
                w_cons_lock=0,
                y_prod_ping_lock=2,
                y_prod_pong_lock=2,
                rtp_available_lock=0,
                y_cons_ping_lock=0,
                y_cons_pong_lock=0,
            ),
        )
        flag = 1 if send_x_out else 0

        def proj_body(yy0, ww0, xx0, yy1, ww1, xx1, sw, sk, kern):
            kern(yy0, ww0, xx0, yy1, ww1, xx1, sw, sk, constant(flag))

        workers.append(
            Worker(
                proj_body,
                [y0, w0, x0, y1, w1, x1, is_swa, skip_kv, proj_k],
                tile=pt,
                while_true=True,
                stack_size=10 * 1024,
            )
        )
        chans = [
            DmaChannel(
                DMAChannelDir.S2MM,
                0,
                _ping_pong(x0, x1, pk["x_prod_lock"], pk["x_cons_lock"]),
            ),
            DmaChannel(
                DMAChannelDir.S2MM,
                1,
                _ping_pong(w0, w1, pk["w_prod_lock"], pk["w_cons_lock"]),
            ),
        ]
        if send_x_out:
            chans.append(
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    [
                        Bd(
                            y,
                            offset=14,
                            length=2 * Q4_M + 2,
                            acquires=[Acquire(pk[f"y_cons_{half}_lock"], value=2)],
                            releases=[Release(pk[f"y_prod_{half}_lock"], value=2)],
                            next=nxt,
                        )
                        for y, half, nxt in ((y0, "ping", 1), (y1, "pong", 0))
                    ],
                )
            )
        rt.add_tile_dma(TileDma(pt, chans))
        return y0, y1

    # proj_send_tiles[group]: the sending cores whose y gathers into that
    # group's memtile.
    proj_send_tiles = []
    for grp in range(2):
        group_send = []
        for csub in (0, 1):
            col = PROJ_COLS[2 * grp + csub]
            for row_pair in range(2):
                send_t = CT[row_pair * 2][col]
                nosend_t = CT[row_pair * 2 + 1][col]
                y0, y1 = build_proj_main(send_t, send_x_out=True)
                build_proj_main(nosend_t, send_x_out=False, main_y0=y0, main_y1=y1)
                group_send.append(send_t)
        proj_send_tiles.append(group_send)

    # --- The projection memtiles. Each splits its column's weights over the
    # column's four cores. MT[0] and MT[6] also gather y from their group,
    # and MT[1] gathers both groups' y and broadcasts x.
    linear_4w_ty = np.ndarray[(4 * W_BLOCK,), bf]
    WB = W_BLOCK
    m = Q4_M

    def mt_locks(mt, ids_inits):
        out = []
        for lock_id, init in ids_inits:
            lock = Lock(tile=mt, lock_id=lock_id, init=init)
            rt.add_lock(lock)
            out.append(lock)
        return out

    def weight_channels(w0, w1, wp0, wp0c0, wp0c1, wp1, wp1c0, wp1c1):
        return {
            "in0": DmaChannel(
                DMAChannelDir.S2MM,
                4,
                _ping_pong(w0, w1, wp0, wp0c0, offset=0, length=2 * WB),
            ),
            "in1": DmaChannel(
                DMAChannelDir.S2MM,
                5,
                _ping_pong(w0, w1, wp1, wp1c0, offset=2 * WB, length=2 * WB),
            ),
            "out": [
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    _ping_pong(w0, w1, wp0c0, wp0c1, offset=0, length=WB),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    1,
                    _ping_pong(w0, w1, wp0c1, wp0, offset=WB, length=WB),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    2,
                    _ping_pong(w0, w1, wp1c0, wp1c1, offset=2 * WB, length=WB),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    3,
                    _ping_pong(w0, w1, wp1c1, wp1, offset=3 * WB, length=WB),
                ),
            ],
        }

    def weight_buffers(mt):
        r, c = mt.row, mt.col
        w0 = Buffer(type=linear_4w_ty, name=f"w_buffer_0_{r}_{c}", tile=mt)
        w1 = Buffer(type=linear_4w_ty, name=f"w_buffer_1_{r}_{c}", tile=mt)
        return w0, w1

    WEIGHT_LOCKS = [(5, 2), (6, 0), (7, 0), (8, 2), (9, 0), (10, 0)]

    def build_assemble_col(mt):
        r, c = mt.row, mt.col
        m_col_ty = np.ndarray[(8 * m + 2,), bf]
        y0 = Buffer(type=m_col_ty, name=f"y_buffer_0_{r}_{c}", tile=mt)
        y1 = Buffer(type=m_col_ty, name=f"y_buffer_1_{r}_{c}", tile=mt)
        w0, w1 = weight_buffers(mt)
        yp0, yp1, yp2, yp3, yc = mt_locks(mt, [(0, 2), (1, 0), (2, 0), (3, 0), (4, 0)])
        wc = weight_channels(w0, w1, *mt_locks(mt, WEIGHT_LOCKS))
        rt.add_tile_dma(
            TileDma(
                mt,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        0,
                        _ping_pong(y0, y1, yp0, yp1, offset=0, length=2 * m + 2),
                    ),
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        1,
                        _ping_pong(y0, y1, yp1, yp2, offset=2 * m + 2, length=2 * m),
                    ),
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        2,
                        _ping_pong(y0, y1, yp2, yp3, offset=4 * m + 2, length=2 * m),
                    ),
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        3,
                        _ping_pong(y0, y1, yp3, yc, offset=6 * m + 2, length=2 * m),
                    ),
                    wc["in0"],
                    *wc["out"],
                    DmaChannel(DMAChannelDir.MM2S, 4, _ping_pong(y0, y1, yc, yp0)),
                    wc["in1"],
                ],
            )
        )

    def build_assemble_weight_only(mt):
        w0, w1 = weight_buffers(mt)
        wc = weight_channels(w0, w1, *mt_locks(mt, WEIGHT_LOCKS))
        rt.add_tile_dma(TileDma(mt, [wc["in0"], *wc["out"], wc["in1"]]))

    def build_assemble_weight_x(mt):
        r, c = mt.row, mt.col
        x_chunk_ty = np.ndarray[(X_SLICE * 2,), bf]
        m_full_ty = np.ndarray[(16 * m + 2,), bf]
        y0 = Buffer(type=m_full_ty, name=f"y_buffer_0_{r}_{c}", tile=mt)
        y1 = Buffer(type=m_full_ty, name=f"y_buffer_1_{r}_{c}", tile=mt)
        x0 = Buffer(type=x_chunk_ty, name=f"x_buffer_0_{r}_{c}", tile=mt)
        x1 = Buffer(type=x_chunk_ty, name=f"x_buffer_1_{r}_{c}", tile=mt)
        mp0, mp1, mc, xp, xc = mt_locks(mt, [(0, 2), (1, 0), (2, 0), (3, 2), (4, 0)])
        w0, w1 = weight_buffers(mt)
        wc = weight_channels(w0, w1, *mt_locks(mt, WEIGHT_LOCKS))
        rt.add_tile_dma(
            TileDma(
                mt,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        0,
                        _ping_pong(y0, y1, mp0, mp1, offset=0, length=8 * m + 2),
                    ),
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        1,
                        _ping_pong(y0, y1, mp1, mc, offset=8 * m + 2, length=8 * m),
                    ),
                    DmaChannel(DMAChannelDir.S2MM, 3, _ping_pong(x0, x1, xp, xc)),
                    wc["in0"],
                    wc["in1"],
                    DmaChannel(DMAChannelDir.MM2S, 5, _ping_pong(y0, y1, mc, mp0)),
                    DmaChannel(DMAChannelDir.MM2S, 4, _ping_pong(x0, x1, xc, xp)),
                    *wc["out"],
                ],
            )
        )

    build_assemble_col(MT[0])
    build_assemble_col(MT[6])
    build_assemble_weight_only(MT[7])
    build_assemble_weight_x(MT[1])
    proj_main_mt = MT[1]

    def proj_route():
        # The weights from the shim into each memtile, halves on S2MM 4 and 5.
        for mtid in PROJ_COLS:
            for ch in (0, 1):
                rt.add_flow(
                    Flow(
                        IT[mtid],
                        MT[mtid],
                        src_channel=ch,
                        dst_channel=4 + ch,
                        shim_symbol=f"proj_w{ch}_{mtid}",
                    )
                )
        # The memtile's MM2S j to S2MM 1 of its column's core in row j.
        for col in PROJ_COLS:
            for j in range(4):
                _connect(rt, MT[col], j, CT[j][col], 1)
        # x from MT[1]'s MM2S 4 to every projection core's S2MM 0.
        for col in PROJ_COLS:
            for j in range(4):
                _connect(rt, proj_main_mt, 4, CT[j][col], 0)
        # y from each group's sending cores to its memtile. The first keeps the
        # packet header, which carries the consumer's id to MT[1].
        pkts = [
            _ProjPkt.to_swa_rope,
            _ProjPkt.to_rope,
            _ProjPkt.to_rms,
            _ProjPkt.to_glu,
        ]
        gather_mts = [MT[0], MT[6]]
        for grp in range(2):
            for combo_j, send_t in enumerate(proj_send_tiles[grp]):
                for pk in pkts:
                    _connect(
                        rt,
                        send_t,
                        0,
                        gather_mts[grp],
                        combo_j,
                        pkt_id=pk,
                        keep_pkt_header=combo_j == 0,
                    )
        for pk in pkts:
            _connect(rt, MT[0], 4, proj_main_mt, 0, pkt_id=pk, keep_pkt_header=True)
        for pk in pkts:
            _connect(rt, MT[6], 4, proj_main_mt, 1, pkt_id=pk, keep_pkt_header=False)

    # --- Attention in column 2: the global pair in rows 2 and 3, the
    # sliding-window pair in rows 4 and 5. k and v come from MT[2], q from
    # RoPE, and the scores go from the qk core to the kv core through a fifo.
    attn_s_ty = np.ndarray[(NQ_PADDED * 16 + 32, 1), bf]
    f32 = np.dtype[np.float32]

    def build_attn_kv(
        kv_tile,
        name,
        rtp_name,
        dh,
        v_kv_head_style,
        pkt_id,
        of_s,
        two_kv_heads,
        rtp_addr,
    ):
        r, c = kv_tile.row, kv_tile.col
        NQ = g.num_attn_heads
        o_repeats = D // (Q4_M * 16)
        v_ty = np.ndarray[(LK, NUM_KV * dh if v_kv_head_style else dh), bf]
        o_ty = np.ndarray[(dh * NQ,), bf]
        y_ty = np.ndarray[(dh * NQ,), f32]
        L = Buffer(
            type=RTP_ty,
            name=rtp_name,
            tile=kv_tile,
            use_write_rtp=True,
            address=rtp_addr,
        )
        v0 = Buffer(type=v_ty, name=f"v_0_{r}_{c}", tile=kv_tile)
        v1 = Buffer(type=v_ty, name=f"v_1_{r}_{c}", tile=kv_tile)
        y = Buffer(type=y_ty, name=f"y_{r}_{c}", tile=kv_tile)
        o = Buffer(type=o_ty, name=f"o_{r}_{c}", tile=kv_tile)
        kl = locks(
            kv_tile,
            ATTN_KV_LOCKS,
            dict(o_prod_lock=o_repeats, o_cons_lock=0, v_prod_lock=2, v_cons_lock=0),
        )
        l_ty = np.ndarray[(8,), f32]
        lbuf = Buffer(type=l_ty, name=f"l_{r}_{c}", tile=kv_tile)
        k_begin = k(name, f"{name}_begin", [y_ty, l_ty])
        k_finish = k(name, f"{name}_finish", [y_ty, o_ty, l_ty])
        # A round's loop count is the RTP's L rounded up to whole rounds. The
        # begin kernel waits on the qk core, which reads the RTP after q
        # arrives.
        if two_kv_heads:
            k_sbeg = k(name, f"{name}_s_begin", [attn_s_ty, y_ty, l_ty])
            k_vhalf = k(name, f"{name}_v_half", [attn_s_ty, v_ty, v_ty, y_ty, np.int32])

            def kv_body(s_in, v_0, v_1, yy, ll, oo, rtp_l, kb, ksb, kvh, kf):
                kb(yy, ll)
                for _ in range_((rtp_l[0] + 15) // 16):
                    s = s_in.acquire(1)
                    ksb(s, yy, ll)
                    for j in range_(2):
                        kvh(s, v_0, v_1, yy, j)
                    s_in.release(1)
                kf(yy, oo, ll)

            args = [of_s.cons(), v0, v1, y, lbuf, o, L]
            args += [k_begin, k_sbeg, k_vhalf, k_finish]
        else:
            k_round = k(name, f"{name}_round", [attn_s_ty, v_ty, v_ty, y_ty, l_ty])

            def kv_body(s_in, v_0, v_1, yy, ll, oo, rtp_l, kb, kr, kf):
                kb(yy, ll)
                for _ in range_((rtp_l[0] + 15) // 16):
                    s = s_in.acquire(1)
                    kr(s, v_0, v_1, yy, ll)
                    s_in.release(1)
                kf(yy, oo, ll)

            args = [of_s.cons(), v0, v1, y, lbuf, o, L, k_begin, k_round, k_finish]

        workers.append(
            Worker(kv_body, args, tile=kv_tile, while_true=True, stack_size=1024 * 6)
        )
        rt.add_tile_dma(
            TileDma(
                kv_tile,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        1,
                        _ping_pong(v0, v1, kl["v_prod_lock"], kl["v_cons_lock"]),
                    ),
                    DmaChannel(
                        DMAChannelDir.MM2S,
                        0,
                        [
                            Bd(
                                o,
                                packet=(0, pkt_id),
                                offset=0,
                                length=NQ * dh,
                                sizes=[NQ, dh // 8, 8],
                                strides=[8, NQ * 8, 1],
                                acquires=[Acquire(kl["o_cons_lock"])],
                                releases=[Release(kl["o_prod_lock"])],
                            ),
                        ],
                    ),
                ],
            )
        )

    def build_attn_qk(
        qk_tile,
        name,
        rtp_name,
        dh,
        k_kv_head_style,
        of_s,
        q_fifo,
        rtp_addr,
        two_kv_heads,
    ):
        r, c = qk_tile.row, qk_tile.col
        k_ty = np.ndarray[(LK, NUM_KV * dh if k_kv_head_style else dh), bf]
        q_ty = np.ndarray[(NQ_PADDED * dh,), bf]
        k0 = Buffer(type=k_ty, name=f"k_0_{r}_{c}", tile=qk_tile)
        k1 = Buffer(type=k_ty, name=f"k_1_{r}_{c}", tile=qk_tile)
        ql = locks(qk_tile, ATTN_QK_LOCKS, dict(k_prod_lock=2, k_cons_lock=0))
        rt.add_lock(Lock(tile=qk_tile, lock_id=ATTN_HANDSHAKE_LOCK, init=0))
        L = Buffer(
            type=RTP_ty,
            name=rtp_name,
            tile=qk_tile,
            use_write_rtp=True,
            address=rtp_addr,
        )
        q_in_order = [(NQ_PADDED, 8), (dh // 8, NQ_PADDED * 8), (8, 1)]
        m_ty = np.ndarray[(16,), bf]
        c_ty = np.ndarray[(8,), f32]
        m_buf = Buffer(type=m_ty, name=f"m_{r}_{c}", tile=qk_tile)
        c_local = Buffer(type=c_ty, name=f"c_local_{r}_{c}", tile=qk_tile)
        k_begin = k(name, f"{name}_begin", [m_ty])
        # The q acquire orders the RTP read: q arrives only after the sequence
        # has written the RTPs.
        if two_kv_heads:
            k_half = k(
                name,
                f"{name}_half",
                [q_ty, k_ty, k_ty, attn_s_ty, m_ty, c_ty] + [np.int32] * 3,
            )
            k_storec = k(name, f"{name}_store_c", [attn_s_ty, c_ty])

            def qk_body(s_out, q_h, k_0, k_1, mm, cc, rtp_l, kb, kh, ks):
                q = q_h.acquire(1)
                kb(mm)
                for i in range_((rtp_l[0] + 15) // 16):
                    s = s_out.acquire(1)
                    for j in range_(2):
                        kh(q, k_0, k_1, s, mm, cc, j, i, rtp_l[0])
                    ks(s, cc)
                    s_out.release(1)
                q_h.release(1)

            kerns = [k_begin, k_half, k_storec]
        else:
            k_round = k(
                name,
                f"{name}_round",
                [q_ty, k_ty, k_ty, attn_s_ty, m_ty, c_ty, np.int32, np.int32],
            )

            def qk_body(s_out, q_h, k_0, k_1, mm, cc, rtp_l, kb, kr):
                q = q_h.acquire(1)
                kb(mm)
                for i in range_((rtp_l[0] + 15) // 16):
                    s = s_out.acquire(1)
                    kr(q, k_0, k_1, s, mm, cc, i, rtp_l[0])
                    s_out.release(1)
                q_h.release(1)

            kerns = [k_begin, k_round]

        args = [
            of_s.prod(),
            q_fifo.cons(dims_from_stream=q_in_order),
            k0,
            k1,
            m_buf,
            c_local,
            L,
        ] + kerns
        workers.append(
            Worker(qk_body, args, tile=qk_tile, while_true=True, stack_size=1024 * 4)
        )
        rt.add_tile_dma(
            TileDma(
                qk_tile,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        1,
                        _ping_pong(k0, k1, ql["k_prod_lock"], ql["k_cons_lock"]),
                    ),
                ],
            )
        )

    attn_qk_tile = CT[0][2]
    attn_kv_tile = CT[1][2]
    of_g_s = ObjectFifo(attn_s_ty, name="attn_s", delegate_tile=attn_kv_tile)
    build_attn_kv(
        attn_kv_tile,
        "attn_kv",
        f"RTP_L_attn_kv_core_{attn_kv_tile.row}_{attn_kv_tile.col}",
        g.dh,
        v_kv_head_style=not two_kv,
        pkt_id=_X_FROM_ATTN,
        of_s=of_g_s,
        two_kv_heads=two_kv,
        rtp_addr=rtp["l_kv"],
    )
    build_attn_qk(
        attn_qk_tile,
        "attn_qk",
        f"RTP_L_attn_qk_core_{attn_qk_tile.row}_{attn_qk_tile.col}",
        g.dh,
        k_kv_head_style=not two_kv,
        of_s=of_g_s,
        q_fifo=q_of_g,
        rtp_addr=rtp["l_qk"],
        two_kv_heads=two_kv,
    )
    # A sliding-window round covers every KV head, so its k and v rows hold
    # them all.
    swa_qk_tile = CT[2][2]
    swa_kv_tile = CT[3][2]
    of_swa_s = ObjectFifo(attn_s_ty, name="swa_attn_s", delegate_tile=swa_kv_tile)
    build_attn_kv(
        swa_kv_tile,
        "swa_attn_kv",
        f"RTP_L_swa_attn_kv_core_{swa_kv_tile.row}_{swa_kv_tile.col}",
        g.swa_dh,
        v_kv_head_style=True,
        pkt_id=_X_FROM_ATTN,
        of_s=of_swa_s,
        two_kv_heads=False,
        rtp_addr=rtp["swa_l_kv"],
    )
    build_attn_qk(
        swa_qk_tile,
        "swa_attn_qk",
        f"RTP_L_swa_attn_qk_core_{swa_qk_tile.row}_{swa_qk_tile.col}",
        g.swa_dh,
        k_kv_head_style=True,
        of_s=of_swa_s,
        q_fifo=q_of_swa,
        rtp_addr=rtp["swa_l_qk"],
        two_kv_heads=False,
    )

    # --- The attention memtile, MT[2]: k, v, swa_k and swa_v each in whole
    # rows, and out to its core in the order its kernel reads.
    amt = MT[2]
    amt_name = f"{amt.row}_{amt.col}"
    k_row = NUM_KV * g.dh
    sk_row = NUM_KV * g.swa_dh
    k_mem_ty = np.ndarray[(LK, k_row), bf]
    sk_mem_ty = np.ndarray[(LK, sk_row), bf]
    amt_bufs = {}
    for key, ty in (
        ("k", k_mem_ty),
        ("v", k_mem_ty),
        ("swa_k", sk_mem_ty),
        ("swa_v", sk_mem_ty),
    ):
        for i in (0, 1):
            amt_bufs[key, i] = Buffer(
                type=ty, name=f"{key}_mem_buffer_{i}_{amt_name}", tile=amt
            )
    amt_locks = dict(
        zip(
            ("k", "v", "swa_k", "swa_v"),
            (
                mt_locks(amt, pairs)
                for pairs in (
                    [(0, 2), (1, 0)],
                    [(3, 2), (4, 0)],
                    [(5, 2), (6, 0)],
                    [(7, 2), (8, 0)],
                )
            ),
        )
    )
    # A kernel reads kv_head_per_round heads a round: all of them.
    k_order = [(k_row // 8, 8), (16, k_row), (8, 1)]
    if not two_kv:
        v_order = [(LK // 8, LK // 2 * k_row), (k_row // 8, 8), (8, k_row), (8, 1)]
    else:
        v_order = [(k_row // 8, 8), (LK, k_row), (8, 1)]
    sk_order = [(sk_row // 8, 8), (16, sk_row), (8, 1)]
    sv_order = [(LK // 8, LK // 2 * sk_row), (sk_row // 8, 8), (8, sk_row), (8, 1)]
    amt_chans = []
    for ch, (key, order, length) in enumerate(
        (
            ("k", k_order, k_row * LK),
            ("v", v_order, k_row * LK),
            ("swa_k", sk_order, sk_row * LK),
            ("swa_v", sv_order, sk_row * LK),
        )
    ):
        b0, b1 = amt_bufs[key, 0], amt_bufs[key, 1]
        prod, cons = amt_locks[key]
        amt_chans += [
            DmaChannel(DMAChannelDir.S2MM, ch, _ping_pong(b0, b1, prod, cons)),
            DmaChannel(
                DMAChannelDir.MM2S,
                ch,
                _ping_pong(
                    b0, b1, cons, prod, offset=0, length=length, dimensions=order
                ),
            ),
        ]
    rt.add_tile_dma(TileDma(amt, amt_chans))

    # Flows route in the order they are added, and long flows need to go
    # first. A shim channel that carries two legs names its symbol on its
    # first flow.
    rt.add_flow(
        PacketFlow(
            _ShimPkt.to_rms,
            IT[3],
            rms_tile,
            src_channel=0,
            dst_channel=0,
            keep_pkt_header=False,
            shim_symbol="send_x",
        )
    )
    rt.add_flow(
        PacketFlow(
            _ShimPkt.to_rms,
            IT[3],
            rms_tile,
            src_channel=1,
            dst_channel=1,
            keep_pkt_header=False,
            shim_symbol="send_rms",
        )
    )
    rt.add_flow(
        PacketFlow(
            _ShimPkt.to_rope,
            IT[3],
            rope_tile,
            src_channel=0,
            dst_channel=1,
            keep_pkt_header=False,
            shim_symbol="send_rope_rms",
        )
    )
    _connect(rt, IT[3], 1, swa_rope_tile, 1, pkt_id=_ShimPkt.to_rope)
    _connect(rt, rms_tile, 0, proj_main_mt, 3, pkt_id=_X_FROM_RMS)

    proj_route()

    for dst, pk in (
        (glu_tile, _ProjPkt.to_glu),
        (rms_tile, _ProjPkt.to_rms),
        (rope_tile, _ProjPkt.to_rope),
        (swa_rope_tile, _ProjPkt.to_swa_rope),
    ):
        _connect(rt, proj_main_mt, 5, dst, 0, pkt_id=pk)

    # This token's k and v, out to the KV cache.
    rt.add_flow(
        Flow(rope_tile, IT[2], src_channel=1, dst_channel=0, shim_symbol="recv_k")
    )
    rt.add_flow(
        Flow(swa_rope_tile, IT[2], src_channel=1, dst_channel=1, shim_symbol="recv_v")
    )
    _connect(rt, attn_kv_tile, 0, proj_main_mt, 3, pkt_id=_X_FROM_ATTN)
    _connect(rt, swa_kv_tile, 0, proj_main_mt, 3, pkt_id=_X_FROM_ATTN)
    _connect(rt, glu_tile, 0, proj_main_mt, 3, pkt_id=_X_FROM_GLU)

    # The KV cache into MT[2]: packet 12 to the global buffers, 13 to the
    # sliding-window ones.
    rt.add_flow(
        PacketFlow(
            _KV_PKT_GLOBAL,
            IT[2],
            amt,
            src_channel=0,
            dst_channel=0,
            keep_pkt_header=False,
            shim_symbol="move_k",
        )
    )
    _connect(rt, IT[2], 0, amt, 2, pkt_id=_KV_PKT_SWA)
    rt.add_flow(
        PacketFlow(
            _KV_PKT_GLOBAL,
            IT[2],
            amt,
            src_channel=1,
            dst_channel=1,
            keep_pkt_header=False,
            shim_symbol="move_v",
        )
    )
    _connect(rt, IT[2], 1, amt, 3, pkt_id=_KV_PKT_SWA)
    _connect(rt, amt, 0, attn_qk_tile, 1)
    _connect(rt, amt, 1, attn_kv_tile, 1)
    _connect(rt, amt, 2, swa_qk_tile, 1)
    _connect(rt, amt, 3, swa_kv_tile, 1)

    # The per-layer-input path.
    rt.add_flow(
        Flow(IT[4], ple_tile, src_channel=0, dst_channel=0, shim_symbol="pli_rope_rms")
    )
    rt.add_flow(
        Flow(IT[4], ple_tile, src_channel=1, dst_channel=1, shim_symbol="pli_down")
    )
    _connect(rt, ple_tile, 1, plm_tile, 0)
    rt.add_flow(
        Flow(IT[5], gle_tile, src_channel=0, dst_channel=1, shim_symbol="pli_gate")
    )
    _connect(rt, gle_tile, 1, plm_tile, 1)
    _connect(rt, plm_tile, 0, plu_tile, 0)
    rt.add_flow(
        Flow(IT[5], plu_tile, src_channel=1, dst_channel=1, shim_symbol="pli_up")
    )
    # The layer output, out to x.
    rt.add_flow(
        Flow(plu_tile, IT[3], src_channel=0, dst_channel=0, shim_symbol="recv_y")
    )

    return Program(dev, rt, workers=workers).resolve_program()
