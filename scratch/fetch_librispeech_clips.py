#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Export amd/IRON#218's validation clips as standalone WAV fixtures, for
Whisper's WER tests to read without a LibriSpeech archive of their own.

Each clip is fetched once through ``iron.tests.support.librispeech``
(cached, sha256-pinned from the same openslr test-clean.tar.gz every
other LibriSpeech-backed test reads), then written as a mono 16 kHz
PCM16 WAV plus its reference transcript line, with one ``PROVENANCE.md``
recording the source, license and each WAV's own sha256.
"""

import argparse
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from iron.applications.whisper.audio import save_wav
from iron.tests.support.librispeech import LIBRISPEECH, transcript, utterance

# amd/IRON#218's single-window clips (<= 30 s, Whisper.transcribe's bar) and
# its long-form ones (needs transcribe_long's timestamp-aware decoding, not
# yet built): named here so a later WER test can ask for either.
SINGLE_WINDOW = ["1919-142785-0007", "3170-137482-0000"]
LONG_FORM = ["422-122949-0013"]
JOINED = ["2902-9006-0005", "2902-9006-0007", "2902-9006-0015"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("/proj/rdi/staff/ehunhoff/models/librispeech-clips"),
    )
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    digests = {}
    for name in [*SINGLE_WINDOW, *LONG_FORM, *JOINED]:
        wav = args.out / f"{name}.wav"
        save_wav(wav, utterance(name))
        (args.out / f"{name}.txt").write_text(transcript(name) + "\n")
        digests[wav.name] = hashlib.file_digest(wav.open("rb"), "sha256").hexdigest()

    stamp = datetime.now(timezone.utc).astimezone().isoformat()
    lines = [
        "# LibriSpeech test-clean clips for Whisper's WER tests",
        "",
        f"Source: {LIBRISPEECH.url} (CC BY 4.0, V. Panayotov et al., 2015), "
        f"sha256 {LIBRISPEECH.sha256}, fetched {stamp}",
        "",
        "Each WAV is one utterance (`speaker-chapter-index`), decoded from the "
        "archive's FLAC member to mono 16 kHz PCM16; its `.txt` is the "
        "archive's own reference transcript line. amd/IRON#218 (Giuseppe "
        f"Capaldo)'s validation bar: {', '.join(SINGLE_WINDOW)} decode as one "
        f"window; {', '.join(LONG_FORM)} and {'+'.join(JOINED)} joined (97 s) "
        "need long-form, timestamp-aware decoding.",
        "",
        "```",
        *(f"{digest}  {name}" for name, digest in sorted(digests.items())),
        "```",
    ]
    (args.out / "PROVENANCE.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {len(digests)} clips to {args.out}")


if __name__ == "__main__":
    main()
