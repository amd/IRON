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

import os
import re
from functools import lru_cache
from pathlib import Path

import stream
import torch
from stream.api import optimize_allocation_co

from iron.common.stream.hardware import ComputeArray
from iron.common.stream.mapping import (
    FusedGroup,
    Placement,
    emit_mapping,
    group_boundaries,
)
from iron.common.stream.workload import export_workload
from iron.operators.swiglu_prefill_stream import reference
from iron.operators.swiglu_prefill_stream.reference import swiglu_module

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

# The kernel tile every layer is compiled and mapped for. The mapping carries these
# and no absolute dimension, so it holds across problem sizes; _check_shapes rejects
# a workload they cannot tile evenly.
SEQ_TILE, EMBEDDING_TILE, HIDDEN_TILE = 32, 32, 64
GATE_UP_TILES = (SEQ_TILE, EMBEDDING_TILE, HIDDEN_TILE)
DOWN_TILES = (SEQ_TILE, HIDDEN_TILE, EMBEDDING_TILE)

# Sequence positions an elementwise layer works at a time when it reads from and
# writes to memory. Its tile is then this many whole rows, which is contiguous in
# a row-major tensor, so each transfer runs the length of the rows rather than one
# MAC tile at a time.
ELEMENTWISE_ROWS = 1

