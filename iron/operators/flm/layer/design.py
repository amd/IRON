# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's fused decode layer on the whole array, one token through one layer.

Reproduces FastFlowLM's xclbin and runtime sequence. One core runs each
stage (RMS norm and residual, RoPE, 16 q4nx projection cores, GLU, the
per-layer-input path, one attention pair per kind); the sequence writes the
layer type into RTPs, then streams the weights, KV cache and hidden state.
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
from aie.extras import types as T
from aie.extras.dialects.arith import constant
from aie.helpers.npdtypes import np_ndarray_type_get_shape
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Acquire,
    Bd,
    Buffer,
    DispatchTime,
    DmaChannel,
    ExternalFunction,
    Lock,
    ObjectFifo,
    ObjectFifoPool,
    Program,
    Release,
    Runtime,
    TileDma,
    Worker,
    require,
)
from aie.iron.controlflow import else_, if_, range_
from aie.iron.dataflow import (
    Flow,
    ObjectFifoHandle,
    Packet,
    PacketFlow,
    Port,
    Transport,
)
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
# The projections' input slice. Every projection's input dimension is a
# multiple of it.
X_SLICE = 256
# Keys per attention round.
LK = 16
# The padding in the engine's per-layer-input stream (gemma4e_npu_sequence.hpp).
MIN_BF16_PAD = 32
# The memtiles of the projection engine's four groups. Group i's memtile
# feeds its cores proj_{i}_0 to proj_{i}_3 their weights, and proj_shim_{i}
# feeds the memtile.
PROJ_MEMS = ("proj_gather_0", "proj_x", "proj_gather_1", "proj_weight")

_CORE, _MEM, _SHIM = AIETileType.CoreTile, AIETileType.MemTile, AIETileType.ShimNOCTile
# The tile type of each stage. The placer chooses every tile, and keeps two
# cores that share a buffer next to each other.
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


def _lock_ids(*names):
    """Lock ids for ``names``, numbered from 0 in the order the design declares them.

    A kernel takes a lock id as a compile-time constant, so the design has to
    pin every lock a kernel names. It pins them from 0 up, which is what the
    compiler would pick, and leaves the ids above them to the compiler.
    """
    return {name: i for i, name in enumerate(names)}


# Core locks, by the name of the factory argument that gives the kernel the id.
RMS_LOCKS = _lock_ids(
    "y_prod_lock",
    "y_cons_lock",
    "x_prod_lock",
    "x_cons_lock",
)
ROPE_LOCKS = {}
PLE_LOCKS = {}
GLE_LOCKS = {}
PLU_LOCKS = {}
GLU_LOCKS = {}
PROJ_LOCKS = _lock_ids(
    "x_prod_lock",
    "x_cons_lock",
    "w_prod_lock",
    "w_cons_lock",
    "y_prod_ping_lock",
    "y_prod_pong_lock",
    "y_cons_ping_lock",
    "y_cons_pong_lock",
)
ATTN_KV_LOCKS = {}
ATTN_QK_LOCKS = {}


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


KV_STREAMS = (
    ("k", 0, _KV_PKT_GLOBAL, 0, "attn_qk"),
    ("v", 1, _KV_PKT_GLOBAL, 1, "attn_kv"),
    ("swa_k", 0, _KV_PKT_SWA, 2, "swa_attn_qk"),
    ("swa_v", 1, _KV_PKT_SWA, 3, "swa_attn_kv"),
)


PLI_WEIGHTS = (
    ("pli_down", "proj_layer_embedding_mvm", "pl_shim_0", 1),
    ("pli_gate", "gate_layer_embedding_mvm", "pl_shim_1", 0),
    ("pli_up", "per_layer_up_mvm", "pl_shim_1", 1),
)


def layer_kernels(geometry):
    """Return the flm_gemma4_decode_* kernels linked by this design, by name.

    The factories build for the selected device. The global attention kernels
    depend on the geometry's KV head count.
    """
    two_kv = geometry.num_kv_heads == 2

    def build(factory, locks, **kwargs):
        return factory(geometry=geometry, **locks, **kwargs)

    return {
        "rms_residual": build(flm_gemma4.flm_gemma4_decode_rms_residual, RMS_LOCKS),
        "rope": build(flm_gemma4.flm_gemma4_decode_rope, ROPE_LOCKS),
        "swa_rope": build(
            flm_gemma4.flm_gemma4_decode_rope, ROPE_LOCKS, sliding_window=True
        ),
        "proj_layer_embedding": build(
            flm_gemma4.flm_gemma4_decode_proj_layer_embedding, PLE_LOCKS
        ),
        "proj_layer_embedding_mvm": build(
            flm_gemma4.flm_gemma4_decode_proj_layer_embedding_mvm, {}
        ),
        "proj_layer_embedding_store": build(
            flm_gemma4.flm_gemma4_decode_proj_layer_embedding_store, {}
        ),
        "gate_layer_embedding": build(
            flm_gemma4.flm_gemma4_decode_gate_layer_embedding, GLE_LOCKS
        ),
        "gate_layer_embedding_mvm": build(
            flm_gemma4.flm_gemma4_decode_gate_layer_embedding_mvm, {}
        ),
        "gate_layer_embedding_store": build(
            flm_gemma4.flm_gemma4_decode_gate_layer_embedding_store, {}
        ),
        "per_layer_up": build(flm_gemma4.flm_gemma4_decode_per_layer_up, PLU_LOCKS),
        "per_layer_up_mvm": build(flm_gemma4.flm_gemma4_decode_per_layer_up_mvm, {}),
        "per_layer_up_store": build(
            flm_gemma4.flm_gemma4_decode_per_layer_up_store, {}
        ),
        "bf16_proj_zero": build(flm_gemma4.flm_gemma4_decode_bf16_proj_zero, {}),
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
            ATTN_QK_LOCKS,
        ),
        "swa_attn_kv": build(flm_gemma4.flm_gemma4_decode_swa_attn_kv, ATTN_KV_LOCKS),
        "swa_attn_qk": build(
            flm_gemma4.flm_gemma4_decode_attn_qk, ATTN_QK_LOCKS, sliding_window=True
        ),
    }


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


def _fill_bd(pool, **bd_args):
    """One BD of a hand-written chain, filling ``pool``'s one segment.

    It takes the lock protocol that pool's core endpoint expects: acquire the
    object, write it, hand it over.
    """
    (segment,) = pool.segments
    (buffer,) = pool.buffers
    return Bd(
        buffer,
        acquires=[Acquire(segment.produce_lock)],
        releases=[Release(segment.consume_lock)],
        **bd_args,
    )


