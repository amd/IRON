# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's fused decode layer on the whole array, one token through one layer.

Reproduces FastFlowLM's xclbin and runtime sequence. One core runs each
stage (RMS norm and residual, RoPE, 16 q4nx projection cores, GLU, the
per-layer-input path, one attention pair per kind); the sequence writes the
layer type into RTPs, then streams the weights, KV cache and hidden state.
Each core's body calls its kernel's compute steps and takes the locks of
the DMA channels around it.
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
from aie.iron.controlflow import else_, if_, range_
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
PROJ_CORES = 4 * len(PROJ_MEMS)

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


# The consumer of each projection after qkv, whose consumer is the layer
# type's RoPE core.
_PROJ_PKT = {
    "o": _ProjPkt.to_rms,
    "up_gate": _ProjPkt.to_glu,
    "down": _ProjPkt.to_rms,
}

# Packet ids into the projection engine's x input.
_X_FROM_RMS = 0
_X_FROM_ATTN = 0
_X_FROM_GLU = 22
# Packet ids of the KV cache streams into the attention memtile.
_KV_PKT_GLOBAL = 12
_KV_PKT_SWA = 13


def layer_kernels(geometry):
    """Return the flm_gemma4_decode_* kernels this design's cores call, by name.

    The global attention kernels also depend on the geometry's KV head
    count.
    """
    g = geometry
    two_kv = g.num_kv_heads == 2
    return {
        "rms_residual": flm_gemma4.flm_gemma4_decode_rms_residual(geometry=g),
        "rope": flm_gemma4.flm_gemma4_decode_rope(geometry=g),
        "swa_rope": flm_gemma4.flm_gemma4_decode_rope(geometry=g, sliding_window=True),
        "bf16_proj_zero": flm_gemma4.flm_gemma4_decode_bf16_proj_zero(geometry=g),
        "proj_layer_embedding": flm_gemma4.flm_gemma4_decode_proj_layer_embedding(
            geometry=g
        ),
        "proj_layer_embedding_mvm": (
            flm_gemma4.flm_gemma4_decode_proj_layer_embedding_mvm(geometry=g)
        ),
        "proj_layer_embedding_store": (
            flm_gemma4.flm_gemma4_decode_proj_layer_embedding_store(geometry=g)
        ),
        "gate_layer_embedding": flm_gemma4.flm_gemma4_decode_gate_layer_embedding(
            geometry=g
        ),
        "gate_layer_embedding_mvm": (
            flm_gemma4.flm_gemma4_decode_gate_layer_embedding_mvm(geometry=g)
        ),
        "gate_layer_embedding_store": (
            flm_gemma4.flm_gemma4_decode_gate_layer_embedding_store(geometry=g)
        ),
        "per_layer_up": flm_gemma4.flm_gemma4_decode_per_layer_up(geometry=g),
        "per_layer_up_mvm": flm_gemma4.flm_gemma4_decode_per_layer_up_mvm(geometry=g),
        "per_layer_up_store": flm_gemma4.flm_gemma4_decode_per_layer_up_store(
            geometry=g
        ),
        "glu": flm_gemma4.flm_gemma4_decode_glu(geometry=g),
        "proj_main": flm_gemma4.flm_gemma4_decode_proj_main(geometry=g),
        "attn_kv": (
            flm_gemma4.flm_gemma4_decode_attn_kv_kvh2(geometry=g)
            if two_kv
            else flm_gemma4.flm_gemma4_decode_attn_kv(geometry=g)
        ),
        "attn_qk": (
            flm_gemma4.flm_gemma4_decode_attn_qk_kvh2(geometry=g)
            if two_kv
            else flm_gemma4.flm_gemma4_decode_attn_qk(geometry=g)
        ),
        "swa_attn_kv": flm_gemma4.flm_gemma4_decode_swa_attn_kv(geometry=g),
        "swa_attn_qk": flm_gemma4.flm_gemma4_decode_attn_qk(
            geometry=g, sliding_window=True
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


def _by_layer_type(swa, skip, values: dict[LayerType, int]):
    """Return this dispatch's entry of ``values``, by its layer type.

    An int where every layer type agrees, else an i32 a core selects from
    ``swa`` and ``skip``, the i1 flags it read from its RTPs.
    """
    if len(set(values.values())) == 1:
        return values[LayerType.GLOBAL]
    by_skip = {
        kind: arith.select(skip, _as_i32(values[skipped]), _as_i32(values[kind]))
        for kind, skipped in (
            (LayerType.GLOBAL, LayerType.GLOBAL_SKIP),
            (LayerType.SWA, LayerType.SWA_SKIP),
        )
    }
    return arith.select(swa, by_skip[LayerType.SWA], by_skip[LayerType.GLOBAL])


class _Pair(NamedTuple):
    """Two buffers of a core that one DMA channel fills or drains in turn.

    The core acquires ``core_acquires``, uses a buffer and releases
    ``core_releases``; the channel does the reverse. A core that takes the
    pair an odd or run-time number of times per layer keeps whose turn it is
    in ``turn``, a word of its memory.
    """

    first: Buffer
    second: Buffer
    core_acquires: Lock
    core_releases: Lock
    direction: DMAChannelDir
    turn: Buffer | None

    def channel(self, channel, **bd_args) -> DmaChannel:
        """Return the DMA channel ``channel`` that fills or drains the pair."""
        return DmaChannel(
            self.direction,
            channel,
            ping_pong(
                self.first,
                self.second,
                self.core_releases,
                self.core_acquires,
                **bd_args,
            ),
        )

    def next(self, use) -> None:
        """Emit the core's turn at the next buffer, calling ``use(buffer)`` under its locks.

        Raises:
            ValueError: The pair keeps no ``turn``.
        """
        turn = self.turn
        if turn is None:
            raise ValueError("_Pair.next: the pair keeps no turn")
        self.core_acquires.acquire()
        with if_(turn[0] == 0) as branch:
            use(self.first)
        with else_(branch):
            use(self.second)
        self.core_releases.release()
        turn[0] = 1 - turn[0]


@dataclass
class _Array:
    """The decode layer's array as its stages build it.

    Each stage adds its cores, locks and DMA channels to ``rt``/``workers``,
    keyed by stage in ``t``, ``flows``, ``rtps`` and ``sync_locks``. RMS,
    GLU, attention-kv and projection cores acquire their sync lock before
    reading RTPs (the sequence sets it after writing); RoPE and
    attention-qk cores instead wait for the projection cores.
    """

    rt: Runtime
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
        for dst in ("attn_qk", "attn_kv", "swa_attn_qk", "swa_attn_kv"):
            ends[f"amt_{dst}"] = t["attn_mem"], t[dst]
        for name, src, dst in (
            ("pli_rope_rms", "pl_shim_0", "pl_embedding"),
            ("pli_down", "pl_shim_0", "pl_embedding"),
            ("ple_y", "pl_embedding", "pl_merge"),
            ("pli_gate", "pl_shim_1", "pl_gate"),
            ("plg_y", "pl_gate", "pl_merge"),
            ("plm_y", "pl_merge", "pl_up"),
            ("pli_up", "pl_shim_1", "pl_up"),
            ("recv_y", "pl_up", "x_shim"),
        ):
            ends[name] = t[src], t[dst]
        self.flows = {
            name: Flow(src, dst, name=name) for name, (src, dst) in ends.items()
        }

    def label(self, tile: Tile) -> str:
        """``tile``'s stage."""
        return next(stage for stage, at in self.t.items() if at is tile)

    def end(self, flow: str, tile: Tile):
        """Return the end of the circuit ``flow`` on ``tile``, for its DMA channel."""
        return self.flows[flow].endpoint(tile)

    def build(self) -> dict[str, Flow | PacketFlow]:
        """Build every stage, then every flow between them.

        Returns the flows the runtime sequence fills and drains, by name.
        """
        g, t = self.g, self.t
        G_DQ = g.num_attn_heads * g.dh
        S_DQ = g.num_attn_heads * g.swa_dh
        two_kv = g.num_kv_heads == 2

        rms_out = self.rms(t["rms"])
        # q from RoPE to the qk core. The qk core's DMA reorders it.
        q_of_g = ObjectFifo(np.ndarray[(G_DQ,), _BF16], depth=2)
        q_of_swa = ObjectFifo(np.ndarray[(S_DQ,), _BF16], depth=2)
        self.rope(t["rope"], "rope", "rope_skip_kv", "recv_k", q_of_g)
        self.rope(t["swa_rope"], "swa_rope", "swa_rope_skip_kv", "recv_v", q_of_swa)
        self.pl_embedding(t["pl_embedding"])
        self.pl_gate(t["pl_gate"], *rms_out)
        self.pl_merge(t["pl_merge"])
        self.pl_up(t["pl_up"])
        self.glu(t["glu"])

        proj_send_tiles = self.proj_cores()
        self.proj_gather_mem(t["proj_gather_0"])
        self.proj_gather_mem(t["proj_gather_1"])
        self.proj_weight_mem(t["proj_weight"])
        self.proj_x_mem(t["proj_x"])

        of_g_s = ObjectFifo(self.scores_ty("attn_kv"), delegate_tile=t["attn_kv"])
        self.attn_kv(t["attn_kv"], "attn_kv", "l_kv", g.dh, of_g_s, two_kv)
        self.attn_qk(t["attn_qk"], "attn_qk", "l_qk", g.dh, of_g_s, q_of_g, two_kv)
        of_swa_s = ObjectFifo(
            self.scores_ty("swa_attn_kv"),
            delegate_tile=t["swa_attn_kv"],
        )
        self.attn_kv(
            t["swa_attn_kv"], "swa_attn_kv", "swa_l_kv", g.swa_dh, of_swa_s, False
        )
        self.attn_qk(
            t["swa_attn_qk"],
            "swa_attn_qk",
            "swa_l_qk",
            g.swa_dh,
            of_swa_s,
            q_of_swa,
            False,
        )
        self.attn_mem(t["attn_mem"])
        return self.route(proj_send_tiles)

    def entry(self, name: str, symbol: str):
        """Return the entry point ``symbol`` of the kernel ``name``, typed by its factory."""
        return getattr(self.kernels[name], symbol)

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

    def locks(self, tile: Tile, *inits: int) -> list[Lock]:
        """Return new locks of ``tile``, one per initial value; the compiler picks their ids."""
        out = [Lock(tile=tile, init=init) for init in inits]
        for lock in out:
            self.rt.add_lock(lock)
        return out

    def pair(
        self, tile: Tile, ty, name: str, direction: DMAChannelDir, turn: bool = False
    ) -> _Pair:
        """Return a ping-pong pair of ``tile``'s buffers for a DMA channel in ``direction``.

        With ``turn``, the core keeps whose turn it is (see ``_Pair``).
        """
        first, second = (Buffer(type=ty, name=f"{name}_{i}", tile=tile) for i in (0, 1))
        free, full = self.locks(tile, 2, 0)
        into = direction == DMAChannelDir.S2MM
        return _Pair(
            first,
            second,
            full if into else free,
            free if into else full,
            direction,
            (
                Buffer(
                    initial_value=np.zeros(1, np.int32), name=f"{name}_turn", tile=tile
                )
                if turn
                else None
            ),
        )

    def core(
        self,
        tile: Tile,
        body,
        args: list,
        channels: list[DmaChannel],
    ) -> None:
        """Run a core on ``body`` and ``args``, with its tile's DMA channels."""
        self.workers.append(Worker(body, args, tile=tile))
        self.rt.add_tile_dma(TileDma(tile, channels))

    def projections(self, swa, skip) -> list[tuple]:
        """Return each projection's (row blocks, input block pairs, packet id) on one core.

        In the layer's order: qkv, o, up_gate and down. A round of the
        projection cores covers ``PROJ_CORES`` row blocks; a core takes its
        input and weight blocks in pairs, one from each buffer of its
        ping-pong pairs. ``swa`` and ``skip`` are the layer type's flags, as
        ``_by_layer_type`` takes them.

        Raises:
            ValueError: A projection's shape does not split into whole rounds
                and block pairs.
        """
        weights = {t: LayerDims(self.g, t).weights for t in LayerType}
        rows_per_round = PROJ_CORES * q4nx.M_TILE
        out = []
        for name in ("qkv", "o", "up_gate", "down"):
            shapes = {t: (w[name].dout, w[name].din) for t, w in weights.items()}
            if any(
                dout % rows_per_round or din % (2 * X_SLICE)
                for dout, din in shapes.values()
            ):
                raise ValueError(
                    f"projections: {name}'s shapes {sorted(set(shapes.values()))} "
                    f"do not split into rounds of {rows_per_round} rows and pairs "
                    f"of {X_SLICE}-wide input blocks"
                )
            packets = (
                {
                    t: _ProjPkt.to_swa_rope if t.swa else _ProjPkt.to_rope
                    for t in LayerType
                }
                if name == "qkv"
                else dict.fromkeys(LayerType, _PROJ_PKT[name])
            )
            out.append(
                (
                    _by_layer_type(
                        swa,
                        skip,
                        {t: dout // rows_per_round for t, (dout, _) in shapes.items()},
                    ),
                    _by_layer_type(
                        swa,
                        skip,
                        {t: din // (2 * X_SLICE) for t, (_, din) in shapes.items()},
                    ),
                    _by_layer_type(swa, skip, {t: int(p) for t, p in packets.items()}),
                )
            )
        return out

    def rms(self, rms_tile: Tile) -> tuple[Buffer, Lock, Lock]:
        """RMS norm and residual.

        Returns y_out, the layer output the gate core reads, and the locks
        that hand it over: the one the gate core acquires, then the one it
        releases.
        """
        k = self.kernels["rms_residual"]
        middle = self.entry("rms_residual", "rms_middle")
        finish = self.entry("rms_residual", "rms_finish")
        x_ty, w_ty, state_ty, y_ty = k.arg_types()
        n = self.label(rms_tile)
        x = self.pair(rms_tile, x_ty, f"x_{n}", DMAChannelDir.S2MM, turn=True)
        w = Buffer(type=w_ty, name=f"w_buffer_{n}", tile=rms_tile)
        state = Buffer(type=state_ty, name=f"x_buf_{n}", tile=rms_tile)
        y = Buffer(type=y_ty, name=f"y_{n}", tile=rms_tile)
        y_out = Buffer(type=x_ty, name=f"y_out_{n}", tile=rms_tile)
        is_swa = self.rtp_buffer(rms_tile, "rms_swa")
        skip = self.rtp_buffer(rms_tile, "rms_skip")
        # y_free counts y's sends; the core waits for all of a projection's.
        w_free, w_full, y_free, y_full, out_free, out_full, rtp_ready = self.locks(
            rms_tile, 1, 0, 0, 0, 1, 0, 0
        )
        self.sync_locks[n] = rtp_ready

        def body(x, w, state, y, y_out, is_swa, skip, begin, middle, finish):
            rtp_ready.acquire()
            projections = self.projections(is_swa[0] != 0, skip[0] != 0)
            qkv_rounds, up_gate_rounds = projections[0][0], projections[2][0]
            w_full.acquire()
            x.next(lambda xb: begin(xb, w, state, y))
            y_full.release(qkv_rounds)

            def norm_attention(xb):
                y_free.acquire(qkv_rounds)
                middle(xb, w, state, y)

            x.next(norm_attention)
            y_full.release(up_gate_rounds)

            def norm_mlp(xb):
                y_free.acquire(up_gate_rounds)
                out_free.acquire()
                finish(xb, w, state, y_out)

            x.next(norm_mlp)
            w_free.release()
            out_full.release()

        self.core(
            rms_tile,
            body,
            [x, w, state, y, y_out, is_swa, skip, k, middle, finish],
            [
                x.channel(0),
                _single_bd(DMAChannelDir.S2MM, 1, w, w_free, w_full),
                _single_bd(
                    DMAChannelDir.MM2S,
                    0,
                    y,
                    y_full,
                    y_free,
                    tap=TensorAccessPattern.full(y.shape)[14:],
                ),
            ],
        )
        return y_out, out_full, out_free

    def rope(
        self, rope_tile: Tile, name: str, rtp_key: str, kv_out: str, q_fifo: ObjectFifo
    ) -> None:
        """RoPE, global or sliding-window. k and v leave on the flow ``kv_out``."""
        g = self.g
        rope_q = self.kernels[name]
        rope_k = self.entry(name, "rope_k")
        rope_v = self.entry(name, "rope_v")
        _, qkv_ty, rope_ty, _ = rope_q.arg_types()
        kv_ty = rope_k.arg_types()[0]
        if g.num_attn_heads % 2:
            raise ValueError(
                f"rope: {g.num_attn_heads} query heads leave the qkv pair's "
                "turn odd past q"
            )

        n = self.label(rope_tile)
        qkv = self.pair(rope_tile, qkv_ty, f"qkv_buffer_{n}", DMAChannelDir.S2MM)
        k_buf = Buffer(type=kv_ty, name=f"k_buffer_{n}", tile=rope_tile)
        v_buf = Buffer(type=kv_ty, name=f"v_buffer_{n}", tile=rope_tile)
        rope_buf = Buffer(type=rope_ty, name=f"rope_buffer_{n}", tile=rope_tile)
        skip_kv = self.rtp_buffer(rope_tile, rtp_key)
        k_free, k_full, v_free, v_full, rope_free, rope_full = self.locks(
            rope_tile, 1, 0, 1, 0, 1, 0
        )
        q_h = q_fifo.prod()

        def body(q_h, qkv, kk, v, rope, skip, rope_q, rope_k, rope_v):
            q = q_h.acquire(1)
            rope_full.acquire()
            # q's heads, then k's and v's, each one qkv buffer; q leaves the
            # pair's turn where it began, and so do k and v together.
            for i in range_(g.num_attn_heads // 2):
                for half, buf in enumerate((qkv.first, qkv.second)):
                    qkv.core_acquires.acquire()
                    rope_q(q, buf, rope, 2 * i + half)
                    qkv.core_releases.release()
            with if_(skip[0] == 0):
                bufs = (qkv.first, qkv.second)
                k_free.acquire()
                for h in range(g.num_kv_heads):
                    qkv.core_acquires.acquire()
                    rope_k(kk, bufs[h % 2], rope, h)
                    qkv.core_releases.release()
                k_full.release()
                v_free.acquire()
                for h in range(g.num_kv_heads):
                    qkv.core_acquires.acquire()
                    rope_v(v, bufs[(g.num_kv_heads + h) % 2], h)
                    qkv.core_releases.release()
                v_full.release()
            rope_free.release()
            q_h.release(1)

        self.core(
            rope_tile,
            body,
            [q_h, qkv, k_buf, v_buf, rope_buf, skip_kv, rope_q, rope_k, rope_v],
            [
                qkv.channel(0),
                DmaChannel(
                    DMAChannelDir.MM2S,
                    self.end(kv_out, rope_tile),
                    [
                        Bd(
                            buf,
                            acquires=[Acquire(full)],
                            releases=[Release(free)],
                            next=nxt,
                        )
                        for buf, full, free, nxt in (
                            (k_buf, k_full, k_free, 1),
                            (v_buf, v_full, v_free, 0),
                        )
                    ],
                ),
                _single_bd(DMAChannelDir.S2MM, 1, rope_buf, rope_free, rope_full),
            ],
        )

    def pl_embedding(self, ple_tile: Tile) -> None:
        """Per-layer-input embedding.

        Its input buffer holds the token's per-layer embedding, the norm
        weight with the values passed on to the up projection, then the
        layer input x0, which the projection reads.
        """
        g = self.g
        P = g.pli_d
        n = self.label(ple_tile)
        finish = self.kernels["proj_layer_embedding"]
        zero = self.kernels["bf16_proj_zero"]
        mvm = self.kernels["proj_layer_embedding_mvm"]
        store = self.kernels["proj_layer_embedding_store"]
        in_ty, x_proj_ty, y_ty = finish.arg_types()
        w_ty, _, acc_ty = mvm.arg_types()[:3]
        inp = Buffer(type=in_ty, name=f"x_{n}", tile=ple_tile)
        x_proj = Buffer(type=x_proj_ty, name=f"x_proj_{n}", tile=ple_tile)
        y = Buffer(type=y_ty, name=f"y_{n}", tile=ple_tile)
        acc = Buffer(type=acc_ty, name=f"acc_{n}", tile=ple_tile)
        w = self.pair(ple_tile, w_ty, f"proj_w_{n}", DMAChannelDir.S2MM)
        (in_len,) = inp.shape
        x0 = in_len - g.model_dim
        # The input's four BDs, each releasing the next; the last, the core's.
        chain = self.locks(ple_tile, 1, 0, 0, 0, 0)
        in_free, in_full = chain[0], chain[-1]
        y_free, y_full = self.locks(ple_tile, 1, 0)
        x = TensorAccessPattern.full(inp.shape)
        taps = (x[:P], x[P : 2 * P], x[2 * P : x0], x[x0:])

        def body(inp, x_proj, y, acc, w, zero, mvm, store, finish):
            in_full.acquire()
            y_free.acquire()
            for i in range_(P // q4nx.M_TILE):
                zero(acc)
                for j in range_(g.model_dim // (2 * X_SLICE)):
                    for half, wb in enumerate((w.first, w.second)):
                        w.core_acquires.acquire()
                        mvm(wb, inp, acc, 2 * j + half, x0)
                        w.core_releases.release()
                store(x_proj, acc, i, 0)
            finish(inp, x_proj, y)
            y_full.release()
            in_free.release()

        self.core(
            ple_tile,
            body,
            [inp, x_proj, y, acc, w, zero, mvm, store, finish],
            [
                DmaChannel(
                    DMAChannelDir.S2MM,
                    self.end("pli_rope_rms", ple_tile),
                    [
                        Bd(
                            inp,
                            tap=tap,
                            acquires=[Acquire(chain[i])],
                            releases=[Release(chain[i + 1])],
                            next=(i + 1) % len(taps),
                        )
                        for i, tap in enumerate(taps)
                    ],
                ),
                w.channel(self.end("pli_down", ple_tile)),
                _single_bd(
                    DMAChannelDir.MM2S, self.end("ple_y", ple_tile), y, y_full, y_free
                ),
            ],
        )

    def pl_gate(self, gle_tile: Tile, x: Buffer, x_full: Lock, x_free: Lock) -> None:
        """Per-layer-input gate, on the layer output ``x`` of the RMS tile.

        ``x_full`` and ``x_free`` are the RMS tile's locks that hand it over.
        """
        g = self.g
        n = self.label(gle_tile)
        begin = self.kernels["gate_layer_embedding"]
        finish = self.entry("gate_layer_embedding", "gate_layer_embedding_finish")
        zero = self.kernels["bf16_proj_zero"]
        mvm = self.kernels["gate_layer_embedding_mvm"]
        store = self.kernels["gate_layer_embedding_store"]
        y_ty = begin.arg_types()[1]
        w_ty, _, acc_ty = mvm.arg_types()[:3]
        y = Buffer(type=y_ty, name=f"y_{n}", tile=gle_tile)
        acc = Buffer(type=acc_ty, name=f"acc_{n}", tile=gle_tile)
        w = self.pair(gle_tile, w_ty, f"proj_w_{n}", DMAChannelDir.S2MM)
        y_free, y_full = self.locks(gle_tile, 1, 0)

        def body(x, y, acc, w, begin, zero, mvm, store, finish):
            x_full.acquire()
            y_free.acquire()
            begin(x, y)
            x_free.release()
            # The projection reads x from y, and writes past it.
            for i in range_(g.pli_d // q4nx.M_TILE):
                zero(acc)
                for j in range_(g.model_dim // (2 * X_SLICE)):
                    for half, wb in enumerate((w.first, w.second)):
                        w.core_acquires.acquire()
                        mvm(wb, y, acc, 2 * j + half, 0)
                        w.core_releases.release()
                store(y, acc, i, g.model_dim)
            finish(y)
            y_full.release()

        self.core(
            gle_tile,
            body,
            [x, y, acc, w, begin, zero, mvm, store, finish],
            [
                w.channel(self.end("pli_gate", gle_tile)),
                _single_bd(
                    DMAChannelDir.MM2S, self.end("plg_y", gle_tile), y, y_full, y_free
                ),
            ],
        )

    def pl_merge(self, plm_tile: Tile) -> None:
        """Per-layer-input merge.

        No kernel runs here, its DMA gathers the embedding and gate outputs
        into one buffer for the up projection.
        """
        D, PLI_D = self.g.model_dim, self.g.pli_d
        plm_dual_y_ty = np.ndarray[(2 * (PLI_D + D) + 32,), _BF16]
        plm_y = Buffer(
            type=plm_dual_y_ty, name=f"y_{self.label(plm_tile)}", tile=plm_tile
        )
        plm_norm_i_prod, plm_res_gate_prod, plm_cons = self.locks(plm_tile, 1, 0, 0)
        self.rt.add_tile_dma(
            TileDma(
                plm_tile,
                [
                    _single_bd(
                        DMAChannelDir.S2MM,
                        self.end("ple_y", plm_tile),
                        plm_y,
                        plm_norm_i_prod,
                        plm_res_gate_prod,
                        tap=TensorAccessPattern.full(plm_y.shape)[: D + PLI_D + 32],
                    ),
                    _single_bd(
                        DMAChannelDir.S2MM,
                        self.end("plg_y", plm_tile),
                        plm_y,
                        plm_res_gate_prod,
                        plm_cons,
                        tap=TensorAccessPattern.full(plm_y.shape)[D + PLI_D + 32 :],
                    ),
                    _single_bd(
                        DMAChannelDir.MM2S,
                        self.end("plm_y", plm_tile),
                        plm_y,
                        plm_cons,
                        plm_norm_i_prod,
                    ),
                ],
            )
        )

    def pl_up(self, plu_tile: Tile) -> None:
        """Per-layer-input up projection."""
        g = self.g
        n = self.label(plu_tile)
        begin = self.kernels["per_layer_up"]
        finish = self.entry("per_layer_up", "per_layer_up_finish")
        zero = self.kernels["bf16_proj_zero"]
        mvm = self.kernels["per_layer_up_mvm"]
        store = self.kernels["per_layer_up_store"]
        x_ty, y_ty = finish.arg_types()
        w_ty, _, acc_ty = mvm.arg_types()[:3]
        x = Buffer(type=x_ty, name=f"x_{n}", tile=plu_tile)
        y = Buffer(type=y_ty, name=f"y_{n}", tile=plu_tile)
        acc = Buffer(type=acc_ty, name=f"acc_{n}", tile=plu_tile)
        # A row takes pli_d // X_SLICE blocks, one with both models.
        w = self.pair(plu_tile, w_ty, f"proj_w_{n}", DMAChannelDir.S2MM, turn=True)
        x_free, x_full, y_free, y_full = self.locks(plu_tile, 1, 0, 1, 0)
        # The per-layer input follows the norm weight and the layer scale.
        pli = g.model_dim + 32

        def body(x, y, acc, w, begin, zero, mvm, store, finish):
            x_full.acquire()
            y_free.acquire()
            begin(x)
            for i in range_(g.model_dim // q4nx.M_TILE):
                zero(acc)
                for j in range_(g.pli_d // X_SLICE):
                    w.next(lambda wb: mvm(wb, x, acc, j, pli))
                store(y, acc, i, 0)
            finish(x, y)
            y_full.release()
            x_free.release()

        self.core(
            plu_tile,
            body,
            [x, y, acc, w, begin, zero, mvm, store, finish],
            [
                _single_bd(
                    DMAChannelDir.S2MM, self.end("plm_y", plu_tile), x, x_free, x_full
                ),
                w.channel(self.end("pli_up", plu_tile)),
                _single_bd(
                    DMAChannelDir.MM2S, self.end("recv_y", plu_tile), y, y_full, y_free
                ),
            ],
        )

    def glu(self, glu_tile: Tile) -> None:
        """GLU."""
        g = self.g
        n = self.label(glu_tile)
        chunk = self.kernels["glu"]
        emit = self.entry("glu", "glu_emit")
        hid_ty, x_ty, _ = chunk.arg_types()
        y_ty = emit.arg_types()[0]
        if g.intermediate_size % g.glu_slice:
            raise ValueError(
                f"glu: glu_slice ({g.glu_slice}) does not divide the "
                f"intermediate size ({g.intermediate_size})"
            )
        x = self.pair(glu_tile, x_ty, f"x_{n}", DMAChannelDir.S2MM)
        y = self.pair(glu_tile, y_ty, f"y_{n}", DMAChannelDir.MM2S)
        hid = Buffer(type=hid_ty, name=f"hid_0_{n}", tile=glu_tile)
        glu_is_skip = self.rtp_buffer(glu_tile, "glu_skip")
        (rtp_ready,) = self.locks(glu_tile, 0)
        self.sync_locks[n] = rtp_ready
        o_rounds = g.model_dim // (PROJ_CORES * q4nx.M_TILE)

        def body(x, y, hid, skip, chunk, emit):
            rtp_ready.acquire()
            # 2 * intermediate_size gate and up values in, a glu_slice at a
            # time; half as many out, a glu_slice // 2 at a time, per round
            # of the down projection; glu_skip doubles both. In pairs.
            pairs = (skip[0] + 1) * (g.intermediate_size // g.glu_slice)
            for i in range_(pairs):
                for half, xb in enumerate((x.first, x.second)):
                    x.core_acquires.acquire()
                    chunk(hid, xb, 2 * i + half)
                    x.core_releases.release()
            for _ in range_(o_rounds):
                for j in range_(pairs):
                    for half, yb in enumerate((y.first, y.second)):
                        y.core_acquires.acquire()
                        emit(yb, hid, 2 * j + half)
                        y.core_releases.release()

        self.core(
            glu_tile,
            body,
            [x, y, hid, glu_is_skip, chunk, emit],
            [x.channel(0), y.channel(0, packet=(0, _X_FROM_GLU))],
        )

    def proj_core(self, group: int, j: int, rows, sends: bool) -> None:
        """Build core ``j`` of projection group ``group``.

        A sending core packs each row block of its own and the row block
        its neighbour hands it through ``rows``, the consumer end, into y
        for its group's memtile; the neighbour gets the producer end.
        """
        n = f"proj_{group}_{j}"
        pt = self.t[n]
        mac = self.kernels["proj_main"]
        zero = self.entry("proj_main", "proj_zero")
        store = self.entry("proj_main", "proj_store")
        pack = self.entry("proj_main", "proj_pack")
        w_ty, x_ty, acc_ty, sums_ty = mac.arg_types()[:4]
        x = self.pair(pt, x_ty, f"x_{n}", DMAChannelDir.S2MM)
        w = self.pair(pt, w_ty, f"w_{n}", DMAChannelDir.S2MM)
        acc = Buffer(type=acc_ty, name=f"acc_{n}", tile=pt)
        sums = Buffer(type=sums_ty, name=f"sums_{n}", tile=pt)
        is_swa = self.rtp_buffer(pt, "proj_swa")
        skip_kv = self.rtp_buffer(pt, "proj_skip")
        (rtp_ready,) = self.locks(pt, 0)
        self.sync_locks[n] = rtp_ready
        chans = [
            x.channel(self.end("proj_x", pt)),
            w.channel(self.end(f"w{j}_{group}", pt)),
        ]
        y = None
        if sends:
            y = self.pair(
                pt, pack.arg_types()[0], f"y_{n}", DMAChannelDir.MM2S, turn=True
            )
            chans.append(y.channel(0, tap=TensorAccessPattern.full(y.first.shape)[14:]))

        def body(x, w, y, rows, acc, sums, is_swa, skip, mac, zero, store, pack):
            rtp_ready.acquire()
            for row_blocks, input_pairs, packet in self.projections(
                is_swa[0] != 0, skip[0] != 0
            ):
                for i in range_(row_blocks):
                    zero(acc)
                    for k in range_(input_pairs):
                        for half, (wb, xb) in enumerate(
                            ((w.first, x.first), (w.second, x.second))
                        ):
                            w.core_acquires.acquire()
                            x.core_acquires.acquire()
                            mac(wb, xb, acc, sums, i, 2 * k + half)
                            w.core_releases.release()
                            x.core_releases.release()
                    row = rows.acquire(1)
                    if y is None:
                        store(row, acc)
                    else:
                        y.next(lambda yb: pack(yb, acc, row, packet))
                    rows.release(1)

        self.core(
            pt,
            body,
            [x, w, y, rows, acc, sums, is_swa, skip_kv, mac, zero, store, pack],
            chans,
        )

    def proj_cores(self) -> list[list[Tile]]:
        """Build the q4nx projection engine: 16 cores, four per group.

        Cores 0 and 2 of each group send y, each with the row blocks of the
        core after it. Returns each gather memtile's two groups' sending
        cores.
        """
        row_ty = self.entry("proj_main", "proj_store").arg_types()[0]
        proj_send_tiles = []
        for grp in range(2):
            group_send = []
            for csub in (0, 1):
                group = 2 * grp + csub
                for j in (0, 2):
                    send = self.t[f"proj_{group}_{j}"]
                    rows = ObjectFifo(row_ty, depth=2, delegate_tile=send)
                    self.proj_core(group, j, rows.cons(), sends=True)
                    self.proj_core(group, j + 1, rows.prod(), sends=False)
                    group_send.append(send)
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
            *self.locks(mt, *_PROJ_MEM_W_INITS),
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
        y_locks = self.locks(mt, 2, 0, 0, 0, 0)
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
        mp0, mp1, mc, xp, xc = self.locks(mt, 2, 0, 0, 2, 0)
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
        self,
        kv_tile: Tile,
        name: str,
        rtp_key: str,
        dh: int,
        of_s: ObjectFifo,
        two_kv_heads: bool,
    ) -> None:
        """Build an attention kv core.

        A round of the two-KV-head kernels covers one KV head per v buffer,
        so both of the pair; a round of the other kernels covers every KV
        head in one. The finished y, bf16 in its first half, is the output
        o, which the down projection reads once per round of its own.
        """
        g = self.g
        n = self.label(kv_tile)
        steps = ("s_begin", "v_half") if two_kv_heads else ("round",)
        kerns = [self.entry(name, f"{name}_{s}") for s in ("begin", *steps, "finish")]
        v_ty = kerns[-2].arg_types()[1]
        y_ty, l_ty = kerns[-1].arg_types()
        L = self.rtp_buffer(kv_tile, rtp_key)
        v = self.pair(
            kv_tile, v_ty, f"v_{n}", DMAChannelDir.S2MM, turn=not two_kv_heads
        )
        y = Buffer(type=y_ty, name=f"y_{n}", tile=kv_tile)
        lbuf = Buffer(type=l_ty, name=f"l_{n}", tile=kv_tile)
        o_rounds = g.model_dim // (PROJ_CORES * q4nx.M_TILE)
        o_free, o_full, rtp_ready = self.locks(kv_tile, o_rounds, 0, 0)
        self.sync_locks[n] = rtp_ready

        def body(s_in, v, yy, ll, rtp_l, kb, *kerns):
            *step, kf = kerns
            o_free.acquire(o_rounds)
            kb(yy, ll)
            rtp_ready.acquire()
            for _ in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_in.acquire(1)
                if two_kv_heads:
                    s_begin, v_half = step
                    s_begin(s, yy, ll)
                    for head, vb in enumerate((v.first, v.second)):
                        v.core_acquires.acquire()
                        v_half(s, vb, yy, head)
                        v.core_releases.release()
                else:
                    v.next(lambda vb: step[0](s, vb, yy, ll))
                s_in.release(1)
            kf(yy, ll)
            o_full.release(o_rounds)

        # o, bf16 in [dh/8, head, 8] order, as float32 words, head by head.
        o_order = TensorAccessPattern.full((dh // 8, g.num_attn_heads, 4)).permute(
            (1, 0, 2)
        )
        self.core(
            kv_tile,
            body,
            [of_s.cons(), v, y, lbuf, L, *kerns],
            [
                v.channel(self.end(f"amt_{name}", kv_tile)),
                _single_bd(
                    DMAChannelDir.MM2S,
                    0,
                    y,
                    o_full,
                    o_free,
                    packet=(0, _X_FROM_ATTN),
                    tap=o_order,
                ),
            ],
        )

    def attn_qk(
        self,
        qk_tile: Tile,
        name: str,
        rtp_key: str,
        dh: int,
        of_s: ObjectFifo,
        q_fifo: ObjectFifo,
        two_kv_heads: bool,
    ) -> None:
        """Build an attention qk core.

        A round of the two-KV-head kernel takes one k buffer per KV head,
        so both of the pair; a round of the others takes one.
        """
        n = self.label(qk_tile)
        # Every qk kernel names its entry points attn_qk_*.
        steps = ("half", "store_c") if two_kv_heads else ("round",)
        kerns = [self.entry(name, f"attn_qk_{s}") for s in ("begin", *steps)]

        # The q acquire orders the RTP read after the sequence's RTP writes.
        def body(s_out, q_h, k, mm, cc, rtp_l, kb, *step):
            q = q_h.acquire(1)
            kb(mm)
            for i in range_((rtp_l[0] + (LK - 1)) // LK):
                s = s_out.acquire(1)
                if two_kv_heads:
                    half, store_c = step
                    for head, kbuf in enumerate((k.first, k.second)):
                        k.core_acquires.acquire()
                        half(q, kbuf, s, mm, cc, head, i, rtp_l[0])
                        k.core_releases.release()
                    store_c(s, cc)
                else:
                    k.next(lambda kbuf: step[0](q, kbuf, s, mm, cc, i, rtp_l[0]))
                s_out.release(1)
            q_h.release(1)

        q_ty, k_ty, _, m_ty, c_ty = kerns[1].arg_types()[:5]
        # The kernel pads each KV head's query group.
        (q_len,) = np_ndarray_type_get_shape(q_ty)
        NQ_PADDED = q_len // dh
        k = self.pair(
            qk_tile, k_ty, f"k_{n}", DMAChannelDir.S2MM, turn=not two_kv_heads
        )
        L = self.rtp_buffer(qk_tile, rtp_key)
        q_in_order = TensorAccessPattern.full((dh // 8, NQ_PADDED, 8)).permute(
            (1, 0, 2)
        )
        m_buf = Buffer(type=m_ty, name=f"m_{n}", tile=qk_tile)
        c_local = Buffer(type=c_ty, name=f"c_local_{n}", tile=qk_tile)
        self.core(
            qk_tile,
            body,
            [
                of_s.prod(),
                q_fifo.cons(from_stream=q_in_order),
                k,
                m_buf,
                c_local,
                L,
                *kerns,
            ],
            [k.channel(self.end(f"amt_{name}", qk_tile))],
        )

    def attn_mem(self, amt: Tile) -> None:
        """Build the attention memtile."""
        g = self.g
        NUM_KV, two_kv = g.num_kv_heads, g.num_kv_heads == 2
        amt_name = self.label(amt)
        k_row = NUM_KV * g.dh
        sk_row = NUM_KV * g.swa_dh
        k = TensorAccessPattern.full((LK, k_row))
        sk = TensorAccessPattern.full((LK, sk_row))
        # k column groups of 8 down every row; v in 8 x 8 blocks, but as k when
        # two heads share the row.
        k_order = k.tile((LK, 8))[0]
        v_order = k_order if two_kv else k.tile((8, 8))
        amt_chans = []
        for ch, (key, dst, row, order) in enumerate(
            (
                ("k", "attn_qk", k_row, k_order),
                ("v", "attn_kv", k_row, v_order),
                ("swa_k", "swa_attn_qk", sk_row, sk.tile((LK, 8))[0]),
                ("swa_v", "swa_attn_kv", sk_row, sk.tile((8, 8))),
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
            prod, cons = self.locks(amt, 2, 0)
            amt_chans += [
                _ping_pong(DMAChannelDir.S2MM, ch, b0, b1, prod, cons),
                _ping_pong(
                    DMAChannelDir.MM2S,
                    self.end(f"amt_{dst}", amt),
                    b0,
                    b1,
                    cons,
                    prod,
                    tap=order,
                ),
            ]
        self.rt.add_tile_dma(TileDma(amt, amt_chans))

    def route(self, proj_send_tiles: list[list[Tile]]) -> dict[str, Flow | PacketFlow]:
        """Add every flow between the stages, long ones first.

        The router places them in the order the design adds them; returns
        the flows the runtime sequence fills and drains, by name.
        """
        rt, t = self.rt, self.t
        x_shim, kv_shim = t["x_shim"], t["kv_shim"]

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

        amt = t["attn_mem"]
        for name, ch, amt_ch, pkt in (
            ("move_k", 0, 0, _KV_PKT_GLOBAL),
            ("move_k_swa", 0, 2, _KV_PKT_SWA),
            ("move_v", 1, 1, _KV_PKT_GLOBAL),
            ("move_v_swa", 1, 3, _KV_PKT_SWA),
        ):
            shim[name] = _connect(rt, kv_shim, ch, amt, amt_ch, pkt_id=pkt, name=name)
        add("amt_attn_qk", "amt_attn_kv", "amt_swa_attn_qk", "amt_swa_attn_kv")
        add("pli_rope_rms", "pli_down", "ple_y", "pli_gate", "plg_y", "plm_y")
        add("pli_up", "recv_y")
        return shim | {
            name: flow
            for name, flow in self.flows.items()
            if any(tile.tile_type == _SHIM for tile in flow.all_tiles())
        }


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
    # Only this layer type's kv core may start: the other one would read this
    # dispatch's L, which differs from its own qk core's past the window.
    for stage in ("rms", "glu", "swa_attn_kv" if dims.swa else "attn_kv"):
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
        ],
    )
    array = _Array(rt, g, kernels)
    shim.update(array.build())
    rtps.update(array.rtps)
    sync_locks.update(array.sync_locks)
    return Program(dev, rt, workers=array.workers).resolve_program()
