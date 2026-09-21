# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import hashlib
import inspect
import logging
import time
from pathlib import Path
import numpy as np
import ml_dtypes
from . import compilation as comp
from .base import AIEOperatorBase, MLIROperator
from .jit_compile import DispatchStream
import aie.utils as aie_utils
from aie.iron.device import NPU2
from aie.utils.hostruntime.tensor_class import CPUOnlyTensor
from aie.utils.npukernel import NPUKernel

try:
    import pyxrt
    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
except ImportError:
    # Host stacks without XRT (e.g. the HRX/amdxdna runtime) have no pyxrt. The two
    # on-device dispatch policies below are XRT-native (pyxrt.elf / hw_context / run,
    # plus XRTTensor views), so they cannot run there; _require_xrt() makes that
    # explicit at construction. The CPU policy and the whole compile path do not care,
    # and must keep importing.
    pyxrt = None
    XRTTensor = None

logger = logging.getLogger(__name__)


def _torch():
    """Import torch for CPU reference/compare paths. Compile and NPU dispatch do not."""
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError(
            "OperatorSequence CPU reference/compare modes need torch. "
            "Compile and NPU dispatch do not."
        ) from exc
    return torch


def _require_xrt() -> None:
    """Fail with the reason, rather than an AttributeError on ``None.elf``."""
    if pyxrt is None:
        raise RuntimeError(
            "this OperatorSequence dispatch policy needs the XRT host runtime (pyxrt), "
            "which is not installed. Use SequenceCPUCallable, or run a single operator "
            "(AIEOperatorBase), which dispatches through aie.utils.DefaultNPURuntime and "
            "works on any backend."
        )


# ##########################################################################
# Dispatch policies
# ##########################################################################


def full_elf_path(seq):
    """Where a fused sequence's ELF is, however it got built.

    Set by FusedDispatch.link_elf() when it compiles one. Nothing else
    produces a full ELF now that the artifact rule is gone.
    """
    elf_path = getattr(seq, "elf_path", None)
    if elf_path is None:
        raise RuntimeError(
            f"{seq.name!r} has no full ELF: link_elf() has not run. "
            "get_callable() triggers it; calling the dispatch policy directly "
            "does not."
        )
    return elf_path


class SequenceDispatch:
    """Policy object that decides how an :class:`OperatorSequence` is compiled
    and how its runtime callable is built.

    One concrete policy corresponds to one dispatch mode. The three hooks are:

    * ``resolve(device)`` -- the only device-aware step; expands ``"auto"`` to
      a concrete policy and validates device requirements. Called once, at
      ``set_up_artifacts()`` time (the device is not known at construction).
    * ``set_up_artifacts(seq)`` -- registers the compile artifacts for this
      mode on the owning sequence.
    * ``make_callable(seq)`` -- returns the runtime callable for this mode.
    """

    name = None

    def resolve(self, device):
        """Return the concrete policy for ``device`` (default: unchanged)."""
        return self

    def set_up_artifacts(self, seq):
        """Register the compile artifacts needed by this mode on ``seq``."""
        raise NotImplementedError

    def link(self, seq):
        """Build this mode's image and return its path; ``None`` if it has none.

        The ahead-of-time half of ``make_callable``: everything up to, but
        not including, the runtime that loads it, so a host without an NPU
        can compile a sequence and hand the image on.
        """
        return None

    def make_callable(self, seq):
        """Return the runtime callable for this mode."""
        raise NotImplementedError


class AutoDispatch(SequenceDispatch):
    """Selects the platform default: full-ELF on NPU2, chained-xclbin elsewhere."""

    name = "auto"

    def resolve(self, device):
        if isinstance(device, NPU2):
            return FusedDispatch()
        return SeparateDispatch()


def _trace_tag(seq):
    """Tracing adds a runtime-sequence argument, so a traced build cannot reuse an
    untraced one's ELF. Empty when untraced."""
    return f"_traced{seq.trace_size}" if seq.trace_size else ""


class FusedDispatch(SequenceDispatch):
    """Single-ELF dispatch (NPU2 only): all operators fused into one ELF."""

    name = "fused"

    def resolve(self, device):
        if not isinstance(device, NPU2):
            raise RuntimeError(
                "dispatch='fused' requires NPU2; NPU1 has no full-ELF dispatch"
            )
        return self

    def set_up_artifacts(self, seq):
        # Nothing. Each child's kernels are ExternalFunctions its design
        # declares, compiled by CompilableDesign when the fused ELF is built,
        # and the fused MLIR is computed fresh in memory by build_fused_mlir().
        return

    def link_elf(self, seq):
        """Link the fused ELF.

        Done here rather than as a compilation rule: this is the step that now
        goes through CompilableDesign, which keys its cache on content, locks
        across processes and validates depfiles -- none of which the artifact
        graph does.
        """
        from .jit_compile import compile_fused_elf

        if getattr(seq, "elf_path", None) is not None:
            return seq.elf_path
        seq.elf_path = compile_fused_elf(
            lambda: self.build_fused_mlir(seq),
            Path(seq.context.build_dir) / f"{seq.name}{_trace_tag(seq)}.elf",
            extra_flags=seq.extra_flags,
            trace_size=seq.trace_size,
        )
        return seq.elf_path

    def build_fused_mlir(self, seq, runlist=None) -> str:
        """Build the fused MLIR source that inlines every operator into a
        single module, and return it as text.

        ``seq``'s buffer-layout attributes (``subbuffer_layout``,
        ``buffer_sizes``, ``slice_info``) must already be set. ``runlist``
        is a slice of the sequence's, for a chunk: the module carries the
        designs that slice uses, over the whole sequence's buffer layout.
        """
        return build_fused_mlir(seq, runlist)

    def link(self, seq):
        return self.link_elf(seq)

    def make_callable(self, seq):
        self.link_elf(seq)
        return SequenceFullELFCallable(seq)


