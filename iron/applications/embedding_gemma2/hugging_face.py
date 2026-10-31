# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own EmbeddingGemma 2, in float32.

What the tests' goldens beside the checkpoint are recorded from: its
processors, its model and each tower alone. It needs torch, torchvision
and transformers, which are not IRON's requirements, only to record.
"""

from pathlib import Path

import numpy as np
import torch  # pyright: ignore[reportMissingImports]
import transformers  # pyright: ignore[reportMissingImports]
from transformers.models.embedding_gemma2 import (  # pyright: ignore[reportMissingImports]
    modeling_embedding_gemma2,
)
from transformers.models.gemma4 import (  # pyright: ignore[reportMissingImports]
    image_processing_gemma4,
    modeling_gemma4,
)

from iron.lm import Checkpoint


class HuggingFace:
    """Hugging Face's processors and model over the checkpoint in `directory`, in float32.

    And each tower alone with its projection into the text model's space.

    Args:
        directory: The checkpoint directory, as Hugging Face loads it.
    """

    def __init__(self, directory):
        directory = Path(directory)
        self.processor = transformers.AutoProcessor.from_pretrained(directory)
        # Not eager: there Gemma4AudioAttention inverts the additive float mask
        # create_bidirectional_mask gives it.
        self.model = transformers.AutoModel.from_pretrained(
            directory, dtype=torch.float32, attn_implementation="sdpa"
        ).eval()
        self.image_processor = image_processing_gemma4.Gemma4ImageProcessor()
        self.extractor = transformers.AutoFeatureExtractor.from_pretrained(directory)
        config = transformers.AutoConfig.from_pretrained(directory)
        config.vision_config._attn_implementation = "eager"
        config.audio_config._attn_implementation = "sdpa"
        tensors = Checkpoint(directory / "model.safetensors").tensors
        self.vision = modeling_gemma4.Gemma4VisionModel(config.vision_config).eval()
        self.audio = modeling_gemma4.Gemma4AudioModel(config.audio_config).eval()
        self.embed_vision, self.embed_audio = (
            modeling_embedding_gemma2.EmbeddingGemma2MultimodalEmbedder(
                tower, config.text_config
            ).eval()
            for tower in (config.vision_config, config.audio_config)
        )
        for module, prefix in (
            (self.vision, "vision_tower."),
            (self.embed_vision, "embed_vision."),
            (self.audio, "audio_tower."),
            (self.embed_audio, "embed_audio."),
        ):
            module.load_state_dict(
                {
                    k.removeprefix(prefix): torch.from_numpy(v.astype(np.float32))
                    for k, v in tensors.items()
                    if k.startswith(prefix)
                }
            )

    def encode(self, text: str, audio=None, image=None) -> np.ndarray:
        """Return the model's unit-length mean-pooled embedding of `text`.

        With one mono clip `audio` and one decoded image `image` at its
        placeholders.
        """
        media = {}
        if audio is not None:
            media["audio"] = [audio]
        if image is not None:
            media["images"] = [image]
        inputs = self.processor(text=text, return_tensors="pt", **media)
        with torch.no_grad():
            states = self.model(**inputs).last_hidden_state[0].numpy()
        embedding = states.mean(axis=0)
        return embedding / np.linalg.norm(embedding)

    def patches(self, image: np.ndarray, max_tokens: int):
        """Return the image processor's `pixel_values`, float32, and `image_position_ids`, int64.

        For a decoded `image` at `max_tokens`.
        """
        out = self.image_processor.preprocess(
            torch.from_numpy(image).permute(2, 0, 1),
            max_soft_tokens=max_tokens,
            return_tensors="pt",
        )
        return (
            out["pixel_values"][0].numpy().astype(np.float32),
            out["image_position_ids"][0].numpy().astype(np.int64),
        )

    def vision_tower(self, pixel_values, positions) -> np.ndarray:
        """Return the vision tower's soft tokens in the text model's space.

        Over the processor's `pixel_values` and `positions`.
        """
        with torch.no_grad():
            hidden = self.vision(
                pixel_values=torch.from_numpy(pixel_values)[None],
                pixel_position_ids=torch.from_numpy(positions)[None],
            ).last_hidden_state
            soft = self.embed_vision(hidden).numpy()
        return soft.reshape(-1, soft.shape[-1])

    def features(self, waveform) -> np.ndarray:
        """Return the feature extractor's valid features of one mono clip."""
        out = self.extractor([waveform], return_tensors="np")
        return out["input_features"][0][out["input_features_mask"][0].astype(bool)]

    def audio_tower(self, waveform) -> np.ndarray:
        """Return the audio tower's valid soft tokens of one mono clip in the text model's space."""
        out = self.extractor([waveform], return_tensors="np")
        features, mask = out["input_features"][0], out["input_features_mask"][0]
        with torch.no_grad():
            out = self.audio(
                torch.from_numpy(features)[None], torch.from_numpy(mask)[None]
            )
            valid = torch.from_numpy(out.attention_mask[0].numpy())
            return self.embed_audio(out.last_hidden_state)[0][valid].numpy()
