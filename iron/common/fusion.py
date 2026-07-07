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

    def get_kernel_artifacts(self):
        """Collect all kernel artifacts from child operators.

        Returns:
            List of KernelObjectArtifact instances from all unique child operators,
            with filenames and symbol prefixes disambiguated per operator index.
        """
        kernel_artifacts = []
        seen: dict[int, object] = {}
        unique_operators = [
            seen.setdefault(id(op), op) for op, *_ in self.runlist if id(op) not in seen
        ]
        for idx, op in enumerate(unique_operators):
            objs = op.get_kernel_artifacts()
            for obj in objs:
                obj.filename = f"op{idx}_{obj.filename}"
                obj.prefix_symbols = f"op{idx}_"
            kernel_artifacts.extend(objs)
        return kernel_artifacts

    def get_mlir_artifact(self):
        """Build and return the fused MLIR source artifact.

        Constructs the operator MLIR map and run-list, then wraps them in a
        ``SequenceMLIRSource`` artifact.  Buffer layout attributes
        (``subbuffer_layout``, ``buffer_sizes``, ``slice_info``) must already
        be set by ``set_up_artifacts()`` before this method is called.

        Returns:
            A ``SequenceMLIRSource`` artifact ready for compilation.
        """
        # Build operator_mlir_map: {op_name -> PythonGeneratedMLIRArtifact}
        operator_mlir_map = {}
        comp_runlist = []
        op_names = {}  # id(op) -> op_name

        seen2: dict[int, object] = {}
        unique_operators = [
            seen2.setdefault(id(op), op)
            for op, *_ in self.runlist
            if id(op) not in seen2
        ]
        for idx, op in enumerate(unique_operators):
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
        """Set up the artifact dependency graph for this fused operator.

        Computes the buffer layout first, then builds the artifacts.
        The dispatch mode (``"fused"`` vs ``"separate"``) is resolved here
        when set to ``"auto"``.
        """
        # Calculate buffer layout (used by both paths for get_buffer())
        self.subbuffer_layout, self.buffer_sizes, self.slice_info = (
            self._calculate_buffer_layout()
        )

        is_npu2 = isinstance(aie_utils.get_current_device(), NPU2)

        if self._dispatch == "auto":
            self._mode = "fused" if is_npu2 else "separate"
        elif self._dispatch == "fused":
            if not is_npu2:
                raise RuntimeError(
                    "dispatch='fused' requires NPU2 (Strix); "
                    "Phoenix/NPU1 does not support full-ELF dispatch"
                )
            self._mode = "fused"
        else:
            self._mode = self._dispatch  # "separate", "reference", or "compare"

        # Backwards-compat flag (used by get_callable/params_path).
        self._use_full_elf = self._mode == "fused"

        if self._mode == "fused":
            self._set_up_full_elf_artifacts()
        elif self._mode in ("separate", "compare"):
            self._set_up_xclbin_artifacts()
        else:
            # "reference": no NPU artifacts to compile.
            pass

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
        """Chained xclbin path (NPU1/Phoenix): separate xclbin per unique operator.

        Mirrors the pattern from ``chain_swiglu_artifacts`` in
        ``iron/operators/swiglu_base.py``: each unique operator gets its own
        xclbin + insts compiled separately, linked via ``--xclbin-input``.
        """
        seen: dict[int, object] = {}
        unique_operators = [
            seen.setdefault(id(op), op)
            for op, *_ in self.runlist
            if id(op) not in seen
        ]

        # Short hash to keep xclbin kernel names under 31 chars
        # (xclbinutil limits m_name to 64 chars as "name:name")
        name_hash = hashlib.sha1(self.name.encode()).hexdigest()[:6]

        artifacts = []
        prev_xclbin = None
        self._op_xclbin_map = {}   # id(op) -> xclbin artifact
        self._op_insts_map = {}    # id(op) -> insts artifact
        self._op_kernel_name_map = {}  # id(op) -> kernel_name

        for idx, op in enumerate(unique_operators):
            op_label = f"f{name_hash}_op{idx}"
            kernel_id = f"0x{0x901 + idx:x}"

            xclbin, insts = op.get_artifacts(prefix=f"{op_label}_")
            # Use list() to avoid mutating the shared extra_flags list
            # (get_artifacts may alias the same list between xclbin and insts)
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

        # The last xclbin in the chain is the combined xclbin.
        artifacts.append(prev_xclbin)
        self.combined_xclbin = prev_xclbin
        self.add_artifacts(artifacts)

    def get_arg_spec(self):
        raise NotImplementedError(
            "OperatorSequence does not expose a unified arg spec; "
            "use get_layout_for_buffer() to inspect individual buffer layouts"
        )

    def get_callable(self):
        """Return a callable that executes the fused operator on the NPU.

        Returns:
            A ``SequenceFullELFCallable`` when using fused dispatch, or a
            ``SequenceXclbinCallable`` when using separate dispatch.
        """
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
    elf_data = None
    with open(op.artifacts[0].filename, "rb") as f:
        elf_data = np.frombuffer(f.read(), dtype=np.uint32)
    return elf_data


