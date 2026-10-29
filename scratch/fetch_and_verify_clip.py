#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fetch one LibriSpeech clip (cached, sha256-pinned) and save it as a WAV,
for ``npu_single_window.py --wav`` and ``hf_single_window.py`` to read: a
one-shot stand-in for ``fetch_librispeech_clips.py`` while deliverable 1's
own clip is the only one needed.
"""

import argparse
from pathlib import Path

from iron.applications.whisper.audio import save_wav
from iron.tests.support.librispeech import utterance


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--clip", default="4446-2275-0016")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    save_wav(args.out, utterance(args.clip))
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