def build_fused_mlir(seq, runlist=None) -> str:
    """The fused module for ``runlist`` (default: all of ``seq``'s steps)."""
    if runlist is None:
        runlist = seq.runlist
    operator_generators = {}
    comp_runlist = []
    designs, design_of = seq.unique_designs()
    used = {design_of[id(op)] for op, *_ in runlist}
    design_names = {}

    for idx, op in enumerate(designs):
        if idx not in used:
            continue
        generator = op.get_mlir_artifact().generator
            # Ask the design whether it takes a prefix, rather than inferring it
            # from the operator having kernel artifacts: an operator whose
            # design declares ExternalFunctions reports no artifacts at all, and
            # under the old test silently went unprefixed -- every shape then
            # defining the same symbols, kept apart only by each core linking
            # its own object.
        design_fn, _, _ = generator.resolve()
        if "func_prefix" in inspect.signature(design_fn).parameters:
            generator.kwargs["func_prefix"] = f"op{idx}_"
        op_name = f"op{idx}_{op.__class__.__name__}"
        design_names[idx] = op_name
        operator_generators[op_name] = generator

    for op, *bufs in runlist:
        comp_runlist.append((design_names[design_of[id(op)]], *bufs))

    return comp.fuse_mlir(
        operator_generators,
        comp_runlist,
        seq.subbuffer_layout,
        seq.buffer_sizes,
        seq.slice_info,
    )


class ChunkedDispatch(SequenceDispatch):
    """Chunked dispatch: a fused sub-sequence of ``n`` steps per kernel, in one xclbin.

    ``boundaries=chunks(n)`` in the packaging surface, and ``image=xclbin``
    with no boundaries is one chunk of every step (spike S1's construction).
    Each chunk is the fused module of its steps over the whole sequence's
    buffer layout, compiled as an xclbin kernel with its configuration
    switches expanded, and linked onto the previous chunk's xclbin; the
    callable runs the kernels in order over the three arena buffers, as
    the full ELF's one sequence would. Not on this path: scratchpad
    values, which an xclbin run has no scratchpad for (spike S2).
    """

    name = "chunked"

    def __init__(self, n=None):
        if n is not None and n < 1:
            raise ValueError("chunks(n) needs n >= 1")
        self.n = n
        self.chunks = []  # (label, xclbin_path, insts_path, n_steps)
        self.combined_xclbin_path = None

    def resolve(self, device):
        return self

    def set_up_artifacts(self, seq):
        return

    def slices(self, seq):
        n = self.n or len(seq.runlist)
        return [seq.runlist[i : i + n] for i in range(0, len(seq.runlist), n)]

    def link_xclbins(self, seq):
        if self.combined_xclbin_path is not None:
            return
        from .jit_compile import compile_fused_xclbin

        name_hash = hashlib.sha1(seq.name.encode()).hexdigest()[:6]
        build_dir = Path(seq.context.build_dir)
        previous = None
        for idx, steps in enumerate(self.slices(seq)):
            label = f"f{name_hash}_chunk{idx}"
            xclbin_path, insts_path = compile_fused_xclbin(
                lambda steps=steps: build_fused_mlir(seq, steps),
                build_dir,
                label,
                kernel_id=f"0x{0x901 + idx:x}",
                xclbin_input=previous,
                extra_flags=seq.extra_flags,
            )
            self.chunks.append((label, xclbin_path, insts_path, len(steps)))
            previous = xclbin_path
        self.combined_xclbin_path = previous

    def link(self, seq):
        self.link_xclbins(seq)
        return self.combined_xclbin_path

    def make_callable(self, seq):
        self.link_xclbins(seq)
        return SequenceChunkedCallable(seq, self)


