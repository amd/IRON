# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generate the SwiGLU-prefill design with stream-dse.

The workload is exported from :mod:`~iron.operators.swiglu_prefill_stream.reference` and
the mapping from each layer's kernel arguments, both into the experiment's output
directory; the mapping's node names come from the workload. Imported lazily at build."""

import json
import logging
from functools import lru_cache
from pathlib import Path

import torch

from iron.common.stream.design import (
    design_paths,
    digest,
    group_text,
    region_module,
)
from iron.common.stream.hardware import array
from iron.common.stream.runner import (
    design_dir,
    experiment_id,
    run_codegen,
    run_partition_codegen,
)
from iron.common.stream.mapping import (
    FusedGroup,
    emit_mapping,
    group_boundaries,
)
from iron.common.stream.workload import export_workload
from iron.operators.swiglu_prefill_stream import reference
from iron.operators.swiglu_prefill_stream.reference import swiglu_module

# Names for the exported graph's computation nodes, in topological order, and for
# the tensors they produce. They name the roles rather than the ATen ops the
# exporter captured, and they are what the mapping and the generated design are
# read by.
GATE, UP, SILU, MUL, DOWN = "Gemm_Left", "Gemm_Right", "Silu", "Elt_Mul", "Gemm_Down"
NODE_NAMES = [GATE, UP, SILU, MUL, DOWN]
RESULT_NAMES = {
    GATE: reference.GATE_PROJECTION,
    UP: reference.UP_PROJECTION,
    SILU: reference.ACTIVATION,
    MUL: reference.HIDDEN,
}

# GEMM blocks as (sequence, embedding, hidden), tried largest first until stream's solve fits one.
GEMM_BLOCKS = ((64, 64, 64), (32, 32, 64))

# The widest row an elementwise layer holds three operands of; it must divide the dimension.
ELEMENTWISE_WIDTH = 2048

logger = logging.getLogger(__name__)

# Which layers each fused group contains, per number of groups ``k``. Splitting
# makes stream-dse emit one design per group; the tensor handed from one group to
# the next comes from the exported graph.
LAYER_BY_LAYER = 5
GROUP_LAYERS = {
    1: [[GATE, UP, SILU, MUL, DOWN]],
    2: [[GATE, UP, SILU, MUL], [DOWN]],
    LAYER_BY_LAYER: [[GATE], [UP], [SILU], [MUL], [DOWN]],
}


def gemm_blocks(block):
    """Each GEMM layer's compiled block, in the (m, k, n) order the kernel takes."""
    sequence, embedding, hidden = block
    return {
        GATE: (sequence, embedding, hidden),
        UP: (sequence, embedding, hidden),
        DOWN: (sequence, hidden, embedding),
    }


def _row_width(hidden_dim):
    """How much of a row an elementwise core takes at once: the whole row where it fits,
    and otherwise the widest piece that divides it."""
    if hidden_dim <= ELEMENTWISE_WIDTH:
        return hidden_dim
    return max(w for w in range(ELEMENTWISE_WIDTH, 0, -1) if hidden_dim % w == 0)


def partition_layers(seq_len, embedding_dim, hidden_dim, npu, k, gemm_block=None):
    """The layers of each fused group: declared for an explicit ``k``; for ``None``, the
    partition stream prices cheapest (solve plus dispatch overhead), from ``partition.json``.
    """
    if k is not None:
        return GROUP_LAYERS[k]
    eid = _experiment_id(seq_len, embedding_dim, hidden_dim, k, gemm_block)
    marker = Path(design_dir(eid)) / "partition.json"
    if not marker.exists():
        _run_codegen(seq_len, embedding_dim, hidden_dim, npu, k, gemm_block)
    return [list(group) for group in json.loads(marker.read_text())["groups"]]


def _kernel_kwargs(k, hidden_dim, block):
    """Each layer's kernel arguments. Split per layer, the elementwise kernels read whole
    rows so their transfers are contiguous; fused behind a GEMM they take its output block.
    """
    tiles = gemm_blocks(block)

    def gemm(block):
        return dict(zip("mkn", block), layout="default")

    if k == LAYER_BY_LAYER:
        wide = elementwise(1, _row_width(hidden_dim), "contiguous")
        elementwise_kwargs = {SILU: wide, MUL: wide}
    else:
        sequence_tile, _, hidden_tile = block
        fused = elementwise(sequence_tile, hidden_tile, "default")
        elementwise_kwargs = {SILU: fused, MUL: fused}
    return {
        GATE: gemm(tiles[GATE]),
        UP: gemm(tiles[UP]),
        SILU: elementwise_kwargs[SILU],
        MUL: elementwise_kwargs[MUL],
        DOWN: gemm(tiles[DOWN]),
    }


def elementwise(rows, columns, layout):
    return {"layout": layout, "m": rows, "n": columns}


def _groups(k):
    """The fused groups. Their tiling is the kernels' granules, derived by stream."""
    return [
        FusedGroup(f"Fused_Group_{index + 1}", layers)
        for index, layers in enumerate(GROUP_LAYERS[k])
    ]


def _check_shapes(seq_len, embedding_dim, hidden_dim, k):
    """Reject a problem size no compiled block can divide."""
    grid = array()
    sequence_tile, embedding_tile, hidden_tile = GEMM_BLOCKS[-1]
    gemm_split = grid.num_columns if k == LAYER_BY_LAYER else 2
    if seq_len % grid.num_rows or seq_len < sequence_tile * grid.num_rows:
        raise ValueError(
            f"seq_len ({seq_len}) must be a multiple of {grid.num_rows} and at "
            f"least {sequence_tile * grid.num_rows}"
        )
    if embedding_dim % (embedding_tile * gemm_split):
        raise ValueError(
            f"embedding_dim ({embedding_dim}) must be a multiple of "
            f"{embedding_tile * gemm_split}"
        )
    if hidden_dim % (hidden_tile * gemm_split):
        raise ValueError(
            f"hidden_dim ({hidden_dim}) must be a multiple of "
            f"{hidden_tile * gemm_split}"
        )


