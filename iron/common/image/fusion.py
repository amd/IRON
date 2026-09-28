# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Temporal fusion: a sequence's designs as one module, one device per design
and a main runtime sequence that configures and runs them in turn.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any, NamedTuple

import numpy as np
from aie import ir
from aie.dialects import aie, aiex, arith, memref
from aie.helpers.util import mlir_type_to_np_dtype
from aie.utils import bfp
from aie.utils.compile.jit.compilabledesign import compile_context

from ..design import OperatorDesign

# The shim DMA addresses host memory in 32-bit words, so every buffer handed
# to a sub-design must start on one.
SHIM_ADDRESS_ALIGNMENT = 4


class ArgumentSizes(NamedTuple):
    """Bytes of each runtime-sequence argument of a fused image, in argument order.

    ``feedback`` is ``None`` for an image that declares no feedback buffer; the
    argument then does not exist, and the image takes the first three alone.
    """

    input: int
    output: int
    scratch: int
    feedback: int | None = None

    def arguments(self) -> dict[str, int]:
        """The arguments the runtime sequence takes: size by kind, in order, so
        a kind's argument index is its position."""
        sizes = self._asdict()
        if self.feedback is None:
            del sizes["feedback"]
        return sizes


def _memref_bytes(memref_type: ir.MemRefType) -> int:
    """Bytes a runtime-sequence argument of ``memref_type`` spans (a block-float
    element counts its packed block)."""
    dtype = mlir_type_to_np_dtype(memref_type.element_type)
    if dtype is None:
        raise TypeError(f"no host dtype for the elements of {memref_type}")
    return int(np.prod(memref_type.shape)) * bfp.itemsize(dtype)


