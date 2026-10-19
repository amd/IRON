# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What records LogMel's goldens."""

import numpy as np
from ml_dtypes import bfloat16

# The frames the goldens keep.
EVERY = 8


class Extractor:
    """transformers' ``Gemma4AudioFeatureExtractor``, what records a
    golden: every ``EVERY``th frame's features of a float32 wave, rounded
    once to bf16.
    """

    def logits(self, tokens, wave):
        import transformers

        # The extractor's first frame is centred on the wave's start, a half
        # frame of zeros before it, so its frame f + 1 is LogMel's f; the
        # zero after completes the last.
        wave = np.append(wave, np.float32(0))
        extractor = transformers.Gemma4AudioFeatureExtractor()
        features, _ = extractor._extract_spectrogram(wave, np.ones(wave.size, bool))
        return features[1::EVERY].astype(bfloat16).astype(np.float32)
