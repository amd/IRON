# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3's graphs against Hugging Face's Ministral3 and Mistral 3 in
float32 over the same random weights at a toy shape, their outputs recorded
in ``goldens/``, device-free: the shared decoder's tests (``Decoder``), then
Pixtral's tower over a decoded image and the tower and the text decoder as
one ``iron.lm.Multimodal``, its soft tokens placed across a chunk
boundary. The toy was trained at 64 positions, so YaRN stretches it and a
query past 64 is scaled.
"""

from __future__ import annotations

import dataclasses
import json
import math
from typing import TYPE_CHECKING

import numpy as np
import pytest

from iron.applications.ministral3.model import (
    Ministral3,
    Ministral3Config,
    Ministral3VLM,
    Ministral3VLMConfig,
    YarnRopeScaling,
)
from iron.applications.ministral3.vision import VisionConfig, VisionTower
from iron.lm.checkpoint import leaves
from iron.lm.testing import LOGITS, assert_close
from iron.tests.support.llama_model import checkpoint
from iron.tests.support.llama_reference import Decoder, prompt

if TYPE_CHECKING:
    from iron.applications.ministral3.hugging_face import HuggingFaceMistral3

#: Ministral 3's proportions at toy size: GQA, a head_dim of its own, YaRN
#: from 64 positions, the query temperature, an untied head.
TOY = Ministral3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
    eps=1e-5,
    rope_scaling=YarnRopeScaling(factor=4.0, original_max_position_embeddings=64),
    llama_4_scaling_beta=0.1,
)


class TestMinistral3(Decoder):
    model, config, model_type, name = Ministral3, TOY, "ministral3", "toy"
    json = {"pad_token_id": None}
    seed = 0

    @classmethod
    def names(cls):
        c = cls.config
        return super().names() | {"lm_head.weight": (c.vocab_size, c.hidden_size)}

    def test_the_query_scale_steps_up_past_the_trained_context(self, cpu):
        """The last of the toy's 64 trained positions, its query unscaled,
        then a decode step at 64, the first scaled.
        """
        model = self.host(cpu.config, cpu.weights)
        tokens = np.random.default_rng(5).integers(0, cpu.config.vocab_size, 65)
        for n in (64, 65):
            assert_close(model.logits(tokens[:n]), cpu.golden.logits(tokens[:n]))


def test_yarn_scales_cos_and_sin_by_its_attention_factor_else_by_its_factor():
    assert TOY.rope_attention_scaling == pytest.approx(0.1 * math.log(4) + 1)
    yarn = dataclasses.replace(TOY.rope_scaling, attention_factor=1.5)
    assert dataclasses.replace(TOY, rope_scaling=yarn).rope_attention_scaling == 1.5


def test_a_query_temperature_without_yarn_is_refused():
    with pytest.raises(ValueError, match="there is no YaRN"):
        dataclasses.replace(TOY, rope_scaling=None)


#: Mistral 3's text decoder, as transformers 4 and 5 nest it.
NESTED = {
    "transformers 4": ("language_model.model.", "language_model.lm_head."),
    "transformers 5": ("model.language_model.", "lm_head."),
}


@pytest.mark.parametrize("saved", NESTED)
def test_a_mistral_3_checkpoint_reads_its_text_decoder(saved, npu2):
    model, head = NESTED[saved]
    named = {
        (head + n[8:] if n.startswith("lm_head.") else model + n[6:]): s
        for n, s in TestMinistral3.names().items()
    }
    named["model.vision_tower.patch_conv.weight"] = (8, 3, 4, 4)
    tree = checkpoint(TOY, named).tree("random", 0)
    want = dict(leaves(tree))
    got = Ministral3(TOY, tree)
    assert got.lm_head.weight is want[head + "weight"]
    assert got.model.norm.weight is want[model + "norm.weight"]


def test_an_fp8_checkpoint_is_refused(npu2):
    named = TestMinistral3.names() | {"model.norm.weight_scale_inv": (1,)}
    with pytest.raises(ValueError, match="FP8 checkpoint"):
        Ministral3(TOY, checkpoint(TOY, named).tree("random", 0))


def test_the_config_reads_from_a_mistral_3_text_config(tmp_path):
    text = TOY.to_json()
    (tmp_path / "config.json").write_text(json.dumps(text))
    flat = Ministral3Config.from_checkpoint(tmp_path)
    nested = {"model_type": "mistral3", "text_config": text, "vision_config": {}}
    (tmp_path / "config.json").write_text(json.dumps(nested))
    assert Ministral3Config.from_checkpoint(tmp_path) == flat


def test_a_tied_checkpoint_reads_its_head_from_the_embedding(npu2):
    """The released checkpoints tie the head and hold no ``lm_head``."""
    tied = dataclasses.replace(TOY, tie_word_embeddings=True)
    named = {
        "language_model." + n: s
        for n, s in TestMinistral3.names().items()
        if not n.startswith("lm_head.")
    }
    tree = checkpoint(tied, named).tree("random", 0)
    got = Ministral3(tied, tree)
    embedding = dict(leaves(tree))["language_model.model.embed_tokens.weight"]
    assert got.lm_head.weight is embedding


#: Pixtral at toy size: 14-pixel patches merged 2x2 into 28-pixel soft
#: tokens, an image resized to 112 on its longest side, into TOY's width.
VISION = VisionConfig(
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    head_dim=64,
    intermediate_size=512,
    patch_size=14,
    rope_theta=10000.0,
    text_dim=TOY.hidden_size,
    longest_edge=112,
    largest=(240, 320),
)
#: TOY over two prompt chunks.
VLM = Ministral3VLMConfig(
    **{f.name: getattr(TOY, f.name) for f in dataclasses.fields(TOY)}
    | dict(max_seq_len=512, vision=VISION)
)
IMAGE = VISION.image_token


def vision_names(c: VisionConfig) -> dict[str, tuple[int, ...]]:
    """Pixtral's and the projector's tensors of a checkpoint of ``c``'s
    shape, by name, as the released checkpoints name them.
    """
    E, F, P, T = c.hidden_size, c.intermediate_size, c.patch_size, c.text_dim
    out = {
        "vision_tower.patch_conv.weight": (E, 3, P, P),
        "vision_tower.ln_pre.weight": (E,),
        "multi_modal_projector.norm.weight": (E,),
        "multi_modal_projector.patch_merger.merging_layer.weight": (
            E,
            E * c.merge**2,
        ),
        "multi_modal_projector.linear_1.weight": (T, E),
        "multi_modal_projector.linear_2.weight": (T, T),
    }
    for i in range(c.num_hidden_layers):
        p = f"vision_tower.transformer.layers.{i}"
        out |= {f"{p}.attention_norm.weight": (E,), f"{p}.ffn_norm.weight": (E,)}
        out |= {f"{p}.attention.{n}_proj.weight": (E, E) for n in "qkvo"}
        out |= {
            f"{p}.feed_forward.gate_proj.weight": (F, E),
            f"{p}.feed_forward.up_proj.weight": (F, E),
            f"{p}.feed_forward.down_proj.weight": (E, F),
        }
    return out


@pytest.fixture(scope="module")
def weights():
    text = {"language_model." + n: s for n, s in TestMinistral3.names().items()}
    return checkpoint(VLM, text | vision_names(VISION)).tree("random")


def hugging_face(weights) -> HuggingFaceMistral3:
    """transformers' Mistral 3 over ``weights``, imported only to record."""
    from iron.applications.ministral3.hugging_face import HuggingFaceMistral3

    text = TOY.to_json() | {"model_type": "ministral3"}
    return HuggingFaceMistral3.build("mistral3", VISION, weights, text_config=text)


