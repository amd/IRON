# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Temporal fusion of multiple MLIR modules into one module with multiple devices and a main runtime sequence that calls into them.
"""

import numpy as np
import importlib.util
from pathlib import Path
from aie import ir
from aie.dialects import aie, aiex, memref
from aie.extras.context import mlir_mod_ctx
import ml_dtypes

from . import (
    CompilationArtifact,
    CompilationRule,
    CompilationCommand,
    PythonCallbackCompilationCommand,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)

# Compilation Artifacts
# ##########################################################################


class FusedMLIRSource(CompilationArtifact):
    def __init__(
        self,
        filename,
        operator_mlir_map,
        runlist,
        subbuffer_layout,
        buffer_sizes,
        slice_info=None,
    ):
        dependencies = list(operator_mlir_map.values())
        super().__init__(filename, dependencies)
        self.operator_mlir_map = operator_mlir_map
        self.runlist = runlist
        self.subbuffer_layout = subbuffer_layout
        self.buffer_sizes = buffer_sizes
        self.slice_info = slice_info or {}


# Helper Functions
# ##########################################################################


def extract_runtime_sequence_arg_types(dev_op):
    """MLIR helper: Extract argument types from a device operation's runtime sequence."""
    for nested_op in dev_op.body_region.blocks[0].operations:
        op_name = nested_op.operation.name
        if op_name == "aie.runtime_sequence":
            if hasattr(nested_op, "body") and hasattr(nested_op.body, "blocks"):
                if len(nested_op.body.blocks) > 0:
                    entry_block = nested_op.body.blocks[0]
                    arg_types = [
                        entry_block.arguments[i].type
                        for i in range(len(entry_block.arguments))
                    ]
                    return arg_types
    raise RuntimeError("Could not find runtime sequence in device operation")