class SeparateDispatch(SequenceDispatch):
    """Chained-xclbin dispatch: one xclbin+insts per unique operator, linked
    via ``--xclbin-input`` and invoked sequentially. Owns the compiled
    per-operator xclbin/insts path maps consumed by the runtime callable.
    """

    name = "separate"

    def __init__(self):
        self.combined_xclbin_path = None
        self.op_xclbin_path_map = {}  # id(op) -> xclbin path
        self.op_insts_path_map = {}  # id(op) -> insts path
        self.op_kernel_name_map = {}  # id(op) -> kernel_name

    def set_up_artifacts(self, seq):
        # Nothing, for the same reason as FusedDispatch: each operator's
        # kernels are declared by its design and compiled by CompilableDesign
        # in link_xclbins().
        return

    def link_xclbins(self, seq):
        """Compile the chained xclbin+insts pair per unique operator.

        Mirrors ``FusedDispatch.link_elf``: called from ``make_callable`` once
        the artifact graph has resolved kernel-object paths and compiled them,
        so this only has to generate MLIR and hand it to CompilableDesign
        through :func:`jit_compile.compile_xclbin_insts`.
        """
        if self.combined_xclbin_path is not None:
            return
        from .jit_compile import compile_xclbin_insts

        # Short hash keeps kernel names under xclbinutil's 64-char "name:name" limit.
        name_hash = hashlib.sha1(seq.name.encode()).hexdigest()[:6]
        build_dir = Path(seq.context.build_dir)

        # One kernel instance per design, not per operator: with
        # share_designs, operators reporting one design_key generate one
        # module, so they link one xclbin and run one instruction stream.
        designs, design_of = seq.unique_designs()
        prev_xclbin_path = None
        built = []
        for idx, op in enumerate(designs):
            op_label = f"f{name_hash}_op{idx}"
            kernel_id = f"0x{0x901 + idx:x}"
            xclbin_path, insts_path = compile_xclbin_insts(
                op.get_mlir_artifact(image="xclbin").generator,
                build_dir / f"{op_label}.xclbin",
                build_dir / f"{op_label}.bin",
                kernel_name=op_label,
                xclbin_input=prev_xclbin_path,
                extra_flags=[
                    f"--xclbin-instance-name={op_label}",
                    f"--xclbin-kernel-id={kernel_id}",
                ],
            )
            built.append((xclbin_path, insts_path, op_label))
            prev_xclbin_path = xclbin_path

        for op in seq.unique_operators():
            xclbin_path, insts_path, op_label = built[design_of[id(op)]]
            self.op_xclbin_path_map[id(op)] = xclbin_path
            self.op_insts_path_map[id(op)] = insts_path
            self.op_kernel_name_map[id(op)] = op_label

        # The last xclbin in the chain carries all the linked instances.
        self.combined_xclbin_path = prev_xclbin_path

    def link(self, seq):
        self.link_xclbins(seq)
        return self.combined_xclbin_path

    def make_callable(self, seq):
        self.link_xclbins(seq)
        return SequenceXclbinCallable(seq, self)


class CompareDispatch(SeparateDispatch):
    """Same compile path as ``separate``, but the callable additionally re-runs
    each operator's CPU ``reference()`` on the NPU-produced inputs and flags
    per-step deviation.

    Args:
        rel_tol / abs_tol: Per-step tolerances; a step counts as a mismatch
            only when it exceeds both.
        raise_on_mismatch: When True (default), raise ``RuntimeError`` on the
            first mismatching step instead of only logging it.
    """

    name = "compare"

    def __init__(self, rel_tol=0.05, abs_tol=1e-2, raise_on_mismatch=True):
        super().__init__()
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol
        self.raise_on_mismatch = raise_on_mismatch

    def make_callable(self, seq):
        self.link_xclbins(seq)
        return SequenceCompareCallable(seq, self)


class ReferenceDispatch(SequenceDispatch):
    """Pure-CPU evaluation via each operator's ``reference()``; compiles nothing."""

    name = "reference"

    def set_up_artifacts(self, seq):
        pass

    def make_callable(self, seq):
        return SequenceReferenceCallable(seq)


_DISPATCH_ALIASES = {
    "auto": AutoDispatch,
    "fused": FusedDispatch,
    "separate": SeparateDispatch,
    "compare": CompareDispatch,
    "reference": ReferenceDispatch,
    "chunked": ChunkedDispatch,
}


# ##########################################################################
# Compileable: operator sequence
# ##########################################################################


