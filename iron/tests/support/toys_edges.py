# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toy graphs, real IRON operators at small sizes, over the composition contract's edge axes."""

from __future__ import annotations

import dataclasses
import itertools
import math
from typing import Any, Mapping

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron.device import Device
from ml_dtypes import bfloat16

import iron
from iron import Precision, Scratchpad
from iron.common.declare import Profile
from iron.common.declare.composition import Member, Region
from iron.common.graph.record import Recording
from iron.common.image.step import BufferRef, Edge, EdgeKind, HandOff
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.sample import Sample
from iron.operators.selective_scan import SelectiveScan
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support.graphs import Trail

HELDS = ("l1", "memtile", "ddr", "later_phase")


def member(op: Any) -> Member:
    """Return the ``Member`` naming ``op``'s shape as ``candidates`` does: its dims collected as a profile entry's are, and no tunables."""
    return Member(type(op), Profile.dims(type(op), vars(op)))


def realize_helds(
    edges: tuple[Edge, ...], helds: Mapping[int, str]
) -> tuple[tuple[Edge, ...], tuple[tuple[int, ...], ...], tuple[int, ...] | None]:
    """Return ``edges`` with each named index's held place realized, plus the region's ``workers`` and ``phases``.

    ``helds`` maps an edge's index to where its value waits: ``"memtile"``
    (``kind=STAGED``), ``"ddr"`` (``kind=DDR``), ``"later_phase"`` (staged, and
    read a phase after the rest) or ``"l1"`` (its two steps share one worker,
    so no stream kind is needed between them). An index ``helds`` leaves out
    keeps its edge's given ``kind``. The region runs in one phase (``phases``
    None) unless an edge waits a phase: then its consumer reads in phase 1, as
    does every step downstream of it, and the rest in phase 0.
    """
    kinds = {
        "l1": EdgeKind.STREAM,
        "memtile": EdgeKind.STAGED,
        "ddr": EdgeKind.DDR,
        "later_phase": EdgeKind.STAGED,
    }
    new_edges = tuple(
        dataclasses.replace(e, kind=kinds[helds[i]]) if i in helds else e
        for i, e in enumerate(edges)
    )
    later = [helds.get(i) == "later_phase" for i in range(len(new_edges))]
    # A step reading a phase later runs then, and so does all it feeds.
    stepped: dict[int, int] = {}
    for i, e in sorted(enumerate(new_edges), key=lambda pair: pair[1].consumer):
        if e.producer == e.consumer:
            continue
        stepped[e.consumer] = max(
            stepped.get(e.consumer, 0), stepped.get(e.producer, 0), int(later[i])
        )
    phases = (
        tuple(stepped.get(e.consumer, 0) for e in new_edges) if any(later) else None
    )
    parent: dict[int, int] = {}

    def find(x: int) -> int:
        parent.setdefault(x, x)
        while parent[x] != x:
            x = parent[x]
        return x

    for i, e in enumerate(new_edges):
        find(e.producer)
        find(e.consumer)
        if helds.get(i) == "l1" and e.producer != e.consumer:
            ra, rb = find(e.producer), find(e.consumer)
            if ra != rb:
                parent[ra] = rb
    groups: dict[int, list[int]] = {}
    for step in parent:
        groups.setdefault(find(step), []).append(step)
    workers = tuple(sorted(tuple(sorted(g)) for g in groups.values() if len(g) > 1))
    return new_edges, workers, phases


# ---------------------------------------------------------------------------
# Stream window: chains and topologies.
# ---------------------------------------------------------------------------


def chain(cols=(1, 1, 1), size=256):
    """Add -> RMSNorm -> ElementwiseMul: a plain three-step chain, every hand-off equal lanes."""
    add_cols, norm_cols, mul_cols = cols
    add = ElementwiseAdd(size=size, num_aie_columns=add_cols, tile_size=size)
    norm = RMSNorm(rows=1, tile_size=size, num_aie_columns=norm_cols)
    mul = ElementwiseMul(
        size=size, num_aie_columns=mul_cols, tile_size=size // mul_cols
    )
    steps = sequences.steps(
        (add, "a", "b", "h"), (norm, "h", "n"), (mul, "n", "up", "out")
    )
    recording = Recording.of_steps("toy_chain", steps, ["a", "b", "up"], ["out"])
    region = Region(
        (member(add), member(norm), member(mul)),
        (Edge(0, "y", 1, "x"), Edge(1, "y", 2, "a")),
    )
    return recording, region


def fan_in_gate_up_mul(size=256):
    """Return the MLP's gate and up projections into one multiply, the stream window's fan-in."""
    gate = GEMV(M=size, K=size, num_aie_columns=1, num_channels=1)
    up = GEMV(M=size, K=size, num_aie_columns=1, num_channels=1)
    mul = ElementwiseMul(size=size, num_aie_columns=1, tile_size=size)
    steps = sequences.steps(
        (gate, "Wg", "x", "g"), (up, "Wu", "x", "u"), (mul, "g", "u", "out")
    )
    recording = Recording.of_steps("toy_fan_in", steps, ["Wg", "Wu", "x"], ["out"])
    region = Region(
        (member(gate), member(up), member(mul)),
        # The GEMVs' 2-element output objects restage into the multiply's 256.
        (
            Edge(0, "C", 2, "a", kind=EdgeKind.STAGED),
            Edge(1, "C", 2, "b", kind=EdgeKind.STAGED),
        ),
    )
    return recording, region


def fan_out_norm_qkv(columns=(1, 1, 1), size=256):
    """RMSNorm fanned into Q, K and V projections, the stream window's fan-out."""
    qc, kc, vc = columns
    norm = RMSNorm(rows=1, tile_size=size)
    q = GEMV(M=size, K=size, feed_b=True, num_aie_columns=qc)
    k = GEMV(M=size // 4, K=size, feed_b=True, num_aie_columns=kc)
    v = GEMV(M=size // 4, K=size, feed_b=True, num_aie_columns=vc)
    steps = sequences.steps(
        (norm, "x", "n"),
        (q, "Aq", "n", "oq"),
        (k, "Ak", "n", "ok"),
        (v, "Av", "n", "ov"),
    )
    recording = Recording.of_steps(
        "toy_fan_out", steps, ["x", "Aq", "Ak", "Av"], ["oq", "ok", "ov"]
    )
    region = Region(
        (member(norm), member(q), member(k), member(v)),
        (Edge(0, "y", 1, "B"), Edge(0, "y", 2, "B"), Edge(0, "y", 3, "B")),
    )
    return recording, region


def window_with_outside_reader(size=256):
    """Add -> RMSNorm -> GEMV -> Add: the first add's row is also the window's own second input and final residual.

    Covers an intermediate also read outside the window, plus the final
    output, and is the skip connection's toy once the skip edge's depth and
    held place are named (``skip_edge``).
    """
    add = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=size)
    norm = RMSNorm(rows=1, tile_size=size)
    proj = GEMV(M=size, K=size, feed_b=True, num_aie_columns=1)
    add2 = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=size)
    steps = sequences.steps(
        (add, "a", "b", "h"),
        (norm, "h", "n"),
        (proj, "W", "n", "g"),
        (add2, "g", "h", "out"),
    )
    recording = Recording.of_steps(
        "toy_outside_reader", steps, ["a", "b", "W"], ["out"]
    )
    # The projection's 2-element output objects restage into the add's 256.
    forward_edges = (
        Edge(0, "y", 1, "x"),
        Edge(1, "y", 2, "B"),
        Edge(2, "C", 3, "a", kind=EdgeKind.STAGED),
    )
    return (
        recording,
        (member(add), member(norm), member(proj), member(add2)),
        forward_edges,
    )


