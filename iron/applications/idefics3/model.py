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


from iron import Precision, lm
from iron.lm import CausalLM, DecoderConfig, Multimodal, not_json, subtree
from iron.applications.idefics3.vision.model import VisionConfig, VisionTower


@dataclasses.dataclass(frozen=True)
class SmolVLMTextConfig(DecoderConfig):
    """SmolVLM's text backbone's shape, from the checkpoint's nested
    ``text_config``.
    """

    precision: Precision = not_json(Precision.MEDIUM, kw_only=True)
    json_prefix = "text_config."

    eps: float = dataclasses.field(
        default=1e-5, kw_only=True, metadata={"json": "rms_norm_eps"}
    )
    tie_word_embeddings: bool = False


class SmolVLMText(CausalLM):
    """SmolVLM's text backbone on ``config``'s shape and a checkpoint's
    ``weights``, by its names: the decoder under ``model.text_model``, the
    untied ``lm_head`` at the root. Every matrix is read ``(out, in)``, as
    the checkpoint ships it. From its checkpoint and ``tokenizer.json``
    (text-only: no image input).
    """

    config = SmolVLMTextConfig
    profile = Path(__file__).with_name("profiles")

    def __init__(self, config, weights):
        text = subtree(weights, model=weights.model.text_model, lm_head=weights.lm_head)
        super().__init__(config, text)

    @property
    def hugging_face(self):
        """transformers' SmolVLM, imported only where a golden is recorded."""
        from .hugging_face import HuggingFaceVLM

        return HuggingFaceVLM


# The real processor's own ids ("<|im_start|>User:<image>{question}
# <end_of_utterance>\nAssistant:", one image), read off Idefics3Processor's
# output: the turn's opening, its close, the markers around each frame's
# placeholders, the first of the squares' row and column markers
# (<row_1_col_1>, of six by six), and the line after each row of squares,
# the last row's and the whole image's one token.
_USER_IDS = [1, 11126, 42]
_TAIL_IDS = [49279, 198, 9519, 9531, 42]
_FAKE, _GLOBAL, _ROW_COL, _LINE, _LINES = 49189, 49152, 49153, 198, 1116


def build_prompt(
    question: list[int], vision: VisionConfig, rows: int = 0, columns: int = 0
) -> list[int]:
    """The token ids of one image first in the turn, then the
    ``question``'s ids, as the real processor lays them out: each of
    ``rows`` by ``columns`` squares (``VisionConfig.grid``) a run of
    ``vision.image_token`` placeholders, one per soft token, after its row
    and column's marker, a line after each row, then the whole image's run.
    """
    run = [vision.image_token] * vision.tokens
    image = []
    for r in range(rows):
        for k in range(columns):
            image += [_FAKE, _ROW_COL + 6 * r + k, *run]
        image.append(_LINE)
    if rows:
        image[-1] = _LINES
    image += [_FAKE, _GLOBAL, *run, _FAKE]
    return _USER_IDS + image + question + _TAIL_IDS


@dataclasses.dataclass(frozen=True)
class SmolVLMConfig(SmolVLMTextConfig):
    """``SmolVLMTextConfig`` and the vision tower's shape, ``vision``."""

    vision: VisionConfig | None = not_json(None, kw_only=True)

    @classmethod
    def from_checkpoint(cls, path) -> "SmolVLMConfig":
        text = super().from_checkpoint(path)
        return dataclasses.replace(text, vision=VisionConfig.from_checkpoint(path))


class SmolVLM(Multimodal):
    """SmolVLM-256M-Instruct, its text model and vision tower as one
    ``iron.lm.Multimodal``, from its checkpoint and ``tokenizer.json``.
    """

    config = SmolVLMConfig
    hugging_face = SmolVLMText.hugging_face

    def __init__(self, config: SmolVLMConfig, weights):
        self.config, self.weights = config, weights
        tower = VisionTower(config.vision, weights)
        super().__init__(
            SmolVLMText(config, weights), {config.vision.image_token: tower}
        )

    def cpu_reference(self):
        """What the model is judged by, its ``logits`` taking the tokens and
        the image: transformers' own SmolVLM, over the drawn weights, else
        its logits recorded beside the checkpoint.
        """
        if self.random_weights is None:
            return super().cpu_reference()
        return self.hugging_face.build(
            "idefics3", self.config.vision, self.weights, **self.config.to_json()
        )


if __name__ == "__main__":
    lm.main(SmolVLMText)
