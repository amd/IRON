# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Whisper in float32.

What the goldens beside the checkpoint and the reference tests are
recorded from. Needs torch and transformers only when recording or
running ``--check-reference``.
"""

# torch, transformers and safetensors: optional, only reference paths import them.
# pyright: reportMissingImports=false

import copy
from typing import Any

import numpy as np
import torch
from transformers import WhisperFeatureExtractor

from iron.lm.golden import HuggingFace


class HuggingFaceWhisper(HuggingFace):
    """transformers' ``WhisperForConditionalGeneration`` in float32."""

    model_class = "WhisperForConditionalGeneration"

    def __init__(self, model, feature_extractor=None):
        super().__init__(model)
        self.feature_extractor = feature_extractor

    @classmethod
    def load(cls, directory):
        """Load the float32 model and its independent audio feature extractor."""
        import transformers

        model = getattr(transformers, cls.model_class).from_pretrained(
            directory, dtype=torch.float32
        )
        return cls(model, WhisperFeatureExtractor.from_pretrained(directory))

    def features(self, waveform: np.ndarray, *, long_form: bool = False) -> np.ndarray:
        """Extract HF Whisper log-Mel features ``(frames, mels)`` from raw audio."""
        if self.feature_extractor is None:
            raise RuntimeError(
                "HuggingFaceWhisper.features requires a loaded checkpoint"
            )
        samples = np.asarray(waveform, dtype=np.float32).reshape(-1)
        if long_form:
            samples = np.pad(samples, (0, 30 * 16000))
            extracted = self.feature_extractor(
                samples,
                sampling_rate=16000,
                padding="do_not_pad",
                truncation=False,
                return_tensors="np",
            )
        else:
            extracted = self.feature_extractor(
                samples, sampling_rate=16000, return_tensors="np"
            )
        return np.asarray(extracted.input_features[0].T, dtype=np.float32)

    def encode(self, mel: np.ndarray) -> np.ndarray:
        """Return the float32 encoder hidden state ``(frames // 2, hidden_size)`` for ``mel``.

        Args:
            mel: ``(frames, num_mel_bins)`` float32 log-Mel features.
        """
        features = np.asarray(mel, dtype=np.float32)
        if features.ndim == 2:
            features = np.ascontiguousarray(features.T)[None]
        with torch.no_grad():
            out = self.model.model.encoder(torch.from_numpy(features))
        return out.last_hidden_state[0].numpy()

    def logits(self, tokens, *arrays: Any, **kwargs: Any) -> np.ndarray:
        """Return the float32 logits after ``tokens`` given ``mel`` in ``arrays``."""
        if not arrays:
            raise ValueError(
                "HuggingFaceWhisper.logits requires a mel spectrogram array"
            )
        mel = np.asarray(arrays[0], dtype=np.float32)
        if mel.ndim == 2:
            mel = np.ascontiguousarray(mel.T)[None]
        ids = torch.tensor([list(tokens)], dtype=torch.long)
        with torch.no_grad():
            out = self.model(
                input_features=torch.from_numpy(mel),
                decoder_input_ids=ids,
                use_cache=False,
            )
        return out.logits[0, -1].numpy()

    def window(
        self, mel: np.ndarray, prompt: list[int], policy
    ) -> tuple[list[int], np.ndarray]:
        """Return HF's generated continuation for one window using its own processors."""
        features = np.ascontiguousarray(np.asarray(mel, dtype=np.float32).T)[None]
        config = copy.deepcopy(self.model.generation_config)
        config.eos_token_id = policy.eos
        config.decoder_start_token_id = policy.prompt[0]
        config.no_timestamps_token_id = policy.config.no_timestamps_token_id
        config.max_initial_timestamp_index = policy.max_initial_timestamp
        config.suppress_tokens = policy.suppress
        config.begin_suppress_tokens = policy.begin_suppress
        config.forced_decoder_ids = None
        if hasattr(config, "language"):
            config.language = None
        if hasattr(config, "task"):
            config.task = None
        with torch.no_grad():
            output = self.model.generate(
                input_features=torch.from_numpy(features),
                decoder_input_ids=torch.tensor([prompt], dtype=torch.long),
                generation_config=config,
                max_new_tokens=policy.max_new_tokens,
                do_sample=False,
                return_timestamps=policy.timestamps,
                force_unique_generate_call=True,
                return_dict_in_generate=True,
            )
            hidden = self.model.model.encoder(torch.from_numpy(features))
        tokens = output.sequences[0, len(prompt) :].tolist()
        if tokens and tokens[-1] == policy.eos:
            tokens.pop()
        return (
            tokens,
            hidden.last_hidden_state[0].numpy(),
        )