def skip_edge(depth: int | None = None) -> Edge:
    """Return the residual edge from ``window_with_outside_reader``'s add into its own last add.

    Names only the choice of depth; where its value waits (L1, a memtile, DDR
    or a later phase) is for a caller to realize structurally on the region
    holding it, with ``realize_helds``.
    """
    return Edge(0, "y", 3, "b", depth=depth)


def skip_add_gemv_add(size=256):
    """Add -> GEMV -> Add: the residual skip over one step, held on a broadcast edge.

    A skip edge held shallow enough to deadlock hangs the device; a skip
    held 4 deep runs where a 2-deep hold deadlocks.
    """
    add = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=size)
    proj = GEMV(M=size, K=size, feed_b=True, num_aie_columns=1)
    add2 = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=size)
    steps = sequences.steps(
        (add, "a", "b", "h"), (proj, "W", "h", "g"), (add2, "g", "h", "out")
    )
    recording = Recording.of_steps(
        "toy_skip_add_gemv_add", steps, ["a", "b", "W"], ["out"]
    )
    members = (member(add), member(proj), member(add2))
    forward = (Edge(0, "y", 1, "B"), Edge(1, "C", 2, "a"))
    return recording, members, forward


def skip_add_gemv_add_edge(depth: int | None = None) -> Edge:
    """Return the skip edge of ``skip_add_gemv_add``, from the first add into the second."""
    return Edge(0, "y", 2, "b", depth=depth)


def shared_input_two_reads(size=256):
    """One outside input, read twice by two independent members (no on-chip edge names it)."""
    add1 = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=size)
    add2 = ElementwiseMul(size=size, num_aie_columns=1, tile_size=size)
    steps = sequences.steps((add1, "x", "b1", "o1"), (add2, "x", "b2", "o2"))
    recording = Recording.of_steps(
        "toy_shared_input", steps, ["x", "b1", "b2"], ["o1", "o2"]
    )
    region = Region((member(add1), member(add2)), ())
    return recording, region


def scan_with_state_output(heads=2, head_dim=16, state_size=16):
    """SelectiveScan, an operator with two outputs (``y`` and ``final``), into a downstream multiply on ``y``."""
    scan = SelectiveScan(rows=2, heads=heads, head_dim=head_dim, state_size=state_size)
    size = scan.rows * heads * head_dim
    mul = ElementwiseMul(size=size, num_aie_columns=1, tile_size=size)
    steps = sequences.steps(
        (scan, "xbc", "head", "dt", "state", "y", "final"), (mul, "y", "up", "out")
    )
    recording = Recording.of_steps(
        "toy_scan_output", steps, ["xbc", "head", "dt", "state", "up"], ["final", "out"]
    )
    region = Region(
        (member(scan), member(mul)), (Edge(0, "y", 1, "a", kind=EdgeKind.STAGED),)
    )
    return recording, region


def diamond_qkv_merge(size=256):
    """RMSNorm fans into Q and K, which rejoin into an Add: a reconvergent diamond.

    Stands in for attention's head merge: no head-merge operator exists in
    ``iron.operators`` yet (MHA as a graph is not built), so the merge is a
    plain add of the two projections.
    """
    norm = RMSNorm(rows=1, tile_size=size)
    q = GEMV(M=size, K=size, feed_b=True, num_aie_columns=1)
    k = GEMV(M=size, K=size, feed_b=True, num_aie_columns=1)
    merge = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=size)
    steps = sequences.steps(
        (norm, "x", "n"),
        (q, "Aq", "n", "oq"),
        (k, "Ak", "n", "ok"),
        (merge, "oq", "ok", "out"),
    )
    recording = Recording.of_steps("toy_diamond", steps, ["x", "Aq", "Ak"], ["out"])
    region = Region(
        (member(norm), member(q), member(k), member(merge)),
        (
            Edge(0, "y", 1, "B"),
            Edge(0, "y", 2, "B"),
            # The projections' 2-element output objects restage into the add's.
            Edge(1, "C", 3, "a", kind=EdgeKind.STAGED),
            Edge(2, "C", 3, "b", kind=EdgeKind.STAGED),
        ),
    )
    return recording, region


def wide_mlp_window(dev: Device):
    """Return a gate/up/SiLU/multiply window at the widest tunables ``dev`` takes, an over-budget window.

    At Llama decode's recorded widths this window demands 40 cores, 24
    shim-in and 8 shim-out channels, and fits npu2 only at 4 columns; this
    toy keeps the same shape (gate, up, SiLU, multiply), each member at
    every column, the GEMVs at two channels a column, so its members take
    six cores a column, more than a column has (48 of npu2's 32).
    """
    gc = uc = sc = mc = dev.cols
    gate = GEMV(M=2048, K=2048, num_aie_columns=gc, num_channels=2)
    up = GEMV(M=2048, K=2048, num_aie_columns=uc, num_channels=2)
    silu = SiLU(size=2048, num_aie_columns=sc, tile_size=256)
    mul = ElementwiseMul(size=2048, num_aie_columns=mc, tile_size=256)
    steps = sequences.steps(
        (gate, "Wg", "x", "g"),
        (up, "Wu", "x", "u"),
        (silu, "g", "s"),
        (mul, "s", "u", "out"),
    )
    recording = Recording.of_steps("toy_wide_window", steps, ["Wg", "Wu", "x"], ["out"])
    region = Region(
        (member(gate), member(up), member(silu), member(mul)),
        (Edge(0, "C", 2, "x"), Edge(1, "C", 3, "b"), Edge(2, "y", 3, "a")),
    )
    return recording, region


