# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The image an operator sequence builds: one fused ELF, or a chain of xclbins."""

import hashlib
import inspect

import aie.utils as aie_utils
from aie.iron.device import NPU2

from . import fusion
from .jit_compile import dispatch_stream, fused_design, xclbin_design

def build_fused_mlir(seq) -> str:
    """The fused MLIR text: every design inlined into one module.

    ``seq``'s buffer layout (``subbuffer_layout``, ``buffer_sizes``,
    ``slice_info``) must already be set.
    """
    operator_generators = {}
    comp_runlist = []
    designs, design_of = seq.unique_designs()
    design_names = []

    for idx, op in enumerate(designs):
        generator = op.generator()
        # Ask the design whether it takes a prefix, rather than inferring it
        # from the operator having kernel artifacts: a design that declares
        # ExternalFunctions reports no artifacts at all, so inferring leaves
        # every shape defining the same symbols, kept apart only by each
        # core linking its own object.
        design_fn, _, _ = generator.resolve()
        if "func_prefix" in inspect.signature(design_fn).parameters:
            generator.kwargs["func_prefix"] = f"op{idx}_"
        op_name = f"op{idx}_{op.__class__.__name__}"
        design_names.append(op_name)
        operator_generators[op_name] = generator

    for op, *bufs in seq.runlist:
        comp_runlist.append((design_names[design_of[id(op)]], *bufs))

    return fusion.fuse_mlir(
        operator_generators,
        comp_runlist,
        seq.subbuffer_layout,
        seq.buffer_sizes,
        seq.slice_info,
    )


class FusedImage:
    """The full ELF: every design fused into one module (NPU2 only)."""

    def __init__(self):
        self.design = None

    def link(self, seq):
        """Build the ELF once (idempotent); returns its path.

        Through CompilableDesign, which owns the cache: it keys on the fused
        text's content, locks across processes and validates the kernels'
        depfiles, and the ELF lands in its entry.
        """
        if not isinstance(aie_utils.get_current_device(), NPU2):
            raise RuntimeError(
                "dispatch='fused' requires NPU2; NPU1 has no full-ELF dispatch"
            )
        if self.design is None:
            self.design = fused_design(
                lambda: build_fused_mlir(seq),
                extra_flags=seq.extra_flags,
                trace_size=seq.trace_size,
            )
        return self.design.get_cache_entry().elf


class XclbinChain:
    """One xclbin and instruction stream per design, each linked onto the
    previous (``--xclbin-input``); the last link carries every kernel. Holds
    the per-operator designs the xclbin callable dispatches with."""

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
            entry = design.get_cache_entry()
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
