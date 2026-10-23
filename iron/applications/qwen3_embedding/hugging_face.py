# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Qwen3-Embedding in float32, what its golden is
recorded from. It needs torch and transformers, which are not IRON's
requirements, only to record.
"""

import numpy as np
import torch

from iron.lm.golden import HuggingFace


class LastHidden(HuggingFace):
    """transformers' Qwen3 model without its head: the last token's final
    hidden state, unit length.
    """

    model_class = "AutoModel"

    def logits(self, tokens) -> np.ndarray:
        with torch.no_grad():
            out = self.model(torch.tensor([list(tokens)]), use_cache=False)
        last = out.last_hidden_state[0, -1].numpy()
        return last / np.linalg.norm(last)
