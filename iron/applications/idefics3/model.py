#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct over ``iron.lm``: its text model (``SmolVLMText``,
a ``CausalLM`` of Llama's ``DecoderLayer``, 9 heads over 3 KV groups, with an untied
``lm_head``), its vision tower (``vision/``, an ``iron.lm.Tower``), and the
two as one ``iron.lm.Multimodal`` (``VLMRunner.npu``), whose image
placeholders take the tower's soft tokens, judged by transformers' own
SmolVLM's logits (``Reference``). Its shape is read from the
checkpoint's own nested ``config.json``. ``python -m
iron.applications.idefics3.model`` runs the text model alone.

Its tunables at 576 wide, which the default tiles do not divide, are its
profile's: flm.GEMM's ``tile_n`` 32 and ``k_tile`` 192, and a decode
step's residual ``ElementwiseAdd``'s ``tile_size`` 192.
"""

import dataclasses
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron import lm
from iron.lm import CausalLM, DecoderConfig, Multimodal
from iron.lm.golden import flat, config_json
from iron.applications.idefics3.vision.model import VisionConfig, VisionTower
from iron.tune.narrowing import CostTable, JointNarrowing, NarrowingKinds


@dataclasses.dataclass(frozen=True)
class SmolVLMTextConfig(DecoderConfig):
    """SmolVLM's text backbone's shape, from the checkpoint's nested
    ``text_config``.
    """

    vocab_size: int = dataclasses.field(metadata={"json": "text_config.vocab_size"})
    hidden_size: int = dataclasses.field(metadata={"json": "text_config.hidden_size"})
    num_hidden_layers: int = dataclasses.field(
        metadata={"json": "text_config.num_hidden_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        metadata={"json": "text_config.num_attention_heads"}
    )
    num_key_value_heads: int = dataclasses.field(
        metadata={"json": "text_config.num_key_value_heads"}
    )
    head_dim: int | None = dataclasses.field(
        default=None, kw_only=True, metadata={"json": "text_config.head_dim"}
    )
    intermediate_size: int = dataclasses.field(
        metadata={"json": "text_config.intermediate_size"}
    )
    rope_theta: float = dataclasses.field(metadata={"json": "text_config.rope_theta"})
    eps: float = dataclasses.field(
        default=1e-5, kw_only=True, metadata={"json": "text_config.rms_norm_eps"}
    )
    max_seq_len: int = dataclasses.field(
        metadata={"json": "text_config.max_position_embeddings"}
    )
    tie_word_embeddings: bool = dataclasses.field(
        default=False, metadata={"json": "tie_word_embeddings"}
    )


class SmolVLMText(CausalLM):
    """SmolVLM's text backbone on ``config``'s shape and a checkpoint's
    ``weights``, by its names: the decoder under ``model.text_model``, the
    untied ``lm_head`` at the root. Every matrix is read ``(out, in)``, as
    the checkpoint ships it.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, config, weights):
        super().__init__(config, weights, decoder=weights.model.text_model)


#: ``<|im_start|>``, the turn marker every prompt starts with.
BOS = 1


class Runner(lm.Runner):
    """SmolVLM-256M-Instruct's text backbone, from its checkpoint and
    ``tokenizer.json`` (text-only: no image input yet).
    """

    config = SmolVLMTextConfig
    model = SmolVLMText
    bos = BOS

    @property
    def hugging_face(self):
        # No AutoModelForCausalLM loads SmolVLM's checkpoint.
        return HuggingFaceVLM


# The real processor's own ids either side of an image and its question
# ("<|im_start|>User:<image>{question}<end_of_utterance>\nAssistant:", one
# image, no splitting), read off Idefics3Processor's output.
_PREAMBLE_IDS = [1, 11126, 42, 49189, 49152]
_SUFFIX_IDS = [49189]
_TAIL_IDS = [49279, 198, 9519, 9531, 42]


def build_prompt(question: list[int], vision: VisionConfig) -> list[int]:
    """The token ids of one unsplit image, first in the turn, then the
    ``question``'s ids, as the real processor lays them out: the image a run
    of ``vision.image_token`` placeholders, one per soft token.
    """
    image = [vision.image_token] * vision.tokens
    return _PREAMBLE_IDS + image + _SUFFIX_IDS + question + _TAIL_IDS


