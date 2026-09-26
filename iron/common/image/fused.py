# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The image an operator sequence builds: one fused ELF, or a chain of xclbins."""

import hashlib
import inspect

import aie.utils as aie_utils
from aie.iron.device import NPU2

from . import fusion
from .jit_compile import (
    cache_entry,
    design_identity,
    dispatch_stream,
    fused_design,
    source_digest,
    xclbin_design,
)


def fused_plan(seq):
    """Each design's device, by name, and the runlist over those names.

    A device is named for what it is -- its class and its design's identity
    -- not for where it sits in this sequence, so one design is one device
    text whichever graph it is fused into and at whatever step. aiecc's
    device cache keys on that text, and a positional name kept decode and
    prefill from sharing any device, and a graph that gained a step from
    reusing its own. Designs whose identities agree generate the same
    device, so they are fused as one.
    """
    designs, design_of = seq.unique_designs()
    names = []
    generators = {}
    for op in designs:
        generator = op.generator()
        name = f"{type(op).__name__}_{design_identity(generator)[:8]}"
        names.append(name)
        generators.setdefault(name, generator)
    runlist = [(names[design_of[id(op)]], *bufs) for op, *bufs in seq.runlist]
    return generators, runlist


def build_fused_mlir(seq, plan=None) -> str:
    """The fused MLIR text: every design inlined into one module.

    ``seq``'s buffer layout (``subbuffer_layout``, ``buffer_sizes``,
    ``slice_info``) must already be set.
    """
    generators, runlist = plan or fused_plan(seq)
    return fusion.fuse_mlir(
        generators,
        runlist,
        seq.subbuffer_layout,
        seq.buffer_sizes,
        seq.slice_info,
    )


def _design_sources(generator) -> list:
    """The modules a design is defined in: its function's, and its class's.

    A design's own key hashes the operator's class source; the fused key
    also takes its modules, since a helper beside the class is as much the
    design as the class is.
    """
    design_fn, _, kwargs = generator.resolve()
    classes = []
    if "op" in kwargs:
        classes = list(type(kwargs["op"]).__mro__)
    files = set()
    for obj in (design_fn, *classes):
        try:
            files.add(inspect.getsourcefile(obj))
        except TypeError:
            pass  # a builtin
    return sorted(f for f in files if f)


def fused_identity(seq, plan) -> str:
    """What the fused text is a function of, without generating it.

    The designs, each by its identity (:func:`design_identity`: the code
    that generates it and the parameters it is called with); the runlist over
    them; the buffer layout; and the source of what turns those into text --
    IRON's common tree, where the fusion and the declaration layer live, the
    operators' own modules, and mlir-aie's Python frontend
    (:func:`source_digest`). A hit then costs a hash rather than a fusion.
    """
    generators, runlist = plan
    h = hashlib.sha256()
    files = set()
    for name, generator in generators.items():
        h.update(f"{name}={design_identity(generator)};".encode())
        files.update(_design_sources(generator))
    h.update(source_digest(tuple(sorted(files))).encode())
    h.update(
        repr((runlist, seq.subbuffer_layout, seq.buffer_sizes, seq.slice_info)).encode()
    )
    return h.hexdigest()[:24]


class FusedImage:
    """The full ELF: every design fused into one module (NPU2 only)."""

    def __init__(self):
        self.design = None

    def link(self, seq):
        """Build the ELF once (idempotent); returns its path.

        Through CompilableDesign, which owns the cache: it keys on
        :func:`fused_identity`, locks across processes and validates the
        kernels' depfiles, and the ELF lands in its entry.
        """
        if not isinstance(aie_utils.get_current_device(), NPU2):
            raise RuntimeError(
                "dispatch='fused' requires NPU2; NPU1 has no full-ELF dispatch"
            )
        if self.design is None:
            plan = fused_plan(seq)
            self.design = fused_design(
                lambda: build_fused_mlir(seq, plan),
                fused_identity(seq, plan),
                extra_flags=seq.extra_flags,
                trace_size=seq.trace_size,
            )
        return cache_entry(self.design).elf


class XclbinChain:
    """One xclbin and instruction stream per design, each linked onto the
    previous (``--xclbin-input``); the last link carries every kernel. Holds
    the per-operator designs the xclbin callable dispatches with.
    """

    def __init__(self):
        self.combined_xclbin_path = None
        self.op_design_map = {}  # id(op) -> CompilableDesign
        self.op_xclbin_path_map = {}  # id(op) -> xclbin path
        self.op_insts_path_map = {}  # id(op) -> insts path, or a DispatchStream
        self.op_kernel_name_map = {}  # id(op) -> kernel name

    def link(self, seq):
        """Build the chain once (idempotent); returns the last link."""
        if self.combined_xclbin_path is not None:
            return self.combined_xclbin_path
        # Short hash keeps kernel names under xclbinutil's 64-char "name:name" limit.
        name_hash = hashlib.sha1(seq.name.encode()).hexdigest()[:6]

        # One kernel instance per design, not per operator: with
        # share_designs, operators reporting one design_key generate one
        # module, so they link one xclbin and run one instruction stream.
        designs, design_of = seq.unique_designs()
        prev_xclbin_path = None
        built = []
        for idx, op in enumerate(designs):
            op_label = f"f{name_hash}_op{idx}"
            kernel_id = f"0x{0x901 + idx:x}"
            design = xclbin_design(
                op.generator(image="xclbin"),
                kernel_name=op_label,
                xclbin_input=prev_xclbin_path,
                extra_flags=[
                    f"--xclbin-instance-name={op_label}",
                    f"--xclbin-kernel-id={kernel_id}",
                ],
            )
            entry = cache_entry(design)
            stream = dispatch_stream(design) or entry.insts
            built.append((design, entry.xclbin, stream, op_label))
            prev_xclbin_path = entry.xclbin

        for op in seq.unique_operators():
            design, xclbin_path, stream, op_label = built[design_of[id(op)]]
            self.op_design_map[id(op)] = design
            self.op_xclbin_path_map[id(op)] = xclbin_path
            self.op_insts_path_map[id(op)] = stream
            self.op_kernel_name_map[id(op)] = op_label

        # The last xclbin in the chain carries all the linked instances.
        self.combined_xclbin_path = prev_xclbin_path
        return self.combined_xclbin_path
