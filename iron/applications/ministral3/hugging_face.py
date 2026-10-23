# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Mistral 3 in float32 and its image processor, what
the goldens are recorded from. It needs torch and transformers, which are
not IRON's requirements, only to record.
"""

import numpy as np
import torch
from transformers import AutoImageProcessor, PixtralImageProcessor

from iron.lm.golden import HuggingFace


class HuggingFaceMistral3(HuggingFace):
    """transformers' own Mistral 3 (``Mistral3ForConditionalGeneration``)
    in float32, which runs text alone too: transformers maps no causal
    model to a ``mistral3`` checkpoint. Built over the vision config as
    ``HuggingFace.build("mistral3", vision, weights, text_config=...)``,
    its image processor then one of that config's.
    """

    model_class = "AutoModelForImageTextToText"

    # None only where ``HuggingFace.load`` and ``build`` make one, which
    # this class's own wrap in one that has it.
    def __init__(self, model, processor: PixtralImageProcessor | None = None):
        super().__init__(model)
        self.processor = processor

    @classmethod
    def load(cls, directory) -> "HuggingFaceMistral3":
        processor = AutoImageProcessor.from_pretrained(directory)
        return cls(super().load(directory).model, processor)

    @classmethod
    def build(cls, model_type: str, config, weights, **json) -> "HuggingFaceMistral3":
        processor = PixtralImageProcessor(
            size={"longest_edge": config.longest_edge},
            image_mean=list(config.image_mean),
            image_std=list(config.image_std),
        )
        hf = super().build(
            model_type, config, weights, multimodal_projector_bias=False, **json
        )
        return cls(hf.model, processor)

    def pixels(self, image) -> dict:
        """The processor's ``pixel_values`` and ``image_sizes`` of a decoded
        ``image``, ``(height, width, 3)`` uint8, each side resized to whole
        soft tokens.
        """
        c = self.model.config
        block = c.vision_config.patch_size * c.spatial_merge_size
        out = self.processor(
            images=[np.asarray(image)],
            patch_size={"height": block, "width": block},
            return_tensors="pt",
            input_data_format="channels_last",
        )
        return {k: out[k] for k in ("pixel_values", "image_sizes")}

    def logits(self, tokens, *image) -> np.ndarray:
        """The logits after the last of ``tokens``, ``image``, if given, at
        its placeholders: the head of the last position alone, which past 16k
        tokens keeps the forward within a host's memory.
        """
        with torch.no_grad():
            out = self.model(
                input_ids=torch.tensor([list(tokens)]),
                use_cache=False,
                logits_to_keep=1,
                **(self.pixels(*image) if image else {}),
            )
        return out.logits[0, -1].numpy()
