# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own SmolVLM in float32, what the goldens are recorded
from. It needs torch and transformers, which are not IRON's requirements,
only to record.
"""

import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.lm.golden import HuggingFace


class HuggingFaceVLM(HuggingFace):
    """transformers' own SmolVLM (``Idefics3ForConditionalGeneration``) in
    float32, built over both configs as ``HuggingFace.build("idefics3",
    vision, weights, **text.to_json())``.
    """

    model_class = "AutoModelForImageTextToText"

    def pixels(self, image):
        """The ``pixel_values`` of ``image``, as ``VisionTower.inputs``
        takes it, rounded to bfloat16 as the device holds it.
        """
        image = np.asarray(image).astype(bfloat16).astype(np.float32)
        return torch.from_numpy(image.transpose(2, 0, 1).copy())[None, None]

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
