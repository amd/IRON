# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Loading stream-dse generated designs into IRON, independent of the operator; a
stream-backed operator's module holds only its workload, mapping and dimensions."""

import hashlib
import os
import re
from functools import lru_cache
from pathlib import Path

__all__ = [
    "stream_revision",
    "region_module",
    "group_dir",
    "design_paths",
    "group_text",
    "design_digest",
    "trace_size",
    "trace_tiles",
    "traced_tiles",
    "traced_ports",
]

_MEMTILE_PACKET = 3
_EVENT_SLOTS = 8


@lru_cache(maxsize=None)
def stream_revision() -> str:
    """Token over the installed stream package's sources, so a stream-side change
    rebuilds cached designs. File mtimes, not the commit, so uncommitted edits count."""
    import stream

    root = Path(stream.__file__).parent
    stamps = sorted(
        (str(path.relative_to(root)), path.stat().st_mtime_ns)
        for pattern in ("*.py", "*.yaml")
        for path in root.rglob(pattern)
    )
    return hashlib.sha256(f"{stream.__version__}{stamps}".encode()).hexdigest()[:8]


def region_module(mlir_text: str):
    """Parse a group's xDSL-emitted MLIR into an ``aie`` module, since
    ``OperatorSequence`` consumes ``aie.DeviceOp`` objects."""
    from aie import ir
    from aie.extras.context import mlir_mod_ctx

    with mlir_mod_ctx():
        return ir.Module.parse(mlir_text)


def group_dir(output_dir: str, index: int) -> str:
    """Where stream-dse writes one fused group's design and its ``kernels.json``."""
    return os.path.join(output_dir, f"group_{index}", "codegen")


def design_paths(output_dir: str, n_groups: int) -> list[str]:
    """Where stream-dse writes each fused group's MLIR."""
    return [
        os.path.join(group_dir(output_dir, index), "final.mlir")
        for index in range(n_groups)
    ]


def group_text(group_index: int, paths: list[str], generate) -> str:
    """One group's generated MLIR, generating the whole design first if any group's
    file is missing."""
    if not all(os.path.exists(path) for path in paths):
        generate()
    text = Path(paths[group_index]).read_text()
    ports = traced_ports()
    return _watch_dma_ports(text, ports) if ports else text


def _watch_dma_ports(mlir_text: str, ports) -> str:
    """The design with every traced memory tile counting cycles its DMA ``ports`` run, in
    place of the DMA events stream gives it, which name no channel."""
    from aie import ir
    from aie.dialects import aie
    from aie.extras.context import mlir_mod_ctx

    with mlir_mod_ctx():
        module = ir.Module.parse(mlir_text)
        for device in module.body.operations:
            for trace in device.regions[0].blocks[0].operations:
                if trace.operation.name != "aie.trace":
                    continue
                body = trace.regions[0].blocks[0]
                ops = {op.operation.name: op for op in body.operations}
                packet = ops.get("aie.trace.packet")
                if packet is None or (
                    ir.IntegerAttr(packet.operation.attributes["type"]).value
                    != _MEMTILE_PACKET
                ):
                    continue
                if "aie.trace.start" not in ops:
                    raise ValueError("a memory tile trace has no aie.trace.start")
                for op in list(body.operations):
                    if op.operation.name == "aie.trace.event":
                        op.operation.erase()
                with ir.InsertionPoint(ops["aie.trace.start"]):
                    for slot, (direction, channel) in enumerate(ports):
                        aie.trace_port(
                            slot,
                            aie.WireBundle.DMA,
                            channel,
                            getattr(aie.DMAChannelDir, direction),
                        )
                    for slot in range(_EVENT_SLOTS):
                        aie.trace_event(
                            f"PORT_RUNNING_{slot}" if slot < len(ports) else "NONE"
                        )
        return str(module)


def design_digest(mlir_text: str) -> str:
    """Digest of a group's design, for recognising groups that share one."""
    return hashlib.sha256(mlir_text.encode()).hexdigest()


def trace_size() -> int:
    """DDR trace buffer in bytes, 0 for an untraced build. Opt-in: tracing adds a
    runtime-sequence argument, so it changes the ABI."""
    return int(os.environ.get("IRON_TRACE_SIZE", "0"))


def trace_tiles() -> int:
    """How many tiles to trace. Routing, not the packet id space, is the real limit."""
    return int(os.environ.get("IRON_TRACE_NTILES", "4"))


def traced_ports() -> tuple[tuple[str, int], ...]:
    """The DMA ports a traced memory tile watches, from ``IRON_TRACE_PORTS="S2MM:0,MM2S:0"``,
    eight at most; empty keeps the events stream gives it."""
    spec = os.environ.get("IRON_TRACE_PORTS", "")
    ports = tuple(
        (direction, int(channel))
        for direction, channel in (port.split(":") for port in spec.split(",") if port)
    )
    bad = [direction for direction, _ in ports if direction not in ("S2MM", "MM2S")]
    if bad:
        raise ValueError(f"IRON_TRACE_PORTS directions must be S2MM or MM2S, not {bad}")
    if len(ports) > _EVENT_SLOTS:
        raise ValueError(f"a trace unit watches {_EVENT_SLOTS} ports, not {len(ports)}")
    return ports


def traced_tiles() -> tuple[tuple[int, int], ...]:
    """The (column, row) tiles to trace, from ``IRON_TRACE_TILES="col,row;col,row"``; empty
    leaves the choice to stream. A memory tile in the list is traced at its DMA."""
    spec = os.environ.get("IRON_TRACE_TILES", "")
    return tuple(
        tuple(int(v) for v in tile.split(",")) for tile in spec.split(";") if tile
    )
