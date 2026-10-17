# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Gemma 4 text model in float32, which the tests check
the float32 oracle against. It needs torch and transformers, which are not
IRON's requirements, so the tests that use it skip where they are not
installed.
"""

from pathlib import Path

import numpy as np
import torch
import transformers
from safetensors import safe_open
from transformers.models.gemma4 import modeling_gemma4

# Where the multimodal checkpoint keeps the text model.
PREFIX = "model.language_model."


class HuggingFace:
    """Hugging Face's Gemma 4 text model over the checkpoint in
    `directory`, its weights float32 but the per-layer table's, held bf16:
    the model scales a row of it by 16 in bf16, exactly, and adds it in
    float32, so it reads as a float32 table would, at half the memory.

    Args:
        directory: The checkpoint directory, as Hugging Face loads it.

    Raises:
        ValueError: The checkpoint lacks a weight the model reads.
    """

    def __init__(self, directory):
        directory = Path(directory)
        config = transformers.AutoConfig.from_pretrained(directory).text_config
        config._attn_implementation = "eager"
        with torch.device("meta"):
            model = modeling_gemma4.Gemma4ForCausalLM(config)
        held = model.state_dict()
        state = {}
        with safe_open(directory / "model.safetensors", framework="pt") as f:
            for name in f.keys():
                key = "model." + name.removeprefix(PREFIX)
                if not name.startswith(PREFIX) or key not in held:
                    continue
                t = f.get_tensor(name)
                table = key == "model.embed_tokens_per_layer.weight"
                state[key] = t if table else t.float()
        missing, _ = model.load_state_dict(state, strict=False, assign=True)
        if missing != ["lm_head.weight"]:
            raise ValueError(f"the checkpoint lacks {missing}")
        model.lm_head.weight = model.model.embed_tokens.weight
        # The buffers the checkpoint does not hold.
        model.model.rotary_emb = modeling_gemma4.Gemma4TextRotaryEmbedding(config)
        for e in (model.model.embed_tokens, model.model.embed_tokens_per_layer):
            e.embed_scale = torch.tensor(e.scalar_embed_scale)
        self.model = model.eval()

    def logits(self, tokens) -> np.ndarray:
        """The logits after each of `tokens`, `(len(tokens), vocab)` float32."""
        with torch.no_grad():
            out = self.model(torch.tensor([list(tokens)]), use_cache=False)
        return out.logits[0].numpy()
