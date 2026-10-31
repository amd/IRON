# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A profile's fusion entries, and a recording's admissible on-chip fusions, device-free.

Round trips, ``candidates``, ``fusions`` and the compile wiring.
"""

import json
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common.graph.compiled import _words
from iron.common.graph.fusion import candidates, fusions
from iron.common.graph.fusion_tunables import apply as apply_fusion_tunables
from iron.common.image.step import Edge, Fusion, FusionKind
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.relu import ReLU
from iron.operators.silu import SiLU
from iron.tests.support.graphs import Chain as ChainGraph
from iron.tests.support.llama_model import small

pytestmark = pytest.mark.usefixtures("npu2")

LLAMA_NPU2_PROFILE = Path(__file__).resolve().parents[2] / (
    "applications/llama/profiles/npu2.json"
)

W = np.zeros(2048, bfloat16)


def _fuse(producer: int, output: str, input: str) -> Fusion:
    return Fusion(
        FusionKind.STREAM,
        (producer, producer + 1),
        (Edge(producer, output, producer + 1, input),),
    )


def _fused_graph(profile=None):
    """Return a graph recording ``ElementwiseMul(SiLU(x), W)``, fusable at size=2048."""

    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=2048, num_aie_columns=1)
            return ElementwiseMul.step(gate, W, tile_size=2048, num_aie_columns=1)

    if profile is not None:
        Fused.profile = profile
    return Fused()


# --------------------------------------------------------------------------
# Profile fusion entries
# --------------------------------------------------------------------------


def test_a_profile_round_trips_a_fusion(tmp_path):
    p = Profile()
    p.add(SiLU, num_aie_columns=1)
    p.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        [(0, "y", 1, "a")],
    )
    path = tmp_path / "profile.json"
    p.save(path)
    assert "fusions" in json.loads(path.read_text())

    loaded = Profile.load(path)
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert loaded.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")])
    assert not loaded.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "b")])

    roundtrip = tmp_path / "roundtrip.json"
    loaded.save(roundtrip)
    assert roundtrip.read_text() == path.read_text()


def test_a_fusion_steps_own_tunables_round_trip(tmp_path):
    """A step may give the tunables it takes running inside this fusion (narrower than the same shape unfused).

    Kept apart from its own ``add`` entry.
    """
    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [
            (SiLU, dict(size=2048), None),
            (ElementwiseMul, dict(size=2048), {"num_aie_columns": 2}),
        ],
        [(0, "y", 1, "a")],
    )
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert p.fusion_tunables(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")]) == [
        None,
        {"num_aie_columns": 2},
    ]

    path = tmp_path / "profile.json"
    p.save(path)
    assert json.loads(path.read_text())["fusions"][0]["steps"][1]["tunables"] == {
        "num_aie_columns": 2
    }
    loaded = Profile.load(path)
    assert loaded.fusion_tunables(
        FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")]
    ) == [None, {"num_aie_columns": 2}]

    roundtrip = tmp_path / "roundtrip.json"
    loaded.save(roundtrip)
    assert roundtrip.read_text() == path.read_text()


def test_fusion_tunables_is_none_without_a_matching_entry():
    p = Profile()
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert p.fusion_tunables(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")]) is None


def test_add_fusion_checks_a_steps_tunables():
    with pytest.raises(TypeError, match="has no tunable"):
        Profile().add_fusion(
            FusionKind.STREAM,
            [(SiLU, {}, None), (ElementwiseMul, {}, {"nope": 1})],
            [],
        )


def test_a_fusion_over_tuple_valued_params_matches_after_save_and_load(tmp_path):
    """A derived dim a step's build reads but a call never gives (GEMV's, SiLU's, ... own ``finish``) is a tuple live.

    A list once JSON gives it back; ``matches`` must still count them equal, or a fusion
    over any such step goes inert the moment its profile is loaded from a file.
    """
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert gate.finish == () and up.finish == ()  # the tuple this guards

    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [
            (SiLU, dict(size=2048, finish=gate.finish)),
            (ElementwiseMul, dict(size=2048, finish=up.finish)),
        ],
        [(0, "y", 1, "a")],
    )
    path = tmp_path / "profile.json"
    p.save(path)
    loaded = Profile.load(path)
    assert loaded.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")])


def test_a_tunable_entry_over_a_tuple_valued_dim_matches_after_save_and_load(tmp_path):
    gemv = GEMV(M=2048, K=2048).resolved()
    assert gemv.finish == ()  # the tuple this guards

    p = Profile()
    p.add(GEMV, M=2048, K=2048, finish=gemv.finish, num_aie_columns=8)
    path = tmp_path / "profile.json"
    p.save(path)
    loaded = Profile.load(path)
    assert loaded.tunables_for(GEMV, dict(M=2048, K=2048, finish=gemv.finish)) == {
        "num_aie_columns": 8
    }


def test_a_loaded_profiles_fusion_is_live_in_a_compiled_graph(tmp_path):
    p = _fusion_profile()
    path = tmp_path / "profile.json"
    p.save(path)
    version = _fused_graph(Profile.load(path)).compile(
        full_elf=True, check=False, x=(2048,)
    )
    assert version.sequence.fusions == (_fuse(0, "y", "a"),)


def test_a_profile_with_a_copy_fusion_round_trips():
    """Copy's ``src``/``dst`` (``TensorAccessPattern``) are not JSON representable; a fusion entry still names it by its other dims."""
    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [(Copy, dict(input_buffer_size=1024)), (ElementwiseMul, dict(size=1024))],
        [(0, "y", 1, "a")],
    )
    copy_op = Copy(input_buffer_size=1024).resolved()
    mul = ElementwiseMul(size=1024, tile_size=1024).resolved()
    assert p.fused(FusionKind.STREAM, [copy_op, mul], [(0, "y", 1, "a")])