class HuggingFaceVLM:
    """transformers' own SmolVLM (``Idefics3ForConditionalGeneration``) in
    float32: a checkpoint directory's (``load``) or one built from IRON's
    configs over a weights tree (``build``). It takes what a ``Golden`` is
    keyed by: a sequence's tokens, then, if they hold image placeholders,
    the image's bfloat16 bits (``Reference``).
    """

    def __init__(self, model):
        self.model = model.eval()

    @classmethod
    def load(cls, directory) -> "HuggingFaceVLM":
        import torch
        import transformers

        return cls(
            transformers.Idefics3ForConditionalGeneration.from_pretrained(
                directory, dtype=torch.float32
            )
        )

    @classmethod
    def build(cls, text, vision: VisionConfig, weights) -> "HuggingFaceVLM":
        """The model of ``text``'s and ``vision``'s fields as ``config.json``
        names them, over ``weights``, every parameter of which it holds.
        """
        import torch
        import transformers

        hf = transformers.Idefics3Config(**(config_json(vision) | config_json(text)))
        model = transformers.Idefics3ForConditionalGeneration(hf).float()
        model.load_state_dict({k: torch.from_numpy(v) for k, v in flat(weights)})
        return cls(model)

    def pixels(self, bits):
        """The ``pixel_values`` of one image's bfloat16 ``bits``, laid out
        as ``VisionTower.inputs`` takes the image, ``(side, side, 3)``.
        """
        import torch

        S = self.model.config.vision_config.image_size
        image = np.asarray(bits, np.uint16).view(bfloat16).astype(np.float32)
        image = image.reshape(S, S, 3).transpose(2, 0, 1)
        return torch.from_numpy(image.copy())[None, None]

    def logits(self, key) -> np.ndarray:
        """The logits after a sequence's last token, its image at its
        placeholders, from ``key``.
        """
        import torch

        config, n, pixels = self.model.config, key.size, None
        if (key == config.image_token_id).any():
            n -= 3 * config.vision_config.image_size**2
            pixels = self.pixels(key[n:])
        with torch.no_grad():
            out = self.model(
                input_ids=torch.from_numpy(key[None, :n]),
                pixel_values=pixels,
                use_cache=False,
            )
        return out.logits[0, -1].numpy()


class Reference:
    """SmolVLM's logits as ``model`` gives them for a key of the tokens and
    the image's bfloat16 bits (a ``Golden`` or a ``HuggingFaceVLM``), taken
    as ``Multimodal.logits`` takes them.
    """

    def __init__(self, model, image_token: int):
        self.model = model
        self.image_token = image_token

    def logits(self, tokens, raw: dict[int, tuple]) -> np.ndarray:
        """The logits after ``tokens``, the one image ``raw`` holds (by
        placeholder token) at its placeholders.
        """
        (image,) = raw[self.image_token]
        bits = np.asarray(image).astype(bfloat16).view(np.uint16)
        return self.model.logits(np.concatenate([np.ravel(tokens), bits.ravel()]))


class VLMRunner(Runner):
    """SmolVLM-256M-Instruct, its text model and vision tower as one
    ``iron.lm.Multimodal``, from its checkpoint and ``tokenizer.json``.
    """

    def __init__(self, weights_path, tokenizer_path=None, config=None, seed=None):
        super().__init__(weights_path, tokenizer_path, config, seed)
        self.vision_config = VisionConfig.from_checkpoint(weights_path)

    def npu(self, cost_table=None, full_elf=None, kinds=None) -> Multimodal:
        text = SmolVLMText(self.config, self.weights)
        tower = VisionTower(self.vision_config, self.weights)
        model = Multimodal(text, {self.vision_config.image_token: tower})
        tuner = (
            None
            if cost_table is None
            else JointNarrowing(CostTable(cost_table), kinds=kinds or NarrowingKinds())
        )
        return model.load(
            release=self.checkpoint.release, tuner=tuner, full_elf=full_elf
        )

    def reference(self) -> Reference:
        """What the model is judged by: transformers' own SmolVLM, over the
        drawn weights, else its logits recorded beside the checkpoint.
        """
        vision = self.vision_config
        if self.seed is not None:
            model = HuggingFaceVLM.build(self.config, vision, self.weights)
        else:
            model = super().reference()
        return Reference(model, vision.image_token)


if __name__ == "__main__":
    lm.main(Runner, "SmolVLM-256M-Instruct's text backbone on the NPU")