class Fusion:
    """An operator sequence's designs, fused into one module.

    Each design is one device, named for what it is
    (:attr:`OperatorDesign.name`) rather than where it sits in the sequence,
    so one design is one device text whichever graph it is fused into and at
    whatever step: aiecc's device cache keys on that text. Designs whose
    names agree generate the same device and are fused as one.

    ``seq``'s buffer layout (``subbuffer_layout``, ``buffer_sizes``,
    ``slice_info``) must already be set. :meth:`text` is the generator
    ``CompilableDesign`` runs, :attr:`identity` what it is keyed on.
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

    @property
    def identity(self) -> str:
        """What the fused text is a function of, without generating it: each
        design's key (its identity and its sources), the runlist over them,
        the buffer layout and the scratchpad words symbols share. A hit then
        costs a hash rather than a fusion.
        """
        h = hashlib.sha256()
        for name, design in self.designs.items():
            h.update(f"{name}={design.key};".encode())
        state = (
            self.runlist,
            self.subbuffer_layout,
            self.buffer_sizes,
            self.slice_info,
            sorted(self.shared_words.items()),
        )
        h.update(repr(state).encode())
        return h.hexdigest()[:24]

    @property
    def needs_reset(self) -> bool:
        """Whether the sequence must configure one more device than the runlist asks for.

        ``aiecc --expand-load-pdis`` marks each configure point by loading one of two
        otherwise empty PDIs, alternating between them from a fixed start. A load of the
        PDI already loaded has no effect, so a sequence with an odd number of configure
        points ends on the one the next dispatch starts with, and that dispatch
        reconfigures over the state the last design left. Configuring one more device
        makes the count even. Consecutive entries running the same operator share a
        configure point.
        """
        names = [name for name, *_ in self.runlist]
        points = sum(
            1 for i, name in enumerate(names) if i == 0 or name != names[i - 1]
        )
        return points % 2 == 1

    def text(self) -> str:
        """The fused module: every design's device, and a main device whose
        runtime sequence runs them in runlist order.

        ``shared_words`` renames design symbols onto the scratchpad word they
        share (``iron.common.graph.compiled._words``): each reference in a
        device is rewritten and the word declared once.
        """
        runlist = self.runlist
        subbuffer_layout = self.subbuffer_layout
        slice_info = self.slice_info
        shared = self.shared_words
        # A reference is ``@symbol`` ending where the symbol does.
        shared_ref = (
            re.compile(
                "@("
                + "|".join(re.escape(s) for s in sorted(shared, key=len, reverse=True))
                + r")(?![\w$.])"
            )
            if shared
            else None
        )
        arguments = self.buffer_sizes.arguments()

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
        for op_name, mlir_module in self._children():
            device_ops = []
            params_here: dict[str, ir.Type] = {}
            for op in mlir_module.body.operations:
                if isinstance(op, aie.DeviceOp):
                    device_ops.append(op)
                elif op.operation.name == "aiex.scratchpad_parameter":
                    sym_name = ir.StringAttr(op.operation.attributes["sym_name"]).value
                    param_type = ir.TypeAttr(op.operation.attributes["type"]).value
                    params_here[shared.get(sym_name) or sym_name] = param_type
            if len(device_ops) != 1:
                raise ValueError(
                    f"Expected exactly one device operation in MLIR artifact for operator '{op_name}', "
                    f"got {len(device_ops)}"
                )
            device_op = device_ops[0]
            if device_ty is None:
                device_ty = device_op.device
            device_str = str(device_op)
            if shared_ref is not None:
                device_str = shared_ref.sub(
                    lambda m: "@" + shared[m.group(1)], device_str
                )
            device_mlir_strings[op_name] = device_str
            operator_param_decls[op_name] = params_here
            sequence_arg_types[op_name] = self._sequence_arg_types(device_op)

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
        loc = ir.Location.unknown(ir.Context())
        module = ir.Module.create(loc)
        with loc.context, loc, ir.InsertionPoint(module.body):
            # Emit hoisted parameters first.
            with ir.InsertionPoint.at_block_begin(module.body):
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
                module.body.append(dev_op)

            needs_reset = self.needs_reset
            if needs_reset:

                @aie.device(device_ty)  # pyright: ignore[reportCallIssue]  # see main()
                def reset():
                    @aiex.runtime_sequence()
                    def sequence():
                        pass

                reset_op: Any = reset  # a DeviceOp; region_op types it as the function
                reset_op.operation.attributes["sym_name"] = ir.StringAttr.get(
                    self.RESET_DEVICE
                )

            # Create the main device -- this contains the runtime sequence calling into the other devices
            # region_op annotates its decorator as the op it builds; a checker sees the
            # decorated function as not callable.
            @aie.device(device_ty)  # pyright: ignore[reportCallIssue]
            def main():
                # Each argument is a flat run of bytes; a buffer in one is a
                # view of the type its sub-design declares, at the buffer's
                # byte offset, so it keeps its dtype and an offset_parameter
                # on it is scaled by its own element size.
                # numpy array types, which runtime_sequence converts to memrefs.
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

                                # Parsed anew: the sub-design's type may
                                # belong to the context it was generated in.
                                target_type = ir.MemRefType(
                                    ir.Type.parse(str(expected_arg_types[idx]))
                                )
                                expected_bytes = _memref_bytes(target_type)
                                if expected_bytes != length:
                                    raise ValueError(
                                        f"Size mismatch for buffer '{buf_name}': the "
                                        f"runtime sequence of '{op_name}' takes "
                                        f"{target_type} ({expected_bytes} bytes), the "
                                        f"layout gives it {length} bytes"
                                    )
                                # The shim DMA addresses host memory in 32-bit
                                # words: a descriptor's low address bits are
                                # dropped, so a misaligned buffer would
                                # silently move.
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
                            sequence_sym_ref_attr = ir.FlatSymbolRefAttr.get("sequence")
                            aiex.RunOp(sequence_sym_ref_attr, buffer_ssa_values)

                    if needs_reset:
                        reset_op = aiex.ConfigureOp(
                            ir.FlatSymbolRefAttr.get(self.RESET_DEVICE)
                        )
                        reset_op.body.blocks.append()

            return str(module)

    def _children(self):
        """Each design's module, generated as a child of the fusion.

        ``_iron_full_elf`` makes a design's runtime sequence load its own PDI,
        because on that path no xclbin configures the device. Exactly one
        program in a fused build needs that, and it is not the children: the
        fusion inlines each child's device and drives PDI switching itself
        (:attr:`needs_reset`). Generated inside ``compile()`` without this,
        every child also emits a ``load_pdi`` and the two schemes fight: the
        build succeeds, the ELF links, and the device hangs at dispatch with
        ERT_CMD_STATE_TIMEOUT.
        """
        with compile_context(_iron_full_elf=False):
            for name, design in self.designs.items():
                module = design.generator()
                if isinstance(module, str):
                    module = ir.Module.parse(module, ir.Context())
                yield name, module

    @staticmethod
    def _sequence_arg_types(dev_op: Any) -> list[Any]:
        """The argument types of a device's runtime sequence."""
        for nested_op in dev_op.body_region.blocks[0].operations:
            if nested_op.operation.name == "aie.runtime_sequence":
                return [arg.type for arg in nested_op.body.blocks[0].arguments]
        raise RuntimeError("Could not find runtime sequence in device operation")
