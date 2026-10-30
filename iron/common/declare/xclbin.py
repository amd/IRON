# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An image someone else built, declared as an operator's ``image=``."""

from __future__ import annotations

import hashlib
import os
import tempfile
import urllib.request
from pathlib import Path
from typing import Any

from aie.utils.compile import NPU_CACHE_HOME
from aie.utils.npukernel import NPUKernel


class Xclbin(NPUKernel):
    """A downloaded xclbin pinned by ``sha256``.

    Fetched over https into the JIT cache's ``prebuilt/<filename>`` on
    first read of ``xclbin_path``. As an ``image=`` it has no
    instructions; a build runs it ``with_instructions``.

    Args:
        **kernel: ``NPUKernel``'s other arguments, kept as ``settings``.
    """

    def __init__(self, url: str, sha256: str, filename: str, **kernel: Any) -> None:
        super().__init__(**kernel)
        self.url, self.sha256, self.filename = url, sha256, filename
        self.settings = kernel

    @property
    def xclbin_path(self) -> Path:
        if self._xclbin_path is None:
            self._xclbin_path = self.fetch()
        return Path(self._xclbin_path)

    def with_instructions(self, insts_path, **kernel) -> Xclbin:
        """Return this image running ``insts_path``.

        With ``kernel`` (as `NPUKernel` takes it) over the declared
        settings.
        """
        run = Xclbin(
            self.url,
            self.sha256,
            self.filename,
            **{**self.settings, **kernel, "insts_path": insts_path},
        )
        run._xclbin_path = self._xclbin_path
        return run

    def __call__(self, *args, **kwargs):
        if self.insts_path is None:
            raise TypeError(f"{self!r} has no instructions; call with_instructions()")
        return super().__call__(*args, **kwargs)

    def fetch(self, directory=None) -> Path:
        """Return the downloaded file in ``directory``.

        ``NPU_CACHE_HOME``'s ``prebuilt/`` by default, fetched unless
        the pinned content is there.

        Raises:
            ValueError: The URL is not https.
            RuntimeError: The download has another digest.
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
        partial = tempfile.NamedTemporaryFile(
            dir=target.parent, prefix=f"{target.name}.", suffix=".part", delete=False
        )
        try:
            with partial:
                partial.write(content)
                # A temporary file is created owner-only; the cache is read as any file is.
                os.fchmod(partial.fileno(), 0o644)
            os.replace(partial.name, target)
        except BaseException:
            os.unlink(partial.name)
            raise
        return target

    def __repr__(self) -> str:
        return f"Xclbin({self.filename})"
