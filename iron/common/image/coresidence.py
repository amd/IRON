# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Co-residence: several designs' arrays packed into one device configuration.

Temporal fusion (:mod:`.fusion`) gives every design its own ``aie.device`` and
reconfigures the array between steps that run different designs. Packing
merges designs into one ``aie.device`` instead: their tiles, fifos and cores
side by side, each design's runtime sequence kept under its own name, so the
main sequence configures the pack once and ``aiex.run``\\ s any member's
sequence against it, in any order, any number of times. Dataflow between the
members still goes through DDR.

Nothing here reads an operator: the merge is over device ops, whatever built
them. What makes it work is the shape every IRON design already has -- cores
that loop forever, each round gated by a lock its own sequence sets -- so a
member's cores idle while another member's sequence runs.

What the merge has to settle:

- symbols: every symbol a member defines at device scope (fifos, buffers,
  its runtime sequence) is renamed into the member's namespace, uses
  included. A kernel declaration is not: its symbol is the object's, and
  the digest prefix ``declare_kernel`` gives it already keeps two kernels
  apart, so two members calling one kernel share one declaration.
- pinned tiles: two members naming one physical tile share its ``aie.tile``,
  unless both put a core or a DMA program on it, which is a conflict.
  Logical tiles are left to ``aie-place-tiles``, which sees the union.
- device type: every member is built for the same device.

Whether the union *fits* -- cores, shim channels, routes -- is for the
placer, the fifo lowering and the router to say, as they would in aiecc;
:func:`fits` asks them, and
:class:`AdjacentPacking` uses it to pack a runlist without being told what
goes with what.
"""

from __future__ import annotations

import dataclasses
import hashlib
from collections.abc import Iterable, Mapping, Sequence

from aie import ir
from aie.dialects import aie, func
from aie.passmanager import PassManager

# The runtime sequence a device has when nothing names it otherwise.
DEFAULT_SEQUENCE = "sequence"

# Ops of which a physical tile carries at most one: two members pinning one
# of these to the same tile cannot share it.
_EXCLUSIVE_PER_TILE = ("aie.core", "aie.mem", "aie.memtile_dma", "aie.shim_dma")

# What decides whether a merged device fits: the resource stages of aiecc's
# own pipeline, in its order (tools/aiecc/IRTransforms.h: placement, then
# getInputWithAddressesPipeline's fifo lowering and id/address assignment,
# then routing). The fifo lowering is the whole stateful transform, not its
# allocate pass alone: allocate on unsplit fifos checks nothing, which is how
# two designs pinning one shim DMA channel once passed as fitting.
_FIT_PIPELINE = (
    "builtin.module("
    "aie.device(aie-place-tiles),"
    "aie-lower-scratchpad-parameters,"
    "aie.device("
    "aie-objectFifo-stateful-transform,"
    "aie-assign-lock-ids,"
    "aie-reserve-runtime-bd-ids,"
    "aie-assign-bd-ids,"
    "aie-prepare-buffers,"
    "aie-assign-buffer-addresses,"
    "aie-create-pathfinder-flows"
    "))"
)


class CoResidenceError(ValueError):
    """The designs cannot share one device configuration."""


@dataclasses.dataclass(frozen=True)
class Packing:
    """A partition of a sequence's designs into device configurations.

    ``groups`` lists the designs each configuration carries; a design in no
    group has a configuration of its own. A group of one is the same as no
    group, so the plain temporal fusion is ``Packing(())``.
    """

    groups: tuple[tuple[str, ...], ...] = ()

    def __post_init__(self) -> None:
        seen: set[str] = set()
        for group in self.groups:
            for design in group:
                if design in seen:
                    raise ValueError(f"{design} is packed into two groups")
                seen.add(design)

    def _group_of(self, design: str) -> tuple[str, ...]:
        for group in self.groups:
            if design in group and len(group) > 1:
                return group
        return (design,)

    def device_of(self, design: str) -> str:
        """The device symbol ``design`` runs in."""
        group = self._group_of(design)
        return design if len(group) == 1 else self.device_name(group)

    def sequence_of(self, design: str) -> str:
        """The runtime sequence symbol ``design`` runs, inside its device."""
        return DEFAULT_SEQUENCE if len(self._group_of(design)) == 1 else design

    def devices(self, designs: Iterable[str]) -> dict[str, tuple[str, ...]]:
        """Each device symbol and the designs it carries, in first-use order."""
        out: dict[str, tuple[str, ...]] = {}
        for design in designs:
            out.setdefault(self.device_of(design), self._group_of(design))
        return out

    @staticmethod
    def device_name(group: Sequence[str]) -> str:
        """A pack's symbol: a function of its members, not of their order in
        a runlist, so one pack is one device text wherever it is used."""
        digest = hashlib.sha256("|".join(sorted(group)).encode()).hexdigest()[:8]
        return f"pack{len(group)}_{digest}"


def _symbol(op: ir.OpView) -> str | None:
    attrs = op.operation.attributes
    if "sym_name" not in attrs:
        return None
    return ir.StringAttr(attrs["sym_name"]).value


def _is_kernel_declaration(op: ir.OpView) -> bool:
    return isinstance(op, func.FuncOp) and op.is_external


def _body(device: aie.DeviceOp) -> list[ir.OpView]:
    """The device's ops, without its terminator."""
    return [
        op
        for op in device.body_region.blocks[0].operations
        if not isinstance(op, aie.EndOp)
    ]


