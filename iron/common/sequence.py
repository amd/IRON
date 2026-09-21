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
from .base import AIEOperatorBase
from .declare import Operator
from .jit_compile import DispatchStream
import aie.utils as aie_utils
from aie.iron.device import NPU2
from aie.utils.hostruntime.tensor_class import CPUOnlyTensor
from aie.utils.npukernel import NPUKernel

try:
    import pyxrt
    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
except ImportError:
    # Host stacks without XRT (e.g. the HRX/amdxdna runtime) have no pyxrt. The
    # on-device callables below are XRT-native (pyxrt.elf / hw_context / run, plus
    # XRTTensor views), so they cannot run there; _require_xrt() makes that explicit
    # at construction. The reference mode and the whole compile path do not care,
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
            "this OperatorSequence mode needs the XRT host runtime (pyxrt), which is "
            "not installed. Use the reference mode, or run a single operator, which "
            "dispatches through aie.utils.DefaultNPURuntime and works on any backend."
        )


# ##########################################################################
# Images: what a sequence builds, per mode
# ##########################################################################


def _trace_tag(seq):
    """Tracing adds a runtime-sequence argument, so a traced build cannot reuse an
    untraced one's ELF. Empty when untraced."""
    return f"_traced{seq.trace_size}" if seq.trace_size else ""


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
        design_names.append(op_name)
        operator_generators[op_name] = generator

    for op, *bufs in seq.runlist:
        comp_runlist.append((design_names[design_of[id(op)]], *bufs))

    return comp.fuse_mlir(
        operator_generators,
        comp_runlist,
        seq.subbuffer_layout,
        seq.buffer_sizes,
        seq.slice_info,
    )


class FusedImage:
    """The full ELF: every design fused into one module (NPU2 only)."""

    def link(self, seq):
        """Link the ELF once (idempotent); returns its path.

        Goes through CompilableDesign, which keys its cache on content, locks
        across processes and validates depfiles.
        """
        from .jit_compile import compile_fused_elf

        if not isinstance(aie_utils.get_current_device(), NPU2):
            raise RuntimeError(
                "dispatch='fused' requires NPU2; NPU1 has no full-ELF dispatch"
            )
        if getattr(seq, "elf_path", None) is None:
            seq.elf_path = compile_fused_elf(
                lambda: build_fused_mlir(seq),
                Path(seq.context.build_dir) / f"{seq.name}{_trace_tag(seq)}.elf",
                extra_flags=seq.extra_flags,
                trace_size=seq.trace_size,
            )
        return seq.elf_path


class XclbinChain:
    """One xclbin and instruction stream per design, each linked onto the
    previous (``--xclbin-input``); the last link carries every kernel. Holds
    the per-operator paths the xclbin callable dispatches with."""

    def __init__(self):
        self.combined_xclbin_path = None
        self.op_xclbin_path_map = {}  # id(op) -> xclbin path
        self.op_insts_path_map = {}  # id(op) -> insts path, or a DispatchStream
        self.op_kernel_name_map = {}  # id(op) -> kernel name

    def link(self, seq):
        """Build the chain once (idempotent); returns the last link."""
        if self.combined_xclbin_path is not None:
            return self.combined_xclbin_path
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
        return self.combined_xclbin_path


# ##########################################################################
# Compileable: operator sequence
# ##########################################################################


