# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A profile's fusion entries, and a recording's admissible on-chip
fusions, device-free: round trips, ``candidates``, ``fusions`` and the
compile wiring.
"""

import json
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.common.graph.fusion import candidates, fusions
from iron.common.image.step import Edge, Fusion, FusionKind
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
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
    """A graph recording ``ElementwiseMul(SiLU(x), W)``, fusable at size=2048."""

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


def test_a_profile_with_a_copy_fusion_round_trips():
    """Copy's ``src``/``dst`` (``TensorAccessPattern``) are not JSON
    representable; a fusion entry still names it by its other dims.
    """
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
# candidates(): a recording's admissible fusions
# --------------------------------------------------------------------------


@pytest.fixture(scope="module")
def llama_recordings():
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    return model.record(**decode_shapes), model.record(**prompt_shapes)


def test_candidates_finds_silu_mul_and_decodes_gemv_add_residuals(llama_recordings):
    """Decode finds SiLU -> ElementwiseMul (one per layer) and GEMV.C ->
    ElementwiseAdd.b (the attention and MLP residual adds, two per layer); the
    prompt chunk, whose projections are GEMM, finds none of the latter (and,
    not Elementwise-restricted any more, also its final Copy.y -> RMSNorm.x).
    Two-step sub-fusions of these pairs are what this counts.
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


def test_mismatched_tile_sizes_refuse_the_edge():
    class Mismatched(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=1024, num_aie_columns=1)
            return ElementwiseMul.step(gate, W, tile_size=512, num_aie_columns=1)

    recording = Mismatched().record(x=(2048,))
    assert candidates(recording) == ()


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
    """``recording``'s SiLU -> ElementwiseMul candidates: decode's also has
    GEMV -> ElementwiseAdd ones, which ``size`` means nothing to.
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
