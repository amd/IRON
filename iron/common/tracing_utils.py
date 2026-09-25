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

The writing and decoding are mlir-aie's ``TraceConfig``: a dump is its raw trace
text, which ``TraceConfig.read_trace`` reads back to reparse without a further
dispatch, plus one JSON file per traced design for https://ui.perfetto.dev.
:func:`dump_traces` also prints mlir-aie's per-tile cycles summary for each.

Environment:
  * ``IRON_TRACE_DIR``      where to write (default ``outputs/traces``)
  * ``IRON_TRACE_MLIR``     override the MLIR the parser reads
  * ``IRON_TRACE_COLSHIFT`` force the column shift; unset means auto-detect
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np

from aie.utils.trace import TraceConfig, print_cycles_summary

__all__ = ["dump_traces"]

DEFAULT_TRACE_DIR = "outputs/traces"


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
    """Write a completed run's trace buffer as trace text and Perfetto JSON.

    Call it after ``run()``: the callable syncs its trace buffer device->host as part
    of the dispatch, so this only reads host memory. Returns the JSON paths written,
    empty on an untraced build.

    ``tag`` distinguishes one dump from another - a test name or parameter id. The
    text goes to ``<tag>.txt``. A fused sequence shares the buffer between the
    designs it configures, and each gets its own
    ``<tag>_<index>_<device>_<sequence>.json``; otherwise the JSON is ``<tag>.json``.

    ``colshift`` of None lets the parser align the columns itself, which is what you
    want by default: a design configured for one column may be loaded into another.
    Override it when that alignment picks the wrong columns.
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

    words = buffer.numpy().view(np.uint32).reshape(-1)
    tag = _slug(tag)
    config = TraceConfig(
        trace_size=words.nbytes, trace_file=str(out_dir / f"{tag}.txt")
    )
    config.write_trace(words)
    if not words.any():
        print("[trace] buffer is all zeros, no trace data captured")
        return []

    mlir = os.environ.get("IRON_TRACE_MLIR") or run.lowered_mlir_path
    print(f"[trace] parsing against {mlir}")
    try:
        written = config.trace_to_json(
            str(mlir),
            str(out_dir / f"{tag}.json"),
            colshift=colshift,
            kernel=f"{run.device_name}:{run.sequence_name}",
        )
    except Exception as exc:  # a visualisation failure must not fail a run
        print(f"[trace] parse failed ({exc}); raw words kept at {config.trace_file}")
        return []

    paths = [Path(p) for p in written]
    for path in paths:
        print(f"[trace] {path}")
        if summary:
            print_cycles_summary(path)
    return paths