def test_a_profile_without_fusions_saves_as_before(tmp_path):
    p = Profile()
    p.add(SiLU, num_aie_columns=1)
    path = tmp_path / "profile.json"
    p.save(path)
    assert set(json.loads(path.read_text())) == {"entries"}

    roundtrip = tmp_path / "roundtrip.json"
    Profile.load(path).save(roundtrip)
    assert roundtrip.read_text() == path.read_text()


def test_an_existing_profile_saves_byte_identically(tmp_path):
    original = LLAMA_NPU2_PROFILE.read_text()
    roundtrip = tmp_path / "npu2.json"
    Profile.load(LLAMA_NPU2_PROFILE).save(roundtrip)
    assert roundtrip.read_text() == original


def test_add_fusion_checks_its_steps_dims_and_edges():
    with pytest.raises(TypeError, match="at least two steps"):
        Profile().add_fusion(FusionKind.STREAM, [(SiLU, {})], [])
    with pytest.raises(TypeError, match="declares no dim"):
        Profile().add_fusion(
            FusionKind.STREAM,
            [(SiLU, dict(nope=1)), (ElementwiseMul, {})],
            [],
        )
    with pytest.raises(TypeError, match="declares no dim"):
        Profile().add_fusion(
            FusionKind.STREAM,
            [(SiLU, {}), (ElementwiseMul, dict(num_aie_columns=1))],
            [],
        )  # a tunable, not a dim
    with pytest.raises(TypeError, match="declares no input"):
        Profile().add_fusion(
            FusionKind.STREAM,
            [(SiLU, {}), (ElementwiseMul, {})],
            [(0, "y", 1, "nope")],
        )
    with pytest.raises(TypeError, match="outside"):
        Profile().add_fusion(
            FusionKind.STREAM,
            [(SiLU, {}), (ElementwiseMul, {})],
            [(0, "y", 2, "a")],
        )
    with pytest.raises(TypeError, match="itself"):
        Profile().add_fusion(
            FusionKind.STREAM,
            [(SiLU, {}), (ElementwiseMul, {})],
            [(0, "y", 0, "a")],
        )


def test_fused_matches_by_class_dims_and_wiring_like_a_tunable_entry():
    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        [(0, "y", 1, "a")],
    )
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert p.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")])
    other_gate = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    other_up = ElementwiseMul(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    assert not p.fused(FusionKind.STREAM, [other_gate, other_up], [(0, "y", 1, "a")])


# --------------------------------------------------------------------------
# A fusion entry's own versions (as a packing entry's own: Profile.add_
# packing's versions=, PackingEntry), one list serving every fusion kind
# --------------------------------------------------------------------------


def test_an_unscoped_fusion_entry_applies_in_every_version(llama_recordings):
    decode, prompt = llama_recordings
    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        [(0, "y", 1, "a")],
    )
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    edge = [(0, "y", 1, "a")]
    assert p.fused(FusionKind.STREAM, [gate, up], edge)  # no version given, as before
    assert p.fused(FusionKind.STREAM, [gate, up], edge, decode.version)
    assert p.fused(FusionKind.STREAM, [gate, up], edge, prompt.version)


