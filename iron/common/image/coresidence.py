# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Co-residence: several designs' arrays in one aie.iron ``DeviceConfiguration``.

Each member keeps its runtime sequence under its own name, so the main
sequence configures the pack once and runs any member's sequence against it.
Members of one array (``identities``) build it once. A member's
cores idle on the lock its own sequence sets while another runs; dataflow
between members still goes through DDR. Members share the device's symbol
table, which aie.iron names their unnamed fifos and buffers into. Two
members may share a pinned tile unless both program its core or its DMA, which a route
into its TileControl does too: the core verifier and mlir-aie's
``DeviceConfiguration`` refuse those; a logical tile given its column and
row is pinned. The fifo lowering allocates shim channels around
``aie.shim_dma_allocation`` ops alone, so a member routing a pinned shim
channel by hand must allocate it (``conflicts``). Whether the union fits is for aiecc's
placer, fifo lowering and router to say (``fits``).
"""

from __future__ import annotations

import dataclasses
import hashlib
import logging
from collections.abc import Callable, Collection, Hashable, Iterable, Mapping, Sequence

import aie.utils as aie_utils
from aie import ir
from aie.dialects import aie
from aie.iron import DeviceConfiguration, Program
from aie.passmanager import PassManager

from ..declare import Operator
from ..design import BuiltArray, OperatorDesign, configuration, identities

logger = logging.getLogger(__name__)

# aiecc's resource stages, in its order (tools/aiecc/IRTransforms.h). The whole
# stateful transform, since allocate alone on unsplit fifos checks nothing.
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
    """A partition of a sequence's designs into device configurations; a
    design in no group (or a group of one) has its own.
    """

    groups: tuple[tuple[str, ...], ...] = ()

    def __post_init__(self) -> None:
        seen: set[str] = set()
        for group in self.groups:
            for design in group:
                if design in seen:
                    raise ValueError(f"{design} is packed into two groups")
                seen.add(design)

    def group_of(self, design: str) -> tuple[str, ...]:
        for group in self.groups:
            if design in group and len(group) > 1:
                return group
        return (design,)

    @classmethod
    def of(
        cls,
        coresident: Sequence[Sequence[Operator]],
        designs: Collection[str],
        full_elf: bool = True,
    ) -> Packing:
        """Groups of operators as the names of the designs they run as.

        Raises:
            ValueError: A group names a design none of ``designs`` is.
        """
        dev = aie_utils.get_current_device()
        groups = tuple(
            tuple(
                dict.fromkeys(
                    OperatorDesign(op.resolved(dev), full_elf).name for op in group
                )
            )
            for group in coresident
        )
        strays = [n for g in groups for n in g if n not in designs]
        if strays:
            raise ValueError(f"coresident names designs no step runs: {strays}")
        return cls(groups)

    def device_of(self, design: str) -> str:
        group = self.group_of(design)
        return design if len(group) == 1 else self.device_name(group)

    def devices(self, designs: Iterable[str]) -> dict[str, tuple[str, ...]]:
        """Each device symbol and the designs it carries, in first-use order."""
        out: dict[str, tuple[str, ...]] = {}
        for design in designs:
            out.setdefault(self.device_of(design), self.group_of(design))
        return out

    def sharing(
        self,
        arrays: Mapping[str, Hashable],
        fits: Callable[[tuple[str, ...]], str | None] | None = None,
    ) -> Packing:
        """This packing with the designs of one array in one device.

        An array's designs in two or more packs join them only where
        ``fits`` takes the union; otherwise each pack builds the array, and
        its designs in no pack join the first.

        Args:
            arrays: Every design, in first-use order, and its array: its
                `design.identities`, or what stands for it.
            fits: Why the placer refuses a union of packs, or None where it
                takes it; every union is taken where not given.
        """
        order = list(arrays)
        by_array: dict[Hashable, set[str]] = {}
        for design, array in arrays.items():
            by_array.setdefault(array, set()).add(design)
        devices = [set(group) for group in self.groups]
        for mates in by_array.values():
            if len(mates) < 2:
                continue
            touched = [d for d in devices if d & mates]
            union = mates.union(*touched)
            if len(touched) > 1 and fits is not None:
                refused = fits(tuple(sorted(union, key=order.index)))
                if refused is not None:
                    touched[0] |= mates - set().union(*touched)
                    continue
            devices = [d for d in devices if not d & mates] + [union]
        return Packing(tuple(tuple(sorted(g, key=order.index)) for g in devices))

    @staticmethod
    def device_name(group: Sequence[str]) -> str:
        """A pack's symbol, independent of its members' order."""
        digest = hashlib.sha256("|".join(sorted(group)).encode()).hexdigest()[:8]
        return f"pack{len(group)}_{digest}"


def _body(device: aie.DeviceOp) -> list[ir.OpView]:
    return [
        op
        for op in device.body_region.blocks[0].operations
        if not isinstance(op, aie.EndOp)
    ]


def _pinned_tile(op: ir.OpView) -> tuple[int, int] | None:
    """The physical tile ``op`` names: an ``aie.tile``'s, or a logical
    tile's given both its column and its row.
    """
    if isinstance(op, aie.LogicalTileOp):
        if op.col is None or op.row is None:
            return None
    elif not isinstance(op, aie.TileOp):
        return None
    return (
        ir.IntegerAttr(op.operation.attributes["col"]).value,
        ir.IntegerAttr(op.operation.attributes["row"]).value,
    )


def _route_ends(op: ir.OpView):
    """The ends of a route declared by hand: ``(tile, direction, bundle,
    channel)``, the tile its defining op, the bundle and channel ints.
    """
    if isinstance(op, aie.FlowOp):
        ends = [
            (op.source, aie.DMAChannelDir.MM2S, op.source_bundle, op.source_channel),
            (op.dest, aie.DMAChannelDir.S2MM, op.dest_bundle, op.dest_channel),
        ]
    elif isinstance(op, aie.PacketFlowOp):
        ends = [
            (
                end.tile,
                (
                    aie.DMAChannelDir.MM2S
                    if isinstance(end, aie.PacketSourceOp)
                    else aie.DMAChannelDir.S2MM
                ),
                end.bundle,
                end.channel,
            )
            for end in op.regions[0].blocks[0].operations
            if isinstance(end, (aie.PacketSourceOp, aie.PacketDestOp))
        ]
    else:
        return []
    return [
        (
            tile.owner,
            direction,
            ir.IntegerAttr(bundle).value,
            ir.IntegerAttr(channel).value,
        )
        for tile, direction, bundle, channel in ends
    ]


def conflicts(devices: Mapping[str, aie.DeviceOp]) -> None:
    """Refuse ``devices`` (design name -> its own device, each another
    array) co-resident where one leaves a hand-routed shim channel to the
    fifo lowering.

    Raises:
        CoResidenceError: One routes a shim DMA channel by hand with no
            ``aie.shim_dma_allocation`` for it.
    """
    for member, device in devices.items():
        routed: set[tuple[tuple[int, int], aie.DMAChannelDir, int]] = set()
        allocated: set[tuple[tuple[int, int], aie.DMAChannelDir, int]] = set()
        for op in _body(device):
            for tile, direction, bundle, channel in _route_ends(op):
                placed = _pinned_tile(tile)
                if (
                    placed is not None
                    and bundle == aie.WireBundle.DMA
                    and tile.is_shim_tile()
                ):
                    routed.add((placed, direction, channel))
            if isinstance(op, aie.ShimDMAAllocationOp):
                placed = _pinned_tile(op.tile.owner)
                if placed is not None:
                    allocated.add(
                        (
                            placed,
                            aie.DMAChannelDir(ir.IntegerAttr(op.channel_dir).value),
                            ir.IntegerAttr(op.channel_index).value,
                        )
                    )
        if routed - allocated:
            placed, direction, channel = min(routed - allocated)
            raise CoResidenceError(
                f"{member} routes shim tile {placed} {direction} channel "
                f"{channel} by hand with no aie.shim_dma_allocation for it, "
                "so another member's fifo could be given it"
            )


def pack(
    name: str, arrays: Mapping[str, BuiltArray], steps: Sequence[str] = ()
) -> DeviceConfiguration:
    """``arrays`` co-resident in one device configuration named ``name``,
    running ``steps`` (``design.configuration``).

    Raises:
        CoResidenceError: One of its arrays routes a shim channel by hand
            without allocating it (``conflicts``).
    """
    distinct: dict[Hashable, BuiltArray] = {}
    of = identities(arrays)
    for key, array in arrays.items():
        distinct.setdefault(of[key], array)
    if len(distinct) > 1:
        # Each array alone, so a claim names the design that makes it.
        modules = {a.design.name: a.design.module() for a in distinct.values()}
        conflicts(
            {
                member: next(
                    op for op in m.body.operations if isinstance(op, aie.DeviceOp)
                )
                for member, m in modules.items()
            }
        )
    return configuration(name, arrays, steps)


def places(module: ir.Module) -> str | None:
    """``None`` if ``module``'s devices place and allocate, else the
    diagnostic.
    """
    diagnostics: list[str] = []

    def collect(d: ir.Diagnostic) -> bool:
        if d.severity == ir.DiagnosticSeverity.ERROR:
            diagnostics.append(f"{d.location}: {d.message}")
        return True

    handler = module.context.attach_diagnostic_handler(collect)
    try:
        PassManager.parse(_FIT_PIPELINE, module.context).run(module.operation)
    except ir.MLIRError as e:
        return "\n".join(diagnostics) or str(e)
    finally:
        handler.detach()
    return "\n".join(diagnostics) if diagnostics else None


def unvalued(designs: Mapping[str, OperatorDesign]) -> None:
    """Refuse a pack of ``designs`` where one is built for an xclbin and
    takes a per-call value: a dispatch parameter, which a pack's one
    sequence does not carry.

    Raises:
        CoResidenceError: One does.
    """
    for name, design in designs.items():
        if not design.full_elf and design.op.values:
            raise CoResidenceError(
                f"{name} takes per-call value {design.op.values[0].name!r}, a "
                f"dispatch parameter on an xclbin, which a pack does not carry"
            )


def fits(
    designs: Mapping[str, OperatorDesign], words: Mapping[str, str] | None = None
) -> str | None:
    """``None`` if ``designs`` place and allocate as one pack, else the
    diagnostic.

    Args:
        designs: The designs, by the name each takes in the device; one
            another tool exports is a device of its own.
        words: Design symbol -> the scratchpad word it shares with others.
    """
    exported = [n for n, d in designs.items() if d.op.exported_design() is not None]
    try:
        unvalued(designs)
        if exported and len(designs) > 1:
            raise CoResidenceError(
                f"{exported[0]} is exported by another tool, a device of its own"
            )
        if exported:
            (design,) = designs.values()
            module = ir.Module.parse(str(design.build()), ir.Context())
        else:
            arrays = {n: BuiltArray(d, words) for n, d in designs.items()}
            configured = pack(
                (
                    next(iter(arrays))
                    if len(arrays) == 1
                    else Packing.device_name(list(arrays))
                ),
                arrays,
            )
            module = Program.compose(
                [configured], entry=configured.runtimes[0]
            ).resolve_program()
    except (ValueError, RuntimeError, ir.MLIRError) as e:
        return str(e)
    return places(module)


@dataclasses.dataclass(frozen=True)
class AdjacentPacking:
    """Grow a pack along the runlist while ``fits`` accepts the union.

    Greedy: a design recurring far apart is packed where it first appears.
    """

    def pack(
        self,
        order: Sequence[str],
        designs: Mapping[str, OperatorDesign],
        words: Mapping[str, str] | None = None,
    ) -> tuple[Packing, dict[tuple[str, ...], str]]:
        """The packing for runlist ``order`` of ``designs``, and the
        diagnostic that stopped each pack growing, which it also logs.
        """
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
            verdict = (
                fits({d: designs[d] for d in candidate}, words) if current else None
            )
            if verdict is None:
                current = candidate
            else:
                stopped[tuple(current)] = verdict
                logger.info("%s does not pack with %s: %s", design, current, verdict)
                groups.append(tuple(current))
                current = [design]
            placed.add(design)
        if current:
            groups.append(tuple(current))
        return Packing(tuple(g for g in groups if len(g) > 1)), stopped