class OperatorSequence(AIEOperatorBase):
    """Operator that concatenates a runlist of operators into a
    single dispatch.

    Args:
        dispatch: Dispatch strategy, given either as a mode name or as a
            :class:`SequenceDispatch` instance. Recognised names:
            ``"auto"`` (default) selects ``"fused"`` on NPU2 and
            ``"separate"`` on NPU1.  ``"fused"`` uses a single-ELF
            dispatch (requires NPU2).  ``"separate"`` compiles each
            sub-operator to its own xclbin and invokes them sequentially.
            ``"reference"`` runs only the per-operator CPU reference
            implementations (no NPU compilation/dispatch).  ``"compare"``
            runs the ``"separate"`` xclbin path and, after each NPU step,
            also runs the operator's CPU reference on the NPU-produced
            inputs and logs the deviation for testing/debugging.  Pass a
            :class:`CompareDispatch` instance to tune the compare tolerances.
    """

    def __init__(
        self,
        name,
        runlist,
        input_args,
        output_args,
        buffer_sizes=None,
        buffer_offsets=None,
        plan_scratch=True,
        dispatch="auto",
        extra_flags=None,
        trace_size=0,
        share_designs=False,
        *args,
        **kwargs,
    ):
        dispatch = self._coerce_dispatch(dispatch)
        if not all(
            isinstance(op, MLIROperator) and all(isinstance(buf, str) for buf in bufs)
            for op, *bufs in runlist
        ):
            raise TypeError(
                "runlist entries must be (MLIROperator, *str) tuples; "
                "each operator must be an MLIROperator and each buffer name must be a str"
            )
        super().__init__(*args, **kwargs)
        self.runlist = runlist
        # Sharing changes which designs are built, so it belongs in the name that
        # keys the build artifacts.
        self.name = name + "_shared" if share_designs else name
        self.input_args = input_args
        self.output_args = output_args
        # Planned byte offsets per buffer name; None keeps the
        # back-to-back layout this had before.
        self.buffer_offsets = buffer_offsets
        # Pool intermediates whose lifetimes do not overlap. On by default:
        # the layout is inferred from the runlist, so a caller does not supply
        # it. Pass False to fall back to packing every buffer back to back,
        # which is what this did before planning existed.
        self.plan_scratch = plan_scratch
        self.explicit_buffer_sizes = (
            buffer_sizes or {}
        )  # Optional dict: buffer_name -> size_in_bytes
        # Extra aiecc flags forwarded to the full-ELF build.
        self.extra_flags = extra_flags or []
        # Bytes of hardware trace buffer per runlist step; 0 leaves the design untraced.
        self.trace_size = trace_size
        self.share_designs = share_designs
        self._dispatch = dispatch

    @staticmethod
    def _coerce_dispatch(dispatch):
        """Normalise the ``dispatch`` argument to a :class:`SequenceDispatch`."""
        if isinstance(dispatch, SequenceDispatch):
            return dispatch
        elif isinstance(dispatch, str) and dispatch in _DISPATCH_ALIASES:
            return _DISPATCH_ALIASES[dispatch]()
        raise TypeError("selected dispatch mode not supported")

    def unique_operators(self):
        """Operators in runlist order, de-duplicated by identity."""
        seen = {}
        for op, *_ in self.runlist:
            seen.setdefault(id(op), op)
        return list(seen.values())

    def unique_designs(self):
        """The designs to build, and which design each operator uses.

        With ``share_designs`` set, operators reporting the same ``design_key``
        collapse onto one design, so it is built, prefixed and configured once.
        """
        designs = []
        design_of = {}
        first_with_key = {}
        for op in self.unique_operators():
            key = op.design_key() if self.share_designs else None
            if key is not None and key in first_with_key:
                shared = designs[first_with_key[key]]
                if op.get_arg_spec() != shared.get_arg_spec():
                    raise ValueError(
                        f"{op.name} and {shared.name} report the same design_key but "
                        "different runtime arguments, so the design cannot be shared"
                    )
                design_of[id(op)] = first_with_key[key]
                continue
            if key is not None:
                first_with_key[key] = len(designs)
            design_of[id(op)] = len(designs)
            designs.append(op)
        return designs, design_of

    def infer_buffer_offsets(self):
        """Byte offsets letting intermediates with disjoint lifetimes overlap.

        Only buffers this sequence both writes and later reads are pooled.
        Anything the host addresses -- the sequence's own inputs and outputs,
        and any buffer given an explicit size -- is pinned: its contents
        outlive the sequence, so it needs a private, stable address.
        """
        from .allocator import live_ranges, plan

        sizes, steps = {}, []
        for op, *bufs in self.runlist:
            reads, writes = [], []
            for buf, spec in zip(bufs, op.get_arg_spec()):
                sizes.setdefault(buf, spec.nbytes())
                if spec.reads:
                    reads.append(buf)
                if spec.writes:
                    writes.append(buf)
            steps.append((reads, writes))

        pinned = set(self.input_args) | set(self.output_args)
        pinned |= set(self.explicit_buffer_sizes)
        # A slice is not free to move: it has to sit at its parent's offset
        # plus its start, and calculate_buffer_layout resolves it that way.
        # Pooling one would hand it an address unrelated to its parent, which
        # is silent -- the slice simply reads the wrong memory.
        pinned |= {name for name in sizes if "[" in name}
        ranges = live_ranges(steps, pinned=pinned)
        allocations, _ = plan(ranges, sizes)
        return {name: a.offset for name, a in allocations.items()}

    def calculate_buffer_layout(self):
        args = {}  # base_buffer_name -> args_spec
        sliced_buffers = (
            {}
        )  # full_buffer_name (with slice) -> (base_name, start, end, args_spec)

        for op, *bufs in self.runlist:
            args_specs = op.get_arg_spec()
            if len(args_specs) != len(bufs):
                raise ValueError(
                    f"Number of buffers ({len(bufs)}) must match operator argument "
                    f"specification ({len(args_specs)}) for operator {op!r}"
                )
            for i, buf_name in enumerate(bufs):
                args_spec = args_specs[i]

                # Parse slice notation: "buffer_name[start:end]"
                if "[" in buf_name and buf_name.endswith("]"):
                    base_name = buf_name[: buf_name.index("[")]
                    slice_part = buf_name[buf_name.index("[") + 1 : -1]
                    start, end = map(int, slice_part.split(":"))
                    sliced_buffers[buf_name] = (base_name, start, end, args_spec)
                    # Track that base buffer exists (size will be set later)
                    if (
                        base_name not in args
                        and base_name not in self.explicit_buffer_sizes
                    ):
                        raise ValueError(
                            f"Sliced buffer '{buf_name}' requires explicit size for base buffer '{base_name}' in buffer_sizes parameter"
                        )
                else:
                    if buf_name not in args:
                        args[buf_name] = args_spec
                    else:
                        if np.prod(args[buf_name].shape) != np.prod(args_spec.shape):
                            raise ValueError(
                                f"Buffer '{buf_name}' has conflicting sizes between operators: "
                                f"{args[buf_name].shape} vs {args_spec.shape}"
                            )

        # Verify all input/output args are present (either as regular or sliced buffers)
        all_buffer_names = set(args.keys()) | set(sliced_buffers.keys())
        for arg in self.input_args:
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise ValueError(f"Input argument {arg} not found in runlist buffers")
        for arg in self.output_args:
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise ValueError(f"Output argument {arg} not found in runlist buffers")

        subbuffer_layout = {}
        slice_info = {}  # full_buffer_name -> (base_name, start, end)

        def add_buffers(buffer_type, args_list):
            # Without a plan, buffers pack back to back in declaration order and
            # every one stays resident for the whole sequence. A plan assigns
            # offsets from liveness instead, so buffers whose lifetimes do not
            # overlap share addresses; the arena still has to be large enough
            # for the highest byte any of them reaches.
            offsets = self.buffer_offsets
            if offsets is None and self.plan_scratch:
                offsets = self.infer_buffer_offsets()
            offsets = offsets or {}

            def length_of(arg):
                if arg in self.explicit_buffer_sizes:
                    # Explicit size specified - this is a parent buffer for slices
                    return self.explicit_buffer_sizes[arg]
                if arg in args:
                    spec = args[arg]
                    return int(np.prod(spec.shape) * np.dtype(spec.dtype).itemsize)
                return None  # sliced buffers are handled separately

            # Unplanned buffers first, packed back to back exactly as before.
            cursor = 0
            planned = []
            for arg in args_list:
                length = length_of(arg)
                if length is None:
                    continue
                if arg in offsets:
                    planned.append((arg, length))
                    continue
                subbuffer_layout[arg] = (buffer_type, cursor, length)
                cursor += length

            # Then the planned ones, rebased past everything unplanned. A plan
            # is relative to its own pool and starts at zero, so applying it
            # directly would drop the first planned buffer on top of the
            # weights -- an aliasing that is silent, because the arena simply
            # does not grow.
            end = cursor
            for arg, length in planned:
                at = cursor + offsets[arg]
                subbuffer_layout[arg] = (buffer_type, at, length)
                end = max(end, at + length)
            return end  # arena size

        # Add sliced buffer entries to layout (they reference parent buffers)
        for buf_name, (base_name, start, end, args_spec) in sliced_buffers.items():
            slice_info[buf_name] = (base_name, start, end)

        input_buffer_size = add_buffers("input", self.input_args)
        output_buffer_size = add_buffers("output", self.output_args)
        scratch_args = [
            arg
            for arg in args
            if arg not in self.input_args and arg not in self.output_args
        ]
        # Also include explicit buffers that are only used for slicing
        for explicit_buf in self.explicit_buffer_sizes:
            if (
                explicit_buf not in self.input_args
                and explicit_buf not in self.output_args
                and explicit_buf not in scratch_args
            ):
                scratch_args.append(explicit_buf)
        scratch_buffer_size = add_buffers("scratch", scratch_args)

        buffer_sizes = (input_buffer_size, output_buffer_size, scratch_buffer_size)
        return subbuffer_layout, buffer_sizes, slice_info

    def set_up_artifacts(self):
        """Resolve the dispatch policy and build its compile artifacts."""
        self.subbuffer_layout, self.buffer_sizes, self.slice_info = (
            self.calculate_buffer_layout()
        )
        self._dispatch = self._dispatch.resolve(aie_utils.get_current_device())
        self._dispatch.set_up_artifacts(self)

    def compile(self, dry_run: bool = False):
        """Build the artifacts and the image, ahead of time.

        The base class builds the artifact graph (kernel objects and the
        like); the image itself, the fused ELF or the chained xclbins, was
        only linked on the way to a callable, so ``compile()`` on a host
        without a runtime stopped short of the thing worth handing on.
        ``link()`` is idempotent and ``get_callable()`` still goes through it.
        """
        super().compile(dry_run=dry_run)
        if not dry_run:
            self.link()
        return self

    def link(self):
        """Build this sequence's image for its dispatch; sets ``self.image``."""
        if not hasattr(self, "subbuffer_layout"):
            AIEOperatorBase.compile(self)
        self.image = self._dispatch.link(self)
        return self.image

    def get_arg_spec(self):
        raise NotImplementedError(
            "OperatorSequence does not expose a unified arg spec; "
            "use get_layout_for_buffer() to inspect individual buffer layouts"
        )

    def get_callable(self):
        """Return the runtime callable for the resolved dispatch policy.

        Compiles first if that has not happened yet, so a caller can dispatch
        a sequence without compiling it explicitly. Calling ``compile()``
        beforehand remains the ahead-of-time path and does the same work --
        the only difference is when. ``compile()`` skips artifacts already on
        disk, so arriving here twice costs nothing the second time.
        """
        if not hasattr(self, "subbuffer_layout"):
            self.compile()
        return self._dispatch.make_callable(self)

    def get_layout_for_buffer(self, buffer_name):
        """Return the (buffer_type, offset, length) layout for a named buffer.

        Sliced buffers are resolved recursively to their parent's absolute
        offset.

        Args:
            buffer_name: Name of the buffer, optionally with slice notation.

        Returns:
            Tuple of (buf_type, offset_bytes, length_bytes).
        """
        if buffer_name in self.slice_info:
            buf_name, start, end = self.slice_info[buffer_name]
            buf_type, parent_start, parent_end = self.get_layout_for_buffer(buf_name)
            return buf_type, parent_start + start, parent_start + end

        buf_type, offset, length = self.subbuffer_layout[buffer_name]
        return buf_type, offset, length