class OperatorSequence(AIEOperatorBase):
    """Operator that concatenates a runlist of operators into a
    single dispatch.

    Args:
        dispatch: The mode. ``"auto"`` (default) is ``"fused"`` on NPU2 and
            ``"separate"`` elsewhere. ``"fused"`` builds one full ELF (NPU2
            only); ``"separate"`` one xclbin per design, chained, dispatched
            one step at a time. ``"reference"`` builds nothing and runs each
            operator's CPU ``reference()``; ``"compare"`` runs the chain and
            after each step re-runs the reference on the NPU-produced inputs
            (``SequenceCompareCallable`` holds the tolerances).
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
        mode = self._coerce_dispatch(dispatch)
        if not all(
            isinstance(op, Operator) and all(isinstance(buf, str) for buf in bufs)
            for op, *bufs in runlist
        ):
            raise TypeError(
                "runlist entries must be (Operator, *str) tuples; "
                "each operator must be an Operator and each buffer name must be a str"
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
        self.mode = mode  # None until the device is known (set_up_artifacts)
        self._image = None  # the mode's image builder, once resolved

    @staticmethod
    def _coerce_dispatch(dispatch):
        if dispatch == "auto" or dispatch is None:
            return None  # the platform default, resolved when the device is known
        if isinstance(dispatch, str) and dispatch in _MODES:
            return dispatch
        raise TypeError(
            f"dispatch {dispatch!r} is not one of {sorted(_MODES)} or 'auto'"
        )

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
        """Lay the buffers out and settle the mode; nothing else is an artifact
        (each design's kernels are compiled with its image)."""
        self.subbuffer_layout, self.buffer_sizes, self.slice_info = (
            self.calculate_buffer_layout()
        )
        if self.mode is None:
            # The platform default for a hand-written sequence; a graph goes
            # through packaging.plan, which also weighs its values and boundaries.
            npu2 = isinstance(aie_utils.get_current_device(), NPU2)
            self.mode = "fused" if npu2 else "separate"
        image, _ = _MODES[self.mode]
        self._image = image() if image is not None else None

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
        """Build this sequence's image, once; sets ``self.image`` (``None`` for
        the reference mode)."""
        if not hasattr(self, "subbuffer_layout"):
            AIEOperatorBase.compile(self)
        self.image = self._image.link(self) if self._image is not None else None
        return self.image

    def get_arg_spec(self):
        raise NotImplementedError(
            "OperatorSequence does not expose a unified arg spec; "
            "use get_layout_for_buffer() to inspect individual buffer layouts"
        )

    def get_callable(self):
        """The runtime callable of this sequence's mode, compiling first if
        that has not happened (``compile()`` beforehand is the ahead-of-time
        path; the work is the same, only when it happens differs)."""
        if not hasattr(self, "subbuffer_layout"):
            self.compile()
        self.link()
        return _MODES[self.mode][1](self)

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
    """Runs an ``OperatorSequence`` once per call.

    Buffers are one per name, a slice a view into its parent; inputs sync to
    the device before the run and everything else back to the host after.
    Subclasses give the buffer (``_make_buffer``) and the run (``_run``); the
    full-ELF callable replaces the buffer model with its three arenas.
    """

    def __init__(self, seq):
        self.op = seq
        self.last_elapsed = 0.0
        self._buffer_cache = {}
        self._allocate_buffers()

    def _make_buffer(self, n_elements):
        return XRTTensor((n_elements,), dtype=ml_dtypes.bfloat16)

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
        for name in self.op.input_args:
            self._buffers[name].to("npu")

    def _sync_outputs(self):
        for name in self.op.subbuffer_layout:
            if name not in self.op.input_args:
                self._buffers[name].to("cpu")

    def _run(self):
        raise NotImplementedError

    def __call__(self):
        self._sync_inputs()
        t0 = time.perf_counter()
        self._run()
        self.last_elapsed = time.perf_counter() - t0
        self._sync_outputs()


class SequenceFullELFCallable(SequenceCallable):
    """The full ELF (NPU2): every operator shares three consolidated
    input/output/scratch buffers addressed by offset. ``get_buffer`` returns a
    sub-view into whichever consolidated buffer holds the named argument.
    """

    def __init__(self, seq, device_name="main", sequence_name="sequence"):
        _require_xrt()
        self.device_name = device_name
        self.sequence_name = sequence_name

        xrt_elf = pyxrt.elf(str(seq.elf_path))
        xrt_context = pyxrt.hw_context(aie_utils.DefaultNPURuntime._device, xrt_elf)
        self.xrt_kernel = pyxrt.ext.kernel(
            xrt_context, f"{self.device_name}:{self.sequence_name}"
        )

        super().__init__(seq)

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

        params_path = fused_work_dir(self.op.elf_path) / "params.txt"
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
        in_sz, out_sz, scratch_sz = self.op.buffer_sizes
        self.input_buffer = XRTTensor((_n_elements(in_sz),), dtype=ml_dtypes.bfloat16)
        self.output_buffer = XRTTensor((_n_elements(out_sz),), dtype=ml_dtypes.bfloat16)
        self.scratch_buffer = XRTTensor(
            (_n_elements(scratch_sz),), dtype=ml_dtypes.bfloat16
        )
        # Trace lowering appends one buffer covering every configured design, after
        # the consolidated three. Its size depends on how many channels and
        # sub-designs claim a share, so read it from the lowered module.
        self.trace_buffer = None
        if self.op.trace_size:
            total = comp.trace_buffer_size(self.lowered_mlir_text())
            if total:
                self.trace_buffer = XRTTensor((total,), dtype=np.int8)

    def lowered_mlir_text(self) -> str:
        """aiecc's post-lowering module, which carries the trace buffer layout."""
        from .jit_compile import fused_work_dir

        path = fused_work_dir(self.op.elf_path) / "input_with_addresses.mlir"
        return path.read_text()

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

    def _run(self):
        self.run_handle.start()
        ret_code = self.run_handle.wait()
        if ret_code != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel execution failed with return code {ret_code}")


class SequenceXclbinCallable(SequenceCallable):
    """Executes each runlist step as its own xclbin dispatch. Buffers shared by
    name give zero-copy handoff between consecutive operators. The chain's
    per-operator paths are on ``seq._image`` (an :class:`XclbinChain`).
    """

    def __init__(self, seq):
        _require_xrt()
        super().__init__(seq)

    def _allocate_buffers(self):
        super()._allocate_buffers()
        chain = self.op._image
        self._op_callable_map = {}  # id(op) -> NPUKernel
        # Per-call scalars of dispatch-time kernels, by symbol; a graph sets
        # them before each run (CompiledGraph._write_values).
        self.dispatch_values = {}
        for op_id, xclbin_path in chain.op_xclbin_path_map.items():
            stream = chain.op_insts_path_map[op_id]
            if isinstance(stream, DispatchStream):
                self._op_callable_map[op_id] = NPUKernel(
                    xclbin_path=str(chain.combined_xclbin_path),
                    kernel_name=chain.op_kernel_name_map[op_id],
                    dispatch_params=list(stream.params),
                    dispatch_lib_path=str(stream.lib_path),
                )
            else:
                self._op_callable_map[op_id] = NPUKernel(
                    xclbin_path=str(chain.combined_xclbin_path),
                    kernel_name=chain.op_kernel_name_map[op_id],
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


class SequenceReferenceCallable(SequenceCallable):
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
    """Runs the xclbin chain and, after each step, re-runs the operator's
    reference on the same NPU-produced inputs, logging per-step deviation. The
    NPU output propagates on both sides, so each comparison isolates a single
    operator (no error accumulation). A step is a mismatch when it exceeds
    both tolerances; ``raise_on_mismatch`` turns the first one into an error.
    """

    def __init__(self, seq, rel_tol=0.05, abs_tol=1e-2, raise_on_mismatch=True):
        super().__init__(seq)
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol
        self.raise_on_mismatch = raise_on_mismatch
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


# The modes a sequence can be built in: the image (None builds nothing) and
# the callable that runs it.
_MODES = {
    "fused": (FusedImage, SequenceFullELFCallable),
    "separate": (XclbinChain, SequenceXclbinCallable),
    "reference": (None, SequenceReferenceCallable),
    "compare": (XclbinChain, SequenceCompareCallable),
}
