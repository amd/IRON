# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Temporal fusion of multiple MLIR modules into one module with multiple devices and a main runtime sequence that calls into them.
"""

from __future__ import annotations

import numpy as np
import importlib.util
from functools import partial
from pathlib import Path
from aie import ir
from aie.dialects import aie, aiex, memref
from aie.extras.context import mlir_mod_ctx
import ml_dtypes

from typing import Any

from . import (
    CompilationArtifactGraph,
    CompilationRule,
    CompilationCommand,
    PythonCallbackCompilationCommand,
    PythonGeneratedMLIRArtifact,
    MLIRArtifact,
)

RESET_DEVICE = "reset_device"


# Compilation Artifacts
# ##########################################################################


class SequenceMLIRArtifact(MLIRArtifact):
    def __init__(
        self,
        filename: str,
        operator_mlir_map: dict[str, PythonGeneratedMLIRArtifact],
        runlist: list[tuple[str, ...]],
        subbuffer_layout: dict[str, tuple[str, int, int]],
        buffer_sizes: tuple[int, int, int],
        slice_info: dict[str, tuple[str, int, int]] | None = None,
        trace_size: int = 0,
    ) -> None:
        dependencies = list(operator_mlir_map.values())
        super().__init__(filename, dependencies)
        self.operator_mlir_map = operator_mlir_map
        self.runlist = runlist
        self.subbuffer_layout = subbuffer_layout
        self.buffer_sizes = buffer_sizes
        self.slice_info = slice_info or {}
        # Bytes of trace buffer per runlist step, 0 for an untraced build.
        self.trace_size = trace_size


# Helper Functions
# ##########################################################################


def extract_runtime_sequence_arg_types(dev_op: Any) -> list[Any]:
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


def get_child_mlir_module(mlir_artifact: PythonGeneratedMLIRArtifact) -> Any:
    """Extract MLIR module from a PythonGeneratedMLIRArtifact.

    Uses the artifact's DesignGenerator to dynamically import the design
    module and call the callback, returning the raw (non-stringified) MLIR
    module object for further inspection by the fusion pass.
    """
    if not isinstance(mlir_artifact, PythonGeneratedMLIRArtifact):
        raise TypeError(
            f"Expected PythonGeneratedMLIRArtifact, got {type(mlir_artifact).__name__}"
        )
    gen = mlir_artifact.generator
    spec = importlib.util.spec_from_file_location(gen.source_path.name, gen.source_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    callback_function = getattr(module, gen.fn_name)
    return callback_function(*gen.args, **gen.kwargs)


def needs_additional_reset(runlist: list[Any]) -> bool:
    """Whether the sequence must configure one more device than the runlist asks for.

    ``aiecc --expand-load-pdis`` marks each configure point by loading one of two
    otherwise empty PDIs, alternating between them from a fixed start. A load of the
    PDI already loaded has no effect, so a sequence with an odd number of configure
    points ends on the one the next dispatch starts with, and that dispatch
    reconfigures over the state the last design left. Configuring one more device
    makes the count even. Consecutive entries running the same operator share a
    configure point.
    """
    points = 0
    previous = None
    for op_name, *_ in runlist:
        if op_name != previous:
            points += 1
            previous = op_name
    return points % 2 == 1


def fuse_mlir(artifact: SequenceMLIRArtifact) -> None:
    """Fuse multiple MLIR modules by inlining their device operations and adding a new main device and runtime sequence that call into sequence of operations based on a runlist."""

    input_buffer_size, output_buffer_size, scratch_buffer_size = artifact.buffer_sizes

    # Extract device operations and module-level parameter decls from each
    # operator's MLIR artifact.  Note: in the current MLIR-AIE pipeline,
    # ``aiex.scratchpad_parameter`` ops are emitted at *module* scope (above the
    # ``aie.device``), because the scratchpad is a single hardware resource
    # shared across all PDIs in a runlist and the verifier on
    # ``aiex.read_scratchpad_parameter`` requires the decl to be visible at module
    # scope.  We collect those module-level decls per-operator so we can
    # re-declare them once at the top of the fused module.
    device_mlir_strings = {}
    operator_param_decls: dict[str, dict[str, ir.Type]] = {}
    device_ty = None
    sequence_arg_types = {}
    for op_name, mlir_artifact in artifact.operator_mlir_map.items():
        mlir_module = get_child_mlir_module(mlir_artifact)
        device_ops = []
        params_here: dict[str, ir.Type] = {}
        for op in mlir_module.body.operations:
            if isinstance(op, aie.DeviceOp):
                device_ops.append(op)
            elif op.operation.name == "aiex.scratchpad_parameter":
                sym_name = ir.StringAttr(op.operation.attributes["sym_name"]).value
                param_type = ir.TypeAttr(op.operation.attributes["type"]).value
                params_here[sym_name] = param_type
        if len(device_ops) != 1:
            raise ValueError(
                f"Expected exactly one device operation in MLIR artifact for operator '{op_name}', "
                f"got {len(device_ops)}"
            )
        device_op = device_ops[0]
        if device_ty is None:
            device_ty = device_op.device
        device_mlir_strings[op_name] = str(device_op)
        operator_param_decls[op_name] = params_here
        sequence_arg_types[op_name] = extract_runtime_sequence_arg_types(device_op)

    # Deduplicate parameter decls across operators (same name must have the
    # same type; otherwise indices would collide in the global state table).
    hoisted_params: dict[str, ir.Type] = {}
    for op_name, params_here in operator_param_decls.items():
        for sym_name, param_type in params_here.items():
            existing = hoisted_params.get(sym_name)
            if existing is not None and str(existing) != str(param_type):
                raise ValueError(
                    f"ScratchpadParameter '{sym_name}' is declared with conflicting "
                    f"types across operators: {existing} vs {param_type}"
                )
            hoisted_params[sym_name] = param_type

    # Build fused MLIR module
    with mlir_mod_ctx() as ctx:

        # Emit hoisted parameters first.
        with ir.InsertionPoint.at_block_begin(ctx.module.body):
            for sym_name, param_type in hoisted_params.items():
                aiex.scratchpad_parameter(sym_name, param_type)

        # Concatenate aie.device ops.
        params_preamble = "\n".join(
            f"  aiex.scratchpad_parameter @{name} : {param_type}"
            for name, param_type in hoisted_params.items()
        )
        for op_name, device_str in device_mlir_strings.items():
            wrapped = f"module {{\n{params_preamble}\n{device_str}\n}}"
            wrapper_module = ir.Module.parse(wrapped)
            # Find the (sole) DeviceOp in the wrapper module.
            dev_op = None
            for op in wrapper_module.body.operations:
                if isinstance(op, aie.DeviceOp):
                    dev_op = op
                    break
            assert (
                dev_op is not None
            ), f"DeviceOp missing after re-parse for operator '{op_name}'"
            dev_op.sym_name = ir.StringAttr.get(op_name)
            ctx.module.body.append(dev_op)

        needs_reset = needs_additional_reset(artifact.runlist)
        if needs_reset:

            @aie.device(device_ty)
            def reset():
                @aiex.runtime_sequence()
                def sequence():
                    pass

            reset.operation.attributes["sym_name"] = ir.StringAttr.get(RESET_DEVICE)

        # Create the main device -- this contains the runtime sequence calling into the other devices
        @aie.device(device_ty)
        def main():
            buf_dtype = np.dtype[
                ml_dtypes.bfloat16
            ]  # TODO: support for other data types
            itemsize = np.dtype(ml_dtypes.bfloat16).itemsize

            # RuntimeSequenceOp
            trace_size = getattr(artifact, "trace_size", 0)
            n_traced = len(artifact.runlist) if trace_size else 0

            @aiex.runtime_sequence(
                np.ndarray[(input_buffer_size // itemsize,), buf_dtype],
                np.ndarray[(output_buffer_size // itemsize,), buf_dtype],
                np.ndarray[(scratch_buffer_size // itemsize,), buf_dtype],
                *(
                    [np.ndarray[(max(1, n_traced * trace_size),), np.dtype[np.int8]]]
                    if trace_size
                    else []
                ),
            )
            def sequence(input_buf, output_buf, scratch_buf, *trace_bufs):
                consolidated_buffers = {
                    "input": input_buf,
                    "output": output_buf,
                    "scratch": scratch_buf,
                }

                # Execute operations in runlist order
                configure_op = None
                last_op_name = None
                run_index = 0
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

                        # Trace lowering appends a buffer to the callee, so the call
                        # has to carry one too. Each op writes its own slice.
                        if trace_size:
                            buffer_ssa_values.append(
                                memref.subview(
                                    trace_bufs[0],
                                    [run_index * trace_size],
                                    [trace_size],
                                    [1],
                                )
                            )

                        # Run Op
                        sequence_sym_ref_attr = ir.FlatSymbolRefAttr.get("sequence")
                        run_op = aiex.RunOp(sequence_sym_ref_attr, buffer_ssa_values)
                        run_index += 1

                if needs_reset:
                    reset_op = aiex.ConfigureOp(ir.FlatSymbolRefAttr.get(RESET_DEVICE))
                    reset_op.body.blocks.append()

        # Write the fused MLIR to file
        with open(artifact.filename, "w") as f:
            f.write(str(ctx.module))


# Compilation Rules
# ##########################################################################


class FusePythonGeneratedMLIRCompilationRule(CompilationRule):
    """Compilation rule that fuses multiple MLIR modules into one."""

    def matches(self, graph: CompilationArtifactGraph) -> bool:
        return any(graph.get_worklist(SequenceMLIRArtifact))

    def compile(self, graph: CompilationArtifactGraph) -> list[CompilationCommand]:
        commands: list[CompilationCommand] = []
        worklist = graph.get_worklist(SequenceMLIRArtifact)
        for artifact in worklist:
            callback = partial(fuse_mlir, artifact)
            commands.append(PythonCallbackCompilationCommand(callback))
            artifact.available = True
        return commands
