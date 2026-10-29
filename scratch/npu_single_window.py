#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Single-window Whisper.transcribe on the NPU (deliverable 1 and the
single-window half of deliverable 4): load a checkpoint, transcribe one
WAV, report its word error rate against an optional reference transcript,
and dump the result for ``hf_single_window.py`` (a separate, torch-bearing
venv) to compare against Hugging Face's own greedy ``generate``.
"""

import argparse
import json
from pathlib import Path

from iron.applications.whisper.audio import load_wav
from iron.applications.whisper.model import Whisper
from iron.applications.whisper.wer import word_error_rate
from iron.lm.testing import weights_dir


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", default="whisper-small")
    parser.add_argument("--wav", type=Path, required=True)
    parser.add_argument("--reference-text", type=Path, help="WER against this file")
    parser.add_argument("--max-tokens", type=int, default=224)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    directory = weights_dir(args.checkpoint)
    model = Whisper.load(directory)
    audio = load_wav(args.wav)
    prompt = model.prompt_tokens(language="en", task="transcribe")
    generated, text = model.transcribe(audio, max_tokens=args.max_tokens)

    wer = None
    if args.reference_text:
        wer = word_error_rate(args.reference_text.read_text(), text)
        print(f"WER vs {args.reference_text}: {100 * wer:.1f}%")

    args.out.write_text(
        json.dumps(
            dict(
                checkpoint=args.checkpoint,
                wav=str(args.wav),
                prompt=prompt,
                generated=[int(t) for t in generated],
                text=text,
                wer=wer,
                samples=audio.size,
            )
        )
    )
    print(f"wrote {args.out}: {len(generated)} tokens, prompt {prompt}")
    print(f"text: {text}")


if __name__ == "__main__":
    main()
