# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generate the SwiGLU-prefill design with stream-dse.

Both inputs stream-dse needs are produced here, from IRON:

* the **workload**, exported from :mod:`~iron.operators.swiglu_prefill_stream.reference`,
  the same module the test checks the result against;
* the **mapping**, from the placement below.

Both are written into the experiment's output directory at build time, never into
the source tree, and the mapping's node names come from the exported workload, so
the two cannot disagree. stream-dse then solves the allocation and emits the MLIR.

This module is imported lazily (by ``DesignGenerator`` at compile time), so
importing the operator does not require ``stream-dse`` to be installed, only
building it does.
"""

import hashlib
import os
import re
from functools import lru_cache
from pathlib import Path

import stream
import torch
from stream.api import optimize_allocation_co

from iron.operators.swiglu_prefill_stream import reference
from iron.operators.swiglu_prefill_stream.reference import swiglu_module
from iron.operators.swiglu_prefill_stream.stream.hardware import ComputeArray
from iron.operators.swiglu_prefill_stream.stream.mapping import (
    FusedGroup,
    Placement,
    emit_mapping,
    group_boundaries,
)
from iron.operators.swiglu_prefill_stream.stream.workload import export_workload

# Hardware description for the whole-array Strix (npu2) target, shipped as package
# data inside the installed stream package.
ACCELERATOR = os.path.join(
    os.path.dirname(stream.__file__),
    "inputs",
    "aie",
    "hardware",
    "whole_array_strix.yaml",
)

BACKEND = "ortools_gscip"  # license-free OR-Tools GSCIP, no Gurobi needed
OUTPUT_ROOT = "outputs"

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

# The kernel tile each layer is compiled and mapped for, as (sequence, embedding,
# hidden). A core holds the operands of every layer in its group, so the tile a group
# can afford shrinks as more layers fuse onto it. Carrying the tile and no absolute
# dimension is what lets one mapping hold across problem sizes.
FUSED_TILES = (32, 32, 64)  # k=1, k=2: several layers share a core
LAYER_TILES = (64, 64, 64)  # k=5: one layer per core

# Sequence positions an elementwise layer works at a time when it reads from and
# writes to memory. Its tile is then this many whole rows, which is contiguous in
# a row-major tensor, so each transfer runs the length of the rows rather than one
# MAC tile at a time.
ELEMENTWISE_ROWS = 1

# Which layers each fused group contains, per number of groups ``k``. Splitting
# makes stream-dse emit one design per group; the tensor handed from one group to
# the next comes from the exported graph.
LAYER_BY_LAYER = 5
GROUP_LAYERS = {
    1: [[GATE, UP, SILU, MUL, DOWN]],
    2: [[GATE, UP, SILU, MUL], [DOWN]],
    LAYER_BY_LAYER: [[GATE], [UP], [SILU], [MUL], [DOWN]],
}


def tiles_for(k):
    """The kernel tile, as (sequence, embedding, hidden), for ``k`` fused groups."""
    return LAYER_TILES if k == LAYER_BY_LAYER else FUSED_TILES


def gemm_tiles(k):
    """Each GEMM layer's kernel tile, in the (m, k, n) order the kernel takes."""
    sequence, embedding, hidden = tiles_for(k)
    return {
        GATE: (sequence, embedding, hidden),
        UP: (sequence, embedding, hidden),
        DOWN: (sequence, hidden, embedding),
    }


@lru_cache(maxsize=None)
def array() -> ComputeArray:
    """The compute grid of the device being built for."""
    import aie.utils as aie_utils

    return ComputeArray.from_device(aie_utils.get_current_device())


