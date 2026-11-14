# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The composition contract names every dataflow pattern the plan's coverage list asks for."""

from pathlib import Path

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import (
    Binding,
    Configuration,
    Entry,
    Member,
    Region,
    Schedule,
    Variants,
)
from iron.common.image.step import Edge, EdgeKind, HandOff, Held
from iron.operators.copy import Copy, Gather
from iron.operators.decode import Decode
from iron.operators.depthwise_conv1d import DepthwiseConv1d
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.sample import Sample
from iron.operators.selective_scan import SelectiveScan
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.tests.support.tuning import unbuilt

N = 2048


def _layer() -> tuple[Member, ...]:
    return (
        Member(ElementwiseAdd, {"size": N}),
        Member(RMSNorm, {"rows": 1}),
        Member(GEMV, {"M": N, "K": N}),
        Member(SiLU, {"size": N}),
        Member(ElementwiseMul, {"size": N}),
        Member(GEMV, {"M": N, "K": N}),
        Member(ElementwiseAdd, {"size": N}),
    )


def _skip() -> Entry:
    return Entry(
        Region(
            _layer(),
            (
                Edge(0, "y", 1, "x"),
                Edge(1, "y", 2, "B"),
                Edge(2, "C", 3, "x"),
                Edge(3, "y", 4, "a"),
                Edge(4, "y", 5, "B"),
                Edge(5, "C", 6, "b"),
                Edge(0, "y", 6, "a", held=Held.MEMTILE),
            ),
        )
    )


def _qkv_fan_out_and_fan_in() -> Entry:
    return Entry(
        Region(
            (
                Member(RMSNorm, {"rows": 1}),
                Member(GEMV, {"M": N, "K": N}),
                Member(GEMV, {"M": 512, "K": N}),
                Member(GEMV, {"M": 512, "K": N}),
                Member(SiLU, {"size": 512}),
                Member(ElementwiseMul, {"size": 512}),
            ),
            (
                Edge(0, "y", 1, "B"),
                Edge(0, "y", 2, "B"),
                Edge(0, "y", 3, "B"),
                Edge(2, "C", 4, "x"),
                Edge(4, "y", 5, "a"),
                Edge(3, "C", 5, "b"),
            ),
        )
    )


def _routing_and_gather() -> Entry:
    return Entry(
        Region(
            (
                Member(GEMV, {"M": 64, "K": N}),
                Member(Softmax, {"rows": 1, "cols": 64}),
                Member(Sample, {"vocab": 64, "k_max": 2}),
                Member(Gather, {"rows": 2, "table_rows": 64}),
                Member(GEMV, {"M": N, "K": N}),
            ),
            (
                Edge(0, "C", 1, "x"),
                Edge(1, "y", 2, "logits"),
                Edge(2, "ids", 3, "ids"),
                Edge(3, "y", 4, "A", kind=EdgeKind.DDR),
            ),
        )
    )


def _encoder_decoder_cross() -> Entry:
    return Entry(
        Configuration(
            (
                Region((Member(GEMV, {"M": N, "K": N}),)),
                Region(
                    (
                        Member(GEMV, {"M": N, "K": N}),
                        Member(GEMV, {"M": 512, "K": N}),
                    ),
                    (Edge(0, "C", 1, "B", kind=EdgeKind.DDR),),
                ),
            )
        )
    )


def _recurrent_state() -> Entry:
    return Entry(
        Region(
            (
                Member(RoPE, {"rows": 1, "cols": 64}),
                Member(Copy, {"rows": 1, "table_rows": N}),
                Member(GEMV, {"M": N, "K": 64}),
                Member(SelectiveScan, {"rows": 1, "heads": 8, "head_dim": 64}),
            ),
            (
                Edge(0, "y", 1, "x"),
                Edge(3, "state", 3, "state", delay=1),
            ),
            order=((1, 2),),
        )
    )


def _layer_into_layer() -> Entry:
    first, second = _layer(), _layer()
    return Entry(
        Region(
            first + second,
            (
                Edge(1, "y", 2, "B"),
                Edge(6, "y", 7, "a"),
                Edge(6, "y", 8, "x"),
                Edge(8, "y", 9, "B"),
            ),
        )
    )


def _multi_rate() -> Entry:
    return Entry(
        Region(
            (
                Member(DepthwiseConv1d, {"rows": 64, "channels": 256}),
                Member(ElementwiseAdd, {"size": 32 * 256}),
                Member(SiLU, {"size": 128 * 256}),
            ),
            (
                Edge(0, "y", 1, "a", rate=(2, 1)),
                Edge(1, "y", 2, "x", rate=(1, 4)),
            ),
        )
    )


