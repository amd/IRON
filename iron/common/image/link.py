# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The image an operator sequence builds: one full ELF, or a chain of xclbins.

Both compile through mlir-aie's ``CompilableDesign``, which owns the cache:
it keys on what the text is a function of, locks across processes and
validates the kernels' depfiles, and the image lands in its entry.
"""

from dataclasses import dataclass
from pathlib import Path

import aie.utils as aie_utils
from aie import ir
from aie.iron import CompileTime
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.npukernel import NPUKernel

from ..design import OperatorDesign
from .compose import Composition
from .packaging import require_device


class FullELF:
    """The full ELF: every design composed into one module (NPU2 only)."""

    # --get-scratchpad-parameters emits the parameter table the host writes
    # through. Without it the ELF is not the same program.
    FLAGS = ("--get-scratchpad-parameters",)
    # Only when the composition expands its loads (``Composition.expands``): what makes
    # a multi-device runlist switch PDIs between steps.
    EXPAND_FLAG = "--expand-load-pdis"
    # Only when tracing: the trace parser reads the lowered module for the
    # buffer layout and each design's traced tiles and events.
    TRACE_FLAG = "--get-input-with-addresses"

    def __init__(self):
        self.composition: Composition | None = None
        self.design: CompilableDesign | None = None

    def link(self, seq) -> Path:
        """Build the ELF once (idempotent); returns its path.

        Keyed on ``Composition.identity``, so a hit generates nothing: the
        designs are composed, inside ``compile()``, only on a miss.
        """
        design = self.design
        if design is None:
            dev = require_device()
            if not dev.dispatches_full_elf:
                raise RuntimeError(
                    f"{dev.name} ({dev.arch}) does not dispatch a full ELF"
                )
            composition = self.composition = Composition(seq)
            flags = [
                *([self.EXPAND_FLAG] if composition.expands else []),
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

    ``links`` is by ``id(op)`` over the sequence's operators.
    """

    def __init__(self):
        self.image: Path | None = None
        self.links: dict[int, Link] = {}

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
        configs = [
            op.xclbin_operator() if op.external is None else None for op in designs
        ]
        chained = [op for op, config in zip(designs, configs) if config is op]
        # The key reads the current device: bound first, keys before and after agree.
        aie_utils.ensure_current_device()
        built = dict(
            zip(
                map(id, chained),
                CompilableDesign.chain(
                    [OperatorDesign(op, full_elf=False).compilable() for op in chained],
                    seq.name,
                ),
            )
        )
        # One design alone is the xclbin the operator compiled alone builds.
        named = len(chained) > 1

        def kernel(xclbin, design, name="MLIR_AIE") -> NPUKernel:
            return NPUKernel(
                xclbin,
                design.get_cache_entry().insts,
                kernel_name=name,
                dispatch_params=design.dispatch_params,
                dispatch_lib_path=design.get_dispatch_lib_path(),
            )

        links = []
        for op, config in zip(designs, configs):
            if config is None:
                own = OperatorDesign(op, full_elf=False).compile(insts_only=True)
                shipped = op.external.with_instructions(own.get_cache_entry().insts)
                links.append(Link(own, None, op.name, shipped))
                continue
            if config is op:
                design, image, label = built[id(op)]
                name = label if named else op.name
                links.append(Link(design, design, name, kernel(image, design, label)))
                continue
            image = OperatorDesign(config, full_elf=False).compile()
            # On an xclbin a per-call value is a dispatch-time scalar: the
            # stream is generated per call, by a library only a full build has.
            own = OperatorDesign(op, full_elf=False).compile(
                image=None if op.values else image, insts_only=not op.values
            )
            xclbin = image.get_cache_entry().xclbin
            links.append(Link(own, image, config.name, kernel(xclbin, own)))
        for op in seq.unique_operators():
            self.links[id(op)] = links[design_of[id(op)]]
        last = built[id(chained[-1])][1] if chained else links[-1].kernel.xclbin_path
        self.image = Path(last)
        return self.image