def _placements(k, hidden_dim):
    """Where each layer runs.

    Fused (k=1, k=2): the layers sit on disjoint columns, two per GEMM and one per
    elementwise layer, so they pipeline across steady-state iterations. Each splits
    over the array's rows (D0, the sequence dimension) and a GEMM over its two
    columns as well (D2, the output dimension).

    Layer by layer (k=5): the layers run in turn, so each takes the whole array.
    The GEMMs use every row; the elementwise layers take one core per column and
    split the sequence across them, the shape IRON's channeled operators use. They
    also read whole rows, so their transfers to and from memory are contiguous.
    """
    grid = array()
    sequence_tile, _, hidden_tile = tiles_for(k)
    tiles = gemm_tiles(k)

    def gemm(tiles):
        return dict(
            zip("mkn", tiles), utilization=61.8, layout="default", bfp16_mmul=True
        )

    def elementwise(rows, columns, layout, bfp16_mmul=False):
        return {
            "utilization": 50.0,
            "layout": layout,
            "m": rows,
            "n": columns,
            "bfp16_mmul": bfp16_mmul,
        }

    if k == LAYER_BY_LAYER:
        wide = grid.all_columns
        gemm_split = (("D0", grid.num_rows), ("D2", grid.num_columns))
        elementwise_split = (("D0", grid.num_columns),)
        rows_wide = elementwise(ELEMENTWISE_ROWS, hidden_dim, "contiguous")
        return {
            GATE: Placement(wide, gemm_split, gemm(tiles[GATE])),
            UP: Placement(wide, gemm_split, gemm(tiles[UP])),
            SILU: Placement(wide, elementwise_split, rows_wide, rows=[0]),
            MUL: Placement(wide, elementwise_split, rows_wide, rows=[0]),
            DOWN: Placement(wide, gemm_split, gemm(tiles[DOWN])),
        }

    columns = dict(zip(NODE_NAMES, grid.allocate([2, 2, 1, 1, 2])))
    gemm_split = (("D0", grid.num_rows), ("D2", 2))
    elementwise_split = (("D0", grid.num_rows),)
    # Fused behind a GEMM, so the operands take the layout that GEMM writes.
    fused = elementwise(sequence_tile, hidden_tile, "default", bfp16_mmul=True)
    return {
        GATE: Placement(columns[GATE], gemm_split, gemm(tiles[GATE])),
        UP: Placement(columns[UP], gemm_split, gemm(tiles[UP])),
        SILU: Placement(columns[SILU], elementwise_split, fused),
        MUL: Placement(columns[MUL], elementwise_split, fused),
        DOWN: Placement(columns[DOWN], gemm_split, gemm(tiles[DOWN])),
    }


def _layer_tiling(layer, hidden_dim, k):
    """Intra-core tiling of one layer, over the dimensions it iterates."""
    if layer not in (GATE, UP, DOWN):
        return [(layer, "D1", hidden_dim), (layer, "D0", ELEMENTWISE_ROWS)]
    sequence, contraction, output = gemm_tiles(k)[layer]
    return [
        (layer, "D1", contraction),
        (layer, "D2", output),
        (layer, "D0", sequence),
    ]


def _groups(k, hidden_dim):
    """The fused groups, each with the intra-core tiling of its leading GEMM.

    Splitting makes stream-dse emit one design per group, which IRON then deploys
    as a single full ELF. D0 is the sequence dimension, D1 the contraction and D2
    the output dimension.
    """
    sequence_tile, embedding_tile, hidden_tile = tiles_for(k)
    if k == LAYER_BY_LAYER:
        tiling = [_layer_tiling(layers[0], hidden_dim, k) for layers in GROUP_LAYERS[k]]
    elif k == 2:
        tiling = [
            _layer_tiling(GATE, hidden_dim, k),
            _layer_tiling(DOWN, hidden_dim, k),
        ]
    else:
        tiling = [
            [
                (GATE, "D1", embedding_tile),
                (DOWN, "D2", embedding_tile),
                (GATE, "D2", hidden_tile),
                (GATE, "D0", sequence_tile),
            ]
        ]
    return [
        FusedGroup(f"Fused_Group_{index + 1}", layers, group_tiling)
        for index, (layers, group_tiling) in enumerate(zip(GROUP_LAYERS[k], tiling))
    ]


