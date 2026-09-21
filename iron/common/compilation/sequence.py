# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Temporal fusion of multiple MLIR modules into one module with multiple devices and a main runtime sequence that calls into them.
"""

from __future__ import annotations

import numpy as np
from aie import ir
from aie.dialects import aie, aiex, memref
from aie.extras.context import mlir_mod_ctx
from aie.utils.trace import get_trace_slices
import ml_dtypes

from typing import Any

from . import DesignGenerator

RESET_DEVICE = "reset_device"


# Compilation Artifacts
# ##########################################################################


def trace_buffer_size(mlir_text: str) -> int:
    """Bytes of the fused trace buffer the dispatched sequence takes.

    `-aie-fuse-trace-buffers` gives the sequence one buffer covering every design
    it configures, and records the split on the sequence. Returns 0 for an
    untraced build.
    """
    slices = get_trace_slices(mlir_text)
    return max((s["offset"] + s["size"] for s in slices), default=0)


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


def get_child_mlir_module(generator: DesignGenerator) -> Any:
    """Call a per-operator MLIR generator and return its raw Module.

    Shares DesignGenerator.resolve() rather than repeating the import and
    call: this path needs the module object instead of its string form
    (DesignGenerator.__call__ stringifies), and when the two were separate a
    change to argument assembly reached only one.
    """
    callback_function, args, kwargs = generator.resolve()
    return callback_function(*args, **kwargs)


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


def fuse_mlir(
    operator_generators: dict[str, DesignGenerator],
    runlist: list[tuple[str, ...]],
    subbuffer_layout: dict[str, tuple[str, int, int]],
    buffer_sizes: tuple[int, int, int],
    slice_info: dict[str, tuple[str, int, int]] | None = None,
    child_scalars: dict[str, list[str]] | None = None,
    sequences: dict[str, list[tuple[str, ...]]] | None = None,
) -> str:
    """Fuse multiple MLIR modules into one, and return the result as text.

    Inlines each operator's device operations and adds a new main device and
    runtime sequence that calls into them in ``runlist`` order. A plain
    function rather than an artifact+rule: nothing here needs the artifact
    graph's file-based caching, since the caller (``FusedDispatch.link_elf``)
    hands the returned text straight to ``CompilableDesign``, which keys its
    own cache on the text's content.

    ``child_scalars`` names, per operator, the dispatch-time scalars its
    sequence takes after its buffers (an image without a scratchpad). The
    main sequence then takes one ``i32`` per distinct name, after the three
    arenas, in first-use order, and forwards each child its own.

    ``sequences`` (a module) names several runlists, each becoming its own
    runtime sequence of the main device over the same arenas, named for its
    entry point; ``runlist`` is then their concatenation, which is what the
    buffer layout was computed over.
    """
    slice_info = slice_info or {}
    child_scalars = child_scalars or {}
    main_scalars: list[str] = []
    for op_name, *_ in runlist:
        for name in child_scalars.get(op_name, ()):
            if name not in main_scalars:
                main_scalars.append(name)
    input_buffer_size, output_buffer_size, scratch_buffer_size = buffer_sizes

    # Extract device operations and module-level parameter decls from each
    # operator's MLIR generator.  Note: in the current MLIR-AIE pipeline,
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
    for op_name, generator in operator_generators.items():
        mlir_module = get_child_mlir_module(generator)
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

        entries = sequences or {"sequence": runlist}
        needs_reset = any(needs_additional_reset(r) for r in entries.values())
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

            def body(input_buf, output_buf, scratch_buf, scalar_args, runlist):
                consolidated_buffers = {
                    "input": input_buf,
                    "output": output_buf,
                    "scratch": scratch_buf,
                }
                scalar_of = dict(zip(main_scalars, scalar_args))

                # Execute operations in runlist order
                configure_op = None
                last_op_name = None
                for op_name, *buffer_names in runlist:
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
                            if buf_name in slice_info:
                                base_name, start, end = slice_info[buf_name]
                                # Get parent buffer info
                                buf_type, parent_offset, parent_length = (
                                    subbuffer_layout[base_name]
                                )
                                # Calculate actual offset and length for slice
                                offset = parent_offset + start
                                length = end - start
                            else:
                                # Regular buffer
                                buf_type, offset, length = subbuffer_layout[buf_name]

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

                        # Run Op; the child's scalars follow its buffers.
                        sequence_sym_ref_attr = ir.FlatSymbolRefAttr.get("sequence")
                        scalars = [scalar_of[n] for n in child_scalars.get(op_name, ())]
                        run_op = aiex.RunOp(
                            sequence_sym_ref_attr, buffer_ssa_values + scalars
                        )

                if needs_additional_reset(runlist):
                    reset_op = aiex.ConfigureOp(ir.FlatSymbolRefAttr.get(RESET_DEVICE))
                    reset_op.body.blocks.append()

            # One runtime sequence per entry point (a module), or the one
            # named "sequence", all over the same arenas and scalars.
            arg_types = [
                np.ndarray[(input_buffer_size // itemsize,), buf_dtype],
                np.ndarray[(output_buffer_size // itemsize,), buf_dtype],
                np.ndarray[(scratch_buffer_size // itemsize,), buf_dtype],
                *([np.int32] * len(main_scalars)),
            ]
            for entry_name, entry_runlist in entries.items():

                def sequence(input_buf, output_buf, scratch_buf, *scalar_args, _r=entry_runlist):
                    body(input_buf, output_buf, scratch_buf, scalar_args, _r)

                aiex.runtime_sequence(*arg_types, sym_name=entry_name)(sequence)

        return str(ctx.module)
