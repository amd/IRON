# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every model that is not a decoder records, device-free, whole, and
every step of every version resolves on the device: none of a model's call
path hides host compute or a shape the device refuses. The decoders'
reference tests check the same (``Decoder``'s
``test_every_step_of_every_version_resolves``).

Each model is built at its released checkpoint's config from the
checkpoint's header alone (``.tree("unread")``), through the model's own
``__init__`` and ``load_state_dict`` or ``load_layers``.
"""

import aie.utils as aie_utils
import pytest

from iron.applications.embedding_gemma2.model import Config as EmbeddingGemmaConfig
from iron.applications.embedding_gemma2.model import Multimodal as EmbeddingGemma2
from iron.applications.gemma4.audio import AudioConfig, AudioTower
from iron.applications.gemma4.model import Gemma4MultimodalConfig
from iron.applications.gemma4.vision import VisionConfig, VisionTower
from iron.common.declare.operator import Operator
from iron.lm import Checkpoint
from iron.lm.testing import require, weights_dir

pytestmark = pytest.mark.usefixtures("npu2")


def steps(model, calls: list[dict] | None = None) -> list[Operator]:
    """Every step's operator, over every version ``calls`` lists, or
    ``model.shapes()``'s for a ``Model`` with no single shape of its own.
    """
    out = []
    for call in calls if calls is not None else model.shapes():
        out += [step.op for step in model.record(**call).steps]
    return out


def assert_on_npu(model, calls: list[dict] | None = None) -> None:
    """Every step of every version of ``model`` resolves on the bound device."""
    recorded = steps(model, calls)
    assert recorded, f"{type(model).__name__}: no steps recorded"
    dev = aie_utils.get_current_device()
    for op in recorded:
        op.resolved(dev)


def test_gemma4_towers_are_on_npu():
    directory = weights_dir("gemma-4-e2b-it")
    require(directory / "model.safetensors", directory / "config.json")
    config = Gemma4MultimodalConfig.from_checkpoint(directory)
    weights = Checkpoint(directory / "model.safetensors").tree("unread")
    assert_on_npu(VisionTower(config.vision, weights.model))
    assert_on_npu(AudioTower(config.audio, weights.model))


def test_embedding_gemma2_is_on_npu():
    directory = weights_dir("embeddinggemma-2")
    require(directory / "model.safetensors", directory / "config.json")
    weights = Checkpoint(directory / "model.safetensors").tree("unread")
    model = EmbeddingGemma2(
        EmbeddingGemmaConfig.from_checkpoint(directory),
        weights,
        audio_config=AudioConfig.from_checkpoint(directory),
        vision_config=VisionConfig.from_checkpoint(directory),
    )
    assert_on_npu(model)
