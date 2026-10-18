# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Whisper in float32, what the tests' goldens are
recorded from. It needs torch and transformers, which are not IRON's
requirements, only to record.
"""

import numpy as np
import torch

from iron.lm.golden import HuggingFace


class HuggingFaceWhisper(HuggingFace):
    """transformers' ``WhisperForConditionalGeneration`` in float32, what
    records Whisper's goldens: the logits after the decoder's tokens over a
    clip's features, ``(num_mel_bins, frames)``.
    """

    model_class = "AutoModelForSpeechSeq2Seq"

    def logits(self, tokens, features) -> np.ndarray:
        with torch.no_grad():
            out = self.model(
                input_features=torch.from_numpy(np.asarray(features, np.float32))[None],
                decoder_input_ids=torch.tensor([list(tokens)]),
                use_cache=False,
            )
        return out.logits[0, -1].numpy()
