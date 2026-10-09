# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""stream-dse design for the prefill attention core of every head. The workload and
mapping come from :mod:`iron.operators.mha_prefill_stream.reference`, so the design, golden
output and runtime arguments share names; placement is stream's to derive."""

from functools import lru_cache
from pathlib import Path

import torch

from iron.common.stream.design import (
    design_digest,
    design_paths,
    group_text,
    region_module,
)
from iron.common.stream.hardware import array
from iron.common.stream.kernel_library import (
    fixed_dims,
    load_library,
    pinned_to_block,
)
from iron.common.stream.mapping import (
    FusedGroup,
    emit_mapping,
    group_boundaries,
)
from iron.common.stream.runner import design_dir, experiment_id, run_codegen
from iron.common.stream.workload import export_workload
from iron.operators.mha_prefill_stream.reference import (
    CONTEXT_NODE,
    NODE_NAMES,
    RESULT_NAMES,
    SCORES_NODE,
    SOFTMAX_NODE,
    attention_core_module,
)

LAYER_BY_LAYER = 3

_KEY_BLOCK = 64

FLASH_BLOCK = fixed_dims("matmul_PV", "aie2p")["k"]

FLASH_MAX_SEQ = 8192

FUSED_QUERY_TILE = 16

CORE_BYTES = 64 * 1024
BYTES_PER_ELEMENT = 2


SWEEP_POINTS = [
    dict(seq_len=s, d_head=FLASH_BLOCK, heads=32, flash=True)
    for s in (64, 128, 256, 512, 1024, 2048, 4096, 8192)
]


def flash_blocks(kernel_dir: str | None = None) -> tuple[int, ...]:
    """Query blocks the online-softmax source compiles for, finest first."""
    blocks = load_library(kernel_dir).spec("partial_softmax").dim("m").blocks
    return tuple(sorted(blocks))


def sweep_candidates() -> list[dict]:
    """The designs stream chooses between at a sweep point, as constructor kwargs."""
    return [dict(query_block=block) for block in flash_blocks()]


def flash_query_seed(query_block=None) -> int:
    """The query block a flash mapping's search starts at: the caller's when pinned,
    otherwise the finest one the kernels compile for."""
    return query_block or min(flash_blocks())


def key_tile(seq_len, k, flash=False):
    if flash:
        return FLASH_BLOCK
    return seq_len if k == 1 else _KEY_BLOCK


def group_layers(k) -> list:
    """The layers of each of the ``k`` fused groups, in the order the groups run."""
    return {
        1: [[SCORES_NODE, SOFTMAX_NODE, CONTEXT_NODE]],
        LAYER_BY_LAYER: [[SCORES_NODE], [SOFTMAX_NODE], [CONTEXT_NODE]],
    }[k]


def query_per_core(seq_len):
    """Query positions one core holds when a layer has a column to itself."""
    return seq_len // array().num_rows


def query_tile(seq_len, k, flash=False, query_block=None):
    """Query positions one core works at a time: split off, its whole slice (the lowering
    has one reuse variable per window); fused, a tile beside the resident key and value;
    flash, the searched block."""
    if flash:
        return flash_query_seed(query_block)
    return FUSED_QUERY_TILE if k == 1 else query_per_core(seq_len)


def _softmax_rows(seq_len, k, flash=False, query_block=None):
    """Query rows one softmax call normalizes. Fused, the group's layers share one query
    tile and the kernel loops the rows of it; split off, the tile is a single row."""
    return query_tile(seq_len, k, flash, query_block) if k == 1 else 1


def _scores_tile(seq_len, d_head, k, flash=False, query_block=None):
    """The score GEMM's (m, k, n), of which one dimension iterates. Fused, the softmax
    needs whole rows, so the query streams; split off, the key streams while it spans more
    than a block, otherwise the contraction."""
    if flash:
        return flash_query_seed(query_block), d_head, FLASH_BLOCK
    query, key = query_tile(seq_len, k), seq_len
    if k == 1:
        return query, d_head, seq_len
    if key > _KEY_BLOCK:
        return query, d_head, _KEY_BLOCK
    return query, d_head // 2, key


def kernel_tiles(seq_len, d_head, k, flash=False, query_block=None):
    """Each GEMM layer's kernel tile, in the (m, k, n) order the kernel takes. The
    kernel tile and the intra-core tile are the same tile, so they are declared once."""
    return {
        SCORES_NODE: _scores_tile(seq_len, d_head, k, flash, query_block),
        CONTEXT_NODE: (
            query_tile(seq_len, k, flash, query_block),
            key_tile(seq_len, k, flash),
            d_head,
        ),
    }


def _kernel_kwargs(seq_len, d_head, k, causal, flash=False, query_block=None):
    """Each layer's kernel arguments; where the layers run is stream's to derive."""
    tiles = kernel_tiles(seq_len, d_head, k, flash, query_block)

    def gemm(m, contraction, n):
        return dict(m=m, k=contraction, n=n, layout="default")

    softmax = dict(
        m=_softmax_rows(seq_len, k, flash, query_block),
        n=FLASH_BLOCK if flash else seq_len,
        layout="contiguous",
    )
    scores, context = gemm(*tiles[SCORES_NODE]), gemm(*tiles[CONTEXT_NODE])
    if flash:
        scores["causal"] = True
        context["flash"] = True
    elif causal:
        softmax["causal"] = True
    return {SCORES_NODE: scores, SOFTMAX_NODE: softmax, CONTEXT_NODE: context}


