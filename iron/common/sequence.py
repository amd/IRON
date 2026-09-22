# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import hashlib
import inspect
import logging
import time
import numpy as np
import ml_dtypes
from . import fusion
from .context import AIEContext
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
        from .jit_compile import fused_design

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
        from .jit_compile import dispatch_stream, xclbin_design

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


# ##########################################################################
# Compileable: operator sequence
# ##########################################################################


class OperatorSequence:
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
        if args:
            raise TypeError(
                f"OperatorSequence takes no positional extras, got {args!r}"
            )
        self.context = kwargs.pop("context", None) or AIEContext.default()
        if kwargs:
            raise TypeError(f"unexpected keyword arguments {sorted(kwargs)}")
        self.runlist = runlist
        # Sharing changes which designs are built, so it belongs in the label
        # the chain's kernel instances are named from.
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
        self.mode = mode  # None until the device is known (prepare)
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
                if _signature(op) != _signature(shared):
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
            for buf, b in zip(bufs, op.buffers):
                sizes.setdefault(buf, b.nbytes)
                if b.direction in ("in", "inout"):
                    reads.append(buf)
                if b.direction in ("out", "inout"):
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
        args = {}  # base_buffer_name -> the declared buffer
        sliced_buffers = {}  # full_buffer_name (with slice) -> (base_name, start, end, buffer)

        for op, *bufs in self.runlist:
            declared = op.buffers
            if len(declared) != len(bufs):
                raise ValueError(
                    f"Number of buffers ({len(bufs)}) must match the operator's "
                    f"declared buffers ({len(declared)}) for operator {op!r}"
                )
            for i, buf_name in enumerate(bufs):
                args_spec = declared[i]

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
                    return args[arg].nbytes
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

    def prepare(self):
        """Lay the buffers out and settle the mode, before anything is built."""
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

    def compile(self):
        """Build the image ahead of time, and record what it consists of.

        ``link()`` is idempotent and ``get_callable()`` still goes through
        it, so this is the ahead-of-time path: a host with the toolchain and
        no runtime compiles and hands the image on.
        """
        self.prepare()
        self.link()
        if self.context.record == "disk" and self.artifacts is not None:
            self.artifacts.dump()
        return self

    def link(self):
        """Build this sequence's image, once; sets ``self.image`` (``None`` for
        the reference mode) and :attr:`artifacts`."""
        if not hasattr(self, "subbuffer_layout"):
            self.prepare()
        self.image = self._image.link(self) if self._image is not None else None
        self._artifacts = self._record()
        return self.image

    @property
    def elf_path(self):
        """The fused ELF, when that is this sequence's image."""
        return self.image if isinstance(self._image, FusedImage) else None

    @property
    def artifacts(self):
        """The record of what :meth:`link` produced (``None`` in reference mode)."""
        return getattr(self, "_artifacts", None)

    def _record(self):
        """What this image consists of: its designs, its steps, its buffers."""
        from .artifacts import Artifacts, Design, Step

        if self._image is None:
            return None
        designs, design_of = self.unique_designs()
        operators = list(self.unique_operators())
        labels = [f"op{i}_{type(op).__name__}" for i, op in enumerate(designs)]
        sharing = [
            tuple(op.name for op in operators if design_of[id(op)] == i)
            for i in range(len(designs))
        ]
        if isinstance(self._image, FusedImage):
            entry = self._image.design.get_cache_entry()
            records = tuple(
                Design(name=labels[i], operators=sharing[i])
                for i in range(len(designs))
            )
            kind, image, insts = "elf", entry.elf, None
        else:
            chain = self._image
            entry = None
            records = []
            for i, op in enumerate(designs):
                design = chain.op_design_map[id(op)]
                own = design.get_cache_entry()
                entry = entry or own
                records.append(
                    Design(
                        name=chain.op_kernel_name_map[id(op)],
                        operators=sharing[i],
                        entry=own,
                        image=own.xclbin,
                        insts=chain.op_insts_path_map[id(op)],
                    )
                )
            records = tuple(records)
            kind, image, insts = "xclbin", chain.combined_xclbin_path, None
        by_design = {id(op): labels[design_of[id(op)]] for op in operators}
        if kind == "xclbin":
            by_design = {id(op): chain.op_kernel_name_map[id(op)] for op in operators}
        steps = tuple(
            Step(i, op.name, by_design[id(op)], tuple(names))
            for i, (op, *names) in enumerate(self.runlist)
        )
        return Artifacts(
            kind=kind,
            image=image,
            insts=insts,
            entry=entry,
            designs=records,
            steps=steps,
            buffers=dict(self.subbuffer_layout),
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


def _signature(op):
    """The runtime arguments an operator takes: direction, shape and dtype each."""
    return [(b.direction, tuple(b.shape), np.dtype(b.dtype)) for b in op.buffers]


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
        """Yield ``(op, in_names, in_buffers, out_name, out_buffer)`` per runlist step."""
        for step_op, *buf_names in self.op.runlist:
            specs = step_op.buffers
            if len(specs) != len(buf_names):
                raise ValueError(
                    f"Operator {step_op!r} declares {len(specs)} buffers but the "
                    f"runlist names {len(buf_names)}"
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

        xrt_elf = pyxrt.elf(str(seq.image))
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

        The ``params.txt`` describing the runtime parameters is requested
        from aiecc via ``--get-scratchpad-parameters`` and lands in the
        build's cache entry, which :attr:`Artifacts.params` names. Returns
        ``None`` if the sequence declared no runtime parameters: the file
        still exists, but holds a count of zero and there is no ctrl
        scratchpad buffer object to bind to.
        """
        if self._params is not None:
            return self._params
        params_path = self.op.artifacts.params
        if params_path is None:
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
            total = fusion.trace_buffer_size(self.lowered_mlir_text())
            if total:
                self.trace_buffer = XRTTensor((total,), dtype=np.int8)

    def lowered_mlir_text(self) -> str:
        """aiecc's post-lowering module, which carries the trace buffer layout."""
        return self.op.artifacts.lowered_mlir.read_text()

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
