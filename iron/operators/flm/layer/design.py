# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's fused decode layer on the whole array: one token through one layer.

The design reproduces the xclbin and the runtime sequence of FastFlowLM's
fused decode layer.

One core runs each stage: RMS norm and residual, RoPE for the global and the
sliding-window layers, 16 q4nx projection cores, GLU, the per-layer-input
path, and one attention pair (qk and kv) for each attention kind. The runtime
sequence writes the layer type into RTPs. It then streams the weights, the KV
cache and the hidden state.
"""

from dataclasses import dataclass
from enum import IntEnum
from functools import partial
from typing import NamedTuple

import numpy as np
from aie.dialects import arith
from aie.dialects.aie import DMAChannelDir
from aie.dialects.aiex import _as_i32, npu_write32
from aie.extras.dialects.arith import constant
from aie.helpers.npdtypes import np_ndarray_type_get_shape
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Acquire,
    Bd,
    Buffer,
    DispatchTime,
    DmaChannel,
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
from aie.iron.dataflow import Flow, PacketFlow
from aie.iron.device import Tile
from aie.iron.kernels import (
    FLM_GEMMA4_E2B_DECODE,
    FLM_GEMMA4_E4B_DECODE,
    FlmGemma4DecodeGeometry,
    flm_gemma4,
)
from ml_dtypes import bfloat16

from iron.operators.flm import q4nx
from iron.operators.flm.dataflow import ping_pong

LAYER_TYPES = ("global", "swa", "global_skip", "swa_skip")

# The KV cache rows that the runtime sequence's buffer types allow. The
# sequence takes the row count, max_l, at dispatch.
MAX_CONTEXT = 32768
SLIDING_WINDOW = 512

# The L1 address of each RTP, per geometry, from FastFlowLM's address book. The
# runtime sequence writes the RTPs at these addresses.
#
# The allocator places four unpinned RTP buffers at other addresses. The
# sequence's writes then land in other buffers.
#
# The design pins every RTP buffer at its address.
RTP_ADDRESSES = {
    FLM_GEMMA4_E2B_DECODE: {
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
    FLM_GEMMA4_E4B_DECODE: {
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

# The symbol of each RTP buffer, by RTP_ADDRESSES key. proj_swa and proj_skip
# have one symbol per projection core.
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

# One q4nx block in bf16 elements, the unit the weight buffers are typed in.
W_BLOCK = q4nx.BLOCK_BYTES // 2
# The projections' input slice. Every projection's input dimension is a
# multiple of it.
X_SLICE = 256
# Keys per attention round.
LK = 16
# The padding in the engine's per-layer-input stream (gemma4e_npu_sequence.hpp).
MIN_BF16_PAD = 32
# The columns of the projection cores. Each column holds four cores in rows 2
# to 5. The column's shim tile and memtile feed them weights.
PROJ_COLS = (0, 1, 6, 7)

# The tile of each stage, as (column, row). Row 0 holds the shim tiles, row 1
# the memtiles and rows 2 to 5 the cores.
PLACEMENT = {
    # Cores.
    "attn_qk": (2, 2),
    "attn_kv": (2, 3),
    "swa_attn_qk": (2, 4),
    "swa_attn_kv": (2, 5),
    "rms": (3, 2),
    "glu": (3, 3),
    "rope": (3, 4),
    "swa_rope": (3, 5),
    "pl_gate": (4, 2),
    "pl_embedding": (4, 3),
    "pl_up": (5, 2),
    "pl_merge": (5, 3),
    # Memtiles.
    "proj_gather_0": (0, 1),
    "proj_x": (1, 1),
    "attn_mem": (2, 1),
    "proj_gather_1": (6, 1),
    "proj_weight": (7, 1),
    # Shim tiles.
    "kv_shim": (2, 0),
    "x_shim": (3, 0),
    "pl_shim_0": (4, 0),
    "pl_shim_1": (5, 0),
}

_BF16 = np.dtype[bfloat16]
_RTP_TY = np.ndarray[(16,), np.dtype[np.int32]]

# Core locks, by the name of the factory argument that gives the kernel the id.
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
# The lock of the DMA's second norm_w BD. No kernel takes it.
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

# The RMS, GLU and projection cores acquire this lock before they read their
# RTPs. The sequence sets it after it writes them. The RoPE and attention
# cores read their RTPs after data from the projection cores arrives.
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


def layer_kernels(geometry):
    """The flm_gemma4_decode_* kernels that this design's cores link, by kernel name.

    The factories build for the selected device. The global attention kernels
    depend on the geometry's KV head count.
    """
    two_kv = geometry.num_kv_heads == 2
    qk_handshake = "l_prod_lock" if two_kv else "l_cons_lock"

    def build(factory, locks, **kwargs):
        return factory(geometry=geometry, **locks, **kwargs)

    attn_qk_locks = {**ATTN_QK_LOCKS, qk_handshake: ATTN_HANDSHAKE_LOCK}
    swa_qk_locks = {**ATTN_QK_LOCKS, "l_cons_lock": ATTN_HANDSHAKE_LOCK}
    return {
        "rms_residual": build(flm_gemma4.flm_gemma4_decode_rms_residual, RMS_LOCKS),
        "rope": build(flm_gemma4.flm_gemma4_decode_rope, ROPE_LOCKS),
        "swa_rope": build(
            flm_gemma4.flm_gemma4_decode_rope, ROPE_LOCKS, sliding_window=True
        ),
        "proj_layer_embedding": build(
            flm_gemma4.flm_gemma4_decode_proj_layer_embedding, PLE_LOCKS
        ),
        "gate_layer_embedding": build(
            flm_gemma4.flm_gemma4_decode_gate_layer_embedding, GLE_LOCKS
        ),
        "per_layer_up": build(flm_gemma4.flm_gemma4_decode_per_layer_up, PLU_LOCKS),
        "glu": build(flm_gemma4.flm_gemma4_decode_glu, GLU_LOCKS),
        "proj_main": build(flm_gemma4.flm_gemma4_decode_proj_main, PROJ_LOCKS),
        "attn_kv": build(
            (
                flm_gemma4.flm_gemma4_decode_attn_kv_kvh2
                if two_kv
                else flm_gemma4.flm_gemma4_decode_attn_kv
            ),
            ATTN_KV_LOCKS,
        ),
        "attn_qk": build(
            (
                flm_gemma4.flm_gemma4_decode_attn_qk_kvh2
                if two_kv
                else flm_gemma4.flm_gemma4_decode_attn_qk
            ),
            attn_qk_locks,
        ),
        "swa_attn_kv": build(flm_gemma4.flm_gemma4_decode_swa_attn_kv, ATTN_KV_LOCKS),
        "swa_attn_qk": build(
            flm_gemma4.flm_gemma4_decode_attn_qk, swa_qk_locks, sliding_window=True
        ),
    }


class BlobWeight(NamedTuple):
    """One weight matrix in the engine's weight blob.

    offset and size count bf16 elements. dout and din give the matrix shape.
    """

    offset: int
    size: int
    dout: int
    din: int


def weight_layout(geometry, layer_type):
    """The weights in the blob that the sequence reads from proj, in blob order.

    The engine packs one blob per layer: qkv, o, up_gate and down in q4nx,
    then the per-layer-input down, gate and up projections in bf16. qkv is
    q alone on a skip layer. A skip layer with double_wide_mlp has twice the
    intermediate size.
    """
    g = geometry
    is_swa = layer_type in ("swa", "swa_skip")
    is_skip = layer_type in ("global_skip", "swa_skip")
    D = g.model_dim
    dh = g.swa_dh if is_swa else g.dh
    dq, dk = g.num_attn_heads * dh, g.num_kv_heads * dh
    inter = g.intermediate_size * (2 if is_skip and g.double_wide_mlp else 1)
    shapes = {
        "qkv": (dq if is_skip else dq + 2 * dk, D, True),
        "o": (D, dq, True),
        "up_gate": (2 * inter, D, True),
        "down": (D, inter, True),
        "pli_down": (g.pli_d, D, False),
        "pli_gate": (g.pli_d, D, False),
        "pli_up": (D, g.pli_d, False),
    }
    layout, offset = {}, 0
    for name, (dout, din, packed) in shapes.items():
        size = q4nx.packed_bytes(dout * din) // 2 if packed else dout * din
        layout[name] = BlobWeight(offset, size, dout, din)
        offset += size
    return layout


def arg_sizes(geometry):
    """Upper bounds on the element counts of the sequence's buffers, by name.

    The four layer types share one xclbin. proj therefore holds the largest
    blob of the four.
    """
    D, pli = geometry.model_dim, geometry.pli_d
    dk = geometry.num_kv_heads * geometry.dh
    proj = max(
        w.offset + w.size
        for t in LAYER_TYPES
        for w in weight_layout(geometry, t).values()
    )
    return {
        "x": 3 * D,
        "proj": proj,
        "rms": 4 * D,
        "rope_rms": 3 * geometry.dh + pli * 2 + D + 64,
        "kv": 2 * dk * MAX_CONTEXT,
    }


def _single_bd(direction, channel, buf, acq, rel, **bd_args):
    """A DMA channel of one BD that repeats behind one lock pair."""
    return DmaChannel(
        direction,
        channel,
        [Bd(buf, acquires=[Acquire(acq)], releases=[Release(rel)], **bd_args)],
    )


def _call_kernel(*args):
    """A core body that calls the kernel, its last argument, on the others."""
    args[-1](*args[:-1])


def _connect(
    rt, src, src_ch, dst, dst_ch, pkt_id=None, keep_pkt_header=False, name=None
):
    """Add a circuit-switched flow, or a packet flow when pkt_id is set.

    Returns:
        The flow.
    """
    ends = dict(src_channel=src_ch, dst_channel=dst_ch, name=name)
    if pkt_id is None:
        flow = Flow(src, dst, **ends)
    else:
        flow = PacketFlow(pkt_id, src, dst, keep_pkt_header=keep_pkt_header, **ends)
    rt.add_flow(flow)
    return flow


@dataclass
class _Ctx:
    """The state that every stage builder adds to."""

    rt: Runtime
    workers: list
    g: FlmGemma4DecodeGeometry
    rtp: dict
    kernels: dict

    def entry(self, name, symbol):
        """The entry point ``symbol`` of the kernel ``name``, typed by its factory."""
        return getattr(self.kernels[name], symbol)

    def rtp_buffer(self, tile, key, name=None):
        """The RTP buffer of RTP_ADDRESSES key ``key``, pinned at its address."""
        return Buffer(
            type=_RTP_TY,
            name=name or RTP_SYMBOLS[key],
            tile=tile,
            use_write_rtp=True,
            address=self.rtp[key],
        )

    def add_locks(self, tile, ids_inits):
        """The tile's locks, one per (lock id, init) pair."""
        out = [Lock(tile=tile, lock_id=i, init=init) for i, init in ids_inits]
        for lock in out:
            self.rt.add_lock(lock)
        return out

    def locks(self, tile, table, inits):
        """The tile's locks named in ``table``, with ``inits`` by name."""
        ids_inits = [(table[name], init) for name, init in inits.items()]
        return dict(zip(inits, self.add_locks(tile, ids_inits)))


