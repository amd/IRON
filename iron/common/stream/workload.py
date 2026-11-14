# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A reference ``torch.nn.Module`` exported into the ONNX workload stream-dse solves.

``torch.onnx.export`` captures the module and lowers it through ``ops``'
translation table, so every operator is emitted in the form stream-dse
parses. The module is the only description of the computation, so the
design cannot drift from the reference the operator is tested against.
Weight payloads are dropped (stream-dse reads shapes), and nodes and their
results take the operator's names, which the mapping refers to.
"""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .ops import op_for_onnx_type, translation_table

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
    """An exported workload: the ONNX model and the names the mapping refers to.

    Attributes:
        model: The ``onnx.ModelProto``.
        nodes: Each computation node's name and kernel, in topological order.
        buffers: The runtime buffers, activations then weights then the output.
    """

    model: Any
    nodes: tuple[tuple[str, str], ...]
    buffers: tuple[str, ...]

    @property
    def graph(self):
        return self.model.graph

    @property
    def shapes(self) -> dict[str, tuple[int, ...]]:
        """Every named tensor's shape, as the exported graph declares it."""
        graph = self.graph
        declared = list(graph.input) + list(graph.value_info) + list(graph.output)
        shapes = {
            value.name: tuple(d.dim_value for d in value.type.tensor_type.shape.dim)
            for value in declared
        }
        shapes.update({init.name: tuple(init.dims) for init in graph.initializer})
        return shapes

    def write(self, path) -> str:
        """Write the ONNX model to ``path`` and return the path."""
        import onnx

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        onnx.save(self.model, str(path))
        return str(path)


def _drop_weight_data(model) -> None:
    for initializer in model.graph.initializer:
        for name in _WEIGHT_DATA_FIELDS:
            initializer.ClearField(name)


def _rename(model, node_names, result_names, output_name: str) -> None:
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
        renamed[produced] = (
            output_name
            if produced == graph_output
            else result_names.get(node.name, f"out_{node.name}")
        )
    for node in nodes:
        node.input[:] = [renamed.get(name, name) for name in node.input]
        node.output[:] = [renamed.get(name, name) for name in node.output]
    for value in [*model.graph.value_info, *model.graph.output]:
        value.name = renamed.get(value.name, value.name)


def export_workload(
    module,
    example_inputs,
    node_names=None,
    result_names=None,
    output_name: str = "output",
) -> StreamWorkload:
    """Export ``module`` at the shapes of ``example_inputs``.

    Tensors are named by the module: its ``forward`` arguments and
    parameters. The exporter names nodes after the operators it captured,
    which the mapping would then have to name, so both can be renamed.

    Args:
        module: The reference module.
        example_inputs: Its inputs, which fix every shape.
        node_names: Each computation node's name, in topological order.
        result_names: Per node name, the tensor it produces
            (``out_<node>`` otherwise); the final result is ``output_name``.
        output_name: The name of the module's result.

    Raises:
        ValueError: ``node_names`` does not name every node.
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
    assert program is not None, "the dynamo exporter returns its program"
    model = program.model_proto
    _drop_weight_data(model)
    _rename(model, node_names, result_names or {}, output_name)
    nodes = tuple(
        (node.name, op_for_onnx_type(node.op_type).kernel) for node in model.graph.node
    )
    buffers = (
        tuple(i.name for i in model.graph.input)
        + tuple(i.name for i in model.graph.initializer)
        + (output_name,)
    )
    return StreamWorkload(model, nodes, buffers)
