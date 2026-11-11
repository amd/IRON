# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Composition: a sequence's designs as one module, mlir-aie's ``Program.compose``.

A ``DeviceConfiguration`` per array, designs of one array sharing their
device, and a main one whose runtime sequence configures and runs them in
turn.
"""

from __future__ import annotations

import dataclasses
import hashlib
import itertools
import logging
import math
from collections.abc import Hashable, Iterable, Mapping, Sequence

import numpy as np
from aie import ir
from aie.dialects import memref
from aie.extras.dialects.arith import constant
from aie.helpers.npdtypes import np_ndarray_type_get_dtype, np_ndarray_type_get_shape
from aie.helpers.util import np_ndarray_type_to_memref_type
from aie.iron import DeviceConfiguration, Program, Runtime
from aie.passmanager import PassManager
from aie.utils import bfp
from aie.utils.compile.jit.compilabledesign import compile_context

from ..design import BuiltArray, OperatorDesign, configuration, identities
from .step import BufferRef, Edge, Fusion, FusionKind

logger = logging.getLogger(__name__)

# The shim DMA addresses host memory in 32-bit words, so every buffer handed
# to a sub-design must start on one.
SHIM_ADDRESS_ALIGNMENT = 4

# aiecc's resource stages, in its order (tools/aiecc/IRTransforms.h). The whole
# stateful transform, since allocate alone on unsplit fifos checks nothing.
_FIT_PIPELINE = (
    "builtin.module("
    "aie.device(aie-place-tiles{{placer={placer}}}),"
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


SEQUENTIAL, ANNEALED = "sequential_placer", "sa_placer"

# Each packed group's placer and the diagnostic where none routes it, by its
# designs' identities.
_placed: dict[tuple[str, ...], tuple[str, str | None]] = {}


class CoResidenceError(ValueError):
    """The designs cannot share one device configuration."""


@dataclasses.dataclass(frozen=True)
class Packing:
    """A partition of a sequence's designs into device configurations.

    A design in no group (or a group of one) has its own.
    """

    groups: tuple[tuple[str, ...], ...] = ()
    # Designs whose device routes only as the annealing placer places it; out
    # of the repr, so an image without one keeps its cache key.
    annealed: tuple[str, ...] = dataclasses.field(default=(), repr=False)

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

    def device_of(self, design: str) -> str:
        group = self.group_of(design)
        return design if len(group) == 1 else self.device_name(group)

    def devices(self, designs: Iterable[str]) -> dict[str, tuple[str, ...]]:
        """Each device symbol and the designs it carries, in first-use order."""
        out: dict[str, tuple[str, ...]] = {}
        for design in designs:
            out.setdefault(self.device_of(design), self.group_of(design))
        return out

    def sharing(self, arrays: Mapping[str, Hashable]) -> Packing:
        """Return this packing with one array's designs in one device.

        ``arrays`` maps each design in first-use order to it.
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
            devices = [d for d in devices if not d & mates] + [union]
        return dataclasses.replace(
            self, groups=tuple(tuple(sorted(g, key=order.index)) for g in devices)
        )

    def annealed_devices(self) -> set[str]:
        """Return the device symbols the annealing placer places before the image is built."""
        return {self.device_of(d) for d in self.annealed}

    @staticmethod
    def device_name(group: Sequence[str]) -> str:
        """Return a pack's symbol, independent of its members' order."""
        digest = hashlib.sha256("|".join(sorted(group)).encode()).hexdigest()[:8]
        return f"pack{len(group)}_{digest}"


def unvalued(designs: Mapping[str, OperatorDesign]) -> None:
    """Raise ``CoResidenceError`` where one of ``designs`` is built for an xclbin.

    And takes a per-call value, a dispatch parameter a pack's sequence
    cannot carry.
    """
    for name, design in designs.items():
        if not design.full_elf and design.op.values:
            raise CoResidenceError(
                f"{name} takes per-call value {design.op.values[0].name!r}, a "
                f"dispatch parameter on an xclbin, which a pack does not carry"
            )


