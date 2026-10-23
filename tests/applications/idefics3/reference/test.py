# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM's graphs against transformers' own SmolVLM and image processor in
float32 over the same random weights, its outputs recorded in ``goldens/``,
device-free (no checkpoint, no NPU), at a toy shape: the vision tower's
``EncoderLayer``s on SigLIP's names over a decoded image, and the tower and
the text model as one ``iron.lm.Multimodal``, its soft tokens placed across
a chunk boundary.
"""

from __future__ import annotations

import dataclasses
import re
from typing import TYPE_CHECKING

import numpy as np
import pytest

from iron.applications.idefics3.model import SmolVLMText, SmolVLMTextConfig
from iron.applications.idefics3.vision.model import VisionConfig, VisionTower
from iron.lm import Multimodal
from iron.lm.testing import LOGITS, assert_close
from iron.tests.support.llama_model import checkpoint, shapes
from iron.tests.support.llama_reference import prompt

if TYPE_CHECKING:
    from iron.applications.idefics3.hugging_face import HuggingFaceVLM

pytestmark = pytest.mark.usefixtures("npu2")

#: SmolVLM's vision tower at toy size: a 16x16 patch grid, shuffled 2x2,
#: an image first resized to 512 on its longest side.
VISION = VisionConfig(
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    intermediate_size=512,
    patch_size=16,
    image_size=256,
    scale_factor=2,
    text_dim=256,
    image_token=511,
    longest_edge=512,
    largest=(480, 640),
)
#: Its text model, Llama's layer under ``model.text_model``.
TEXT = SmolVLMTextConfig(
    vocab_size=512,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    num_key_value_heads=2,
    head_dim=64,
    intermediate_size=512,
    rope_theta=1e5,
    max_seq_len=1024,
    prefill_chunk=256,
)
IMAGE = VISION.image_token


def vision_names(c: VisionConfig) -> dict[str, tuple[int, ...]]:
    """The vision tower's and connector's tensors of a checkpoint of ``c``'s
    shape, by name.
    """
    E, F = c.hidden_size, c.intermediate_size
    v = "model.vision_model"
    out = {
        f"{v}.embeddings.patch_embedding.weight": (E, 3, c.patch_size, c.patch_size),
        f"{v}.embeddings.patch_embedding.bias": (E,),
        f"{v}.embeddings.position_embedding.weight": (c.side**2, E),
        f"{v}.post_layernorm.weight": (E,),
        f"{v}.post_layernorm.bias": (E,),
        "model.connector.modality_projection.proj.weight": (
            c.text_dim,
            E * c.scale_factor**2,
        ),
    }
    for i in range(c.num_hidden_layers):
        p = f"{v}.encoder.layers.{i}"
        for norm in ("layer_norm1", "layer_norm2"):
            out |= {f"{p}.{norm}.weight": (E,), f"{p}.{norm}.bias": (E,)}
        for proj in ("q_proj", "k_proj", "v_proj", "out_proj"):
            out |= {
                f"{p}.self_attn.{proj}.weight": (E, E),
                f"{p}.self_attn.{proj}.bias": (E,),
            }
        out |= {
            f"{p}.mlp.fc1.weight": (F, E),
            f"{p}.mlp.fc1.bias": (F,),
            f"{p}.mlp.fc2.weight": (E, F),
            f"{p}.mlp.fc2.bias": (E,),
        }
    return out


def text_names(c: SmolVLMTextConfig) -> dict[str, tuple[int, ...]]:
    """The text model's tensors of a checkpoint of ``c``'s shape, by name."""
    text = {
        k.replace("model.", "model.text_model.", 1): v for k, v in shapes(c).items()
    }
    return text | {"lm_head.weight": (c.vocab_size, c.hidden_size)}


@pytest.fixture(scope="module")
def weights():
    return checkpoint(TEXT, text_names(TEXT) | vision_names(VISION)).tree("random")


class SoftTokens:
    """transformers' soft tokens of an image: ``logits``, as ``Golden``
    reads them.
    """

    def __init__(self, hf: HuggingFaceVLM):
        self.hf = hf

    def logits(self, tokens, image):
        import torch

        with torch.no_grad():
            out = self.hf.model.model.get_image_features(self.hf.pixels(image))
        return out.pooler_output[0].numpy()


def test_the_vision_tower_s_soft_tokens_match_transformers(golden, weights):
    """The tower's reference against transformers' soft tokens: bf16
    against float32, so within 5% of the largest soft token's magnitude,
    as a decoder's logits are held.
    """
    tower = VisionTower(VISION, weights)
    rng = np.random.default_rng(1)
    image = rng.integers(0, 256, (300, 200, 3), dtype=np.uint8)
    buffer, values = tower.inputs(image)
    got = np.asarray(tower.reference(buffer, **values), np.float32)

    # transformers and torch, optional: only recording a golden imports them
    def record():
        from iron.applications.idefics3.hugging_face import HuggingFaceVLM

        return SoftTokens(
            HuggingFaceVLM.build("idefics3", VISION, weights, **TEXT.to_json())
        )

    reference = golden(
        "soft_tokens",
        record,
        TEXT,
        VISION,
        weights,
    )
    want = reference.logits([], image)
    assert got.shape == (tower.soft_rows, VISION.text_dim)
    err, scale = np.abs(got - want).max(), np.abs(want).max()
    # Measured 0.79%.
    assert err <= LOGITS * scale, f"|diff| {err:.4f} against |soft tokens| {scale:.3f}"


def test_the_image_s_soft_tokens_take_its_placeholders_across_a_chunk(golden, weights):
    """Each version's reference in turn, its states carried from one to the
    next: the tower, then each chunk, both holding some of the run of
    placeholders that crosses their boundary, through ``placed``, then a
    decode step, against transformers' logits.
    """
    model = Multimodal(
        SmolVLMText(TEXT, weights), {IMAGE: VisionTower(VISION, weights)}
    )

    def record():
        from iron.applications.idefics3.hugging_face import HuggingFaceVLM

        return HuggingFaceVLM.build("idefics3", VISION, weights, **TEXT.to_json())

    reference = golden(
        "small",
        record,
        TEXT,
        VISION,
        weights,
    )
    rng = np.random.default_rng(2)
    tokens = rng.integers(0, IMAGE, 300)
    tokens[220 : 220 + VISION.tokens] = IMAGE
    image = rng.integers(0, 256, (160, 240, 3), dtype=np.uint8)
    raw = {IMAGE: (image,)}
    for inputs, values in model.tower_calls(tokens, raw):
        model.reference(
            *inputs, token=0, position=0, start=0, rows=1, rope_start=0, **values
        )
    logits, carry = prompt(model, tokens, **model.idle)
    assert_close(logits, reference.logits(tokens, image))
    tokens = np.append(tokens, carry["token"])
    logits, _ = model.reference(start=0, rows=1, rope_start=0, **carry, **model.idle)
    assert_close(logits, reference.logits(tokens, image))


@pytest.mark.parametrize(
    "image,size",
    [
        # As Idefics3ImageProcessor resizes them at a longest edge of 2048.
        ((512, 512), (2048, 2048)),
        ((480, 640), (1536, 2048)),
        ((500, 333), (2048, 1364)),
        ((37, 53), (1430, 2048)),
        ((3, 4096), (2, 2048)),
        ((296, 970), (624, 2048)),
    ],
)
def test_the_first_resize_is_the_processor_s(image, size):
    """The processor's first size: its longest edge's, the other side at
    the image's aspect, truncated, then made even.
    """
    vision = dataclasses.replace(VISION, longest_edge=2048)
    assert vision.size(*image) == size


def test_a_rope_scaling_nested_in_the_text_config_is_refused():
    """SmolVLM's ``config.json`` nests its text model's keys under
    ``text_config``: a ``rope_scaling`` there is refused as a flat one is.
    """
    nested = TEXT.to_json()["text_config"]
    scaling = {"rope_type": "yarn", "factor": 4.0}
    with pytest.raises(ValueError, match=re.escape(f"rope_scaling {scaling}")):
        SmolVLMTextConfig.from_json({"text_config": nested | {"rope_scaling": scaling}})
