# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An image someone else built, declared as an operator's ``image=``."""

from __future__ import annotations

import hashlib
import os
import tempfile
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from aie.utils.compile import NPU_CACHE_HOME


@dataclass(frozen=True, kw_only=True, repr=False)
class Xclbin:
    """An image someone else built: a downloaded xclbin, pinned by digest.

    Given as ``image=`` when a class is declared (``class Shipped(GEMM,
    image=Xclbin(...))``). Every stream of such a class is pinned with
    ``via=`` and every derived value has an ``address``, because nothing else
    records where its endpoints are; the library emits the sequence against
    those pins.
    """

    url: str
    sha256: str
    filename: str
    kernel_name: str = "MLIR_AIE"

    def __repr__(self) -> str:
        return f"Xclbin({self.filename})"

    def fetch(self, directory=None) -> Path:
        """The downloaded file, by digest: fetched unless a file of the pinned
        content is already there.

        Into the JIT cache's own root by default (``NPU_CACHE_HOME``'s
        ``prebuilt/``), so an external image is found where every other built
        artifact is and no caller has to name a directory for it.
        """
        if directory is None:
            directory = Path(NPU_CACHE_HOME) / "prebuilt"
        target = Path(directory) / self.filename
        if target.exists():
            with open(target, "rb") as f:
                if hashlib.file_digest(f, "sha256").hexdigest() == self.sha256:
                    return target
        if not self.url.startswith("https://"):
            raise ValueError(f"refusing to download over {self.url!r}")
        with urllib.request.urlopen(self.url, timeout=60) as response:
            content = response.read()
        if (got := hashlib.sha256(content).hexdigest()) != self.sha256:
            raise RuntimeError(f"{self.url} has SHA-256 {got}, expected {self.sha256}")
        target.parent.mkdir(parents=True, exist_ok=True)
        # A file of this fetch's own, renamed over the target whole: concurrent
        # fetches never share one, and none sees a partial target.
        with tempfile.NamedTemporaryFile(
            dir=target.parent, prefix=f"{target.name}.", suffix=".part", delete=False
        ) as partial:
            partial.write(content)
            # A temporary file is created owner-only; the cache is read as any file is.
            os.fchmod(partial.fileno(), 0o644)
        try:
            os.replace(partial.name, target)
        except OSError:
            os.unlink(partial.name)
            raise
        return target
