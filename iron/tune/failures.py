# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What went wrong while tuning, kept so a later toolchain can be checked
against it.

A ``Ledger`` holds one entry per failure signature: its kind (a compiler
crash, a build failure, a version not bit-identical, a device hang), the
device, the toolchain that first hit it, the diagnostic and a repro (the
composed MLIR module, gzipped, where one exists), and whether it is still
open. ``python -m iron.tune.failures`` lists the entries; ``--recheck``
places each compiler-side repro again with the current toolchain and marks
those that now pass as fixed by it.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime
import functools
import gzip
import hashlib
import json
import re
import subprocess
import tempfile
from enum import Enum
from pathlib import Path

import aie.utils.config as aie_config
from aie.utils.compile import NPU_CACHE_HOME

from iron.common.image.compose import _FIT_PIPELINE

# Per machine, beside the cost cache.
LEDGER = Path(NPU_CACHE_HOME) / "iron" / "tuner-failures"


class Kind(Enum):
    """What failed."""

    CRASH = "compiler crash"
    BUILD = "build failure"
    MISMATCH = "not bit-identical"
    HANG = "device hang"


@functools.cache
def toolchain() -> str:
    """The toolchain a failure is seen with: the aie-opt binary, by hash."""
    h = hashlib.sha256()
    with open(Path(aie_config.aiecc_path()).with_name("aie-opt"), "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()[:16]


def first_error(diagnostic: str) -> str:
    """``diagnostic``'s first line naming a failure: an assertion, an error or
    a crash, else its first line.
    """
    lines = diagnostic.strip().splitlines()
    marks = ("Assertion", "error", "Segmentation fault", "Aborted", "Stack dump")
    return next(
        (l for l in lines if any(m in l for m in marks)), lines[0] if lines else ""
    )


def signature(kind: Kind, diagnostic: str) -> str:
    """A failure's identity: its kind and its first error, with numbers,
    locations and addresses dropped so reruns collapse into one.
    """
    words = re.sub(
        r"0x[0-9a-f]+|\d+|[\w./-]+\.(mlir|py|cpp|h)", "#", first_error(diagnostic)
    )
    return f"{kind.value}: {words.strip()[:200]}"


def place(module: str) -> tuple[str, str | None]:
    """Run the fit pipeline on ``module`` in an ``aie-opt`` of its own, so a
    compiler crash ends that process, not the caller: ``("fits", None)``,
    ``("refused", diagnostic)`` or ``("crash", diagnostic)``.
    """
    with tempfile.NamedTemporaryFile("w", suffix=".mlir") as f:
        f.write(module)
        f.flush()
        done = subprocess.run(
            [
                str(Path(aie_config.aiecc_path()).with_name("aie-opt")),
                f"--pass-pipeline={_FIT_PIPELINE}",
                f.name,
                "-o",
                "/dev/null",
            ],
            capture_output=True,
            text=True,
        )
    if done.returncode == 0:
        return "fits", None
    crashed = done.returncode < 0 or "Stack dump" in done.stderr
    return ("crash" if crashed else "refused"), done.stderr[-4000:]


@dataclasses.dataclass
class Entry:
    """One failure signature: where it was first seen and whether it holds."""

    signature: str
    kind: str
    device: str
    toolchain: str
    first_seen: str
    context: str
    diagnostic: str
    repro: str | None = None
    status: str = "open"
    fixed_by: str | None = None
    issue: str | None = None


class Ledger:
    """The failures tuning has hit, one JSON line per signature in
    ``directory/ledger.jsonl``, each repro beside it by hash."""

    def __init__(self, directory: Path = LEDGER):
        self.directory = Path(directory)
        self.path = self.directory / "ledger.jsonl"

    def entries(self) -> list[Entry]:
        if not self.path.exists():
            return []
        return [
            Entry(**json.loads(line)) for line in self.path.read_text().splitlines()
        ]

    def _write(self, entries: list[Entry]) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        text = "".join(json.dumps(dataclasses.asdict(e)) + "\n" for e in entries)
        self.path.write_text(text)

    def record(
        self,
        kind: Kind,
        device: str,
        diagnostic: str,
        context: str,
        module: str | None = None,
    ) -> Entry:
        """The entry for this failure, added if its signature is new; a
        fixed one seen again is reopened.
        """
        entries = self.entries()
        sig = signature(kind, diagnostic)
        for entry in entries:
            if entry.signature == sig and entry.device == device:
                if entry.status != "open":
                    entry.status, entry.fixed_by = "open", None
                    self._write(entries)
                return entry
        repro = None
        if module is not None:
            data = gzip.compress(module.encode())
            repro = hashlib.sha256(data).hexdigest()[:16] + ".mlir.gz"
            self.directory.mkdir(parents=True, exist_ok=True)
            (self.directory / repro).write_bytes(data)
        entry = Entry(
            signature=sig,
            kind=kind.value,
            device=device,
            toolchain=toolchain(),
            first_seen=datetime.date.today().isoformat(),
            context=context,
            diagnostic=diagnostic[-2000:],
            repro=repro,
        )
        entries.append(entry)
        self._write(entries)
        return entry

    def recheck(self) -> list[tuple[Entry, str]]:
        """Place each open compiler-side entry's repro again with the current
        toolchain; one that now places or is refused cleanly is marked fixed
        by it. Returns each rechecked entry and its outcome.
        """
        entries = self.entries()
        out = []
        for entry in entries:
            if entry.status != "open" or entry.repro is None:
                continue
            if entry.kind not in (Kind.CRASH.value, Kind.BUILD.value):
                continue
            path = self.directory / entry.repro
            verdict, _ = place(gzip.decompress(path.read_bytes()).decode())
            if verdict != "crash" and entry.kind == Kind.CRASH.value:
                entry.status, entry.fixed_by = "fixed", toolchain()
            out.append((entry, verdict))
        self._write(entries)
        return out


def main() -> None:
    """List the ledger's entries, or recheck its compiler-side ones."""
    p = argparse.ArgumentParser(description="Failures tuning has hit")
    p.add_argument("--ledger", type=Path, default=LEDGER)
    p.add_argument("--recheck", action="store_true")
    args = p.parse_args()
    ledger = Ledger(args.ledger)
    if args.recheck:
        for entry, outcome in ledger.recheck():
            print(f"{entry.status:6s} {outcome:22s} {entry.signature}")
        return
    for entry in ledger.entries():
        fixed = f" (fixed by {entry.fixed_by})" if entry.fixed_by else ""
        print(f"{entry.status:6s} {entry.device:6s} {entry.signature}{fixed}")
        print(
            f"       first {entry.first_seen} with {entry.toolchain}: {entry.context}"
        )


if __name__ == "__main__":
    main()
