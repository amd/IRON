# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import hashlib
import logging
import time
import numpy as np
import ml_dtypes
import pyxrt
import ctypes
import torch
from . import compilation as comp
from .base import AIEOperatorBase, MLIROperator
from .utils import XRTSubBuffer
import aie.utils as aie_utils
from aie.iron.device import NPU2
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from aie.utils.npukernel import NPUKernel

logger = logging.getLogger(__name__)

# Fused Operator
# ##########################################################################


class OperatorSequence(AIEOperatorBase):
    """Operator that fuses multiple MLIROperators into one.

    Args:
        dispatch: Dispatch strategy for the fused operator.
            ``"auto"`` (default) selects ``"fused"`` on NPU2 and
            ``"separate"`` on NPU1.  ``"fused"`` uses a single-ELF
            dispatch (requires NPU2).  ``"separate"`` compiles each
            sub-operator to its own xclbin and invokes them sequentially.
            ``"reference"`` runs only the per-operator CPU reference
            implementations (no NPU compilation/dispatch).  ``"compare"``
            runs the ``"separate"`` xclbin path and, after each NPU step,
            also runs the operator's CPU reference on the NPU-produced
            inputs and logs the deviation.
    """

    DISPATCH_MODES = ("auto", "fused", "separate", "reference", "compare")

    def __init__(
        self,
        name,
        runlist,
        input_args,
        output_args,
        buffer_sizes=None,
        dispatch="auto",
        *args,
        **kwargs,
    ):
        if dispatch not in self.DISPATCH_MODES:
            raise ValueError(
                f"dispatch must be one of {self.DISPATCH_MODES!r}, got {dispatch!r}"
            )
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
        self.name = name
        self.input_args = input_args
        self.output_args = output_args
        self.explicit_buffer_sizes = (
            buffer_sizes or {}
        )  # Optional dict: buffer_name -> size_in_bytes
        self._dispatch = dispatch

    def _unique_operators(self):
        """Operators in runlist order, de-duplicated by identity."""
        seen = {}
        for op, *_ in self.runlist:
            seen.setdefault(id(op), op)
        return list(seen.values())

    def get_kernel_artifacts(self):
        """Kernel artifacts from all child operators, prefixed per operator index."""
        kernel_artifacts = []
        for idx, op in enumerate(self._unique_operators()):
            objs = op.get_kernel_artifacts()
            for obj in objs:
                obj.filename = f"op{idx}_{obj.filename}"
                obj.prefix_symbols = f"op{idx}_"
            kernel_artifacts.extend(objs)
        return kernel_artifacts

    def get_mlir_artifact(self):
        """Build the fused MLIR source artifact.

        The buffer layout attributes (``subbuffer_layout``, ``buffer_sizes``,
        ``slice_info``) must already be set by ``set_up_artifacts()``.
        """
        operator_mlir_map = {}
        comp_runlist = []
        op_names = {}  # id(op) -> op_name

        for idx, op in enumerate(self._unique_operators()):
            mlir_artifact = op.get_mlir_artifact()
            if len(op.get_kernel_artifacts()) > 0:
                mlir_artifact.generator.kwargs["func_prefix"] = f"op{idx}_"
            op_name = f"op{idx}_{op.__class__.__name__}"
            op_names[id(op)] = op_name
            operator_mlir_map[op_name] = mlir_artifact

        for op, *bufs in self.runlist:
            comp_runlist.append((op_names[id(op)], *bufs))

        filename = self.name + "_fused.mlir"
        fused_artifact = comp.SequenceMLIRSource(
            filename,
            operator_mlir_map=operator_mlir_map,
            runlist=comp_runlist,
            subbuffer_layout=self.subbuffer_layout,
            buffer_sizes=self.buffer_sizes,
            slice_info=self.slice_info,
        )

        return fused_artifact

    def _calculate_buffer_layout(self):
        args = {}  # base_buffer_name -> args_spec
        sliced_buffers = (
            {}
        )  # full_buffer_name (with slice) -> (base_name, start, end, args_spec)

        # Collect all buffer specs from operators
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
                    # Regular buffer (no slice)
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
            # Check if it's a base buffer name in explicit_buffer_sizes
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise ValueError(f"Input argument {arg} not found in runlist buffers")
        for arg in self.output_args:
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise ValueError(f"Output argument {arg} not found in runlist buffers")

        # Determine buffer types and create layout
        subbuffer_layout = {}
        slice_info = {}  # full_buffer_name -> (base_name, start, end)

        def add_buffers(buffer_type, args_list):
            offset = 0
            for arg in args_list:
                if arg in self.explicit_buffer_sizes:
                    # Explicit size specified - this is a parent buffer for slices
                    length = self.explicit_buffer_sizes[arg]
                    subbuffer_layout[arg] = (buffer_type, offset, length)
                    offset += length
                elif arg in args:
                    # Regular buffer with inferred size
                    arg_spec = args[arg]
                    length = int(
                        np.prod(arg_spec.shape) * np.dtype(arg_spec.dtype).itemsize
                    )
                    subbuffer_layout[arg] = (buffer_type, offset, length)
                    offset += length
                # Note: sliced buffers are handled separately, not in args_list
            return offset  # == total length

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
        """Resolve the dispatch mode and build the matching compile artifacts."""
        self.subbuffer_layout, self.buffer_sizes, self.slice_info = (
            self._calculate_buffer_layout()
        )

        is_npu2 = isinstance(aie_utils.get_current_device(), NPU2)

        if self._dispatch == "auto":
            self._mode = "fused" if is_npu2 else "separate"
        elif self._dispatch == "fused":
            if not is_npu2:
                raise RuntimeError(
                    "dispatch='fused' requires NPU2; NPU1 has no full-ELF dispatch"
                )
            self._mode = "fused"
        else:
            self._mode = self._dispatch  # "separate", "reference", or "compare"

        if self._mode == "fused":
            self._set_up_full_elf_artifacts()
        elif self._mode in ("separate", "compare"):
            self._set_up_xclbin_artifacts()
        # "reference" compiles nothing.

    def _set_up_full_elf_artifacts(self):
        """Full-ELF path (NPU2): fuse MLIR into a single ELF."""
        operator_name = self.name
        mlir_artifact = self.get_mlir_artifact()
        kernel_objects = self.get_kernel_artifacts()
        full_elf_artifact = comp.FullElfArtifact(
            f"{operator_name}.elf",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact] + kernel_objects,
        )
        self.add_artifacts([full_elf_artifact])

    def _set_up_xclbin_artifacts(self):
        """Chained-xclbin path: one xclbin+insts per unique operator, linked
        via ``--xclbin-input``."""
        # Short hash keeps kernel names under xclbinutil's 64-char "name:name" limit.
        name_hash = hashlib.sha1(self.name.encode()).hexdigest()[:6]

        artifacts = []
        prev_xclbin = None
        self._op_xclbin_map = {}  # id(op) -> xclbin artifact
        self._op_insts_map = {}  # id(op) -> insts artifact
        self._op_kernel_name_map = {}  # id(op) -> kernel_name

        for idx, op in enumerate(self._unique_operators()):
            op_label = f"f{name_hash}_op{idx}"
            kernel_id = f"0x{0x901 + idx:x}"

            xclbin, insts = op.get_artifacts(prefix=f"{op_label}_")
            # Copy so we don't mutate the (possibly aliased) shared flags list.
            xclbin.extra_flags = list(xclbin.extra_flags) + [
                f"--xclbin-instance-name={op_label}",
                f"--xclbin-kernel-id={kernel_id}",
            ]
            xclbin.kernel_name = op_label

            if prev_xclbin is not None:
                xclbin.xclbin_input = prev_xclbin
                xclbin.dependencies.add(prev_xclbin)

            artifacts.append(insts)
            self._op_xclbin_map[id(op)] = xclbin
            self._op_insts_map[id(op)] = insts
            self._op_kernel_name_map[id(op)] = op_label
            prev_xclbin = xclbin

        # The last xclbin in the chain carries all the linked instances.
        artifacts.append(prev_xclbin)
        self.combined_xclbin = prev_xclbin
        self.add_artifacts(artifacts)

    def get_arg_spec(self):
        raise NotImplementedError(
            "OperatorSequence does not expose a unified arg spec; "
            "use get_layout_for_buffer() to inspect individual buffer layouts"
        )

    def get_callable(self):
        """Return the runtime callable for the resolved dispatch mode."""
        if self._mode == "fused":
            return SequenceFullELFCallable(self)
        if self._mode == "reference":
            return SequenceReferenceCallable(self)
        if self._mode == "compare":
            return SequenceCompareCallable(self)
        return SequenceXclbinCallable(self)

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