def _check_shapes(seq_len, embedding_dim, hidden_dim, k):
    """Reject a problem size the placement and the kernel tiles cannot divide."""
    grid = array()
    sequence_tile, embedding_tile, hidden_tile = tiles_for(k)
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


def group_ports(seq_len, embedding_dim, hidden_dim, k=1):
    """Per fused group, the tensor names it takes in and hands on.

    These are the operator's runtime arguments, including the tensors a split
    design passes from one group to the next.
    """
    return group_boundaries(
        workload_for(seq_len, embedding_dim, hidden_dim), GROUP_LAYERS[k]
    )


def build_inputs(seq_len, embedding_dim, hidden_dim, output_dir, k=1):
    """Write the workload and mapping for one configuration; return their paths."""
    _check_shapes(seq_len, embedding_dim, hidden_dim, k)
    workload = workload_for(seq_len, embedding_dim, hidden_dim)
    output_dir = Path(output_dir)
    return (
        workload.write(output_dir / "workload.onnx"),
        emit_mapping(
            workload,
            _placements(k, hidden_dim),
            _groups(k, hidden_dim),
            array(),
            output_dir / "mapping.yaml",
        ),
    )


def _experiment_id(seq_len, embedding_dim, hidden_dim, k):
    grid = array()
    hardware = os.path.splitext(os.path.basename(ACCELERATOR))[0]
    suffix = f"_k{k}" if k > 1 else ""
    if trace_size():
        suffix += "_traced"
    return (
        f"{hardware}-swiglu{suffix}_{seq_len}_{embedding_dim}_{hidden_dim}"
        f"-{grid.num_rows}_row_{grid.num_columns}_col"
    )


def trace_size():
    """DDR trace buffer in bytes, 0 for an untraced build.

    Opt-in: tracing adds a runtime-sequence argument, so it changes the ABI.
    """
    return int(os.environ.get("IRON_TRACE_SIZE", "0"))


def trace_tiles():
    """How many tiles to trace. Routing capacity sets the practical limit."""
    return int(os.environ.get("IRON_TRACE_NTILES", "4"))


def _design_paths(seq_len, embedding_dim, hidden_dim, k):
    """Where stream-dse writes each group's MLIR.

    A single fused group goes through stream-dse's single-design pipeline and lands
    in ``codegen/``; several groups each land in their own ``group_i/codegen/``.
    """
    output_dir = os.path.join(
        OUTPUT_ROOT, _experiment_id(seq_len, embedding_dim, hidden_dim, k)
    )
    if k == 1:
        return [os.path.join(output_dir, "codegen", "final.mlir")]
    return [
        os.path.join(output_dir, f"group_{index}", "codegen", "final.mlir")
        for index in range(len(GROUP_LAYERS[k]))
    ]


def _run_codegen(seq_len, embedding_dim, hidden_dim, npu, k):
    """Run stream-dse's constraint optimization and code generation once."""
    grid = array()
    experiment_id = _experiment_id(seq_len, embedding_dim, hidden_dim, k)
    workload_path, mapping_path = build_inputs(
        seq_len,
        embedding_dim,
        hidden_dim,
        os.path.join(OUTPUT_ROOT, experiment_id),
        k=k,
    )
    optimize_allocation_co(
        hardware=ACCELERATOR,
        workload=workload_path,
        mapping=mapping_path,
        experiment_id=experiment_id,
        output_path=OUTPUT_ROOT,
        skip_if_exists=False,
        enable_codegen=True,
        trace_size=trace_size(),
        trace_max_tiles=trace_tiles(),
        nb_cols_to_use=grid.num_columns,
        npu=npu,
        backend=BACKEND,
    )