def _halo() -> Entry:
    return Entry(
        Region(
            (
                Member(DepthwiseConv1d, {"rows": 64, "channels": 256}),
                Member(DepthwiseConv1d, {"rows": 64, "channels": 256}),
            ),
            (Edge(0, "y", 1, "x", rate=(1, 5)),),
        )
    )


def _split_k_cascade() -> Entry:
    parts = tuple(
        Member(GEMV, {"M": N, "K": N}, part=("K", k * N // 4, (k + 1) * N // 4))
        for k in range(4)
    )
    return Entry(
        Region(
            parts,
            tuple(
                Edge(k, "C", k + 1, "C", kind=EdgeKind.CASCADE, dtype="float32")
                for k in range(3)
            ),
        )
    )


def _broadcast_weights() -> Entry:
    return Entry(
        Region(
            (
                Member(RMSNorm, {"rows": 1}),
                Member(GEMV, {"M": N, "K": N}),
            ),
            (Edge(0, "y", 1, "B", shape=HandOff.BROADCAST),),
        )
    )


def _gemm_tiles() -> Entry:
    return Entry(
        Region(
            (
                Member(GEMM, {"M": 256, "K": N, "N": N}),
                Member(GEMM, {"M": 256, "K": N, "N": N}),
            ),
            (Edge(0, "C", 1, "A", rate=(1, 1), shape=HandOff.EQUAL),),
        )
    )


def _around_a_host_step() -> Entry:
    return Entry(
        Configuration(
            (
                Region(_layer()[:3], (Edge(0, "y", 1, "x"), Edge(1, "y", 2, "B"))),
                Member(Sample, {"vocab": N, "k_max": 1}, runs_on="host"),
                Region(_layer()[3:], (Edge(0, "y", 1, "a"),)),
            )
        )
    )


def _alternative_operator() -> Entry:
    return Entry(Region((Member(GEMV, {"M": N, "K": N}, {"implementation": "GEMM"}),)))


def _coded_weights() -> Entry:
    return Entry(
        Region(
            (Member(Decode, {"M": N, "K": N}), Member(GEMV, {"M": N, "K": N})),
            (Edge(0, "y", 1, "A", held=Held.L1),),
            workers=((0, 1),),
        )
    )


PATTERNS = {
    "residual skip": _skip,
    "Q/K/V fan-out and gate/up fan-in": _qkv_fan_out_and_fan_in,
    "routing and gather": _routing_and_gather,
    "encoder-decoder cross edge": _encoder_decoder_cross,
    "recurrent state": _recurrent_state,
    "a layer streaming into the next": _layer_into_layer,
    "multi-rate edges": _multi_rate,
    "halo and sliding window": _halo,
    "split-K over the cascade": _split_k_cascade,
    "broadcast weights": _broadcast_weights,
    "GEMM tiles producer to consumer": _gemm_tiles,
    "regions around a host step": _around_a_host_step,
    "an alternative operator": _alternative_operator,
    "coded weights decoded on chip": _coded_weights,
}


def _profile(entry: Entry) -> Profile:
    profile = Profile()
    profile.add_entry(entry)
    profile.add_schedule(Schedule("decode", order=((0, 1),), calls_per_command=2))
    profile.add_variants(
        Variants(("kv_valid",), (((1, 256),), entry), (((257, N),), entry))
    )
    profile.add_binding(Binding("kv_valid", "runtime"))
    return profile


@pytest.mark.parametrize("name", sorted(PATTERNS))
def test_every_coverage_pattern_is_an_entry_a_profile_holds(name: str) -> None:
    entry = PATTERNS[name]()
    profile = _profile(entry)
    assert profile.entries() == [entry]
    assert profile.bindings() == [Binding("kv_valid", "runtime")]


@unbuilt
@pytest.mark.parametrize("name", sorted(PATTERNS))
def test_every_coverage_pattern_round_trips_through_a_saved_profile(
    name: str, tmp_path: Path
) -> None:
    profile = _profile(PATTERNS[name]())
    profile.save(tmp_path / "npu2.json")
    loaded = Profile.load(tmp_path / "npu2.json")
    assert loaded.entries() == profile.entries()
    assert loaded.schedules() == profile.schedules()
    assert loaded.variants() == profile.variants()
    assert loaded.bindings() == profile.bindings()