def _ceil_mul(v, chunk):
    """v rounded up to a multiple of chunk."""
    # The C++ generator cannot lower the floordivsi that `//` emits.
    return arith.divsi(v + (chunk - 1), _as_i32(chunk)) * chunk


def _mask_ge(v, bound):
    """All ones if v >= bound, else 0."""
    return arith.shrsi(_as_i32(bound - 1) - v, _as_i32(31))


def _min_const(v, bound):
    """min(v, bound). The C++ generator cannot lower arith.minsi."""
    d = v - _as_i32(bound)
    return _as_i32(bound) + arith.andi(d, arith.shrsi(d, _as_i32(31)))


def _sequence(
    g,
    rtp,
    layer_type,
    sliding_window,
    shim,
    x_arg,
    proj_arg,
    rms_arg,
    rope_rms_arg,
    kv_arg,
    len_arg,
    max_l_arg,
):
    """The runtime sequence of one ``layer_type`` dispatch.

    The sequence writes the RTPs, then starts the shim DMA legs in the order of
    the engine's gen_layer_seq. ``shim`` holds the shim flows by name. Offsets
    and lengths count bf16 elements. L counts the tokens up to and including
    this one.
    """
    IS_SWA = layer_type in ("swa", "swa_skip")
    IS_SKIP = layer_type in ("global_skip", "swa_skip")
    D = g.model_dim
    L = _as_i32(len_arg) + 1
    MAX_L_v = _as_i32(max_l_arg)
    SW = sliding_window
    DH = g.swa_dh if IS_SWA else g.dh
    DK = g.num_kv_heads * DH
    weights = weight_layout(g, layer_type)

    require(_as_i32(len_arg) >= 0, "context_len must be >= 0")
    require(MAX_L_v <= MAX_CONTEXT, f"max_l exceeds {MAX_CONTEXT}")
    if not IS_SWA:
        require(L <= MAX_L_v, "context_len must be below max_l")

    for c in PROJ_COLS:
        for r in (2, 3, 4, 5):
            npu_write32(rtp["proj_swa"], int(IS_SWA), column=c, row=r)
            npu_write32(rtp["proj_skip"], int(IS_SKIP), column=c, row=r)
            npu_write32(RTP_SYNC_LOCK_ADDR, 1, column=c, row=r)

    def write(stage, addr, value):
        col, row = PLACEMENT[stage]
        npu_write32(addr, value, column=col, row=row)

    L_local = _min_const(L, SW) if IS_SWA else L
    write("attn_qk", rtp["l_qk"], L_local)
    write("attn_kv", rtp["l_kv"], L_local)
    write("swa_attn_qk", rtp["swa_l_qk"], L_local)
    write("swa_attn_kv", rtp["swa_l_kv"], L_local)
    write("rms", rtp["rms_swa"], int(IS_SWA))
    write("rms", rtp["rms_skip"], int(IS_SKIP))
    write("rope", rtp["rope_skip_kv"], int(IS_SKIP))
    write("swa_rope", rtp["swa_rope_skip_kv"], int(IS_SKIP))
    write("glu", rtp["glu_skip"], int(IS_SKIP and g.double_wide_mlp))
    write("rms", RTP_SYNC_LOCK_ADDR, 1)
    write("glu", RTP_SYNC_LOCK_ADDR, 1)

    # The sequence keeps two rounds of legs in flight, as the engine's
    # bd_offset double buffer does. A shim tile has 16 BDs.
    DEPTH_ROUNDS = 2
    window = []

    def flush(force=False):
        while len(window) > (0 if force else DEPTH_ROUNDS):
            tasks = window.pop(0)
            for task, token in tasks:
                if token:
                    task.await_()
            for task, _ in tasks:
                task.free()

    def emit(*legs):
        """Keep one round of started legs in flight."""
        window.append(legs)
        flush()

    def leg(flow, mem, off, length, token=True):
        """A (task, token) pair: ``mem[off : off + length]`` into ``shim[flow]``."""
        task = shim[flow].fill(
            mem, tap=mem[off : off + length], wait=token, managed=False
        )
        return task, token

    emit(leg("send_x", x_arg, 0, D))
    emit(leg("send_rms", rms_arg, 0, 4 * D))
    # The RoPE weights go out on the channel whose flow reaches this layer
    # type's RoPE tile.
    emit(leg("send_rms_rope" if IS_SWA else "send_x_rope", rope_rms_arg, 0, 3 * DH))
    recv_y = shim["recv_y"].drain(x_arg, tap=x_arg[:D], wait=True, managed=False)

    def move_weights(w):
        """The engine's _move_weights: a round is 2 legs to each proj column."""
        bpr = w.din // q4nx.K_TILE
        # One core's M_TILE output rows, in bf16 elements.
        stripe = bpr * W_BLOCK
        cores = len(PROJ_COLS) * 4
        for rnd in range(w.dout // q4nx.M_TILE // cores):
            legs = []
            for ci, col in enumerate(PROJ_COLS):
                for half in (0, 1):
                    off = w.offset + (rnd * cores + ci * 4 + 2 * half) * stripe
                    legs.append(leg(f"proj_w{half}_{col}", proj_arg, off, 2 * stripe))
            emit(*legs)

    def pli_leg(name):
        """One leg over the bf16 weight ``name``, on the shim flow ``name``."""
        return leg(name, proj_arg, weights[name].offset, weights[name].size)

    v_cache_off = DK * SW if IS_SWA else MAX_L_v * DK
    move_weights(weights["qkv"])
    if not IS_SKIP:
        # recv_k carries the global layers' k and v, recv_v the sliding-window
        # layers'.
        L_off = (arith.andi(L - 1, _as_i32(SW - 1)) if IS_SWA else (L - 1)) * DK
        recv = "recv_v" if IS_SWA else "recv_k"
        for off in (L_off, L_off + v_cache_off):
            task = shim[recv].drain(
                kv_arg, tap=kv_arg[off : off + DK], wait=True, managed=False
            )
            emit((task, True))
    emit(leg("pli_rope_rms", rope_rms_arg, 3 * DH, g.pli_d * 2 + D + MIN_BF16_PAD))
    # x reuses pli_rope_rms's channel as a second BD.
    emit(leg("pli_rope_rms", x_arg, 2 * D, D, token=False))
    emit(pli_leg("pli_down"))
    # The KV cache into the attention memtile.
    move_k, move_v = ("move_k_swa", "move_v_swa") if IS_SWA else ("move_k", "move_v")
    if not IS_SWA:
        d2m = _ceil_mul(L, LK) * DK
        emit(leg(move_k, kv_arg, 0, d2m))
        emit(leg(move_v, kv_arg, v_cache_off, d2m))
    else:
        # The sliding-window cache is a ring of `rows` rows. Its oldest row is
        # `start`. Phase 1 sends rows start..rows-1. Phase 2 sends rows
        # 0..start-1. The sequence cannot branch on L, so masks select the
        # phase bounds. mlir-aie rejects a zero-length BD. When start is 0,
        # phase 1 therefore ends one row early and phase 2 sends the last row.
        # Both phases feed one stream into the memtile, so the split point
        # does not change the data the memtile receives.
        _m = _mask_ge(L, SW)
        _nm = arith.xori(_m, _as_i32(-1))
        _lb = arith.andi(L, _as_i32(SW - 1))
        _Lp = arith.andi(L + (LK - 1), _as_i32(-LK))
        rows = arith.ori(arith.andi(_m, _as_i32(SW)), arith.andi(_nm, _Lp))
        start = arith.andi(_m, _lb)
        # All ones if start is 0, else 0.
        _z = arith.xori(_mask_ge(start, 1), _as_i32(-1))
        p1_off = start * DK
        p1_len = (rows - start) * DK - arith.andi(_z, _as_i32(DK))
        p2_off = arith.andi(_z, p1_len)
        p2_len = arith.ori(start * DK, arith.andi(_z, _as_i32(DK)))
        emit(leg(move_k, kv_arg, p1_off, p1_len))
        emit(leg(move_v, kv_arg, p1_off + v_cache_off, p1_len))
        emit(leg(move_k, kv_arg, p2_off, p2_len, token=False))
        emit(leg(move_v, kv_arg, p2_off + v_cache_off, p2_len, token=False))
    for name in ("o", "up_gate", "down"):
        move_weights(weights[name])
    emit(pli_leg("pli_gate"))
    emit(pli_leg("pli_up"))
    flush(force=True)
    recv_y.await_()
    recv_y.free()


def _build_rms(ctx, rms_tile):
    """RMS norm and residual. Returns y_out, the layer output the gate tile reads.

    x arrives on S2MM 0, the norm weights on S2MM 1. y leaves on MM2S 0
    behind its packet header.
    """
    rms_k = ctx.entry("rms_residual", "rms_residual")
    rms_y_pkt_ty, rms_x_ty, _, _, rms_w_ty, rms_x_buf_ty, _, _ = rms_k.arg_types()
    rms_name = f"{rms_tile.row}_{rms_tile.col}"
    rms_x_ping = Buffer(type=rms_x_ty, name=f"x_ping_{rms_name}", tile=rms_tile)
    rms_x_pong = Buffer(type=rms_x_ty, name=f"x_pong_{rms_name}", tile=rms_tile)
    rms_x_buf = Buffer(type=rms_x_buf_ty, name=f"x_buf_{rms_name}", tile=rms_tile)
    rms_w = Buffer(type=rms_w_ty, name=f"w_buffer_{rms_name}", tile=rms_tile)
    rms_y_out = Buffer(type=rms_x_ty, name=f"y_out_{rms_name}", tile=rms_tile)
    rms_y = Buffer(type=rms_y_pkt_ty, name=f"y_{rms_name}", tile=rms_tile)
    rms_is_swa = ctx.rtp_buffer(rms_tile, "rms_swa")
    rms_skip = ctx.rtp_buffer(rms_tile, "rms_skip")
    rl = ctx.locks(
        rms_tile,
        RMS_LOCKS,
        dict(
            w_prod_lock=1,
            w_cons_lock=0,
            y_prod_lock=0,
            y_cons_lock=0,
            x_prod_lock=2,
            x_cons_lock=0,
            # No DMA takes these three. lm_head_out_* hand y_out to the gate
            # tile's kernel.
            rtp_available_lock=0,
            lm_head_out_prod_lock=1,
            lm_head_out_cons_lock=0,
        ),
    )

    ctx.workers.append(
        Worker(
            _call_kernel,
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
            stack_size=1024 * 4,
        )
    )
    ctx.rt.add_tile_dma(
        TileDma(
            rms_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    ping_pong(
                        rms_x_ping,
                        rms_x_pong,
                        rl["x_prod_lock"],
                        rl["x_cons_lock"],
                    ),
                ),
                _single_bd(
                    DMAChannelDir.S2MM,
                    1,
                    rms_w,
                    rl["w_prod_lock"],
                    rl["w_cons_lock"],
                ),
                _single_bd(
                    DMAChannelDir.MM2S,
                    0,
                    rms_y,
                    rl["y_cons_lock"],
                    rl["y_prod_lock"],
                    tap=TensorAccessPattern.full(rms_y.shape)[14:],
                ),
            ],
        )
    )
    return rms_y_out