# ##########################################################################
# Module helpers
# ##########################################################################


BF16 = np.dtype(ml_dtypes.bfloat16)


def _n_elements(nbytes):
    return max(nbytes, BF16.itemsize) // BF16.itemsize


# ##########################################################################
# Runtime callables
# ##########################################################################


class SequenceCallable:
    """Base for the runtime callables of an ``OperatorSequence``.

    Subclasses provide a buffer model (``_allocate_buffers`` / ``get_buffer``)
    and a step-execution primitive (``_run``). Shared here: step/arg zipping,
    input and output syncing, and timing. Calling the object runs the whole
    sequence once.
    """

    def __init__(self, op):
        self.op = op
        self.last_elapsed = 0.0
        self._buffer_cache = {}
        self._allocate_buffers()

    def _allocate_buffers(self):
        raise NotImplementedError

    def get_buffer(self, buffer_name):
        raise NotImplementedError

    def _iter_steps(self):
        """Yield ``(op, in_names, in_specs, out_name, out_spec)`` per runlist step."""
        for step_op, *buf_names in self.op.runlist:
            specs = step_op.get_arg_spec()
            if len(specs) != len(buf_names):
                raise ValueError(
                    f"Operator {step_op!r} arg-spec count {len(specs)} does not "
                    f"match runlist buffer count {len(buf_names)}"
                )
            *in_names, out_name = buf_names
            *in_specs, out_spec = specs
            yield step_op, in_names, in_specs, out_name, out_spec

    def _sync_inputs(self):
        pass

    def _sync_outputs(self):
        pass

    def _run(self):
        raise NotImplementedError

    def __call__(self):
        self._sync_inputs()
        t0 = time.perf_counter()
        self._run()
        self.last_elapsed = time.perf_counter() - t0
        self._sync_outputs()