# Which layers each fused group contains, per number of groups ``k``. Splitting
# makes stream-dse emit one design per group; the tensor handed from one to the
# next is derived from the exported graph, not named here. k=5 is layer by layer,
# every layer its own design, as in :mod:`iron.operators.swiglu_prefill`.
LAYER_BY_LAYER = 5
GROUP_LAYERS = {
    1: [[GATE, UP, SILU, MUL, DOWN]],
    2: [[GATE, UP, SILU, MUL], [DOWN]],
    LAYER_BY_LAYER: [[GATE], [UP], [SILU], [MUL], [DOWN]],
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

    def gemm(tiles):
        return dict(zip("mkn", tiles), utilization=61.8, layout="default")

    def elementwise(rows, columns, layout):
        return {"utilization": 50.0, "layout": layout, "m": rows, "n": columns}

    if k == LAYER_BY_LAYER:
        wide = grid.all_columns
        gemm_split = (("D0", grid.num_rows), ("D2", grid.num_columns))
        elementwise_split = (("D0", grid.num_columns),)
        rows_wide = elementwise(ELEMENTWISE_ROWS, hidden_dim, "contiguous")
        return {
            GATE: Placement(wide, gemm_split, gemm(GATE_UP_TILES)),
            UP: Placement(wide, gemm_split, gemm(GATE_UP_TILES)),
            SILU: Placement(wide, elementwise_split, rows_wide, rows=[0]),
            MUL: Placement(wide, elementwise_split, rows_wide, rows=[0]),
            DOWN: Placement(wide, gemm_split, gemm(DOWN_TILES)),
        }

    columns = dict(zip(NODE_NAMES, grid.allocate([2, 2, 1, 1, 2])))
    gemm_split = (("D0", grid.num_rows), ("D2", 2))
    elementwise_split = (("D0", grid.num_rows),)
    # Fused behind a GEMM, so the operands keep the layout the GEMM writes.
    fused = elementwise(SEQ_TILE, HIDDEN_TILE, "default")
    return {
        GATE: Placement(columns[GATE], gemm_split, gemm(GATE_UP_TILES)),
        UP: Placement(columns[UP], gemm_split, gemm(GATE_UP_TILES)),
        SILU: Placement(columns[SILU], elementwise_split, fused),
        MUL: Placement(columns[MUL], elementwise_split, fused),
        DOWN: Placement(columns[DOWN], gemm_split, gemm(DOWN_TILES)),
    }


def _layer_tiling(layer, hidden_dim):
    """Intra-core tiling of one layer, over the dimensions it iterates."""
    if layer is DOWN:
        contraction, output = HIDDEN_TILE, EMBEDDING_TILE
    elif layer in (GATE, UP):
        contraction, output = EMBEDDING_TILE, HIDDEN_TILE
    else:
        return [(layer, "D1", hidden_dim), (layer, "D0", ELEMENTWISE_ROWS)]
    return [
        (layer, "D1", contraction),
        (layer, "D2", output),
        (layer, "D0", SEQ_TILE),
    ]


def _groups(k, hidden_dim):
    """The fused groups, each with the intra-core tiling of its leading GEMM.

    Splitting makes stream-dse emit one design per group, which IRON then deploys
    as a single full ELF. D0 is the sequence dimension, D1 the contraction and D2
    the output dimension.
    """
    if k == LAYER_BY_LAYER:
        tiling = [_layer_tiling(layers[0], hidden_dim) for layers in GROUP_LAYERS[k]]
    elif k == 2:
        tiling = [_layer_tiling(GATE, hidden_dim), _layer_tiling(DOWN, hidden_dim)]
    else:
        tiling = [
            [
                (GATE, "D1", EMBEDDING_TILE),
                (DOWN, "D2", EMBEDDING_TILE),
                (GATE, "D2", HIDDEN_TILE),
                (GATE, "D0", SEQ_TILE),
            ]
        ]
    return [
        FusedGroup(f"Fused_Group_{index + 1}", layers, group_tiling)
        for index, (layers, group_tiling) in enumerate(zip(GROUP_LAYERS[k], tiling))
    ]


def _check_shapes(seq_len, embedding_dim, hidden_dim, k):
    """Reject a problem size the placement and the kernel tiles cannot divide."""
    grid = array()
    gemm_split = grid.num_columns if k == LAYER_BY_LAYER else 2
    if seq_len % grid.num_rows or seq_len < SEQ_TILE * grid.num_rows:
        raise ValueError(
            f"seq_len ({seq_len}) must be a multiple of {grid.num_rows} and at "
            f"least {SEQ_TILE * grid.num_rows}"
        )
    if embedding_dim % (EMBEDDING_TILE * gemm_split):
        raise ValueError(
            f"embedding_dim ({embedding_dim}) must be a multiple of "
            f"{EMBEDDING_TILE * gemm_split}"
        )
    if hidden_dim % (HIDDEN_TILE * gemm_split):
        raise ValueError(
            f"hidden_dim ({hidden_dim}) must be a multiple of "
            f"{HIDDEN_TILE * gemm_split}"
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
    return (
        f"{hardware}-swiglu{suffix}_{seq_len}_{embedding_dim}_{hidden_dim}"
        f"-{grid.num_rows}_row_{grid.num_columns}_col"
    )


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
        trace_size=0,
        nb_cols_to_use=grid.num_columns,
        npu=npu,
        backend=BACKEND,
    )


def _prefixed(mlir_text: str, func_prefix: str) -> str:
    """Apply a fused-operator ``func_prefix`` (``op<idx>_``) to a group's MLIR.

    ``OperatorSequence`` renames each child's kernel object files and symbols to
    ``op<idx>_...`` so the groups stay distinct inside one ELF; the group's MLIR
    must reference the same prefixed names. Prefix the ``link_with`` object files
    and every privately declared kernel symbol, and its call sites.
    """
    if not func_prefix:
        return mlir_text
    mlir_text = re.sub(
        r'link_with\s*=\s*"([^"]+)"',
        lambda m: f'link_with = "{func_prefix}{m.group(1)}"',
        mlir_text,
    )
    symbols = sorted(
        set(re.findall(r"func\.func\s+private\s+@([A-Za-z0-9_]+)", mlir_text)),
        key=len,
        reverse=True,
    )
    for symbol in symbols:
        mlir_text = re.sub(
            rf"@{re.escape(symbol)}\b", f"@{func_prefix}{symbol}", mlir_text
        )
    return mlir_text


def region_module(mlir_text: str, func_prefix: str = ""):
    """Parse a group's MLIR text into an ``aie`` module for fusion.

    ``OperatorSequence`` consumes ``aie.DeviceOp`` objects, so the xDSL-emitted
    group text is re-parsed with the mlir-aie bindings, after ``func_prefix``
    rewriting.
    """
    from aie import ir
    from aie.extras.context import mlir_mod_ctx

    with mlir_mod_ctx():
        return ir.Module.parse(_prefixed(mlir_text, func_prefix))


def load_group(
    group_index, func_prefix="", *, k, seq_len, embedding_dim, hidden_dim, npu
):
    """Generate the ``k``-group design once and return one group's aie module.

    ``group_index`` selects the group, in the order :data:`GROUP_LAYERS` lists them.
    ``func_prefix`` is injected by ``OperatorSequence``. Every group loader calls
    this; the first generates the design and the rest reuse the files on disk.
    """
    finals = _design_paths(seq_len, embedding_dim, hidden_dim, k)
    if not all(os.path.exists(final) for final in finals):
        _run_codegen(seq_len, embedding_dim, hidden_dim, npu, k)
    return region_module(Path(finals[group_index]).read_text(), func_prefix)