def _build_rope(ctx, rope_tile, name, rtp_key, dh, q_fifo):
    """RoPE, global or sliding-window.

    qkv arrives on S2MM 0, the RoPE weights on S2MM 1. q leaves through
    q_fifo to the qk core, k and v on MM2S 1.
    """
    kern = ctx.entry(name, "rope")
    q_ty, kv_ty, _, qkv_ty, _, rope_ty, _ = kern.arg_types()

    r, c = rope_tile.row, rope_tile.col
    qkv_0 = Buffer(type=qkv_ty, name=f"qkv_buffer_0_{r}_{c}", tile=rope_tile)
    qkv_1 = Buffer(type=qkv_ty, name=f"qkv_buffer_1_{r}_{c}", tile=rope_tile)
    k_buf = Buffer(type=kv_ty, name=f"k_buffer_{r}_{c}", tile=rope_tile)
    v_buf = Buffer(type=kv_ty, name=f"v_buffer_{r}_{c}", tile=rope_tile)
    rope_buf = Buffer(type=rope_ty, name=f"rope_buffer_{r}_{c}", tile=rope_tile)
    skip_kv = ctx.rtp_buffer(rope_tile, rtp_key)
    lk = ctx.locks(
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
    ctx.add_locks(rope_tile, [(ROPE_Q_PASS_LOCK, 0)])

    def rope_body(q_h, kk, v, q0, q1, rope, skip, kern):
        q = q_h.acquire(1)
        kern(q, kk, v, q0, q1, rope, skip)
        q_h.release(1)

    ctx.workers.append(
        Worker(
            rope_body,
            [q_fifo.prod(), k_buf, v_buf, qkv_0, qkv_1, rope_buf, skip_kv, kern],
            tile=rope_tile,
            stack_size=1024 * 4,
        )
    )
    ctx.rt.add_tile_dma(
        TileDma(
            rope_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    ping_pong(qkv_0, qkv_1, lk["qkv_prod_lock"], lk["qkv_cons_lock"]),
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
                _single_bd(
                    DMAChannelDir.S2MM,
                    1,
                    rope_buf,
                    lk["rope_prod_lock"],
                    lk["rope_cons_lock"],
                ),
            ],
        )
    )


