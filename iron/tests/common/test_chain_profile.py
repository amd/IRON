# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A profile's chain entries, and a recording's admissible on-chip chains,
device-free: round trips, ``candidates``, ``chains`` and the compile wiring.
"""

import json
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.common.graph.chain import candidates, chains
from iron.common.image.step import Chain
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


def _fused_graph(profile=None):
    """A graph recording ``ElementwiseMul(SiLU(x), W)``, chainable at size=2048."""

    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=2048, num_aie_columns=1)
            return ElementwiseMul.step(gate, W, tile_size=2048, num_aie_columns=1)

    if profile is not None:
        Fused.profile = profile
    return Fused()


# --------------------------------------------------------------------------
# Profile chain entries
# --------------------------------------------------------------------------


def test_a_profile_round_trips_a_chain(tmp_path):
    p = Profile()
    p.add(SiLU, num_aie_columns=1)
    p.add_chain(
        SiLU,
        ElementwiseMul,
        "a",
        producer_dims=dict(size=2048),
        consumer_dims=dict(size=2048),
    )
    path = tmp_path / "profile.json"
    p.save(path)
    assert "chains" in json.loads(path.read_text())

    loaded = Profile.load(path)
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert loaded.chained(gate, up, "a")
    assert not loaded.chained(gate, up, "b")

    roundtrip = tmp_path / "roundtrip.json"
    loaded.save(roundtrip)
    assert roundtrip.read_text() == path.read_text()


def test_a_profile_without_chains_saves_as_before(tmp_path):
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


def test_add_chain_checks_its_dims_and_input():
    with pytest.raises(TypeError, match="declares no dim"):
        Profile().add_chain(SiLU, ElementwiseMul, "a", producer_dims=dict(nope=1))
    with pytest.raises(TypeError, match="declares no dim"):
        Profile().add_chain(
            SiLU, ElementwiseMul, "a", consumer_dims=dict(num_aie_columns=1)
        )  # a tunable, not a dim
    with pytest.raises(TypeError, match="declares no input"):
        Profile().add_chain(SiLU, ElementwiseMul, "nope")


def test_chained_matches_by_class_and_dims_like_a_tunable_entry():
    p = Profile()
    p.add_chain(
        SiLU,
        ElementwiseMul,
        "a",
        producer_dims=dict(size=2048),
        consumer_dims=dict(size=2048),
    )
    gate = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved()
    assert p.chained(gate, up, "a")
    other_gate = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    other_up = ElementwiseMul(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    assert not p.chained(other_gate, other_up, "a")


# --------------------------------------------------------------------------
# candidates(): a recording's admissible edges
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
    """
    decode, prompt = llama_recordings
    for recording, gemv_add_edges in ((decode, 4), (prompt, 0)):
        edges = candidates(recording)
        kinds = [
            (
                type(recording.steps[e.producer].op.resolved()).__name__,
                e.output,
                type(recording.steps[e.producer + 1].op.resolved()).__name__,
                e.input,
            )
            for e in edges
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
            type(prompt.steps[e.producer].op.resolved()).__name__,
            type(prompt.steps[e.producer + 1].op.resolved()).__name__,
        )
        for e in candidates(prompt)
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
    assert candidates(recording) == (Chain(0, "y", "a"),)


def test_candidates_overlap_where_a_step_is_both_consumer_and_producer():
    # add, silu, mul, add, silu: admissible at every adjacent pair, so silu
    # (step 1) is the first edge's consumer and the second's producer.
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    assert candidates(recording) == (
        Chain(0, "y", "x"),
        Chain(1, "y", "a"),
        Chain(2, "y", "a"),
        Chain(3, "y", "x"),
    )


# --------------------------------------------------------------------------
# chains(): the candidates a profile names
# --------------------------------------------------------------------------


