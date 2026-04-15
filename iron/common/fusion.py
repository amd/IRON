# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import hashlib
import logging
import time
import numpy as np
import ml_dtypes
import pyxrt
import ctypes
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


class FusedMLIROperator(AIEOperatorBase):
    """Operator that fuses multiple MLIROperators into one.

    Args:
        dispatch: Dispatch strategy for the fused operator.
            ``"auto"`` (default) selects ``"fused"`` on NPU2 and
            ``"separate"`` on NPU1.  ``"fused"`` uses a single-ELF
            dispatch (requires NPU2).  ``"separate"`` compiles each
            sub-operator to its own xclbin and invokes them sequentially.
    """

    DISPATCH_MODES = ("auto", "fused", "separate")

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
        ``FusedMLIRSource`` artifact.  Buffer layout attributes
        (``subbuffer_layout``, ``buffer_sizes``, ``slice_info``) must already
        be set by ``set_up_artifacts()`` before this method is called.

        Returns:
            A ``FusedMLIRSource`` artifact ready for compilation.
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
        fused_artifact = comp.FusedMLIRSource(
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
            self._use_full_elf = is_npu2
        elif self._dispatch == "fused":
            if not is_npu2:
                raise RuntimeError(
                    "dispatch='fused' requires NPU2 (Strix); "
                    "Phoenix/NPU1 does not support full-ELF dispatch"
                )
            self._use_full_elf = True
        else:  # "separate"
            self._use_full_elf = False

        if self._use_full_elf:
            self._set_up_full_elf_artifacts()
        else:
            self._set_up_xclbin_artifacts()

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
            "FusedMLIROperator does not expose a unified arg spec; "
            "use get_layout_for_buffer() to inspect individual buffer layouts"
        )

    def get_callable(self):
        """Return a callable that executes the fused operator on the NPU.

        Returns:
            A ``FusedFullELFCallable`` when using fused dispatch, or a
            ``FusedXclbinCallable`` when using separate dispatch.
        """
        if self._use_full_elf:
            return FusedFullELFCallable(self)
        return FusedXclbinCallable(self)

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


class FusedFullELFCallable(FullELFCallable):
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
        )

        self._buffer_cache[buffer_name] = sub_buffer
        return sub_buffer

    def __call__(self):
        self.input_buffer.to("npu")
        super().__call__(
            self.input_buffer.buffer_object(),
            self.output_buffer.buffer_object(),
            self.scratch_buffer.buffer_object(),
        )
        self.output_buffer.to("cpu")


class FusedXclbinCallable:
    """Callable for FusedMLIROperator on NPU1 (Phoenix) using chained xclbins.

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

        # Cache for get_buffer() sub-buffer views (compatible with FusedFullELFCallable API)
        self._buffer_cache = {}

        # Expose input/output/scratch buffers for API compatibility with
        # FusedFullELFCallable (used by tests for .to("cpu") etc.)
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

        Compatible with the ``FusedFullELFCallable.get_buffer()`` API so that
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