def _build_pl_embedding(ctx, ple_tile):
    """Per-layer-input embedding.

    x0_per_layer, the norm weights and x0 arrive on S2MM 0 as a 4-BD cycle,
    the weights on S2MM 1. y leaves on MM2S 1.
    """
    PLI_D = ctx.g.pli_d
    ple_name = f"{ple_tile.row}_{ple_tile.col}"
    ple_k = ctx.entry("proj_layer_embedding", "proj_layer_embedding")
    ple_norm_w_ty, ple_x0_pl_ty, ple_x0_ty, _, ple_y_ty, w_ty, _ = ple_k.arg_types()
    ple_norm_w = Buffer(type=ple_norm_w_ty, name=f"norm_w_{ple_name}", tile=ple_tile)
    ple_x0_pl = Buffer(
        type=ple_x0_pl_ty, name=f"x0_per_layer_{ple_name}", tile=ple_tile
    )
    ple_x0 = Buffer(type=ple_x0_ty, name=f"x0_{ple_name}", tile=ple_tile)
    ple_x_proj = Buffer(type=ple_x0_pl_ty, name=f"x_proj_{ple_name}", tile=ple_tile)
    ple_y = Buffer(type=ple_y_ty, name=f"y_{ple_name}", tile=ple_tile)
    ple_w0 = Buffer(type=w_ty, name=f"proj_w_0_{ple_name}", tile=ple_tile)
    ple_w1 = Buffer(type=w_ty, name=f"proj_w_1_{ple_name}", tile=ple_tile)
    pl = ctx.locks(
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
    (ple_norm_w_p2,) = ctx.add_locks(ple_tile, [(PLE_NORM_W_P2_LOCK, 0)])

    ctx.workers.append(
        Worker(
            _call_kernel,
            [ple_norm_w, ple_x0_pl, ple_x0, ple_x_proj, ple_y, ple_w0, ple_w1, ple_k],
            tile=ple_tile,
            stack_size=1024 * 4,
        )
    )
    ctx.rt.add_tile_dma(
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
                            tap=TensorAccessPattern.full(ple_norm_w.shape)[:PLI_D],
                            acquires=[Acquire(pl["norm_w_prod_lock"])],
                            releases=[Release(ple_norm_w_p2)],
                            next=2,
                        ),
                        Bd(
                            ple_norm_w,
                            tap=TensorAccessPattern.full(ple_norm_w.shape)[PLI_D:],
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
                    ping_pong(
                        ple_w0,
                        ple_w1,
                        pl["proj_w_prod_lock"],
                        pl["proj_w_cons_lock"],
                    ),
                ),
                _single_bd(
                    DMAChannelDir.MM2S, 1, ple_y, pl["y_cons_lock"], pl["y_prod_lock"]
                ),
            ],
        )
    )


def _build_pl_gate(ctx, gle_tile, x):
    """Per-layer-input gate.

    x is the RMS tile's y_out. The weights arrive on S2MM 1. y leaves on
    MM2S 1.
    """
    gle_name = f"{gle_tile.row}_{gle_tile.col}"
    gle_k = ctx.entry("gate_layer_embedding", "gate_layer_embedding")
    _, w_ty, _, gle_y_ty = gle_k.arg_types()
    gle_w0 = Buffer(type=w_ty, name=f"proj_w_0_{gle_name}", tile=gle_tile)
    gle_w1 = Buffer(type=w_ty, name=f"proj_w_1_{gle_name}", tile=gle_tile)
    gle_y = Buffer(type=gle_y_ty, name=f"y_{gle_name}", tile=gle_tile)
    gl = ctx.locks(
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

    ctx.workers.append(
        Worker(
            _call_kernel,
            [x, gle_w0, gle_w1, gle_y, gle_k],
            tile=gle_tile,
            stack_size=1024 * 4,
        )
    )
    ctx.rt.add_tile_dma(
        TileDma(
            gle_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    ping_pong(
                        gle_w0,
                        gle_w1,
                        gl["proj_w_prod_lock"],
                        gl["proj_w_cons_lock"],
                    ),
                ),
                _single_bd(
                    DMAChannelDir.MM2S, 1, gle_y, gl["y_cons_lock"], gl["y_prod_lock"]
                ),
            ],
        )
    )


def _build_pl_merge(ctx, plm_tile):
    """Per-layer-input merge.

    The tile runs no kernel. Its DMA gathers the embedding and the gate
    outputs into one buffer and sends the buffer to the up projection.
    """
    D, PLI_D = ctx.g.model_dim, ctx.g.pli_d
    plm_dual_y_ty = np.ndarray[(2 * (PLI_D + D) + 32,), _BF16]
    plm_y = Buffer(
        type=plm_dual_y_ty, name=f"y_{plm_tile.row}_{plm_tile.col}", tile=plm_tile
    )
    plm_norm_i_prod, plm_res_gate_prod, plm_cons = ctx.add_locks(
        plm_tile, [(0, 1), (1, 0), (2, 0)]
    )
    ctx.rt.add_tile_dma(
        TileDma(
            plm_tile,
            [
                _single_bd(
                    DMAChannelDir.S2MM,
                    0,
                    plm_y,
                    plm_norm_i_prod,
                    plm_res_gate_prod,
                    tap=TensorAccessPattern.full(plm_y.shape)[: D + PLI_D + 32],
                ),
                _single_bd(
                    DMAChannelDir.S2MM,
                    1,
                    plm_y,
                    plm_res_gate_prod,
                    plm_cons,
                    tap=TensorAccessPattern.full(plm_y.shape)[D + PLI_D + 32 :],
                ),
                _single_bd(DMAChannelDir.MM2S, 0, plm_y, plm_cons, plm_norm_i_prod),
            ],
        )
    )


