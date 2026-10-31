# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A small Llama with a tower on its image placeholder.

And Hugging Face's logits for it.
"""

import dataclasses

import numpy as np
from ml_dtypes import bfloat16

from iron import Scratchpad
from iron.applications.llama.model import Llama
from iron.lm import Multimodal, Tower
from iron.lm.golden import HuggingFace
from iron.operators.copy import Copy
from iron.tests.support.llama_model import PROFILE, SMALL, checkpoint


@dataclasses.dataclass(frozen=True)
class Width:
    hidden_size: int
    text_dim: int
    num_hidden_layers: int = 0


class Features(Tower):
    """A tower whose soft tokens are the rows it is given."""

    def __init__(self, width: int, rows: int):
        super().__init__(Width(width, width), rows, rows)

    def front(self, features, *, rows):
        return Copy.step(features)[:rows], None

    def head(self, x):
        return x

    def inputs(self, features) -> tuple[np.ndarray, dict]:
        buffer = np.zeros((self.max_tokens, self.config.hidden_size), bfloat16)
        buffer[: len(features)] = features
        return buffer, dict(rows=len(features))

    def shapes(self) -> list[dict]:
        return [dict(features=((self.max_tokens, self.config.hidden_size), bfloat16))]

    def body(self, features, *, rows: Scratchpad[np.int32]):
        x, angles = self.front(features, rows=rows)
        return self.forward(x, rows, angles)


IMAGE = SMALL.vocab_size - 1


class Placed(HuggingFace):
    """Hugging Face's Llama with ``soft`` at its image placeholders.

    The logits after a sequence's tokens.
    """

    def logits(self, tokens, soft) -> np.ndarray:
        import torch  # records a golden only: not a requirement

        tokens = torch.from_numpy(np.asarray(tokens))
        with torch.no_grad():
            x = self.model.model.embed_tokens(tokens)
            x[tokens == IMAGE] = torch.from_numpy(soft.astype(np.float32))
            out = self.model(inputs_embeds=x[None], use_cache=False)
        return out.logits[0, -1].numpy()


def small_causal(golden):
    """Build a small Llama over chunks of 256 of 1024 positions, a tower on its image placeholder.

    Hugging Face's logits for it (``reference(tokens, soft)``, from
    ``goldens/multimodal.npz``), and a prompt whose run of 16 soft tokens
    crosses its first chunk's end.
    """
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    weights = checkpoint(config).tree("random")
    text = Llama(config, weights)
    text.profile = PROFILE
    model = Multimodal(text, {IMAGE: Features(config.hidden_size, 64)})
    model.profile = PROFILE
    rng = np.random.default_rng(8)
    tokens = rng.integers(0, IMAGE, 300)
    tokens[250:266] = IMAGE
    soft = (rng.standard_normal((16, config.hidden_size)) / 8).astype(bfloat16)

    hf = golden(
        "multimodal", lambda: Placed.build("llama", config, weights), config, weights
    )
    return model, hf.logits, tokens, soft
