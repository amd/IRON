# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The image an operator sequence builds: one fused ELF, or a chain of xclbins.

Both compile through mlir-aie's ``CompilableDesign``, which owns the cache:
it keys on what the text is a function of, locks across processes and
validates the kernels' depfiles, and the image lands in its entry.
"""

import hashlib
from pathlib import Path

import aie.utils as aie_utils
from aie import ir
from aie.iron import CompileTime
from aie.utils.compile.jit.compilabledesign import CompilableDesign

from ..design import OperatorDesign
from .fusion import Fusion
from .packaging import full_elf


class FusedImage:
    """The full ELF: every design fused into one module (NPU2 only)."""

    # --expand-load-pdis is what makes a multi-device runlist switch PDIs
    # between steps; --get-scratchpad-parameters emits the parameter table the
    # host writes through. Without them the ELF is not the same program.
    FLAGS = ("--expand-load-pdis", "--get-scratchpad-parameters")
    # Only when tracing: the trace parser reads the lowered module for the
    # buffer layout and each design's traced tiles and events.
    TRACE_FLAG = "--get-input-with-addresses"

    def __init__(self):
        self.fusion: Fusion | None = None
        self.design: CompilableDesign | None = None

    def link(self, seq) -> Path:
        """Build the ELF once (idempotent); returns its path.

        Keyed on ``Fusion.identity``, so a hit generates nothing: the
        designs are fused, inside ``compile()``, only on a miss.
        """
        design = self.design
        if design is None:
            dev = aie_utils.ensure_current_device()
            if dev is None:
                raise RuntimeError("dispatch='fused' links for a device; none is bound")
            if not full_elf(dev):
                raise RuntimeError(
                    f"dispatch='fused' needs a full ELF, which {dev.name} "
                    f"({dev.arch}) does not dispatch"
                )
            fusion = self.fusion = Fusion(seq)
            flags = [*self.FLAGS, *([self.TRACE_FLAG] if seq.traced else [])]

            # The cache follows the modules a generator reaches, not the state
            # of what it closes over, so the identity is one.
            def generator(key: CompileTime[str]) -> ir.Module:
                return ir.Module.parse(fusion.text())

            design = CompilableDesign(
                generator,
                compile_kwargs={"key": fusion.identity},
                full_elf=True,
                aiecc_flags=list(
                    dict.fromkeys(
                        [
                            *flags,
                            *seq.extra_flags,
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


class XclbinChain:
    """One xclbin and instruction stream per design, each linked onto the
    previous (``--xclbin-input``); the last link carries every kernel.

    ``designs`` and ``labels`` are by ``id(op)`` over the sequence's
    operators: the compiled design and the kernel name each dispatches with.
    """

    def __init__(self):
        self.image: Path | None = None
        self.designs: dict[int, CompilableDesign] = {}
        self.labels: dict[int, str] = {}

    def link(self, seq) -> Path:
        """Build the chain once (idempotent); returns the last link."""
        if self.image is not None:
            return self.image
        # Short hash keeps kernel names under xclbinutil's 64-char "name:name" limit.
        name_hash = hashlib.sha1(seq.name.encode()).hexdigest()[:6]

        # One kernel instance per design, not per operator: operators
        # reporting one design_key generate one module, so they link one
        # xclbin and run one instruction stream.
        designs, design_of = seq.unique_designs()
        built = []
        for idx, op in enumerate(designs):
            label = f"f{name_hash}_op{idx}"
            flags = [
                f"--xclbin-kernel-name={label}",
                f"--xclbin-instance-name={label}",
                f"--xclbin-kernel-id=0x{0x901 + idx:x}",
            ]
            if self.image is not None:
                # The predecessor is part of what this image is, and reaches
                # the key through the flags.
                flags.append(f"--xclbin-input={self.image.resolve()}")
            design = OperatorDesign(op, "xclbin").compile(aiecc_flags=flags)
            built.append((design, label))
            entry = design.get_cache_entry()
            assert entry is not None and entry.xclbin is not None
            self.image = Path(entry.xclbin)

        for op in seq.unique_operators():
            self.designs[id(op)], self.labels[id(op)] = built[design_of[id(op)]]
        assert self.image is not None, "a sequence has at least one design"
        return self.image
