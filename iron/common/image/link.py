# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The image an operator sequence builds: one full ELF, or a chain of xclbins.

Both compile through mlir-aie's ``CompilableDesign``, which owns the cache:
it keys on what the text is a function of, locks across processes and
validates the kernels' depfiles, and the image lands in its entry.
"""

import hashlib
import itertools
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import aie.utils as aie_utils
from aie import ir
from aie.iron import CompileTime, Program
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.npukernel import NPUKernel

from ..declare import Operator
from ..design import BuiltArray, OperatorDesign
from .artifacts import Design
from .callable import FullELFCallable, PerStepCallable
from .compose import Composition
from .coresidence import AdjacentPacking, Packing, pack, unvalued
from .packaging import require_device


class FullELF:
    """The full ELF: every design composed into one module (NPU2 only).

    Args:
        coresident: Groups of operators whose designs share one device
            configuration, or an ``AdjacentPacking`` that chooses them.
        reconfigure: Configure the array at every call even where it runs
            one design, which the first call otherwise configures for all
            (``Composition.expands``).
        commands: The steps that start a command of their own after the
            first's, each command a runtime sequence a call queues after
            the one before it.
        shared_words: Design symbol -> the scratchpad word it shares with
            others that always hold the same number.
    """

    # --get-scratchpad-parameters emits the parameter table the host writes
    # through. Without it the ELF is not the same program.
    FLAGS = ("--get-scratchpad-parameters",)
    # Only when tracing: the trace parser reads the lowered module for the
    # buffer layout and each design's traced tiles and events.
    TRACE_FLAG = "--get-input-with-addresses"

    def __init__(
        self,
        coresident: Sequence[Sequence[Operator]] | AdjacentPacking = (),
        reconfigure: bool = False,
        commands: Sequence[int] = (),
        shared_words: Mapping[str, str] | None = None,
    ):
        self.coresident = coresident
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
        """Build the ELF once (idempotent); returns its path.

        Keyed on ``Composition.identity``, so a hit generates nothing: the
        designs are composed, inside ``compile()``, only on a miss.
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
    """Where one design of an xclbin chain runs.

    Attributes:
        design: Its own build, whose stream (or dispatch library) it runs.
        configuration: The build whose xclbin it runs on; None on a shipped
            image.
        name: The design's name in the record.
        kernel: Its stream on the xclbin carrying its kernel instance.
    """

    design: CompilableDesign
    configuration: CompilableDesign | None
    name: str
    kernel: NPUKernel


