#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Single-window Whisper.transcribe on the NPU (deliverable 1's device
half): load a checkpoint, fetch one LibriSpeech clip, transcribe it, and
dump the result for ``hf_single_window.py`` (a separate, torch-bearing
venv) to compare against Hugging Face's own greedy ``generate``.
"""

import argparse
import json
from pathlib import Path

from iron.applications.whisper.audio import save_wav
from iron.applications.whisper.model import Whisper
from iron.lm.testing import weights_dir
from iron.tests.support.librispeech import utterance


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", default="whisper-small")
    parser.add_argument("--clip", default="4446-2275-0016")
    parser.add_argument("--max-tokens", type=int, default=224)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--wav-out", type=Path, required=True)
    args = parser.parse_args()

    directory = weights_dir(args.checkpoint)
    model = Whisper.load(directory)
    audio = utterance(args.clip)
    save_wav(args.wav_out, audio)
    prompt = model.prompt_tokens(language="en", task="transcribe")
    generated, text = model.transcribe(audio, max_tokens=args.max_tokens)

    args.out.write_text(
        json.dumps(
            dict(
                checkpoint=args.checkpoint,
                clip=args.clip,
                wav=str(args.wav_out),
                prompt=prompt,
                generated=[int(t) for t in generated],
                text=text,
                samples=audio.size,
            )
        )
    )
    print(f"wrote {args.out}: {len(generated)} tokens, prompt {prompt}")
    print(f"text: {text}")


if __name__ == "__main__":
    main()
