# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.validate``'s pure parts, device-free: version labels, the
live-fusion and live-packing accounting a report reads, the profile
subsets a bisection trial builds, and ``changed_versions``' assertion.
"""

import pytest

from iron import Profile
from iron.common.graph.fusion import candidates
from iron.common.image.step import FusionKind
from iron.lm import validate
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU
from iron.tests.support.llama_model import small

pytestmark = pytest.mark.usefixtures("npu2")


def _silu_mul_entry(recording):
    """The ``(SiLU, dims)`` -> ``(ElementwiseMul, dims)`` fusion entry
    ``recording`` admits, in ``Profile.add_fusion``'s own shape.
    """
    fusion = next(
        f
        for f in candidates(recording)
        if len(f.steps) == 2
        and type(recording.steps[f.steps[0]].op.resolved()).__name__ == "SiLU"
    )
    gate = recording.steps[fusion.steps[0]].op.resolved()
    mul = recording.steps[fusion.steps[1]].op.resolved()
    edge = fusion.edges[0]
    return (
        FusionKind.STREAM,
        [(SiLU, dict(size=gate.size)), (ElementwiseMul, dict(size=mul.size))],
        [(0, edge.output, 1, edge.input)],
    )


def test_version_labels_names_decode_and_prompt():
    assert validate.version_labels(small()) == ["decode", "prompt"]


def test_entry_applies_only_to_the_recording_it_was_taken_from():
    model = small()
    decode_shape, prompt_shape = model.shapes()
    decode = model.record(**decode_shape)
    prompt = model.record(**prompt_shape)
    entry = _silu_mul_entry(decode)
    assert validate.entry_applies("fusion", entry, decode)
    assert not validate.entry_applies("fusion", entry, prompt)  # a different size


def test_classify_entries_tags_by_matching_version():
    model = small()
    decode_shape, prompt_shape = model.shapes()
    recordings = {
        "decode": model.record(**decode_shape),
        "prompt": model.record(**prompt_shape),
    }
    entry = _silu_mul_entry(recordings["decode"])
    candidate = Profile()
    candidate.add_fusion(*entry)
    [(tag, matches)] = validate.classify_entries(candidate, recordings)
    assert tag == ("fusion", candidate.fusions()[0])
    assert matches == {"decode"}


def test_classify_entries_tags_a_packing_by_the_versions_it_names():
    """Both versions run SiLU and a multiply; a packing naming the decode
    step's version is tagged decode alone, one naming none both."""
    model = small()
    decode_shape, prompt_shape = model.shapes()
    recordings = {
        "decode": model.record(**decode_shape),
        "prompt": model.record(**prompt_shape),
    }
    members = [(SiLU, {}), (ElementwiseMul, {})]
    candidate = Profile()
    candidate.add_packing(members, versions=[recordings["decode"].version])
    candidate.add_packing(members)
    scoped, everywhere = validate.classify_entries(candidate, recordings)
    assert scoped[1] == {"decode"}
    assert everywhere[1] == {"decode", "prompt"}


def _raw_entry():
    return (
        FusionKind.STREAM,
        [(SiLU, {"size": 2048}), (ElementwiseMul, {"size": 2048})],
        [(0, "y", 1, "a")],
    )


def test_build_variant_adds_tagged_entries_to_the_stock_profile(tmp_path):
    stock_path = tmp_path / "npu2.json"
    Profile().save(stock_path)
    entry = _raw_entry()
    expected = Profile()
    expected.add_fusion(*entry)
    variant = validate.build_variant(stock_path, [("fusion", entry)])
    assert variant.fusions() == expected.fusions()


def test_build_variant_with_no_stock_path_starts_empty():
    entry = _raw_entry()
    expected = Profile()
    expected.add_fusion(*entry)
    variant = validate.build_variant(None, [("fusion", entry)])
    assert variant.fusions() == expected.fusions() and len(variant) == 0


def test_verify_live_and_changed_versions_see_a_candidates_live_fusion():
    stock_model = small()
    entry = _silu_mul_entry(stock_model.record(**stock_model.shapes()[0]))
    candidate_profile = Profile()
    candidate_profile.add_fusion(*entry)
    candidate_model = small()
    candidate_model.profile = candidate_profile

    decode_shape = stock_model.shapes()[0]
    stock_model.compile(full_elf=True, check=False, **decode_shape)
    candidate_model.compile(full_elf=True, check=False, **decode_shape)

    stock_live = validate.verify_live("stock", stock_model)
    candidate_live = validate.verify_live("candidate", candidate_model)
    assert stock_live["decode"]["n_fusions"] == 0
    # SMALL's two layers share one shape, so the entry (matched by dims
    # alone) fuses both layers' SiLU -> ElementwiseMul.
    assert candidate_live["decode"]["n_fusions"] == 2
    assert candidate_live["decode"]["kinds"] == {"stream": 2}

    assert validate.changed_versions(stock_live, candidate_live) == ["decode"]


def test_changed_versions_rejects_a_live_candidate_sharing_stocks_image():
    stock_live = {"decode": {"image_path": "a"}}
    candidate_live = {
        "decode": {"image_path": "a", "n_fusions": 1, "packed_groups": []}
    }
    with pytest.raises(AssertionError, match="share one compiled image"):
        validate.changed_versions(stock_live, candidate_live)


def test_changed_versions_counts_a_candidate_changing_only_tunables():
    stock_live = {"decode": {"image_path": "a"}, "prompt": {"image_path": "p"}}
    candidate_live = {
        "decode": {"image_path": "b", "n_fusions": 0, "packed_groups": []},
        "prompt": {"image_path": "p", "n_fusions": 0, "packed_groups": []},
    }
    assert validate.changed_versions(stock_live, candidate_live) == ["decode"]


def test_changed_versions_ignores_an_unchanged_candidate():
    stock_live = {"decode": {"image_path": "a"}}
    candidate_live = {
        "decode": {"image_path": "a", "n_fusions": 0, "packed_groups": []}
    }
    assert validate.changed_versions(stock_live, candidate_live) == []
