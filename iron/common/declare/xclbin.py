# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An image someone else built, declared as an operator's ``image=``."""

from __future__ import annotations

import hashlib
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

        def digest(path):
            with open(path, "rb") as f:
                return hashlib.file_digest(f, "sha256").hexdigest()

        if target.exists() and digest(target) == self.sha256:
            return target
        if not self.url.startswith("https://"):
            raise ValueError(f"refusing to download over {self.url!r}")
        target.parent.mkdir(parents=True, exist_ok=True)
        # Beside the target and renamed, so an interrupted fetch cannot leave a
        # truncated file that a later run reports as a digest mismatch.
        partial = target.with_suffix(target.suffix + ".part")
        with urllib.request.urlopen(self.url, timeout=60) as response:
            partial.write_bytes(response.read())
        if (got := digest(partial)) != self.sha256:
            partial.unlink()
            raise RuntimeError(f"{self.url} has SHA-256 {got}, expected {self.sha256}")
        partial.replace(target)
        return target
