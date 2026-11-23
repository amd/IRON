# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's fused decode layer on the whole array, one token through one layer.

Workers schedule RMS/residual, RoPE, projection, GLU, per-layer input and
attention. The runtime follows FastFlowLM's weight and KV-cache protocol.
"""

from dataclasses import dataclass, field
from enum import IntEnum, StrEnum
from functools import partial
from typing import NamedTuple

import numpy as np
from aie.dialects import arith
from aie.dialects._aie_enum_gen import AIETileType
from aie.dialects.aie import DMAChannelDir
from aie.dialects.aiex import _as_i32
from aie.helpers.npdtypes import np_ndarray_type_get_shape
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    DispatchTime,
    DmaChannel,
    Lock,
    ObjectFifo,
    ObjectFifoPool,
    Program,
    Runtime,
    TileDma,
    Worker,
    require,
)
from aie.iron.controlflow import if_, range_
from aie.iron.dataflow import (
    ObjectFifoHandle,
    Packet,
    PacketFlow,
    Port,
    Transport,
)
from aie.iron.device import Tile
from aie.iron.kernels import (
    BF16_PROJ_K,
    BF16_PROJ_M,
    DECODE_KEYS_PER_ROUND,
    FLM_GEMMA4_E2B_DECODE,
    FLM_GEMMA4_E4B_DECODE,
    FlmGemma4DecodeGeometry,
    flm_gemma4,
)
from ml_dtypes import bfloat16

from iron.operators.flm import q4nx
from iron.operators.flm.dataflow import ping_pong


class LayerType(StrEnum):
    """Global or sliding-window (swa) attention.

    And whether the layer reads an earlier layer's KV cache (skip) instead
    of writing its own.
    """

    GLOBAL = "global"
    SWA = "swa"
    GLOBAL_SKIP = "global_skip"
    SWA_SKIP = "swa_skip"

    @property
    def swa(self) -> bool:
        return self in (LayerType.SWA, LayerType.SWA_SKIP)

    @property
    def skip(self) -> bool:
        return self in (LayerType.GLOBAL_SKIP, LayerType.SWA_SKIP)


# The KV cache rows that the runtime sequence's buffer types allow. The
# sequence takes the row count, max_l, at dispatch.
MAX_CONTEXT = 32768
# A power of two of at least LK: the sequence takes the remainder by it with
# a mask, and the attention memtile takes the cache in buffers of LK rows.
SLIDING_WINDOW = 512

# The geometries the FLM decode kernels are built for.
GEOMETRIES = (FLM_GEMMA4_E2B_DECODE, FLM_GEMMA4_E4B_DECODE)

# One q4nx block in bf16 elements, the unit the weight buffers are typed in.
W_BLOCK = q4nx.BLOCK_BYTES // 2
# Keys per attention round.
LK = DECODE_KEYS_PER_ROUND
# The padding in the engine's per-layer-input stream (gemma4e_npu_sequence.hpp).
MIN_BF16_PAD = 32
# The memtiles of the projection engine's four groups. Group i's memtile
# feeds its cores proj_{i}_0 to proj_{i}_3 their weights, and proj_shim_{i}
# feeds the memtile.
PROJ_MEMS = ("proj_gather_0", "proj_x", "proj_gather_1", "proj_weight")

_CORE, _MEM, _SHIM = AIETileType.CoreTile, AIETileType.MemTile, AIETileType.ShimNOCTile
STAGES = {
    "attn_qk": _CORE,
    "attn_kv": _CORE,
    "swa_attn_qk": _CORE,
    "swa_attn_kv": _CORE,
    "rms": _CORE,
    "glu": _CORE,
    "rope": _CORE,
    "swa_rope": _CORE,
    "pl_gate": _CORE,
    "pl_embedding": _CORE,
    "pl_up": _CORE,
    "pl_merge": _CORE,
    **{f"proj_{i}_{j}": _CORE for i in range(len(PROJ_MEMS)) for j in range(4)},
    **dict.fromkeys(PROJ_MEMS, _MEM),
    "attn_mem": _MEM,
    **{f"proj_shim_{i}": _SHIM for i in range(len(PROJ_MEMS))},
    "kv_shim": _SHIM,
    "x_shim": _SHIM,
    "pl_shim_0": _SHIM,
    "pl_shim_1": _SHIM,
}

_BF16 = np.dtype[bfloat16]
_RTP_TY = np.ndarray[(16,), np.dtype[np.int32]]


class _ProjPkt(IntEnum):
    """Packet ids of the projection output, one per consumer."""

    to_rope = 1
    to_swa_rope = 2
    to_rms = 4
    to_glu = 8


# Packet ids of the KV cache streams into the attention memtile.
_KV_PKT_GLOBAL = 12
_KV_PKT_SWA = 13


KV_STREAMS = (
    ("k", 0, _KV_PKT_GLOBAL, 0),
    ("v", 1, _KV_PKT_GLOBAL, 1),
    ("swa_k", 0, _KV_PKT_SWA, 2),
    ("swa_v", 1, _KV_PKT_SWA, 3),
)


class BlobWeight(NamedTuple):
    """One weight matrix in the engine's weight blob.

    ``offset``/``size`` count bf16 elements, ``dout``/``din`` the matrix
    shape, ``packed`` q4nx versus bf16.
    """

    offset: int
    size: int
    dout: int
    din: int
    packed: bool


@dataclass(frozen=True)
class LayerDims:
    """One layer type's dimensions, in elements, and its weight blob.

    A skip layer with ``double_wide_mlp`` has twice the intermediate size.
    """

    geometry: FlmGemma4DecodeGeometry
    layer_type: LayerType

    @property
    def swa(self) -> bool:
        return self.layer_type.swa

    @property
    def skip(self) -> bool:
        return self.layer_type.skip

    @property
    def dh(self) -> int:
        return self.geometry.swa_dh if self.swa else self.geometry.dh

    @property
    def dq(self) -> int:
        return self.geometry.num_attn_heads * self.dh

    @property
    def dk(self) -> int:
        return self.geometry.num_kv_heads * self.dh

    @property
    def intermediate_size(self) -> int:
        wide = self.skip and self.geometry.double_wide_mlp
        return self.geometry.intermediate_size * (2 if wide else 1)

    @property
    def weights(self) -> dict[str, BlobWeight]:
        """Return the weights in the blob the sequence reads from proj, in blob order.

        qkv (q alone on a skip layer), o, up_gate and down in q4nx, then the
        per-layer-input down, gate and up projections in bf16.
        """
        D, P, dq, dk = self.geometry.model_dim, self.geometry.pli_d, self.dq, self.dk
        inter = self.intermediate_size
        shapes = {
            "qkv": (dq if self.skip else dq + 2 * dk, D, True),
            "o": (D, dq, True),
            "up_gate": (2 * inter, D, True),
            "down": (D, inter, True),
            "pli_down": (P, D, False),
            "pli_gate": (P, D, False),
            "pli_up": (D, P, False),
        }
        layout, offset = {}, 0
        for name, (dout, din, packed) in shapes.items():
            size = q4nx.packed_bytes(dout * din) // 2 if packed else dout * din
            layout[name] = BlobWeight(offset, size, dout, din, packed)
            offset += size
        return layout

    def kv_rows(self, max_l: int) -> int:
        """Rows of each half (K, then V) of the kv cache."""
        return SLIDING_WINDOW if self.swa else max_l

    def kv_row(self, context_len: int) -> int:
        """Return the cache row of the token at position context_len."""
        return context_len % SLIDING_WINDOW if self.swa else context_len


def arg_sizes(geometry):
    """Return upper bounds on the sequence's buffer element counts, by name.

    proj holds the largest of the four layer types' blobs, since they
    share one xclbin.
    """
    D, pli = geometry.model_dim, geometry.pli_d
    dk = geometry.num_kv_heads * geometry.dh
    proj = max(
        w.offset + w.size
        for t in LayerType
        for w in LayerDims(geometry, t).weights.values()
    )
    return {
        "x": 3 * D,
        "proj": proj,
        "rms": 4 * D,
        "rope_rms": 3 * geometry.dh + pli * 2 + D + 64,
        "kv": 2 * dk * MAX_CONTEXT,
    }


def _bf16_proj(
    y,
    w_h,
    x,
    y_acc,
    m_blocks,
    k_blocks,
    x_offset,
    y_offset,
    zero,
    mvm,
    store,
):
    """One bf16 projection: ``m_blocks`` output blocks over ``k_blocks`` weight blocks.

    ``w_h`` consumes the stage's weight ObjectFifo, one block per MVM, in the
    order the sequence fills it.
    """
    for i in range_(m_blocks):
        zero(y_acc)
        for j in range_(k_blocks):
            w = w_h.acquire(1)
            mvm(w, x, y_acc, j, x_offset)
            w_h.release(1)
        store(y, y_acc, i, y_offset)


def _kv_fifos(g, steps, amt, kv_shim):
    """One ObjectFifo per KV stream: shim, attention memtile, then core.

    Returns the producer handles in KV_STREAMS order, for the runtime, and
    each stream's core-side fifo by name. The memtile walks every object into
    the order its core's kernel reads. A two-KV-head core reads half an object
    at a time, so its forward re-chunks.
    """
    NUM_KV, two_kv = g.num_kv_heads, g.num_kv_heads == 2
    k_row, sk_row = NUM_KV * g.dh, NUM_KV * g.swa_dh
    k_order = [(k_row // 8, 8), (16, k_row), (8, 1)]
    if not two_kv:
        v_order = [(LK // 8, LK // 2 * k_row), (k_row // 8, 8), (8, k_row), (8, 1)]
    else:
        v_order = [(k_row // 8, 8), (LK, k_row), (8, 1)]
    sk_order = [(sk_row // 8, 8), (16, sk_row), (8, 1)]
    sv_order = [(LK // 8, LK // 2 * sk_row), (sk_row // 8, 8), (8, sk_row), (8, 1)]
    rows = dict(k=k_row, v=k_row, swa_k=sk_row, swa_v=sk_row)
    orders = dict(k=k_order, v=v_order, swa_k=sk_order, swa_v=sv_order)

    prods, cores = [], {}
    for (key, shim_ch, pkt, mem_ch), step in zip(KV_STREAMS, steps):
        row, order = rows[key], orders[key]
        of = ObjectFifo(
            np.ndarray[(LK, row), _BF16],
            name=f"{key}_in",
            depth=2,
            transport=Transport.dma(packet=Packet(id=pkt)),
        )
        cores[key] = of.cons().forward(
            tile=amt,
            obj_type=step.arg_types()[1],
            depth=2,
            name=f"{key}_to_core",
            to_stream=TensorAccessPattern(
                (LK, row),
                0,
                [size for size, _ in order],
                [stride for _, stride in order],
            ),
            port=Port.dma(mem_ch),
        )
        prods.append(of.prod(tile=kv_shim, port=Port.dma(shim_ch)))
    return prods, cores


def _ping_pong(direction, channel, b0, b1, acq, rel, **bd_args):
    """Return a DMA channel of two BDs that alternate between b0 and b1."""
    return DmaChannel(direction, channel, ping_pong(b0, b1, acq, rel, **bd_args))


def _connect(rt, src, src_ch, dst, dst_ch, pkt_id, keep_pkt_header=False, name=None):
    """Add a packet flow. A packet flow's channels are always given."""
    flow = PacketFlow(
        pkt_id,
        src,
        dst,
        src_channel=src_ch,
        dst_channel=dst_ch,
        keep_pkt_header=keep_pkt_header,
        name=name,
    )
    rt.add_flow(flow)
    return flow


