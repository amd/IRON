# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Shared per-op NPU hardware-trace wiring for the iron/operators designs.

Semantics:
  * explicit ``trace_size`` wins; otherwise fall back to ``IRON_TRACE_SIZE``
  * ``IRON_TRACE_NTILES`` (default 1) caps how many workers get traced; 0 traces none
  * no-op when neither is set, so production paths are unaffected
"""

import os

__all__ = ["maybe_enable_trace", "resolve_trace_size"]


def resolve_trace_size(trace_size=None):
    """Effective trace size: explicit argument first, then ``IRON_TRACE_SIZE``, else 0."""
    if trace_size and trace_size > 0:
        return int(trace_size)
    # Deliberately unguarded: a malformed IRON_TRACE_SIZE should raise rather than
    # silently disable tracing.
    return int(os.environ.get("IRON_TRACE_SIZE", "0"))


def _default_coretile_events():
    import aie.utils.trace as trace_utils

    ev = trace_utils.events
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


def maybe_enable_trace(rt, trace_size, workers, coretile_events=None):
    """Configure per-op hardware trace on ``rt`` if tracing is requested.

    Call inside the ``rt.sequence(...)`` block, before ``rt.start(...)``.

    Args:
        rt: the ``Runtime`` being built.
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

    rt.enable_trace(
        ts,
        workers=list(workers)[:ntiles],
        coretile_events=(
            coretile_events
            if coretile_events is not None
            else _default_coretile_events()
        ),
    )
    return ts