def patch_elf(elf_data, patches):
    for i, patch in patches.items():
        val, mask = patch
        val = np.uint64(val)
        mask = np.uint64(mask)  # avoid numpy overflow errors
        elf_data[i] = np.uint32((elf_data[i] & ~mask) | (val & mask))
    return elf_data


class FullELFCallable:
    def __init__(
        self,
        elf_data,
        device_name="main",
        sequence_name="sequence",
    ):
        self.device_name = device_name
        self.sequence_name = sequence_name
        self.reload_elf(elf_data)

    def __call__(self, *args):
        run = pyxrt.run(self.xrt_kernel)
        for i, arg in enumerate(args):
            assert isinstance(arg, pyxrt.bo), f"Argument {i} is not a pyxrt.bo"
            run.set_arg(i, arg)
        run.start()
        ret_code = run.wait()
        if ret_code != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel execution failed with return code {ret_code}")

    def reload_elf(self, elf_data):
        # Create a PyCapsule from the numpy array pointer for pybind11
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


class SequenceFullELFCallable(FullELFCallable):
    def __init__(self, op, elf_data=None):
        if elf_data is None:
            elf_data = load_elf(op)
        super().__init__(elf_data)

        self.op = op
        input_buffer_size, output_buffer_size, scratch_buffer_size = op.buffer_sizes
        itemsize = np.dtype(ml_dtypes.bfloat16).itemsize

        self.input_buffer = XRTTensor(
            (max(input_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )

        self.output_buffer = XRTTensor(
            (max(output_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )

        self.scratch_buffer = XRTTensor(
            (max(scratch_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )

        self._buffer_cache = {}

    def get_buffer(self, buffer_name):
        # Return cached buffer if already allocated
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]

        buf_type, offset, length = self.op.get_layout_for_buffer(buffer_name)

        # Select the appropriate main buffer
        if buf_type == "input":
            main_buffer = self.input_buffer
        elif buf_type == "output":
            main_buffer = self.output_buffer
        elif buf_type == "scratch":
            main_buffer = self.scratch_buffer
        else:
            raise ValueError(
                f"Unknown buffer type '{buf_type}' for buffer '{buffer_name}'"
            )

        itemsize = np.dtype(ml_dtypes.bfloat16).itemsize
        sub_buffer = XRTSubBuffer(
            parent_bo=main_buffer.buffer_object(),
            offset_bytes=offset,
            size_bytes=length,
            shape=(length // itemsize,),
            dtype=ml_dtypes.bfloat16,
            parent=main_buffer,
        )

        self._buffer_cache[buffer_name] = sub_buffer
        return sub_buffer

    def __call__(self):
        # Sub-views handed out by get_buffer() propagate their device state to
        # these consolidated parents, so a caller that writes a sub-view via
        # torch_view() and then calls .to("npu") on it leaves the parent marked
        # host-dirty; the parent syncs to the device here. The kernel writes its
        # results into the device-side output buffer, which is synced back to
        # the host afterwards.
        self.input_buffer.to("npu")
        super().__call__(
            self.input_buffer.buffer_object(),
            self.output_buffer.buffer_object(),
            self.scratch_buffer.buffer_object(),
        )
        self.output_buffer.to("cpu")


class SequenceXclbinCallable:
    """Callable for OperatorSequence on NPU1 (Phoenix) using chained xclbins.

    Instead of a single ELF dispatch, each step in the runlist is executed as a
    separate ``NPUKernel`` invocation.  Buffers are shared (same ``XRTTensor``)
    across steps that reference the same buffer name, giving zero-copy handoff
    between sequential operators.
    """

    def __init__(self, op):
        self.op = op
        self.last_elapsed = 0.0

        combined_xclbin_path = op.combined_xclbin.filename

        # Build an NPUKernel per unique operator
        self._op_callable_map = {}  # id(op) -> NPUKernel
        for op_id, xclbin in op._op_xclbin_map.items():
            insts = op._op_insts_map[op_id]
            kernel_name = op._op_kernel_name_map[op_id]
            self._op_callable_map[op_id] = NPUKernel(
                xclbin_path=combined_xclbin_path,
                kernel_name=kernel_name,
                insts_path=insts.filename,
            )

        # Allocate one XRTTensor per unique base buffer name.
        # Buffers that appear in multiple runlist entries share the same tensor
        # (zero-copy between operators).
        itemsize = np.dtype(ml_dtypes.bfloat16).itemsize
        self._buffers = {}  # base buffer name -> XRTTensor
        for buf_name in list(op.subbuffer_layout.keys()):
            _, _, length = op.subbuffer_layout[buf_name]
            self._buffers[buf_name] = XRTTensor(
                (max(length, itemsize) // itemsize,),
                dtype=ml_dtypes.bfloat16,
            )

        # Pre-build the execution plan: list of (NPUKernel, [XRTTensor args])
        self._execution_plan = []
        for step_op, *buf_names in op.runlist:
            kernel = self._op_callable_map[id(step_op)]
            args = []
            for buf_name in buf_names:
                args.append(self._resolve_buffer(buf_name))
            self._execution_plan.append((kernel, args))

        # Cache for get_buffer() sub-buffer views (compatible with SequenceFullELFCallable API)
        self._buffer_cache = {}

        # Expose input/output/scratch buffers for API compatibility with
        # SequenceFullELFCallable (used by tests for .to("cpu") etc.)
        input_buffer_size, output_buffer_size, scratch_buffer_size = op.buffer_sizes
        self.input_buffer = XRTTensor(
            (max(input_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )
        self.output_buffer = XRTTensor(
            (max(output_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )
        self.scratch_buffer = XRTTensor(
            (max(scratch_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )

    def _resolve_buffer(self, buf_name):
        """Resolve a buffer name (possibly with slice notation) to an XRTTensor.

        Regular buffer names map directly to an allocated XRTTensor.
        Sliced buffer names (e.g. ``queries[0:128]``) create an XRTSubBuffer
        view into the parent buffer.
        """
        if buf_name in self._buffers:
            return self._buffers[buf_name]

        # Sliced buffer: "base_name[start:end]"
        if buf_name in self.op.slice_info:
            base_name, start_bytes, end_bytes = self.op.slice_info[buf_name]
            parent = self._buffers[base_name]
            itemsize = np.dtype(ml_dtypes.bfloat16).itemsize
            size_bytes = end_bytes - start_bytes
            sub = XRTSubBuffer(
                parent_bo=parent.buffer_object(),
                offset_bytes=start_bytes,
                size_bytes=size_bytes,
                shape=(size_bytes // itemsize,),
                dtype=ml_dtypes.bfloat16,
            )
            # Cache so the same slice always returns the same object
            self._buffers[buf_name] = sub
            return sub

        raise ValueError(f"Unknown buffer '{buf_name}' in fused runlist")

    def get_buffer(self, buffer_name):
        """Return an XRTTensor(-like) view for a named buffer.

        Compatible with the ``SequenceFullELFCallable.get_buffer()`` API so that
        test helpers (``_load_input``, ``_get_output_tensor``, etc.) work
        unchanged.

        For the xclbin path, each buffer is its own standalone XRTTensor (or
        XRTSubBuffer for sliced buffers), so this just returns the resolved
        buffer directly.
        """
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]
        buf = self._resolve_buffer(buffer_name)
        self._buffer_cache[buffer_name] = buf
        return buf

    def __call__(self):
        # Sync all input buffers to device
        for buf_name in self.op.input_args:
            self._buffers[buf_name].to("npu")

        t0 = time.perf_counter()
        for kernel, args in self._execution_plan:
            kernel(*args)
        self.last_elapsed = time.perf_counter() - t0

        # Sync all base buffers from device so callers can read results
        # (covers both output and scratch buffers)
        for buf_name in self.op.subbuffer_layout:
            if buf_name not in self.op.input_args:
                self._buffers[buf_name].to("cpu")


# ---------------------------------------------------------------------------
# Reference and compare dispatch
# ---------------------------------------------------------------------------


class _CPUBuffer:
    """Minimal buffer adapter compatible with the ``XRTTensor`` API used by
    callers (``torch_view``, ``to("npu")``, ``to("cpu")``, ``fill_``).

    Backed by a flat 1D ``torch.bfloat16`` tensor in host memory.  All device
    sync calls are no-ops.
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
    """Slice a flat host buffer to the element count implied by ``spec`` and
    reshape it to the operator-declared shape.

    Returns a view (no copy)."""
    n = int(np.prod(spec.shape)) if spec.shape else 1
    return flat_tensor[:n].reshape(spec.shape)


def _call_reference(step_op, inputs):
    """Invoke ``step_op.reference(*inputs)`` if available.

    Returns the reference output tensor, or ``None`` if the operator has no
    reference implementation.  Propagates other exceptions.
    """
    ref_fn = getattr(step_op, "reference", None)
    if ref_fn is None:
        return None
    try:
        return ref_fn(*inputs)
    except NotImplementedError:
        return None


class SequenceReferenceCallable:
    """Pure-CPU evaluation of a fused operator runlist.

    No NPU compilation or dispatch occurs.  Each runlist step calls
    ``op.reference(*inputs)`` on host-side ``torch.bfloat16`` buffers.

    Useful for validating the reference implementations themselves and for
    comparing layer-by-layer expected outputs against NPU output.
    """

    def __init__(self, op):
        self.op = op
        self.last_elapsed = 0.0
        itemsize = np.dtype(ml_dtypes.bfloat16).itemsize

        self._buffers = {}  # base buffer name -> _CPUBuffer
        for buf_name, (_, _, length) in op.subbuffer_layout.items():
            n = max(length, itemsize) // itemsize
            self._buffers[buf_name] = _CPUBuffer(n)

        # API parity with SequenceFullELFCallable / SequenceXclbinCallable
        input_buffer_size, output_buffer_size, scratch_buffer_size = op.buffer_sizes
        self.input_buffer = _CPUBuffer(max(input_buffer_size, itemsize) // itemsize)
        self.output_buffer = _CPUBuffer(max(output_buffer_size, itemsize) // itemsize)
        self.scratch_buffer = _CPUBuffer(max(scratch_buffer_size, itemsize) // itemsize)

        self._buffer_cache = {}

    def _resolve_buffer(self, buf_name):
        if buf_name in self._buffers:
            return self._buffers[buf_name]
        if buf_name in self.op.slice_info:
            base_name, start_bytes, end_bytes = self.op.slice_info[buf_name]
            parent = self._buffers[base_name]
            itemsize = np.dtype(ml_dtypes.bfloat16).itemsize
            start = start_bytes // itemsize
            end = end_bytes // itemsize
            sliced = _CPUBuffer.__new__(_CPUBuffer)
            sliced._t = parent.torch_view()[start:end]
            self._buffers[buf_name] = sliced
            return sliced
        raise ValueError(f"Unknown buffer '{buf_name}' in fused runlist")

    def get_buffer(self, buffer_name):
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]
        buf = self._resolve_buffer(buffer_name)
        self._buffer_cache[buffer_name] = buf
        return buf

    def __call__(self):
        t0 = time.perf_counter()
        for step_op, *buf_names in self.op.runlist:
            arg_specs = step_op.get_arg_spec()
            if len(arg_specs) != len(buf_names):
                raise ValueError(
                    f"Operator {step_op!r} arg-spec count {len(arg_specs)} "
                    f"does not match runlist buffer count {len(buf_names)}"
                )
            *in_names, out_name = buf_names
            *in_specs, out_spec = arg_specs

            inputs = []
            for name, spec in zip(in_names, in_specs):
                flat = self._resolve_buffer(name).torch_view()
                inputs.append(_reshape_for_spec(flat, spec).clone())

            out = _call_reference(step_op, inputs)
            if out is None:
                raise NotImplementedError(
                    f"Operator {type(step_op).__name__} has no reference "
                    f"implementation; cannot use dispatch='reference'"
                )

            out_flat = self._resolve_buffer(out_name).torch_view()
            n_out = int(np.prod(out_spec.shape)) if out_spec.shape else 1
            out_flat[:n_out].copy_(out.reshape(-1).to(torch.bfloat16))
        self.last_elapsed = time.perf_counter() - t0


class SequenceCompareCallable(SequenceXclbinCallable):
    """Run the separate-xclbin NPU pipeline and, after each step, run the
    operator's CPU reference on the same (NPU-produced) inputs.

    Logs per-step max-abs and max-rel error.  The NPU output is what
    propagates to the next step on both sides, so each comparison reflects
    only the deviation of the current operator (no error accumulation).
    """

    def __init__(self, op, rel_tol=0.05, abs_tol=1e-2):
        super().__init__(op)
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol
        # Per-step diagnostic records populated on each __call__.
        self.last_step_stats = []

    def _read_buffer_to_cpu(self, name, spec):
        """Sync a device buffer to host and return a reshaped float32 view."""
        buf = self._resolve_buffer(name)
        buf.to("cpu")
        flat = buf.torch_view()
        n = int(np.prod(spec.shape)) if spec.shape else 1
        return flat[:n].clone().reshape(spec.shape)

    def __call__(self):
        # Sync inputs to device.
        for buf_name in self.op.input_args:
            self._buffers[buf_name].to("npu")

        self.last_step_stats = []
        t0 = time.perf_counter()

        for step_idx, (kernel, args) in enumerate(self._execution_plan):
            step_op, *buf_names = self.op.runlist[step_idx]
            arg_specs = step_op.get_arg_spec()
            *in_names, out_name = buf_names
            *in_specs, out_spec = arg_specs

            # Snapshot NPU-side inputs before running the kernel.
            cpu_inputs = [
                self._read_buffer_to_cpu(name, spec)
                for name, spec in zip(in_names, in_specs)
            ]

            # Run NPU step.
            kernel(*args)

            # Read NPU output.
            npu_out = self._read_buffer_to_cpu(out_name, out_spec).to(torch.float32)

            # Run reference on the same inputs.
            ref_out = _call_reference(step_op, cpu_inputs)
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

        self.last_elapsed = time.perf_counter() - t0

        # Sync all base buffers back so callers can read results.
        for buf_name in self.op.subbuffer_layout:
            if buf_name not in self.op.input_args:
                self._buffers[buf_name].to("cpu")
