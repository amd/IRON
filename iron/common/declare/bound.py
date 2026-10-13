# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A declared value bound to an operator instance."""

from __future__ import annotations

from typing import Any

import numpy as np

from .member import _Value


class BoundValue:
    """A value on an operator: per call, or written once per build.

    On a full ELF ``param`` is the ``ScratchpadParameter`` the build creates.
    On an xclbin (no scratchpad) it is a dispatch-time scalar, ``ssa`` its
    value in the sequence body.
    """

    def __init__(self, member: _Value, owner) -> None:
        self.member = member
        self.name = member.name
        self.dtype = member.dtype
        self.param: Any = None
        self.symbol: str | None = None
        self.ssa = None
        self.targets: list[tuple[Any, int]] = []
        self.address = member.address
        self.lock = member.lock
        self.optional = member.optional
        self.derive = member.derive

    def bind(self, buffers, index: int = 0) -> None:
        """Bind to runtime-parameter buffers whose ``[index]`` the preamble writes."""
        if not isinstance(buffers, (list, tuple)):
            buffers = [buffers]
        self.targets.extend((b, index) for b in buffers)

    def __repr__(self) -> str:
        return f"<{self.member.kind} {self.name} {np.dtype(self.dtype).name}>"
