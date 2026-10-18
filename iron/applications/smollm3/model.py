#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM3 3B on the shared decoder (``iron.lm``), its shape read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.smollm3.model``.

SmolLM3 is Llama's layer, but every fourth layer turns nothing by RoPE
(NoPE): ``no_rope_layers[i]`` is 0 where layer ``i`` attends without
positions. Its output head is the input embedding, tied.
"""

import dataclasses

from iron import lm
from iron.lm import CausalLM, DecoderConfig


@dataclasses.dataclass(frozen=True)
class SmolLM3Config(DecoderConfig):
    """``DecoderConfig`` and which layers turn q and k by RoPE."""

    no_rope_layers: tuple[int, ...] = dataclasses.field(
        kw_only=True, metadata={"convert": tuple}
    )


class SmolLM3(CausalLM):
    """SmolLM3 on ``config``'s shape and a checkpoint's ``weights``, from
    its checkpoint and ``tokenizer.json``.
    """

    config = SmolLM3Config

    def __init__(self, config: SmolLM3Config, weights):
        super().__init__(config, weights)
        for layer, rope in zip(self.layers, config.no_rope_layers):
            if not rope:
                layer.rope = None


if __name__ == "__main__":
    lm.main(SmolLM3)