def _build_pl_up(ctx, plu_tile):
    """Per-layer-input up projection.

    x arrives on S2MM 0, the weights on S2MM 1. The layer output leaves on
    MM2S 0.
    """
    plu_name = f"{plu_tile.row}_{plu_tile.col}"
    plu_k = ctx.entry("per_layer_up", "per_layer_up")
    plu_dual_x_ty, w_ty, _, plu_y_ty = plu_k.arg_types()
    plu_x = Buffer(type=plu_dual_x_ty, name=f"x_{plu_name}", tile=plu_tile)
    plu_y = Buffer(type=plu_y_ty, name=f"y_{plu_name}", tile=plu_tile)
    plu_w0 = Buffer(type=w_ty, name=f"proj_w_0_{plu_name}", tile=plu_tile)
    plu_w1 = Buffer(type=w_ty, name=f"proj_w_1_{plu_name}", tile=plu_tile)
    ul = ctx.locks(
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

    ctx.workers.append(
        Worker(
            _call_kernel,
            [plu_x, plu_w0, plu_w1, plu_y, plu_k],
            tile=plu_tile,
            stack_size=1024 * 4,
        )
    )
    ctx.rt.add_tile_dma(
        TileDma(
            plu_tile,
            [
                _single_bd(
                    DMAChannelDir.S2MM, 0, plu_x, ul["x_prod_lock"], ul["x_cons_lock"]
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    ping_pong(
                        plu_w0,
                        plu_w1,
                        ul["proj_w_prod_lock"],
                        ul["proj_w_cons_lock"],
                    ),
                ),
                _single_bd(
                    DMAChannelDir.MM2S, 0, plu_y, ul["y_cons_lock"], ul["y_prod_lock"]
                ),
            ],
        )
    )


def _build_glu(ctx, glu_tile):
    """GLU.

    gate and up arrive on S2MM 0. The activations leave on MM2S 0 with a
    packet header to the projection engine.
    """
    glu_name = f"{glu_tile.row}_{glu_tile.col}"
    glu_k = ctx.entry("glu", "glu")
    glu_hid_ty, glu_up_gate_ty, _, glu_y_ty, _, _ = glu_k.arg_types()
    glu_x_0 = Buffer(type=glu_up_gate_ty, name=f"x_0_{glu_name}", tile=glu_tile)
    glu_x_1 = Buffer(type=glu_up_gate_ty, name=f"x_1_{glu_name}", tile=glu_tile)
    glu_y_0 = Buffer(type=glu_y_ty, name=f"y_0_{glu_name}", tile=glu_tile)
    glu_y_1 = Buffer(type=glu_y_ty, name=f"y_1_{glu_name}", tile=glu_tile)
    glu_hid = Buffer(type=glu_hid_ty, name=f"hid_0_{glu_name}", tile=glu_tile)
    glu_is_skip = ctx.rtp_buffer(glu_tile, "glu_skip")
    ll = ctx.locks(
        glu_tile,
        GLU_LOCKS,
        dict(x_prod_lock=2, x_cons_lock=0, y_prod_lock=2, y_cons_lock=0, rtp_lock=0),
    )

    ctx.workers.append(
        Worker(
            _call_kernel,
            [glu_hid, glu_x_0, glu_x_1, glu_y_0, glu_y_1, glu_is_skip, glu_k],
            tile=glu_tile,
            stack_size=4 * 1024,
        )
    )
    ctx.rt.add_tile_dma(
        TileDma(
            glu_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    ping_pong(glu_x_0, glu_x_1, ll["x_prod_lock"], ll["x_cons_lock"]),
                ),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    0,
                    ping_pong(
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


def _build_proj_core(ctx, pt, kern, send_x_out, main_y0=None, main_y1=None):
    """One q4nx projection core. Returns its y buffers (y0, y1).

    A core that does not send y fills the second slot of main_y0 and main_y1,
    the y buffers of the sending core in the row below.
    """
    r, c = pt.row, pt.col
    y_ty, w_ty, x_ty = kern.arg_types()[:3]
    is_swa = ctx.rtp_buffer(pt, "proj_swa", f"RTP_PROJ_IS_SWA_BUFFER_{r}_{c}")
    skip_kv = ctx.rtp_buffer(pt, "proj_skip", f"RTP_PROJ_SKIP_KV_BUFFER_{r}_{c}")
    x0 = Buffer(type=x_ty, name=f"x_0_{r}_{c}", tile=pt)
    w0 = Buffer(type=w_ty, name=f"w_0_{r}_{c}", tile=pt)
    x1 = Buffer(type=x_ty, name=f"x_1_{r}_{c}", tile=pt)
    w1 = Buffer(type=w_ty, name=f"w_1_{r}_{c}", tile=pt)
    if send_x_out:
        y0 = Buffer(type=y_ty, name=f"y_0_{r}_{c}", tile=pt)
        y1 = Buffer(type=y_ty, name=f"y_1_{r}_{c}", tile=pt)
    else:
        y0, y1 = main_y0, main_y1
    pk = ctx.locks(
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

    def proj_body(yy0, ww0, xx0, yy1, ww1, xx1, sw, sk, kern):
        kern(yy0, ww0, xx0, yy1, ww1, xx1, sw, sk, constant(int(send_x_out)))

    ctx.workers.append(
        Worker(
            proj_body,
            [y0, w0, x0, y1, w1, x1, is_swa, skip_kv, kern],
            tile=pt,
            stack_size=10 * 1024,
        )
    )
    chans = [
        DmaChannel(
            DMAChannelDir.S2MM,
            0,
            ping_pong(x0, x1, pk["x_prod_lock"], pk["x_cons_lock"]),
        ),
        DmaChannel(
            DMAChannelDir.S2MM,
            1,
            ping_pong(w0, w1, pk["w_prod_lock"], pk["w_cons_lock"]),
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
                        tap=TensorAccessPattern.full(y.shape)[14:],
                        acquires=[Acquire(pk[f"y_cons_{half}_lock"], value=2)],
                        releases=[Release(pk[f"y_prod_{half}_lock"], value=2)],
                        next=nxt,
                    )
                    for y, half, nxt in ((y0, "ping", 1), (y1, "pong", 0))
                ],
            )
        )
    ctx.rt.add_tile_dma(TileDma(pt, chans))
    return y0, y1


def _build_proj_cores(ctx, grid):
    """The q4nx projection engine: 16 cores in PROJ_COLS.

    The cores in rows 2 and 4 send y. Returns the sending cores of each group
    of two columns.
    """
    proj_k = ctx.entry("proj_main", "proj_main")

    proj_send_tiles = []
    for grp in range(2):
        group_send = []
        for csub in (0, 1):
            col = PROJ_COLS[2 * grp + csub]
            for row_pair in range(2):
                send_t = grid[col, 2 + row_pair * 2]
                nosend_t = grid[col, 3 + row_pair * 2]
                y0, y1 = _build_proj_core(ctx, send_t, proj_k, send_x_out=True)
                _build_proj_core(
                    ctx, nosend_t, proj_k, send_x_out=False, main_y0=y0, main_y1=y1
                )
                group_send.append(send_t)
        proj_send_tiles.append(group_send)
    return proj_send_tiles


_LINEAR_4W_TY = np.ndarray[(4 * W_BLOCK,), _BF16]
# (lock id, init) of a projection memtile's weight locks.
_PROJ_MEM_W_LOCKS = [(5, 2), (6, 0), (7, 0), (8, 2), (9, 0), (10, 0)]


def _proj_weight_channels(w0, w1, wp0, wp0c0, wp0c1, wp1, wp1c0, wp1c1):
    """A projection memtile's weight channels.

    Each weight half arrives on S2MM 4 or 5 and leaves as two blocks, one to
    each of two cores.
    """
    w = TensorAccessPattern.full(w0.shape)
    return {
        "in0": DmaChannel(
            DMAChannelDir.S2MM,
            4,
            ping_pong(w0, w1, wp0, wp0c0, tap=w[: 2 * W_BLOCK]),
        ),
        "in1": DmaChannel(
            DMAChannelDir.S2MM,
            5,
            ping_pong(w0, w1, wp1, wp1c0, tap=w[2 * W_BLOCK :]),
        ),
        "out": [
            DmaChannel(
                DMAChannelDir.MM2S,
                0,
                ping_pong(w0, w1, wp0c0, wp0c1, tap=w[:W_BLOCK]),
            ),
            DmaChannel(
                DMAChannelDir.MM2S,
                1,
                ping_pong(w0, w1, wp0c1, wp0, tap=w[W_BLOCK : 2 * W_BLOCK]),
            ),
            DmaChannel(
                DMAChannelDir.MM2S,
                2,
                ping_pong(w0, w1, wp1c0, wp1c1, tap=w[2 * W_BLOCK : 3 * W_BLOCK]),
            ),
            DmaChannel(
                DMAChannelDir.MM2S,
                3,
                ping_pong(w0, w1, wp1c1, wp1, tap=w[3 * W_BLOCK :]),
            ),
        ],
    }


def _proj_weight_buffers(mt):
    """A projection memtile's weight ping and pong buffers."""
    r, c = mt.row, mt.col
    w0 = Buffer(type=_LINEAR_4W_TY, name=f"w_buffer_0_{r}_{c}", tile=mt)
    w1 = Buffer(type=_LINEAR_4W_TY, name=f"w_buffer_1_{r}_{c}", tile=mt)
    return w0, w1


def _build_proj_gather_mem(ctx, mt):
    """A projection memtile that also gathers y from its group's sending cores."""
    m = q4nx.M_TILE
    r, c = mt.row, mt.col
    m_col_ty = np.ndarray[(8 * m + 2,), _BF16]
    y0 = Buffer(type=m_col_ty, name=f"y_buffer_0_{r}_{c}", tile=mt)
    y1 = Buffer(type=m_col_ty, name=f"y_buffer_1_{r}_{c}", tile=mt)
    w0, w1 = _proj_weight_buffers(mt)
    yp0, yp1, yp2, yp3, yc = ctx.add_locks(mt, [(0, 2), (1, 0), (2, 0), (3, 0), (4, 0)])
    y = TensorAccessPattern.full(y0.shape)
    wc = _proj_weight_channels(w0, w1, *ctx.add_locks(mt, _PROJ_MEM_W_LOCKS))
    ctx.rt.add_tile_dma(
        TileDma(
            mt,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    ping_pong(y0, y1, yp0, yp1, tap=y[: 2 * m + 2]),
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    ping_pong(y0, y1, yp1, yp2, tap=y[2 * m + 2 : 4 * m + 2]),
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    2,
                    ping_pong(y0, y1, yp2, yp3, tap=y[4 * m + 2 : 6 * m + 2]),
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    3,
                    ping_pong(y0, y1, yp3, yc, tap=y[6 * m + 2 :]),
                ),
                wc["in0"],
                *wc["out"],
                DmaChannel(DMAChannelDir.MM2S, 4, ping_pong(y0, y1, yc, yp0)),
                wc["in1"],
            ],
        )
    )


