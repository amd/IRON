# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A reference ``torch.nn.Module`` exported into the ONNX workload stream-dse solves.

``torch.onnx.export`` captures the module and lowers it through ``ops``'
translation table, so every operator is emitted in the form stream-dse
parses. stream-dse reads the graph and its shapes from it; what each node
computes is its kernel's, and the operator's ``reference()`` is what a run
is judged by. Weight payloads are dropped (stream-dse reads shapes), and the nodes take
the operator's names for its layers, which the mapping refers to.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

# The name of an exported module's result.
OUTPUT = "output"
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

    def group_arguments(
        self, layers: Sequence[str]
    ) -> tuple[tuple[str, ...], tuple[str, ...]]:
        """Return the tensors a fused group reads from outside it and those it writes for outside.

        They are the group's runtime arguments, in the order its layers use
        them, which is the order of its design's runtime sequence.
        """
        graph = self.graph
        members = set(layers)
        produced_by = {out: node.name for node in graph.node for out in node.output}
        readers: dict[str, set[str]] = {}
        for node in graph.node:
            for tensor in node.input:
                readers.setdefault(tensor, set()).add(node.name)
        graph_outputs = {out.name for out in graph.output}

        inputs: list[str] = []
        outputs: list[str] = []
        for node in graph.node:
            if node.name not in members:
                continue
            for tensor in node.input:
                if produced_by.get(tensor) not in members and tensor not in inputs:
                    inputs.append(tensor)
            for tensor in node.output:
                leaves = tensor in graph_outputs or readers.get(tensor, set()) - members
                if leaves and tensor not in outputs:
                    outputs.append(tensor)
        return tuple(inputs), tuple(outputs)

    def write(self, path) -> str:
        """Write the ONNX model to ``path`` and return the path."""
        import onnx  # pyright: ignore[reportMissingImports]

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        onnx.save(self.model, str(path))
        return str(path)


def _drop_weight_data(model) -> None:
    for initializer in model.graph.initializer:
        for name in _WEIGHT_DATA_FIELDS:
            initializer.ClearField(name)


def _rename(model, node_names) -> None:
    """Name each node, and its result ``out_<node>``; the graph's result is ``OUTPUT``."""
    nodes = list(model.graph.node)
    if len(node_names) != len(nodes):
        raise ValueError(
            f"node_names has {len(node_names)} entries but the exported graph has "
            f"{len(nodes)} nodes"
        )
    graph_output = model.graph.output[0].name
    renamed: dict[str, str] = {}
    for node, name in zip(nodes, node_names):
        node.name = name
        produced = node.output[0]
        renamed[produced] = OUTPUT if produced == graph_output else f"out_{name}"
    for node in nodes:
        node.input[:] = [renamed.get(name, name) for name in node.input]
        node.output[:] = [renamed.get(name, name) for name in node.output]
    for value in [*model.graph.value_info, *model.graph.output]:
        value.name = renamed.get(value.name, value.name)


def export_workload(module, example_inputs, node_names) -> StreamWorkload:
    """Export ``module`` at the shapes of ``example_inputs``.

    The module names the input tensors: its ``forward`` arguments and
    parameters. The exporter would name each node after the operator it
    captured, so the caller names them.

    Args:
        module: The reference module.
        example_inputs: Its inputs, which fix every shape.
        node_names: Each computation node's name, in topological order.

    Raises:
        ValueError: ``node_names`` does not name every node.
    """
    import torch  # pyright: ignore[reportMissingImports]

    from .ops import op_for_onnx_type, translation_table

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
    _rename(model, node_names)
    nodes = tuple(
        (node.name, op_for_onnx_type(node.op_type).kernel) for node in model.graph.node
    )
    buffers = (
        tuple(i.name for i in model.graph.input)
        + tuple(i.name for i in model.graph.initializer)
        + (OUTPUT,)
    )
    return StreamWorkload(model, nodes, buffers)
