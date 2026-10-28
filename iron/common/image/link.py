# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The image an operator sequence builds: one full ELF, or a chain of xclbins.

Both compile through mlir-aie's ``CompilableDesign``, which owns the cache:
it keys on what the text is a function of, locks across processes and
validates the kernels' depfiles, and the image lands in its entry.
"""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import aie.utils as aie_utils
from aie import ir
from aie.iron import CompileTime
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.npukernel import NPUKernel

from ..declare import Operator
from ..design import OperatorDesign
from ..design.design import capped_aiecc_flags
from .artifacts import Design
from .callable import FullELFCallable, PerStepCallable
from .compose import Composition
from .packaging import require_device


class FullELF:
    """The full ELF: every design composed into one module (NPU2 only).

    Args:
        reconfigure: Configure the array at every call, even for one design.
        commands: The steps that each start a command after the first.
        shared_words: Design symbol -> the scratchpad word it shares.
    """

    # --get-scratchpad-parameters emits the parameter table the host writes
    # through. Without it the ELF is not the same program.
    FLAGS = ("--get-scratchpad-parameters",)
    # Only when tracing: the trace parser reads the lowered module for the
    # buffer layout and each design's traced tiles and events.
    TRACE_FLAG = "--get-input-with-addresses"

    def __init__(
        self,
        reconfigure: bool = False,
        commands: Sequence[int] = (),
        shared_words: Mapping[str, str] | None = None,
    ):
        self.reconfigure = reconfigure
        self.commands = tuple(commands)
        self.shared_words = dict(shared_words or {})
        self.composition: Composition | None = None
        self.design: CompilableDesign | None = None

    @staticmethod
    def in_arena(scratch: list[str], residents: Mapping[str, object]) -> list[str]:
        """The scratch buffers an arena holds: all of them, one argument."""
        return scratch

    def link(self, seq) -> Path:
        """Build the ELF once and return its path; keyed on
        ``Composition.identity``, a cache hit composes nothing.
        """
        design = self.design
        if design is None:
            dev = require_device()
            if not dev.can_dispatch_full_elf:
                raise RuntimeError(
                    f"{dev.name} ({dev.arch}) does not dispatch a full ELF"
                )
            composition = self.composition = Composition(seq)
            flags = [
                *self.FLAGS,
                *([self.TRACE_FLAG] if seq.traced else []),
            ]

            # The cache follows the modules a generator reaches, not the state
            # of what it closes over, so the identity is one.
            def generator(key: CompileTime[str]) -> ir.Module:
                return ir.Module.parse(composition.text())

            design = CompilableDesign(
                generator,
                compile_kwargs={"key": composition.identity},
                full_elf=True,
                aiecc_flags=capped_aiecc_flags(
                    [
                        *flags,
                        *(f for op in seq.unique_operators() for f in op.aiecc_flags),
                    ]
                ),
            )
            design.compile()
            self.design = design
        entry = design.get_cache_entry()
        assert entry is not None and entry.elf is not None, "compile() built it"
        return Path(entry.elf)

    def record(self, designs: list[Operator], sharing: list[tuple[str, ...]]):
        """The designs' records, the ELF's cache entry, and no one stream."""
        assert self.design is not None, "link() built the image"
        records = tuple(
            Design(name=f"op{i}_{type(op).__name__}", operators=sharing[i])
            for i, op in enumerate(designs)
        )
        return records, self.design.get_cache_entry(), None

    def callable(self, seq, arena) -> FullELFCallable:
        return FullELFCallable(seq, arena=arena)


@dataclass(frozen=True)
class Link:
    """Where one design of an xclbin chain runs: its own ``design``'s stream on
    ``configuration``'s xclbin (None on a shipped image), as ``kernel``.
    """

    design: CompilableDesign
    configuration: CompilableDesign | None
    name: str
    kernel: NPUKernel


class PerStep:
    """An xclbin and stream per design, each linked onto the previous
    (``CompilableDesign.chain``), ``image`` the last link; a design on another
    operator's ``configuration``, or a shipped image, runs that xclbin unlinked.
    """

    def __init__(self, check: bool = False):
        self.check = check
        self.image: Path | None = None
        self.links: dict[int, Link] = {}

    @staticmethod
    def in_arena(scratch: list[str], residents: Mapping[str, object]) -> list[str]:
        """The scratch buffers the arena holds: only the residents, as the rest
        live in this image's own pool (``PerStepCallable``).
        """
        return [r for r in scratch if r in residents]

    def link(self, seq) -> Path:
        """Build the chain once and return the last link, or the last design's
        own image where none is linked.
        """
        if self.image is not None:
            return self.image
        # One kernel instance per design, not per operator: operators
        # reporting one design_key generate one module, so they link one
        # xclbin and run one instruction stream.
        designs, design_of = seq.unique_designs()
        configs = [
            op.xclbin_operator() if op.external is None else None for op in designs
        ]
        chained = [op for op, config in zip(designs, configs) if config is op]
        # The key reads the current device: bound first, keys before and after agree.
        aie_utils.ensure_current_device()
        built = CompilableDesign.chain(
            [OperatorDesign(op, full_elf=False).compilable() for op in chained],
            seq.name,
        )
        # One design alone is the xclbin the operator compiled alone builds.
        named = len(built) > 1

        def kernel(xclbin, design, name="MLIR_AIE") -> NPUKernel:
            return NPUKernel(
                xclbin,
                design.get_cache_entry().insts,
                kernel_name=name,
                dispatch_params=design.dispatch_params,
                dispatch_lib_path=design.get_dispatch_lib_path(),
            )

        def linked(design, image, label, name) -> Link:
            return Link(
                design, design, label if named else name, kernel(image, design, label)
            )

        ops = dict(zip(map(id, chained), built))
        links: dict[int, Link] = {}
        for i, (op, config) in enumerate(zip(designs, configs)):
            if config is None:
                own = OperatorDesign(op, full_elf=False).compile(insts_only=True)
                shipped = op.external.with_instructions(own.get_cache_entry().insts)
                links[i] = Link(own, None, op.name, shipped)
            elif config is op:
                links[i] = linked(*ops[id(op)], op.name)
            else:
                image = OperatorDesign(config, full_elf=False).compile()
                # On an xclbin a per-call value is a dispatch-time scalar: the
                # stream is generated per call, by a library only a full build has.
                own = OperatorDesign(op, full_elf=False).compile(
                    image=None if op.values else image, insts_only=not op.values
                )
                xclbin = image.get_cache_entry().xclbin
                links[i] = Link(own, image, config.name, kernel(xclbin, own))
        for op in seq.unique_operators():
            self.links[id(op)] = links[design_of[id(op)]]
        last = built[-1][1] if built else list(links.values())[-1].kernel.xclbin_path
        self.image = Path(last)
        return self.image

    def record(self, designs: list[Operator], sharing: list[tuple[str, ...]]):
        """The designs' records, the first design's cache entry, and its
        stream where it is the only one.
        """
        links = [self.links[id(op)] for op in designs]
        records = tuple(
            Design(
                name=link.name,
                operators=sharing[i],
                entry=(
                    link.design if link.configuration is None else link.configuration
                ).get_cache_entry(),
                image=Path(link.kernel.xclbin_path),
                insts=link.design.get_cache_entry().insts,
            )
            for i, link in enumerate(links)
        )
        entry = links[0].design.get_cache_entry()
        return records, entry, entry.insts if len(links) == 1 else None

    def callable(self, seq, arena) -> PerStepCallable:
        return PerStepCallable(seq, check=self.check, arena=arena)