def _build_proj_weight_mem(ctx, mt):
    """A projection memtile that carries weights only."""
    w0, w1 = _proj_weight_buffers(mt)
    wc = _proj_weight_channels(w0, w1, *ctx.add_locks(mt, _PROJ_MEM_W_LOCKS))
    ctx.rt.add_tile_dma(TileDma(mt, [wc["in0"], *wc["out"], wc["in1"]]))


def _build_proj_x_mem(ctx, mt):
    """The projection memtile that gathers both groups' y and broadcasts x."""
    m = q4nx.M_TILE
    r, c = mt.row, mt.col
    x_chunk_ty = np.ndarray[(X_SLICE * 2,), _BF16]
    m_full_ty = np.ndarray[(16 * m + 2,), _BF16]
    y0 = Buffer(type=m_full_ty, name=f"y_buffer_0_{r}_{c}", tile=mt)
    y1 = Buffer(type=m_full_ty, name=f"y_buffer_1_{r}_{c}", tile=mt)
    x0 = Buffer(type=x_chunk_ty, name=f"x_buffer_0_{r}_{c}", tile=mt)
    x1 = Buffer(type=x_chunk_ty, name=f"x_buffer_1_{r}_{c}", tile=mt)
    mp0, mp1, mc, xp, xc = ctx.add_locks(mt, [(0, 2), (1, 0), (2, 0), (3, 2), (4, 0)])
    y = TensorAccessPattern.full(y0.shape)
    w0, w1 = _proj_weight_buffers(mt)
    wc = _proj_weight_channels(w0, w1, *ctx.add_locks(mt, _PROJ_MEM_W_LOCKS))
    ctx.rt.add_tile_dma(
        TileDma(
            mt,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    0,
                    ping_pong(y0, y1, mp0, mp1, tap=y[: 8 * m + 2]),
                ),
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    ping_pong(y0, y1, mp1, mc, tap=y[8 * m + 2 :]),
                ),
                DmaChannel(DMAChannelDir.S2MM, 3, ping_pong(x0, x1, xp, xc)),
                wc["in0"],
                wc["in1"],
                DmaChannel(DMAChannelDir.MM2S, 5, ping_pong(y0, y1, mc, mp0)),
                DmaChannel(DMAChannelDir.MM2S, 4, ping_pong(x0, x1, xc, xp)),
                *wc["out"],
            ],
        )
    )


def _scores_ty(ctx, name):
    """The type of the scores that the qk core sends kv kernel ``name``.

    It is the first argument of the kernel's round, or of its s_begin for
    two KV heads.
    """
    kv = ctx.kernels[name]
    first = getattr(kv, f"{name}_round", None) or getattr(kv, f"{name}_s_begin")
    return first.arg_types()[0]


def _build_attn_kv(ctx, kv_tile, name, rtp_key, dh, of_s, two_kv_heads):
    """An attention kv core.

    The core takes the scores from of_s and v on S2MM 1. It sends o to the
    projection engine on MM2S 0.

    A round of the two-KV-head kernels covers one KV head. A round of the
    other kernels covers every KV head.
    """
    g = ctx.g
    D = g.model_dim
    r, c = kv_tile.row, kv_tile.col
    NQ = g.num_attn_heads
    o_repeats = D // (q4nx.M_TILE * 16)
    k_begin = ctx.entry(name, f"{name}_begin")
    k_finish = ctx.entry(name, f"{name}_finish")
    if two_kv_heads:
        k_sbeg = ctx.entry(name, f"{name}_s_begin")
        k_vhalf = ctx.entry(name, f"{name}_v_half")
        v_ty = k_vhalf.arg_types()[1]
    else:
        k_round = ctx.entry(name, f"{name}_round")
        v_ty = k_round.arg_types()[1]
    y_ty, o_ty, l_ty = k_finish.arg_types()
    L = ctx.rtp_buffer(kv_tile, rtp_key)
    v0 = Buffer(type=v_ty, name=f"v_0_{r}_{c}", tile=kv_tile)
    v1 = Buffer(type=v_ty, name=f"v_1_{r}_{c}", tile=kv_tile)
    y = Buffer(type=y_ty, name=f"y_{r}_{c}", tile=kv_tile)
    o = Buffer(type=o_ty, name=f"o_{r}_{c}", tile=kv_tile)
    kl = ctx.locks(
        kv_tile,
        ATTN_KV_LOCKS,
        dict(o_prod_lock=o_repeats, o_cons_lock=0, v_prod_lock=2, v_cons_lock=0),
    )
    lbuf = Buffer(type=l_ty, name=f"l_{r}_{c}", tile=kv_tile)
    if two_kv_heads:

        def kv_body(s_in, v_0, v_1, yy, ll, oo, rtp_l, kb, ksb, kvh, kf):
            kb(yy, ll)
            for _ in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_in.acquire(1)
                ksb(s, yy, ll)
                for j in range_(2):
                    kvh(s, v_0, v_1, yy, j)
                s_in.release(1)
            kf(yy, oo, ll)

        args = [of_s.cons(), v0, v1, y, lbuf, o, L]
        args += [k_begin, k_sbeg, k_vhalf, k_finish]
    else:

        def kv_body(s_in, v_0, v_1, yy, ll, oo, rtp_l, kb, kr, kf):
            kb(yy, ll)
            for _ in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_in.acquire(1)
                kr(s, v_0, v_1, yy, ll)
                s_in.release(1)
            kf(yy, oo, ll)

        args = [of_s.cons(), v0, v1, y, lbuf, o, L, k_begin, k_round, k_finish]

    ctx.workers.append(Worker(kv_body, args, tile=kv_tile, stack_size=1024 * 6))
    ctx.rt.add_tile_dma(
        TileDma(
            kv_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    ping_pong(v0, v1, kl["v_prod_lock"], kl["v_cons_lock"]),
                ),
                _single_bd(
                    DMAChannelDir.MM2S,
                    0,
                    o,
                    kl["o_cons_lock"],
                    kl["o_prod_lock"],
                    packet=(0, _X_FROM_ATTN),
                    tap=TensorAccessPattern.full((dh // 8, NQ, 8)).permute((1, 0, 2)),
                ),
            ],
        )
    )


