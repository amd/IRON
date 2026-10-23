# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own SmolVLM in float32 and its image processor, what the
goldens are recorded from. It needs torch and transformers, which are not
IRON's requirements, only to record.
"""

import numpy as np
import torch
from ml_dtypes import bfloat16
from transformers import AutoImageProcessor, Idefics3ImageProcessor
from transformers.image_utils import PILImageResampling

from iron.lm.golden import HuggingFace


class HuggingFaceVLM(HuggingFace):
    """transformers' own SmolVLM (``Idefics3ForConditionalGeneration``) in
    float32, built over both configs as ``HuggingFace.build("idefics3",
    vision, weights, **text.to_json())``, and its image processor: the
    checkpoint's, or for a built model one of the vision config's sizes and
    splitting.
    """

    model_class = "AutoModelForImageTextToText"

    # None only where ``HuggingFace.load`` and ``build`` make one, which
    # this class's own wrap in one that has it.
    def __init__(self, model, processor: Idefics3ImageProcessor | None = None):
        super().__init__(model)
        self.processor = processor

    @classmethod
    def load(cls, directory) -> "HuggingFaceVLM":
        processor = AutoImageProcessor.from_pretrained(directory)
        return cls(super().load(directory).model, processor)

    @classmethod
    def build(cls, model_type: str, config, weights, **json) -> "HuggingFaceVLM":
        processor = Idefics3ImageProcessor(
            do_image_splitting=config.do_image_splitting,
            size={"longest_edge": config.longest_edge},
            max_image_size={"longest_edge": config.image_size},
            resample=PILImageResampling.LANCZOS,
            image_mean=list(config.image_mean),
            image_std=list(config.image_std),
        )
        hf = super().build(model_type, config, weights, **json)
        return cls(hf.model, processor)

    def pixels(self, image):
        """The processor's ``pixel_values`` of a decoded ``image``,
        ``(height, width, 3)`` uint8, a frame each, rounded to bfloat16 as
        the device holds them.
        """
        out = self.processor(
            images=[np.asarray(image)],
            return_tensors="pt",
            input_data_format="channels_last",
        )
        values = out["pixel_values"].numpy().astype(bfloat16).astype(np.float32)
        return torch.from_numpy(values)

    def logits(self, tokens, *image) -> np.ndarray:
        """The logits after ``tokens``, ``image``, if given, at its
        placeholders.
        """
        with torch.no_grad():
            out = self.model(
                input_ids=torch.from_numpy(np.asarray(tokens, np.int64)[None]),
                pixel_values=self.pixels(*image) if image else None,
                use_cache=False,
            )
        return out.logits[0, -1].numpy()
