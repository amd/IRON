# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Co-residence: several designs' arrays merged into one ``aie.device``.

Each member keeps its runtime sequence under its own name, so the main
sequence configures the pack once and runs any member's sequence against it.
Members whose devices are one array (``array_text``) keep one copy of it.
A member's cores idle on the lock its own sequence sets while another runs;
dataflow between members still goes through DDR. Two members may share a
pinned tile unless both program its core or its DMA, which a route into its
TileControl does too. The fifo lowering allocates shim channels around
``aie.shim_dma_allocation`` ops alone, so a member routing a pinned shim
channel by hand must allocate it. Whether the union fits is for aiecc's
placer, fifo lowering and router to say (``fits``).
"""

from __future__ import annotations

import dataclasses
import hashlib
from collections.abc import Hashable, Iterable, Mapping, Sequence

from aie import ir
from aie.dialects import aie, func
from aie.passmanager import PassManager

DEFAULT_SEQUENCE = "sequence"

_EXCLUSIVE_PER_TILE = ("aie.core", "aie.mem", "aie.memtile_dma", "aie.shim_dma")

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

    def _group_of(self, design: str) -> tuple[str, ...]:
        for group in self.groups:
            if design in group and len(group) > 1:
                return group
        return (design,)

    def device_of(self, design: str) -> str:
        group = self._group_of(design)
        return design if len(group) == 1 else self.device_name(group)

    def sequence_of(self, design: str) -> str:
        return DEFAULT_SEQUENCE if len(self._group_of(design)) == 1 else design

    def devices(self, designs: Iterable[str]) -> dict[str, tuple[str, ...]]:
        """Each device symbol and the designs it carries, in first-use order."""
        out: dict[str, tuple[str, ...]] = {}
        for design in designs:
            out.setdefault(self.device_of(design), self._group_of(design))
        return out

    def sharing(self, arrays: Mapping[str, Hashable]) -> Packing:
        """This packing with the designs of one array in one device.

        Args:
            arrays: Every design, in first-use order, and its array: its
                `array_text`, or what stands for it.
        """
        order = list(arrays)
        by_text: dict[Hashable, list[str]] = {}
        for design, text in arrays.items():
            by_text.setdefault(text, []).append(design)
        merged: list[set[str]] = []
        for group in [
            *map(set, self.groups),
            *(set(c) for c in by_text.values() if len(c) > 1),
        ]:
            for other in [m for m in merged if m & group]:
                merged.remove(other)
                group |= other
            merged.append(group)
        return Packing(tuple(tuple(sorted(g, key=order.index)) for g in merged))

    @staticmethod
    def device_name(group: Sequence[str]) -> str:
        """A pack's symbol, independent of its members' order."""
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


def array_text(device: aie.DeviceOp) -> str:
    """``device`` as text without its name or runtime sequences: equal for two
    designs whose sequences can run on one configured array.
    """
    clone = device.operation.clone(ip=False)
    if "sym_name" in clone.attributes:
        del clone.attributes["sym_name"]
    for op in list(clone.regions[0].blocks[0].operations):
        if isinstance(op, aie.RuntimeSequenceOp):
            op.operation.erase()
    text = str(clone)
    clone.erase()
    return text


def _namespace(device: aie.DeviceOp, member: str) -> None:
    """Prefix every symbol but a runtime sequence or a kernel declaration,
    which members share, with ``member``.
    """
    for op in _body(device):
        old = _symbol(op)
        if (
            old is None
            or _is_kernel_declaration(op)
            or isinstance(op, aie.RuntimeSequenceOp)
        ):
            continue
        new = f"{member}__{old}"
        ir.SymbolTable.replace_all_symbol_uses(old, new, device.operation)
        op.operation.attributes["sym_name"] = ir.StringAttr.get(new)


def merge_devices(name: str, members: Mapping[str, aie.DeviceOp]) -> aie.DeviceOp:
    """Merge ``members`` (design name -> device op, one module) into the first,
    renamed ``name``, each member's runtime sequence named for it.

    Raises:
        CoResidenceError: The members target different devices, declare one
            kernel differently, or put an exclusive op on one pinned tile.
    """
    if len(members) < 2:
        raise ValueError(f"a pack needs two or more designs, got {list(members)}")
    kinds = {str(d.device) for d in members.values()}
    if len(kinds) != 1:
        raise CoResidenceError(
            f"{list(members)} are built for different devices ({sorted(kinds)})"
        )

    held: dict[str, aie.DeviceOp] = {}  # array text -> the device keeping it
    arrays: dict[str, aie.DeviceOp] = {}  # member -> the array it keeps
    for member, device in members.items():
        [sequence] = [
            op for op in _body(device) if isinstance(op, aie.RuntimeSequenceOp)
        ]
        old = _symbol(sequence)
        assert old is not None, "a runtime sequence has a symbol"
        ir.SymbolTable.replace_all_symbol_uses(old, member, device.operation)
        sequence.operation.attributes["sym_name"] = ir.StringAttr.get(member)
        text = array_text(device)
        holder = held.get(text)
        if holder is None:
            held[text] = arrays[member] = device
            continue
        # Equal text, so the arrays' ops correspond in order.
        kept = [op for op in _body(holder) if not isinstance(op, aie.RuntimeSequenceOp)]
        ours = [op for op in _body(device) if not isinstance(op, aie.RuntimeSequenceOp)]
        for mine, theirs in zip(ours, kept):
            for a, b in zip(mine.results, theirs.results):
                a.replace_all_uses_with(b)
        ops = holder.body_region.blocks[0].operations
        sequence.operation.move_before(ops[len(ops) - 1])
        device.operation.erase()

    pack = next(iter(arrays.values()))
    if len(arrays) == 1:
        pack.operation.attributes["sym_name"] = ir.StringAttr.get(name)
        return pack
    for member, device in arrays.items():
        _namespace(device, member)

    end = pack.body_region.blocks[0].operations[
        len(pack.body_region.blocks[0].operations) - 1
    ]
    kernels: dict[str, str] = {}
    tiles: dict[tuple[int, int], ir.Value] = {}
    exclusive: dict[tuple[str, tuple[int, int]], tuple[str, str]] = {}

    for member, device in arrays.items():
        routed: set[tuple[tuple[int, int], aie.DMAChannelDir, int]] = set()
        allocated: set[tuple[tuple[int, int], aie.DMAChannelDir, int]] = set()
        for op in _body(device):
            if _is_kernel_declaration(op):
                symbol = _symbol(op)
                assert symbol is not None, "a func.func has a symbol"
                # Mid-merge the module need not verify, and a printer that
                # verifies first falls back to the generic form.
                text = op.operation.get_asm(assume_verified=True)
                seen = kernels.get(symbol)
                if seen is not None:
                    if seen != text:
                        raise CoResidenceError(
                            f"kernel {symbol} is declared differently by two designs"
                        )
                    op.operation.erase()
                    continue
                kernels[symbol] = text
            coords = _pinned_tile(op)
            if coords is not None:
                if coords in tiles:
                    op.result.replace_all_uses_with(tiles[coords])
                    op.operation.erase()
                    continue
                tiles[coords] = op.result
            claims: list[tuple[str, tuple[int, int], str]] = []
            if op.operation.name in _EXCLUSIVE_PER_TILE:
                placed = _pinned_tile(op.operation.operands[0].owner)
                if placed is not None:
                    claims.append(
                        (op.operation.name, placed, f"an {op.operation.name}")
                    )
            for tile, direction, bundle, channel in _route_ends(op):
                placed = _pinned_tile(tile)
                if placed is None:
                    continue
                if bundle == aie.WireBundle.TileControl:
                    kind = (
                        "aie.shim_dma"
                        if tile.is_shim_tile()
                        else "aie.memtile_dma" if tile.is_mem_tile() else "aie.mem"
                    )
                    claims.append((kind, placed, "a TileControl route"))
                elif bundle == aie.WireBundle.DMA and tile.is_shim_tile():
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
            for kind, placed, what in claims:
                key = (kind, placed)
                if key in exclusive and exclusive[key][0] != member:
                    holder, held = exclusive[key]
                    raise CoResidenceError(
                        f"{holder} puts {held} and {member} puts {what} "
                        f"on tile {placed}, which carries one {kind}"
                    )
                exclusive[key] = (member, what)
            if device is not pack:
                op.operation.move_before(end)
        if routed - allocated:
            placed, direction, channel = min(routed - allocated)
            raise CoResidenceError(
                f"{member} routes shim tile {placed} {direction} channel "
                f"{channel} by hand with no aie.shim_dma_allocation for it, "
                "so another member's fifo could be given it"
            )
        if device is not pack:
            device.operation.erase()

    pack.operation.attributes["sym_name"] = ir.StringAttr.get(name)
    return pack


def fits(device_texts: Mapping[str, str], params_preamble: str = "") -> str | None:
    """``None`` if ``device_texts`` (design name -> ``aie.device`` text),
    merged, places and allocates, else the diagnostic.
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
            # Parsed alone and named first: two unnamed devices are one symbol twice.
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
    """Grow a pack along the runlist while ``fits`` accepts the union.

    Greedy: a design recurring far apart is packed where it first appears.
    """

    max_members: int | None = None

    def pack(
        self,
        order: Sequence[str],
        device_texts: Mapping[str, str],
        params_preamble: str = "",
    ) -> tuple[Packing, dict[tuple[str, ...], str]]:
        """The packing for runlist ``order``, and the diagnostic that stopped
        each pack growing.
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