def _build_attn_qk(ctx, qk_tile, name, rtp_key, dh, of_s, q_fifo, two_kv_heads):
    """An attention qk core.

    The core takes q from q_fifo and k on S2MM 1. It sends the scores to of_s.
    """
    r, c = qk_tile.row, qk_tile.col
    # Every qk kernel names its entry points attn_qk_*.
    k_begin = ctx.entry(name, "attn_qk_begin")
    if two_kv_heads:
        k_half = ctx.entry(name, "attn_qk_half")
        k_storec = ctx.entry(name, "attn_qk_store_c")
        k_step = k_half
    else:
        k_round = ctx.entry(name, "attn_qk_round")
        k_step = k_round
    q_ty, k_ty, _, _, m_ty, c_ty = k_step.arg_types()[:6]
    # The kernel pads each KV head's query group.
    (q_len,) = np_ndarray_type_get_shape(q_ty)
    NQ_PADDED = q_len // dh
    k0 = Buffer(type=k_ty, name=f"k_0_{r}_{c}", tile=qk_tile)
    k1 = Buffer(type=k_ty, name=f"k_1_{r}_{c}", tile=qk_tile)
    ql = ctx.locks(qk_tile, ATTN_QK_LOCKS, dict(k_prod_lock=2, k_cons_lock=0))
    ctx.add_locks(qk_tile, [(ATTN_HANDSHAKE_LOCK, 0)])
    L = ctx.rtp_buffer(qk_tile, rtp_key)
    q_in_order = TensorAccessPattern.full((dh // 8, NQ_PADDED, 8)).permute((1, 0, 2))
    m_buf = Buffer(type=m_ty, name=f"m_{r}_{c}", tile=qk_tile)
    c_local = Buffer(type=c_ty, name=f"c_local_{r}_{c}", tile=qk_tile)
    # The q acquire orders the RTP read after the sequence's RTP writes.
    if two_kv_heads:

        def qk_body(s_out, q_h, k_0, k_1, mm, cc, rtp_l, kb, kh, ks):
            q = q_h.acquire(1)
            kb(mm)
            for i in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_out.acquire(1)
                for j in range_(2):
                    kh(q, k_0, k_1, s, mm, cc, j, i, rtp_l[0])
                ks(s, cc)
                s_out.release(1)
            q_h.release(1)

        kerns = [k_begin, k_half, k_storec]
    else:

        def qk_body(s_out, q_h, k_0, k_1, mm, cc, rtp_l, kb, kr):
            q = q_h.acquire(1)
            kb(mm)
            for i in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_out.acquire(1)
                kr(q, k_0, k_1, s, mm, cc, i, rtp_l[0])
                s_out.release(1)
            q_h.release(1)

        kerns = [k_begin, k_round]

    args = [
        of_s.prod(),
        q_fifo.cons(from_stream=q_in_order),
        k0,
        k1,
        m_buf,
        c_local,
        L,
    ] + kerns
    ctx.workers.append(Worker(qk_body, args, tile=qk_tile, stack_size=1024 * 4))
    ctx.rt.add_tile_dma(
        TileDma(
            qk_tile,
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    1,
                    ping_pong(k0, k1, ql["k_prod_lock"], ql["k_cons_lock"]),
                ),
            ],
        )
    )


def _build_attn_mem(ctx, amt):
    """The attention memtile.

    It takes k, v, swa_k and swa_v in whole rows. It sends each to its core in
    the order the core's kernel reads.
    """
    g = ctx.g
    NUM_KV, two_kv = g.num_kv_heads, g.num_kv_heads == 2
    amt_name = f"{amt.row}_{amt.col}"
    k_row = NUM_KV * g.dh
    sk_row = NUM_KV * g.swa_dh
    k = TensorAccessPattern.full((LK, k_row))
    sk = TensorAccessPattern.full((LK, sk_row))
    # k column groups of 8 down every row; v in 8 x 8 blocks, but as k when
    # two heads share the row.
    k_order = k.tile((LK, 8))[0]
    v_order = k_order if two_kv else k.tile((8, 8))
    amt_chans = []
    for ch, (key, row, order, lock_ids) in enumerate(
        (
            ("k", k_row, k_order, (0, 1)),
            ("v", k_row, v_order, (3, 4)),
            ("swa_k", sk_row, sk.tile((LK, 8))[0], (5, 6)),
            ("swa_v", sk_row, sk.tile((8, 8)), (7, 8)),
        )
    ):
        b0, b1 = (
            Buffer(
                type=np.ndarray[(LK, row), _BF16],
                name=f"{key}_mem_buffer_{i}_{amt_name}",
                tile=amt,
            )
            for i in (0, 1)
        )
        prod, cons = ctx.add_locks(amt, [(lock_ids[0], 2), (lock_ids[1], 0)])
        amt_chans += [
            DmaChannel(DMAChannelDir.S2MM, ch, ping_pong(b0, b1, prod, cons)),
            DmaChannel(
                DMAChannelDir.MM2S,
                ch,
                ping_pong(
                    b0,
                    b1,
                    cons,
                    prod,
                    tap=order,
                ),
            ),
        ]
    ctx.rt.add_tile_dma(TileDma(amt, amt_chans))