class PerStep:
    """One xclbin and instruction stream per design, each linked onto the
    previous (mlir-aie's ``CompilableDesign.chain``): the last link of each
    chain carries its kernels, ``image`` the last chain's.

    A design whose ``Operator.configuration`` is another operator runs that
    configuration's own xclbin, built once for every shape it serves, and a
    shipped image (``image=``) is the download: neither is linked into the
    chain, and only the design's stream is built.

    Steps that run back to back on one pack of ``coresident`` are one link
    instead, the pack's arrays and one sequence running theirs in turn
    (``Runtime.merge``), so a dispatch configures the array once for them;
    a step of a pack between steps of others runs its own design.

    A run is cut where it would pass the kernel more than ``HOST_BUFFERS``
    buffers.

    ``links`` is by ``id(op)`` over the sequence's operators, and ``runs``
    by a run's first step: its end and link.

    Args:
        check: Check each step against its reference on the NPU's inputs
            (``callable.check_step``).
        coresident: Groups of operators whose steps run as one, or an
            ``AdjacentPacking`` that chooses them.

    Raises:
        ValueError: Both are given, as ``check`` dispatches each step alone.
    """

    # aiecc binds at most this many host buffer objects to a kernel (kMaxHostBOs).
    HOST_BUFFERS = 16

    def __init__(
        self,
        check: bool = False,
        coresident: Sequence[Sequence[Operator]] | AdjacentPacking = (),
    ):
        if check and coresident:
            raise ValueError(
                "check=True dispatches each step alone, so nothing packs: pass "
                "check=False or drop coresident"
            )
        self.check = check
        self.coresident = coresident
        self.image: Path | None = None
        self.links: dict[int, Link] = {}
        self.runs: dict[int, tuple[int, Link]] = {}
        self.run_records: tuple[Design, ...] = ()

    @staticmethod
    def in_arena(scratch: list[str], residents: Mapping[str, object]) -> list[str]:
        """The scratch buffers the cross-version arena holds: the residents,
        as every other one lives in this image's own pool instead
        (``PerStepCallable``).
        """
        return [r for r in scratch if r in residents]

    def link(self, seq) -> Path:
        """Build the chain once (idempotent); returns the last link, or the
        last design's own image where none is linked.
        """
        if self.image is not None:
            return self.image
        # One kernel instance per design, not per operator: operators
        # reporting one design_key generate one module, so they link one
        # xclbin and run one instruction stream.
        designs, design_of = seq.unique_designs()
        names = [OperatorDesign(op, full_elf=False).name for op in designs]
        order = [names[design_of[id(s.op)]] for s in seq.steps]
        runs = self._runs(order, dict(zip(names, designs)))
        merged = {i for start, end in runs for i in range(start, end)}
        alone = {
            design_of[id(s.op)] for i, s in enumerate(seq.steps) if i not in merged
        }
        configs = [
            op.xclbin_operator() if op.external is None else None for op in designs
        ]
        chained = [
            op
            for i, (op, config) in enumerate(zip(designs, configs))
            if config is op and i in alone
        ]
        packs = {tuple(order[a:b]): runs[a, b] for a, b in runs}
        # The key reads the current device: bound first, keys before and after agree.
        aie_utils.ensure_current_device()
        built = CompilableDesign.chain(
            [
                *(OperatorDesign(op, full_elf=False).compilable() for op in chained),
                *(_run(group, steps) for steps, group in packs.items()),
            ],
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

        by_pack = {
            steps: linked(*b, Packing.device_name(packs[steps]))
            for steps, b in zip(packs, built[len(chained) :])
        }
        ops = dict(zip(map(id, chained), built))
        links: dict[int, Link] = {}
        for i, (op, config) in enumerate(zip(designs, configs)):
            if i not in alone:
                continue
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
        self.runs = {a: (b, by_pack[tuple(order[a:b])]) for a, b in runs}
        operators: dict[int, dict[str, None]] = {}
        for a, (b, run) in self.runs.items():
            operators.setdefault(id(run), {}).update(
                dict.fromkeys(s.op.name for s in seq.steps[a:b])
            )
        self.run_records = tuple(
            Design(
                name=run.name,
                operators=tuple(operators[id(run)]),
                entry=run.design.get_cache_entry(),
                image=Path(run.kernel.xclbin_path),
                insts=run.design.get_cache_entry().insts,
            )
            for run in by_pack.values()
        )
        for op in seq.unique_operators():
            d = design_of[id(op)]
            self.links[id(op)] = links.get(d) or next(
                link for a, (b, link) in self.runs.items() if names[d] in order[a:b]
            )
        last = built[-1][1] if built else list(links.values())[-1].kernel.xclbin_path
        self.image = Path(last)
        return self.image

    def _runs(
        self, order: list[str], designs: Mapping[str, Operator]
    ) -> dict[tuple[int, int], dict[str, OperatorDesign]]:
        """Each run of two or more steps back to back on one pack, by its
        ``(first, end)`` steps: the pack's designs, by name.

        Raises:
            CoResidenceError: A run's pack holds a design that takes a
                per-call value.
        """
        if not self.coresident:
            return {}
        own = {n: OperatorDesign(op, full_elf=False) for n, op in designs.items()}
        if isinstance(self.coresident, AdjacentPacking):
            packing, _ = self.coresident.pack(order, own)
        else:
            packing = Packing.of(self.coresident, own, full_elf=False)
        pieces: list[tuple[list[int], tuple[str, ...]]] = []
        for device, steps in itertools.groupby(
            enumerate(order), key=lambda step: packing.device_of(step[1])
        ):
            if device in designs:
                continue
            count = self.HOST_BUFFERS
            for i, name in steps:
                # The merged sequence takes each step's buffers in turn.
                n = len(designs[name].buffers)
                if count + n > self.HOST_BUFFERS:
                    pieces.append(([], packing.group_of(name)))
                    count = 0
                pieces[-1][0].append(i)
                count += n
        runs = {}
        for steps, group in pieces:
            if len(steps) > 1:
                members = {n: own[n] for n in group}
                unvalued(members)
                runs[steps[0], steps[-1] + 1] = members
        return runs

    def record(self, designs: list[Operator], sharing: list[tuple[str, ...]]):
        """The designs' records then the runs', the first design's cache
        entry, and its stream where it is the only one.
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
        return (
            (*records, *self.run_records),
            entry,
            entry.insts if len(links) == 1 else None,
        )

    def callable(self, seq, arena) -> PerStepCallable:
        return PerStepCallable(seq, check=self.check, arena=arena)


def _run(
    group: Mapping[str, OperatorDesign], steps: tuple[str, ...]
) -> CompilableDesign:
    """``group``'s arrays in one device whose one sequence runs ``steps``'
    in turn, keyed on what its text is a function of.
    """
    h = hashlib.sha256(
        repr(([d.compilable().recipe_hash for d in group.values()], steps)).encode()
    )

    def generator(key: CompileTime[str]) -> ir.Module:
        configured = pack(
            Composition.device, {n: BuiltArray(d) for n, d in group.items()}, steps
        )
        return Program.compose(
            [configured], entry=configured.runtimes[0]
        ).resolve_program()

    return CompilableDesign(
        generator,
        compile_kwargs={"key": h.hexdigest()[:24]},
        aiecc_flags=list(
            dict.fromkeys(f for d in group.values() for f in d.op.aiecc_flags)
        ),
    )
