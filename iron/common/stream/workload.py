# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Export a reference ``nn.Module`` into the ONNX workload stream-dse optimizes.

:func:`torch.onnx.export` captures the module and lowers it through the
translation table in :mod:`~iron.common.stream.ops`, so every operator is emitted
in the form stream-dse's parsers expect. Because the operator's reference module is
the only description of the computation, the generated design cannot drift from the
reference the operator is tested against.

The exported graph is then adjusted for what stream-dse consumes: weight payloads
are dropped (it needs shapes, not values) and nodes and their results are given the
operator's names, which the mapping refers to.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from iron.common.stream.ops import op_for_onnx_type, translation_table

_WEIGHT_DATA_FIELDS = (
    "float_data",
    "double_data",
    "int32_data",
    "int64_data",
    "uint64_data",
    "raw_data",
)


@dataclass(frozen=True)
class StreamWorkload:
    """An exported workload: the ONNX model and the names the mapping refers to."""

    model: object  # onnx.ModelProto
    nodes: tuple[tuple[str, str], ...]  # (node name, kernel key), topological order
    buffers: tuple[str, ...]  # runtime buffer names, in argument order

    @property
    def shapes(self) -> dict[str, tuple[int, ...]]:
        """Every named tensor's shape, as the exported graph declares it."""
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
        import onnx

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        onnx.save(self.model, str(path))
        return str(path)


def _drop_weight_data(model) -> None:
    """Keep each initializer's shape and type, drop its values."""
    for initializer in model.graph.initializer:
        for field in _WEIGHT_DATA_FIELDS:
            initializer.ClearField(field)


def _rename(model, node_names, result_names, output_name: str) -> None:
    """Give nodes and the tensors they produce the operator's names."""
    nodes = list(model.graph.node)
    if node_names is not None and len(node_names) != len(nodes):
        raise ValueError(
            f"node_names has {len(node_names)} entries but the exported graph has "
            f"{len(nodes)} nodes"
        )

    graph_output = model.graph.output[0].name
    renamed: dict[str, str] = {}
    for position, node in enumerate(nodes):
        if node_names is not None:
            node.name = node_names[position]
        produced = node.output[0]
        target = (
            output_name
            if produced == graph_output
            else result_names.get(node.name, f"out_{node.name}")
        )
        renamed[produced] = target

    for node in nodes:
        node.input[:] = [renamed.get(name, name) for name in node.input]
        node.output[:] = [renamed.get(name, name) for name in node.output]
    for value in model.graph.value_info:
        value.name = renamed.get(value.name, value.name)
    for output in model.graph.output:
        output.name = renamed.get(output.name, output.name)


def export_workload(
    module,
    example_inputs,
    node_names=None,
    result_names=None,
    output_name: str = "output",
) -> StreamWorkload:
    """Export ``module`` into a :class:`StreamWorkload`.

    ``example_inputs`` fixes the shapes: re-exporting with different ones is all
    that is needed for a different problem size, since the mapping carries tile
    sizes and placement but no absolute dimensions.

    Tensor names come from the module -- its ``forward`` argument names and its
    parameter names. The exporter names the computation nodes and their results
    after the operators it captured, which the mapping would then have to refer to,
    so both can be renamed:

    * ``node_names`` -- computation nodes, in topological order.
    * ``result_names`` -- node name -> the name of the tensor it produces
      (default ``out_{node_name}``). The final result is always ``output_name``.
    """
    import torch

    program = torch.onnx.export(
        module,
        tuple(example_inputs),
        dynamo=True,
        custom_translation_table=translation_table(),
        optimize=False,
        verbose=False,
    )
    model = program.model_proto
    _drop_weight_data(model)
    _rename(model, node_names, result_names or {}, output_name)

    nodes = tuple(
        (node.name, op_for_onnx_type(node.op_type).kernel.key)
        for node in model.graph.node
    )
    # Runtime buffer order: activations, then weights in module order, then the
    # output -- the order the operator's argument spec and the mapping follow.
    buffers = (
        tuple(i.name for i in model.graph.input)
        + tuple(i.name for i in model.graph.initializer)
        + (output_name,)
    )
    return StreamWorkload(model, nodes, buffers)
