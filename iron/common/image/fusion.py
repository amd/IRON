# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Temporal fusion: a sequence's designs as one module, one device per array
(designs whose devices differ only in their runtime sequences share one) or
per pack of arrays (``coresidence``), and a main runtime sequence that
configures and runs them in turn.
"""

from __future__ import annotations

import hashlib
import logging
from collections.abc import Mapping
from typing import Any, NamedTuple

import numpy as np
from aie import ir
from aie.dialects import aie, aiex, arith, memref
from aie.helpers.util import mlir_type_to_np_dtype
from aie.utils import bfp
from aie.utils.compile.jit.compilabledesign import compile_context

from ..design import OperatorDesign
from .coresidence import AdjacentPacking, Packing, array_text, merge_devices

logger = logging.getLogger(__name__)

# The shim DMA addresses host memory in 32-bit words, so every buffer handed
# to a sub-design must start on one.
SHIM_ADDRESS_ALIGNMENT = 4


class ArgumentSizes(NamedTuple):
    """Bytes of each runtime-sequence argument of a fused image, in argument
    order; ``feedback`` is ``None`` where the image takes no such argument.
    """

    input: int
    output: int
    scratch: int
    feedback: int | None = None

    def arguments(self) -> dict[str, int]:
        """Size by kind, in argument order."""
        sizes = self._asdict()
        if self.feedback is None:
            del sizes["feedback"]
        return sizes


def _memref_bytes(memref_type: ir.MemRefType) -> int:
    """Bytes a runtime-sequence argument of ``memref_type`` spans."""
    dtype = mlir_type_to_np_dtype(memref_type.element_type)
    if dtype is None:
        raise TypeError(f"no host dtype for the elements of {memref_type}")
    return int(np.prod(memref_type.shape)) * bfp.itemsize(dtype)


class GeneratedDesign(NamedTuple):
    """A design's module taken apart: its one device and its module-scope
    scratchpad parameters (symbol -> type). The module keeps the ops alive.
    """

    module: ir.Module
    device: Any  # aie.DeviceOp
    parameters: dict[str, ir.Type]


def generate(design: OperatorDesign, context: ir.Context) -> GeneratedDesign:
    """``design``'s module, generated in ``context`` as a child of a fusion,
    taken apart.
    """
    # The fusion drives PDI loading itself; a child that also loads its own
    # links fine and hangs at dispatch (ERT_CMD_STATE_TIMEOUT).
    with compile_context(_iron_full_elf=False):
        module = (
            design.build(context=context)
            if design.exported is None
            else design.exported()
        )
    if not isinstance(module, ir.Module) or module.context is not context:
        module = ir.Module.parse(str(module), context)
    devices = []
    parameters: dict[str, ir.Type] = {}
    for op in module.body.operations:
        if isinstance(op, aie.DeviceOp):
            devices.append(op)
        elif op.operation.name == "aiex.scratchpad_parameter":
            sym_name = ir.StringAttr(op.operation.attributes["sym_name"]).value
            parameters[sym_name] = ir.TypeAttr(op.operation.attributes["type"]).value
    if len(devices) != 1:
        raise ValueError(
            f"expected exactly one device operation in the module of "
            f"'{design.name}', got {len(devices)}"
        )
    return GeneratedDesign(module, devices[0], parameters)


def parameters_preamble(parameters: Mapping[str, ir.Type]) -> str:
    """Module-scope declarations of ``parameters``, as text."""
    return "\n".join(
        f"  aiex.scratchpad_parameter @{name} : {param_type}"
        for name, param_type in parameters.items()
    )


class Fusion:
    """An operator sequence's designs, fused into one module.

    Each device is named for its design, not its step, so its text is the
    same in every graph and aiecc's device cache hits. ``seq.coresident``
    packs designs into one device each. ``seq``'s buffer layout must already
    be set.
    """

    RESET_DEVICE = "reset_device"

    def __init__(self, seq):
        designs, design_of = seq.unique_designs()
        own = [OperatorDesign(op) for op in designs]
        self.designs: dict[str, OperatorDesign] = {}
        for design in own:
            self.designs.setdefault(design.name, design)
        self.runlist = [
            (own[design_of[id(op)]].name, *bufs) for op, *bufs in seq.runlist
        ]
        self.subbuffer_layout = seq.subbuffer_layout
        self.buffer_sizes = seq.buffer_sizes
        self.slice_info = seq.slice_info or {}
        self.shared_words = dict(seq.shared_words or {})
        self.packing: Packing | AdjacentPacking = (
            seq.coresident
            if isinstance(seq.coresident, AdjacentPacking)
            else Packing(
                tuple(
                    tuple(dict.fromkeys(own[design_of[id(op)]].name for op in group))
                    for group in seq.coresident
                )
            )
        )

    @property
    def identity(self) -> str:
        """What ``text()`` is a function of, so a cache hit costs a hash
        rather than a fusion.
        """
        h = hashlib.sha256()
        for name, design in self.designs.items():
            h.update(f"{name}={design.compilable().recipe_hash};".encode())
        state = (
            self.runlist,
            self.subbuffer_layout,
            self.buffer_sizes,
            self.slice_info,
            sorted(self.shared_words.items()),
            self.packing,
        )
        h.update(repr(state).encode())
        return h.hexdigest()[:24]

    def needs_reset(self, packing: Packing) -> bool:
        """Whether the sequence must configure one more device than the runlist asks for.

        ``aiecc --expand-load-pdis`` marks each configure point by loading one of two
        otherwise empty PDIs, alternating between them from a fixed start. A load of the
        PDI already loaded has no effect, so a sequence with an odd number of configure
        points ends on the one the next dispatch starts with, and that dispatch
        reconfigures over the state the last design left. Configuring one more device
        makes the count even. Consecutive entries running in one device (one design,
        or one pack) share a configure point.
        """
        names = [packing.device_of(name) for name, *_ in self.runlist]
        points = sum(
            1 for i, name in enumerate(names) if i == 0 or name != names[i - 1]
        )
        return points % 2 == 1

    def text(self) -> str:
        """``module()`` as text."""
        return str(self.module(ir.Context()))

    def module(self, context: ir.Context) -> ir.Module:
        """The fused module, built in ``context``: every design's device, and a
        main device whose runtime sequence runs them in runlist order.
        """
        runlist = self.runlist
        subbuffer_layout = self.subbuffer_layout
        slice_info = self.slice_info
        shared = self.shared_words
        arguments = self.buffer_sizes.arguments()

        devices: dict[str, Any] = {}
        arrays: dict[str, str] = {}
        operator_param_decls: dict[str, dict[str, ir.Type]] = {}
        sequence_arg_types = {}
        # Each design's module owns its device until the device moves.
        generated_modules = []
        for op_name, design in self.designs.items():
            generated = generate(design, context)
            generated_modules.append(generated.module)
            device_op = generated.device
            for sym_name in generated.parameters:
                if sym_name in shared:
                    ir.SymbolTable.replace_all_symbol_uses(
                        sym_name, shared[sym_name], device_op.operation
                    )
            devices[op_name] = device_op
            arrays[op_name] = array_text(device_op)
            operator_param_decls[op_name] = {
                shared.get(sym_name) or sym_name: param_type
                for sym_name, param_type in generated.parameters.items()
            }
            sequence_arg_types[op_name] = self._sequence_arg_types(device_op)
        device_ty = next(iter(devices.values())).device
        by_key: dict[Any, list[str]] = {}
        for op_name, design in self.designs.items():
            by_key.setdefault(design.op.array_key(), []).append(op_name)
        for names in by_key.values():
            if len({arrays[n] for n in names}) > 1:
                logger.info(
                    "%s have one array_key, but their devices differ beyond "
                    "the runtime sequence, so they do not share an array",
                    names,
                )

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

        loc = ir.Location.unknown(context)
        module = ir.Module.create(loc)
        with context, loc, ir.InsertionPoint(module.body):
            # Emit hoisted parameters first.
            with ir.InsertionPoint.at_block_begin(module.body):
                for sym_name, param_type in hoisted_params.items():
                    aiex.scratchpad_parameter(sym_name, param_type)

            # Concatenate aie.device ops, merging each pack's into one.
            packing = self.packing
            if isinstance(packing, AdjacentPacking):
                packing, _ = packing.pack(
                    [op_name for op_name, *_ in runlist],
                    {op_name: str(device) for op_name, device in devices.items()},
                    parameters_preamble(hoisted_params),
                )
            packing = packing.sharing(arrays)
            for device_name, members in packing.devices(devices).items():
                member_ops = {}
                for op_name in members:
                    dev_op = devices[op_name]
                    dev_op.sym_name = ir.StringAttr.get(op_name)
                    module.body.append(dev_op)
                    member_ops[op_name] = dev_op
                if len(member_ops) > 1:
                    merge_devices(device_name, member_ops)

            needs_reset = self.needs_reset(packing)
            if needs_reset:

                @aie.device(device_ty)
                def reset():
                    @aiex.runtime_sequence()
                    def sequence():
                        pass

                reset_op: Any = reset  # a DeviceOp; region_op types it as the function
                reset_op.operation.attributes["sym_name"] = ir.StringAttr.get(
                    self.RESET_DEVICE
                )

            # Create the main device -- this contains the runtime sequence calling into the other devices
            @aie.device(device_ty)
            def main():
                # Flat bytes; each buffer is a typed view at its byte offset.
                arg_types: list[Any] = [
                    np.ndarray[(nbytes,), np.dtype[np.int8]]
                    for nbytes in arguments.values()
                ]

                @aiex.runtime_sequence(*arg_types)
                def sequence(*buffers):
                    consolidated_buffers = dict(zip(arguments, buffers))

                    # Execute operations in runlist order
                    configure_op = None
                    configure_body = None
                    last_device = None
                    for op_name, *buffer_names in runlist:
                        expected_arg_types = sequence_arg_types[op_name]
                        device_name = packing.device_of(op_name)

                        # Consecutive steps in one device share its configure point
                        if configure_op is None or device_name != last_device:
                            configure_op = aiex.ConfigureOp(
                                ir.FlatSymbolRefAttr.get(device_name)
                            )
                            configure_body = configure_op.body.blocks.append()
                            last_device = device_name

                        assert configure_body is not None
                        with ir.InsertionPoint(configure_body):
                            # For each buffer, view its bytes as the argument type
                            # the sub-design declares
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
                                    buf_type, offset, length = subbuffer_layout[
                                        buf_name
                                    ]

                                target_type = ir.MemRefType(expected_arg_types[idx])
                                expected_bytes = _memref_bytes(target_type)
                                if expected_bytes != length:
                                    raise ValueError(
                                        f"Size mismatch for buffer '{buf_name}': the "
                                        f"runtime sequence of '{op_name}' takes "
                                        f"{target_type} ({expected_bytes} bytes), the "
                                        f"layout gives it {length} bytes"
                                    )
                                # Low address bits are dropped: it would move.
                                if offset % SHIM_ADDRESS_ALIGNMENT:
                                    raise ValueError(
                                        f"Buffer '{buf_name}' of '{op_name}' starts at "
                                        f"byte {offset} of the {buf_type} argument, "
                                        f"which is not a multiple of "
                                        f"{SHIM_ADDRESS_ALIGNMENT}"
                                    )
                                buffer_ssa_values.append(
                                    memref.view(
                                        target_type,
                                        consolidated_buffers[buf_type],
                                        arith.constant(ir.IndexType.get(), offset),
                                        [],
                                    )
                                )

                            # Run Op
                            sequence_sym_ref_attr = ir.FlatSymbolRefAttr.get(
                                packing.sequence_of(op_name)
                            )
                            aiex.RunOp(sequence_sym_ref_attr, buffer_ssa_values)

                    if needs_reset:
                        reset_op = aiex.ConfigureOp(
                            ir.FlatSymbolRefAttr.get(self.RESET_DEVICE)
                        )
                        reset_op.body.blocks.append()

            return module

    @staticmethod
    def _sequence_arg_types(dev_op: Any) -> list[Any]:
        """The argument types of a device's runtime sequence."""
        for nested_op in dev_op.body_region.blocks[0].operations:
            if nested_op.operation.name == "aie.runtime_sequence":
                return [arg.type for arg in nested_op.body.blocks[0].arguments]
        raise RuntimeError("Could not find runtime sequence in device operation")
