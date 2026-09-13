# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One content-addressed cache primitive for every compile-artifact cache in this tree.

Three independent artifact caches in this codebase have each, independently, defaulted to
mtime-as-identity (`@iron.jit`'s original `_hash.py`, `ExternalFunction._content_digest`, and
`CompilationArtifact.is_available_in_filesystem`) -- fixing one never fixed the others. The
recurring failure was never "forgot to hash content"; it was a caller hand-enumerating "the
inputs" and missing one (an included header, a downstream flag). This module removes the caller
from that job: identity comes from what the compiler itself says it read (its `-MD`/`-MF`
depfile), not from a hand-maintained list.

    key = content_key(inputs, flags, toolchain_fingerprint)
    store = ContentStore(root)          # path = key, never a caller-chosen name
    store.get(key)  -> Path | None       # None means "not built with this exact identity, ever"
    store.put(key, src_path) -> Path

mtime never appears in a key. It is a legitimate memoization hint for OTHER callers deciding
whether to re-hash an unchanged file, but this module always reads bytes: the cost that matters
here is compiling, not hashing a handful of kernel sources.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import tempfile
from pathlib import Path
from typing import Iterable, Mapping, Sequence

__all__ = ["content_digest", "parse_depfile", "content_key", "ContentStore"]

# Streamed so a large input (a linked archive, not just a kernel source) cannot pull the whole
# file into memory before it can be hashed.
_DIGEST_CHUNK = 1 << 20


def content_digest(path: str | Path) -> str:
    """sha256 of a file's bytes, streamed.

    Fail-closed, not fail-open: an input this cannot read (missing, permission error, a
    directory where a file was expected) returns a marker naming the failure instead of
    raising or being skipped. A skipped input silently drops out of the key -- a caller-side
    "forgot to declare a dependency" with extra steps. A marker guarantees the key differs from
    any run where the same input WAS readable, so a broken input can only ever miss the cache,
    never ride a stale hit under a shortened key.
    """
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            while chunk := fh.read(_DIGEST_CHUNK):
                h.update(chunk)
    except OSError as exc:
        return f"<unreadable:{type(exc).__name__}:{exc.errno}>"
    return h.hexdigest()


def parse_depfile(path: str | Path) -> list[str]:
    """Return the prerequisite paths a `-MD -MF <path>` depfile names, dropping the target.

    Returns [] for a missing or unparsable depfile rather than raising -- the caller folds
    that into content_key() as an ordinary (absent) input via its own fail-closed digest, so a
    missing depfile still changes the key rather than silently narrowing the input set.

    Hand-scans rather than `str.split()`: `-MF`'s own escaping backslash-escapes a space or a
    literal backslash in a path (clang/gcc agree on this), and `str.split()` would split ON
    that escaped space before a regex could see the backslash preceding it. It deliberately
    does not attempt full Make-quoting semantics beyond those two sequences, which the depfile
    format itself never uses.
    """
    try:
        text = Path(path).read_text()
    except OSError:
        return []
    # Join continuation lines, then split the first (only) rule on its ':'.
    joined = text.replace("\\\n", " ")
    _, sep, rest = joined.partition(":")
    if not sep:
        return []
    deps: list[str] = []
    token: list[str] = []
    i, n = 0, len(rest)
    while i < n:
        c = rest[i]
        if c == "\\" and i + 1 < n and rest[i + 1] in (" ", "\\"):
            token.append(rest[i + 1])
            i += 2
            continue
        if c.isspace():
            if token:
                deps.append("".join(token))
                token = []
            i += 1
            continue
        token.append(c)
        i += 1
    if token:
        deps.append("".join(token))
    return deps


def content_key(
    inputs: Iterable[str | Path],
    flags: Mapping[str, object],
    toolchain_fingerprint: str,
) -> str:
    """The one content-addressed key every cache site in this tree should compute from.

    `inputs` -- every file whose bytes can change the output. Pass the compiler's own
    dependency list (parse_depfile()'s return, or equivalent), not a hand-enumerated guess:
    every prior instance of this defect class was a caller enumerating "the inputs" and
    missing one. Order-independent (sorted before hashing).

    `flags` -- the build's own configuration as a plain, JSON-scalar-valued mapping (compiler
    flags, symbol renames, a row-batch count, anything that changes the output without
    changing which files are read). Order-independent (sorted by key); values are stringified
    with `repr` so `1` and `"1"` do not collide.

    `toolchain_fingerprint` -- an opaque string identifying the compiler/toolchain build.
    Callers should stamp this once (e.g. from a toolchain instance's own content-addressed
    id, or a compiler binary's own `--version` output) rather than re-hashing toolchain
    binaries on every lookup -- this function treats it as a black box either way.
    """
    h = hashlib.sha256()
    h.update(b"content-key-v1\0")
    for p in sorted(str(p) for p in inputs):
        h.update(p.encode())
        h.update(b"\0")
        h.update(content_digest(p).encode())
        h.update(b"\0")
    for k in sorted(flags, key=str):
        h.update(repr(k).encode())
        h.update(b"=")
        h.update(repr(flags[k]).encode())
        h.update(b"\0")
    h.update(b"toolchain\0")
    h.update(toolchain_fingerprint.encode())
    return h.hexdigest()


class ContentStore:
    """Content-addressed artifact store: a slot's path is a pure function of its key.

    This is the property that kills a collision class structurally instead of merely
    detecting one instance of it: two builds can only land in the same slot if they are
    byte-for-byte the same logical input, by construction of `content_key`. A hand-added
    special case (namespace kernel objects by arch; suffix a sequence name by a flag someone
    remembered) closes exactly the axis it was written for and reopens on the next one nobody
    has hit yet; this does not have an axis to remember.
    """

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)

    def _slot(self, key: str) -> Path:
        # Git-style sharding (2 hex chars -> 256 subdirectories) keeps any one directory's
        # listing small at scale; the split point itself is arbitrary.
        return self.root / key[:2] / key

    def get(self, key: str) -> Path | None:
        """The stored path for `key`, or None if this exact identity was never built."""
        slot = self._slot(key)
        return slot if slot.exists() else None

    def put(self, key: str, src: str | Path) -> Path:
        """Copy `src`'s bytes into the store under `key`, atomically.

        Idempotent by construction: if `key` is already present, its bytes are ALREADY what
        `src` would produce (same key implies same content), so a second `put` for the same
        key is a no-op rather than a redundant copy or a correctness question. Writes go to a
        sibling temp file first, then `os.replace` -- a reader can only ever observe either no
        entry or a complete one, and two concurrent writers computing the same key race
        harmlessly (both write the same bytes; whichever `replace` lands last wins, over
        identical content).
        """
        slot = self._slot(key)
        slot.parent.mkdir(parents=True, exist_ok=True)
        if slot.exists():
            return slot
        fd, tmp_name = tempfile.mkstemp(dir=slot.parent, prefix=".tmp-")
        os.close(fd)
        tmp = Path(tmp_name)
        try:
            shutil.copyfile(src, tmp)
            os.replace(tmp, slot)
        except BaseException:
            tmp.unlink(missing_ok=True)
            raise
        return slot