@dataclass
class _Array:
    """The decode layer's array as its stages build it.

    Each stage adds its cores, locks and DMA channels to ``rt``/``workers``,
    keyed by stage in ``t``, ``rtps`` and ``sync_locks``. RMS,
    GLU and projection cores acquire their sync lock before reading RTPs
    (the sequence sets it after writing). RoPE and attention-qk wait for the
    projection cores; each attention-qk core then hands off to its kv core.
    """

    rt: Runtime = field(init=False)
    g: FlmGemma4DecodeGeometry
    workers: list[Worker] = field(default_factory=list, init=False)
    rtps: dict[tuple[str, str], Buffer] = field(default_factory=dict, init=False)
    sync_locks: dict[str, Lock] = field(default_factory=dict, init=False)
    t: dict[str, Tile] = field(init=False)

    def __post_init__(self) -> None:
        g = self.g
        self.k_rms_emit = flm_gemma4.flm_gemma4_decode_emit(geometry=g)
        self.k_attn_emit = flm_gemma4.flm_gemma4_decode_emit(geometry=g, attention=True)
        self.k_swa_attn_emit = flm_gemma4.flm_gemma4_decode_emit(
            geometry=g, attention=True, sliding_window=True
        )
        self.k_rms_residual = flm_gemma4.flm_gemma4_decode_rms_residual(geometry=g)
        self.k_rope = flm_gemma4.flm_gemma4_decode_rope(geometry=g)
        self.k_swa_rope = flm_gemma4.flm_gemma4_decode_rope(
            geometry=g, sliding_window=True
        )
        self.k_proj_layer_embedding = flm_gemma4.flm_gemma4_decode_proj_layer_embedding(
            geometry=g
        )
        self.k_proj_layer_embedding_mvm = (
            flm_gemma4.flm_gemma4_decode_proj_layer_embedding_mvm(geometry=g)
        )
        self.k_gate_layer_embedding_mvm = (
            flm_gemma4.flm_gemma4_decode_gate_layer_embedding_mvm(geometry=g)
        )
        self.k_per_layer_up_mvm = flm_gemma4.flm_gemma4_decode_per_layer_up_mvm(
            geometry=g
        )
        self.k_bf16_proj_zero = flm_gemma4.flm_gemma4_decode_bf16_proj_zero(geometry=g)
        self.k_proj_main = flm_gemma4.flm_gemma4_decode_proj_main(geometry=g)
        self.k_swa_attn_kv = flm_gemma4.flm_gemma4_decode_swa_attn_kv(geometry=g)
        self.k_swa_attn_qk = flm_gemma4.flm_gemma4_decode_attn_qk(
            geometry=g, sliding_window=True
        )
        if g.num_kv_heads == 2:
            kv = flm_gemma4.flm_gemma4_decode_attn_kv_kvh2(geometry=g)
            qk = flm_gemma4.flm_gemma4_decode_attn_qk_kvh2(geometry=g)
            self.kv_step = getattr(kv, "attn_kv_v_half")
            self.qk_step = getattr(qk, "attn_qk_half")
            self.kv_s_begin = getattr(kv, "attn_kv_s_begin")
            self.qk_store_c = getattr(qk, "attn_qk_store_c")
        else:
            kv = flm_gemma4.flm_gemma4_decode_attn_kv(geometry=g)
            qk = flm_gemma4.flm_gemma4_decode_attn_qk(geometry=g)
            self.kv_step = getattr(kv, "attn_kv_round")
            self.qk_step = getattr(qk, "attn_qk_round")
            self.kv_s_begin, self.qk_store_c = None, None
        self.k_attn_kv, self.k_attn_qk = kv, qk
        self.t = {stage: Tile(tile_type=at) for stage, at in STAGES.items()}
        # Keep the attention pairs off the top row; the greedy placer needs
        # room for both their shared scores and the query input connection.
        for stage in ("attn_qk", "swa_attn_qk"):
            self.t[stage].row = 2
        for stage in ("attn_kv", "swa_attn_kv"):
            self.t[stage].row = 3
        t = self.t
        pli_weights = (
            ("pli_down", self.k_proj_layer_embedding_mvm, "pl_shim_0", 1),
            ("pli_gate", self.k_gate_layer_embedding_mvm, "pl_shim_1", 0),
            ("pli_up", self.k_per_layer_up_mvm, "pl_shim_1", 1),
        )
        self.pli_w = {
            name: ObjectFifo(kern.arg_types()[0], name=f"{name}_w", depth=2)
            for name, kern, _, _ in pli_weights
        }
        self.y_of = ObjectFifo(
            np.ndarray[(g.model_dim,), _BF16], name="layer_y", depth=1
        )
        kv_prods, self.kv_cores = _kv_fifos(
            g,
            (
                self.qk_step,
                self.kv_step,
                getattr(self.k_swa_attn_qk, "attn_qk_round"),
                getattr(self.k_swa_attn_kv, "swa_attn_kv_round"),
            ),
            t["attn_mem"],
            t["kv_shim"],
        )
        self.shim_fifos = {
            name: self.pli_w[name].prod(tile=t[shim], port=Port.dma(ch))
            for name, _, shim, ch in pli_weights
        }
        self.shim_fifos["recv_y"] = self.y_of.cons(tile=t["x_shim"], port=Port.dma(0))
        self.shim_fifos.update(
            zip(("move_k", "move_v", "move_k_swa", "move_v_swa"), kv_prods)
        )
        self.host_fifos = {
            name: self.host_input(name, kernel.arg_types()[arg], shim, ch)
            for name, kernel, arg, shim, ch in (
                ("send_rms", self.k_rms_residual, 1, "x_shim", 1),
                ("send_x_rope", self.k_rope, 2, "x_shim", 1),
                ("send_rms_rope", self.k_swa_rope, 2, "x_shim", 1),
                ("pli_rope_rms", self.k_proj_layer_embedding, 0, "pl_shim_0", 0),
            )
        }
        self.proj_weights = {}
        for group, mem in enumerate(PROJ_MEMS):
            for half in (0, 1):
                name = f"proj_w{half}_{group}"
                incoming = ObjectFifo(
                    np.ndarray[(2 * W_BLOCK,), _BF16], name=name, depth=2
                )
                self.shim_fifos[name] = incoming.prod(
                    tile=t[f"proj_shim_{group}"], port=Port.dma(half)
                )
                first, second = incoming.cons().split(
                    [0, W_BLOCK],
                    tile=t[mem],
                    obj_types=[np.ndarray[(W_BLOCK,), _BF16]] * 2,
                    names=[f"w{2 * half}_{group}", f"w{2 * half + 1}_{group}"],
                )
                self.proj_weights[group, 2 * half] = first
                self.proj_weights[group, 2 * half + 1] = second
        self.rope_outputs = {}
        for channel, (name, stage) in enumerate(
            (("recv_k", self.k_rope), ("recv_v", self.k_swa_rope))
        ):
            fifo = ObjectFifo(
                getattr(stage, "rope_k").arg_types()[0],
                name=name,
                depth=2,
                transport=Transport.dma(),
            )
            self.rope_outputs[name] = fifo
            self.shim_fifos[name] = fifo.cons(tile=t["kv_shim"], port=Port.dma(channel))
        self.proj_x = ObjectFifo(
            np.ndarray[(512,), _BF16],
            name="proj_x",
            depth=2,
            consumer_obj_type=np.ndarray[(q4nx.K_TILE,), _BF16],
        )
        self.proj_inputs: dict[str, ObjectFifo] = dict(
            zip(
                ("rms", "attn_kv", "swa_attn_kv", "glu"),
                self.proj_x.prod().merge(
                    4,
                    tile=t["proj_x"],
                    names=[
                        "x_from_rms",
                        "x_from_attn",
                        "x_from_swa_attn",
                        "x_from_glu",
                    ],
                ),
            )
        )
        D, PLI = g.model_dim, g.pli_d
        self.plu_x_of = ObjectFifo(
            np.ndarray[(2 * (PLI + D) + 32,), _BF16], name="pl_x", depth=1
        )
        self.ple_y_of, self.gle_y_of = self.plu_x_of.prod().join(
            [0, D + PLI + 32],
            tile=t["pl_merge"],
            obj_types=[
                np.ndarray[(PLI + D + 32,), _BF16],
                np.ndarray[(D + PLI,), _BF16],
            ],
            names=["pl_embedding_y", "pl_gate_y"],
        )

    def label(self, tile: Tile) -> str:
        """``tile``'s stage."""
        return next(stage for stage, at in self.t.items() if at is tile)

    def build(self) -> dict[str, PacketFlow | ObjectFifoHandle]:
        """Build every stage, then every flow between them.

        Returns the flows the runtime sequence fills and drains, by name.
        """
        g, t = self.g, self.t
        G_DQ = g.num_attn_heads * g.dh
        S_DQ = g.num_attn_heads * g.swa_dh
        rms_y_out = self.rms(t["rms"])
        # q from RoPE to the qk core. The qk core's DMA reorders it.
        q_of_g = ObjectFifo(np.ndarray[(G_DQ,), _BF16], depth=2)
        q_of_swa = ObjectFifo(np.ndarray[(S_DQ,), _BF16], depth=2)
        self.rope(t["rope"], self.k_rope, "rope_skip_kv", "recv_k", q_of_g)
        self.rope(
            t["swa_rope"], self.k_swa_rope, "swa_rope_skip_kv", "recv_v", q_of_swa
        )
        self.pl_embedding(t["pl_embedding"], self.pli_w["pli_down"], self.ple_y_of)
        self.pl_gate(
            t["pl_gate"],
            rms_y_out,
            self.pli_w["pli_gate"],
            self.gle_y_of,
        )
        self.pl_up(t["pl_up"], self.plu_x_of, self.pli_w["pli_up"], self.y_of)
        self.glu(t["glu"])

        proj_send_tiles = self.proj_cores()
        self.proj_gather_mem(t["proj_gather_0"])
        self.proj_gather_mem(t["proj_gather_1"])
        self.proj_x_mem(t["proj_x"])

        for prefix, dh, q_fifo, kv_steps, qk_steps in (
            (
                "",
                g.dh,
                q_of_g,
                (
                    self.k_attn_kv,
                    self.kv_step,
                    getattr(self.k_attn_kv, "attn_kv_finish"),
                    self.kv_s_begin,
                    self.k_attn_emit,
                ),
                (self.k_attn_qk, self.qk_step, self.qk_store_c),
            ),
            (
                "swa_",
                g.swa_dh,
                q_of_swa,
                (
                    self.k_swa_attn_kv,
                    getattr(self.k_swa_attn_kv, "swa_attn_kv_round"),
                    getattr(self.k_swa_attn_kv, "swa_attn_kv_finish"),
                    None,
                    self.k_swa_attn_emit,
                ),
                (
                    self.k_swa_attn_qk,
                    getattr(self.k_swa_attn_qk, "attn_qk_round"),
                    None,
                ),
            ),
        ):
            kv_name, qk_name = f"{prefix}attn_kv", f"{prefix}attn_qk"
            (handshake,) = self.add_locks(t[kv_name], [0])
            scores = ObjectFifo(
                kv_steps[1].arg_types()[0],
                delegate_tile=t[kv_name],
                transport=Transport.shared_mem(),
            )
            self.attn_kv(
                kv_name,
                f"{prefix}l_kv",
                dh,
                scores,
                self.kv_cores[f"{prefix}v"],
                handshake,
                kv_steps,
            )
            self.attn_qk(
                qk_name,
                f"{prefix}l_qk",
                dh,
                scores,
                q_fifo,
                self.kv_cores[f"{prefix}k"],
                handshake,
                qk_steps,
            )
        # Place the attention pairs before the independent projection pairs;
        # their score storage and handshake must share the KV tile's memory.
        self.workers.sort(key=lambda w: "attn" not in self.label(w.tile))
        return self.route(proj_send_tiles)

    def rtp_buffer(self, tile: Tile, key: str) -> Buffer:
        """Return the RTP buffer ``key`` of ``tile``, which the sequence writes."""
        buf = Buffer(
            type=_RTP_TY,
            name=f"rtp_{key}_{self.label(tile)}",
            tile=tile,
            use_write_rtp=True,
        )
        self.rtps[key, self.label(tile)] = buf
        return buf

    def add_locks(self, tile, inits):
        locks = [Lock(tile=tile, init=init) for init in inits]
        for lock in locks:
            self.rt.add_lock(lock)
        return locks

    def manual_pool(self, tile, buffers, obj_type, drain=False):
        """Wrap manual DMA buffers; drain=True makes the core the producer."""
        if isinstance(buffers, Buffer):
            buffers = [buffers]
        stem = buffers[0].name
        prod = Lock(tile=tile, init=len(buffers), name=f"{stem}_prod")
        cons = Lock(tile=tile, init=0, name=f"{stem}_cons")
        for lock in (prod, cons):
            self.rt.add_lock(lock)
        return ObjectFifoPool(
            obj_type,
            tile=tile,
            depth=len(buffers),
            name=f"{stem}_pool",
            buffers=list(buffers),
            produce_lock=prod,
            consume_lock=cons,
            manual_fill=not drain,
            manual_drain=drain,
        )

    def host_input(self, name, obj_type, shim, channel):
        """Return a host-fed FIFO, sharing the shim channel through packets."""
        fifo = ObjectFifo(
            obj_type,
            name=name,
            depth=1,
            transport=Transport.dma(packet=Packet()),
        )
        self.shim_fifos[name] = fifo.prod(tile=self.t[shim], port=Port.dma(channel))
        return fifo

    def rms(self, tile):
        """Three norm/residual phases, retaining weights and residual state.

        Input still merges host and projection packets through a manual DMA.
        The projection input's repetition count depends on the dispatch RTPs.
        """
        g, D = self.g, self.g.model_dim
        begin = self.k_rms_residual
        middle = getattr(self.k_rms_residual, "rms_middle")
        finish = getattr(self.k_rms_residual, "rms_finish")
        x_ty, _, state_ty, y_ty = begin.arg_types()
        xs = [Buffer(type=x_ty, tile=tile, name=f"rms_x_{i}") for i in range(2)]
        x_pool = self.manual_pool(tile, xs, x_ty)
        (segment,) = x_pool.segments
        w = self.host_fifos["send_rms"]
        state = Buffer(type=state_ty, tile=tile, name="rms_state")
        y = Buffer(type=y_ty, tile=tile, name="rms_y")
        out = ObjectFifo(
            x_ty, depth=1, name="rms_to_gate", transport=Transport.shared_mem()
        )
        swa = self.rtp_buffer(tile, "rms_swa")
        skip = self.rtp_buffer(tile, "rms_skip")
        (sync,) = self.add_locks(tile, [0])
        self.sync_locks["rms"] = sync
        rows = q4nx.M_TILE * 16

        def body(
            x_h, w_h, out_h, proj_h, state, y, swa, skip, begin, middle, finish, emit
        ):
            sync.acquire(1)
            is_swa = swa[0] != 0
            is_skip = skip[0] != 0
            dh = arith.select(is_swa, _as_i32(g.swa_dh), _as_i32(g.dh))
            heads = arith.select(
                is_skip,
                _as_i32(g.num_attn_heads),
                _as_i32(g.num_attn_heads + 2 * g.num_kv_heads),
            )
            q_repeats = arith.divsi(arith.muli(dh, heads), _as_i32(rows))
            up_repeats = _as_i32(2 * g.intermediate_size // rows)
            if g.double_wide_mlp:
                up_repeats = arith.select(
                    is_skip, arith.muli(up_repeats, _as_i32(2)), up_repeats
                )

            w = w_h.acquire(1)
            for norm, repeats in ((begin, q_repeats), (middle, up_repeats)):
                norm(x_h.acquire(1), w, state, y)
                x_h.release(1)
                for _ in range_(repeats):
                    for chunk in range_(D // 512):
                        emit(y, proj_h.acquire(1), chunk)
                        proj_h.release(1)
            x = x_h.acquire(1)
            finish(x, w, state, out_h.acquire(1))
            x_h.release(1)
            out_h.release(1)
            w_h.release(1)

        self.workers.append(
            Worker(
                body,
                [
                    x_pool.cons(),
                    w.cons(port=Port.dma(1)),
                    out.prod(),
                    self.proj_inputs["rms"].prod(port=Port.dma(0)),
                    state,
                    y,
                    swa,
                    skip,
                    begin,
                    middle,
                    finish,
                    self.k_rms_emit,
                ],
                tile=tile,
                stack_size=4096,
            )
        )
        self.rt.add_tile_dma(
            TileDma(
                tile,
                [
                    _ping_pong(
                        DMAChannelDir.S2MM,
                        0,
                        xs[0],
                        xs[1],
                        segment.produce_lock,
                        segment.consume_lock,
                    ),
                ],
            )
        )
        return out

    def rope(self, rope_tile, kernel, rtp_key, kv_out, q_fifo):
        """RoPE, global or sliding-window.

        qkv arrives on S2MM 0, the RoPE weights on S2MM 1. q leaves through
        q_fifo to the qk core, k and v on MM2S 1.
        """
        rope_q, rope_k, rope_v = kernel, kernel.rope_k, kernel.rope_v
        _, qkv_ty, _, _ = rope_q.arg_types()
        n_q, n_kv = self.g.num_attn_heads, self.g.num_kv_heads

        n = self.label(rope_tile)
        qkv_0 = Buffer(type=qkv_ty, name=f"qkv_buffer_0_{n}", tile=rope_tile)
        qkv_1 = Buffer(type=qkv_ty, name=f"qkv_buffer_1_{n}", tile=rope_tile)
        rope_name = "send_x_rope" if n == "rope" else "send_rms_rope"
        rope_buf = self.host_fifos[rope_name]
        skip_kv = self.rtp_buffer(rope_tile, rtp_key)
        qkv_pool = self.manual_pool(rope_tile, [qkv_0, qkv_1], qkv_ty)
        (qkv_seg,) = qkv_pool.segments

        def rope_body(q_h, kv_h, qkv_h, rope_h, skip, rq, rk, rv):
            q = q_h.acquire(1)
            rope = rope_h.acquire(1)
            for i in range_(n_q):
                rq(q, qkv_h.acquire(1), rope, i)
                qkv_h.release(1)
            # The layer reuses another layer's KV cache when skip_kv is set, so k
            # and v stay behind.
            with if_(skip[0] == 0):
                kk = kv_h.acquire(1)
                for i in range_(n_kv):
                    rk(kk, qkv_h.acquire(1), rope, i)
                    qkv_h.release(1)
                kv_h.release(1)
                v = kv_h.acquire(1)
                for i in range_(n_kv):
                    rv(v, qkv_h.acquire(1), i)
                    qkv_h.release(1)
                kv_h.release(1)
            rope_h.release(1)
            q_h.release(1)

        self.workers.append(
            Worker(
                rope_body,
                [
                    q_fifo.prod(),
                    self.rope_outputs[kv_out].prod(port=Port.dma(1)),
                    qkv_pool.cons(),
                    rope_buf.cons(port=Port.dma(1)),
                    skip_kv,
                    rope_q,
                    rope_k,
                    rope_v,
                ],
                tile=rope_tile,
                stack_size=1024 * 4,
            )
        )
        self.rt.add_tile_dma(
            TileDma(
                rope_tile,
                [
                    _ping_pong(
                        DMAChannelDir.S2MM,
                        0,
                        qkv_0,
                        qkv_1,
                        qkv_seg.produce_lock,
                        qkv_seg.consume_lock,
                    ),
                ],
            )
        )

    def pl_embedding(self, tile, w_fifo, y_fifo):
        """Project and normalize one packed per-layer-input object."""
        g = self.g
        finish = self.k_proj_layer_embedding
        zero = self.k_bf16_proj_zero
        mvm = self.k_proj_layer_embedding_mvm
        store = flm_gemma4.flm_gemma4_decode_proj_layer_embedding_store(geometry=self.g)
        _, proj_ty, _ = finish.arg_types()
        acc_ty = mvm.arg_types()[2]
        inputs = self.host_fifos["pli_rope_rms"]
        projected = Buffer(type=proj_ty, tile=tile, name="pli_projected")
        acc = Buffer(type=acc_ty, tile=tile, name="pli_acc")

        def body(in_h, w_h, out_h, projected, acc, zero, mvm, store, finish):
            x = in_h.acquire(1)
            _bf16_proj(
                projected,
                w_h,
                x,
                acc,
                g.pli_d // BF16_PROJ_M,
                g.model_dim // BF16_PROJ_K,
                2 * g.pli_d + g.model_dim + MIN_BF16_PAD,
                0,
                zero,
                mvm,
                store,
            )
            finish(x, projected, out_h.acquire(1))
            out_h.release(1)
            in_h.release(1)

        self.workers.append(
            Worker(
                body,
                [
                    inputs.cons(port=Port.dma(0)),
                    w_fifo.cons(port=Port.dma(1)),
                    y_fifo.prod(port=Port.dma(1)),
                    projected,
                    acc,
                    zero,
                    mvm,
                    store,
                    finish,
                ],
                tile=tile,
                stack_size=4096,
            )
        )

    def pl_gate(self, gle_tile, x, w_fifo, y_fifo):
        """Project and activate the RMS output into the per-layer-input gate."""
        D, PLI_D = self.g.model_dim, self.g.pli_d
        gle_name = self.label(gle_tile)
        gle_begin = flm_gemma4.flm_gemma4_decode_gate_layer_embedding(geometry=self.g)
        gle_finish = getattr(gle_begin, "gate_layer_embedding_finish")
        gle_zero = self.k_bf16_proj_zero
        gle_mvm = self.k_gate_layer_embedding_mvm
        gle_store = flm_gemma4.flm_gemma4_decode_gate_layer_embedding_store(
            geometry=self.g
        )
        _, _, gle_y_acc_ty, _, _ = gle_mvm.arg_types()
        gle_y_acc = Buffer(type=gle_y_acc_ty, name=f"y_acc_{gle_name}", tile=gle_tile)

        def gle_body(
            x_h,
            w_h,
            y_h,
            y_acc,
            begin,
            finish,
            zero,
            mvm,
            store,
        ):
            xx = x_h.acquire(1)
            y = y_h.acquire(1)
            begin(xx, y)
            _bf16_proj(
                y,
                w_h,
                y,
                y_acc,
                PLI_D // BF16_PROJ_M,
                D // BF16_PROJ_K,
                0,
                D,
                zero,
                mvm,
                store,
            )
            finish(y)
            y_h.release(1)
            x_h.release(1)

        self.workers.append(
            Worker(
                gle_body,
                [
                    x.cons(),
                    w_fifo.cons(port=Port.dma(1)),
                    y_fifo.prod(port=Port.dma(1)),
                    gle_y_acc,
                    gle_begin,
                    gle_finish,
                    gle_zero,
                    gle_mvm,
                    gle_store,
                ],
                tile=gle_tile,
                stack_size=1024 * 4,
            )
        )

    def pl_up(self, plu_tile, x_fifo, w_fifo, y_fifo):
        """Apply the per-layer-input up projection and final residual."""
        D, PLI_D = self.g.model_dim, self.g.pli_d
        plu_name = self.label(plu_tile)
        plu_begin = flm_gemma4.flm_gemma4_decode_per_layer_up(geometry=self.g)
        plu_finish = getattr(plu_begin, "per_layer_up_finish")
        plu_zero = self.k_bf16_proj_zero
        plu_mvm = self.k_per_layer_up_mvm
        plu_store = flm_gemma4.flm_gemma4_decode_per_layer_up_store(geometry=self.g)
        _, _, plu_y_acc_ty, _, _ = plu_mvm.arg_types()
        plu_y_acc = Buffer(type=plu_y_acc_ty, name=f"y_acc_{plu_name}", tile=plu_tile)

        def plu_body(
            x_h,
            w_h,
            y_h,
            y_acc,
            begin,
            finish,
            zero,
            mvm,
            store,
        ):
            x = x_h.acquire(1)
            y = y_h.acquire(1)
            begin(x)
            _bf16_proj(
                y,
                w_h,
                x,
                y_acc,
                D // BF16_PROJ_M,
                PLI_D // BF16_PROJ_K,
                D + 32,
                0,
                zero,
                mvm,
                store,
            )
            finish(x, y)
            y_h.release(1)
            x_h.release(1)

        self.workers.append(
            Worker(
                plu_body,
                [
                    x_fifo.cons(port=Port.dma(0)),
                    w_fifo.cons(port=Port.dma(1)),
                    y_fifo.prod(port=Port.dma(0)),
                    plu_y_acc,
                    plu_begin,
                    plu_finish,
                    plu_zero,
                    plu_mvm,
                    plu_store,
                ],
                tile=plu_tile,
                stack_size=1024 * 4,
            )
        )

    def glu(self, glu_tile):
        """Apply GLU and repeat its output for the down projection."""
        (sync,) = self.add_locks(glu_tile, [0])
        self.sync_locks[self.label(glu_tile)] = sync
        glu_name = self.label(glu_tile)
        chunk_k = flm_gemma4.flm_gemma4_decode_glu(geometry=self.g)
        emit_k = getattr(chunk_k, "glu_emit")
        glu_hid_ty, glu_up_gate_ty, _ = chunk_k.arg_types()
        glu_x_0 = Buffer(type=glu_up_gate_ty, name=f"x_0_{glu_name}", tile=glu_tile)
        glu_x_1 = Buffer(type=glu_up_gate_ty, name=f"x_1_{glu_name}", tile=glu_tile)
        glu_hid = Buffer(type=glu_hid_ty, name=f"hid_0_{glu_name}", tile=glu_tile)
        glu_is_skip = self.rtp_buffer(glu_tile, "glu_skip")
        x_pool = self.manual_pool(glu_tile, [glu_x_0, glu_x_1], glu_up_gate_ty)
        (x_seg,) = x_pool.segments
        # The gate and up halves arrive one glu_slice at a time; the down
        # projection then reads the activations back once per repeat.
        chunks = 2 * self.g.intermediate_size // self.g.glu_slice
        repeats = self.g.model_dim // (4 * len(PROJ_MEMS) * q4nx.M_TILE)

        def glu_body(hid, x_h, y_h, skip, chunk, emit):
            sync.acquire(1)
            n = arith.select(skip[0] != 0, _as_i32(2 * chunks), _as_i32(chunks))
            for i in range_(n):
                chunk(hid, x_h.acquire(1), i)
                x_h.release(1)
            for _ in range_(repeats):
                for j in range_(n):
                    emit(y_h.acquire(1), hid, j)
                    y_h.release(1)

        self.workers.append(
            Worker(
                glu_body,
                [
                    glu_hid,
                    x_pool.cons(),
                    self.proj_inputs["glu"].prod(port=Port.dma(0)),
                    glu_is_skip,
                    chunk_k,
                    emit_k,
                ],
                tile=glu_tile,
                stack_size=4 * 1024,
            )
        )
        self.rt.add_tile_dma(
            TileDma(
                glu_tile,
                [
                    _ping_pong(
                        DMAChannelDir.S2MM,
                        0,
                        glu_x_0,
                        glu_x_1,
                        x_seg.produce_lock,
                        x_seg.consume_lock,
                    ),
                ],
            )
        )

    def proj_core(self, group, j, peer, *, send):
        """Stream projection blocks and pair their output rows at the sender."""
        g, tile = self.g, self.t[f"proj_{group}_{j}"]
        n = self.label(tile)
        accumulate = self.k_proj_main
        zero = getattr(self.k_proj_main, "proj_zero")
        store = getattr(self.k_proj_main, "proj_pack" if send else "proj_store")
        w_ty, x_ty, acc_ty, sums_ty = accumulate.arg_types()[:4]
        acc = Buffer(type=acc_ty, tile=tile, name=f"acc_{n}")
        sums = Buffer(type=sums_ty, tile=tile, name=f"sums_{n}")
        swa = self.rtp_buffer(tile, "proj_swa")
        skip = self.rtp_buffer(tile, "proj_skip")
        (sync,) = self.add_locks(tile, [0])
        self.sync_locks[n] = sync
        channels = []
        if send:
            y_ty = store.arg_types()[0]
            ys = [Buffer(type=y_ty, tile=tile, name=f"y_{i}_{n}") for i in range(2)]
            y_pool = self.manual_pool(tile, ys, y_ty, drain=True)
            (seg,) = y_pool.segments
            channels.append(
                _ping_pong(
                    DMAChannelDir.MM2S,
                    0,
                    ys[0],
                    ys[1],
                    seg.consume_lock,
                    seg.produce_lock,
                    tap=TensorAccessPattern.full(ys[0].shape)[14:],
                )
            )
            output, other = y_pool.prod(), peer.cons()
        else:
            output, other = peer.prod(), None

        def body(x_h, w_h, y_h, peer_h, acc, sums, swa, skip, zero, mac, store):
            sync.acquire(1)
            is_swa, is_skip = swa[0] != 0, skip[0] != 0
            dh = arith.select(is_swa, _as_i32(g.swa_dh), _as_i32(g.dh))
            qkv_heads = arith.select(
                is_skip,
                _as_i32(g.num_attn_heads),
                _as_i32(g.num_attn_heads + 2 * g.num_kv_heads),
            )
            inter = _as_i32(g.intermediate_size)
            if g.double_wide_mlp:
                inter = arith.select(is_skip, arith.muli(inter, _as_i32(2)), inter)
            rope_packet = arith.select(
                is_swa, _as_i32(_ProjPkt.to_swa_rope), _as_i32(_ProjPkt.to_rope)
            )
            for M, K, packet in (
                (arith.muli(dh, qkv_heads), g.model_dim, rope_packet),
                (
                    g.model_dim,
                    arith.muli(dh, _as_i32(g.num_attn_heads)),
                    _ProjPkt.to_rms,
                ),
                (arith.muli(_as_i32(2), inter), g.model_dim, _ProjPkt.to_glu),
                (g.model_dim, inter, _ProjPkt.to_rms),
            ):
                for i in range_(arith.divsi(_as_i32(M), _as_i32(16 * q4nx.M_TILE))):
                    zero(acc)
                    for k in range_(arith.divsi(_as_i32(K), _as_i32(q4nx.K_TILE))):
                        w, x = w_h.acquire(1), x_h.acquire(1)
                        mac(w, x, acc, sums, i, k)
                        w_h.release(1)
                        x_h.release(1)
                    y = y_h.acquire(1)
                    if send:
                        store(y, acc, peer_h.acquire(1), _as_i32(packet))
                        peer_h.release(1)
                    else:
                        store(y, acc)
                    y_h.release(1)

        self.workers.append(
            Worker(
                body,
                [
                    self.proj_x.cons(),
                    self.proj_weights[group, j].cons(),
                    output,
                    other,
                    acc,
                    sums,
                    swa,
                    skip,
                    zero,
                    accumulate,
                    store,
                ],
                tile=tile,
                stack_size=10 * 1024,
            )
        )
        self.rt.add_tile_dma(TileDma(tile, channels))

    def proj_cores(self):
        """Sixteen projection cores, paired through shared-memory FIFOs."""
        send_tiles = []
        row_ty = getattr(self.k_proj_main, "proj_store").arg_types()[0]
        for grp in range(2):
            group_send = []
            for csub in (0, 1):
                group = 2 * grp + csub
                for j in (0, 2):
                    sender = self.t[f"proj_{group}_{j}"]
                    peer = ObjectFifo(
                        row_ty,
                        name=f"proj_peer_{group}_{j}",
                        depth=2,
                        transport=Transport.shared_mem(),
                    )
                    self.proj_core(group, j, peer, send=True)
                    self.proj_core(group, j + 1, peer, send=False)
                    group_send.append(sender)
            send_tiles.append(group_send)
        return send_tiles

    def proj_gather_mem(self, mt: Tile) -> None:
        """Build a memtile that also gathers y from its group's sending cores."""
        m = q4nx.M_TILE
        n = self.label(mt)
        m_col_ty = np.ndarray[(8 * m + 2,), _BF16]
        y0 = Buffer(type=m_col_ty, name=f"y_buffer_0_{n}", tile=mt)
        y1 = Buffer(type=m_col_ty, name=f"y_buffer_1_{n}", tile=mt)
        # A lock per sending core, each releasing the next; the last, yc, the send.
        y_locks = self.add_locks(mt, [2, 0, 0, 0, 0])
        yc = y_locks[-1]
        y = TensorAccessPattern.full(y0.shape)
        # The first slot carries the packet header's 2 words.
        ends = [0] + [2 * m * (j + 1) + 2 for j in range(4)]
        self.rt.add_tile_dma(
            TileDma(
                mt,
                [
                    *(
                        _ping_pong(
                            DMAChannelDir.S2MM,
                            j,
                            y0,
                            y1,
                            y_locks[j],
                            y_locks[j + 1],
                            tap=y[ends[j] : ends[j + 1]],
                        )
                        for j in range(4)
                    ),
                    _ping_pong(DMAChannelDir.MM2S, 4, y0, y1, yc, y_locks[0]),
                ],
            )
        )

    def proj_x_mem(self, mt: Tile) -> None:
        """Build the projection memtile that gathers both groups' y and broadcasts x."""
        m = q4nx.M_TILE
        n = self.label(mt)
        m_full_ty = np.ndarray[(16 * m + 2,), _BF16]
        y0 = Buffer(type=m_full_ty, name=f"y_buffer_0_{n}", tile=mt)
        y1 = Buffer(type=m_full_ty, name=f"y_buffer_1_{n}", tile=mt)
        mp0, mp1, mc = self.add_locks(mt, [2, 0, 0])
        y = TensorAccessPattern.full(y0.shape)
        self.rt.add_tile_dma(
            TileDma(
                mt,
                [
                    _ping_pong(
                        DMAChannelDir.S2MM, 0, y0, y1, mp0, mp1, tap=y[: 8 * m + 2]
                    ),
                    _ping_pong(
                        DMAChannelDir.S2MM, 1, y0, y1, mp1, mc, tap=y[8 * m + 2 :]
                    ),
                    _ping_pong(DMAChannelDir.MM2S, 5, y0, y1, mc, mp0),
                ],
            )
        )

    def attn_kv(self, name, rtp_key, dh, of_s, v_fifo, handshake, steps):
        """Accumulate attention values and emit the normalized projection input.

        Wait for the QK handshake before reading RTPs.
        """
        k_begin, k_step, k_finish, k_sbeg, emitter = steps
        tile = self.t[name]
        g = self.g
        o_repeats = g.model_dim // (q4nx.M_TILE * 16)
        y_ty, l_ty = k_finish.arg_types()
        L = self.rtp_buffer(tile, rtp_key)
        y = Buffer(type=y_ty, name=f"y_{name}", tile=tile)
        lbuf = Buffer(type=l_ty, name=f"l_{name}", tile=tile)

        def kv_body(
            hs, s_in, v_h, yy, ll, rtp_l, begin, step, finish, s_begin, out_h, emit
        ):
            begin(yy, ll)
            hs.acquire(1)
            for _ in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_in.acquire(1)
                if s_begin is not None:
                    s_begin(s, yy, ll)
                    for j in range_(2):
                        v = v_h.acquire(1)
                        step(s, v, yy, j)
                        v_h.release(1)
                else:
                    v = v_h.acquire(1)
                    step(s, v, yy, ll)
                    v_h.release(1)
                s_in.release(1)
            finish(yy, ll)
            for _ in range_(o_repeats):
                for chunk in range_(g.num_attn_heads * dh // 512):
                    emit(yy, out_h.acquire(1), chunk)
                    out_h.release(1)

        self.workers.append(
            Worker(
                kv_body,
                [
                    handshake,
                    of_s.cons(),
                    v_fifo.cons(port=Port.dma(1)),
                    y,
                    lbuf,
                    L,
                    k_begin,
                    k_step,
                    k_finish,
                    k_sbeg,
                    self.proj_inputs[name].prod(port=Port.dma(0)),
                    emitter,
                ],
                tile=tile,
                stack_size=1024 * 6,
            )
        )

    def attn_qk(self, name, rtp_key, dh, of_s, q_fifo, k_fifo, handshake, steps):
        """Compute attention scores and signal KV after acquiring the query."""
        k_begin, k_step, k_storec = steps
        tile = self.t[name]
        q_ty, _, _, m_ty, c_ty = k_step.arg_types()[:5]
        # The kernel pads each KV head's query group.
        (q_len,) = np_ndarray_type_get_shape(q_ty)
        NQ_PADDED = q_len // dh
        L = self.rtp_buffer(tile, rtp_key)
        q_in_order = TensorAccessPattern(
            (NQ_PADDED, dh), 0, [NQ_PADDED, dh // 8, 8], [8, NQ_PADDED * 8, 1]
        )
        m_buf = Buffer(type=m_ty, name=f"m_{name}", tile=tile)
        c_local = Buffer(type=c_ty, name=f"c_local_{name}", tile=tile)

        def qk_body(hs, s_out, q_h, k_h, mm, cc, rtp_l, begin, step, store_c):
            # The q acquire orders the RTP read after the sequence's RTP writes.
            q = q_h.acquire(1)
            begin(mm)
            hs.release(1)
            for i in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_out.acquire(1)
                if store_c is not None:
                    for j in range_(2):
                        k = k_h.acquire(1)
                        step(q, k, s, mm, cc, j, i, rtp_l[0])
                        k_h.release(1)
                    store_c(s, cc)
                else:
                    k = k_h.acquire(1)
                    step(q, k, s, mm, cc, i, rtp_l[0])
                    k_h.release(1)
                s_out.release(1)
            q_h.release(1)

        self.workers.append(
            Worker(
                qk_body,
                [
                    handshake,
                    of_s.prod(),
                    q_fifo.cons(from_stream=q_in_order),
                    k_fifo.cons(port=Port.dma(1)),
                    m_buf,
                    c_local,
                    L,
                    k_begin,
                    k_step,
                    k_storec,
                ],
                tile=tile,
                stack_size=1024 * 4,
            )
        )

    def route(
        self, proj_send_tiles: list[list[Tile]]
    ) -> dict[str, PacketFlow | ObjectFifoHandle]:
        """Add every flow between the stages, long ones first.

        The router places them in the order the design adds them; returns
        the flows the runtime sequence fills and drains, by name.
        """
        rt, t = self.rt, self.t
        x_shim = t["x_shim"]

        proj_x = t["proj_x"]
        shim = {"send_x": _connect(rt, x_shim, 0, t["rms"], 0, pkt_id=0, name="send_x")}
        # y from each group's sending cores to its memtile. The first keeps the
        # packet header, which carries the consumer's id to proj_x.
        pkts = [
            _ProjPkt.to_swa_rope,
            _ProjPkt.to_rope,
            _ProjPkt.to_rms,
            _ProjPkt.to_glu,
        ]
        gather_mts = [t["proj_gather_0"], t["proj_gather_1"]]
        for gather_mt, send_tiles in zip(gather_mts, proj_send_tiles):
            for j, send_t in enumerate(send_tiles):
                for pk in pkts:
                    _connect(
                        rt, send_t, 0, gather_mt, j, pkt_id=pk, keep_pkt_header=j == 0
                    )
        for ch, gather_mt in enumerate(gather_mts):
            for pk in pkts:
                _connect(
                    rt, gather_mt, 4, proj_x, ch, pkt_id=pk, keep_pkt_header=ch == 0
                )

        for dst, pk in (
            ("glu", _ProjPkt.to_glu),
            ("rms", _ProjPkt.to_rms),
            ("rope", _ProjPkt.to_rope),
            ("swa_rope", _ProjPkt.to_swa_rope),
        ):
            _connect(rt, proj_x, 5, t[dst], 0, pkt_id=pk)

        return shim | self.shim_fifos


def _ceil_mul(v, chunk):
    """Round `v` up to a multiple of `chunk`."""
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
    rtps,
    sync_locks,
    layer_type,
    shim,
    x_arg,
    proj_arg,
    rms_arg,
    rope_rms_arg,
    kv_arg,
    len_arg,
    max_l_arg,
    _fifo_handles,
):
    """Build the runtime sequence of one ``layer_type`` dispatch.

    Writes the RTPs, then starts the shim DMA legs in ``gen_layer_seq``'s
    order. Offsets and lengths count bf16 elements; L counts tokens up to
    and including this one.
    """
    dims = LayerDims(g, LayerType(layer_type))
    D = g.model_dim
    L = _as_i32(len_arg) + 1
    MAX_L_v = _as_i32(max_l_arg)
    SW = SLIDING_WINDOW
    weights = dims.weights

    require(
        _as_i32(len_arg) >= 0,
        "context_len must be >= 0",
    )
    require(
        MAX_L_v <= MAX_CONTEXT,
        f"max_l exceeds {MAX_CONTEXT}",
    )
    if not dims.swa:
        require(L <= MAX_L_v, "context_len must be below max_l")

    for i in range(len(PROJ_MEMS)):
        for j in range(4):
            rtps["proj_swa", f"proj_{i}_{j}"][0] = int(dims.swa)
            rtps["proj_skip", f"proj_{i}_{j}"][0] = int(dims.skip)
            sync_locks[f"proj_{i}_{j}"].set(1)

    def write(stage, key, value):
        rtps[key, stage][0] = value

    L_local = _min_const(L, SW) if dims.swa else L
    write("attn_qk", "l_qk", L_local)
    write("attn_kv", "l_kv", L_local)
    write("swa_attn_qk", "swa_l_qk", L_local)
    write("swa_attn_kv", "swa_l_kv", L_local)
    write("rms", "rms_swa", int(dims.swa))
    write("rms", "rms_skip", int(dims.skip))
    write("rope", "rope_skip_kv", int(dims.skip))
    write("swa_rope", "swa_rope_skip_kv", int(dims.skip))
    write("glu", "glu_skip", int(dims.skip and g.double_wide_mlp))
    # The active qk core releases its kv core's handshake after it receives q.
    for stage in ("rms", "glu"):
        sync_locks[stage].set(1)

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
        """Return a (task, token) pair: ``mem[off : off + length]`` into ``shim[flow]``."""
        task = shim[flow].fill(
            mem, tap=mem[off : off + length], wait=token, managed=False
        )
        return task, token

    emit(leg("send_x", x_arg, 0, D))
    emit(leg("send_rms", rms_arg, 0, 4 * D))
    # The RoPE weights go out on the channel whose flow reaches this layer
    # type's RoPE tile.
    emit(
        leg(
            "send_rms_rope" if dims.swa else "send_x_rope", rope_rms_arg, 0, 3 * dims.dh
        )
    )
    recv_y = shim["recv_y"].drain(x_arg, tap=x_arg[:D], wait=True, managed=False)

    def move_weights(w):
        """Emit the engine's _move_weights legs: a round is 2 legs to each proj group."""
        bpr = w.din // q4nx.K_TILE
        # One core's M_TILE output rows, in bf16 elements.
        stripe = bpr * W_BLOCK
        cores = len(PROJ_MEMS) * 4
        for rnd in range(w.dout // q4nx.M_TILE // cores):
            legs = []
            for i in range(len(PROJ_MEMS)):
                for half in (0, 1):
                    off = w.offset + (rnd * cores + i * 4 + 2 * half) * stripe
                    legs.append(leg(f"proj_w{half}_{i}", proj_arg, off, 2 * stripe))
            emit(*legs)

    def pli_leg(name):
        """One leg over the bf16 weight ``name``, on the shim flow ``name``."""
        return leg(name, proj_arg, weights[name].offset, weights[name].size)

    v_cache_off = dims.dk * SW if dims.swa else MAX_L_v * dims.dk
    move_weights(weights["qkv"])
    if not dims.skip:
        # recv_k carries the global layers' k and v, recv_v the sliding-window
        # layers'.
        L_off = (
            arith.andi(L - 1, _as_i32(SW - 1)) if dims.swa else (L - 1)
        ) * dims.dk  # pyright: ignore[reportOperatorIssue]
        recv = "recv_v" if dims.swa else "recv_k"
        for off in (L_off, L_off + v_cache_off):
            task = shim[recv].drain(
                kv_arg, tap=kv_arg[off : off + dims.dk], wait=True, managed=False
            )
            emit((task, True))
    emit(leg("pli_rope_rms", rope_rms_arg, 3 * dims.dh, g.pli_d * 2 + D + MIN_BF16_PAD))
    # Complete the same packed embedding object with its input row.
    emit(leg("pli_rope_rms", x_arg, 2 * D, D, token=False))
    emit(pli_leg("pli_down"))
    # The KV cache into the attention memtile.
    move_k, move_v = ("move_k_swa", "move_v_swa") if dims.swa else ("move_k", "move_v")
    if not dims.swa:
        d2m = _ceil_mul(L, LK) * dims.dk
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
        p1_off = start * dims.dk  # pyright: ignore[reportOperatorIssue]
        p1_len = (
            rows - start
        ) * dims.dk - arith.andi(  # pyright: ignore[reportOperatorIssue]
            _z, _as_i32(dims.dk)
        )
        p2_off = arith.andi(_z, p1_len)
        p2_len = arith.ori(
            start * dims.dk,  # pyright: ignore[reportOperatorIssue]
            arith.andi(_z, _as_i32(dims.dk)),
        )
        emit(leg(move_k, kv_arg, p1_off, p1_len))
        emit(leg(move_v, kv_arg, p1_off + v_cache_off, p1_len))
        emit(leg(move_k, kv_arg, p2_off, p2_len, token=False))
        emit(
            leg(
                move_v,
                kv_arg,
                p2_off + v_cache_off,  # pyright: ignore[reportOperatorIssue]
                p2_len,
                token=False,
            )
        )
    for name in ("o", "up_gate", "down"):
        move_weights(weights[name])
    emit(pli_leg("pli_gate"))
    emit(pli_leg("pli_up"))
    flush(force=True)
    recv_y.await_()
    recv_y.free()


def decode_layer(
    dev,
    geometry,
    layer_type,
    *,
    context_len: DispatchTime[np.int32],
    max_l: DispatchTime[np.int32],
):
    """Return the MLIR module of one decode layer of ``layer_type`` for ``geometry``.

    ``layer_type`` sets only the runtime sequence. README.md explains
    ``context_len`` and ``max_l``.
    """
    g = geometry
    sizes = arg_sizes(g)
    # The array fills these in before the sequence body runs.
    shim, rtps, sync_locks = {}, {}, {}
    array = _Array(g)
    rt = Runtime(
        partial(_sequence, g, rtps, sync_locks, layer_type, shim),
        [
            np.ndarray[(sizes["x"],), _BF16],
            np.ndarray[(sizes["proj"],), _BF16],
            np.ndarray[(sizes["rms"],), _BF16],
            np.ndarray[(sizes["rope_rms"],), _BF16],
            np.ndarray[(sizes["kv"],), _BF16],
            context_len,
            max_l,
            list(array.shim_fifos.values()),
        ],
    )
    array.rt = rt
    shim.update(array.build())
    rtps.update(array.rtps)
    sync_locks.update(array.sync_locks)
    return Program(dev, rt, workers=array.workers).resolve_program()
