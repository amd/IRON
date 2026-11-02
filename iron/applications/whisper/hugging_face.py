# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own Whisper in float32.

What the goldens beside the checkpoint and the reference tests are
recorded from. Needs torch and transformers only when recording or
running ``--check-reference``.
"""

# torch, transformers and safetensors: only recording imports them.
# pyright: reportMissingImports=false

import copy
from typing import Any, cast

import numpy as np
import torch
from transformers import WhisperTimeStampLogitsProcessor

from iron.lm.golden import HuggingFace


class HuggingFaceWhisper(HuggingFace):
    """transformers' ``WhisperForConditionalGeneration`` in float32."""

    model_class = "WhisperForConditionalGeneration"

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
        """Greedy-decode one 30 s window ``mel`` ``(frames, mels)`` under ``policy``."""
        features = np.ascontiguousarray(np.asarray(mel, dtype=np.float32).T)[None]
        timestamp_rules = None
        if policy.timestamps:
            config = copy.deepcopy(self.model.generation_config)
            config.no_timestamps_token_id = 50363
            config.max_initial_timestamp_index = 50
            timestamp_rules = WhisperTimeStampLogitsProcessor(
                config, begin_index=len(prompt)
            )
        with torch.no_grad():
            encoder_out = self.model.model.encoder(torch.from_numpy(features))
            hidden = encoder_out.last_hidden_state
            past = None
            ids = list(prompt)
            generated: list[int] = []
            while True:
                out = self.model(
                    encoder_outputs=(hidden,),
                    decoder_input_ids=torch.tensor([ids], dtype=torch.long),
                    past_key_values=past,
                    use_cache=True,
                )
                past = out.past_key_values
                scores = out.logits[:, -1].clone()
                scores[:, policy.suppress] = -torch.inf
                for lo, hi in policy.ranges(generated):
                    scores[:, lo:hi] = -torch.inf
                if timestamp_rules is not None:
                    scores = timestamp_rules(
                        cast(
                            torch.LongTensor,
                            torch.tensor([prompt + generated], dtype=torch.long),
                        ),
                        scores,
                    )
                token = int(scores.argmax())
                generated.append(token)
                if token == policy.eos or len(generated) >= policy.max_new_tokens:
                    return generated, hidden[0].numpy()
                ids = [token]
