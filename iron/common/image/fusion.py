# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Temporal fusion: a sequence's designs as one module, mlir-aie's
``Program.compose``: a ``DeviceConfiguration`` per array (designs of one
array each run their own sequence over it) or per pack of arrays
(``coresidence``), and a main one whose runtime sequence configures and
runs them in turn.
"""

from __future__ import annotations

import hashlib
import itertools
import logging
import math
from collections.abc import Collection, Hashable
from typing import NamedTuple

import numpy as np
from aie import ir
from aie.dialects import aie, arith, memref
from aie.helpers.npdtypes import np_ndarray_type_get_dtype, np_ndarray_type_get_shape
from aie.helpers.util import mlir_type_to_np_dtype, np_ndarray_type_to_memref_type
from aie.iron import DeviceConfiguration, Program, Runtime
from aie.utils import bfp
from aie.utils.compile.jit.compilabledesign import compile_context

from ..design import BuiltArray, OperatorDesign, identities
from .allocator import BANK
from .coresidence import AdjacentPacking, CoResidenceError, Packing, fits, pack
from .step import BufferRef

logger = logging.getLogger(__name__)

# The shim DMA addresses host memory in 32-bit words, so every buffer handed
# to a sub-design must start on one.
SHIM_ADDRESS_ALIGNMENT = 4


class ArgumentSizes(NamedTuple):
    """Bytes of each runtime-sequence argument of a fused image, in argument
    order; ``feedback`` is ``None`` where the image takes no such argument.

    The scratch arena is passed as its banks (``allocator.BANK``), each an
    argument: ``scratch`` the first, ``scratch_k`` the k-th after it, the
    last arguments.
    """

    input: int
    output: int
    scratch: int
    feedback: int | None = None

    @property
    def bank_kinds(self) -> list[str]:
        """The scratch arena's arguments, a bank each: ``scratch``, then
        ``scratch_1`` on.
        """
        banks = max(1, -(-self.scratch // BANK))
        return ["scratch", *(f"scratch_{k}" for k in range(1, banks))]

    def arguments(self) -> dict[str, int]:
        """Size by kind, in argument order."""
        kinds = self.bank_kinds
        banks = [min(BANK, self.scratch - k * BANK) for k in range(len(kinds))]
        sizes = {"input": self.input, "output": self.output, "scratch": banks[0]}
        if self.feedback is not None:
            sizes["feedback"] = self.feedback
        sizes.update(zip(kinds[1:], banks[1:]))
        return sizes

    def scratch_argument(self, offset: int, length: int) -> tuple[str, int]:
        """The argument a scratch buffer of ``length`` bytes at ``offset``
        is in, and its offset there.

        Raises:
            ValueError: It crosses from one bank into the next.
        """
        k = offset // BANK
        if length and (offset + length - 1) // BANK != k:
            raise ValueError(
                f"a scratch buffer of {length} bytes at {offset} crosses from "
                f"bank {k} into the next, of {BANK} bytes each"
            )
        return self.bank_kinds[k], offset - k * BANK


class Fusion:
    """An operator sequence's designs, fused into one module.

    Each device is named for its design, not its step, so its text is the
    same in every graph and aiecc's device cache hits. ``seq.coresident``
    packs designs into one device each. ``seq``'s buffer layout must already
    be set.
    """

    def __init__(self, seq):
        designs, design_of = seq.unique_designs()
        own = [OperatorDesign(op) for op in designs]
        self.designs: dict[str, OperatorDesign] = {}
        for design in own:
            existing = self.designs.setdefault(design.name, design)
            if existing.identity != design.identity:
                raise ValueError(
                    f"{existing.op.name} and {design.op.name} are different designs "
                    f"whose device names collide, {design.name}; a tunable given "
                    f"to either one (a tile size, a column count) separates them"
                )
        self.steps = [(own[design_of[id(s.op)]].name, s.buffers) for s in seq.steps]
        self.expands = self.expanded(
            self.designs, traced=seq.traced, reconfigure=seq.reconfigure
        )
        self.layout = seq.layout
        self.buffer_sizes = seq.buffer_sizes
        self.commands = seq.commands
        self.shared_words = dict(seq.shared_words or {})
        self.packing: Packing | AdjacentPacking = (
            seq.coresident
            if isinstance(seq.coresident, AdjacentPacking)
            else Packing(
                tuple(
                    tuple(dict.fromkeys(own[design_of[id(op)]].name for op in group))
                    for group in seq.coresident
                )
            )
        )

    @staticmethod
    def expanded(
        designs: Collection[Hashable],
        *,
        traced: bool = False,
        reconfigure: bool = False,
    ) -> bool:
        """Whether a full ELF of ``designs`` expands its loads, configuring
        the array at every call. One design is configured by the first
        dispatch alone, as the firmware skips an unexpanded load of the PDI
        it has loaded, unless the build is traced or asks to ``reconfigure``.
        """
        return len(designs) > 1 or traced or reconfigure

    @property
    def identity(self) -> str:
        """What ``text()`` is a function of, so a cache hit costs a hash
        rather than a fusion. ``expands`` reaches the key through the link's
        flags.
        """
        h = hashlib.sha256()
        for name, design in self.designs.items():
            h.update(f"{name}={design.compilable().recipe_hash};".encode())
        state = (
            self.steps,
            self.layout,
            self.buffer_sizes,
            sorted(self.shared_words.items()),
            self.packing,
            # Absent when unsplit, so every one-command image keeps its key.
            *([self.commands] if self.commands else []),
        )
        h.update(repr(state).encode())
        return h.hexdigest()[:24]

    def text(self) -> str:
        """The fused module: a device configuration per array or pack, and a
        main one whose runtime sequence configures each in runlist order and
        runs its steps there.

        Raises:
            CoResidenceError: A pack holds a design another tool exports, or
                two of its arrays program one pinned tile.
            ValueError: A buffer's layout disagrees with the sequence it is
                handed to, or a shared word names an exported design's own.
        """
        words = self.shared_words
        arrays: dict[str, BuiltArray] = {}
        exported: dict[str, str] = {}
        for name, design in self.designs.items():
            if design.op.exported_design() is None:
                arrays[name] = BuiltArray(design, words)
                continue
            # The fusion configures each device; a child that also loads its
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

        packing = self.packing
        if isinstance(packing, AdjacentPacking):
            packing, _ = packing.pack(
                [name for name, _ in self.steps], self.designs, words
            )
        packing = packing.sharing(
            {n: of[n] if n in arrays else n for n in self.designs},
            lambda members: fits({m: self.designs[m] for m in members}, words),
        )
        device = next(iter(self.designs.values())).op.array_device()
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
                configured = pack(symbol, {m: arrays[m] for m in members})
                for m in members:
                    types[m] = [b.flat_type for b in arrays[m].op.buffers]
            configurations[symbol] = configured
            runtimes.update(zip(members, configured.runtimes))

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
                                        arith.constant(ir.IndexType.get(), offset),
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
        main = DeviceConfiguration("main", device, runtimes=entries)
        module = Program.compose(
            [*configurations.values(), main],
            entry=entries[0],
        ).resolve_program()
        return str(module)

    @staticmethod
    def sequence_name(command: int) -> str:
        """The runtime sequence of the ``command``-th command in ``main``."""
        return "sequence" if command == 0 else f"sequence_{command}"

    def _exported(
        self, symbol: str, name: str, text: str
    ) -> tuple[DeviceConfiguration, list]:
        """Exported design ``name``'s device as configuration ``symbol``, and
        its runtime sequence's argument types.

        Raises:
            ValueError: A shared word names one of its parameters.
        """
        with ir.Context(), ir.Location.unknown():
            foreign = ir.Module.parse(text)
            configured = DeviceConfiguration.from_module(symbol, foreign)
            (device_op,) = [
                op for op in foreign.body.operations if isinstance(op, aie.DeviceOp)
            ]
            (sequence_op,) = [
                op
                for op in device_op.body_region.blocks[0].operations
                if isinstance(op, aie.RuntimeSequenceOp)
            ]
            types = []
            for arg in sequence_op.body.blocks[0].arguments:
                memref_type = ir.MemRefType(arg.type)
                dtype = mlir_type_to_np_dtype(memref_type.element_type)
                types.append(np.ndarray[tuple(memref_type.shape), np.dtype[dtype]])
        (runtime,) = configured.runtimes
        renamed = sorted(
            {p.name for p in runtime.scratchpad_parameters} & set(self.shared_words)
        )
        if renamed:
            raise ValueError(
                f"{name} is exported by another tool, so its scratchpad words "
                f"{renamed} are its own to name; none is shared"
            )
        return configured, types

    def _views(
        self, name: str, buffers: tuple[BufferRef, ...], types
    ) -> list[tuple[str, int, type]]:
        """Where step ``name``'s buffers are in the fused image's arguments:
        ``(argument, byte offset, type)`` each, ``type`` that of its
        sequence's argument.

        Raises:
            ValueError: A buffer's bytes differ from its argument's, or it
                starts off a shim address.
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
