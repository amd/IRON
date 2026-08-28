# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Read a traced run's hardware trace buffers back and write Perfetto JSON.

Tracing is configured at build time (``IRON_TRACE_SIZE`` / ``IRON_TRACE_NTILES``,
consumed by the operator's design) and the runtime already syncs the resulting
buffers device->host after every dispatch. Nothing reads them, though, so a traced
run leaves its data sitting in host memory. This module is that last step: one call
after ``run()`` turns those buffers into files.

    from iron.common.tracing_utils import dump_traces

    run = operator.get_callable()
    run()
    dump_traces(run, "my_operator")

No-op on an untraced build, so the call can stay in a test unconditionally.

Two files land per traced dispatch: the raw 32-bit words as hex text, and the
parsed JSON for https://ui.perfetto.dev. The raw text is kept because reparsing is
free and re-dispatching is not - see :func:`parse_trace_words` to reparse it with a
different column shift without touching the device.

``dump_traces`` also prints a per-tile summary, since the Perfetto timeline of a
few hundred short kernel calls is hard to read at a glance and the numbers a
designer wants - how much of the run a core spent computing, and how much waiting -
are a few sums away. :func:`print_trace_summary` does the same for a JSON file
written earlier.

Environment:
  * ``IRON_TRACE_DIR``      where to write (default ``outputs/traces``)
  * ``IRON_TRACE_MLIR``     override the MLIR the parser reads (see below)
  * ``IRON_TRACE_COLSHIFT`` force the column shift; unset means auto-detect
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np

from . import compilation as comp

__all__ = [
    "dump_traces",
    "parse_trace_words",
    "lowered_mlir",
    "trace_words",
    "summarize_trace",
    "print_trace_summary",
]

DEFAULT_TRACE_DIR = "outputs/traces"

# The kernel brackets: aie_kernels sources wrap their body in event0()/event1(),
# so one pair is one kernel invocation. Everything between two pairs is the core
# waiting - on its input object FIFO, on a lock, on the next descriptor.
KERNEL_START, KERNEL_END = "INSTR_EVENT_0", "INSTR_EVENT_1"


def lowered_mlir(run) -> tuple[Path, str]:
    """The post-lowering MLIR for a callable, as ``(path, text)``.

    mlir-aie's trace parser recovers which tiles and events were traced by scanning
    for ``aiex.npu.write32`` ops and pattern-matching the trace-unit config
    addresses. It does not understand the declarative ``aie.trace`` ops a design is
    written with, so the module handed to aiecc is useless to it: those ops only
    become register writes inside aiecc, in ``aie-insert-trace-flows``. A traced
    build asks aiecc for ``--get-input-with-addresses``, which lands the lowered
    module in the work dir beside the source (``<source>.mlir.d/``).
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


def trace_words(buf) -> np.ndarray:
    """A trace buffer's contents as uint32 words, with the unfilled tail dropped.

    The buffer is allocated at the full trace size and only partly written, so the
    trailing zeros are absence of events rather than events. Trimming them keeps the
    JSON small and stops the parser inventing a long idle tail.
    """
    raw = buf.to_torch().numpy().astype(np.uint8)
    raw = raw[: raw.size - raw.size % 4]
    words = raw.view(np.uint32)  # little-endian on x86, matching the DMA layout
    if not words.any():
        return words[:0]
    return words[: int(np.nonzero(words)[0][-1]) + 1]


def parse_trace_words(
    words, mlir_text: str, colshift: int | None = None, device: str | None = None
):
    """Trace words plus the lowered MLIR into Trace Event Format events.

    ``colshift`` of None lets the parser align the columns itself, which is what you
    want by default: a design configured for one column may be loaded into another.
    Override it only when the tiles in the output do not match the placement.

    ``device`` names the ``aie.device`` whose trace configuration these words were
    written by. A fused sequence holds one per sub-design, and they routinely share
    tile coordinates, so leaving it unset merges their event assignments.

    The parser calls ``sys.exit`` rather than raising on some malformed input, so
    SystemExit is caught here - a visualisation failure should never take a test
    down with it.
    """
    from aie.utils.trace.parse import parse_trace

    try:
        return parse_trace(
            np.asarray(words, dtype=np.uint32), mlir_text, colshift, device
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


def _by_tile(events):
    """Group Trace Event Format records by pid, resolving each pid's tile name.

    The parser emits one process per traced tile (``process_name`` metadata), and
    one thread per monitored event slot. Metadata records carry no timestamp, so
    they are separated out here rather than filtered at every use.
    """
    names, records = {}, {}
    for index, event in enumerate(events):
        pid = event.get("pid")
        if event.get("ph") == "M":
            if event.get("name") == "process_name":
                names[pid] = event.get("args", {}).get("name", str(pid))
            continue
        if "ts" in event:
            records.setdefault(pid, []).append((event["ts"], index, event))
    for pid in records:
        records[pid].sort()  # index breaks ts ties, keeping emission order
    return names, records


def _state_cycles(records):
    """Cycles each event name was asserted, summed over its begin/end intervals.

    A level event (a stall, vector activity) is emitted as ``B``/``E`` pairs on its
    own thread, re-asserted at every trace command, so one logical stall arrives as
    many short intervals. Summing them gives the time in that state. These overlap
    each other and the kernel brackets - a core stalls *during* a kernel call - so
    they are shares of the window, not a partition of it.
    """
    open_at, totals = {}, {}
    for ts, _, event in records:
        key = (event.get("tid"), event.get("name"))
        if event.get("ph") == "B":
            open_at.setdefault(key, ts)
        elif event.get("ph") == "E" and key in open_at:
            totals[key[1]] = totals.get(key[1], 0) + ts - open_at.pop(key)
    return totals


def _invocations(records):
    """Kernel invocations as ``(start, end)`` cycle pairs.

    Pairs each ``event0`` with the next ``event1``, ignoring repeats of either -
    the same rule mlir-aie's own summary uses, so the call counts agree.
    """
    spans, start = [], None
    for ts, _, event in records:
        if event.get("ph") != "B":
            continue
        if event.get("name") == KERNEL_START and start is None:
            start = ts
        elif event.get("name") == KERNEL_END and start is not None:
            spans.append((start, ts))
            start = None
    return spans


def _stats(values):
    if not values:
        return None
    ordered = sorted(values)
    return {
        "count": len(ordered),
        "total": sum(ordered),
        "min": ordered[0],
        "max": ordered[-1],
        "mean": sum(ordered) / len(ordered),
    }


def summarize_trace(source) -> dict:
    """Per-tile cycle accounting for a parsed trace.

    Accepts a JSON path or an already-parsed event list. Returns
    ``{tile_name: {...}}`` with, per tile: the traced ``window`` in cycles, the
    kernel invocations (``busy``), the gaps between them (``waiting``), and the
    cycles spent in each monitored state.

    All figures are AIE core cycles, from the trace unit's own timer.
    """
    if isinstance(source, (str, Path)):
        source = json.loads(Path(source).read_text())

    names, per_pid = _by_tile(source)
    summary = {}
    for pid, records in per_pid.items():
        window = records[-1][0] - records[0][0]
        spans = _invocations(records)
        busy = _stats([end - start for start, end in spans])
        waiting = _stats([nxt[0] - cur[1] for cur, nxt in zip(spans, spans[1:])])
        summary[names.get(pid, str(pid))] = {
            "window": window,
            "busy": busy,
            "waiting": waiting,
            "states": _state_cycles(records),
        }
    return summary


def _pct(part, whole):
    return f"{100.0 * part / whole:5.1f}%" if whole else "    -"


def print_trace_summary(source, title: str | None = None) -> dict:
    """Print :func:`summarize_trace` as a short per-tile report, and return it.

    Reads as: how much of the traced window each core spent inside a kernel, how
    much it spent between kernels, and what it was stalled on meanwhile.
    """
    summary = summarize_trace(source)
    if title is None and isinstance(source, (str, Path)):
        title = Path(source).name
    if title:
        print(f"\n[trace] {title}")

    for tile, data in summary.items():
        window = data["window"]
        busy, waiting = data["busy"], data["waiting"]
        print(f"  {tile}  -  {window} cycles traced")

        if busy:
            print(
                f"    in kernel  {busy['count']:>6} calls  {busy['total']:>10} cyc  "
                f"{_pct(busy['total'], window)}   "
                f"min/mean/max {busy['min']}/{busy['mean']:.1f}/{busy['max']}"
            )
        else:
            print(
                f"    in kernel       no {KERNEL_START}/{KERNEL_END} pairs - does "
                "this kernel call event0()/event1()?"
            )
        if waiting:
            print(
                f"    between    {waiting['count']:>6} gaps   "
                f"{waiting['total']:>10} cyc  {_pct(waiting['total'], window)}   "
                f"min/mean/max {waiting['min']}/{waiting['mean']:.1f}/{waiting['max']}"
            )

        # Stalls and vector activity overlap the above, so they are listed apart.
        states = {
            name: cycles
            for name, cycles in data["states"].items()
            if name not in (KERNEL_START, KERNEL_END) and cycles
        }
        for name, cycles in sorted(states.items(), key=lambda s: -s[1]):
            print(f"    {name.lower():<12} {cycles:>22} cyc  {_pct(cycles, window)}")
    if summary:
        print(
            "    (stall and vector shares overlap the kernel time above, "
            "they are not a partition)"
        )
    return summary


def dump_traces(
    run,
    tag: str,
    out_dir=None,
    colshift: int | None = None,
    summary: bool = True,
) -> list[Path]:
    """Write every trace buffer of a completed run out as hex text and Perfetto JSON.

    Call it after ``run()``: the callable syncs its trace buffers device->host as
    part of the dispatch, so this only reads host memory. Returns the JSON paths
    written, empty on an untraced build.

    ``tag`` distinguishes one dump from another - a test name or parameter id. The
    buffer is split by the layout the compiler recorded on the dispatched sequence,
    so a fused sequence yields one pair of files per configured design.
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

    all_words = buffer.to_torch().numpy().astype(np.uint8).view(np.uint32)
    tag = _slug(tag)
    written = []
    for index, entry in enumerate(run.trace_slices):
        name = f"{index}_{entry['device']}"
        start = entry["offset"] // 4
        region = all_words[start : start + entry["size"] // 4]
        words = region[: int(np.nonzero(region)[0][-1]) + 1] if region.any() else region
        if not words.size:
            print(f"[trace] {name}: buffer is all zeros, no trace data captured")
            continue
        if words.size == region.size:
            print(
                f"[trace] {name}: slice full ({entry['size']} B), trace is likely "
                "truncated - raise IRON_TRACE_SIZE"
            )

        stem = out_dir / f"{tag}_{_slug(name)}"
        stem.with_suffix(".txt").write_text("\n".join(f"{w:08x}" for w in words) + "\n")

        try:
            events = parse_trace_words(words, mlir_text, colshift, entry["device"])
        except Exception as exc:  # never let a visualisation failure fail a run
            print(f"[trace] {name}: parse failed ({exc}); raw words kept at {stem}.txt")
            continue

        target = stem.with_suffix(".json")
        target.write_text(json.dumps(events))
        print(f"[trace] {target} ({len(events)} events)")
        written.append(target)

        if summary:
            try:
                print_trace_summary(events, title=target.name)
            except Exception as exc:  # a summary is never worth failing a run over
                print(f"[trace] {name}: summary failed ({exc})")
    return written
