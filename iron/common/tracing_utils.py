# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Write a traced run's hardware trace buffer as Perfetto JSON.

Tracing is configured at build time (``IRON_TRACE_SIZE`` / ``IRON_TRACE_NTILES``,
read by the operator's design), and the runtime syncs the buffer device->host after
every dispatch. Call :func:`dump_traces` after ``run()`` to write it out:

    from iron.common.tracing_utils import dump_traces

    run = operator.get_callable()
    run()
    dump_traces(run, "my_operator")

On an untraced build the call returns an empty list, so a test can call it
unconditionally.

A dump writes the raw 32-bit words as hex text, plus one JSON file per traced
design for https://ui.perfetto.dev. Keep the text: :func:`parse_trace_buffer`
reparses it with a different column shift for the price of no further dispatch.

:func:`dump_traces` also prints mlir-aie's per-tile cycles summary for each file it
writes.

Environment:
  * ``IRON_TRACE_DIR``      where to write (default ``outputs/traces``)
  * ``IRON_TRACE_MLIR``     override the MLIR the parser reads
  * ``IRON_TRACE_COLSHIFT`` force the column shift; unset means auto-detect
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np

from aie.utils.trace import parse_trace_slices, print_cycles_summary

from . import compilation as comp

__all__ = [
    "dump_traces",
    "parse_trace_buffer",
    "lowered_mlir",
]

DEFAULT_TRACE_DIR = "outputs/traces"


def lowered_mlir(run) -> tuple[Path, str]:
    """The post-lowering MLIR for a callable, as ``(path, text)``.

    mlir-aie's trace parser matches ``aiex.npu.write32`` ops against the trace unit's
    config addresses. ``aie-insert-trace-flows`` emits those writes inside aiecc, so
    the parser needs aiecc's lowered module. A traced build requests it with
    ``--get-input-with-addresses``, which lands it in the work dir beside the source
    (``<source>.mlir.d/``).
    """
    override = os.environ.get("IRON_TRACE_MLIR")
    if override:
        path = Path(override)
        return path, path.read_text()

    source = Path(run.op.artifacts[0].mlir_input.filename)
    path = comp._aiecc_work_dir(str(source)) / "input_with_addresses.mlir"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} is missing; a traced build passes --get-input-with-addresses "
            "to aiecc. Point IRON_TRACE_MLIR at a lowered module to override."
        )
    return path, path.read_text()


def parse_trace_buffer(words, mlir_text: str, colshift: int | None = None):
    """A trace buffer's words as ``(slice_info, events)`` per traced design.

    The parser splits the buffer by the layout the compiler recorded on the
    dispatched sequence, and decodes each region against the device that wrote it.

    ``colshift`` of None lets the parser align the columns itself, which is what you
    want by default: a design configured for one column may be loaded into another.
    Override it when that alignment picks the wrong columns.

    The parser calls ``sys.exit`` on some malformed input, so SystemExit becomes a
    RuntimeError here: a visualisation failure must not fail a test.
    """
    try:
        return parse_trace_slices(
            np.asarray(words, dtype=np.uint32), mlir_text, colshift
        )
    except SystemExit as exc:
        raise RuntimeError(
            "mlir-aie's trace parser exited; the usual cause is an MLIR without the "
            "trace register writes, or a column shift that does not match the data. "
            "Run with logging at DEBUG to see the tiles it found."
        ) from exc


def _slug(text: str) -> str:
    keep = "-_."
    return "".join(c if c.isalnum() or c in keep else "_" for c in text)


def dump_traces(
    run,
    tag: str,
    out_dir=None,
    colshift: int | None = None,
    summary: bool = True,
) -> list[Path]:
    """Write a completed run's trace buffer as hex text and Perfetto JSON.

    Call it after ``run()``: the callable syncs its trace buffer device->host as part
    of the dispatch, so this only reads host memory. Returns the JSON paths written,
    empty on an untraced build.

    ``tag`` distinguishes one dump from another - a test name or parameter id. The
    layout the compiler recorded on the dispatched sequence splits the buffer, so a
    fused sequence yields one JSON file per configured design.
    """
    buffer = getattr(run, "trace_buffer", None)
    if buffer is None:
        if getattr(getattr(run, "op", None), "trace_size", 0):
            raise TypeError(
                f"{type(run).__name__} was built with tracing enabled but exposes no "
                "trace_buffer; only the full-ELF sequence callable allocates one."
            )
        return []

    out_dir = Path(out_dir or os.environ.get("IRON_TRACE_DIR", DEFAULT_TRACE_DIR))
    out_dir.mkdir(parents=True, exist_ok=True)

    if colshift is None:
        env = os.environ.get("IRON_TRACE_COLSHIFT")
        colshift = int(env) if env else None

    mlir_path, mlir_text = lowered_mlir(run)
    print(f"[trace] parsing against {mlir_path}")

    words = buffer.to_torch().numpy().astype(np.uint8).view(np.uint32)
    tag = _slug(tag)
    raw = (out_dir / tag).with_suffix(".txt")
    raw.write_text("\n".join(f"{w:08x}" for w in words) + "\n")
    if not words.any():
        print("[trace] buffer is all zeros, no trace data captured")
        return []

    try:
        parsed = parse_trace_buffer(words, mlir_text, colshift)
    except Exception as exc:  # a visualisation failure must not fail a run
        print(f"[trace] parse failed ({exc}); raw words kept at {raw}")
        return []

    written = []
    for index, (entry, events) in enumerate(parsed):
        # A device may hold several runtime sequences, so both names identify a slice.
        name = f"{index}_{entry['device']}_{entry['sequence']}" if entry else "trace"
        if entry and words[(entry["offset"] + entry["size"]) // 4 - 1]:
            print(
                f"[trace] {name}: slice full ({entry['size']} B), trace is likely "
                "truncated - raise IRON_TRACE_SIZE"
            )

        target = (out_dir / f"{tag}_{_slug(name)}").with_suffix(".json")
        target.write_text(json.dumps(events))
        print(f"[trace] {target} ({len(events)} events)")
        written.append(target)

        if summary:
            print_cycles_summary(target)
    return written