def test_a_fusion_entry_scoped_to_decode_does_not_apply_to_the_prompt(
    llama_recordings,
):
    decode, prompt = llama_recordings
    assert decode.version != prompt.version
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    edge = [(0, "y", 1, "a")]

    scoped_to_decode = Profile()
    scoped_to_decode.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        edge,
        versions=[decode.version],
    )
    assert scoped_to_decode.fused(FusionKind.STREAM, [gate, up], edge, decode.version)
    assert not scoped_to_decode.fused(
        FusionKind.STREAM, [gate, up], edge, prompt.version
    )
    assert not scoped_to_decode.fused(FusionKind.STREAM, [gate, up], edge)

    scoped_to_prompt = Profile()
    scoped_to_prompt.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        edge,
        versions=[prompt.version],
    )
    assert scoped_to_prompt.fused(FusionKind.STREAM, [gate, up], edge, prompt.version)
    assert not scoped_to_prompt.fused(
        FusionKind.STREAM, [gate, up], edge, decode.version
    )


def test_add_fusion_checks_its_versions():
    with pytest.raises(TypeError, match="at least one version"):
        Profile().add_fusion(
            FusionKind.STREAM,
            [(SiLU, {}), (ElementwiseMul, {})],
            [(0, "y", 1, "a")],
            versions=[],
        )


def test_a_fusion_entrys_versions_round_trip_through_json(tmp_path):
    """A version is a dict key in a running profile (``frozenset[Version]``); JSON gives every tuple in it back as a list.

    The same bug a dim's own tuple-valued field hit before ``matches`` normalized it
    (``test_a_fusion_ over_tuple_valued_params_matches_after_save_and_load``) -- a
    version must round-trip to the exact tuple it was, not merely an equal-looking one,
    or ``version in entry_versions`` never finds it again.
    """
    version = (("x", (2048,), "bfloat16"),)
    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        [(0, "y", 1, "a")],
        versions=[version],
    )
    path = tmp_path / "profile.json"
    p.save(path)
    assert json.loads(path.read_text())["fusions"][0]["versions"] == [
        {"x": [[2048], "bfloat16"]}
    ]

    loaded = Profile.load(path)
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert loaded.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")], version)
    (fusion_versions,) = (versions for *_, versions in loaded.fusions())
    assert fusion_versions == frozenset({version})

    roundtrip = tmp_path / "roundtrip.json"
    loaded.save(roundtrip)
    assert roundtrip.read_text() == path.read_text()


# --------------------------------------------------------------------------
# candidates(): a recording's admissible fusions
# --------------------------------------------------------------------------


@pytest.fixture(scope="module")
def llama_recordings():
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    return model.record(**decode_shapes), model.record(**prompt_shapes)


def test_candidates_finds_silu_mul_and_decodes_gemv_add_residuals(llama_recordings):
    """Decode finds SiLU -> ElementwiseMul and GEMV.C -> ElementwiseAdd.b; the prompt chunk not the latter.

    SiLU -> ElementwiseMul one per layer, GEMV.C -> ElementwiseAdd.b the attention and
    MLP residual adds, two per layer. The prompt chunk, whose projections are GEMM,
    finds none of the latter (and, not
    Elementwise-restricted any more, also its final Copy.y -> RMSNorm.x). Two-step
    sub-fusions of these pairs are what this counts.
    """
    decode, prompt = llama_recordings
    for recording, gemv_add_edges in ((decode, 4), (prompt, 0)):
        edges = [f for f in candidates(recording) if len(f.steps) == 2]
        kinds = [
            (
                type(recording.steps[f.steps[0]].op.resolved()).__name__,
                f.edges[0].output,
                type(recording.steps[f.steps[1]].op.resolved()).__name__,
                f.edges[0].input,
            )
            for f in edges
        ]
        silu_mul = [k for k in kinds if k[0] == "SiLU"]
        gemv_add = [k for k in kinds if k[0] == "GEMV"]
        assert all(k == ("SiLU", "y", "ElementwiseMul", "a") for k in silu_mul)
        assert all(k == ("GEMV", "C", "ElementwiseAdd", "b") for k in gemv_add)
        assert len(silu_mul) == 2  # SMALL's num_hidden_layers
        assert len(gemv_add) == gemv_add_edges

    # The prompt chunk's last step is a plain, non-Elementwise Copy feeding
    # the final RMSNorm: admissible now that candidates() tries a real build
    # rather than requiring both ends to be Elementwise.
    kinds = {
        (
            type(prompt.steps[f.steps[0]].op.resolved()).__name__,
            type(prompt.steps[f.steps[1]].op.resolved()).__name__,
        )
        for f in candidates(prompt)
        if len(f.steps) == 2
    }
    assert ("Copy", "RMSNorm") in kinds


