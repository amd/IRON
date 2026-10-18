#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct over ``iron.lm``: its text model (``SmolVLMText``,
a ``CausalLM`` of Llama's ``DecoderLayer``, 9 heads over 3 KV groups, with an untied
``lm_head``), its vision tower (``vision/``, an ``iron.lm.Tower``), and the
two as one ``iron.lm.Multimodal`` (``SmolVLM``), whose image
placeholders take the tower's soft tokens, judged by transformers' own
SmolVLM's logits (``hugging_face.py``). Its shape is read from the
checkpoint's own nested ``config.json``. ``python -m
iron.applications.idefics3.model`` runs the text model alone.

Its tunables at 576 wide, which the default tiles do not divide, are its
profile's: flm.ProjectionGEMM's ``tile_n`` 32 and ``k_tile`` 192, and a decode
step's residual ``ElementwiseAdd``'s ``tile_size`` 192.
"""

import dataclasses
from pathlib import Path


from iron import lm
from iron.lm import CausalLM, DecoderConfig, Multimodal
from iron.applications.idefics3.vision.model import VisionConfig, VisionTower


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


#: ``<|im_start|>``, the turn marker every prompt starts with.
BOS = 1


class SmolVLMText(CausalLM):
    """SmolVLM's text backbone on ``config``'s shape and a checkpoint's
    ``weights``, by its names: the decoder under ``model.text_model``, the
    untied ``lm_head`` at the root. Every matrix is read ``(out, in)``, as
    the checkpoint ships it. From its checkpoint and ``tokenizer.json``
    (text-only: no image input).
    """

    config = SmolVLMTextConfig
    profile = Path(__file__).with_name("profiles")
    bos = BOS

    def __init__(self, config, weights):
        super().__init__(config, weights, decoder=weights.model.text_model)

    @property
    def hugging_face(self):
        """transformers' SmolVLM, imported only where a golden is recorded."""
        from .hugging_face import HuggingFaceVLM

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


@dataclasses.dataclass(frozen=True)
class SmolVLMConfig(SmolVLMTextConfig):
    """``SmolVLMTextConfig`` and the vision tower's shape, ``vision``."""

    vision: VisionConfig | None = dataclasses.field(default=None, kw_only=True)

    @classmethod
    def from_checkpoint(cls, path) -> "SmolVLMConfig":
        text = super().from_checkpoint(path)
        return dataclasses.replace(text, vision=VisionConfig.from_checkpoint(path))


class SmolVLM(Multimodal):
    """SmolVLM-256M-Instruct, its text model and vision tower as one
    ``iron.lm.Multimodal``, from its checkpoint and ``tokenizer.json``.
    """

    config = SmolVLMConfig
    bos = BOS
    hugging_face = SmolVLMText.hugging_face

    def __init__(self, config: SmolVLMConfig, weights):
        self.config = config
        tower = VisionTower(config.vision, weights)
        super().__init__(
            SmolVLMText(config, weights), {config.vision.image_token: tower}
        )

    def cpu_reference(self):
        """What the model is judged by, its ``logits`` taking the tokens and
        the image: transformers' own SmolVLM, over the drawn weights, else
        its logits recorded beside the checkpoint.
        """
        if self.seed is None:
            return super().cpu_reference()
        return self.hugging_face.build(
            "idefics3", self.config.vision, self.text.weights, **self.config.to_json()
        )


if __name__ == "__main__":
    lm.main(SmolVLMText)
