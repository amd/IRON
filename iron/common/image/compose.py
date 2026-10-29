# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Composition: a sequence's designs as one module, mlir-aie's
``Program.compose``: a ``DeviceConfiguration`` per array, designs of one
array sharing their device, and a main one whose runtime sequence
configures and runs them in turn.
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
        """This packing with one array's designs in one device, ``arrays`` mapping
        each design in first-use order to it.
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
        return Packing(tuple(tuple(sorted(g, key=order.index)) for g in devices))

    @staticmethod
    def device_name(group: Sequence[str]) -> str:
        """A pack's symbol, independent of its members' order."""
        digest = hashlib.sha256("|".join(sorted(group)).encode()).hexdigest()[:8]
        return f"pack{len(group)}_{digest}"


def independent(seq, fusion: Fusion) -> None:
    """Raise ``CoResidenceError`` where ``fusion`` (a pack) joins two steps
    of ``seq`` that are not independent: one drains a buffer root another
    fills or drains too, a hazard were they issued concurrently.
    """
    reads: dict[int, set[str]] = {}
    writes: dict[int, set[str]] = {}
    for j in fusion.steps:
        step = seq.steps[j]
        r, w = set(), set()
        for ref, b in zip(step.buffers, step.op.buffers):
            if b.fills:
                r.add(ref.root)
            if b.drains:
                w.add(ref.root)
        reads[j], writes[j] = r, w
    for a, i in enumerate(fusion.steps):
        for k in fusion.steps[a + 1 :]:
            if writes[i] & (reads[k] | writes[k]) or writes[k] & reads[i]:
                raise CoResidenceError(
                    f"pack {fusion.steps}: step {i} and step {k} are not "
                    f"independent, so issuing them concurrently is a hazard"
                )


def unvalued(designs: Mapping[str, OperatorDesign]) -> None:
    """Raise ``CoResidenceError`` where one of ``designs`` is built for an xclbin
    and takes a per-call value, a dispatch parameter a pack's sequence cannot carry.
    """
    for name, design in designs.items():
        if not design.full_elf and design.op.values:
            raise CoResidenceError(
                f"{name} takes per-call value {design.op.values[0].name!r}, a "
                f"dispatch parameter on an xclbin, which a pack does not carry"
            )


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


def fits(
    designs: Mapping[str, OperatorDesign], words: Mapping[str, str] | None = None
) -> str | None:
    """``None`` if ``designs``, by device name, place and allocate, else the
    diagnostic; ``words`` maps a design symbol to the scratchpad word it shares.
    """
    exported = [n for n, d in designs.items() if d.op.exported_design() is not None]
    try:
        unvalued(designs)
        if exported:
            (design,) = designs.values()
            module = ir.Module.parse(str(design.build()), ir.Context())
        else:
            arrays = {n: BuiltArray(d, words) for n, d in designs.items()}
            configured = configuration(next(iter(arrays)), arrays)
            module = Program.compose(
                [configured], entry=configured.runtimes[0]
            ).resolve_program()
    except (ValueError, RuntimeError, ir.MLIRError) as e:
        return str(e)
    return places(module)


class Composition:
    """An operator sequence's designs in one module, each device named for its design
    so aiecc's device cache hits in any graph; ``seq`` is laid out, on a ``FullELF``.
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
        # A step fed by another in its fusion is not a step of its own; the
        # fusion reports one combined entry, at its first member's place.
        consumed = {s for fusion in seq.fusions for s in fusion.steps[1:]}
        starts = {fusion.steps[0]: fusion for fusion in seq.fusions}
        self.fusions: dict[str, tuple[tuple[OperatorDesign, ...], Fusion]] = {}
        steps = []
        for i, s in enumerate(seq.steps):
            if i in consumed:
                continue
            fusion = starts.get(i)
            if fusion is None:
                steps.append((own[design_of[id(s.op)]].name, s.buffers))
                continue
            if fusion.kind is FusionKind.PACK:
                independent(seq, fusion)
            member_designs = tuple(
                own[design_of[id(seq.steps[j].op)]] for j in fusion.steps
            )
            symbol = self.fusion_name(fusion, [d.name for d in member_designs])
            self.fusions[symbol] = (member_designs, fusion)
            elided = {(e.producer, e.output) for e in fusion.edges} | {
                (e.consumer, e.input) for e in fusion.edges
            }
            buffers = tuple(
                ref
                for j in fusion.steps
                for ref, b in zip(seq.steps[j].buffers, seq.steps[j].op.buffers)
                if (j, b.name) not in elided
            )
            steps.append((symbol, buffers))
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
        self.commands = full_elf.commands
        self.shared_words = full_elf.shared_words
        self.packing = Packing()

    @staticmethod
    def fusion_name(fusion: Fusion, designs: Sequence[str]) -> str:
        """A fusion's device symbol: content-named, so one hits the cache
        across processes, and distinct from any member's own. Wiring is
        spelled by each member's place in the fusion, not in the sequence,
        so one recurring down a model shares a symbol.
        """
        local = {step: i for i, step in enumerate(fusion.steps)}
        wiring = ",".join(
            f"{local[e.producer]}:{e.output}>{local[e.consumer]}:{e.input}"
            for e in fusion.edges
        )
        digest = hashlib.sha256(
            f"{fusion.kind.value}[{'|'.join(designs)}]({wiring})".encode()
        ).hexdigest()[:8]
        return f"fusion{len(designs)}_{digest}"

    @property
    def identity(self) -> str:
        """What ``text()`` is a function of, so a cache hit costs a hash
        rather than a composition.
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
            *(["expands"] if self.expands else []),
        )
        h.update(repr(state).encode())
        return h.hexdigest()[:24]

    def text(self) -> str:
        """The composed module: a device configuration per array or pack, and
        ``main``, whose runtime sequence configures each in turn and runs its steps.
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

        for symbol, (designs, fusion) in self.fusions.items():
            fanout = {}
            for e in fusion.edges:
                fanout[(e.producer, e.output)] = (
                    fanout.get((e.producer, e.output), 0) + 1
                )
            shared = next(((p, o) for (p, o), n in fanout.items() if n > 1), None)
            if shared is not None:
                raise CoResidenceError(
                    f"{symbol}: step {shared[0]}'s {shared[1]!r} feeds more than "
                    f"one input on-chip; fan-out is not yet buildable"
                )
            incoming: dict[int, list[Edge]] = {}
            for e in fusion.edges:
                incoming.setdefault(e.consumer, []).append(e)
            step_arrays: dict[int, BuiltArray] = {}
            for pos, j in enumerate(fusion.steps):
                fed = {}
                for e in incoming.get(j, ()):
                    (source,) = [
                        b
                        for b in step_arrays[e.producer].op.buffers
                        if b.name == e.output
                    ]
                    fed[e.input] = source
                step_arrays[j] = BuiltArray(designs[pos], words, fed=fed)
            configured = configuration(
                symbol,
                {str(j): step_arrays[j] for j in fusion.steps},
                steps=[str(j) for j in fusion.steps],
                # A merge's steps have no edge to keep alive across a shared
                # task group; run them back to back, each fully awaited.
                fuse=fusion.kind is not FusionKind.MERGE,
            )
            configurations[symbol] = configured
            runtimes[symbol] = configured.runtimes[0]
            types[symbol] = [
                b.flat_type
                for j in fusion.steps
                for b in step_arrays[j].op.buffers
                if not b.on_chip
            ]

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
                        for _, runtime, views, _ in steps:
                            runtime.call(
                                *(
                                    memref.view(
                                        np_ndarray_type_to_memref_type(view_type),
                                        held[kind].op,
                                        constant(offset, index=True),
                                        [],
                                    )
                                    for kind, offset, view_type in views
                                )
                            )

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
        return str(module)

    # The device configuration every full ELF's commands run on.
    device = "main"

    @staticmethod
    def sequence_name(command: int) -> str:
        """The runtime sequence of the ``command``-th command in ``main``."""
        return "sequence" if command == 0 else f"sequence_{command}"

    def _exported(
        self, symbol: str, name: str, text: str
    ) -> tuple[DeviceConfiguration, list]:
        """Exported design ``name``'s device as configuration ``symbol``, and its
        sequence's argument types; none of its parameters may be a shared word.
        """
        with ir.Context(), ir.Location.unknown():
            configured = DeviceConfiguration.from_module(symbol, ir.Module.parse(text))
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
        """Each of step ``name``'s buffers as ``(argument, byte offset, type)`` in
        the full ELF's arguments; each must match its type's bytes, on a shim word.
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