def test_mismatched_tile_sizes_stage_the_edge():
    """A stream edge refuses SiLU's 1024-element tiles into ElementwiseMul's 512; a staged one forwards them through a memtile."""

    class Mismatched(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=1024, num_aie_columns=1)
            return ElementwiseMul.step(gate, W, tile_size=512, num_aie_columns=1)

    recording = Mismatched().record(x=(2048,))
    assert candidates(recording, (FusionKind.STREAM,)) == ()
    assert candidates(recording) == (
        Fusion(FusionKind.STAGED, (0, 1), (Edge(0, "y", 1, "a"),)),
    )


def test_matching_tile_sizes_admit_the_edge():
    recording = _fused_graph().record(x=(2048,))
    assert candidates(recording) == (_fuse(0, "y", "a"),)


def test_candidates_includes_overlapping_sub_runs_of_a_longer_admissible_run():
    # add, silu, mul, add, silu: admissible at every adjacent pair, one
    # connected run of all five steps; every contiguous sub-run of 2+ steps
    # is a candidate, overlapping ones included.
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    found = candidates(recording)
    pairs = tuple(f for f in found if len(f.steps) == 2)
    assert pairs == (
        _fuse(0, "y", "x"),
        _fuse(1, "y", "a"),
        _fuse(2, "y", "a"),
        _fuse(3, "y", "x"),
    )
    assert len(found) == 10  # every contiguous window of 2..5 of 5 steps
    whole = next(f for f in found if f.steps == (0, 1, 2, 3, 4))
    assert whole.kind is FusionKind.STREAM
    assert len(whole.edges) == 4


# --------------------------------------------------------------------------
# fusions(): the candidates a profile names
# --------------------------------------------------------------------------


def test_fusions_picks_one_of_two_overlapping_candidates_first_in_step_order():
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    p = Profile()
    for producer, consumer, input in (
        (ElementwiseAdd, SiLU, "x"),
        (SiLU, ElementwiseMul, "a"),
        (ElementwiseMul, ElementwiseAdd, "a"),
        (ElementwiseAdd, SiLU, "x"),
    ):
        p.add_fusion(
            FusionKind.STREAM,
            [(producer, dict(size=2048)), (consumer, dict(size=2048))],
            [(0, "y", 1, input)],
        )
    # Every pair is named, but step 1 (silu) is both the first pair's
    # consumer and the second's producer: the first in step order wins, and
    # the steps it uses are no longer available to a later candidate.
    assert fusions(recording, p) == (_fuse(0, "y", "x"), _fuse(2, "y", "a"))


def test_fusions_falls_back_to_the_second_edge_when_only_it_is_named():
    # add, silu, mul: add->silu and silu->mul overlap at silu (step 1).
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    pairs = [f for f in candidates(recording) if len(f.steps) == 2]
    first, second = pairs[:2]
    assert (first, second) == (_fuse(0, "y", "x"), _fuse(1, "y", "a"))

    both = Profile()
    both.add_fusion(
        FusionKind.STREAM,
        [(ElementwiseAdd, dict(size=2048)), (SiLU, dict(size=2048))],
        [(0, "y", 1, "x")],
    )
    both.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        [(0, "y", 1, "a")],
    )
    # The first wins the overlap; the second never appears alongside it.
    assert first in fusions(recording, both) and second not in fusions(recording, both)

    second_only = Profile()
    second_only.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        [(0, "y", 1, "a")],
    )
    assert fusions(recording, second_only) == (second,)


def _silu_edges(recording):
    """Return ``recording``'s SiLU -> ElementwiseMul candidates.

    Decode's also has GEMV -> ElementwiseAdd ones, which ``size`` means nothing to.
    """
    return tuple(
        f
        for f in candidates(recording)
        if len(f.steps) == 2
        and type(recording.steps[f.steps[0]].op.resolved()).__name__ == "SiLU"
    )


