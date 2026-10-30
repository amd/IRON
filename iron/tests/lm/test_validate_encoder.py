# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.validate``'s model-general path, device-free, at EmbeddingGemma
2's shape, weights drawn (``iron.common.graph.fill.filled``'s own ``Clipped``
bound, which a q, k and v projection sharing an input agrees on): an encoder
is not a ``CausalLM``, its versions carry no duplicate label, every version
has a tune point to compare it at, and a version ``compare_versions`` finds
no tune point for is reported rather than raising.
"""

import pytest

from iron import Profile
from iron.applications.embedding_gemma2 import Multimodal
from iron.lm import validate
from iron.lm.causal import CausalLM
from iron.lm.testing import require, weights_dir
from iron.lm.tune import application_model

pytestmark = pytest.mark.usefixtures("npu2")

CHECKPOINT = weights_dir("embeddinggemma-2")


def _require_checkpoint():
    require(CHECKPOINT / "model.safetensors", CHECKPOINT / "config.json")


def test_application_model_resolves_embedding_gemma2_to_multimodal():
    assert application_model("embedding_gemma2") is Multimodal
    assert not issubclass(Multimodal, CausalLM)


def test_random_weights_satisfy_clipped_same_input():
    """The audio and vision towers' q, k and v (and the vision MLP's gate and
    up) each clamp their shared input alike (``Clipped.same_input``), drawn
    weights included: construction alone raises if they do not.
    """
    _require_checkpoint()
    Multimodal.from_checkpoint(CHECKPOINT, random_weights=0)
    Multimodal.from_checkpoint(CHECKPOINT, random_weights=1)


def test_version_labels_are_one_per_version():
    _require_checkpoint()
    model = Multimodal.from_checkpoint(CHECKPOINT, random_weights=0)
    labels = validate.version_labels(model)
    assert len(labels) == len(model.shapes())
    assert len(set(labels)) == len(labels), labels


def test_version_recordings_match_every_shapes_tune_point():
    _require_checkpoint()
    model = Multimodal.from_checkpoint(CHECKPOINT, random_weights=0)
    recordings = validate.version_recordings(model)
    assert len(recordings) == len(model.shapes()), "a version collided with another"
    calls = {
        c.recording.version: c
        for c in validate.model_tune_points(Multimodal, CHECKPOINT)
    }
    assert set(recordings) == set(calls)


def test_compare_versions_reports_a_version_with_no_tune_point():
    _require_checkpoint()
    bogus = (("nowhere", (1,), "int32"),)
    out = validate.compare_versions(
        Multimodal,
        CHECKPOINT,
        None,
        Profile(),
        Profile(),
        ["nowhere"],
        {"nowhere": bogus},
    )
    assert out == {
        "nowhere": {"compared": False, "note": "no tune point for this version"}
    }