# ---------------------------------------------------------------------------
# Dependences through memory: a KV-style write then read, ordered by the
# recording's shared buffer, which the dataflow analysis is to derive (no
# ``Region`` field names it).
# ---------------------------------------------------------------------------


def kv_write_then_read(position: int, table_rows: int = 8, row: int = 8):
    """Return a write of row ``position`` into a cache, then a read of its first ``n`` rows, sharing that cache buffer.

    Both are ``Copy``: the write puts one row at ``position``, and the read,
    bounded per call, gathers the rows written so far (``n`` is
    ``position + 1`` in a decode).
    """
    cache = iron.state((table_rows, row), np.int32, name="cache")

    class _KV(iron.Graph):
        def body(self, new_row, *, n: Scratchpad[np.int32]):
            Copy.step(new_row, cache[position : position + 1], dtype=np.int32)
            return Copy.step(cache[:n], dtype=np.int32)

    recording = dataclasses.replace(
        _KV().record(new_row=((1, row), np.int32)), name="toy_kv_write_read"
    )
    return recording, tuple(member(s.op) for s in recording.steps)


def interleaved_kv_write(position: int, table_rows: int = 8, row: int = 8):
    """Two writers (K and V) of one cache at interleaved elements: each writes every other row."""
    k_write = Copy(
        input_buffer_size=row,
        src=TensorAccessPattern((row,), 0, [1, 1, 1, row], [0, 0, 0, 1]),
        output_buffer_size=table_rows * row,
        dst=TensorAccessPattern(
            (table_rows * row,), 2 * position * row, [1, 1, 1, row], [0, 0, 0, 1]
        ),
        dtype=np.int32,
    )
    v_write = Copy(
        input_buffer_size=row,
        src=TensorAccessPattern((row,), 0, [1, 1, 1, row], [0, 0, 0, 1]),
        output_buffer_size=table_rows * row,
        dst=TensorAccessPattern(
            (table_rows * row,), (2 * position + 1) * row, [1, 1, 1, row], [0, 0, 0, 1]
        ),
        dtype=np.int32,
    )
    steps = sequences.steps((k_write, "k_row", "cache"), (v_write, "v_row", "cache"))
    recording = Recording.of_steps(
        "toy_interleaved_write", steps, ["k_row", "v_row", "cache"], ["cache"]
    )
    return recording, (member(k_write), member(v_write))


# ---------------------------------------------------------------------------
# Feedback loops: cycles carried by initial values, within and across calls.
# ---------------------------------------------------------------------------


def scan_state_cycle(heads=2, head_dim=16, state_size=16):
    """Return a running state updated every firing within a call: ``SelectiveScan``'s own recurrence, named as a self-loop edge.

    Its state is both the scan's own input and output, so the edge's
    ``producer`` and ``consumer`` are the same part; the initial tokens on it
    are the recording's and the operator's own, which the dataflow analysis
    derives.
    """
    scan = SelectiveScan(rows=4, heads=heads, head_dim=head_dim, state_size=state_size)
    size = scan.rows * heads * head_dim
    mul = ElementwiseMul(size=size, num_aie_columns=1, tile_size=size)
    steps = sequences.steps(
        (scan, "xbc", "head", "dt", "state", "y", "state"), (mul, "y", "up", "out")
    )
    recording = Recording.of_steps(
        "toy_scan_cycle",
        steps,
        ["xbc", "head", "dt", "up"],
        ["out"],
        feedback=["state"],
    )
    members = (member(scan), member(mul))
    cycle = Edge(0, "final", 0, "state")
    # The scan's lanes join into the multiply's one, through a memtile.
    forward = (Edge(0, "y", 1, "a", kind=EdgeKind.STAGED),)
    return recording, members, forward, cycle


def sample_token_cycle(size=256, vocab=256):
    """Return a projection into ``Sample``, the drawn token fed back as the next call's record: the token across decode steps.

    ``Sample``'s own ``tokens``/``token`` is the cross-call carry; the edge's
    ``producer`` and ``consumer`` are again the same part.
    """
    proj = GEMV(M=vocab, K=size, feed_b=True, num_aie_columns=1)
    sample = Sample(vocab=vocab, k_max=4, cores=1)
    steps = sequences.steps(
        (proj, "A", "x", "logits"), (sample, "logits", "draws", "tokens", "token")
    )
    recording = Recording.of_steps(
        "toy_sample_cycle", steps, ["A", "x", "draws"], ["tokens", "token"]
    )
    members = (member(proj), member(sample))
    cycle = Edge(1, "token", 1, "tokens")
    forward = (Edge(0, "C", 1, "logits"),)
    return recording, members, forward, cycle


def cross_call_trail(successor_len=8, steps=4):
    """``Trail``'s body version: a node gathered and recorded each call, the next call's node and step count its own carry.

    No ``Region``/``Edge`` field names this cycle: ``Trail`` threads it
    through ``iron.carry``, a graph-level mechanism outside the Region's
    parts and edges (a gap the report calls out).
    """
    successor = np.random.default_rng(0).permutation(successor_len).astype(np.int32)
    trail = Trail(successor, steps)
    recording = trail.record()
    region = Region(tuple(member(s.op) for s in recording.steps))
    return recording, region


# ---------------------------------------------------------------------------
# Hand-off shapes: both directions over the stream window's chains. Each
# toy realizes its named ``HandOff`` with real lane counts; the dataflow
# analysis is what derives that the hand-off is this shape, never the toy.
# ---------------------------------------------------------------------------