@lru_cache(maxsize=None)
def workload_for(seq_len, embedding_dim, hidden_dim):
    """The exported workload for one problem size."""
    return export_workload(
        swiglu_module(embedding_dim, hidden_dim),
        (torch.zeros(seq_len, embedding_dim, dtype=torch.bfloat16),),
        node_names=NODE_NAMES,
        result_names=RESULT_NAMES,
    )


def group_ports(seq_len, embedding_dim, hidden_dim, k=1, npu="npu2", gemm_block=None):
    """Per fused group, the tensor names it takes in and hands on.

    These are the operator's runtime arguments, including the tensors a split
    design passes from one group to the next.
    """
    return group_boundaries(
        workload_for(seq_len, embedding_dim, hidden_dim),
        partition_layers(seq_len, embedding_dim, hidden_dim, npu, k, gemm_block),
    )


def build_inputs(
    seq_len, embedding_dim, hidden_dim, output_dir, k=1, block=GEMM_BLOCKS[-1]
):
    """Write the workload and mapping for one configuration; return their paths."""
    _check_shapes(seq_len, embedding_dim, hidden_dim, k)
    workload = workload_for(seq_len, embedding_dim, hidden_dim)
    output_dir = Path(output_dir)
    return (
        workload.write(output_dir / "workload.onnx"),
        emit_mapping(
            workload,
            _kernel_kwargs(k, hidden_dim, block),
            _groups(k),
            output_dir / "mapping.yaml",
        ),
    )


def _blocks(gemm_block):
    """The GEMM blocks a build may take, largest first: only the caller's when pinned."""
    return GEMM_BLOCKS if gemm_block is None else (tuple(gemm_block),)


def _experiment_id(seq_len, embedding_dim, hidden_dim, k, gemm_block=None):
    suffix = "_kauto" if k is None else (f"_k{k}" if k > 1 else "")
    if gemm_block is not None:
        suffix += f"_b{'x'.join(map(str, gemm_block))}"
    return experiment_id("swiglu", f"{seq_len}_{embedding_dim}_{hidden_dim}", suffix)


def _run_codegen(seq_len, embedding_dim, hidden_dim, npu, k, gemm_block=None):
    """Build with the largest block the solve accepts; the last candidate must hold.
    With ``k=None`` every allowed (partition, block) pair is a candidate stream picks from.
    """
    eid = _experiment_id(seq_len, embedding_dim, hidden_dim, k, gemm_block)
    blocks = _blocks(gemm_block)
    if k is None:
        base = Path(design_dir(eid))
        candidates, errors = [], []
        for candidate_k in (1, LAYER_BY_LAYER):
            for block in blocks:
                candidate_dir = (
                    base / f"candidate_k{candidate_k}_b{'x'.join(map(str, block))}"
                )
                try:
                    workload_path, mapping_path = build_inputs(
                        seq_len,
                        embedding_dim,
                        hidden_dim,
                        candidate_dir,
                        k=candidate_k,
                        block=block,
                    )
                except ValueError as error:
                    errors.append(error)
                    continue
                candidates.append(mapping_path)
        if not candidates:
            raise errors[-1]
        import yaml

        chosen = run_partition_codegen(eid, workload_path, candidates, npu)
        groups = yaml.safe_load(Path(candidates[chosen]).read_text())["fused_groups"]
        (base / "partition.json").write_text(
            json.dumps({"groups": [group["layers"] for group in groups]})
        )
        return
    for block in blocks:
        workload_path, mapping_path = build_inputs(
            seq_len, embedding_dim, hidden_dim, design_dir(eid), k=k, block=block
        )
        try:
            run_codegen(eid, workload_path, mapping_path, npu)
        except RuntimeError as error:
            if block == blocks[-1]:
                raise
            logger.info("Block %s does not fit (%s); trying the next", block, error)
            continue
        return


def design_root(*, k, seq_len, embedding_dim, hidden_dim, npu, gemm_block=None):
    """The directory stream writes this design and its estimate to."""
    return design_dir(_experiment_id(seq_len, embedding_dim, hidden_dim, k, gemm_block))


def _design_paths(seq_len, embedding_dim, hidden_dim, k, npu, gemm_block=None):
    return design_paths(
        design_dir(_experiment_id(seq_len, embedding_dim, hidden_dim, k, gemm_block)),
        len(partition_layers(seq_len, embedding_dim, hidden_dim, npu, k, gemm_block)),
    )


def _group_text(
    group_index, *, k, seq_len, embedding_dim, hidden_dim, npu, gemm_block=None
) -> str:
    return group_text(
        group_index,
        _design_paths(seq_len, embedding_dim, hidden_dim, k, npu, gemm_block),
        lambda: _run_codegen(seq_len, embedding_dim, hidden_dim, npu, k, gemm_block),
    )


def group_digest(group_index, **dims) -> str:
    """Digest of a group's design, for recognising groups that share one."""
    return digest(_group_text(group_index, **dims))


def load_group(group_index, func_prefix="", **dims):
    """Generate the ``k``-group design once and return group ``group_index``'s aie module;
    ``func_prefix`` is injected by ``OperatorSequence``."""
    return region_module(_group_text(group_index, **dims), func_prefix)
