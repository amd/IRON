# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a build produced: a record of an image, by identity, wherever it sits.

``CompilableDesign`` owns building and caching: every compile lands in an
entry keyed on the content it was built from. What it does not know is
the structure IRON gave the build: which operators share which design,
which step of a graph runs which design, and where each buffer lands in
the image's plan. :class:`Artifacts` is that view, one shape for an
operator compiled alone (one design, one step) and for a graph, with
every path resolved through the entries. It is held in memory and, when
the context asks for it, written beside the image as ``artifacts.json``.
"""

from __future__ import annotations

import dataclasses
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Design:
    """One distinct array design in an image, and what runs on it."""

    name: str  # its symbol in the module (``op3_RoPE``), or the operator's label
    operators: tuple[str, ...]  # labels of the operators sharing it
    entry: Any = None  # its own cache entry, when built as its own image
    image: Path | None = None  # its own image, when it has one (an xclbin chain)
    insts: Path | None = None  # its own instruction stream, likewise


@dataclass(frozen=True)
class Step:
    """One runlist step: which operator, on which design, over which buffers."""

    index: int
    operator: str
    design: str
    buffers: tuple[str, ...]


@dataclass(frozen=True)
class Artifacts:
    """The record of one image.

    ``kind`` is ``"elf"`` (one fused image) or ``"xclbin"`` (one image per
    design, chained; ``image`` is the last link). ``entry`` is the cache
    entry whose work directory holds the image's sidecars: the parameter
    table (``params``) and the lowered module (``lowered_mlir``).
    ``buffers`` maps each buffer name to ``(arena, offset, nbytes)``.
    """

    kind: str
    image: Path
    insts: Path | None
    entry: Any
    designs: tuple[Design, ...]
    steps: tuple[Step, ...]
    buffers: dict[str, tuple[str, int, int]]

    @property
    def params(self) -> Path | None:
        return getattr(self.entry, "params", None)

    @property
    def lowered_mlir(self) -> Path | None:
        return getattr(self.entry, "lowered_mlir", None)

    @property
    def directory(self) -> Path | None:
        return getattr(self.entry, "directory", None)

    def report(self, name: str = "") -> str:
        lines = [f"{name or 'image'}: {self.kind} {self.image}"]
        for d in self.designs:
            shared = f" (x{len(d.operators)})" if len(d.operators) > 1 else ""
            lines.append(f"  design {d.name}{shared}: {', '.join(d.operators)}")
        for s in self.steps:
            lines.append(f"  step {s.index}: {s.operator} on {s.design}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        def path(p):
            return None if p is None else str(p)

        def entry(e):
            if e is None:
                return None
            return {
                f.name: (
                    [str(x) for x in v]
                    if isinstance(v, tuple)
                    else path(v) if isinstance(v, Path) else v
                )
                for f in dataclasses.fields(e)
                for v in [getattr(e, f.name)]
            }

        return {
            "kind": self.kind,
            "image": str(self.image),
            "insts": path(self.insts),
            "entry": entry(self.entry),
            "designs": [
                {
                    "name": d.name,
                    "operators": list(d.operators),
                    "entry": entry(d.entry),
                    "image": path(d.image),
                    "insts": path(d.insts),
                }
                for d in self.designs
            ],
            "steps": [dataclasses.asdict(s) for s in self.steps],
            "buffers": {k: list(v) for k, v in self.buffers.items()},
        }

    def dump(self, path: Path | None = None) -> Path:
        """Write the record as JSON; beside the image by default."""
        path = Path(path) if path else Path(self.image).parent / "artifacts.json"
        path.write_text(json.dumps(self.to_dict(), indent=2))
        return path

    @staticmethod
    def load(path) -> dict:
        """A dumped record, as data; paths are strings."""
        return json.loads(Path(path).read_text())