# aie.ir re-exports MLIR's compiled bindings with a wildcard import, which
# pyright's stub does not see through: every ir.<X> below is suppressed for it.
def places(
    module: ir.Module,
    placer: str = SEQUENTIAL,
) -> str | None:
    """Return ``None`` if ``module``'s devices place, allocate and route under ``placer``, else the diagnostic."""
    diagnostics: list[str] = []

    def collect(
        d: ir.Diagnostic,
    ) -> bool:
        severity = ir.DiagnosticSeverity
        if d.severity == severity.ERROR:
            diagnostics.append(f"{d.location}: {d.message}")
        return True

    handler = module.context.attach_diagnostic_handler(collect)
    # MLIR's generated ir.pyi types the handler as object.
    assert isinstance(handler, ir.DiagnosticHandler)
    try:
        PassManager.parse(_FIT_PIPELINE.format(placer=placer), module.context).run(
            module.operation
        )
    except ir.MLIRError as e:
        return "\n".join(diagnostics) or str(e)
    finally:
        handler.detach()
    return "\n".join(diagnostics) if diagnostics else None


def fused_configuration(
    name: str,
    fusion: Fusion,
    designs: Sequence[OperatorDesign],
    words: Mapping[str, str] | None = None,
    dispatch: Sequence[Mapping[str, object]] | None = None,
) -> tuple[DeviceConfiguration, list[BuiltArray]]:
    """Return ``fusion``'s members, ``designs`` in its step order, as one device configuration ``name`` and their arrays.

    Each array fed where an edge feeds it (staged through memtiles in a staged fusion),
    and one sequence running every member, in one task group, or back to back in a
    merge; a ``phased`` fusion's members in one sequence per phase (``phases``). On an
    xclbin, ``dispatch`` is each member's dispatch-time scalars.
    """
    incoming: dict[int, list[Edge]] = {}
    for e in fusion.edges:
        incoming.setdefault(e.consumer, []).append(e)
    arrays: dict[int, BuiltArray] = {}
    scalars = [None] * len(designs) if dispatch is None else dispatch
    for design, j, own in zip(designs, fusion.steps, scalars, strict=True):
        fed = {}
        for e in incoming.get(j, ()):
            (source,) = [b for b in arrays[e.producer].op.buffers if b.name == e.output]
            fed[e.input] = source
        arrays[j] = BuiltArray(
            design, words, own, fed=fed, staged=fusion.kind is FusionKind.STAGED
        )
    grouped: dict[int, list[str]] = {}
    if fusion.phased:
        for j, p in phases(fusion, arrays).items():
            grouped.setdefault(p, []).append(str(j))
    configured = configuration(
        name,
        {str(j): arrays[j] for j in fusion.steps},
        steps=[str(j) for j in fusion.steps],
        # A merge's steps have no edge to keep alive across a shared task
        # group; run them back to back, each fully awaited.
        fuse=fusion.kind is not FusionKind.MERGE,
        phases=[grouped[p] for p in sorted(grouped)],
    )
    return configured, [arrays[j] for j in fusion.steps]


def phases(fusion: Fusion, arrays: Mapping[int, BuiltArray]) -> dict[int, int]:
    """Return each member's phase, the sequence of a phased fusion that runs it.

    A member fed through an input whose lanes each move one object a call (GEMV's
    fed ``B``, the whole vector) runs a phase after its producer, else in the latest
    of its producers'. Such a consumer takes its input whole before computing, so its
    producer finishes into the consumer's fifo without waiting on the consumer's own
    host transfers: a sequence can end there and the next begin.

    Raises:
        ValueError: Members of one phase are not consecutive in ``fusion.steps``,
            so the phases' sequences could not run in step order.
    """
    incoming: dict[int, list[Edge]] = {}
    for e in fusion.edges:
        incoming.setdefault(e.consumer, []).append(e)
    phase: dict[int, int] = {}
    for j in fusion.steps:
        phase[j] = 0
        for e in incoming.get(j, ()):
            (sink,) = [b for b in arrays[j].op.buffers if b.name == e.input]
            per_object = math.prod(sink.obj_shape)
            whole = all(n <= per_object for n in sink.moved_per_lane().values())
            phase[j] = max(phase[j], phase[e.producer] + int(whole))
    order = [phase[j] for j in fusion.steps]
    if order != sorted(order):
        raise ValueError(
            f"fusion {fusion.steps}: its phases {order} do not follow step order"
        )
    # A phase with no host transfer holds no shim channel, and its own sequence would
    # take no arguments: it runs in the latest hosted phase before it, else the first.
    hosted = sorted(
        {
            phase[j]
            for j in fusion.steps
            if any(not b.on_chip for b in arrays[j].op.buffers)
        }
    ) or [order[0]]
    merged = {
        p: hosted.index(max((q for q in hosted if q <= p), default=hosted[0]))
        for p in set(order)
    }
    return {j: merged[phase[j]] for j in fusion.steps}


