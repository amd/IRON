# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The image an operator sequence builds: one full ELF, or a chain of xclbins.

Both compile through mlir-aie's ``CompilableDesign``, which owns the cache:
it keys on what the text is a function of, locks across processes and
validates the kernels' depfiles, and the image lands in its entry.
"""

import functools
import hashlib
import inspect
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from pathlib import Path

import aie.utils as aie_utils
from aie import ir
from aie.iron import CompileTime, DispatchTime, Program
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.npukernel import NPUKernel

from ..declare import Operator
from ..design import BuiltArray, OperatorDesign, configuration
from .artifacts import Design
from .callable import FullELFCallable, PerStepCallable
from .compose import Composition
from .packaging import require_device
from .step import Fusion


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
                aiecc_flags=list(
                    dict.fromkeys(
                        [
                            *flags,
                            *(
                                f
                                for op in seq.unique_operators()
                                for f in op.aiecc_flags
                            ),
                        ]
                    )
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


class FusedDesign:
    """A stream fusion's steps as one design: each member's array, fed where
    an edge feeds it on-chip, and one ``MergedRuntime.fuse`` sequence
    (``configuration(..., fuse=True)``), compiled as one xclbin, dispatched
    once with every member's per-call values as dispatch-time scalars.
    """

    def __init__(self, fusion: Fusion, ops: Sequence[Operator]):
        foreign = [
            op
            for op in ops
            if op.external is not None or op.xclbin_operator() is not op
        ]
        if foreign:
            raise ValueError(
                f"{fusion.kind.value} fusion: "
                f"{[type(op).__name__ for op in foreign]} ships or shares another "
                f"operator's xclbin, which a fusion cannot build into one"
            )
        self.fusion = fusion
        self.designs = [OperatorDesign(op, full_elf=False) for op in ops]
        dtypes: dict[str, object] = {}
        for design in self.designs:
            for v in design.op.values:
                seen = dtypes.setdefault(v.symbol, v.dtype)
                if seen != v.dtype:
                    raise ValueError(
                        f"{type(design.op).__name__}.{v.name}: per-call value "
                        f"{v.symbol!r} is {seen} in one fusion member and "
                        f"{v.dtype} in another"
                    )
        P = inspect.Parameter
        params = [
            P(symbol, P.KEYWORD_ONLY, annotation=DispatchTime[dtype])
            for symbol, dtype in dtypes.items()
        ]
        keys = [
            P("ops", P.KEYWORD_ONLY, annotation=CompileTime[tuple]),
            P("identity", P.KEYWORD_ONLY, annotation=CompileTime[str]),
        ]

        def generator(ops: CompileTime[tuple], identity: CompileTime[str], **kwargs):
            return self.module(**kwargs)

        setattr(generator, "__signature__", inspect.Signature([*params, *keys]))
        self.generator = generator

    def module(self, **dispatch):
        """The fused module: each member's array, in fusion order, wired by
        its edges, as one device configuration and sequence.
        """
        incoming: dict[int, list] = {}
        for e in self.fusion.edges:
            incoming.setdefault(e.consumer, []).append(e)
        arrays: dict[int, BuiltArray] = {}
        for pos, j in enumerate(self.fusion.steps):
            fed = {}
            for e in incoming.get(j, ()):
                (source,) = (
                    b for b in arrays[e.producer].op.buffers if b.name == e.output
                )
                fed[e.input] = source
            arrays[j] = BuiltArray(self.designs[pos], dispatch=dispatch, fed=fed)
        keys = [str(j) for j in self.fusion.steps]
        configured = configuration(
            self.name,
            dict(zip(keys, (arrays[j] for j in self.fusion.steps))),
            steps=keys,
            fuse=True,
        )
        return Program.compose(
            [configured], entry=configured.runtimes[0]
        ).resolve_program()

    @functools.cached_property
    def identity(self) -> str:
        """What ``module()`` is built from: each member's own identity and the
        wiring between them, distinct from any standalone design's.
        """
        text = repr(
            (
                self.fusion.kind.value,
                tuple(d.identity for d in self.designs),
                tuple(
                    (e.producer, e.output, e.consumer, e.input)
                    for e in self.fusion.edges
                ),
                "xclbin",
            )
        )
        return hashlib.sha256(text.encode()).hexdigest()[:24]

    @property
    def name(self) -> str:
        """The fusion's device symbol, content-named like a full ELF's
        (``Composition.fusion_name``), so a recurring fusion hits the cache.
        """
        return Composition.fusion_name(self.fusion, [d.name for d in self.designs])

    def compilable(self, **options) -> CompilableDesign:
        flags = [
            *options.pop("aiecc_flags", ()),
            *dict.fromkeys(f for d in self.designs for f in d.op.aiecc_flags),
        ]
        return CompilableDesign(
            self.generator,
            compile_kwargs={
                "ops": tuple(d.op for d in self.designs),
                "identity": self.identity,
            },
            aiecc_flags=flags,
            **options,
        )


class PerStep:
    """An xclbin and stream per design, each linked onto the previous
    (``CompilableDesign.chain``), ``image`` the last link; a design on another
    operator's ``configuration``, or a shipped image, runs that xclbin unlinked.
    A fusion's steps link as one ``FusedDesign``, dispatched together.
    """

    def __init__(self, check: bool = False):
        self.check = check
        self.image: Path | None = None
        # By operator identity, for record(): a unique design's own Link.
        self.links: dict[int, Link] = {}
        # By step index, for PerStepCallable: the same operator identity can
        # be a fusion's member at one step and its own design at another, so
        # dispatch keys on the step, not the operator.
        self.step_links: dict[int, Link] = {}

    @staticmethod
    def in_arena(scratch: list[str], residents: Mapping[str, object]) -> list[str]:
        """The scratch buffers the arena holds: only the residents, as the rest
        live in this image's own pool (``PerStepCallable``).
        """
        return [r for r in scratch if r in residents]

    def link(self, seq) -> Path:
        """Build the chain once and return the last link, or the last design's
        own image where none is linked; a fusion's steps take their place in
        the chain as one ``FusedDesign``.
        """
        if self.image is not None:
            return self.image
        # One kernel instance per design, not per operator: operators
        # reporting one design_key generate one module, so they link one
        # xclbin and run one instruction stream. seq.unique_designs() does
        # not know about fusions, so a fused member's design may also be
        # shared with a plain (unfused) use elsewhere; plain_idx tracks
        # which unique designs have one.
        designs, design_of = seq.unique_designs()
        configs = [
            op.xclbin_operator() if op.external is None else None for op in designs
        ]
        starts = {fusion.steps[0]: fusion for fusion in seq.fusions}
        consumed = {s for fusion in seq.fusions for s in fusion.steps[1:]}
        chain_items: list[Operator | Fusion] = []
        plain_idx: dict[int, int] = {}
        for i, step in enumerate(seq.steps):
            if i in consumed:
                continue
            fusion = starts.get(i)
            if fusion is not None:
                chain_items.append(fusion)
                continue
            idx = design_of[id(step.op)]
            if configs[idx] is not designs[idx] or idx in plain_idx:
                continue
            plain_idx[idx] = len(chain_items)
            chain_items.append(designs[idx])
        # The key reads the current device: bound first, keys before and after agree.
        aie_utils.ensure_current_device()
        fused_designs: dict[int, FusedDesign] = {}

        def compilable(item: Operator | Fusion) -> CompilableDesign:
            if isinstance(item, Fusion):
                design = fused_designs[id(item)] = FusedDesign(
                    item, [seq.steps[j].op for j in item.steps]
                )
                return design.compilable()
            return OperatorDesign(item, full_elf=False).compilable()

        built = CompilableDesign.chain(
            [compilable(item) for item in chain_items], seq.name
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

        chained = dict(zip(map(id, chain_items), built))
        links: dict[int, Link] = {}
        for i, (op, config) in enumerate(zip(designs, configs)):
            if config is None:
                own = OperatorDesign(op, full_elf=False).compile(insts_only=True)
                shipped = op.external.with_instructions(own.get_cache_entry().insts)
                links[i] = Link(own, None, op.name, shipped)
            elif config is op:
                if i not in plain_idx:
                    continue  # every use of this design is a fusion member
                links[i] = linked(*chained[id(op)], op.name)
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
            i = design_of[id(op)]
            if i in links:
                self.links[id(op)] = links[i]
        for i, step in enumerate(seq.steps):
            if i in consumed:
                continue
            fusion = starts.get(i)
            if fusion is None:
                idx = design_of[id(step.op)]
                if idx in links:
                    self.step_links[i] = links[idx]
                continue
            design = fused_designs[id(fusion)]
            base = linked(*chained[id(fusion)], design.name)
            self.step_links[i] = base
            for j in fusion.steps:
                # Shares the fused xclbin (kernel, design, configuration);
                # each member keeps its own name to report, as a full ELF's
                # fusion members each keep theirs.
                self.links[id(seq.steps[j].op)] = replace(
                    base, name=seq.steps[j].op.name
                )
        last = (
            built[-1][1] if built else list(self.links.values())[-1].kernel.xclbin_path
        )
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