def test_chains_picks_one_of_two_overlapping_candidates_first_in_step_order():
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    p = Profile()
    for producer, consumer, input in (
        (ElementwiseAdd, SiLU, "x"),
        (SiLU, ElementwiseMul, "a"),
        (ElementwiseMul, ElementwiseAdd, "a"),
        (ElementwiseAdd, SiLU, "x"),
    ):
        p.add_chain(
            producer,
            consumer,
            input,
            producer_dims=dict(size=2048),
            consumer_dims=dict(size=2048),
        )
    # Every edge is profiled, but step 1 (silu) is both the first edge's
    # consumer and the second's producer: the first in step order wins, and
    # the steps it uses are no longer available to a later edge.
    assert chains(recording, p) == (Chain(0, "y", "x"), Chain(2, "y", "a"))


def test_chains_falls_back_to_the_second_edge_when_only_it_is_named():
    # add, silu, mul: add->silu and silu->mul overlap at silu (step 1).
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    first, second = candidates(recording)[:2]
    assert (first, second) == (Chain(0, "y", "x"), Chain(1, "y", "a"))

    both = Profile()
    both.add_chain(
        ElementwiseAdd,
        SiLU,
        "x",
        producer_dims=dict(size=2048),
        consumer_dims=dict(size=2048),
    )
    both.add_chain(
        SiLU,
        ElementwiseMul,
        "a",
        producer_dims=dict(size=2048),
        consumer_dims=dict(size=2048),
    )
    # The first wins the overlap; the second never appears alongside it.
    assert first in chains(recording, both) and second not in chains(recording, both)

    second_only = Profile()
    second_only.add_chain(
        SiLU,
        ElementwiseMul,
        "a",
        producer_dims=dict(size=2048),
        consumer_dims=dict(size=2048),
    )
    assert chains(recording, second_only) == (second,)


def _silu_edges(recording):
    """``recording``'s SiLU -> ElementwiseMul candidates: decode's also has
    GEMV -> ElementwiseAdd ones, which ``size`` means nothing to.
    """
    return tuple(
        e
        for e in candidates(recording)
        if type(recording.steps[e.producer].op.resolved()).__name__ == "SiLU"
    )


def test_chains_returns_candidates_a_matching_profile_names(llama_recordings):
    decode, prompt = llama_recordings
    decode_edges, prompt_edges = _silu_edges(decode), _silu_edges(prompt)
    decode_size = decode.steps[decode_edges[0].producer].op.resolved().size
    prompt_size = prompt.steps[prompt_edges[0].producer].op.resolved().size
    assert decode_size != prompt_size

    matching = Profile()
    matching.add_chain(
        SiLU,
        ElementwiseMul,
        "a",
        producer_dims=dict(size=decode_size),
        consumer_dims=dict(size=decode_size),
    )
    # The profile names only SiLU -> ElementwiseMul: decode's GEMV -> Add
    # candidates are left out, unnamed.
    assert chains(decode, matching) == decode_edges
    assert chains(prompt, matching) == ()  # the prompt's size does not match

    empty = Profile()
    assert chains(decode, empty) == () and chains(prompt, empty) == ()


# --------------------------------------------------------------------------
# Graph.compile: chains reach Image only on a full ELF, unchecked
# --------------------------------------------------------------------------


def _chain_profile() -> Profile:
    p = Profile()
    p.add_chain(
        SiLU,
        ElementwiseMul,
        "a",
        producer_dims=dict(size=2048),
        consumer_dims=dict(size=2048),
    )
    return p


def test_compile_passes_full_elf_chains_to_the_image():
    version = _fused_graph(_chain_profile()).compile(
        full_elf=True, check=False, x=(2048,)
    )
    assert version.sequence.chains == (Chain(0, "y", "a"),)


def test_compile_withholds_chains_under_check_or_a_step_per_xclbin():
    checked = _fused_graph(_chain_profile()).compile(check=True, x=(2048,))
    assert checked.plan.full_elf is False and checked.sequence.chains == ()

    per_step = _fused_graph(_chain_profile()).compile(
        full_elf=False, check=False, x=(2048,)
    )
    assert per_step.plan.full_elf is False and per_step.sequence.chains == ()


def test_a_profile_with_no_chain_entries_compiles_unaffected():
    version = _fused_graph().compile(full_elf=True, check=False, x=(2048,))
    assert version.sequence.chains == ()