def _groups(k):
    """The fused groups. Their tiling is the kernels' granules, derived by stream:
    innermost first, the carried key leading under flash."""
    return [
        FusedGroup(f"Fused_Group_{index + 1}", layers)
        for index, layers in enumerate(group_layers(k))
    ]


def _check_shapes(seq_len, d_head, k, flash=False):
    if flash:
        if k != 1:
            raise ValueError("flash attention is generated as one fused group, so k=1")
        if d_head != FLASH_BLOCK:
            raise ValueError(
                f"mha.cc's flash kernels reuse the score GEMM's compiled block, which "
                f"holds only when d_head is {FLASH_BLOCK}, not {d_head}"
            )
        if seq_len % FLASH_BLOCK or seq_len > FLASH_MAX_SEQ:
            raise ValueError(
                f"seq_len {seq_len} must be a multiple of the {FLASH_BLOCK} key block "
                f"and at most {FLASH_MAX_SEQ}"
            )
        return
    for name, extent, split in (
        ("query", seq_len, array().num_rows),
        ("head", d_head, 1),
    ):
        if extent % split or (extent // split) % 16:
            raise ValueError(
                f"{name} {extent} split {split} ways is not a multiple of 16 per core"
            )
    if seq_len % _KEY_BLOCK:
        raise ValueError(f"seq_len {seq_len} must be a multiple of {_KEY_BLOCK}")
    if k == 1:
        query = FUSED_QUERY_TILE
        resident = BYTES_PER_ELEMENT * (
            d_head * seq_len + 2 * query * d_head + 2 * query * seq_len
        )
        if resident > CORE_BYTES:
            raise ValueError(
                f"the fused score core needs {resident} bytes, over the {CORE_BYTES} "
                f"byte core; block the key dimension to go further"
            )


@lru_cache(maxsize=None)
def workload_for(seq_len, d_head, heads=1, flash=False):
    """The exported workload for one problem size, its leading axis the heads."""

    def zeros(*shape):
        return torch.zeros((heads, *shape), dtype=torch.bfloat16)

    return export_workload(
        attention_core_module(flash=flash),
        (zeros(seq_len, d_head), zeros(d_head, seq_len), zeros(seq_len, d_head)),
        node_names=NODE_NAMES,
        result_names=RESULT_NAMES,
    )


def build_inputs(
    seq_len,
    d_head,
    output_dir,
    heads=1,
    k=LAYER_BY_LAYER,
    causal=False,
    flash=False,
    query_block=None,
):
    """Write the workload and mapping for one configuration; return their paths."""
    _check_shapes(seq_len, d_head, k, flash)
    workload = workload_for(seq_len, d_head, heads, flash)
    output_dir = Path(output_dir)
    return (
        workload.write(output_dir / "workload.onnx"),
        emit_mapping(
            workload,
            _kernel_kwargs(seq_len, d_head, k, causal, flash, query_block),
            _groups(k),
            output_dir / "mapping.yaml",
        ),
    )


def _experiment_id(*, k, seq_len, d_head, heads, causal, flash, query_block=None):
    suffix = f"_k{k}" if k != LAYER_BY_LAYER else ""
    if flash:
        suffix += "_flash" if query_block is None else f"_flash_q{query_block}"
    elif causal:
        suffix += "_causal"
    return experiment_id("mha", f"{heads}_{seq_len}_{d_head}", suffix)


def design_root(**dims):
    """The directory stream writes this design and its estimate to."""
    return design_dir(_experiment_id(**dims))


def _run_codegen(npu, query_block=None, **dims):
    """Run stream-dse's constraint optimization and code generation once."""
    experiment = _experiment_id(query_block=query_block, **dims)
    workload_path, mapping_path = build_inputs(
        output_dir=design_dir(experiment), query_block=query_block, **dims
    )
    library = None if query_block is None else pinned_to_block(query_block)
    run_codegen(experiment, workload_path, mapping_path, npu, library)


def _group_text(group_index, npu, **dims) -> str:
    return group_text(
        group_index,
        design_paths(design_root(**dims), len(group_layers(dims["k"]))),
        lambda: _run_codegen(npu, **dims),
    )


def group_ports(seq_len, d_head, heads=1, k=LAYER_BY_LAYER):
    """Per fused group, the tensor names it takes in and hands on, read off the plain
    graph, whose three nodes the flash graph shares."""
    return group_boundaries(workload_for(seq_len, d_head, heads), group_layers(k))


def group_digest(group_index, **dims) -> str:
    """Digest of a group's design, for recognising groups that share one."""
    return design_digest(_group_text(group_index, **dims))


def load_group(group_index, **dims):
    """Generate the ``k``-group design once and return one group's aie module."""
    return region_module(_group_text(group_index, **dims))
