# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LibriSpeech's test-clean utterances, the speech the audio models' tests hear."""

import tarfile
from pathlib import Path

import numpy as np

from iron.lm.testing import Download, cache_dir

# LibriSpeech's test-clean (CC BY 4.0, V. Panayotov et al., 2015), as openslr
# publishes it, fetched once into IRON's cache.
LIBRISPEECH = Download(
    "https://www.openslr.org/resources/12/test-clean.tar.gz",
    "39fde525e59672dc6d1551919b1478f724438a95aa55f874b576be21967e6c23",
)


def _cached_member(member: str) -> Path:
    """``member``, a path inside the archive, taken from it into IRON's
    cache the first time; the cached file either way.
    """
    path = cache_dir() / member
    if not path.exists():
        with tarfile.open(LIBRISPEECH.fetch()) as archive:
            data = archive.extractfile(member).read()
        path.parent.mkdir(parents=True, exist_ok=True)
        # Renamed into place, so an interrupted extraction leaves no clip.
        from uuid import uuid4

        partial = path.with_suffix(f".{uuid4().hex}.part")
        partial.write_bytes(data)
        partial.replace(path)
    return path


def utterance(name: str) -> np.ndarray:
    """The utterance `name` (`speaker-chapter-index`), its FLAC member taken
    from the archive in IRON's cache the first time, decoded: float32
    samples in [-1, 1) at 16 kHz, mono.

    Raises:
        ValueError: The member is not 16 kHz mono.
    """
    speaker, chapter, _ = name.split("-")
    path = _cached_member(f"LibriSpeech/test-clean/{speaker}/{chapter}/{name}.flac")
    import soundfile

    samples, rate = soundfile.read(path, dtype="float32")
    if samples.ndim != 1 or rate != 16000:
        raise ValueError(f"{name}: not 16 kHz mono")
    return samples


def transcript(name: str) -> str:
    """``name``'s reference line from its chapter's ``.trans.txt``, the
    archive's own normalized-caps transcript, taken from the archive into
    IRON's cache the first time.

    Raises:
        ValueError: The chapter's transcript holds no such utterance.
    """
    speaker, chapter, _ = name.split("-")
    path = _cached_member(
        f"LibriSpeech/test-clean/{speaker}/{chapter}/{speaker}-{chapter}.trans.txt"
    )
    prefix = f"{name} "
    for line in path.read_text().splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :]
    raise ValueError(f"{name}: not in {path.name}")
