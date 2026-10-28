# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""NPU hardware tracing, read back after a run.

An operator built with ``trace=TraceConfig(...)`` (``aie.utils.trace``) traces the
workers its ``build()`` marks ``Worker(trace=)``, else its first. After ``run()``,
``dump_traces(run, path)`` writes mlir-aie's raw trace text and Perfetto JSON.
"""

from __future__ import annotations

import logging
from pathlib import Path

import numpy as np
from aie.utils.trace import TraceConfig, print_cycles_summary

from .image.callable import FullELFCallable, ImageCallable

__all__ = ["dump_traces"]

logger = logging.getLogger(__name__)


def dump_traces(
    run: ImageCallable,
    trace_file: str | Path,
    *,
    colshift: int | None = None,
    mlir: str | Path | None = None,
    summary: bool = True,
) -> list[Path]:
    """Write a completed run's trace buffer as text to ``trace_file`` and Perfetto
    JSON beside it, one per traced design; returns the JSON paths, empty on an
    untraced build, so a test can call it unconditionally.

    Args:
        colshift: None lets the parser align the columns, as a design may load
            into another column; override it when that picks the wrong ones.
        mlir: The lowered module the parser reads, else the build's own.
        summary: Also print mlir-aie's per-tile cycles summary for each.
    """
    if not isinstance(run, FullELFCallable):
        if run.op.traced:
            raise TypeError(
                f"{type(run).__name__} was built with tracing enabled but has no "
                "trace buffer; only the full-ELF sequence callable allocates one"
            )
        return []
    buffer = run.trace_buffer
    if buffer is None:
        return []

    trace_file = Path(trace_file)
    trace_file.parent.mkdir(parents=True, exist_ok=True)
    words = buffer.numpy().view(np.uint32).reshape(-1)
    config = TraceConfig(trace_size=words.nbytes, trace_file=str(trace_file))
    config.write_trace(words)
    if not words.any():
        logger.warning("trace buffer is all zeros, no trace data captured")
        return []

    mlir = mlir or run.lowered_mlir_path
    logger.info("parsing the trace against %s", mlir)
    try:
        written = config.trace_to_json(
            str(mlir),
            str(trace_file.with_suffix(".json")),
            colshift=colshift,
            kernel=f"{run.device_name}:{run.sequence_name}",
        )
    except Exception as exc:  # a visualisation failure must not fail a run
        logger.warning("trace parse failed (%s); raw words kept at %s", exc, trace_file)
        return []

    paths = [Path(p) for p in written]
    for path in paths:
        logger.info("trace written to %s", path)
        if summary:
            print_cycles_summary(path)
    return paths
