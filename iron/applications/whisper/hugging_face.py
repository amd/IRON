# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Whisper in float32, what the tests' goldens are
recorded from. It needs torch and transformers, which are not IRON's
requirements, only to record.
"""

import numpy as np
import torch
import transformers

from iron.lm.golden import HuggingFace


class HuggingFaceWhisper(HuggingFace):
    """transformers' ``WhisperForConditionalGeneration`` in float32, what
    records Whisper's goldens: the logits after the decoder's tokens over a
    clip's samples, through its ``WhisperFeatureExtractor``.
    """

    model_class = "AutoModelForSpeechSeq2Seq"

    def features(self, audio) -> np.ndarray:
        """The extractor's ``input_features`` of ``audio``, ``(num_mel_bins,
        frames)``, its clip two frames a position of a hop of 160 samples.
        """
        c = self.model.config
        extractor = transformers.WhisperFeatureExtractor(
            feature_size=c.num_mel_bins, chunk_length=c.max_source_positions // 50
        )
        out = extractor(np.asarray(audio, np.float32), sampling_rate=16000)
        return out.input_features[0]

    def logits(self, tokens, audio) -> np.ndarray:
        with torch.no_grad():
            out = self.model(
                input_features=torch.from_numpy(self.features(audio))[None],
                decoder_input_ids=torch.tensor([list(tokens)]),
                use_cache=False,
            )
        return out.logits[0, -1].numpy()
