# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""NPU hardware tracing, both halves: switch it on at build, read it after a run.

:func:`maybe_enable_trace` is called by ``build_design`` while the program
is being built. Explicit ``trace_size`` wins; otherwise ``IRON_TRACE_SIZE``
decides, ``IRON_TRACE_NTILES`` (default 1) caps how many workers are traced
and 0 traces none. With neither set it is a no-op, so production paths are
unaffected.

:func:`dump_traces` is called after ``run()`` and writes what the buffer
holds::

    from iron.common.tracing import dump_traces

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
from aie.utils.trace import events as trace_events

from .image.callable import SequenceCallable, SequenceFullELFCallable

__all__ = [
    "maybe_enable_trace",
    "resolve_trace_size",
    "dump_traces",
]


# --------------------------------------------------------------------------
# Build time: switch tracing on
# --------------------------------------------------------------------------


def resolve_trace_size(trace_size=None):
    """Effective trace size: explicit argument first, then ``IRON_TRACE_SIZE``, else 0."""
    if trace_size and trace_size > 0:
        return int(trace_size)
    # Deliberately unguarded: a malformed IRON_TRACE_SIZE should raise rather than
    # silently disable tracing.
    return int(os.environ.get("IRON_TRACE_SIZE", "0"))


def _default_coretile_events():
    ev = trace_events
    return [
        ev.PortEvent(ev.CoreEvent.PORT_RUNNING_0, ev.WireBundle.DMA, 0, True),
        ev.PortEvent(ev.CoreEvent.PORT_RUNNING_1, ev.WireBundle.DMA, 1, True),
        ev.PortEvent(ev.CoreEvent.PORT_RUNNING_2, ev.WireBundle.DMA, 0, False),
        ev.CoreEvent.INSTR_EVENT_0,
        ev.CoreEvent.INSTR_EVENT_1,
        ev.CoreEvent.MEMORY_STALL,
        ev.CoreEvent.LOCK_STALL,
        ev.CoreEvent.INSTR_VECTOR,
    ]


def maybe_enable_trace(prog, trace_size, workers, coretile_events=None):
    """Configure per-op hardware trace if tracing is requested.

    Args:
        prog: the ``Program`` being built.
        trace_size: the design's ``trace_size`` argument (may be None/0).
        workers: the design's workers; the first ``IRON_TRACE_NTILES`` are traced.
        coretile_events: override the default core-tile event set.

    Returns:
        The effective trace size (0 when tracing is off and nothing was configured).
    """
    ts = resolve_trace_size(trace_size)
    if ts <= 0:
        return 0

    # A count, so 0 legitimately means "trace no tiles"; only negatives are
    # meaningless (a negative slice index would silently drop the LAST worker).
    ntiles = max(0, int(os.environ.get("IRON_TRACE_NTILES", "1")))

    prog.enable_trace(
        ts,
        workers=list(workers)[:ntiles],
        coretile_events=(
            coretile_events
            if coretile_events is not None
            else _default_coretile_events()
        ),
    )
    return ts


# --------------------------------------------------------------------------
# After the run: read the buffer back
# --------------------------------------------------------------------------

DEFAULT_TRACE_DIR = "outputs/traces"


def _slug(text: str) -> str:
    keep = "-_."
    return "".join(c if c.isalnum() or c in keep else "_" for c in text)


def dump_traces(
    run: SequenceCallable,
    tag: str,
    out_dir: str | Path | None = None,
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
    if not isinstance(run, SequenceFullELFCallable):
        if run.op.trace_size:
            raise TypeError(
                f"{type(run).__name__} was built with tracing enabled but has no "
                "trace buffer; only the full-ELF sequence callable allocates one."
            )
        return []
    buffer = run.trace_buffer
    if buffer is None:
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