def _route(rt, grid, t, proj_send_tiles):
    """Add every flow between the stages.

    ``grid`` holds every tile by (column, row), ``t`` the tile of each
    PLACEMENT stage. The router places flows in the order the design adds
    them. Long flows go first.

    Returns:
        The flows the runtime sequence fills and drains, by name.
    """
    x_shim, kv_shim = t["x_shim"], t["kv_shim"]
    proj_x = t["proj_x"]
    shim = {}
    for name, ch, dst, dst_ch, pkt in (
        ("send_x", 0, t["rms"], 0, _ShimPkt.to_rms),
        ("send_rms", 1, t["rms"], 1, _ShimPkt.to_rms),
        ("send_x_rope", 0, t["rope"], 1, _ShimPkt.to_rope),
        ("send_rms_rope", 1, t["swa_rope"], 1, _ShimPkt.to_rope),
    ):
        shim[name] = _connect(rt, x_shim, ch, dst, dst_ch, pkt_id=pkt, name=name)
    _connect(rt, t["rms"], 0, proj_x, 3, pkt_id=_X_FROM_RMS)

    # The weights from the shim into each memtile.
    for col in PROJ_COLS:
        for ch in (0, 1):
            name = f"proj_w{ch}_{col}"
            shim[name] = _connect(rt, grid[col, 0], ch, grid[col, 1], 4 + ch, name=name)
    # The weights from each memtile to its column's cores.
    for col in PROJ_COLS:
        for j in range(4):
            _connect(rt, grid[col, 1], j, grid[col, 2 + j], 1)
    # x to every projection core.
    for col in PROJ_COLS:
        for j in range(4):
            _connect(rt, proj_x, 4, grid[col, 2 + j], 0)
    # y from each group's sending cores to its memtile. The first keeps the
    # packet header, which carries the consumer's id to proj_x.
    pkts = [_ProjPkt.to_swa_rope, _ProjPkt.to_rope, _ProjPkt.to_rms, _ProjPkt.to_glu]
    gather_mts = [t["proj_gather_0"], t["proj_gather_1"]]
    for gather_mt, send_tiles in zip(gather_mts, proj_send_tiles):
        for j, send_t in enumerate(send_tiles):
            for pk in pkts:
                _connect(rt, send_t, 0, gather_mt, j, pkt_id=pk, keep_pkt_header=j == 0)
    for ch, gather_mt in enumerate(gather_mts):
        for pk in pkts:
            _connect(rt, gather_mt, 4, proj_x, ch, pkt_id=pk, keep_pkt_header=ch == 0)

    for dst, pk in (
        ("glu", _ProjPkt.to_glu),
        ("rms", _ProjPkt.to_rms),
        ("rope", _ProjPkt.to_rope),
        ("swa_rope", _ProjPkt.to_swa_rope),
    ):
        _connect(rt, proj_x, 5, t[dst], 0, pkt_id=pk)

    # This token's k and v, out to the KV cache.
    shim["recv_k"] = _connect(rt, t["rope"], 1, kv_shim, 0, name="recv_k")
    shim["recv_v"] = _connect(rt, t["swa_rope"], 1, kv_shim, 1, name="recv_v")
    _connect(rt, t["attn_kv"], 0, proj_x, 3, pkt_id=_X_FROM_ATTN)
    _connect(rt, t["swa_attn_kv"], 0, proj_x, 3, pkt_id=_X_FROM_ATTN)
    _connect(rt, t["glu"], 0, proj_x, 3, pkt_id=_X_FROM_GLU)

    # The KV cache into the attention memtile.
    amt = t["attn_mem"]
    for name, ch, amt_ch, pkt in (
        ("move_k", 0, 0, _KV_PKT_GLOBAL),
        ("move_k_swa", 0, 2, _KV_PKT_SWA),
        ("move_v", 1, 1, _KV_PKT_GLOBAL),
        ("move_v_swa", 1, 3, _KV_PKT_SWA),
    ):
        shim[name] = _connect(rt, kv_shim, ch, amt, amt_ch, pkt_id=pkt, name=name)
    _connect(rt, amt, 0, t["attn_qk"], 1)
    _connect(rt, amt, 1, t["attn_kv"], 1)
    _connect(rt, amt, 2, t["swa_attn_qk"], 1)
    _connect(rt, amt, 3, t["swa_attn_kv"], 1)

    # The per-layer-input path.
    pl_shim_0, pl_shim_1 = t["pl_shim_0"], t["pl_shim_1"]
    shim["pli_rope_rms"] = _connect(
        rt, pl_shim_0, 0, t["pl_embedding"], 0, name="pli_rope_rms"
    )
    shim["pli_down"] = _connect(rt, pl_shim_0, 1, t["pl_embedding"], 1, name="pli_down")
    _connect(rt, t["pl_embedding"], 1, t["pl_merge"], 0)
    shim["pli_gate"] = _connect(rt, pl_shim_1, 0, t["pl_gate"], 1, name="pli_gate")
    _connect(rt, t["pl_gate"], 1, t["pl_merge"], 1)
    _connect(rt, t["pl_merge"], 0, t["pl_up"], 0)
    shim["pli_up"] = _connect(rt, pl_shim_1, 1, t["pl_up"], 1, name="pli_up")
    # The layer output, out to x.
    shim["recv_y"] = _connect(rt, t["pl_up"], 0, x_shim, 0, name="recv_y")
    return shim


def decode_layer(
    dev,
    geometry,
    rtp,
    layer_type,
    sliding_window=SLIDING_WINDOW,
    *,
    kernels,
    context_len: DispatchTime[np.int32],
    max_l: DispatchTime[np.int32],
):
    """The MLIR module of one decode layer of ``layer_type`` for ``geometry``.

    ``rtp`` maps each RTP_ADDRESSES key to the address that the engine writes.
    ``layer_type`` sets the runtime sequence only. ``kernels`` holds
    layer_kernels(geometry). README.md gives the meaning of the dispatch
    parameters ``context_len`` and ``max_l``.
    """
    if layer_type not in LAYER_TYPES:
        raise ValueError(f"layer_type must be one of {LAYER_TYPES}")
    if sliding_window < LK or sliding_window & (sliding_window - 1):
        raise ValueError(
            f"sliding_window ({sliding_window}) must be a power of two of at "
            f"least {LK}: the sequence takes the remainder by it with a mask, "
            "and the attention memtile takes the cache in buffers of LK rows"
        )
    g = geometry
    G_DQ = g.num_attn_heads * g.dh
    S_DQ = g.num_attn_heads * g.swa_dh
    two_kv = g.num_kv_heads == 2

    sizes = arg_sizes(g)
    # _route fills the shim flows in before the sequence body runs.
    shim = {}
    rt = Runtime(
        partial(_sequence, g, rtp, layer_type, sliding_window, shim),
        [
            np.ndarray[(sizes["x"],), _BF16],
            np.ndarray[(sizes["proj"],), _BF16],
            np.ndarray[(sizes["rms"],), _BF16],
            np.ndarray[(sizes["rope_rms"],), _BF16],
            np.ndarray[(sizes["kv"],), _BF16],
            context_len,
            max_l,
        ],
    )
    workers = []

    grid = {
        (c, r): Tile(c, r, tile_type=dev.get_tile_type(c, r))
        for r in range(dev.rows)
        for c in range(dev.cols)
    }
    t = {stage: grid[at] for stage, at in PLACEMENT.items()}

    ctx = _Ctx(rt, workers, g, rtp, kernels)

    rms_y_out = _build_rms(ctx, t["rms"])
    # q from RoPE to the qk core. The qk core's DMA reorders it.
    q_of_g = ObjectFifo(np.ndarray[(G_DQ,), _BF16], name="q_in", depth=2)
    q_of_swa = ObjectFifo(np.ndarray[(S_DQ,), _BF16], name="swa_q_in", depth=2)
    _build_rope(ctx, t["rope"], "rope", "rope_skip_kv", g.dh, q_of_g)
    _build_rope(ctx, t["swa_rope"], "swa_rope", "swa_rope_skip_kv", g.swa_dh, q_of_swa)
    _build_pl_embedding(ctx, t["pl_embedding"])
    _build_pl_gate(ctx, t["pl_gate"], rms_y_out)
    _build_pl_merge(ctx, t["pl_merge"])
    _build_pl_up(ctx, t["pl_up"])
    _build_glu(ctx, t["glu"])

    proj_send_tiles = _build_proj_cores(ctx, grid)
    _build_proj_gather_mem(ctx, t["proj_gather_0"])
    _build_proj_gather_mem(ctx, t["proj_gather_1"])
    _build_proj_weight_mem(ctx, t["proj_weight"])
    _build_proj_x_mem(ctx, t["proj_x"])

    of_g_s = ObjectFifo(
        _scores_ty(ctx, "attn_kv"), name="attn_s", delegate_tile=t["attn_kv"]
    )
    _build_attn_kv(ctx, t["attn_kv"], "attn_kv", "l_kv", g.dh, of_g_s, two_kv)
    _build_attn_qk(ctx, t["attn_qk"], "attn_qk", "l_qk", g.dh, of_g_s, q_of_g, two_kv)
    of_swa_s = ObjectFifo(
        _scores_ty(ctx, "swa_attn_kv"),
        name="swa_attn_s",
        delegate_tile=t["swa_attn_kv"],
    )
    _build_attn_kv(
        ctx, t["swa_attn_kv"], "swa_attn_kv", "swa_l_kv", g.swa_dh, of_swa_s, False
    )
    _build_attn_qk(
        ctx,
        t["swa_attn_qk"],
        "swa_attn_qk",
        "swa_l_qk",
        g.swa_dh,
        of_swa_s,
        q_of_swa,
        False,
    )
    _build_attn_mem(ctx, t["attn_mem"])

    shim.update(_route(rt, grid, t, proj_send_tiles))
    return Program(dev, rt, workers=workers).resolve_program()