def fits(
    designs: Mapping[str, OperatorDesign],
    words: Mapping[str, str] | None = None,
    fusion: Fusion | None = None,
    placer: str = SEQUENTIAL,
) -> str | None:
    """Return ``None`` if ``designs``, by device name, place, allocate and route under ``placer``, else the diagnostic.

    ``words`` maps a design symbol to the scratchpad word it shares. Given ``fusion``,
    ``designs`` are its members in step order, built fused (``fused_configuration``).
    """
    exported = [n for n, d in designs.items() if d.op.exported_design() is not None]
    try:
        unvalued(designs)
        if exported:
            (design,) = designs.values()
            module = ir.Module.parse(
                str(design.build()),
                ir.Context(),
            )
        else:
            if fusion is None:
                arrays = {n: BuiltArray(d, words) for n, d in designs.items()}
                configured = configuration(next(iter(arrays)), arrays)
            else:
                configured, _ = fused_configuration(
                    "fused", fusion, list(designs.values()), words
                )
            module = Program.compose(
                [configured], entry=configured.runtimes[0]
            ).resolve_program()
    except (
        ValueError,
        RuntimeError,
        ir.MLIRError,
    ) as e:
        return str(e)
    return places(module, placer)


class Composition:
    """An operator sequence's designs in one module, each device named for its design.

    So aiecc's device cache hits in any graph; ``seq`` is laid out, on a
    ``FullELF``.
    """

    def __init__(self, seq):
        full_elf = seq.packaging
        designs, design_of = seq.unique_designs()
        # unique_designs() made one design per identity, so one name is a collision.
        own = [OperatorDesign(op) for op in designs]
        named: dict[str, OperatorDesign] = {}
        for design in own:
            existing = named.setdefault(design.name, design)
            if existing is not design:
                raise ValueError(
                    f"{existing.op.name} and {design.op.name} are different designs "
                    f"whose device names collide, {design.name}; a tunable given "
                    f"to either one (a tile size, a column count) separates them"
                )
        # A fusion is one step of the composition, at its first member's place.
        self.fusions: dict[str, tuple[tuple[OperatorDesign, ...], Fusion]] = {}
        steps = []
        place: dict[int, int] = {}
        for i, fusion in Fusion.dispatches(seq.fusions, len(seq.steps)):
            place[i] = len(steps)
            if fusion is None:
                s = seq.steps[i]
                steps.append((own[design_of[id(s.op)]].name, s.buffers))
                continue
            member_designs = tuple(
                own[design_of[id(seq.steps[j].op)]] for j in fusion.steps
            )
            symbol = fusion.name([d.name for d in member_designs])
            self.fusions[symbol] = (member_designs, fusion)
            steps.append((symbol, fusion.host_refs(seq.steps)))
        self.steps = steps
        used = {name for name, _ in steps}
        self.designs = {name: design for name, design in named.items() if name in used}
        # A full ELF expands its loads, configuring the array at every call,
        # where it runs more than one design: one design is configured by the
        # first dispatch alone, as the firmware skips an unexpanded load of
        # the PDI it has loaded, unless the build is traced or asks to
        # reconfigure.
        self.expands = (
            len(self.designs) + len(self.fusions) > 1
            or seq.traced
            or full_elf.reconfigure
        )
        self.layout = seq.layout
        self.buffer_sizes = seq.buffer_sizes
        inside = set(range(len(seq.steps))) - set(place)
        if inside & set(full_elf.commands):
            raise ValueError(
                f"a command starts at steps {sorted(inside & set(full_elf.commands))}, "
                f"within a fusion's members, which are one call"
            )
        self.commands = tuple(place[i] for i in full_elf.commands)
        self.shared_words = full_elf.shared_words
        self.packing = self.placed(full_elf.packing)

    def placed(self, packing: Packing) -> Packing:
        """Return ``packing``'s groups that place and route as one device.

        A group the default placer cannot route is placed by the annealing one where
        that routes it (``Packing.annealed``); one neither routes (an operator's
        mapping changed since the profile was tuned) runs unpacked, with a warning.
        """
        groups, annealed = [], set()
        for group in packing.groups:
            members = {n: self.designs[n] for n in group if n in self.designs}
            if len(members) < 2:
                continue
            key = tuple(d.identity for d in members.values())
            if key not in _placed:
                refused = fits(members)
                if refused is None:
                    _placed[key] = (SEQUENTIAL, None)
                elif fits(members, placer=ANNEALED) is None:
                    _placed[key] = (ANNEALED, None)
                else:
                    _placed[key] = (SEQUENTIAL, refused)
            placer, refused = _placed[key]
            if refused is not None:
                logger.warning(
                    "packing %s does not place, so it is not packed: %s",
                    ", ".join(members),
                    refused,
                )
                continue
            groups.append(tuple(members))
            if placer == ANNEALED:
                annealed.update(members)
        return Packing(tuple(groups), tuple(sorted(annealed)))

    @property
    def identity(self) -> str:
        """Return what ``text()`` is a function of.

        So a cache hit costs a hash rather than a composition.
        """
        h = hashlib.sha256()
        for name, design in self.designs.items():
            h.update(f"{name}={design.compilable().recipe_hash};".encode())
        for symbol, (designs, _) in self.fusions.items():
            recipe = "+".join(d.compilable().recipe_hash for d in designs)
            h.update(f"{symbol}={recipe};".encode())
        state = (
            self.steps,
            self.layout,
            self.buffer_sizes,
            sorted(self.shared_words.items()),
            self.packing,
            # Absent when unsplit, so every one-command image keeps its key.
            *([self.commands] if self.commands else []),
            *([self.packing.annealed] if self.packing.annealed else []),
            *(["expands"] if self.expands else []),
        )
        h.update(repr(state).encode())
        return h.hexdigest()[:24]

    def text(self) -> str:
        """Return the composed module: a device configuration per array or pack, and ``main``.

        ``main``'s runtime sequence configures each in turn and runs its
        steps.
        """
        words = self.shared_words
        arrays: dict[str, BuiltArray] = {}
        exported: dict[str, str] = {}
        for name, design in self.designs.items():
            if design.op.exported_design() is None:
                arrays[name] = BuiltArray(design, words)
                continue
            # The composition configures each device; a child that also loads its
            # own links fine and hangs at dispatch (ERT_CMD_STATE_TIMEOUT).
            with compile_context(_iron_full_elf=False):
                exported[name] = str(design.build())
        of = identities(arrays)
        split: dict[Hashable, dict[Hashable, str]] = {}
        for name, array in arrays.items():
            split.setdefault(array.op.array_key(), {}).setdefault(of[name], name)
        for shared in split.values():
            if len(shared) > 1:
                logger.info(
                    "%s have one array_key, but their cores read other scratchpad "
                    "words, so they do not share an array",
                    list(shared.values()),
                )

        packing = self.packing.sharing(
            {n: of[n] if n in arrays else n for n in self.designs}
        )
        sample = next(iter(self.designs.values()), None)
        if sample is None:
            sample = next(iter(self.fusions.values()))[0][0]
        device = sample.op.array_device()
        configurations: dict[str, DeviceConfiguration] = {}
        runtimes: dict[str, Runtime] = {}
        types: dict[str, list] = {}
        for symbol, members in packing.devices(self.designs).items():
            outside = [m for m in members if m in exported]
            if outside and len(members) > 1:
                raise CoResidenceError(
                    f"{outside[0]} is exported by another tool, a device of its "
                    f"own, so it packs with none of {list(members)}"
                )
            if outside:
                (name,) = outside
                configured, types[name] = self._exported(symbol, name, exported[name])
            else:
                configured = configuration(symbol, {m: arrays[m] for m in members})
                for m in members:
                    types[m] = [
                        b.flat_type for b in arrays[m].op.buffers if not b.on_chip
                    ]
            configurations[symbol] = configured
            runtimes.update(zip(members, configured.runtimes))

        # A phased fusion's sequences, each with the span of the fusion's buffers its
        # members take, run in turn where the fusion's step runs.
        phased: dict[str, list[tuple[Runtime, int, int]]] = {}
        for symbol, (designs, fusion) in self.fusions.items():
            configured, members = fused_configuration(symbol, fusion, designs, words)
            configurations[symbol] = configured
            runtimes[symbol] = configured.runtimes[0]
            taken = [
                [b.flat_type for b in array.op.buffers if not b.on_chip]
                for array in members
            ]
            types[symbol] = [t for each in taken for t in each]
            if len(configured.runtimes) > 1:
                ends = list(itertools.accumulate(len(each) for each in taken))
                per = phases(fusion, dict(zip(fusion.steps, members)))
                last = {per[j]: k for k, j in enumerate(fusion.steps)}
                firsts = [0, *(ends[last[p]] for p in sorted(last))]
                phased[symbol] = list(
                    zip(configured.runtimes, firsts[:-1], firsts[1:], strict=True)
                )

        calls = [
            (
                configurations[packing.device_of(name)],
                runtimes[name],
                self._views(name, buffers, types[name]),
                name,
            )
            for name, buffers in self.steps
        ]
        commands = [
            calls[a:b] for a, b in itertools.pairwise((0, *self.commands, len(calls)))
        ]
        arguments = self.buffer_sizes.arguments()

        def sequence_of(command):
            def sequence(*tensors):
                held = dict(zip(arguments, tensors))
                # Consecutive steps in one device share its configure point.
                for configured, steps in itertools.groupby(command, key=lambda c: c[0]):
                    with configured.configure():
                        for _, runtime, views, name in steps:
                            args = [
                                memref.view(
                                    np_ndarray_type_to_memref_type(view_type),
                                    held[kind].op,
                                    constant(offset, index=True),
                                    [],
                                )
                                for kind, offset, view_type in views
                            ]
                            for sequence, a, b in phased.get(
                                name, [(runtime, 0, len(args))]
                            ):
                                sequence.call(*args[a:b])

            return sequence

        # Flat bytes; each buffer is a typed view at its byte offset.
        entries = [
            Runtime(
                sequence_of(command),
                [
                    np.ndarray[(nbytes,), np.dtype[np.int8]]
                    for nbytes in arguments.values()
                ],
                name=self.sequence_name(k),
            )
            for k, command in enumerate(commands)
        ]
        main = DeviceConfiguration(self.device, device, runtimes=entries)
        module = Program.compose(
            [*configurations.values(), main],
            entry=entries[0],
            expand_load_pdis=self.expands or None,
        ).resolve_program()
        # aiecc places the rest with its default placer; these route only so.
        annealed = packing.annealed_devices()
        place = PassManager.parse(
            f"aie.device(aie-place-tiles{{placer={ANNEALED}}})", module.context
        )
        for op in module.body.operations:
            if "sym_name" in op.attributes and (
                ir.StringAttr(op.attributes["sym_name"]).value in annealed
            ):
                place.run(op.operation)
        return str(module)

    # The device configuration every full ELF's commands run on.
    device = "main"

    @staticmethod
    def sequence_name(command: int) -> str:
        """Return the runtime sequence of the ``command``-th command in ``main``."""
        return "sequence" if command == 0 else f"sequence_{command}"

    def _exported(
        self, symbol: str, name: str, text: str
    ) -> tuple[DeviceConfiguration, list]:
        """Return exported design ``name``'s device as configuration ``symbol``, and its sequence's argument types.

        None of its parameters may be a shared word.
        """
        with (
            ir.Context(),
            ir.Location.unknown(),
        ):
            configured = DeviceConfiguration.from_module(
                symbol,
                ir.Module.parse(text),
            )
        (runtime,) = configured.runtimes
        renamed = sorted(
            {p.name for p in runtime.scratchpad_parameters} & set(self.shared_words)
        )
        if renamed:
            raise ValueError(
                f"{name} is exported by another tool, so its scratchpad words "
                f"{renamed} are its own to name; none is shared"
            )
        return configured, runtime.arg_types

    def _views(
        self, name: str, buffers: tuple[BufferRef, ...], types
    ) -> list[tuple[str, int, type]]:
        """Return each of step ``name``'s buffers as ``(argument, byte offset, type)``.

        In the full ELF's arguments; each must match its type's bytes, on a
        shim word.
        """
        views = []
        for buffer, view_type in zip(buffers, types):
            kind, offset, length = buffer.place(self.layout)
            nbytes = math.prod(np_ndarray_type_get_shape(view_type)) * bfp.itemsize(
                np_ndarray_type_get_dtype(view_type)
            )
            if nbytes != length:
                raise ValueError(
                    f"Size mismatch for buffer '{buffer}': the runtime sequence of "
                    f"'{name}' takes {view_type} ({nbytes} bytes), the layout "
                    f"gives it {length} bytes"
                )
            # Low address bits are dropped: it would move.
            if offset % SHIM_ADDRESS_ALIGNMENT:
                raise ValueError(
                    f"Buffer '{buffer}' of '{name}' starts at byte {offset} of the "
                    f"{kind} argument, which is not a multiple of "
                    f"{SHIM_ADDRESS_ALIGNMENT}"
                )
            if kind == "scratch":
                kind, offset = self.buffer_sizes.scratch_argument(offset, length)
            views.append((kind, offset, view_type))
        return views
