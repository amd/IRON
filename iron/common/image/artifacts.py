# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a build produced: which operators share a design, which step runs
which, and where each buffer lands, over ``CompilableDesign``'s cache entries.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from aie.utils.compile.jit.compilabledesign import CacheEntry

from .step import BufferRef


@dataclass(frozen=True)
class Design:
    """One distinct array design in an image, and what runs on it."""

    name: str  # its symbol in the module (``op3_RoPE``), or the operator's label
    operators: tuple[str, ...]  # labels of the operators sharing it
    entry: CacheEntry | None = None  # its own cache entry, when built as its own image
    image: Path | None = None  # its own image, when it has one (an xclbin chain)
    insts: Path | None = None  # its own instruction stream, likewise


@dataclass(frozen=True)
class Step:
    """One step: which operator, on which design, over which buffers."""

    index: int
    operator: str
    design: str
    buffers: tuple[BufferRef, ...]


@dataclass(frozen=True)
class Parameter:
    """One row of an image's parameter table: a word of its ctrl scratchpad."""

    name: str
    index: int
    dtype: str
    # "core": a core reads it, and the scratchpad holds it shifted left by
    # 2; "addr": it patches a DMA address, and is held as it is.
    kind: str

    @property
    def shift(self) -> int:
        return 2 if self.kind == "core" else 0


@dataclass(frozen=True)
class Artifacts:
    """The record of one image.

    Attributes:
        full_elf: One fused image, else an xclbin per design, chained
            (``image`` is the last link).
        entry: The cache entry holding the parameter table and lowered module.
        buffers: Each buffer to ``(argument kind, byte offset, bytes)``.
    """

    full_elf: bool
    image: Path
    insts: Path | None
    entry: CacheEntry | None
    designs: tuple[Design, ...]
    steps: tuple[Step, ...]
    buffers: dict[str, tuple[str, int, int]]

    @property
    def params(self) -> Path | None:
        return self.entry.params if self.entry is not None else None

    @property
    def parameter_table(self) -> list[Parameter]:
        """The scratchpad words the image declares, in the table's order."""
        if self.params is None:
            return []
        count, *rows = self.params.read_text().splitlines()
        table = []
        for row in rows[: int(count)]:
            name, index, dtype, kind, _, _ = row.split()
            table.append(Parameter(name, int(index), dtype, kind))
        return table

    @property
    def parameters(self) -> frozenset[str]:
        """The names of the scratchpad words the image declares."""
        return frozenset(p.name for p in self.parameter_table)

    @property
    def lowered_mlir(self) -> Path | None:
        return self.entry.lowered_mlir if self.entry is not None else None

    @property
    def directory(self) -> Path | None:
        return self.entry.directory if self.entry is not None else None

    def report(self, name: str = "") -> str:
        kind = "full ELF" if self.full_elf else "xclbin"
        lines = [f"{name or 'image'}: {kind} {self.image}"]
        for d in self.designs:
            shared = f" (x{len(d.operators)})" if len(d.operators) > 1 else ""
            lines.append(f"  design {d.name}{shared}: {', '.join(d.operators)}")
        for s in self.steps:
            lines.append(f"  step {s.index}: {s.operator} on {s.design}")
        return "\n".join(lines)