class _ArenaCallable(SequenceCallable):
    """Buffer model of a fused sequence: three consolidated input/output/
    scratch buffers addressed by offset. ``get_buffer`` returns a sub-view
    into whichever holds the named argument.
    """

    def _allocate_buffers(self):
        in_sz, out_sz, scratch_sz = self.op.buffer_sizes
        self.input_buffer = XRTTensor((_n_elements(in_sz),), dtype=ml_dtypes.bfloat16)
        self.output_buffer = XRTTensor((_n_elements(out_sz),), dtype=ml_dtypes.bfloat16)
        self.scratch_buffer = XRTTensor(
            (_n_elements(scratch_sz),), dtype=ml_dtypes.bfloat16
        )
        self.trace_buffer = None

    def get_buffer(self, buffer_name):
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]
        buf_type, offset, length = self.op.get_layout_for_buffer(buffer_name)
        parent = {
            "input": self.input_buffer,
            "output": self.output_buffer,
            "scratch": self.scratch_buffer,
        }[buf_type]
        sub = parent.subview(offset, (length // BF16.itemsize,), ml_dtypes.bfloat16)
        self._buffer_cache[buffer_name] = sub
        return sub

    def _sync_inputs(self):
        # Sub-views handed out by get_buffer() share the parent's coherence map, so
        # a write through one (e.g. torch_view()) marks its byte range host-dirty
        # there too, and `to("npu")` here syncs every dirty range in one pass.
        self.input_buffer.to("npu")

    def _sync_outputs(self):
        # _run just rewrote the output arena on the device, so the device holds the
        # authoritative copy. Force the device->host sync: assert device residency first
        # so `to("cpu")` fires even if a prior read of get_buffer(...) marked some
        # range "cpu" (otherwise a looped dispatch would read stale output).
        self.output_buffer.device = "npu"
        self.output_buffer.to("cpu")
        if self.trace_buffer is not None:
            self.trace_buffer.device = "npu"
            self.trace_buffer.to("cpu")


class SequenceChunkedCallable(_ArenaCallable):
    """Chunked dispatch: the arenas of a fused sequence, run through one
    xclbin kernel per chunk, in order."""

    def __init__(self, op, dispatch):
        _require_xrt()
        self._dispatch = dispatch
        super().__init__(op)
        self.kernels = [
            NPUKernel(
                xclbin_path=str(dispatch.combined_xclbin_path),
                kernel_name=label,
                insts_path=str(insts_path),
            )
            for label, _, insts_path, _ in dispatch.chunks
        ]

    def _run(self):
        args = [self.input_buffer, self.output_buffer, self.scratch_buffer]
        for kernel in self.kernels:
            kernel(*args)


class SequenceFullELFCallable(_ArenaCallable):
    """Single-ELF dispatch (NPU2): every operator shares three consolidated
    input/output/scratch buffers addressed by offset. ``get_buffer`` returns a
    sub-view into whichever consolidated buffer holds the named argument.
    """

    def __init__(self, op, device_name="main", sequence_name="sequence"):
        _require_xrt()
        self.device_name = device_name
        self.sequence_name = sequence_name

        xrt_elf = pyxrt.elf(str(full_elf_path(op)))
        xrt_context = pyxrt.hw_context(aie_utils.DefaultNPURuntime._device, xrt_elf)
        self.xrt_kernel = pyxrt.ext.kernel(
            xrt_context, f"{self.device_name}:{self.sequence_name}"
        )

        super().__init__(op)

        # Persistent run handle: reused across dispatches so that the
        # ctrl-scratchpad backing buffer (and any ParameterScratchpad state
        # built on top of it) stays valid across calls.
        self.run_handle = pyxrt.run(self.xrt_kernel)
        self.run_handle.set_arg(0, self.input_buffer.buffer_object())
        self.run_handle.set_arg(1, self.output_buffer.buffer_object())
        self.run_handle.set_arg(2, self.scratch_buffer.buffer_object())
        if self.trace_buffer is not None:
            self.run_handle.set_arg(3, self.trace_buffer.buffer_object())

        self._params = None

    @property
    def params(self):
        """Lazy ParameterScratchpad bound to this ELF's ctrl scratchpad BO.

        The ``params.txt`` describing the runtime parameters is requested from
        aiecc via ``--get-scratchpad-parameters``; it is a graph output, so it
        lands in aiecc's ``--output-dir``, which compile_mlir_module() points at
        the work dir (see ``_aiecc_work_dir``) for the fused MLIR source.
        Returns ``None`` if the sequence declared no runtime parameters: the
        file is still written, but holds a count of zero and there is no ctrl
        scratchpad buffer object to bind to.
        """
        if self._params is not None:
            return self._params
        from .jit_compile import fused_work_dir

        params_path = fused_work_dir(full_elf_path(self.op)) / "params.txt"
        if not params_path.exists():
            return None
        if params_path.read_text().split("\n", 1)[0].strip() == "0":
            return None
        from aie.utils.hostruntime.xrtruntime.parameter_scratchpad import (
            ParameterScratchpad,
        )

        self._params = ParameterScratchpad(self.run_handle, str(params_path))
        return self._params

    def _allocate_buffers(self):
        super()._allocate_buffers()
        # Trace lowering appends one buffer covering every configured design, after
        # the consolidated three. Its size depends on how many channels and
        # sub-designs claim a share, so read it from the lowered module.
        if self.op.trace_size:
            total = comp.trace_buffer_size(self.lowered_mlir_text())
            if total:
                self.trace_buffer = XRTTensor((total,), dtype=np.int8)

    def lowered_mlir_text(self) -> str:
        """aiecc's post-lowering module, which carries the trace buffer layout."""
        from .jit_compile import fused_work_dir

        path = fused_work_dir(full_elf_path(self.op)) / "input_with_addresses.mlir"
        return path.read_text()

    def _run(self):
        self.run_handle.start()
        ret_code = self.run_handle.wait()
        if ret_code != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel execution failed with return code {ret_code}")


class _PerBufferCallable(SequenceCallable):
    """Callable whose buffers are allocated one per name, with slice views into
    their parent. Inputs sync to the device before the run, all non-input
    buffers back to the host afterwards.
    """

    def _make_buffer(self, n_elements):
        raise NotImplementedError

    def _allocate_buffers(self):
        self._buffers = {}
        for name, (_, _, length) in self.op.subbuffer_layout.items():
            self._buffers[name] = self._make_buffer(_n_elements(length))

    def _resolve_buffer(self, buf_name):
        if buf_name in self._buffers:
            return self._buffers[buf_name]
        if buf_name in self.op.slice_info:
            base_name, start_bytes, end_bytes = self.op.slice_info[buf_name]
            size_bytes = end_bytes - start_bytes
            sub = self._buffers[base_name].subview(
                start_bytes, (size_bytes // BF16.itemsize,), BF16
            )
            self._buffers[buf_name] = sub
            return sub
        raise ValueError(f"Unknown buffer '{buf_name}' in fused runlist")

    def get_buffer(self, buffer_name):
        if buffer_name not in self._buffer_cache:
            self._buffer_cache[buffer_name] = self._resolve_buffer(buffer_name)
        return self._buffer_cache[buffer_name]

    def _sync_inputs(self):
        for name in self.op.input_args:
            self._buffers[name].to("npu")

    def _sync_outputs(self):
        for name in self.op.subbuffer_layout:
            if name not in self.op.input_args:
                self._buffers[name].to("cpu")


class SequenceXclbinCallable(_PerBufferCallable):
    """Executes each runlist step as its own xclbin dispatch. Buffers shared by
    name give zero-copy handoff between consecutive operators.

    The compiled per-operator xclbin/insts maps live on the ``SeparateDispatch``
    policy passed in as ``dispatch``.
    """

    def __init__(self, op, dispatch):
        _require_xrt()
        self._dispatch = dispatch
        super().__init__(op)

    def _make_buffer(self, n_elements):
        return XRTTensor((n_elements,), dtype=ml_dtypes.bfloat16)

    def _allocate_buffers(self):
        super()._allocate_buffers()
        dispatch = self._dispatch
        combined_xclbin_path = dispatch.combined_xclbin_path
        self._op_callable_map = {}  # id(op) -> NPUKernel
        # Per-call scalars of dispatch-time kernels, by symbol; a graph sets
        # them before each run (CompiledGraph._write_values).
        self.dispatch_values = {}
        for op_id, xclbin_path in dispatch.op_xclbin_path_map.items():
            stream = dispatch.op_insts_path_map[op_id]
            if isinstance(stream, DispatchStream):
                self._op_callable_map[op_id] = NPUKernel(
                    xclbin_path=str(combined_xclbin_path),
                    kernel_name=dispatch.op_kernel_name_map[op_id],
                    dispatch_params=list(stream.params),
                    dispatch_lib_path=str(stream.lib_path),
                )
            else:
                self._op_callable_map[op_id] = NPUKernel(
                    xclbin_path=str(combined_xclbin_path),
                    kernel_name=dispatch.op_kernel_name_map[op_id],
                    insts_path=str(stream),
                )
        self._execution_plan = [
            (
                self._op_callable_map[id(step_op)],
                [self._resolve_buffer(name) for name in buf_names],
            )
            for step_op, *buf_names in self.op.runlist
        ]

    def _run(self):
        # Walk the execution plan alongside the resolved runlist steps; the
        # per-step behaviour is delegated to _run_step so that compare mode can
        # reuse this loop verbatim.
        for step_idx, ((kernel, args), step) in enumerate(
            zip(self._execution_plan, self._iter_steps())
        ):
            self._run_step(step_idx, kernel, args, step)

    def _run_step(self, step_idx, kernel, args, step):
        scalars = {name: self.dispatch_values[name] for name in kernel.dispatch_params}
        kernel(*args, **scalars)


def _reshape_for_spec(flat_tensor, spec):
    """Slice a flat host buffer to ``spec``'s element count and reshape (a view)."""
    n = int(np.prod(spec.shape)) if spec.shape else 1
    return flat_tensor[:n].reshape(spec.shape)


class SequenceReferenceCallable(_PerBufferCallable):
    """Pure-CPU evaluation via each operator's ``reference()``; no NPU dispatch.
    Device syncs are no-ops on the CPU buffers.
    """

    def _make_buffer(self, n_elements):
        return CPUOnlyTensor((n_elements,), dtype=BF16)

    def _sync_inputs(self):
        # CPU-only inputs must stay CPU-resident, including lazily created subviews.
        pass

    def _run(self):
        torch = _torch()
        for step_op, in_names, in_specs, out_name, out_spec in self._iter_steps():
            inputs = [
                _reshape_for_spec(self._resolve_buffer(n).torch_view(), s).clone()
                for n, s in zip(in_names, in_specs)
            ]
            out = step_op.reference(*inputs)
            out_flat = self._resolve_buffer(out_name).torch_view()
            n_out = int(np.prod(out_spec.shape)) if out_spec.shape else 1
            out_flat[:n_out].copy_(out.reshape(-1).to(torch.bfloat16))


class SequenceCompareCallable(SequenceXclbinCallable):
    """Runs the xclbin pipeline and, after each step, re-runs the operator's
    reference on the same NPU-produced inputs, logging per-step deviation. The
    NPU output propagates on both sides, so each comparison isolates a single
    operator (no error accumulation).
    """

    def __init__(self, op, dispatch):
        super().__init__(op, dispatch)
        self.rel_tol = dispatch.rel_tol
        self.abs_tol = dispatch.abs_tol
        self.raise_on_mismatch = dispatch.raise_on_mismatch
        self.last_step_stats = []

    def _read_to_cpu(self, name, spec):
        buf = self._resolve_buffer(name)
        buf.to("cpu")
        n = int(np.prod(spec.shape)) if spec.shape else 1
        return buf.torch_view()[:n].clone().reshape(spec.shape)

    def _run(self):
        # Reset per-invocation stats, then reuse SequenceXclbinCallable._run's
        # execution-plan loop; only the per-step behaviour (_run_step) differs.
        self.last_step_stats = []
        super()._run()

    def _run_step(self, step_idx, kernel, args, step):
        step_op, in_names, in_specs, out_name, out_spec = step

        cpu_inputs = [
            self._read_to_cpu(name, spec) for name, spec in zip(in_names, in_specs)
        ]

        kernel(*args)

        torch = _torch()
        npu_out = self._read_to_cpu(out_name, out_spec).to(torch.float32)
        ref_out = step_op.reference(*cpu_inputs)

        stats = {
            "step": step_idx,
            "op": type(step_op).__name__,
            "op_name": getattr(step_op, "name", type(step_op).__name__),
            "inputs": list(in_names),
            "output": out_name,
        }

        ref_flat = ref_out.reshape(out_spec.shape).to(torch.float32)
        diff = (npu_out - ref_flat).abs()
        ref_mag = ref_flat.abs()
        max_abs = float(diff.max())
        ref_max = float(ref_mag.max())
        rel = float((diff / (ref_mag + 1e-6)).max())
        mean_abs = float(diff.mean())
        stats.update(
            skipped=False,
            max_abs=max_abs,
            mean_abs=mean_abs,
            max_rel=rel,
            ref_max=ref_max,
        )
        fail = (max_abs > self.abs_tol) and (rel > self.rel_tol)
        stats["mismatch"] = fail
        level = logging.ERROR if fail else logging.INFO
        logger.log(
            level,
            "[compare step %d] %s -> %s: max_abs=%.4g mean_abs=%.4g max_rel=%.4g ref_max=%.4g%s",
            step_idx,
            stats["op"],
            out_name,
            max_abs,
            mean_abs,
            rel,
            ref_max,
            "  MISMATCH" if fail else "",
        )
        if fail and self.raise_on_mismatch:
            raise RuntimeError(
                f"[compare step {step_idx}] {stats['op']} (name={stats['op_name']}) "
                f"-> {out_name}: NPU output deviates from reference "
                f"(max_abs={max_abs:.4g}, max_rel={rel:.4g}, "
                f"ref_max={ref_max:.4g}; inputs={list(in_names)}; "
                f"tolerances abs_tol={self.abs_tol}, rel_tol={self.rel_tol})"
            )
        self.last_step_stats.append(stats)
