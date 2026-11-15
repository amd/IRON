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

import numpy as np  # noqa: E402
import torch  # noqa: E402
import yaml  # noqa: E402
from aie.utils.verify import compare  # noqa: E402
from ml_dtypes import bfloat16  # noqa: E402

from iron.operators.swiglu_prefill_stream import design  # noqa: E402
from iron.operators.swiglu_prefill_stream.op import (  # noqa: E402
    DOWN,
    GATE,
    LAYERS,
    MUL,
    PARTITIONS,
    POST_OP_PARTITION,
    SILU,
    UP,
    SwiGLUFusedStream,
)

pytestmark = pytest.mark.usefixtures("npu2")

DIMS = (256, 512, 2048)


@pytest.fixture(scope="module")
def workload():
    return design.workload(*DIMS)


def _seeds(mappings):
    """Return each mapping's number of groups and the block its down projection is seeded at."""
    return [
        (len(m.groups), tuple(m.kernels[DOWN][dim] for dim in ("m", "n", "k")))
        for m in mappings
    ]


def test_the_nodes_are_the_operators_layers(workload):
    assert [name for name, _ in workload.nodes] == list(LAYERS)
    assert workload.buffers == ("input", "w_gate", "w_up", "w_down", "output")


@pytest.mark.parametrize("partition", sorted(PARTITIONS))
def test_every_group_argument_is_a_named_tensor(workload, partition):
    known = set(workload.buffers) | {f"out_{layer}" for layer in LAYERS}
    for layers in PARTITIONS[partition]:
        inputs, outputs = workload.group_arguments(layers)
        assert set(inputs) | set(outputs) <= known


def test_the_fused_group_takes_the_blocks_buffers_in_order(workload):
    inputs, outputs = workload.group_arguments(LAYERS)
    assert inputs + outputs == workload.buffers


def test_each_layers_group_writes_what_the_next_reads(workload):
    arguments = {layer: workload.group_arguments((layer,)) for layer in LAYERS}
    assert arguments[MUL] == (("out_silu", "out_up"), ("out_mul",))
    written = {name for _, outputs in arguments.values() for name in outputs}
    read = {name for inputs, _ in arguments.values() for name in inputs}
    assert (read - written) | (written - read) == set(workload.buffers)


@pytest.mark.parametrize("partition", sorted(PARTITIONS))
def test_the_mapping_declares_kernels_and_no_placement(workload, partition):
    mapping = design.mapping(partition, design.GEMM_BLOCKS[-1], DIMS[2])
    text = mapping.to_dict(workload)
    assert [g["layers"] for g in text["fused_groups"]] == [
        list(g) for g in PARTITIONS[partition]
    ]
    for layer in text["layers"]:
        assert layer["core_allocation"] == [] and layer["kernel"]["name"]
    assert yaml.safe_load(yaml.dump(text)) == text


def test_a_mapping_naming_a_layer_the_workload_has_not_is_refused(workload):
    mapping = design.mapping(1, design.GEMM_BLOCKS[-1], DIMS[2])
    mapping.kernels["other"] = {}
    with pytest.raises(ValueError, match="other"):
        mapping.to_dict(workload)


def test_a_block_no_core_can_divide_is_no_candidate(npu2):
    large, small = design.GEMM_BLOCKS
    assert _seeds(design.candidates(256, 512, 2048, npu2)) == [
        (1, large),
        (1, small),
        (2, large),
        (5, large),
    ]
    with pytest.raises(ValueError, match="hidden_dim"):
        design.candidates(256, 512, 2000, npu2, partition=1)


def test_a_sequence_too_short_for_the_large_block_offers_every_partition_the_small_one(
    npu2,
):
    """128 rows over four core rows take the 32-row block only: each partition is offered it."""
    small = design.GEMM_BLOCKS[-1]
    assert _seeds(design.candidates(128, 1024, 4096, npu2)) == [
        (partition, small) for partition in sorted(PARTITIONS)
    ]


def test_the_post_ops_run_in_the_group_of_the_gate_and_up_projections(workload):
    mapping = design.mapping(POST_OP_PARTITION, design.GEMM_BLOCKS[-1], DIMS[2])
    gated, down = mapping.to_dict(workload)["fused_groups"]
    assert gated["post_ops"] == [SILU, MUL]
    assert "post_ops" not in down
    assert workload.group_arguments(gated["layers"]) == (
        ("input", "w_gate", "w_up"),
        ("out_mul",),
    )


def test_only_the_gemms_with_post_ops_narrow_their_embedding():
    kernels = design.mapping(POST_OP_PARTITION, design.GEMM_BLOCKS[0], DIMS[2]).kernels
    assert kernels[GATE]["k"] == kernels[UP]["k"] == design.POST_OP_EMBEDDING
    assert (kernels[DOWN]["m"], kernels[DOWN]["k"], kernels[DOWN]["n"]) == (64, 64, 64)


def test_the_exported_module_computes_what_the_reference_does():
    """The torch module the design is solved from and the numpy reference a run is judged by agree."""
    seq_len, embedding_dim, hidden_dim = 128, 512, 2048
    rng = np.random.default_rng(0)

    def draw(*shape):
        return (rng.standard_normal(shape) * embedding_dim**-0.25).astype(bfloat16)

    x = draw(seq_len, embedding_dim)
    weights = dict(
        w_gate=draw(hidden_dim, embedding_dim),
        w_up=draw(hidden_dim, embedding_dim),
        w_down=draw(embedding_dim, hidden_dim),
    )
    module = design.swiglu_module(embedding_dim, hidden_dim).float()
    module.load_state_dict(
        {name: torch.from_numpy(w.astype(np.float32)) for name, w in weights.items()}
    )
    with torch.no_grad():
        exported = module(torch.from_numpy(x.astype(np.float32))).numpy()
    op = SwiGLUFusedStream(
        seq_len=seq_len, embedding_dim=embedding_dim, hidden_dim=hidden_dim
    )
    verdict = compare(exported, op.reference(x, **weights), op.tolerance())
    assert verdict, verdict.detail
