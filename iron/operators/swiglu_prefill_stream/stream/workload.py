# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Build the ONNX workload stream-dse optimizes from an operator's layers.

The layers are the ones the operator's reference evaluates, so the generated
design cannot drift from the reference the operator is tested against. Every
operator is emitted in the form stream-dse's parsers expect, through the registry
in ``iron.operators.swiglu_prefill_stream.stream.ops``. Weights carry their shape
and no values: stream-dse needs shapes, not values.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import onnx
from onnx import TensorProto, helper

from iron.operators.swiglu_prefill_stream.stream.ops import (
    CUSTOM_DOMAIN,
    op_for_onnx_type,
)

ONNX_OPSET = 20


@dataclass(frozen=True)
class StreamWorkload:
    """A workload: the ONNX model and the names the mapping refers to."""

    model: onnx.ModelProto
    nodes: tuple[tuple[str, str], ...]  # (node name, kernel key), topological order
    buffers: tuple[str, ...]  # runtime buffer names, in argument order

    @property
    def shapes(self) -> dict[str, tuple[int, ...]]:
        """Every named tensor's shape, as the graph declares it."""
        graph = self.model.graph
        declared = list(graph.input) + list(graph.value_info) + list(graph.output)
        shapes = {
            value.name: tuple(d.dim_value for d in value.type.tensor_type.shape.dim)
            for value in declared
        }
        shapes.update(
            {
                initializer.name: tuple(initializer.dims)
                for initializer in graph.initializer
            }
        )
        return shapes

    def write(self, path) -> str:
        """Write the ONNX model to ``path`` and return it.

        stream-dse's parser loads the workload from a file, so the model is
        materialized at build time (under the build directory, never in the tree).
        """
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        onnx.save(self.model, str(path))
        return str(path)


def build_workload(
    layers,
    tensors: dict[str, np.ndarray],
    inputs: tuple[str, ...],
    node_names,
    output_name: str = "output",
) -> StreamWorkload:
    """Build a ``StreamWorkload`` of ``layers``.

    Args:
        `layers`: `(result, ONNX operator, operands)` triples in topological order.
        `tensors`: every tensor the layers name, evaluated at the problem size;
            only their shapes and dtypes are read, so a different problem size is
            all a different workload needs.
        `inputs`: the activations. Every other operand no layer produces is a
            weight.
        `node_names`: the computation nodes' names, one per layer, which the
            mapping refers to.
        `output_name`: the result the graph returns.

    Returns:
        The workload, its runtime buffers ordered activations, then weights in
        the order the layers use them, then the output.
    """
    if len(node_names) != len(layers):
        raise ValueError(
            f"node_names has {len(node_names)} entries but there are "
            f"{len(layers)} layers"
        )
    produced = [result for result, _, _ in layers]
    weights = tuple(
        dict.fromkeys(
            name
            for _, _, operands in layers
            for name in operands
            if name not in produced and name not in inputs
        )
    )

    def value(name):
        tensor = tensors[name]
        return helper.make_tensor_value_info(
            name, helper.np_dtype_to_tensor_dtype(tensor.dtype), tensor.shape
        )

    nodes = [
        helper.make_node(
            onnx_type,
            operands,
            [result],
            name=name,
            domain=op_for_onnx_type(onnx_type).domain,
            **op_for_onnx_type(onnx_type).attributes,
        )
        for name, (result, onnx_type, operands) in zip(node_names, layers)
    ]
    graph = helper.make_graph(
        nodes,
        "main_graph",
        [value(name) for name in inputs],
        [value(output_name)],
        initializer=[
            TensorProto(
                name=name,
                data_type=helper.np_dtype_to_tensor_dtype(tensors[name].dtype),
                dims=tensors[name].shape,
            )
            for name in weights
        ],
        value_info=[
            value(name) for name in (*weights, *produced) if name != output_name
        ],
    )
    model = helper.make_model(
        graph,
        opset_imports=[
            helper.make_opsetid("", ONNX_OPSET),
            helper.make_opsetid(CUSTOM_DOMAIN, 1),
        ],
        ir_version=10,
    )
    return StreamWorkload(
        model,
        tuple((node.name, op_for_onnx_type(node.op_type).kernel.key) for node in nodes),
        (*inputs, *weights, output_name),
    )