def region_module(mlir_text: str, renames: dict | None = None):
    """Parse a group's MLIR text into an ``aie`` module for fusion.

    ``OperatorSequence`` consumes ``aie.DeviceOp`` objects, so the xDSL-emitted
    group text is re-parsed with the mlir-aie bindings.

    Fused, groups keep the names they were generated with: every object name
    here already carries what distinguishes its recipe (``mm_<m>_<k>_<n>.o``),
    and groups that name one object build it identically, so they share it.
    """
    from aie import ir
    from aie.extras.context import mlir_mod_ctx

    with mlir_mod_ctx():
        return ir.Module.parse(_renamed(mlir_text, renames))


def _renamed(mlir_text: str, renames: dict | None) -> str:
    """Point the generated design at the symbols the objects actually define.

    stream-dse suffixes a GEMM's symbols with its tile shape so several shapes
    coexist in one design. ExternalFunction can only prefix, so the objects end
    up prefixed instead and the text is rewritten to agree.
    """
    if not renames:
        return mlir_text
    for old, new in sorted(renames.items(), key=lambda kv: len(kv[0]), reverse=True):
        mlir_text = re.sub(rf"@{re.escape(old)}\b", f"@{new}", mlir_text)
    return mlir_text


def _group_text(group_index, *, k, seq_len, embedding_dim, hidden_dim, npu) -> str:
    """One group's generated MLIR, before any symbol renames."""
    finals = _design_paths(seq_len, embedding_dim, hidden_dim, k)
    if not all(os.path.exists(final) for final in finals):
        _run_codegen(seq_len, embedding_dim, hidden_dim, npu, k)
    return Path(finals[group_index]).read_text()


def group_digest(group_index, **dims) -> str:
    """Digest of a group's design, for recognising groups that share one."""
    return hashlib.sha256(_group_text(group_index, **dims).encode()).hexdigest()


def load_group(
    *,
    group_index,
    k,
    seq_len,
    embedding_dim,
    hidden_dim,
    npu,
    kernels_dir,
):
    """Generate the ``k``-group design once and return one group's aie module.

    ``group_index`` selects the group, in the order :data:`GROUP_LAYERS` lists
    them, and is keyword-only like the rest: the compile cache keys on a
    design's parameters by name, so a positional one would not reach the key.
    Every group loader calls this; the first generates the design and the rest
    reuse the files on disk.

    The kernels are declared here rather than by the operator because an
    ExternalFunction registers into a process-global set that CompilableDesign
    clears when it begins generating; one built earlier is discarded and its
    object never compiled.
    """
    renames = declare_group_kernels(group_index, k=k, kernels_dir=kernels_dir)
    text = _group_text(
        group_index,
        k=k,
        seq_len=seq_len,
        embedding_dim=embedding_dim,
        hidden_dim=hidden_dim,
        npu=npu,
    )
    return region_module(text, renames=renames)


def declare_group_kernels(group_index, *, k, kernels_dir) -> dict:
    """Compile every kernel this group runs; return the symbol renames forced.

    The registry is the single place a kernel's source, compile flags and
    symbol names are declared, so the object and the generated design agree.
    """
    from iron.common.kernels import target_arch
    from iron.operators.swiglu_prefill_stream.stream.ops import ELTWISE_MUL, GEMM, SILU

    tiles = gemm_tiles(k)
    per_layer = {
        GATE: (GEMM, tiles[GATE]),
        UP: (GEMM, tiles[UP]),
        DOWN: (GEMM, tiles[DOWN]),
        SILU: (SILU, None),
        MUL: (ELTWISE_MUL, None),
    }
    kernels_dir = Path(kernels_dir)
    kernel_dir = target_arch()
    renames = {}
    layers = GROUP_LAYERS[k][group_index]
    for kernel, shape in dict.fromkeys(per_layer[layer] for layer in layers):
        renames.update(
            kernel.declare_kernels(
                kernels_dir,
                kernel_dir,
                **(dict(zip("mkn", shape)) if shape else {}),
            )
        )
    return renames
