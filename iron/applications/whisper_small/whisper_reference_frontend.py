# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import os

import argparse

import torch

from whisper_audio import (
    load_wav,
    log_mel_spectrogram,
)

from whisper_common import (
    ARTIFACT_ROOT,
    whisper_checkpoint,
    FRAMES,
    MELS,
    SEQ,
    STATE,
)
import torch.nn.functional as F
from safetensors import safe_open

parser = argparse.ArgumentParser(description=("Whisper-small FP32 frontend reference."))

input_group = parser.add_mutually_exclusive_group()

input_group.add_argument(
    "--input",
    type=Path,
    default=None,
    help=("Optional .pt artifact containing a 'mel' tensor."),
)

input_group.add_argument(
    "--wav",
    type=Path,
    default=None,
    help=(
        "Optional mono 16-kHz PCM16 WAV. "
        "Its Whisper log-Mel features become the frontend input."
    ),
)

parser.add_argument(
    "--output",
    type=Path,
    default=None,
    help=("Optional output reference artifact path."),
)

args = parser.parse_args()


ROOT = ARTIFACT_ROOT

OUT = (
    args.output
    if args.output is not None
    else (ROOT / "whisper-small-frontend-reference-128.pt")
)

OUT.parent.mkdir(
    parents=True,
    exist_ok=True,
)

torch.manual_seed(20260921)


# ============================================================
# Frontend input
#
# Default mode preserves the deterministic synthetic regression.
# An optional artifact can instead provide an exact Whisper
# log-Mel tensor under the "mel" key.
# ============================================================

if args.input is None and args.wav is None:

    input_mode = "synthetic"

    mel = torch.randn(
        1,
        MELS,
        FRAMES,
        dtype=torch.float32,
    )

    # Keep the magnitude in a realistic bounded range rather than
    # feeding arbitrarily large Gaussian values.
    mel = torch.tanh(mel) * 2.0

elif args.input is not None:

    input_mode = "artifact"

    source = torch.load(
        args.input,
        map_location="cpu",
        weights_only=True,
    )

    if "mel" not in source:
        raise KeyError(f"Input artifact has no 'mel' tensor: {args.input}")

    mel = source["mel"].float().clone()

    print(
        "Input artifact:",
        args.input,
    )

else:

    input_mode = "wav"

    waveform = load_wav(args.wav)

    mel = log_mel_spectrogram(
        waveform,
        FRAMES,
    )

    print(
        "Input WAV:",
        args.wav,
    )


# ============================================================
# Official Whisper-small parameters
# ============================================================

with safe_open(
    str(whisper_checkpoint()),
    framework="pt",
    device="cpu",
) as f:

    conv1_w = f.get_tensor("model.encoder.conv1.weight").float()

    conv1_b = f.get_tensor("model.encoder.conv1.bias").float()

    conv2_w = f.get_tensor("model.encoder.conv2.weight").float()

    conv2_b = f.get_tensor("model.encoder.conv2.bias").float()

    positions = f.get_tensor("model.encoder.embed_positions.weight").float()


# ============================================================
# Canonical frontend
# ============================================================

conv1 = F.conv1d(
    mel,
    conv1_w,
    conv1_b,
    stride=1,
    padding=1,
)

gelu1 = F.gelu(
    conv1,
    approximate="tanh",
)

conv2 = F.conv1d(
    gelu1,
    conv2_w,
    conv2_b,
    stride=2,
    padding=1,
)

gelu2 = F.gelu(
    conv2,
    approximate="tanh",
)

tokens = gelu2.squeeze(0).transpose(0, 1).contiguous()

assert tokens.shape == (
    SEQ,
    STATE,
)

block0_input = tokens + positions[:SEQ]


print("=" * 80)
print("WHISPER-SMALL FRONTEND CPU REFERENCE")
print("=" * 80)

for name, x in (
    ("mel", mel),
    ("conv1", conv1),
    ("gelu1", gelu1),
    ("conv2", conv2),
    ("gelu2", gelu2),
    ("tokens", tokens),
    ("block0_input", block0_input),
):
    print(
        f"{name:14s}",
        "shape=",
        tuple(x.shape),
        "min=",
        x.min().item(),
        "max=",
        x.max().item(),
        "norm=",
        torch.linalg.vector_norm(x).item(),
    )

assert torch.isfinite(block0_input).all()


torch.save(
    {
        "mel": mel.cpu(),
        "input_mode": input_mode,
        "input_artifact": (str(args.input) if args.input is not None else None),
        "input_wav": (str(args.wav) if args.wav is not None else None),
        "conv1": conv1.cpu(),
        "gelu1": gelu1.cpu(),
        "conv2": conv2.cpu(),
        "gelu2": gelu2.cpu(),
        "tokens": tokens.cpu(),
        "block0_input": block0_input.cpu(),
    },
    OUT,
)

print()
print("Saved:", OUT)
print("=" * 80)
print("CPU FRONTEND REFERENCE: PASS")
print("=" * 80)