def test_fusions_returns_candidates_a_matching_profile_names(llama_recordings):
    decode, prompt = llama_recordings
    decode_edges, prompt_edges = _silu_edges(decode), _silu_edges(prompt)
    decode_size = decode.steps[decode_edges[0].steps[0]].op.resolved().size
    prompt_size = prompt.steps[prompt_edges[0].steps[0]].op.resolved().size
    assert decode_size != prompt_size

    matching = Profile()
    matching.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=decode_size)), (ElementwiseMul, dict(size=decode_size))],
        [(0, "y", 1, "a")],
    )
    # The profile names only SiLU -> ElementwiseMul: decode's GEMV -> Add
    # candidates are left out, unnamed.
    assert fusions(decode, matching) == decode_edges
    assert fusions(prompt, matching) == ()  # the prompt's size does not match

    empty = Profile()
    assert fusions(decode, empty) == () and fusions(prompt, empty) == ()


# --------------------------------------------------------------------------
# Graph.compile: fusions reach Image only on a full ELF, unchecked
# --------------------------------------------------------------------------


def _fusion_profile() -> Profile:
    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=2048)), (ElementwiseMul, dict(size=2048))],
        [(0, "y", 1, "a")],
    )
    return p


def test_compile_passes_full_elf_fusions_to_the_image():
    version = _fused_graph(_fusion_profile()).compile(
        full_elf=True, check=False, x=(2048,)
    )
    assert version.sequence.fusions == (_fuse(0, "y", "a"),)


def test_compile_applies_a_fusions_own_tunables_to_its_steps():
    """A step inside a taken fusion is rebuilt at the tunables its entry gives it (``iron.common.graph.fusion_tunables``).

    Narrower than how the graph itself recorded it; a stream edge's producer and
    consumer must still meet at the same lane count, so both give the same narrower
    width.
    """
    size = 8192
    w = np.zeros(size, bfloat16)

    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=2048, num_aie_columns=4)
            return ElementwiseMul.step(gate, w, tile_size=2048, num_aie_columns=4)

    p = Profile()
    p.add_fusion(
        FusionKind.STREAM,
        [
            (SiLU, dict(size=size), {"num_aie_columns": 2}),
            (ElementwiseMul, dict(size=size), {"num_aie_columns": 2}),
        ],
        [(0, "y", 1, "a")],
    )
    Fused.profile = p
    version = Fused().compile(full_elf=True, check=False, x=(size,))
    silu, mul = version.recording.steps[0].op, version.recording.steps[1].op
    assert silu.num_aie_columns == 2  # the fusion's own, narrower than recorded (4)
    assert mul.num_aie_columns == 2  # a stream edge's lanes must still match


class BoundedPair(iron.Graph):
    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(ReLU.step(x[:n], num_aie_columns=4), num_aie_columns=4)


def test_a_narrowed_step_keeps_its_per_call_values(npu2):
    """A step narrowed inside a fusion is a design of its own, reading its own value symbols.

    Each value bound to the recorded step is written to the narrowed one's, or its rows
    stay whatever the scratchpad last held.
    """
    recording = BoundedPair().record(x=(4096,))
    p = Profile()
    p.add_fusion(
        FusionKind.MERGE,
        [
            (ReLU, dict(size=4096), {"num_aie_columns": 2}),
            (ReLU, dict(size=4096), {"num_aie_columns": 2}),
        ],
        [],
    )
    fused = fusions(recording, p)
    assert fused
    patched = apply_fusion_tunables(recording, p, fused, npu2)
    written = {w.symbol for w in _words(patched)[0]}
    for old, new in zip(recording.steps, patched.steps):
        names = {b.member.name for b in recording.bindings if b.op is old.op}
        assert names and new.op.num_aie_columns == 2
        assert {new.op.value(n).symbol for n in names} <= written


def test_compile_withholds_fusions_under_check_but_not_a_step_per_xclbin():
    checked = _fused_graph(_fusion_profile()).compile(check=True, x=(2048,))
    assert checked.plan.full_elf is False and checked.sequence.fusions == ()

    per_step = _fused_graph(_fusion_profile()).compile(
        full_elf=False, check=False, x=(2048,)
    )
    assert per_step.plan.full_elf is False
    assert per_step.sequence.fusions == (_fuse(0, "y", "a"),)


def test_a_profile_with_no_fusion_entries_compiles_unaffected():
    version = _fused_graph().compile(full_elf=True, check=False, x=(2048,))
    assert version.sequence.fusions == ()
