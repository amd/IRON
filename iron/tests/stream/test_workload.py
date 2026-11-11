# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The workload a stream-dse operator exports, its mapping and its groups' arguments.

The design is solved from the torch module the workload is exported from,
and its groups' runtime arguments are read off that graph, so the names
the mapping and the operators use are the exported graph's.
"""

import pytest

pytest.importorskip("stream", reason="stream-dse is not installed")
pytest.importorskip("onnxscript", reason="onnxscript is not installed")

import yaml  # noqa: E402

from iron.common.stream.mapping import build_mapping, group_boundaries  # noqa: E402
from iron.operators.swiglu_prefill_stream import design  # noqa: E402
from iron.operators.swiglu_prefill_stream.op import (  # noqa: E402
    DOWN,
    GATE,
    LAYERS,
    MUL,
    PARTITIONS,
    READS,
    RESULTS,
    SILU,
    UP,
)

pytestmark = pytest.mark.usefixtures("npu2")

DIMS = (256, 512, 2048)


@pytest.fixture(scope="module")
def workload():
    return design.workload(*DIMS)


def test_the_nodes_are_the_operators_layers(workload):
    assert [name for name, _ in workload.nodes] == list(LAYERS)
    assert workload.buffers == ("input", "w_gate", "w_up", "w_down", "output")


@pytest.mark.parametrize("k", sorted(PARTITIONS))
def test_every_group_argument_is_a_named_tensor(workload, k):
    known = set(workload.buffers) | set(RESULTS.values())
    for inputs, outputs in group_boundaries(workload, PARTITIONS[k]):
        assert set(inputs) | set(outputs) <= known


def test_the_fused_group_takes_the_blocks_buffers_in_order(workload):
    [(inputs, outputs)] = group_boundaries(workload, PARTITIONS[1])
    assert inputs + outputs == workload.buffers


def test_a_split_group_hands_on_what_the_next_reads(workload):
    boundaries = dict(zip(LAYERS, group_boundaries(workload, PARTITIONS[5])))
    assert boundaries[MUL] == (("left_swished", "right"), ("intermediate",))
    produced = {n for _, outputs in boundaries.values() for n in outputs}
    consumed = {n for inputs, _ in boundaries.values() for n in inputs}
    external = (consumed - produced) | (produced - consumed)
    assert external == set(workload.buffers)


@pytest.mark.parametrize("k", sorted(PARTITIONS))
def test_the_mapping_declares_kernels_and_no_placement(workload, k):
    kernels, groups = design.mapping(k, design.GEMM_BLOCKS[-1], DIMS[2])
    mapping = build_mapping(workload, kernels, groups)
    assert [g["layers"] for g in mapping["fused_groups"]] == [
        list(g) for g in PARTITIONS[k]
    ]
    for layer in mapping["layers"]:
        assert layer["core_allocation"] == [] and layer["inter_core_tiling"] == []
        assert layer["kernel"]["name"]
    assert yaml.safe_load(yaml.dump(mapping)) == mapping


def test_a_block_no_core_can_divide_is_no_candidate(npu2):
    labels = [label for label, _ in design.candidates(256, 512, 2048, npu2)]
    seeds = {k: design.GEMM_BLOCKS if k == 1 else design.GEMM_BLOCKS[:1] for k in PARTITIONS}
    assert labels == [(k, b) for k in sorted(PARTITIONS) for b in seeds[k]]
    with pytest.raises(ValueError, match="hidden_dim"):
        design.candidates(256, 512, 2000, npu2, k=1)


def test_the_layers_read_what_the_exported_graph_says(workload):
    produced_by = {
        out: node.name for node in workload.graph.node for out in node.output
    }
    reads = {
        node.name: tuple(produced_by[t] for t in node.input if t in produced_by)
        for node in workload.graph.node
    }
    assert reads == READS


def test_the_post_op_partition_hands_the_gate_to_the_up_projection(workload):
    """SiLU and the product run as post-ops of the gate and up projections.

    The up projection reads the gate's result from the core beside it, so
    both are one group.
    """
    kernels, groups = design.mapping(2, design.GEMM_BLOCKS[-1], DIMS[2])
    mapping = build_mapping(workload, kernels, groups)
    front, down = mapping["fused_groups"]
    assert front["post_ops"] == [SILU, MUL]
    assert "post_ops" not in down
    assert group_boundaries(workload, [front["layers"]]) == [
        (("input", "w_gate", "w_up"), ("intermediate",))
    ]


def test_only_the_gemms_with_post_ops_narrow_their_embedding():
    kernels, _ = design.mapping(2, design.GEMM_BLOCKS[0], DIMS[2])
    assert kernels[GATE]["k"] == kernels[UP]["k"] == design.POST_OP_EMBEDDING
    assert (kernels[DOWN]["m"], kernels[DOWN]["k"], kernels[DOWN]["n"]) == (64, 64, 64)