def get_child_mlir_module(mlir_artifact):
    """Extract MLIR module from a PythonGeneratedMLIRArtifact."""
    assert isinstance(mlir_artifact, PythonGeneratedMLIRArtifact)
    spec = importlib.util.spec_from_file_location(
        Path(mlir_artifact.import_path).name, mlir_artifact.import_path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if mlir_artifact.requires_context:
        raise NotImplementedError("Not handled, make your operator return a ctx.module")

    callback_function = getattr(module, mlir_artifact.callback_fn)
    mlir_module = callback_function(
        *mlir_artifact.callback_args, **mlir_artifact.callback_kwargs
    )
    return mlir_module


def fuse_mlir(artifact):
    """Fuse multiple MLIR modules by inlining their device operations and adding a new main device and runtime sequence that call into sequence of operations based on a runlist."""

    input_buffer_size, output_buffer_size, scratch_buffer_size = artifact.buffer_sizes

    # Extract device operations from each operator's MLIR artifact
    device_mlir_strings = {}
    device_ty = None
    sequence_arg_types = {}
    for op_name, mlir_artifact in artifact.operator_mlir_map.items():
        mlir_module = get_child_mlir_module(mlir_artifact)
        device_ops = [
            op for op in mlir_module.body.operations if isinstance(op, aie.DeviceOp)
        ]
        assert (
            len(device_ops) == 1
        ), f"Expected exactly one device operation in MLIR artifact for operator '{op_name}'"
        device_op = device_ops[0]
        if device_ty is None:
            device_ty = device_op.device
        device_mlir_strings[op_name] = str(device_op)
        sequence_arg_types[op_name] = extract_runtime_sequence_arg_types(device_op)

    # Build fused MLIR module
    with mlir_mod_ctx() as ctx:

        # Concatenate aie.device ops
        for op_name, device_str in device_mlir_strings.items():
            dev_op = aie.DeviceOp.parse(device_str)
            dev_op.sym_name = ir.StringAttr.get(op_name)
            ctx.module.body.append(dev_op)

        # Create the main device -- this contains the runtime sequence calling into the other devices
        @aie.device(device_ty)
        def main():
            buf_dtype = np.dtype[
                ml_dtypes.bfloat16
            ]  # TODO: support for other data types
            itemsize = 2

            # RuntimeSequenceOp
            @aiex.runtime_sequence(
                np.ndarray[(input_buffer_size // itemsize,), buf_dtype],
                np.ndarray[(output_buffer_size // itemsize,), buf_dtype],
                np.ndarray[(scratch_buffer_size // itemsize,), buf_dtype],
            )
            def sequence(input_buf, output_buf, scratch_buf):
                consolidated_buffers = {
                    "input": input_buf,
                    "output": output_buf,
                    "scratch": scratch_buf,
                }

                # Execute operations in runlist order
                configure_op = None
                last_op_name = None
                for op_name, *buffer_names in artifact.runlist:
                    expected_arg_types = sequence_arg_types[op_name]

                    # Avoid reconfiguring altogether if the same op is called multiple times consecutively
                    if configure_op is None or op_name != last_op_name:
                        # Configure Op
                        configure_sym_ref_attr = ir.FlatSymbolRefAttr.get(op_name)
                        configure_op = aiex.ConfigureOp(
                            configure_sym_ref_attr
                        )  # TODO: optimization -- if previous op was in the same device, skip reconfiguration
                        configure_body = configure_op.body.blocks.append()
                        last_op_name = op_name

                    with ir.InsertionPoint(configure_body):

                        # For each buffer, add subview and reinterpret_cast ops
                        buffer_ssa_values = []
                        for idx, buf_name in enumerate(buffer_names):
                            # Check if this is a sliced buffer
                            if buf_name in artifact.slice_info:
                                base_name, start, end = artifact.slice_info[buf_name]
                                # Get parent buffer info
                                buf_type, parent_offset, parent_length = (
                                    artifact.subbuffer_layout[base_name]
                                )
                                # Calculate actual offset and length for slice
                                offset = parent_offset + start
                                length = end - start
                            else:
                                # Regular buffer
                                buf_type, offset, length = artifact.subbuffer_layout[
                                    buf_name
                                ]

                            # Subview Op
                            consolidated_buf = consolidated_buffers[buf_type]
                            offset_elements = offset // itemsize
                            size_elements = length // itemsize
                            subview = memref.subview(
                                consolidated_buf,
                                [offset_elements],
                                [size_elements],
                                [1],
                            )

                            # Reinterpret_cast Op
                            target_type = expected_arg_types[idx]
                            expected_memref = ir.MemRefType(target_type)
                            target_shape = [
                                expected_memref.shape[i]
                                for i in range(expected_memref.rank)
                            ]
                            expected_size = np.prod(target_shape)
                            assert (
                                expected_size == size_elements
                            ), f"Size mismatch for buffer '{buf_name}': MLIR runtime sequence expected {expected_size}, Python fused operator provided {size_elements}"
                            strides = []
                            stride = 1
                            for dim in reversed(target_shape):
                                strides.insert(0, stride)
                                stride *= dim
                            result_type = ir.MemRefType.get(
                                target_shape, ir.BF16Type.get()
                            )
                            reinterpreted = memref.reinterpret_cast(
                                result=result_type,
                                source=subview,
                                offsets=[],
                                sizes=[],
                                strides=[],
                                static_offsets=[0],
                                static_sizes=target_shape,
                                static_strides=strides,
                            )
                            buffer_ssa_values.append(reinterpreted)

                        # Run Op
                        sequence_sym_ref_attr = ir.FlatSymbolRefAttr.get("sequence")
                        run_op = aiex.RunOp(sequence_sym_ref_attr, buffer_ssa_values)

        # Write the fused MLIR to file
        with open(artifact.filename, "w") as f:
            f.write(str(ctx.module))


# Compilation Rules
# ##########################################################################


class FusePythonGeneratedMLIRCompilationRule(CompilationRule):
    """Compilation rule that fuses multiple MLIR modules into one."""

    def matches(self, graph):
        return any(graph.get_worklist(FusedMLIRSource))

    def compile(self, graph):
        commands = []
        worklist = graph.get_worklist(FusedMLIRSource)
        for artifact in worklist:
            callback = lambda artifact=artifact: fuse_mlir(artifact)
            commands.append(PythonCallbackCompilationCommand(callback))
            new_artifact = SourceArtifact(artifact.filename)
            new_artifact.available = True
            graph.replace(artifact, new_artifact)
        return commands
