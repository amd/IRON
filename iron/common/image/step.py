# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A step of a sequence, and where its buffers are in the image's."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from ..declare import Operator


@dataclass(frozen=True)
class BufferRef:
    """Where a step's buffer is.

    ``nbytes`` bytes of the image's buffer ``root`` from byte ``start``, or
    all of it where ``nbytes`` is None.
    """

    root: str
    start: int = 0
    nbytes: int | None = None

    def place(self, layout: Mapping[str, tuple[str, int, int]]) -> tuple[str, int, int]:
        """Return where this is, ``layout`` placing each buffer.

        Its ``(argument kind, byte offset, bytes)``.
        """
        kind, offset, nbytes = layout[self.root]
        return kind, offset + self.start, nbytes if self.nbytes is None else self.nbytes

    def __str__(self) -> str:
        if self.nbytes is None:
            return self.root
        return f"{self.root}[{self.start}:{self.start + self.nbytes}]"


@dataclass(frozen=True)
class SequenceStep:
    """One step: an operator, and where each of its declared buffers is."""

    op: Operator
    buffers: tuple[BufferRef, ...]
