# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM3 3B on the shared decoder (``iron.lm``), its shape read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.smollm3.model``.

SmolLM3 is Llama's layer, but it skips RoPE on every fourth layer (NoPE):
``no_rope_layers[i]`` is 0 where layer ``i`` attends without positions.
Its output head is the input embedding, tied.
"""

import dataclasses
from pathlib import Path

from iron import Precision, lm
from iron.lm import CausalLM, DecoderConfig, not_json


@dataclasses.dataclass(frozen=True)
class SmolLM3Config(DecoderConfig):
    """``DecoderConfig``, which layers turn q and k by RoPE, and every
    projection's ``precision``: ``Precision.HIGH``, as 3B's other dense
    decoder (Llama 3.2 3B) and Granite 4.2 3B are.
    """

    no_rope_layers: tuple[int, ...] = dataclasses.field(
        kw_only=True, metadata={"convert": tuple}
    )
    precision: Precision = lm.not_json(Precision.HIGH, kw_only=True)
    # The down projection's K = 11008 = 43 x 256 leaves B one memtile slot,
    # and a bounded call's ring passes must fit one queue push of 256.
    prefill_chunk: int = not_json(1024)

    def __post_init__(self):
        super().__post_init__()
        if len(self.no_rope_layers) != self.num_hidden_layers:
            raise ValueError(
                f"SmolLM3Config: {len(self.no_rope_layers)} no_rope_layers for "
                f"{self.num_hidden_layers} layers"
            )


class SmolLM3(CausalLM):
    """SmolLM3 on ``config``'s shape and a checkpoint's ``weights``, from
    its checkpoint and ``tokenizer.json``.
    """

    config = SmolLM3Config
    profile = Path(__file__).with_name("profiles")

    def __init__(self, config: SmolLM3Config, weights):
        super().__init__(config, weights)
        for layer, rope in zip(self.layers, config.no_rope_layers):
            if not rope:
                layer.rope = None


if __name__ == "__main__":
    lm.main(SmolLM3)