def _pinned_tile(op: ir.OpView) -> tuple[int, int] | None:
    if not isinstance(op, aie.TileOp):
        return None
    return (
        ir.IntegerAttr(op.operation.attributes["col"]).value,
        ir.IntegerAttr(op.operation.attributes["row"]).value,
    )


def _namespace(device: aie.DeviceOp, member: str) -> None:
    """Rename every symbol ``device`` defines into ``member``'s namespace.

    Its runtime sequence becomes ``member``; everything else but a kernel
    declaration gets ``member`` as a prefix. Uses anywhere under the device
    (cores, the sequence, links) follow the rename.
    """
    for op in _body(device):
        old = _symbol(op)
        if old is None or _is_kernel_declaration(op):
            continue
        is_sequence = isinstance(op, aie.RuntimeSequenceOp)
        new = member if is_sequence else f"{member}__{old}"
        ir.SymbolTable.replace_all_symbol_uses(old, new, device.operation)
        op.operation.attributes["sym_name"] = ir.StringAttr.get(new)


def merge_devices(name: str, members: Mapping[str, aie.DeviceOp]) -> aie.DeviceOp:
    """Merge ``members`` (design name -> its device op) into one device op.

    The first member's op becomes the pack, renamed ``name``; the others are
    emptied into it and erased. Every member must be in the same module.
    """
    if len(members) < 2:
        raise ValueError(f"a pack needs two or more designs, got {list(members)}")
    devices = list(members.values())
    kinds = {str(d.device) for d in devices}
    if len(kinds) != 1:
        raise CoResidenceError(
            f"{list(members)} are built for different devices ({sorted(kinds)})"
        )

    for member, device in members.items():
        _namespace(device, member)

    pack = devices[0]
    end = pack.body_region.blocks[0].operations[
        len(pack.body_region.blocks[0].operations) - 1
    ]
    kernels: dict[str, str] = {}
    tiles: dict[tuple[int, int], ir.Value] = {}
    exclusive: dict[tuple[str, tuple[int, int]], str] = {}

    for member, device in members.items():
        for op in _body(device):
            symbol = _symbol(op)
            if _is_kernel_declaration(op):
                seen = kernels.get(symbol)
                if seen is not None:
                    if seen != str(op):
                        raise CoResidenceError(
                            f"kernel {symbol} is declared differently by two designs"
                        )
                    op.operation.erase()
                    continue
                kernels[symbol] = str(op)
            coords = _pinned_tile(op)
            if coords is not None:
                if coords in tiles:
                    op.result.replace_all_uses_with(tiles[coords])
                    op.operation.erase()
                    continue
                tiles[coords] = op.result
            if op.operation.name in _EXCLUSIVE_PER_TILE:
                owner = op.operation.operands[0].owner
                placed = (
                    _pinned_tile(owner.opview)
                    if isinstance(owner, ir.Operation)
                    else None
                )
                if placed is not None:
                    key = (op.operation.name, placed)
                    if key in exclusive and exclusive[key] != member:
                        raise CoResidenceError(
                            f"{exclusive[key]} and {member} both put an "
                            f"{op.operation.name} on tile {placed}"
                        )
                    exclusive[key] = member
            if device is not pack:
                op.operation.move_before(end)
        if device is not pack:
            device.operation.erase()

    pack.operation.attributes["sym_name"] = ir.StringAttr.get(name)
    return pack