def join_in_pairs(dev: Device, size=2048):
    """ElementwiseAdd at every column of ``dev`` joined in pairs into RMSNorm at half of them (8 into 4 on npu2): realizes ``HandOff.JOIN``."""
    add = ElementwiseAdd(size=dev.cols * size, num_aie_columns=dev.cols, tile_size=size)
    norm = RMSNorm(rows=dev.cols, tile_size=size, num_aie_columns=dev.cols // 2)
    steps = sequences.steps((add, "a", "b", "mid"), (norm, "mid", "out"))
    recording = Recording.of_steps("toy_join", steps, ["a", "b"], ["out"])
    region = Region(
        (member(add), member(norm)), (Edge(0, "y", 1, "x", kind=EdgeKind.STAGED),)
    )
    return recording, region


def split_in_two(dev: Device, size=2048):
    """GEMV at half of ``dev``'s columns, each lane split in two into SiLU at all: realizes ``HandOff.SPLIT`` (npu2's 4 -> 8 split once hung)."""
    gemv = GEMV(M=size, K=size, num_aie_columns=dev.cols // 2, feed_b=True)
    silu = SiLU(size=size, num_aie_columns=dev.cols, tile_size=size // dev.cols)
    steps = sequences.steps((gemv, "A", "B", "mid"), (silu, "mid", "out"))
    recording = Recording.of_steps("toy_split", steps, ["A", "B"], ["out"])
    region = Region(
        (member(gemv), member(silu)), (Edge(0, "C", 1, "x", kind=EdgeKind.STAGED),)
    )
    return recording, region


def broadcast_weight_to_columns(dev: Device, size=2048):
    """One vector read by every column of a GEMV at half of ``dev``'s columns: realizes ``HandOff.BROADCAST``."""
    add = ElementwiseAdd(size=size, num_aie_columns=1, tile_size=size)
    gemv = GEMV(M=size, K=size, num_aie_columns=dev.cols // 2, feed_b=True)
    steps = sequences.steps((add, "a", "b", "mid"), (gemv, "A", "mid", "out"))
    recording = Recording.of_steps("toy_broadcast", steps, ["a", "b", "A"], ["out"])
    region = Region((member(add), member(gemv)), (Edge(0, "y", 1, "B"),))
    return recording, region


def slices_qkv(size=2048):
    """One GEMV computing ``[q|k|v]`` into one buffer, each third read by its own consumer: realizes ``HandOff.SLICES``."""
    qkv = GEMV(M=3 * size, K=size, num_aie_columns=1, feed_b=True)
    third = size * np.dtype(bfloat16).itemsize
    readers = [SiLU(size=size, num_aie_columns=1) for _ in range(3)]
    steps = sequences.steps(
        (qkv, "A", "x", "qkv"),
        *(
            (silu, BufferRef("qkv", k * third, third), name)
            for k, (silu, name) in enumerate(zip(readers, ("q", "k", "v")))
        ),
    )
    recording = Recording.of_steps("toy_slices", steps, ["A", "x"], ["q", "k", "v"])
    region = Region(
        tuple(member(s.op) for s in recording.steps),
        tuple(Edge(0, "C", k, "x") for k in (1, 2, 3)),
    )
    return recording, region


def ratio_two_into_three(dev: Device, size=288):
    """GEMV at half of ``dev``'s columns into a multiply at three quarters (4 into 6 on npu2): realizes ``HandOff.RATIO``.

    A consumer lane takes parts of two producer lanes.
    """
    producers, consumers = lane_counts(HandOff.RATIO, dev.cols)
    gemv = GEMV(M=size, K=size, num_aie_columns=producers, feed_b=True)
    mul = ElementwiseMul(
        size=size, num_aie_columns=consumers, tile_size=size // consumers
    )
    steps = sequences.steps((gemv, "A", "B", "mid"), (mul, "mid", "up", "out"))
    recording = Recording.of_steps("toy_ratio", steps, ["A", "B", "up"], ["out"])
    region = Region(
        (member(gemv), member(mul)), (Edge(0, "C", 1, "a", kind=EdgeKind.STAGED),)
    )
    return recording, region


def ratio_three_into_two(dev: Device, size=288):
    """Return the reverse of ``ratio_two_into_three``: a multiply at three quarters of ``dev``'s columns into an add at half.

    Each of the add's lanes takes parts of two of the multiply's.
    """
    consumers, producers = lane_counts(HandOff.RATIO, dev.cols)
    mul = ElementwiseMul(
        size=size, num_aie_columns=producers, tile_size=size // producers
    )
    add = ElementwiseAdd(
        size=size, num_aie_columns=consumers, tile_size=size // consumers
    )
    steps = sequences.steps((mul, "a", "b", "mid"), (add, "mid", "c", "out"))
    recording = Recording.of_steps("toy_ratio_reverse", steps, ["a", "b", "c"], ["out"])
    region = Region(
        tuple(member(s.op) for s in recording.steps),
        (Edge(0, "y", 1, "a", kind=EdgeKind.STAGED),),
    )
    return recording, region


def layout_transpose(rows=64, cols=128, tile=32):
    """GEMM's ``tile`` x ``tile`` output tiles read by RMSNorm as whole rows: realizes ``HandOff.LAYOUT``.

    A tile narrower than a row is not a run of whole rows, so the rows a
    norm reads need the tiles' elements reordered on the way.
    """
    gemm = GEMM(
        M=rows,
        K=rows,
        N=cols,
        precision=Precision.MEDIUM,
        num_aie_columns=1,
        tile_m=tile,
        tile_n=tile,
    )
    norm = RMSNorm(rows=rows, tile_size=cols, num_aie_columns=1)
    steps = sequences.steps((gemm, "A", "B", "mid"), (norm, "mid", "out"))
    recording = Recording.of_steps("toy_layout", steps, ["A", "B"], ["out"])
    region = Region(
        tuple(member(s.op) for s in recording.steps),
        (Edge(0, "C", 1, "x", kind=EdgeKind.STAGED),),
    )
    return recording, region


# ---------------------------------------------------------------------------
# Combinations: one builder over the edge axes.
# ---------------------------------------------------------------------------

SHAPES = (
    HandOff.EQUAL,
    HandOff.JOIN,
    HandOff.SPLIT,
    HandOff.RATIO,
    HandOff.BROADCAST,
    HandOff.SLICES,
    HandOff.LAYOUT,
)
ROLES = (
    "chain",
    "fan_out",
    "fan_in",
    "skip",
    "diamond",
    "through_memory",
    "feedback",
)
DEPTHS = ("min_minus_one", "min", "knee", "more")
RATES = ("same", "different")
SIZES = ("recorded", "smaller")

_EDGE_SIZE = 1536


def lane_counts(shape: HandOff, columns: int) -> tuple[int, int]:
    """Return the (producer, consumer) lane counts standing in for ``shape`` on an array ``columns`` wide.

    A plain count ratio stands in for the shape's real routing pattern
    (BROADCAST, SLICES and LAYOUT are really about which elements a lane
    reads, not how many); the full, per-pattern realization of every shape
    is ``test_tuning_hand_off_shapes.py``'s job, one toy per shape with no
    role or held place crossed in. A join and a split span the array; a
    ratio is half its columns against three quarters (4 and 6 on npu2, 2 and
    3 on npu1).
    """
    half = columns // 2
    return {
        HandOff.EQUAL: (2, 2),
        HandOff.JOIN: (columns, 2),
        HandOff.SPLIT: (2, columns),
        HandOff.RATIO: (half, half + half // 2),
        HandOff.BROADCAST: (1, 4),
        HandOff.SLICES: (1, 3),
        HandOff.LAYOUT: (4, 1),
    }[shape]


def _next(values: tuple, value) -> Any:
    """Return the value after ``value`` in ``values``, cyclically (never ``value`` itself)."""
    return values[(values.index(value) + 1) % len(values)]


def min_depth(rate_pair: tuple[int, int]) -> int:
    """Return the minimum deadlock-free depth of an edge at ``rate_pair``: ``p + c - gcd(p, c)``."""
    p, c = rate_pair
    return p + c - math.gcd(p, c)


def depth_from_bounds(depth: str, minimum: int, knee: int) -> int:
    """Return the depth ``depth`` (min−1, min, knee or more) names, given ``minimum`` and ``knee``."""
    return {
        "min_minus_one": minimum - 1,
        "min": minimum,
        "knee": knee,
        "more": knee + 1,
    }[depth]


def with_resolved_depth(region: Region, index: int, depth: int) -> Region:
    """Return ``region`` with its edge at ``index`` set to the concrete depth ``depth``.

    Used once a test has resolved a combination toy's symbolic depth name
    (min−1, min, knee, more) against ``iron.common.graph.sdf.analyze``'s real
    ``min_depth``/``knee_depth`` for that edge.
    """
    edges = tuple(
        e if i != index else Edge(**{**vars(e), "depth": depth})
        for i, e in enumerate(region.edges)
    )
    return Region(
        region.parts,
        edges,
        region.inflows,
        region.workers,
        region.phases,
        region.runtime,
    )


def _chain_combo(lanes, held, rate, bounded):
    """Add -> RMSNorm -> ElementwiseMul, the distinguished edge Add -> RMSNorm."""
    p_cols, c_cols = lanes
    mult = 2 if rate == "different" else 1
    add = ElementwiseAdd(
        size=_EDGE_SIZE, num_aie_columns=p_cols, tile_size=_EDGE_SIZE // (p_cols * mult)
    )
    norm = RMSNorm(rows=c_cols, tile_size=_EDGE_SIZE // c_cols, num_aie_columns=c_cols)
    mul = ElementwiseMul(size=_EDGE_SIZE, num_aie_columns=1, tile_size=_EDGE_SIZE)
    if bounded:
        recording = _chain_bounded_recording(add, norm, mul)
    else:
        steps = sequences.steps(
            (add, "a", "b", "h"), (norm, "h", "n"), (mul, "n", "up", "out")
        )
        recording = Recording.of_steps("combo_chain", steps, ["a", "b", "up"], ["out"])
    edges = (Edge(0, "y", 1, "x"), Edge(1, "y", 2, "a"))
    edges, workers, phases = realize_helds(edges, {0: held, 1: _next(HELDS, held)})
    region = Region(
        (member(add), member(norm), member(mul)), edges, workers=workers, phases=phases
    )
    return recording, region, 0


def _chain_bounded_recording(
    add: ElementwiseAdd, norm: RMSNorm, mul: ElementwiseMul
) -> Recording:
    """Return ``add``, ``norm``, ``mul`` wired as ``_chain_combo`` does, the multiply's ``up`` bound per call to ``n``."""

    class _Chain(iron.Graph):
        def body(self, a, b, up, *, n: Scratchpad[np.int32]):
            h = ElementwiseAdd.step(
                a,
                b,
                size=add.size,
                num_aie_columns=add.num_aie_columns,
                tile_size=add.tile_size,
            )
            normed = RMSNorm.step(
                h.reshape(norm.rows, norm.tile_size),
                rows=norm.rows,
                tile_size=norm.tile_size,
                num_aie_columns=norm.num_aie_columns,
            )
            return ElementwiseMul.step(
                normed.reshape(mul.size),
                up[:n],
                size=mul.size,
                num_aie_columns=mul.num_aie_columns,
                tile_size=mul.tile_size,
            )

    recording = _Chain().record(a=(add.size,), b=(add.size,), up=(mul.size,))
    return dataclasses.replace(recording, name="combo_chain_bounded")


def _fan_out_combo(lanes, held, rate, bounded):
    """RMSNorm fanned into Q, K and V, then a tail add on Q's lane; the distinguished edge is the one into Q."""
    p_cols, c_cols = lanes
    mult = 2 if rate == "different" else 1
    norm = RMSNorm(rows=p_cols, tile_size=_EDGE_SIZE // p_cols, num_aie_columns=p_cols)
    q = GEMV(
        M=_EDGE_SIZE,
        K=_EDGE_SIZE,
        feed_b=True,
        num_aie_columns=c_cols,
        tile_size_output=_EDGE_SIZE // (c_cols * mult),
    )
    k = GEMV(M=_EDGE_SIZE // 4, K=_EDGE_SIZE, feed_b=True, num_aie_columns=1)
    v = GEMV(M=_EDGE_SIZE // 4, K=_EDGE_SIZE, feed_b=True, num_aie_columns=1)
    tail = ElementwiseAdd(size=_EDGE_SIZE, num_aie_columns=1, tile_size=_EDGE_SIZE)
    if bounded:
        recording = _fan_out_bounded_recording(norm, q, k, v, tail)
    else:
        steps = sequences.steps(
            (norm, "x", "n"),
            (q, "Aq", "n", "oq"),
            (k, "Ak", "n", "ok"),
            (v, "Av", "n", "ov"),
            (tail, "oq", "tail_in", "tailed"),
        )
        recording = Recording.of_steps(
            "combo_fan_out",
            steps,
            ["x", "Aq", "Ak", "Av", "tail_in"],
            ["tailed", "ok", "ov"],
        )
    edges = (
        Edge(0, "y", 1, "B"),
        Edge(0, "y", 2, "B"),
        Edge(0, "y", 3, "B"),
        Edge(1, "C", 4, "a"),
    )
    other = _next(HELDS, held)
    edges, workers, phases = realize_helds(
        edges, {0: held, 1: other, 2: other, 3: other}
    )
    region = Region(
        (member(norm), member(q), member(k), member(v), member(tail)),
        edges,
        workers=workers,
        phases=phases,
    )
    return recording, region, 0


def _fan_out_bounded_recording(
    norm: RMSNorm, q: GEMV, k: GEMV, v: GEMV, tail: ElementwiseAdd
) -> Recording:
    """Return ``norm``, ``q``, ``k``, ``v`` and ``tail`` wired as ``_fan_out_combo`` does, the tail's ``tail_in`` bound per call to ``n``."""

    class _FanOut(iron.Graph):
        def body(self, x, aq, ak, av, tail_in, *, n: Scratchpad[np.int32]):
            normed = RMSNorm.step(
                x,
                rows=norm.rows,
                tile_size=norm.tile_size,
                num_aie_columns=norm.num_aie_columns,
            ).reshape(q.K)
            oq = GEMV.step(
                aq,
                normed,
                M=q.M,
                K=q.K,
                feed_b=True,
                num_aie_columns=q.num_aie_columns,
                tile_size_output=q.tile_size_output,
            )
            ok = GEMV.step(
                ak, normed, M=k.M, K=k.K, feed_b=True, num_aie_columns=k.num_aie_columns
            )
            ov = GEMV.step(
                av, normed, M=v.M, K=v.K, feed_b=True, num_aie_columns=v.num_aie_columns
            )
            tailed = ElementwiseAdd.step(
                oq,
                tail_in[:n],
                size=tail.size,
                num_aie_columns=tail.num_aie_columns,
                tile_size=tail.tile_size,
            )
            return tailed, ok, ov

    recording = _FanOut().record(
        x=(norm.rows, norm.tile_size),
        aq=(q.M, q.K),
        ak=(k.M, k.K),
        av=(v.M, v.K),
        tail_in=(tail.size,),
    )
    return dataclasses.replace(recording, name="combo_fan_out_bounded")


def _fan_in_combo(lanes, held, rate, bounded):
    """Gate and up projections into one multiply, then a tail add; the distinguished edge is gate -> multiply."""
    p_cols, c_cols = lanes
    mult = 2 if rate == "different" else 1
    gate = GEMV(
        M=_EDGE_SIZE,
        K=_EDGE_SIZE,
        num_aie_columns=p_cols,
        num_channels=1,
        tile_size_output=_EDGE_SIZE // (p_cols * mult),
    )
    up = GEMV(M=_EDGE_SIZE, K=_EDGE_SIZE, num_aie_columns=1, num_channels=1)
    mul = ElementwiseMul(
        size=_EDGE_SIZE, num_aie_columns=c_cols, tile_size=_EDGE_SIZE // c_cols
    )
    tail = ElementwiseAdd(size=_EDGE_SIZE, num_aie_columns=1, tile_size=_EDGE_SIZE)
    if bounded:
        recording = _fan_in_bounded_recording(gate, up, mul, tail)
    else:
        steps = sequences.steps(
            (gate, "Wg", "x", "g"),
            (up, "Wu", "x", "u"),
            (mul, "g", "u", "m"),
            (tail, "m", "tail_in", "out"),
        )
        recording = Recording.of_steps(
            "combo_fan_in", steps, ["Wg", "Wu", "x", "tail_in"], ["out"]
        )
    edges = (Edge(0, "C", 2, "a"), Edge(1, "C", 2, "b"), Edge(2, "y", 3, "a"))
    other = _next(HELDS, held)
    edges, workers, phases = realize_helds(edges, {0: held, 1: other, 2: other})
    region = Region(
        (member(gate), member(up), member(mul), member(tail)),
        edges,
        workers=workers,
        phases=phases,
    )
    return recording, region, 0


def _fan_in_bounded_recording(
    gate: GEMV, up: GEMV, mul: ElementwiseMul, tail: ElementwiseAdd
) -> Recording:
    """Return ``gate``, ``up``, ``mul`` and ``tail`` wired as ``_fan_in_combo`` does, the tail's ``tail_in`` bound per call to ``n``."""

    class _FanIn(iron.Graph):
        def body(self, wg, wu, x, tail_in, *, n: Scratchpad[np.int32]):
            g = GEMV.step(
                wg,
                x,
                M=gate.M,
                K=gate.K,
                num_aie_columns=gate.num_aie_columns,
                num_channels=gate.num_channels,
                tile_size_output=gate.tile_size_output,
            )
            u = GEMV.step(
                wu,
                x,
                M=up.M,
                K=up.K,
                num_aie_columns=up.num_aie_columns,
                num_channels=up.num_channels,
            )
            m = ElementwiseMul.step(
                g,
                u,
                size=mul.size,
                num_aie_columns=mul.num_aie_columns,
                tile_size=mul.tile_size,
            )
            return ElementwiseAdd.step(
                m,
                tail_in[:n],
                size=tail.size,
                num_aie_columns=tail.num_aie_columns,
                tile_size=tail.tile_size,
            )

    recording = _FanIn().record(
        wg=(gate.M, gate.K), wu=(up.M, up.K), x=(gate.K,), tail_in=(tail.size,)
    )
    return dataclasses.replace(recording, name="combo_fan_in_bounded")


def _skip_combo(lanes, held, rate, bounded):
    """Add -> RMSNorm -> GEMV -> Add -> tail add, the distinguished edge the residual skip into the second add."""
    p_cols, c_cols = lanes
    mult = 2 if rate == "different" else 1
    add = ElementwiseAdd(
        size=_EDGE_SIZE, num_aie_columns=p_cols, tile_size=_EDGE_SIZE // (p_cols * mult)
    )
    norm = RMSNorm(rows=1, tile_size=_EDGE_SIZE, num_aie_columns=1)
    proj = GEMV(M=_EDGE_SIZE, K=_EDGE_SIZE, feed_b=True, num_aie_columns=1)
    add2 = ElementwiseAdd(
        size=_EDGE_SIZE, num_aie_columns=c_cols, tile_size=_EDGE_SIZE // c_cols
    )
    tail = ElementwiseAdd(size=_EDGE_SIZE, num_aie_columns=1, tile_size=_EDGE_SIZE)
    if bounded:
        recording = _skip_bounded_recording(add, norm, proj, add2, tail)
    else:
        steps = sequences.steps(
            (add, "a", "b", "h"),
            (norm, "h", "n"),
            (proj, "W", "n", "g"),
            (add2, "g", "h", "s"),
            (tail, "s", "tail_in", "out"),
        )
        recording = Recording.of_steps(
            "combo_skip", steps, ["a", "b", "W", "tail_in"], ["out"]
        )
    forward = (Edge(0, "y", 1, "x"), Edge(1, "y", 2, "B"), Edge(2, "C", 3, "a"))
    skip = Edge(0, "y", 3, "b")
    tail_edge = Edge(3, "y", 4, "a")
    other = _next(HELDS, held)
    edges = forward + (skip, tail_edge)
    edges, workers, phases = realize_helds(
        edges, {0: other, 1: other, 2: other, 3: held, 4: other}
    )
    region = Region(
        (member(add), member(norm), member(proj), member(add2), member(tail)),
        edges,
        workers=workers,
        phases=phases,
    )
    return recording, region, 3


def _skip_bounded_recording(
    add: ElementwiseAdd,
    norm: RMSNorm,
    proj: GEMV,
    add2: ElementwiseAdd,
    tail: ElementwiseAdd,
) -> Recording:
    """Return ``add``, ``norm``, ``proj``, ``add2`` and ``tail`` wired as ``_skip_combo`` does, the tail's ``tail_in`` bound per call to ``n``."""

    class _Skip(iron.Graph):
        def body(self, a, b, w, tail_in, *, n: Scratchpad[np.int32]):
            h = ElementwiseAdd.step(
                a,
                b,
                size=add.size,
                num_aie_columns=add.num_aie_columns,
                tile_size=add.tile_size,
            )
            normed = RMSNorm.step(
                h.reshape(norm.rows, norm.tile_size),
                rows=norm.rows,
                tile_size=norm.tile_size,
                num_aie_columns=norm.num_aie_columns,
            )
            g = GEMV.step(
                w,
                normed.reshape(proj.K),
                M=proj.M,
                K=proj.K,
                feed_b=True,
                num_aie_columns=proj.num_aie_columns,
            )
            s = ElementwiseAdd.step(
                g,
                h,
                size=add2.size,
                num_aie_columns=add2.num_aie_columns,
                tile_size=add2.tile_size,
            )
            return ElementwiseAdd.step(
                s,
                tail_in[:n],
                size=tail.size,
                num_aie_columns=tail.num_aie_columns,
                tile_size=tail.tile_size,
            )

    recording = _Skip().record(
        a=(add.size,), b=(add.size,), w=(proj.M, proj.K), tail_in=(tail.size,)
    )
    return dataclasses.replace(recording, name="combo_skip_bounded")


def _diamond_combo(lanes, held, rate, bounded):
    """RMSNorm fans into Q and K, rejoining into an Add, then a tail add; the distinguished edge is Q -> the merge."""
    p_cols, c_cols = lanes
    mult = 2 if rate == "different" else 1
    norm = RMSNorm(rows=1, tile_size=_EDGE_SIZE, num_aie_columns=1)
    q = GEMV(
        M=_EDGE_SIZE,
        K=_EDGE_SIZE,
        feed_b=True,
        num_aie_columns=p_cols,
        tile_size_output=_EDGE_SIZE // (p_cols * mult),
    )
    k = GEMV(M=_EDGE_SIZE, K=_EDGE_SIZE, feed_b=True, num_aie_columns=1)
    merge = ElementwiseAdd(
        size=_EDGE_SIZE, num_aie_columns=c_cols, tile_size=_EDGE_SIZE // c_cols
    )
    tail = ElementwiseAdd(size=_EDGE_SIZE, num_aie_columns=1, tile_size=_EDGE_SIZE)
    if bounded:
        recording = _diamond_bounded_recording(norm, q, k, merge, tail)
    else:
        steps = sequences.steps(
            (norm, "x", "n"),
            (q, "Aq", "n", "oq"),
            (k, "Ak", "n", "ok"),
            (merge, "oq", "ok", "m"),
            (tail, "m", "tail_in", "out"),
        )
        recording = Recording.of_steps(
            "combo_diamond", steps, ["x", "Aq", "Ak", "tail_in"], ["out"]
        )
    edges = (
        Edge(0, "y", 1, "B"),
        Edge(0, "y", 2, "B"),
        Edge(1, "C", 3, "a"),
        Edge(2, "C", 3, "b"),
        Edge(3, "y", 4, "a"),
    )
    other = _next(HELDS, held)
    edges, workers, phases = realize_helds(
        edges, {0: other, 1: other, 2: held, 3: other, 4: other}
    )
    region = Region(
        (member(norm), member(q), member(k), member(merge), member(tail)),
        edges,
        workers=workers,
        phases=phases,
    )
    return recording, region, 2


def _diamond_bounded_recording(
    norm: RMSNorm, q: GEMV, k: GEMV, merge: ElementwiseAdd, tail: ElementwiseAdd
) -> Recording:
    """Return ``norm``, ``q``, ``k``, ``merge`` and ``tail`` wired as ``_diamond_combo`` does, the tail's ``tail_in`` bound per call to ``n``."""

    class _Diamond(iron.Graph):
        def body(self, x, aq, ak, tail_in, *, n: Scratchpad[np.int32]):
            normed = RMSNorm.step(
                x,
                rows=norm.rows,
                tile_size=norm.tile_size,
                num_aie_columns=norm.num_aie_columns,
            ).reshape(q.K)
            oq = GEMV.step(
                aq,
                normed,
                M=q.M,
                K=q.K,
                feed_b=True,
                num_aie_columns=q.num_aie_columns,
                tile_size_output=q.tile_size_output,
            )
            ok = GEMV.step(
                ak, normed, M=k.M, K=k.K, feed_b=True, num_aie_columns=k.num_aie_columns
            )
            m = ElementwiseAdd.step(
                oq,
                ok,
                size=merge.size,
                num_aie_columns=merge.num_aie_columns,
                tile_size=merge.tile_size,
            )
            return ElementwiseAdd.step(
                m,
                tail_in[:n],
                size=tail.size,
                num_aie_columns=tail.num_aie_columns,
                tile_size=tail.tile_size,
            )

    recording = _Diamond().record(
        x=(norm.rows, norm.tile_size),
        aq=(q.M, q.K),
        ak=(k.M, k.K),
        tail_in=(tail.size,),
    )
    return dataclasses.replace(recording, name="combo_diamond_bounded")


def _through_memory_combo(lanes, held, rate, bounded):
    """Return a producer streaming into a cache write, the write ordered before a read, the read feeding a consumer.

    The distinguished edge is the producer -> write edge; the write -> read
    dependence (through the shared cache buffer, no edge) is left for the
    dataflow analysis to derive from the recording. ``lanes`` is realized as
    a channel-count pair; ``rate`` as the producer's per-transfer tile (a
    mover's own firing granularity), half as wide so it transfers twice.
    """
    p_cols, c_cols = lanes
    mult = 2 if rate == "different" else 1
    producer = Copy(
        input_buffer_size=_EDGE_SIZE,
        dtype=np.int32,
        num_channels=p_cols,
        tile_size=_EDGE_SIZE // (p_cols * mult),
    )
    write = Copy(input_buffer_size=_EDGE_SIZE, dtype=np.int32)
    read = Copy(input_buffer_size=_EDGE_SIZE, dtype=np.int32)
    consumer = Copy(input_buffer_size=_EDGE_SIZE, dtype=np.int32, num_channels=c_cols)
    if bounded:
        recording = _through_memory_bounded_recording(producer, write, read, consumer)
    else:
        steps = sequences.steps(
            (producer, "src", "pre"),
            (write, "pre", "cache"),
            (read, "cache", "post"),
            (consumer, "post", "out"),
        )
        recording = Recording.of_steps("combo_through_memory", steps, ["src"], ["out"])
    edges = (Edge(0, "y", 1, "x"), Edge(2, "y", 3, "x"))
    edges, workers, phases = realize_helds(edges, {0: held, 1: _next(HELDS, held)})
    region = Region(
        tuple(member(s.op) for s in recording.steps),
        edges,
        workers=workers,
        phases=phases,
    )
    return recording, region, 0


def _through_memory_bounded_recording(
    producer: Copy, write: Copy, read: Copy, consumer: Copy
) -> Recording:
    """Return ``producer``, ``write``, ``read`` and ``consumer`` wired as ``_through_memory_combo`` does, the cache write bound per call to ``n``."""

    class _ThroughMemory(iron.Graph):
        def body(self, src, *, n: Scratchpad[np.int32]):
            pre = Copy.step(
                src,
                input_buffer_size=producer.input_buffer_size,
                dtype=producer.dtype,
                num_channels=producer.num_channels,
            )
            # The bound sits on the one-channel write, over rows of eight: a
            # copy split over several channels cannot bound the axis it
            # splits, and a per-call length counts whole 16-byte units.
            cache = Copy.step(
                pre.reshape(write.input_buffer_size // 8, 8)[:n],
                input_buffer_size=write.input_buffer_size,
                dtype=write.dtype,
            )
            post = Copy.step(
                cache, input_buffer_size=read.input_buffer_size, dtype=read.dtype
            )
            return Copy.step(
                post,
                input_buffer_size=consumer.input_buffer_size,
                dtype=consumer.dtype,
                num_channels=consumer.num_channels,
            )

    recording = _ThroughMemory().record(
        src=((producer.input_buffer_size,), producer.dtype)
    )
    return dataclasses.replace(recording, name="combo_through_memory_bounded")


def _feedback_combo(lanes, held, rate, bounded):
    """Return a carried accumulator (``acc = acc + x``) into a multiply; the distinguished edge is the accumulator's own self-loop."""
    p_cols, c_cols = lanes
    mult = 2 if rate == "different" else 1
    add = ElementwiseAdd(
        size=_EDGE_SIZE, num_aie_columns=p_cols, tile_size=_EDGE_SIZE // (p_cols * mult)
    )
    mul = ElementwiseMul(
        size=_EDGE_SIZE, num_aie_columns=c_cols, tile_size=_EDGE_SIZE // c_cols
    )
    if bounded:
        recording = _feedback_bounded_recording(add, mul)
    else:
        steps = sequences.steps((add, "acc", "x", "acc"), (mul, "acc", "up", "out"))
        recording = Recording.of_steps(
            "combo_feedback", steps, ["x", "up"], ["out"], feedback=["acc"]
        )
    edges = (Edge(0, "y", 0, "a"), Edge(0, "y", 1, "a"))
    edges, workers, phases = realize_helds(edges, {0: held, 1: _next(HELDS, held)})
    region = Region((member(add), member(mul)), edges, workers=workers, phases=phases)
    return recording, region, 0


def _feedback_bounded_recording(add: ElementwiseAdd, mul: ElementwiseMul) -> Recording:
    """Return ``add``'s self-loop into ``mul`` wired as ``_feedback_combo`` does, the multiply's ``up`` bound per call to ``n``.

    The accumulator is state the graph holds, so the add writes back into the
    buffer it reads, as the unbounded toy's recorded ``acc`` does.
    """
    acc = iron.state((add.size,), name="acc")

    class _Feedback(iron.Graph):
        def body(self, x, up, *, n: Scratchpad[np.int32]):
            ElementwiseAdd.step(
                acc,
                x,
                acc,
                size=add.size,
                num_aie_columns=add.num_aie_columns,
                tile_size=add.tile_size,
            )
            return ElementwiseMul.step(
                acc,
                up[:n],
                size=mul.size,
                num_aie_columns=mul.num_aie_columns,
                tile_size=mul.tile_size,
            )

    return dataclasses.replace(
        _Feedback().record(x=(add.size,), up=(mul.size,)),
        name="combo_feedback_bounded",
    )


_ROLE_BUILDERS = {
    "chain": _chain_combo,
    "fan_out": _fan_out_combo,
    "fan_in": _fan_in_combo,
    "skip": _skip_combo,
    "diamond": _diamond_combo,
    "through_memory": _through_memory_combo,
    "feedback": _feedback_combo,
}


def combination_toy(
    dev: Device,
    shape: HandOff,
    role: str,
    held: str,
    depth: str,
    rate: str,
    size: str,
) -> tuple[str, Recording, Region, int]:
    """Return ``(name, Recording, Region, distinguished_edge_index)`` for one cell of the all-pairs cover, on ``dev``.

    ``role`` picks the topology; the distinguished edge's two members take
    real lane counts on ``dev``'s array (``lane_counts``, and, for ``rate``,
    a tile-size split) realizing ``shape`` and ``rate``; every edge's held place (``held`` on the
    distinguished one, the next of ``HELDS`` on the rest) is realized
    structurally (``realize_helds``). ``depth`` is named only: its real
    value is resolved from ``iron.common.graph.sdf.analyze`` inside a test,
    never here, so the returned region's distinguished edge carries
    ``depth=None`` (the analysis's own minimum) until a test calls
    ``with_resolved_depth``.
    """
    recording, region, index = _ROLE_BUILDERS[role](
        lane_counts(shape, dev.cols), held, rate, size == "smaller"
    )
    name = f"{role}_{shape.value}_{held}_{depth}_{rate}_{size}"
    return name, recording, region, index


def all_combinations() -> list[tuple[HandOff, str, str, str, str, str]]:
    """Return an all-pairs cover of the edge axes (shape, role, held, depth, rate, size), plus the skip x split x held-in-L1 triple.

    Every pair of values from two different axes appears in at least one
    combo (a greedy pairwise cover); known-dangerous triples are added
    explicitly.
    """
    axes = [SHAPES, ROLES, HELDS, DEPTHS, RATES, SIZES]
    seen_pairs: set[tuple[int, int, Any, Any]] = set()
    chosen: list[tuple] = []
    pool = list(itertools.product(*axes))
    while True:
        best, best_new = None, -1
        for combo in pool:
            new = sum(
                1
                for i in range(len(axes))
                for j in range(i + 1, len(axes))
                if (i, j, combo[i], combo[j]) not in seen_pairs
            )
            if new > best_new:
                best, best_new = combo, new
        if best_new <= 0:
            break
        chosen.append(best)
        for i in range(len(axes)):
            for j in range(i + 1, len(axes)):
                seen_pairs.add((i, j, best[i], best[j]))
    triple = (HandOff.SPLIT, "skip", "l1", "min", "same", "recorded")
    if triple not in chosen:
        chosen.append(triple)
    return chosen