def load_elf(op):
    assert isinstance(op.artifacts[0], comp.FullElfArtifact)
    with open(op.artifacts[0].filename, "rb") as f:
        return np.frombuffer(f.read(), dtype=np.uint32)


def patch_elf(elf_data, patches):
    for i, patch in patches.items():
        val, mask = patch
        val = np.uint64(val)
        mask = np.uint64(mask)  # uint32 arithmetic would overflow
        elf_data[i] = np.uint32((elf_data[i] & ~mask) | (val & mask))
    return elf_data


BF16 = np.dtype(ml_dtypes.bfloat16)


def _n_elements(nbytes):
    return max(nbytes, BF16.itemsize) // BF16.itemsize


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


class _PerBufferCallable(SequenceCallable):
    """Callable whose buffers are allocated one per name, with slice views into
    their parent. Inputs sync to the device before the run, all non-input
    buffers back to the host afterwards.
    """

    def _make_buffer(self, n_elements):
        raise NotImplementedError

    def _make_subbuffer(self, parent, offset_bytes, size_bytes):
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
            sub = self._make_subbuffer(
                self._buffers[base_name], start_bytes, end_bytes - start_bytes
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
    """

    def _make_buffer(self, n_elements):
        return XRTTensor((n_elements,), dtype=ml_dtypes.bfloat16)

    def _make_subbuffer(self, parent, offset_bytes, size_bytes):
        return XRTSubBuffer(
            parent_bo=parent.buffer_object(),
            offset_bytes=offset_bytes,
            size_bytes=size_bytes,
            shape=(size_bytes // BF16.itemsize,),
            dtype=ml_dtypes.bfloat16,
            parent=parent,
        )

    def _allocate_buffers(self):
        super()._allocate_buffers()
        op = self.op
        combined_xclbin_path = op.combined_xclbin.filename
        self._op_callable_map = {}  # id(op) -> NPUKernel
        for op_id, xclbin in op._op_xclbin_map.items():
            self._op_callable_map[op_id] = NPUKernel(
                xclbin_path=combined_xclbin_path,
                kernel_name=op._op_kernel_name_map[op_id],
                insts_path=op._op_insts_map[op_id].filename,
            )
        self._execution_plan = [
            (
                self._op_callable_map[id(step_op)],
                [self._resolve_buffer(name) for name in buf_names],
            )
            for step_op, *buf_names in op.runlist
        ]

    def _run(self):
        for kernel, args in self._execution_plan:
            kernel(*args)


class SequenceFullELFCallable(SequenceCallable):
    """Single-ELF dispatch (NPU2): every operator shares three consolidated
    input/output/scratch buffers addressed by offset. ``get_buffer`` returns a
    sub-view into whichever consolidated buffer holds the named argument.
    """

    def __init__(self, op, elf_data=None, device_name="main", sequence_name="sequence"):
        self.device_name = device_name
        self.sequence_name = sequence_name
        self.reload_elf(elf_data if elf_data is not None else load_elf(op))
        super().__init__(op)

    def reload_elf(self, elf_data):
        # pyxrt.elf takes a PyCapsule wrapping the raw pointer.
        elf_data_u8 = elf_data.view(dtype=np.uint8)
        ctypes.pythonapi.PyCapsule_New.restype = ctypes.py_object
        ctypes.pythonapi.PyCapsule_New.argtypes = [
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.c_void_p,
        ]
        capsule = ctypes.pythonapi.PyCapsule_New(elf_data_u8.ctypes.data, None, None)
        xrt_elf = pyxrt.elf(capsule, elf_data.nbytes)
        xrt_context = pyxrt.hw_context(aie_utils.DefaultNPURuntime._device, xrt_elf)
        self.xrt_kernel = pyxrt.ext.kernel(
            xrt_context, f"{self.device_name}:{self.sequence_name}"
        )

    def _allocate_buffers(self):
        in_sz, out_sz, scratch_sz = self.op.buffer_sizes
        self.input_buffer = XRTTensor((_n_elements(in_sz),), dtype=ml_dtypes.bfloat16)
        self.output_buffer = XRTTensor((_n_elements(out_sz),), dtype=ml_dtypes.bfloat16)
        self.scratch_buffer = XRTTensor(
            (_n_elements(scratch_sz),), dtype=ml_dtypes.bfloat16
        )

    def get_buffer(self, buffer_name):
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]
        buf_type, offset, length = self.op.get_layout_for_buffer(buffer_name)
        parent = {
            "input": self.input_buffer,
            "output": self.output_buffer,
            "scratch": self.scratch_buffer,
        }[buf_type]
        sub = XRTSubBuffer(
            parent_bo=parent.buffer_object(),
            offset_bytes=offset,
            size_bytes=length,
            shape=(length // BF16.itemsize,),
            dtype=ml_dtypes.bfloat16,
            parent=parent,
        )
        self._buffer_cache[buffer_name] = sub
        return sub

    def _sync_inputs(self):
        # Sub-views handed out by get_buffer() propagate their host-dirty state
        # to this parent, so the parent syncs to the device here.
        self.input_buffer.to("npu")

    def _sync_outputs(self):
        self.output_buffer.to("cpu")

    def _run(self):
        run = pyxrt.run(self.xrt_kernel)
        run.set_arg(0, self.input_buffer.buffer_object())
        run.set_arg(1, self.output_buffer.buffer_object())
        run.set_arg(2, self.scratch_buffer.buffer_object())
        run.start()
        ret_code = run.wait()
        if ret_code != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel execution failed with return code {ret_code}")


class _CPUBuffer:
    """Minimal host-side stand-in for ``XRTTensor``: a flat 1D ``torch.bfloat16``
    tensor with no-op device syncs.
    """

    def __init__(self, n_elements):
        self._t = torch.zeros(n_elements, dtype=torch.bfloat16)

    def torch_view(self):
        return self._t

    def to(self, *_args, **_kwargs):
        return self

    def fill_(self, value):
        self._t.fill_(value)
        return self

    def buffer_object(self):
        return None


def _reshape_for_spec(flat_tensor, spec):
    """Slice a flat host buffer to ``spec``'s element count and reshape (a view)."""
    n = int(np.prod(spec.shape)) if spec.shape else 1
    return flat_tensor[:n].reshape(spec.shape)


class SequenceReferenceCallable(_PerBufferCallable):
    """Pure-CPU evaluation via each operator's ``reference()``; no NPU dispatch.
    Device syncs are no-ops on the CPU buffers.
    """

    def _make_buffer(self, n_elements):
        return _CPUBuffer(n_elements)

    def _make_subbuffer(self, parent, offset_bytes, size_bytes):
        start = offset_bytes // BF16.itemsize
        end = (offset_bytes + size_bytes) // BF16.itemsize
        view = _CPUBuffer.__new__(_CPUBuffer)
        view._t = parent.torch_view()[start:end]
        return view

    def _run(self):
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

    def __init__(self, op, rel_tol=0.05, abs_tol=1e-2):
        super().__init__(op)
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol
        self.last_step_stats = []

    def _read_to_cpu(self, name, spec):
        buf = self._resolve_buffer(name)
        buf.to("cpu")
        n = int(np.prod(spec.shape)) if spec.shape else 1
        return buf.torch_view()[:n].clone().reshape(spec.shape)

    def _run(self):
        self.last_step_stats = []
        for step_idx, ((kernel, args), step) in enumerate(
            zip(self._execution_plan, self._iter_steps())
        ):
            step_op, in_names, in_specs, out_name, out_spec = step

            cpu_inputs = [
                self._read_to_cpu(name, spec) for name, spec in zip(in_names, in_specs)
            ]

            kernel(*args)

            npu_out = self._read_to_cpu(out_name, out_spec).to(torch.float32)
            ref_out = step_op.reference(*cpu_inputs)

            stats = {
                "step": step_idx,
                "op": type(step_op).__name__,
                "op_name": getattr(step_op, "name", type(step_op).__name__),
                "inputs": list(in_names),
                "output": out_name,
            }
            if ref_out is None:
                stats["skipped"] = True
                logger.info(
                    "[compare step %d] %s -> %s: no reference (skipped)",
                    step_idx,
                    stats["op"],
                    out_name,
                )
            else:
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
                level = logging.WARNING if fail else logging.INFO
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
            self.last_step_stats.append(stats)