class SoftTokens:
    """transformers' soft tokens of an image: ``logits``, as ``Golden``
    reads them.
    """

    def __init__(self, hf: HuggingFaceMistral3):
        self.hf = hf

    def logits(self, tokens, image):
        import torch

        with torch.no_grad():
            out = self.hf.model.get_image_features(**self.hf.pixels(image))
        return out.pooler_output[0].numpy()


def test_the_vision_tower_s_soft_tokens_match_transformers(golden, weights):
    """The tower's reference against transformers' soft tokens of an image
    resized to 3 by 4 soft tokens, within 5% of the largest one's
    magnitude, as a decoder's logits are held (measured 0.80%).
    """
    tower = VisionTower(VISION, weights)
    image = np.random.default_rng(1).integers(0, 256, (90, 120, 3), dtype=np.uint8)
    buffer, values = tower.inputs(image)
    assert (values["th"], values["tw"]) == (3, 4)
    got = np.asarray(tower.reference(buffer, **values), np.float32)
    got = got.reshape(-1, VISION.text_dim)[: values["nt"]]
    reference = golden(
        "soft_tokens", lambda: SoftTokens(hugging_face(weights)), VLM, weights
    )
    want = reference.logits([], image)
    err, scale = np.abs(got - want).max(), np.abs(want).max()
    assert err <= LOGITS * scale, f"|diff| {err:.4f} against |soft tokens| {scale:.3f}"


def test_the_image_s_soft_tokens_take_its_placeholders_across_a_chunk(golden, weights):
    """The tower's reference, then each chunk's, the image's placeholders
    and breaks laid out as the processor lays them, crossing the chunks'
    boundary, then a decode step, against transformers' logits.
    """
    model = Ministral3VLM(VLM, weights)
    reference = golden("small", lambda: hugging_face(weights), VLM, weights)
    rng = np.random.default_rng(2)
    image = rng.integers(0, 256, (90, 120, 3), dtype=np.uint8)
    placed = VISION.tokens(*image.shape[:2])
    tokens = rng.integers(VISION.end_token + 1, TOY.vocab_size, 300)
    tokens[250 : 250 + len(placed)] = placed
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


def test_an_image_s_placeholders_are_its_rows_of_soft_tokens_and_breaks():
    """3 rows of 4 soft tokens: each row ended by [IMG_BREAK], the last by
    [IMG_END].
    """
    row = [IMAGE] * 4
    want = [*row, 12, *row, 12, *row, 13]
    assert VISION.tokens(90, 120) == want


@pytest.mark.parametrize(
    "image,size",
    [
        # As PixtralImageProcessor resizes them at a longest edge of 1540
        # into 28-pixel soft tokens.
        ((480, 640), (504, 644)),
        ((375, 500), (392, 504)),
        ((3000, 4000), (1176, 1540)),
        ((1541, 700), (1540, 700)),
        ((1540, 1540), (1540, 1540)),
        ((10, 3000), (28, 1540)),
    ],
)
def test_the_resize_is_the_processor_s(image, size):
    """Within the longest edge at the image's aspect, truncated, then each
    side up to whole soft tokens.
    """
    vision = dataclasses.replace(VISION, longest_edge=1540)
    assert vision.size(*image) == size
