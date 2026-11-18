# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operand's per-firing objectFIFO pattern, read from its operator's own build.

``firings(op)`` builds ``op``'s array once and walks each core's
``aie.objectfifo.acquire``/``release`` ops to say, per operand, what one
firing moves: a prologue of firings issued before any loop, the firing one
loop iteration issues (and at which nesting depth), and an epilogue issued
after. An objectFIFO reached only through a memtile link (GEMM's split,
forward or join) is still found, through the ``aie.objectfifo.link`` ops
that connect it to the operand's own fifo.
"""

from __future__ import annotations

import dataclasses

from aie import ir
from aie.dialects.aie import CoreOp, DeviceOp, ObjectFifoLinkOp

from ..declare import Operator
from ..design import BuiltArray, OperatorDesign

_ACQUIRE = "aie.objectfifo.acquire"
_RELEASE = "aie.objectfifo.release"
_FOR = "scf.for"
_WHILE = "scf.while"


@dataclasses.dataclass(frozen=True)
class Access:
    """One ``objectfifo.acquire`` or ``objectfifo.release`` a core issues.

    Attributes:
        acquire: Whether this is an acquire (``False`` is a release).
        count: The objects it names.
    """

    acquire: bool
    count: int


@dataclasses.dataclass(frozen=True)
class Pattern:
    """One operand's per-firing pattern, read off the fifo its core touches.

    ``prologue`` and ``epilogue`` are the firings issued before and after
    the loop nest, in program order, outside any loop. ``steady`` is what
    one iteration of the loop issues, at ``steady_depth`` (1 the outermost
    ``scf.for``; GEMM's K loop, nested in its tile loop, is 2); an operand
    no loop touches has an empty ``steady`` and ``steady_depth`` 0.

    A firing straight-line code issues more than once (an unrolled ramp-up)
    is one entry per occurrence, in order; a loop whose trip count is a
    per-call value contributes its body once, since the body is the same
    every iteration.

    Attributes:
        prologue: Firings before the loop nest.
        steady: One iteration's firings, at ``steady_depth``.
        steady_depth: The loop nesting depth ``steady`` is read from, 0 with none.
        epilogue: Firings after the loop nest.
    """

    prologue: tuple[Access, ...]
    steady: tuple[Access, ...]
    steady_depth: int
    epilogue: tuple[Access, ...]


def _call_body(core: CoreOp) -> list[ir.Operation]:
    """Return the ops a full ELF's call runs: the ``do`` region of its ``scf.while``.

    The core's own ops, unchanged, where it loops no call at all.
    """
    ops = list(core.operation.regions[0].blocks[0].operations)
    for op in ops:
        if op.name == _WHILE:
            return list(op.regions[1].blocks[0].operations)
    return ops


def _scan(
    ops: list[ir.Operation],
    depth: int,
    prologue: dict[str, list[Access]],
    steady: dict[str, list[tuple[int, Access]]],
    epilogue: dict[str, list[Access]],
    past_loop: bool,
) -> None:
    """Walk ``ops`` (one core's, at loop nesting ``depth``), filling the three dicts by fifo name.

    At depth 0, an op before the (one) top-level ``scf.for`` is a prologue
    firing, one after is an epilogue firing; inside any loop, depth and
    code order no longer matter to the result, so every acquire or release
    found there, however deep, is a steady firing at the depth it sits.
    """
    for op in ops:
        name = op.name
        if name == _ACQUIRE:
            fifo = ir.FlatSymbolRefAttr(op.attributes["objFifo_name"]).value
            access = Access(True, len(op.results))
        elif name == _RELEASE:
            fifo = ir.FlatSymbolRefAttr(op.attributes["objFifo_name"]).value
            access = Access(False, ir.IntegerAttr(op.attributes["size"]).value)
        elif name == _FOR:
            _scan(
                list(op.regions[0].blocks[0].operations),
                depth + 1,
                prologue,
                steady,
                epilogue,
                False,
            )
            past_loop = depth == 0 or past_loop
            continue
        else:
            continue
        if depth == 0:
            (epilogue if past_loop else prologue).setdefault(fifo, []).append(access)
        else:
            steady.setdefault(fifo, []).append((depth, access))


def _core_pattern(core: CoreOp) -> dict[str, Pattern]:
    """Return this core's ``Pattern`` per fifo name it acquires or releases.

    Raises:
        NotImplementedError: A fifo's steady firings sit at more than one
            loop depth.
    """
    prologue: dict[str, list[Access]] = {}
    steady: dict[str, list[tuple[int, Access]]] = {}
    epilogue: dict[str, list[Access]] = {}
    _scan(_call_body(core), 0, prologue, steady, epilogue, False)
    patterns: dict[str, Pattern] = {}
    for fifo in prologue.keys() | steady.keys() | epilogue.keys():
        depths = {depth for depth, _ in steady.get(fifo, ())}
        if len(depths) > 1:
            raise NotImplementedError(
                f"{fifo}: steady firings sit at several loop depths {sorted(depths)}"
            )
        patterns[fifo] = Pattern(
            prologue=tuple(prologue.get(fifo, ())),
            steady=tuple(access for _, access in steady.get(fifo, ())),
            steady_depth=next(iter(depths), 0),
            epilogue=tuple(epilogue.get(fifo, ())),
        )
    return patterns


def _device_patterns(device: DeviceOp) -> dict[str, Pattern]:
    """Return every fifo's ``Pattern``, across every core of ``device``.

    A fifo more than one core acquires (broadcast, or several readers) is
    read off the first core found; every reader is built from the one
    declaration, so its pattern is the same.
    """
    patterns: dict[str, Pattern] = {}
    for op in device.body_region.blocks[0].operations:
        if isinstance(op, CoreOp):
            for fifo, pattern in _core_pattern(op).items():
                patterns.setdefault(fifo, pattern)
    return patterns


def _link_edges(device: DeviceOp) -> dict[str, set[str]]:
    """Return the undirected adjacency ``aie.objectfifo.link`` draws between fifo names.

    GEMM's split, forward and join each link a host-facing fifo to the
    fifo(s) a core acquires; walking this graph either way finds the one
    from the other.
    """
    edges: dict[str, set[str]] = {}
    for op in device.body_region.blocks[0].operations:
        if isinstance(op, ObjectFifoLinkOp):
            ins = [ir.FlatSymbolRefAttr(a).value for a in ir.ArrayAttr(op.fifoIns)]
            outs = [ir.FlatSymbolRefAttr(a).value for a in ir.ArrayAttr(op.fifoOuts)]
            for a in ins:
                edges.setdefault(a, set()).update(outs)
            for b in outs:
                edges.setdefault(b, set()).update(ins)
    return edges


def _reachable(root: str, edges: dict[str, set[str]]) -> set[str]:
    """Return every fifo name ``root`` reaches over ``edges``, ``root`` included."""
    seen = {root}
    frontier = [root]
    while frontier:
        found = [n for node in frontier for n in edges.get(node, ()) if n not in seen]
        seen.update(found)
        frontier = found
    return seen


def firings(op: Operator) -> dict[str, Pattern]:
    """Return each of ``op``'s operands' per-firing objectFIFO pattern.

    Built once, device-free, from ``op``'s own generated core bodies: no
    separate declaration of what an operand moves, so a build that changes
    its cores' acquires and releases is read here unchanged.

    Args:
        op: The operator, resolved or not (its design resolves it).

    Returns:
        Each streamed operand's name to its ``Pattern``, for the operands a
        core actually touches (a pinned, shipped operand's lanes are not
        built from objectFIFOs, and are left out).
    """
    array = BuiltArray(OperatorDesign(op))
    module = array.program().resolve_program()
    (device,) = (d for d in module.body.operations if isinstance(d, DeviceOp))
    edges = _link_edges(device)
    fifo_patterns = _device_patterns(device)
    found: dict[str, Pattern] = {}
    for buffer in array.op.buffers:
        if not buffer.lane_handles:
            continue
        reachable = _reachable(buffer.lane_handles[0].name, edges)
        fifo = next((f for f in sorted(reachable) if f in fifo_patterns), None)
        if fifo is not None:
            found[buffer.name] = fifo_patterns[fifo]
    return found
