#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Hugging Face's own greedy ``generate`` on the WAV ``npu_single_window.py``
dumped, run in the hf-ref venv (torch and transformers; never the nightly
one ``iron`` runs device code in). Compares token ids exactly against the
NPU run's, the single-window deliverable's bar.
"""

import argparse
import json
from pathlib import Path

import torch
import transformers

from iron.applications.whisper.audio import load_wav


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--result", type=Path, required=True, help="npu_single_window.py's --out"
    )
    parser.add_argument("--checkpoint", type=Path, required=True)
    args = parser.parse_args()

    result = json.loads(args.result.read_text())
    audio = load_wav(result["wav"])

    model = transformers.WhisperForConditionalGeneration.from_pretrained(
        args.checkpoint, local_files_only=True, dtype=torch.float32
    ).eval()
    processor = transformers.WhisperProcessor.from_pretrained(
        args.checkpoint, local_files_only=True
    )
    features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features

    with torch.no_grad():
        out = model.generate(
            features,
            language="en",
            task="transcribe",
            do_sample=False,
            num_beams=1,
            return_timestamps=False,
            max_new_tokens=len(result["generated"]) + 8,
        )
    expected = out[0].tolist()
    # transformers' generate repeats decoder_start_token_id (<|startoftranscript|>)
    # at the front of its own prompt; the NPU run's prompt is given separately.
    expected_prompt, expected_generated = expected[:4], expected[4:]

    got = result["generated"]
    match = got == expected_generated or got == expected_generated + [
        model.config.eos_token_id
    ]
    print(f"NPU prompt:      {result['prompt']}")
    print(f"HF prompt:       {expected_prompt}")
    print(f"NPU generated:   {got}")
    print(f"HF generated:    {expected_generated}")
    print(f"exact token match: {match}")
    if not match:
        raise SystemExit("FAILED: token mismatch with Hugging Face's greedy generate")


if __name__ == "__main__":
    main()
