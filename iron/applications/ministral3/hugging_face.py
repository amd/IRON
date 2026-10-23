# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Mistral 3 in float32, what the goldens are recorded
from. It needs torch and transformers, which are not IRON's requirements,
only to record.
"""

import numpy as np
import torch

from iron.lm.golden import HuggingFace


class HuggingFaceMistral3(HuggingFace):
    """transformers' own Mistral 3 (``Mistral3ForConditionalGeneration``)
    in float32, which runs text alone too: transformers maps no causal
    model to a ``mistral3`` checkpoint.
    """

    model_class = "AutoModelForImageTextToText"

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, float32: the head of the
        last position alone, which past 16k tokens keeps the forward within
        a host's memory.
        """
        with torch.no_grad():
            out = self.model(
                input_ids=torch.tensor([list(tokens)]),
                use_cache=False,
                logits_to_keep=1,
            )
        return out.logits[0, -1].numpy()
