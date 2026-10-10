# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""NPU hardware tracing, read back after a run.

An operator is traced when it is built with a ``trace``
(``aie.utils.trace.TraceConfig``): ``build_design`` switches the trace
on for the workers its ``array()`` marks with ``Worker(trace=)``, or its
first. A sequence holding a traced operator carries one trace buffer, and
``dump_traces`` is called after ``run()`` to write what it holds:

```python
from aie.utils.trace import TraceConfig
from iron.common.tracing import dump_traces

norm = LayerNorm(..., trace=TraceConfig(8192))
...
run = sequence.get_callable()
run()
dump_traces(run, "layer_norm.txt")
```

On an untraced build the call returns an empty list, so a test can call it
unconditionally.

The writing and decoding are mlir-aie's ``TraceConfig``: a dump is its raw trace
text, which ``TraceConfig.read_trace`` reads back to reparse without a further
dispatch, plus one JSON file per traced design for https://ui.perfetto.dev.
``dump_traces`` also prints mlir-aie's per-tile cycles summary for each.
"""

from __future__ import annotations

import logging
from pathlib import Path

import numpy as np
from aie.utils.trace import TraceConfig, print_cycles_summary

from .image.callable import FullELFCallable, StepCallable

__all__ = ["dump_traces"]

logger = logging.getLogger(__name__)


def dump_traces(
    run: FullELFCallable | StepCallable,
    trace_file: str | Path,
    *,
    colshift: int | None = None,
    mlir: str | Path | None = None,
    summary: bool = True,
) -> list[Path]:
    """Write a completed run's trace buffer as trace text and Perfetto JSON.

    Call it after ``run()``; it reads the trace buffer back from the device.
    Returns the JSON paths written, empty on an untraced build.

    The text goes to ``trace_file`` and the JSON beside it, under its stem: a
    fused sequence shares the buffer between the designs it configures, and each
    gets its own ``<stem>_<index>_<device>_<sequence>.json``; otherwise the JSON
    is ``<stem>.json``.

    ``colshift`` of None lets the parser align the columns itself, which is what you
    want by default: a design configured for one column may be loaded into another.
    Override it when that alignment picks the wrong columns. ``mlir`` is the
    lowered module the parser reads, the build's own unless given.
    """
    if not isinstance(run, FullELFCallable):
        if run.op.traced:
            raise TypeError(
                f"{type(run).__name__} was built with tracing enabled but has no "
                "trace buffer; only the full-ELF sequence callable allocates one."
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