def fits(device_texts: Mapping[str, str], params_preamble: str = "") -> str | None:
    """Whether ``device_texts`` (design name -> its ``aie.device`` text), merged
    into one device if there are several, places and allocates: ``None`` if
    it does, else the diagnostic.

    Works on a copy in its own context, so nothing the caller holds is
    touched. Each text is parsed alone and named for its design before they
    meet: a device a generator emits carries no name of its own, and two
    unnamed devices in one module are one symbol defined twice.
    """
    with ir.Context() as ctx, ir.Location.unknown():
        diagnostics: list[str] = []

        def collect(d: ir.Diagnostic) -> bool:
            if d.severity == ir.DiagnosticSeverity.ERROR:
                diagnostics.append(f"{d.location}: {d.message}")
            return True

        handler = ctx.attach_diagnostic_handler(collect)
        try:
            module = ir.Module.parse(f"module {{\n{params_preamble}\n}}")
            devices: dict[str, aie.DeviceOp] = {}
            for design, text in device_texts.items():
                alone = ir.Module.parse(f"module {{\n{params_preamble}\n{text}\n}}")
                for op in alone.body.operations:
                    if isinstance(op, aie.DeviceOp):
                        op.operation.attributes["sym_name"] = ir.StringAttr.get(design)
                        module.body.append(op)
                        devices[design] = op
            if len(devices) > 1:
                merge_devices(Packing.device_name(list(devices)), devices)
            PassManager.parse(_FIT_PIPELINE).run(module.operation)
        except CoResidenceError as e:
            return str(e)
        except ir.MLIRError as e:
            return "\n".join(diagnostics) or str(e)
        finally:
            handler.detach()
        return "\n".join(diagnostics) if diagnostics else None


@dataclasses.dataclass(frozen=True)
class AdjacentPacking:
    """Pack designs that run next to each other, as long as the union fits.

    Walks the runlist in order and grows the current pack with each new
    design while :func:`fits` accepts the union; a design that does not fit
    starts the next pack. A design seen before stays where it was placed.
    It knows nothing about any operator: the placer is the only judge.

    Greedy, so not optimal: the objective is the number of runlist steps
    that change device, and a design recurring far apart (a layer's ops,
    once per layer) is packed where it first appears.
    """

    max_members: int | None = None

    def pack(
        self,
        order: Sequence[str],
        device_texts: Mapping[str, str],
        params_preamble: str = "",
    ) -> tuple[Packing, dict[tuple[str, ...], str]]:
        """The packing for runlist ``order``, and why each pack stopped growing
        (the diagnostic of the union that did not fit, keyed by the pack)."""
        groups: list[tuple[str, ...]] = []
        stopped: dict[tuple[str, ...], str] = {}
        current: list[str] = []
        placed: set[str] = set()
        for design in order:
            if design in placed:
                if design not in current and current:
                    groups.append(tuple(current))
                    current = []
                continue
            candidate = current + [design]
            full = self.max_members is not None and len(candidate) > self.max_members
            verdict = (
                "max_members"
                if full
                else (
                    fits({d: device_texts[d] for d in candidate}, params_preamble)
                    if current
                    else None
                )
            )
            if verdict is None:
                current = candidate
            else:
                stopped[tuple(current)] = verdict
                groups.append(tuple(current))
                current = [design]
            placed.add(design)
        if current:
            groups.append(tuple(current))
        return Packing(tuple(g for g in groups if len(g) > 1)), stopped