def _wrapped_call(acquire=(), release=()):
    """Build a core body that acquires, calls the kernel, then releases.

    ``acquire`` and ``release`` hold (lock, value) pairs. The kernel is the
    body's last argument and takes the others.
    """

    def body(*args):
        for lock, value in acquire:
            lock.acquire(value)
        args[-1](*args[:-1])
        for lock, value in release:
            lock.release(value)

    return body


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


def _kv_core_type(kernels, stage, two_kv):
    """Return the k or v object type that ``stage``'s kernel reads."""
    names = {
        "attn_qk": "attn_qk_half" if two_kv else "attn_qk_round",
        "attn_kv": "attn_kv_v_half" if two_kv else "attn_kv_round",
        "swa_attn_qk": "attn_qk_round",
        "swa_attn_kv": "swa_attn_kv_round",
    }
    return getattr(kernels[stage], names[stage]).arg_types()[1]


def _kv_fifos(g, kernels, amt, kv_shim):
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
    for key, shim_ch, pkt, mem_ch, stage in KV_STREAMS:
        row, order = rows[key], orders[key]
        of = ObjectFifo(
            np.ndarray[(LK, row), _BF16],
            name=f"{key}_in",
            depth=2,
            transport=Transport.dma(packet=Packet(id=pkt)),
        )
        cores[key] = of.cons().forward(
            tile=amt,
            obj_type=_kv_core_type(kernels, stage, two_kv),
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


def _single_bd(direction, channel, buf, acq, rel, **bd_args):
    """Return a DMA channel of one BD that repeats behind one lock pair."""
    return DmaChannel(
        direction,
        channel,
        [Bd(buf, acquires=[Acquire(acq)], releases=[Release(rel)], **bd_args)],
    )


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
    keyed by stage in ``t``, ``flows``, ``rtps`` and ``sync_locks``. RMS,
    GLU and projection cores acquire their sync lock before reading RTPs
    (the sequence sets it after writing). RoPE and attention-qk wait for the
    projection cores; each attention-qk core then hands off to its kv core.
    """

    rt: Runtime = field(init=False)
    g: FlmGemma4DecodeGeometry
    kernels: dict[str, ExternalFunction]
    workers: list[Worker] = field(default_factory=list, init=False)
    rtps: dict[tuple[str, str], Buffer] = field(default_factory=dict, init=False)
    sync_locks: dict[str, Lock] = field(default_factory=dict, init=False)
    t: dict[str, Tile] = field(init=False)
    flows: dict[str, Flow] = field(init=False)

    def __post_init__(self) -> None:
        self.t = {stage: Tile(tile_type=at) for stage, at in STAGES.items()}
        # The circuit-switched flows. The compiler assigns their channels, and
        # each stage's DMA reaches them by endpoint.
        t = self.t
        ends = {}
        for i, mem in enumerate(PROJ_MEMS):
            for h in (0, 1):
                ends[f"proj_w{h}_{i}"] = t[f"proj_shim_{i}"], t[mem]
            for j in range(4):
                ends[f"w{j}_{i}"] = t[mem], t[f"proj_{i}_{j}"]
        proj = [t[f"proj_{i}_{j}"] for i in range(len(PROJ_MEMS)) for j in range(4)]
        ends["proj_x"] = t["proj_x"], proj
        ends["recv_k"] = t["rope"], t["kv_shim"]
        ends["recv_v"] = t["swa_rope"], t["kv_shim"]
        ends["pli_rope_rms"] = t["pl_shim_0"], t["pl_embedding"]
        self.flows = {
            name: Flow(src, dst, name=name) for name, (src, dst) in ends.items()
        }

        self.pli_w = {
            name: ObjectFifo(
                self.kernels[kern].arg_types()[0], name=f"{name}_w", depth=2
            )
            for name, kern, _, _ in PLI_WEIGHTS
        }
        g = self.g
        self.y_of = ObjectFifo(
            np.ndarray[(g.model_dim,), _BF16], name="layer_y", depth=1
        )
        kv_prods, self.kv_cores = _kv_fifos(
            g, self.kernels, t["attn_mem"], t["kv_shim"]
        )
        self.shim_fifos = {
            name: self.pli_w[name].prod(tile=t[shim], port=Port.dma(ch))
            for name, _, shim, ch in PLI_WEIGHTS
        }
        self.shim_fifos["recv_y"] = self.y_of.cons(tile=t["x_shim"], port=Port.dma(0))
        self.shim_fifos.update(
            zip(("move_k", "move_v", "move_k_swa", "move_v_swa"), kv_prods)
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

    def end(self, flow: str, tile: Tile):
        """Return the end of the circuit ``flow`` on ``tile``, for its DMA channel."""
        return self.flows[flow].endpoint(tile)

    def build(self) -> dict[str, Flow | PacketFlow | ObjectFifoHandle]:
        """Build every stage, then every flow between them.

        Returns the flows the runtime sequence fills and drains, by name.
        """
        g, t = self.g, self.t
        G_DQ = g.num_attn_heads * g.dh
        S_DQ = g.num_attn_heads * g.swa_dh
        two_kv = g.num_kv_heads == 2

        rms_y_out, out_prod, out_cons = self.rms(t["rms"])
        # q from RoPE to the qk core. The qk core's DMA reorders it.
        q_of_g = ObjectFifo(np.ndarray[(G_DQ,), _BF16], depth=2)
        q_of_swa = ObjectFifo(np.ndarray[(S_DQ,), _BF16], depth=2)
        self.rope(t["rope"], "rope", "rope_skip_kv", "recv_k", q_of_g)
        self.rope(t["swa_rope"], "swa_rope", "swa_rope_skip_kv", "recv_v", q_of_swa)
        self.pl_embedding(t["pl_embedding"], self.pli_w["pli_down"], self.ple_y_of)
        self.pl_gate(
            t["pl_gate"],
            rms_y_out,
            out_prod,
            out_cons,
            self.pli_w["pli_gate"],
            self.gle_y_of,
        )
        self.pl_up(t["pl_up"], self.plu_x_of, self.pli_w["pli_up"], self.y_of)
        self.glu(t["glu"])

        proj_send_tiles = self.proj_cores()
        self.proj_gather_mem(t["proj_gather_0"])
        self.proj_gather_mem(t["proj_gather_1"])
        self.proj_weight_mem(t["proj_weight"])
        self.proj_x_mem(t["proj_x"])

        (g_handshake,) = self.add_locks(t["attn_qk"], [0])
        (swa_handshake,) = self.add_locks(t["swa_attn_qk"], [0])
        of_g_s = ObjectFifo(self.scores_ty("attn_kv"), delegate_tile=t["attn_kv"])
        self.attn_kv(
            t["attn_kv"],
            "attn_kv",
            "l_kv",
            g.dh,
            of_g_s,
            self.kv_cores["v"],
            two_kv,
            g_handshake,
        )
        self.attn_qk(
            t["attn_qk"],
            "attn_qk",
            "l_qk",
            g.dh,
            of_g_s,
            q_of_g,
            self.kv_cores["k"],
            two_kv,
            g_handshake,
        )
        of_swa_s = ObjectFifo(
            self.scores_ty("swa_attn_kv"),
            delegate_tile=t["swa_attn_kv"],
        )
        self.attn_kv(
            t["swa_attn_kv"],
            "swa_attn_kv",
            "swa_l_kv",
            g.swa_dh,
            of_swa_s,
            self.kv_cores["swa_v"],
            False,
            swa_handshake,
        )
        self.attn_qk(
            t["swa_attn_qk"],
            "swa_attn_qk",
            "swa_l_qk",
            g.swa_dh,
            of_swa_s,
            q_of_swa,
            self.kv_cores["swa_k"],
            False,
            swa_handshake,
        )
        return self.route(proj_send_tiles)

    def entry(self, name, symbol):
        """Return entry point ``symbol`` of kernel ``name``, typed by its factory."""
        kernel = self.kernels[name]
        return kernel if kernel.name == symbol else getattr(kernel, symbol)

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
        """Create the tile's locks, one per init value, at ids the compiler picks.

        Only a lock that no kernel names can take an id this way.
        """
        return self.pinned_locks(tile, [(None, init) for init in inits])

    def pinned_locks(self, tile, ids_inits):
        """Create the tile's locks, one per (lock id, init) pair."""
        out = [Lock(tile=tile, lock_id=i, init=init) for i, init in ids_inits]
        for lock in out:
            self.rt.add_lock(lock)
        return out

    def manual_pool(self, tile, buffers, obj_type, drain=False):
        """Create an ObjectFifoPool over ``buffers`` driven by a manual BD chain.

        The core reaches the objects through the pool's handle. ``drain``
        gives the core the filling end and the BD chain the draining one.
        """
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

    def dma_locks(self, tile: Tile, *inits: int) -> list[Lock]:
        """Locks only DMAs take, one per init, their ids the compiler's."""
        return self.add_locks(tile, inits)

    def locks(self, tile, table, inits):
        """Create the tile's locks named in ``table``, with ``inits`` by name."""
        ids_inits = [(table[name], init) for name, init in inits.items()]
        return dict(zip(inits, self.pinned_locks(tile, ids_inits)))

    def core(
        self,
        tile: Tile,
        body,
        args: list,
        channels: list[DmaChannel],
    ) -> None:
        """Run a core on ``body`` and ``args``, with its tile's DMA channels."""
        self.workers.append(Worker(body, args, tile=tile, stack_size=10 * 1024))
        self.rt.add_tile_dma(TileDma(tile, channels))

    def rms(self, rms_tile):
        """RMS norm and residual.

        Returns y_out, the layer output the gate tile reads, and the lock pair that
        hands it over.

        x arrives on S2MM 0, the norm weights on S2MM 1. y leaves on MM2S 0
        behind its packet header.
        """
        (sync,) = self.add_locks(rms_tile, [0])
        self.sync_locks[self.label(rms_tile)] = sync
        D = self.g.model_dim
        rms_k = self.entry("rms_residual", "rms_residual")
        rms_y_pkt_ty, rms_x_ty, _, _, rms_w_ty, rms_x_buf_ty, _, _ = rms_k.arg_types()
        rms_name = self.label(rms_tile)
        rms_x_ping = Buffer(type=rms_x_ty, name=f"x_ping_{rms_name}", tile=rms_tile)
        rms_x_pong = Buffer(type=rms_x_ty, name=f"x_pong_{rms_name}", tile=rms_tile)
        rms_x_buf = Buffer(type=rms_x_buf_ty, name=f"x_buf_{rms_name}", tile=rms_tile)
        rms_w = Buffer(type=rms_w_ty, name=f"w_buffer_{rms_name}", tile=rms_tile)
        rms_y_out = Buffer(type=rms_x_ty, name=f"y_out_{rms_name}", tile=rms_tile)
        rms_y = Buffer(type=rms_y_pkt_ty, name=f"y_{rms_name}", tile=rms_tile)
        rms_is_swa = self.rtp_buffer(rms_tile, "rms_swa")
        rms_skip = self.rtp_buffer(rms_tile, "rms_skip")
        rl = self.locks(
            rms_tile,
            RMS_LOCKS,
            dict(
                y_prod_lock=0,
                y_cons_lock=0,
                x_prod_lock=2,
                x_cons_lock=0,
            ),
        )
        w_prod, w_cons = self.add_locks(rms_tile, [1, 0])
        # No DMA takes these two. They hand y_out to the gate tile's kernel.
        out_prod, out_cons = self.add_locks(rms_tile, [1, 0])

        self.workers.append(
            Worker(
                _wrapped_call(
                    acquire=[(sync, 1), (w_cons, 1), (out_prod, 1)],
                    release=[(w_prod, 1), (out_cons, 1)],
                ),
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
        self.rt.add_tile_dma(
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
                            tap=TensorAccessPattern(rms_x_ping.shape, 0, [D], [1]),
                        ),
                    ),
                    _single_bd(
                        DMAChannelDir.S2MM,
                        1,
                        rms_w,
                        w_prod,
                        w_cons,
                        tap=TensorAccessPattern(rms_w.shape, 0, [4 * D], [1]),
                    ),
                    _single_bd(
                        DMAChannelDir.MM2S,
                        0,
                        rms_y,
                        rl["y_cons_lock"],
                        rl["y_prod_lock"],
                        tap=TensorAccessPattern(rms_y.shape, 14, [D + 2], [1]),
                    ),
                ],
            )
        )
        return rms_y_out, out_prod, out_cons

    def rope(self, rope_tile, name, rtp_key, kv_out, q_fifo):
        """RoPE, global or sliding-window.

        qkv arrives on S2MM 0, the RoPE weights on S2MM 1. q leaves through
        q_fifo to the qk core, k and v on MM2S 1.
        """
        rope_q = self.entry(name, "rope_q")
        rope_k = self.entry(name, "rope_k")
        rope_v = self.entry(name, "rope_v")
        _, qkv_ty, rope_ty, _ = rope_q.arg_types()
        kv_ty = rope_k.arg_types()[0]
        n_q, n_kv = self.g.num_attn_heads, self.g.num_kv_heads

        n = self.label(rope_tile)
        qkv_0 = Buffer(type=qkv_ty, name=f"qkv_buffer_0_{n}", tile=rope_tile)
        qkv_1 = Buffer(type=qkv_ty, name=f"qkv_buffer_1_{n}", tile=rope_tile)
        k_buf = Buffer(type=kv_ty, name=f"k_buffer_{n}", tile=rope_tile)
        v_buf = Buffer(type=kv_ty, name=f"v_buffer_{n}", tile=rope_tile)
        rope_buf = Buffer(type=rope_ty, name=f"rope_buffer_{n}", tile=rope_tile)
        skip_kv = self.rtp_buffer(rope_tile, rtp_key)
        qkv_pool = self.manual_pool(rope_tile, [qkv_0, qkv_1], qkv_ty)
        (qkv_seg,) = qkv_pool.segments
        k_prod, k_cons = self.add_locks(rope_tile, [1, 0])
        v_prod, v_cons = self.add_locks(rope_tile, [1, 0])
        rope_prod, rope_cons = self.add_locks(rope_tile, [1, 0])

        def rope_body(q_h, kk, v, qkv_h, rope, skip, rq, rk, rv):
            q = q_h.acquire(1)
            rope_cons.acquire(1)
            for i in range_(n_q):
                rq(q, qkv_h.acquire(1), rope, i)
                qkv_h.release(1)
            # The layer reuses another layer's KV cache when skip_kv is set, so k
            # and v stay behind.
            zero = constant(0, type=T.i32())
            with if_(arith.cmpi(arith.CmpIPredicate.eq, skip[0], zero)):
                k_prod.acquire(1)
                for i in range_(n_kv):
                    rk(kk, qkv_h.acquire(1), rope, i)
                    qkv_h.release(1)
                k_cons.release(1)
                v_prod.acquire(1)
                for i in range_(n_kv):
                    rv(v, qkv_h.acquire(1), i)
                    qkv_h.release(1)
                v_cons.release(1)
            rope_prod.release(1)
            q_h.release(1)

        self.workers.append(
            Worker(
                rope_body,
                [
                    q_fifo.prod(),
                    k_buf,
                    v_buf,
                    qkv_pool.cons(),
                    rope_buf,
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
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        0,
                        ping_pong(
                            qkv_0, qkv_1, qkv_seg.produce_lock, qkv_seg.consume_lock
                        ),
                    ),
                    DmaChannel(
                        DMAChannelDir.MM2S,
                        self.end(kv_out, rope_tile),
                        [
                            Bd(
                                k_buf,
                                acquires=[Acquire(k_cons)],
                                releases=[Release(k_prod)],
                                next=1,
                            ),
                            Bd(
                                v_buf,
                                acquires=[Acquire(v_cons)],
                                releases=[Release(v_prod)],
                                next=0,
                            ),
                        ],
                    ),
                    _single_bd(
                        DMAChannelDir.S2MM,
                        1,
                        rope_buf,
                        rope_prod,
                        rope_cons,
                    ),
                ],
            )
        )

    def pl_embedding(self, ple_tile, w_fifo, y_fifo):
        """Per-layer-input embedding.

        x0_per_layer, the norm weights and x0 arrive on S2MM 0 as one 3-BD cycle,
        the projection weights through w_fifo on S2MM 1. y leaves through y_fifo
        on MM2S 1, into the front of the up projection's input object.

        The three arrivals share the one channel, which cuts the stream by
        position: a BD per buffer, in the order the sequence sends them. Each
        buffer is a ObjectFifoPool the chain fills by hand, so the core takes them
        with the acquire and release of any other fifo.
        """
        D, PLI_D = self.g.model_dim, self.g.pli_d
        ple_name = self.label(ple_tile)
        ple_finish = self.entry("proj_layer_embedding", "proj_layer_embedding_finish")
        ple_zero = self.entry("bf16_proj_zero", "bf16_proj_zero")
        ple_mvm = self.entry("proj_layer_embedding_mvm", "proj_layer_embedding_mvm")
        ple_store = self.entry(
            "proj_layer_embedding_store", "proj_layer_embedding_store"
        )
        ple_norm_w_ty, ple_x0_pl_ty, ple_x_proj_ty, _ = ple_finish.arg_types()
        _, ple_x0_ty, ple_y_acc_ty, _, _ = ple_mvm.arg_types()
        ple_norm_w = Buffer(
            type=ple_norm_w_ty, name=f"norm_w_{ple_name}", tile=ple_tile
        )
        ple_x0_pl = Buffer(
            type=ple_x0_pl_ty, name=f"x0_per_layer_{ple_name}", tile=ple_tile
        )
        ple_x0 = Buffer(type=ple_x0_ty, name=f"x0_{ple_name}", tile=ple_tile)
        ple_x_proj = Buffer(
            type=ple_x_proj_ty, name=f"x_proj_{ple_name}", tile=ple_tile
        )
        ple_y_acc = Buffer(type=ple_y_acc_ty, name=f"y_acc_{ple_name}", tile=ple_tile)
        # The order the sequence sends them in, which is the order of the BDs.
        pools = [
            self.manual_pool(ple_tile, ple_x0_pl, ple_x0_pl_ty),
            self.manual_pool(ple_tile, ple_norm_w, ple_norm_w_ty),
            self.manual_pool(ple_tile, ple_x0, ple_x0_ty),
        ]

        def ple_body(
            pl_h,
            nw_h,
            x0_h,
            x_proj,
            y_h,
            w_h,
            y_acc,
            finish,
            zero,
            mvm,
            store,
        ):
            x0_per_layer = pl_h.acquire(1)
            norm_w = nw_h.acquire(1)
            x0 = x0_h.acquire(1)
            y = y_h.acquire(1)
            _bf16_proj(
                x_proj,
                w_h,
                x0,
                y_acc,
                PLI_D // 32,
                D // 256,
                0,
                0,
                zero,
                mvm,
                store,
            )
            finish(norm_w, x0_per_layer, x_proj, y)
            y_h.release(1)
            pl_h.release(1)
            nw_h.release(1)
            x0_h.release(1)

        self.workers.append(
            Worker(
                ple_body,
                [
                    *[pool.cons() for pool in pools],
                    ple_x_proj,
                    y_fifo.prod(port=Port.dma(1)),
                    w_fifo.cons(port=Port.dma(1)),
                    ple_y_acc,
                    ple_finish,
                    ple_zero,
                    ple_mvm,
                    ple_store,
                ],
                tile=ple_tile,
                stack_size=1024 * 4,
            )
        )
        self.rt.add_tile_dma(
            TileDma(
                ple_tile,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        self.end("pli_rope_rms", ple_tile),
                        [
                            _fill_bd(pool, next=(i + 1) % len(pools))
                            for i, pool in enumerate(pools)
                        ],
                    ),
                ],
            )
        )

    def pl_gate(self, gle_tile, x, x_prod, x_cons, w_fifo, y_fifo):
        """Per-layer-input gate.

        x is the RMS tile's y_out, behind the x_prod/x_cons pair of that tile. The
        weights arrive through w_fifo on S2MM 1. y leaves through y_fifo on MM2S
        1, into the back of the up projection's input object.
        """
        D, PLI_D = self.g.model_dim, self.g.pli_d
        gle_name = self.label(gle_tile)
        gle_begin = self.entry("gate_layer_embedding", "gate_layer_embedding_begin")
        gle_finish = self.entry("gate_layer_embedding", "gate_layer_embedding_finish")
        gle_zero = self.entry("bf16_proj_zero", "bf16_proj_zero")
        gle_mvm = self.entry("gate_layer_embedding_mvm", "gate_layer_embedding_mvm")
        gle_store = self.entry(
            "gate_layer_embedding_store", "gate_layer_embedding_store"
        )
        _, _, gle_y_acc_ty, _, _ = gle_mvm.arg_types()
        gle_y_acc = Buffer(type=gle_y_acc_ty, name=f"y_acc_{gle_name}", tile=gle_tile)

        def gle_body(
            xx,
            w_h,
            y_h,
            y_acc,
            begin,
            finish,
            zero,
            mvm,
            store,
        ):
            x_cons.acquire(1)
            y = y_h.acquire(1)
            begin(xx, y)
            _bf16_proj(
                y,
                w_h,
                y,
                y_acc,
                PLI_D // 32,
                D // 256,
                0,
                D,
                zero,
                mvm,
                store,
            )
            finish(y)
            y_h.release(1)
            x_prod.release(1)

        self.workers.append(
            Worker(
                gle_body,
                [
                    x,
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
        """Per-layer-input up projection.

        x arrives through x_fifo on S2MM 0, the weights through w_fifo on S2MM 1.
        The layer output leaves through y_fifo on MM2S 0, which the sequence
        drains.
        """
        D, PLI_D = self.g.model_dim, self.g.pli_d
        plu_name = self.label(plu_tile)
        plu_begin = self.entry("per_layer_up", "per_layer_up_begin")
        plu_finish = self.entry("per_layer_up", "per_layer_up_finish")
        plu_zero = self.entry("bf16_proj_zero", "bf16_proj_zero")
        plu_mvm = self.entry("per_layer_up_mvm", "per_layer_up_mvm")
        plu_store = self.entry("per_layer_up_store", "per_layer_up_store")
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
                D // 32,
                PLI_D // 256,
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
        """GLU.

        gate and up arrive on S2MM 0. The activations leave on MM2S 0 with a
        packet header to the projection engine.
        """
        (sync,) = self.add_locks(glu_tile, [0])
        self.sync_locks[self.label(glu_tile)] = sync
        glu_name = self.label(glu_tile)
        chunk_k = self.entry("glu", "glu_chunk")
        emit_k = self.entry("glu", "glu_emit")
        glu_hid_ty, glu_up_gate_ty, _ = chunk_k.arg_types()
        glu_y_ty = emit_k.arg_types()[0]
        glu_x_0 = Buffer(type=glu_up_gate_ty, name=f"x_0_{glu_name}", tile=glu_tile)
        glu_x_1 = Buffer(type=glu_up_gate_ty, name=f"x_1_{glu_name}", tile=glu_tile)
        glu_y_0 = Buffer(type=glu_y_ty, name=f"y_0_{glu_name}", tile=glu_tile)
        glu_y_1 = Buffer(type=glu_y_ty, name=f"y_1_{glu_name}", tile=glu_tile)
        glu_hid = Buffer(type=glu_hid_ty, name=f"hid_0_{glu_name}", tile=glu_tile)
        glu_is_skip = self.rtp_buffer(glu_tile, "glu_skip")
        x_pool = self.manual_pool(glu_tile, [glu_x_0, glu_x_1], glu_up_gate_ty)
        y_pool = self.manual_pool(glu_tile, [glu_y_0, glu_y_1], glu_y_ty, drain=True)
        (x_seg,) = x_pool.segments
        (y_seg,) = y_pool.segments
        # The gate and up halves arrive one glu_slice at a time; the down
        # projection then reads the activations back once per repeat.
        chunks = 2 * self.g.intermediate_size // self.g.glu_slice
        repeats = self.g.model_dim // (4 * len(PROJ_MEMS) * q4nx.M_TILE)

        def sweep(hid, x_h, y_h, chunk, emit, n):
            for i in range_(n):
                chunk(hid, x_h.acquire(1), i)
                x_h.release(1)
            for _ in range_(repeats):
                for j in range_(n):
                    emit(y_h.acquire(1), hid, j)
                    y_h.release(1)

        def glu_body(hid, x_h, y_h, skip, chunk, emit):
            sync.acquire(1)
            # A layer that reuses another's KV cache runs a double-wide MLP.
            zero = constant(0, type=T.i32())
            with if_(arith.cmpi(arith.CmpIPredicate.eq, skip[0], zero)) as skip_if:
                sweep(hid, x_h, y_h, chunk, emit, chunks)
            with else_(skip_if):
                sweep(hid, x_h, y_h, chunk, emit, 2 * chunks)

        self.workers.append(
            Worker(
                glu_body,
                [glu_hid, x_pool.cons(), y_pool.prod(), glu_is_skip, chunk_k, emit_k],
                tile=glu_tile,
                stack_size=4 * 1024,
            )
        )
        self.rt.add_tile_dma(
            TileDma(
                glu_tile,
                [
                    DmaChannel(
                        DMAChannelDir.S2MM,
                        0,
                        ping_pong(
                            glu_x_0, glu_x_1, x_seg.produce_lock, x_seg.consume_lock
                        ),
                    ),
                    DmaChannel(
                        DMAChannelDir.MM2S,
                        0,
                        ping_pong(
                            glu_y_0,
                            glu_y_1,
                            y_seg.consume_lock,
                            y_seg.produce_lock,
                            packet=(0, _X_FROM_GLU),
                        ),
                    ),
                ],
            )
        )

    def proj_core(
        self,
        group: int,
        j: int,
        kern,
        send_x_out: bool,
        main_y0: Buffer | None = None,
        main_y1: Buffer | None = None,
    ) -> tuple[Buffer, Buffer]:
        """Build core ``j`` of projection group ``group``, returning its y buffers.

        (y0, y1); a core that doesn't send y fills the second slot of
        ``main_y0``/``main_y1`` instead, the sending core's own buffers.
        """
        n = f"proj_{group}_{j}"
        pt = self.t[n]
        y_ty, w_ty, x_ty = kern.arg_types()[:3]
        is_swa = self.rtp_buffer(pt, "proj_swa")
        skip_kv = self.rtp_buffer(pt, "proj_skip")
        x0 = Buffer(type=x_ty, name=f"x_0_{n}", tile=pt)
        w0 = Buffer(type=w_ty, name=f"w_0_{n}", tile=pt)
        x1 = Buffer(type=x_ty, name=f"x_1_{n}", tile=pt)
        w1 = Buffer(type=w_ty, name=f"w_1_{n}", tile=pt)
        if send_x_out:
            y0 = Buffer(type=y_ty, name=f"y_0_{n}", tile=pt)
            y1 = Buffer(type=y_ty, name=f"y_1_{n}", tile=pt)
        else:
            if main_y0 is None or main_y1 is None:
                raise TypeError(
                    "proj_core: main_y0 and main_y1 are required when send_x_out "
                    "is False"
                )
            y0, y1 = main_y0, main_y1
        pk = self.locks(
            pt,
            PROJ_LOCKS,
            dict(
                x_prod_lock=2,
                x_cons_lock=0,
                w_prod_lock=2,
                w_cons_lock=0,
                y_prod_ping_lock=2,
                y_prod_pong_lock=2,
                y_cons_ping_lock=0,
                y_cons_pong_lock=0,
            ),
        )
        (sync,) = self.add_locks(pt, [0])
        self.sync_locks[n] = sync

        def proj_body(yy0, ww0, xx0, yy1, ww1, xx1, sw, sk, kern):
            sync.acquire(1)
            kern(yy0, ww0, xx0, yy1, ww1, xx1, sw, sk, constant(int(send_x_out)))

        chans = [
            _ping_pong(
                DMAChannelDir.S2MM,
                self.end("proj_x", pt),
                x0,
                x1,
                pk["x_prod_lock"],
                pk["x_cons_lock"],
            ),
            _ping_pong(
                DMAChannelDir.S2MM,
                self.end(f"w{j}_{group}", pt),
                w0,
                w1,
                pk["w_prod_lock"],
                pk["w_cons_lock"],
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
        self.core(
            pt,
            proj_body,
            [y0, w0, x0, y1, w1, x1, is_swa, skip_kv, kern],
            chans,
        )
        return y0, y1

    def proj_cores(self) -> list[list[Tile]]:
        """Build the q4nx projection engine: 16 cores, four per group.

        Cores 0 and 2 of each group send y. Returns each gather memtile's
        two groups' sending cores.
        """
        proj_k = self.entry("proj_main", "proj_main")

        proj_send_tiles = []
        for grp in range(2):
            group_send = []
            for csub in (0, 1):
                group = 2 * grp + csub
                for j in (0, 2):
                    y0, y1 = self.proj_core(group, j, proj_k, send_x_out=True)
                    self.proj_core(
                        group, j + 1, proj_k, send_x_out=False, main_y0=y0, main_y1=y1
                    )
                    group_send.append(self.t[f"proj_{group}_{j}"])
            proj_send_tiles.append(group_send)
        return proj_send_tiles

    def weight_channels(self, mt: Tile, w0: Buffer, w1: Buffer) -> dict:
        """Return the weight channels of the projection memtile ``mt``."""
        group = PROJ_MEMS.index(self.label(mt))
        return _proj_weight_channels(
            w0,
            w1,
            [self.end(f"proj_w{h}_{group}", mt) for h in (0, 1)],
            [self.end(f"w{j}_{group}", mt) for j in range(4)],
            *self.dma_locks(mt, *_PROJ_MEM_W_INITS),
        )

    def proj_gather_mem(self, mt: Tile) -> None:
        """Build a memtile that also gathers y from its group's sending cores."""
        m = q4nx.M_TILE
        n = self.label(mt)
        m_col_ty = np.ndarray[(8 * m + 2,), _BF16]
        y0 = Buffer(type=m_col_ty, name=f"y_buffer_0_{n}", tile=mt)
        y1 = Buffer(type=m_col_ty, name=f"y_buffer_1_{n}", tile=mt)
        w0, w1 = _proj_weight_buffers(mt, self.label(mt))
        # A lock per sending core, each releasing the next; the last, yc, the send.
        y_locks = self.dma_locks(mt, 2, 0, 0, 0, 0)
        yc = y_locks[-1]
        y = TensorAccessPattern.full(y0.shape)
        # The first slot carries the packet header's 2 words.
        ends = [0] + [2 * m * (j + 1) + 2 for j in range(4)]
        wc = self.weight_channels(mt, w0, w1)
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
                    wc["in0"],
                    *wc["out"],
                    _ping_pong(DMAChannelDir.MM2S, 4, y0, y1, yc, y_locks[0]),
                    wc["in1"],
                ],
            )
        )

    def proj_weight_mem(self, mt: Tile) -> None:
        """Build a projection memtile that carries weights only."""
        w0, w1 = _proj_weight_buffers(mt, self.label(mt))
        wc = self.weight_channels(mt, w0, w1)
        self.rt.add_tile_dma(TileDma(mt, [wc["in0"], *wc["out"], wc["in1"]]))

    def proj_x_mem(self, mt: Tile) -> None:
        """Build the projection memtile that gathers both groups' y and broadcasts x."""
        m = q4nx.M_TILE
        n = self.label(mt)
        x_chunk_ty = np.ndarray[(X_SLICE * 2,), _BF16]
        m_full_ty = np.ndarray[(16 * m + 2,), _BF16]
        y0 = Buffer(type=m_full_ty, name=f"y_buffer_0_{n}", tile=mt)
        y1 = Buffer(type=m_full_ty, name=f"y_buffer_1_{n}", tile=mt)
        x0 = Buffer(type=x_chunk_ty, name=f"x_buffer_0_{n}", tile=mt)
        x1 = Buffer(type=x_chunk_ty, name=f"x_buffer_1_{n}", tile=mt)
        mp0, mp1, mc, xp, xc = self.dma_locks(mt, 2, 0, 0, 2, 0)
        y = TensorAccessPattern.full(y0.shape)
        w0, w1 = _proj_weight_buffers(mt, self.label(mt))
        wc = self.weight_channels(mt, w0, w1)
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
                    _ping_pong(DMAChannelDir.S2MM, 3, x0, x1, xp, xc),
                    wc["in0"],
                    wc["in1"],
                    _ping_pong(DMAChannelDir.MM2S, 5, y0, y1, mc, mp0),
                    _ping_pong(
                        DMAChannelDir.MM2S, self.end("proj_x", mt), x0, x1, xc, xp
                    ),
                    *wc["out"],
                ],
            )
        )

    def scores_ty(self, name: str) -> type[np.ndarray]:
        """Return the type of the scores the qk core sends kv kernel ``name``.

        The first argument of its ``round``, or ``s_begin`` for two KV heads.
        """
        kv = self.kernels[name]
        entries = vars(kv)
        first = entries.get(f"{name}_round") or entries[f"{name}_s_begin"]
        return first.arg_types()[0]

    def attn_kv(
        self, kv_tile, name, rtp_key, dh, of_s, v_fifo, two_kv_heads, handshake
    ):
        """Build an attention kv core.

        The core takes the scores from of_s and v from v_fifo on S2MM 1. It sends o to the
        projection engine on MM2S 0. It reads its RTPs only once it holds
        ``handshake``, a lock of the qk core on the tile below.

        A round of the two-KV-head kernels covers one KV head. A round of the
        other kernels covers every KV head.
        """
        g = self.g
        D = g.model_dim
        n = self.label(kv_tile)
        NQ = g.num_attn_heads
        o_repeats = D // (q4nx.M_TILE * 16)
        k_begin = self.entry(name, f"{name}_begin")
        k_finish = self.entry(name, f"{name}_finish")
        if two_kv_heads:
            k_sbeg = self.entry(name, f"{name}_s_begin")
            k_vhalf = self.entry(name, f"{name}_v_half")
        else:
            k_round = self.entry(name, f"{name}_round")
        y_ty, o_ty, l_ty = k_finish.arg_types()
        L = self.rtp_buffer(kv_tile, rtp_key)
        y = Buffer(type=y_ty, name=f"y_{n}", tile=kv_tile)
        o = Buffer(type=o_ty, name=f"o_{n}", tile=kv_tile)
        # The down projection reads o o_repeats times a dispatch.
        o_prod, o_cons = self.add_locks(kv_tile, [o_repeats, 0])
        lbuf = Buffer(type=l_ty, name=f"l_{n}", tile=kv_tile)
        if two_kv_heads:

            def kv_two_heads(hs, s_in, v_h, yy, ll, oo, rtp_l, kb, ksb, kvh, kf):
                kb(yy, ll)
                hs.acquire(1)
                for _ in range_((rtp_l[0] + (LK - 1)) // LK):
                    s = s_in.acquire(1)
                    ksb(s, yy, ll)
                    for j in range_(2):
                        v = v_h.acquire(1)
                        kvh(s, v, yy, j)
                        v_h.release(1)
                    s_in.release(1)
                o_prod.acquire(o_repeats)
                kf(yy, oo, ll)
                o_cons.release(o_repeats)

            kv_body = kv_two_heads
            args = [
                handshake,
                of_s.cons(),
                v_fifo.cons(port=Port.dma(1)),
                y,
                lbuf,
                o,
                L,
            ]
            args += [k_begin, k_sbeg, k_vhalf, k_finish]
        else:

            def kv_rounds(hs, s_in, v_h, yy, ll, oo, rtp_l, kb, kr, kf):
                kb(yy, ll)
                hs.acquire(1)
                for _ in range_((rtp_l[0] + (LK - 1)) // LK):
                    s = s_in.acquire(1)
                    v = v_h.acquire(1)
                    kr(s, v, yy, ll)
                    v_h.release(1)
                    s_in.release(1)
                o_prod.acquire(o_repeats)
                kf(yy, oo, ll)
                o_cons.release(o_repeats)

            kv_body = kv_rounds
            args = [
                handshake,
                of_s.cons(),
                v_fifo.cons(port=Port.dma(1)),
                y,
                lbuf,
                o,
                L,
                k_begin,
                k_round,
                k_finish,
            ]

        self.workers.append(Worker(kv_body, args, tile=kv_tile, stack_size=1024 * 6))
        self.rt.add_tile_dma(
            TileDma(
                kv_tile,
                [
                    _single_bd(
                        DMAChannelDir.MM2S,
                        0,
                        o,
                        o_cons,
                        o_prod,
                        packet=(0, _X_FROM_ATTN),
                        tap=TensorAccessPattern(
                            o.shape, 0, [NQ, dh // 8, 8], [8, NQ * 8, 1]
                        ),
                    ),
                ],
            )
        )

    def attn_qk(
        self, qk_tile, name, rtp_key, dh, of_s, q_fifo, k_fifo, two_kv_heads, handshake
    ):
        """Build an attention qk core.

        The core takes q from q_fifo and k from k_fifo on S2MM 1. It sends the
        scores to of_s.
        It releases ``handshake`` once it has read its RTPs.
        """
        n = self.label(qk_tile)
        # Every qk kernel names its entry points attn_qk_*.
        k_begin = self.entry(name, "attn_qk_begin")
        if two_kv_heads:
            k_half = self.entry(name, "attn_qk_half")
            k_storec = self.entry(name, "attn_qk_store_c")
            k_step = k_half
        else:
            k_round = self.entry(name, "attn_qk_round")
            k_step = k_round
        q_ty, _, _, m_ty, c_ty = k_step.arg_types()[:5]
        # The kernel pads each KV head's query group.
        (q_len,) = np_ndarray_type_get_shape(q_ty)
        NQ_PADDED = q_len // dh
        L = self.rtp_buffer(qk_tile, rtp_key)
        q_in_order = TensorAccessPattern(
            (NQ_PADDED, dh), 0, [NQ_PADDED, dh // 8, 8], [8, NQ_PADDED * 8, 1]
        )
        m_buf = Buffer(type=m_ty, name=f"m_{n}", tile=qk_tile)
        c_local = Buffer(type=c_ty, name=f"c_local_{n}", tile=qk_tile)
        # The q acquire orders the RTP read after the sequence's RTP writes.
        if two_kv_heads:

            def qk_two_heads(hs, s_out, q_h, k_h, mm, cc, rtp_l, kb, kh, ks):
                q = q_h.acquire(1)
                kb(mm)
                hs.release(1)
                for i in range_((rtp_l[0] + (LK - 1)) // LK):
                    s = s_out.acquire(1)
                    for j in range_(2):
                        k = k_h.acquire(1)
                        kh(q, k, s, mm, cc, j, i, rtp_l[0])
                        k_h.release(1)
                    ks(s, cc)
                    s_out.release(1)
                q_h.release(1)

            qk_body = qk_two_heads
            kerns = [k_begin, k_half, k_storec]
        else:

            def qk_rounds(hs, s_out, q_h, k_h, mm, cc, rtp_l, kb, kr):
                q = q_h.acquire(1)
                kb(mm)
                hs.release(1)
                for i in range_((rtp_l[0] + (LK - 1)) // LK):
                    s = s_out.acquire(1)
                    k = k_h.acquire(1)
                    kr(q, k, s, mm, cc, i, rtp_l[0])
                    k_h.release(1)
                    s_out.release(1)
                q_h.release(1)

            qk_body = qk_rounds
            kerns = [k_begin, k_round]

        args = [
            handshake,
            of_s.prod(),
            q_fifo.cons(from_stream=q_in_order),
            k_fifo.cons(port=Port.dma(1)),
            m_buf,
            c_local,
            L,
        ] + kerns
        self.workers.append(Worker(qk_body, args, tile=qk_tile, stack_size=1024 * 4))

    def route(
        self, proj_send_tiles: list[list[Tile]]
    ) -> dict[str, Flow | PacketFlow | ObjectFifoHandle]:
        """Add every flow between the stages, long ones first.

        The router places them in the order the design adds them; returns
        the flows the runtime sequence fills and drains, by name.
        """
        rt, t = self.rt, self.t
        x_shim = t["x_shim"]

        def add(*names):
            for name in names:
                rt.add_flow(self.flows[name])

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

        groups = range(len(PROJ_MEMS))
        add(*(f"proj_w{h}_{i}" for i in groups for h in (0, 1)))
        add(*(f"w{j}_{i}" for i in groups for j in range(4)))
        add("proj_x")
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

        add("recv_k", "recv_v")
        _connect(rt, t["attn_kv"], 0, proj_x, 3, pkt_id=_X_FROM_ATTN)
        _connect(rt, t["swa_attn_kv"], 0, proj_x, 3, pkt_id=_X_FROM_ATTN)
        _connect(rt, t["glu"], 0, proj_x, 3, pkt_id=_X_FROM_GLU)

        add("pli_rope_rms")
        return (
            shim
            | self.shim_fifos
            | {
                name: flow
                for name, flow in self.flows.items()
                if any(tile.tile_type == _SHIM for tile in flow.all_tiles())
            }
        )


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
    # x reuses pli_rope_rms's channel as a second BD.
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


_LINEAR_4W_TY = np.ndarray[(4 * W_BLOCK,), _BF16]
# The inits of a projection memtile's weight locks.
_PROJ_MEM_W_INITS = (2, 0, 0, 2, 0, 0)


def _proj_weight_channels(w0, w1, in_ends, out_ends, *locks):
    """Return a memtile's weight channels on flow ends ``in_ends``/``out_ends``.

    Each half of a weight object comes in on its own channel, then goes out
    a W_BLOCK at a time on two, behind a chain of three locks.
    """
    w = TensorAccessPattern.full(w0.shape)
    ins, outs = [], []
    for h in (0, 1):
        prod, cons0, cons1 = locks[3 * h : 3 * h + 3]
        ins.append(
            _ping_pong(
                DMAChannelDir.S2MM,
                in_ends[h],
                w0,
                w1,
                prod,
                cons0,
                tap=w[2 * h * W_BLOCK : (2 * h + 2) * W_BLOCK],
            )
        )
        for j, (acq, rel) in enumerate(((cons0, cons1), (cons1, prod))):
            ch = 2 * h + j
            outs.append(
                _ping_pong(
                    DMAChannelDir.MM2S,
                    out_ends[ch],
                    w0,
                    w1,
                    acq,
                    rel,
                    tap=w[ch * W_BLOCK : (ch + 1) * W_BLOCK],
                )
            )
    return {"in0": ins[0], "in1": ins[1], "out": outs}


def _proj_weight_buffers(mt, name):
    """Return a projection memtile's weight ping and pong buffers."""
    w0 = Buffer(type=_LINEAR_4W_TY, name=f"w_buffer_0_{name}", tile=mt)
    w1 = Buffer(type=_LINEAR_4W_TY, name=f"w_buffer_1_{name}", tile=mt)
    return w0, w1


def decode_layer(
    dev,
    geometry,
    layer_type,
    *,
    kernels,
    context_len: DispatchTime[np.int32],
    max_l: DispatchTime[np.int32],
):
    """Return the MLIR module of one decode layer of ``layer_type`` for ``geometry``.

    ``layer_type`` sets only the runtime sequence, ``kernels`` holds
    ``layer_kernels(geometry)``. README.md explains ``context_len`` and
    ``max_l``.
    """
    g = geometry
    sizes = arg_sizes(g)
    # The array fills these in before the sequence body runs.
    shim, rtps, sync_locks = {}, {}, {}
    array = _Array(g, kernels)
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
