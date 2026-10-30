# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Gemma 4 in float32 with its processors.

What the goldens beside the checkpoint are recorded from. It needs
torch, torchvision and transformers, which are not IRON's
requirements, only to record.
"""

import numpy as np
import torch
import transformers

from iron.lm.golden import HuggingFace


class HuggingFaceGemma4(HuggingFace):
    """transformers' ``Gemma4ForConditionalGeneration`` in float32.

    With the checkpoint's image processor and feature extractor; the
    per-layer token table stays bfloat16 (a lookup widens it exactly,
    and its ``sqrt(256)`` scale is a power of two).
    """

    model_class = "AutoModelForImageTextToText"

    def __init__(self, model, processor):
        super().__init__(model)
        self.processor = processor

    @classmethod
    def load(cls, directory) -> "HuggingFaceGemma4":
        model = transformers.AutoModelForImageTextToText.from_pretrained(
            directory, dtype=torch.bfloat16
        )
        table = model.model.language_model.embed_tokens_per_layer
        for module in model.modules():
            if module is table:
                continue
            for p in module.parameters(recurse=False):
                p.data = p.data.float()
            for name, b in module.named_buffers(recurse=False):
                if b.is_floating_point():
                    module._buffers[name] = b.float()
        processor = transformers.AutoProcessor.from_pretrained(directory)
        return cls(model, processor)

    def logits(self, tokens, image, audio) -> np.ndarray:
        """Return the logits after ``tokens``, with ``image`` and ``audio`` at their placeholders.

        ``image`` is ``(height, width, 3)`` uint8, decoded; ``audio``
        is the mono 16 kHz clip; an empty array is none.
        """
        media = {}
        if image.size:
            out = self.processor.image_processor(
                torch.from_numpy(np.asarray(image)).permute(2, 0, 1),
                return_tensors="pt",
            )
            media |= dict(
                pixel_values=out["pixel_values"],
                image_position_ids=out["image_position_ids"],
            )
        if audio.size:
            out = self.processor.feature_extractor([audio], return_tensors="pt")
            media |= dict(
                input_features=out["input_features"],
                input_features_mask=out["input_features_mask"],
            )
        ids = torch.from_numpy(np.asarray(tokens, np.int64)[None])
        with torch.no_grad():
            out = self.model(input_ids=ids, use_cache=False, **media)
        return out.logits[0, -1].numpy()
