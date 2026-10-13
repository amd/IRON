#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's outputs on the EmbeddingGemma 2 tests' fixed inputs, which
the tests check the float32 oracles against without torch.

Run where torch, torchvision and transformers are installed (they are not
IRON's requirements), over the checkpoint directory:

    python -m iron.applications.embedding_gemma2.hugging_face <directory>

It writes the `hugging_face.npz` beside each test, with the versions that
made it and the checkpoint's sha256 in its `metadata`. With `--check` it
compares a fresh run with the saved files instead.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import torch
import transformers
from transformers.models.embedding_gemma2 import modeling_embedding_gemma2
from transformers.models.gemma4 import image_processing_gemma4, modeling_gemma4

from iron.applications.embedding_gemma2 import test as text_test
from iron.lm import Checkpoint
from iron.applications.embedding_gemma2.audio import test as audio_test
from iron.applications.embedding_gemma2.audio.model import audio_tensors
from iron.applications.embedding_gemma2.oracle import PROMPTS
from iron.applications.embedding_gemma2.vision import test as vision_test
from iron.applications.embedding_gemma2.vision.model import VISION, vision_tensors

# A fresh run against the saved files, in relative norm: float32's own
# reordering across hosts and thread counts.
CHECK_RTOL = 1e-5

CHECKPOINT_FILES = [
    "model.safetensors",
    "config.json",
    "tokenizer.json",
    "processor_config.json",
]


def load(module: torch.nn.Module, tensors: dict, prefix: str):
    """Load the checkpoint's `prefix` weights into `module`, in float32."""
    module.load_state_dict(
        {
            k.removeprefix(prefix): torch.from_numpy(v.astype(np.float32))
            for k, v in tensors.items()
            if k.startswith(prefix)
        }
    )


def text_references(directory: Path) -> dict:
    """The ids Hugging Face's processor gives each of the text test's
    `HUGGING_FACE` cases, and its model's unit-length mean-pooled embedding.
    """
    processor = transformers.AutoProcessor.from_pretrained(directory)
    # Not eager: there Gemma4AudioAttention inverts the additive float mask
    # create_bidirectional_mask gives it.
    model = transformers.AutoModel.from_pretrained(
        directory, dtype=torch.float32, attn_implementation="sdpa"
    ).eval()
    out = {}
    for case, (text, task, wave, image) in text_test.HUGGING_FACE.items():
        media = {}
        if wave is not None:
            media["audio"] = [wave]
        if image is not None:
            media["images"] = [image]
        inputs = processor(text=PROMPTS[task] + text, return_tensors="pt", **media)
        with torch.no_grad():
            want = model(**inputs).last_hidden_state[0].numpy().mean(axis=0)
        out[f"{case}/input_ids"] = inputs["input_ids"][0].numpy()
        out[f"{case}/embedding"] = want / np.linalg.norm(want)
    return out


def vision_references(directory: Path) -> dict:
    """The vision tower's soft tokens for the vision test's portrait, and the
    sha256 of the image processor's float32 pixels and int64 positions for
    each of its `RESIZES`.
    """
    config = transformers.AutoConfig.from_pretrained(directory)
    config.vision_config._attn_implementation = "eager"
    tower = modeling_gemma4.Gemma4VisionModel(config.vision_config).eval()
    embedder = modeling_embedding_gemma2.EmbeddingGemma2MultimodalEmbedder(
        config.vision_config, config.text_config
    ).eval()
    tensors = vision_tensors(Checkpoint(directory / "model.safetensors").tensors)
    load(tower, tensors, "vision_tower.")
    load(embedder, tensors, "embed_vision.")
    values, positions = vision_test.processed("portrait")
    with torch.no_grad():
        hidden = tower(
            pixel_values=torch.from_numpy(values)[None],
            pixel_position_ids=torch.from_numpy(positions)[None],
        ).last_hidden_state
        soft = embedder(hidden).numpy().reshape(-1, VISION.text_dim)
    out = {"portrait/soft_tokens": soft}
    processor = image_processing_gemma4.Gemma4ImageProcessor()
    for shape, tokens in vision_test.RESIZES:
        image = np.random.default_rng(0).integers(0, 256, (*shape, 3), dtype=np.uint8)
        want = processor(
            torch.from_numpy(image).permute(2, 0, 1),
            max_soft_tokens=tokens,
            return_tensors="pt",
        )
        key = f"resize/{shape[0]}x{shape[1]}_{tokens}"
        for name, array, dtype in (
            ("pixels", want["pixel_values"][0].numpy(), np.float32),
            ("positions", want["image_position_ids"][0].numpy(), np.int64),
        ):
            digest = hashlib.sha256(np.ascontiguousarray(array, dtype)).hexdigest()
            out[f"{key}/{name}"] = np.array(digest)
    return out


def audio_references(directory: Path) -> dict:
    """The feature extractor's features and mask for the audio test's medium
    clip, and the audio tower's soft tokens over those features.
    """
    config = transformers.AutoConfig.from_pretrained(directory)
    # Not eager: there Gemma4AudioAttention inverts the additive float mask
    # create_bidirectional_mask gives it.
    config.audio_config._attn_implementation = "sdpa"
    tower = modeling_gemma4.Gemma4AudioModel(config.audio_config).eval()
    embedder = modeling_embedding_gemma2.EmbeddingGemma2MultimodalEmbedder(
        config.audio_config, config.text_config
    ).eval()
    tensors = audio_tensors(Checkpoint(directory / "model.safetensors").tensors)
    load(tower, tensors, "audio_tower.")
    load(embedder, tensors, "embed_audio.")
    extractor = transformers.AutoFeatureExtractor.from_pretrained(directory)
    wave = audio_test.chirp(audio_test.CLIPS["medium"])
    processed = extractor([wave], return_tensors="np")
    features = processed["input_features"][0]
    mask = processed["input_features_mask"][0]
    with torch.no_grad():
        out = tower(torch.from_numpy(features)[None], torch.from_numpy(mask)[None])
        valid = torch.from_numpy(out.attention_mask[0].numpy())
        soft = embedder(out.last_hidden_state)[0][valid].numpy()
    return {
        "medium/features": features,
        "medium/mask": mask,
        "medium/soft_tokens": soft,
    }


def mismatches(saved: dict, fresh: dict) -> list[str]:
    """What of `fresh` the saved references do not hold: a missing or extra
    name, a float array off by more than `CHECK_RTOL` in relative norm, any
    other array not equal.
    """
    out = [f"{k}: missing" for k in sorted(fresh.keys() - saved.keys())]
    out += [f"{k}: no longer made" for k in sorted(saved.keys() - fresh.keys())]
    for k in sorted(fresh.keys() & saved.keys()):
        want, got = saved[k], fresh[k]
        if want.shape != got.shape:
            out.append(f"{k}: shape {got.shape}, saved {want.shape}")
        elif np.issubdtype(want.dtype, np.floating):
            error = np.linalg.norm(got - want) / np.linalg.norm(want)
            if error > CHECK_RTOL:
                out.append(f"{k}: relative error {error:.2e}")
        elif not np.array_equal(got, want):
            out.append(f"{k}: differs")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="the checkpoint directory")
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare a fresh run with the saved files rather than write them",
    )
    args = parser.parse_args()
    checkpoint = {}
    for name in CHECKPOINT_FILES:
        with open(args.directory / name, "rb") as f:
            checkpoint[name] = hashlib.file_digest(f, "sha256").hexdigest()
    metadata = {
        "transformers": transformers.__version__,
        "torch": torch.__version__,
        "numpy": np.__version__,
        "checkpoint_sha256": checkpoint,
    }
    failed = False
    for path, references in (
        (text_test.REFERENCES, text_references),
        (vision_test.REFERENCES, vision_references),
        (audio_test.REFERENCES, audio_references),
    ):
        fresh = references(args.directory)
        if args.check:
            with np.load(path) as saved:
                made = json.loads(str(saved["metadata"]))
                problems = mismatches(
                    {k: v for k, v in saved.items() if k != "metadata"}, fresh
                )
            print(f"{path}: saved with {made}")
            for problem in problems:
                print(f"  {problem}")
            failed |= bool(problems)
            continue
        np.savez_compressed(path, metadata=np.array(json.dumps(metadata)), **fresh)
        print(f"{path}: {path.stat().st_size} bytes")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
