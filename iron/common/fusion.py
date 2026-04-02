# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import ml_dtypes
import pyxrt
import ctypes
from . import compilation as comp
from .base import AIEOperatorBase, MLIROperator, AIEBuffer
from .device_manager import AIEDeviceManager

# Fused Operator
# ##########################################################################


class FusedMLIROperator(AIEOperatorBase):
    """Operator that fuses multiple MLIROperators into one."""

    def __init__(
        self, name, runlist, input_args, output_args, buffer_sizes=None, *args, **kwargs
    ):
        assert all(
            isinstance(op, MLIROperator) and all(isinstance(buf, str) for buf in bufs)
            for op, *bufs in runlist
        )
        self.runlist = runlist
        self.name = name
        self.input_args = input_args
        self.output_args = output_args
        self.explicit_buffer_sizes = (
            buffer_sizes or {}
        )  # Optional dict: buffer_name -> size_in_bytes
        self.kernel_archive = "kernels.a"
        super().__init__(*args, **kwargs)

    def get_operator_name(self):
        return self.name

    def get_kernel_artifacts(self):
        """Collect all kernel artifacts from child operators."""
        kernel_artifacts = []
        unique_operators = []
        for op, *_ in self.runlist:
            if op not in unique_operators:
                unique_operators.append(op)
        for idx, op in enumerate(unique_operators):
            objs = op.get_kernel_artifacts()
            for obj in objs:
                obj.filename = f"op{idx}_{obj.filename}"
                obj.prefix_symbols = f"op{idx}_"
            kernel_artifacts.extend(objs)
        return kernel_artifacts

    def get_mlir_artifact(self):
        # Build operator_mlir_map: {op_name -> PythonGeneratedMLIRArtifact}
        operator_mlir_map = {}
        mlir_dependencies = []
        comp_runlist = []
        op_names = {}  # op -> op_name

        unique_operators = []
        for op, *_ in self.runlist:
            if op not in unique_operators:
                unique_operators.append(op)
        for idx, op in enumerate(unique_operators):
            mlir_artifact = op.get_mlir_artifact()
            if len(op.get_kernel_artifacts()) > 0:
                # FIXME: currently hard-coding that the design will accept this argument as an input if it uses kernels
                # Also not handling name collisions of kernels with the same name
                mlir_artifact.callback_kwargs["kernel_archive"] = self.kernel_archive
                mlir_artifact.callback_kwargs["func_prefix"] = f"op{idx}_"
            op_name = f"op{idx}_{op.__class__.__name__}"
            op_names[op] = op_name
            operator_mlir_map[op_name] = mlir_artifact

        for op, *bufs in self.runlist:
            comp_runlist.append((op_names[op], *bufs))

        # Calculate buffer layout: {buffer_name -> (type, offset, length)}
        self.subbuffer_layout, self.buffer_sizes, self.slice_info = (
            self._calculate_buffer_layout()
        )

        filename = self.get_operator_name() + "_fused.mlir"
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
            assert len(args_specs) == len(
                bufs
            ), "Number of buffers must match operator argument specification"
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
                        assert np.prod(args[buf_name].shape) == np.prod(
                            args_spec.shape
                        ), f"Buffer {buf_name} has conflicting sizes between operators"

        # Verify all input/output args are present (either as regular or sliced buffers)
        all_buffer_names = set(args.keys()) | set(sliced_buffers.keys())
        for arg in self.input_args:
            # Check if it's a base buffer name in explicit_buffer_sizes
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise AssertionError(
                    f"Input argument {arg} not found in runlist buffers"
                )
        for arg in self.output_args:
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise AssertionError(
                    f"Output argument {arg} not found in runlist buffers"
                )

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
        operator_name = self.get_operator_name()
        mlir_artifact = self.get_mlir_artifact()
        kernel_objects = self.get_kernel_artifacts()
        kernel_dep = (
            [
                comp.KernelArchiveArtifact(
                    self.kernel_archive,
                    dependencies=kernel_objects,
                )
            ]
            if kernel_objects
            else []
        )
        full_elf_artifact = comp.FullElfArtifact(
            f"{operator_name}.elf",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact] + kernel_dep,
        )
        self.add_artifacts([full_elf_artifact])

    def get_arg_spec(self):
        pass

    def get_callable(self):
        return FusedFullELFCallable(self)

    def get_layout_for_buffer(self, buffer_name):
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
        device_manager=None,
    ):
        self.device_name = device_name
        self.sequence_name = sequence_name
        self.device_manager = device_manager or AIEDeviceManager()
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
        xrt_context = pyxrt.hw_context(self.device_manager.device, xrt_elf)
        self.xrt_kernel = pyxrt.ext.kernel(
            xrt_context, f"{self.device_name}:{self.sequence_name}"
        )


class FusedFullELFCallable(FullELFCallable):
    def __init__(self, op, elf_data=None, device_manager=None):
        if elf_data is None:
            elf_data = load_elf(op)
        super().__init__(elf_data, device_manager=device_manager)

        self.op = op
        input_buffer_size, output_buffer_size, scratch_buffer_size = op.buffer_sizes
        itemsize = np.dtype(ml_dtypes.bfloat16).itemsize

        self.input_buffer = AIEBuffer(
            shape=(max(input_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )

        self.output_buffer = AIEBuffer(
            shape=(max(output_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16,
        )

        self.scratch_buffer = AIEBuffer(
            shape=(max(scratch_buffer_size, itemsize) // itemsize,),
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

        if main_buffer is None:
            raise RuntimeError(f"Main buffer for type '{buf_type}' is not allocated")

        # Convert byte offset/length to element offset/length
        itemsize = np.dtype(ml_dtypes.bfloat16).itemsize
        offset_elements = offset // itemsize
        length_elements = length // itemsize

        # Create subbuffer with appropriate shape
        sub_buffer = main_buffer.subbuffer(
            length=length_elements,
            offset=offset_elements,
            shape=(length_elements,),
            dtype=ml_dtypes.bfloat16,
        )

        # Cache and return
        self._buffer_cache[buffer_name] = sub_buffer
        return sub_buffer

    def __call__(self):
        self.input_buffer.to("npu")
        self.output_buffer.to("npu")
        super().__call__(
            self.input_buffer.bo if self.input_buffer else None,
            self.output_buffer.bo if self.output_buffer else None,
            self.scratch_buffer.bo if self.scratch_buffer else None,
        )
