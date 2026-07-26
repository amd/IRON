# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generate the fused SwiGLU-prefill design with stream-dse.

Both inputs stream-dse needs are produced here, from IRON:

* the **workload**, exported from :mod:`~iron.operators.swiglu_prefill_stream.reference`
  -- the same module the test checks the result against;
* the **mapping**, from the placement below.

Both are written into the experiment's output directory at build time (never into
the source tree), and the mapping's node names come from the exported workload, so
the two cannot disagree. stream-dse then solves the allocation and emits the MLIR.

This module is imported lazily (by ``DesignGenerator`` at compile time), so
importing the operator does not require ``stream-dse`` to be installed -- only
building it does.
"""

import os
import re
from functools import lru_cache
from pathlib import Path

import stream
import torch
from stream.api import optimize_allocation_co

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
# data inside the installed stream package (stream-dse >= 1.13.3).
_ACCELERATOR = os.path.join(
    os.path.dirname(stream.__file__),
    "inputs",
    "aie",
    "hardware",
    "whole_array_strix.yaml",
)

# Names for the exported graph's computation nodes, in topological order, and for
# the tensors they produce. They name the roles rather than the ATen ops
# torch.export captured, and they are what the mapping and the generated design
# are read by.
GATE, UP, SILU, MUL, DOWN = "Gemm_Left", "Gemm_Right", "Silu", "Elt_Mul", "Gemm_Down"
NODE_NAMES = [GATE, UP, SILU, MUL, DOWN]
RESULT_NAMES = {
    GATE: reference.GATE_PROJECTION,
    UP: reference.UP_PROJECTION,
    SILU: reference.ACTIVATION,
    MUL: reference.HIDDEN,
}

# Which layers each fused group contains. Splitting makes stream-dse emit one
# design per group; the tensor handed from one to the next is derived from the
# exported graph, not named here.
GROUP_LAYERS = {
    False: [[GATE, UP, SILU, MUL, DOWN]],
    True: [[GATE, UP, SILU, MUL], [DOWN]],
}

# Compute-tile placement on the 4-row x 8-column array: each GEMM gets two
# columns' worth of cores split 4-ways over rows (D0, the sequence dimension) and
# 2-ways over D2, the two elementwise layers one column each. This is a property
# of the array, not of the problem size, so it holds across shapes.
_GEMM_SPLIT = [[("D0", 4), ("D2", 2)]]
_ELEMENTWISE_SPLIT = [[("D0", 4)]]
_CORES = {
    GATE: [[2, 3, 4, 5, 8, 9, 10, 11]],
    UP: [[14, 15, 16, 17, 20, 21, 22, 23]],
    SILU: [[26, 27, 28, 29]],
    MUL: [[32, 33, 34, 35]],
    DOWN: [[38, 39, 40, 41, 44, 45, 46, 47]],
}


def gemm_tiles(seq_tile, embedding_tile, hidden_tile):
    """Kernel tile shape ``(m, k, n)`` of the gate/up GEMMs and of the down GEMM.

    The gate and up projections contract over the embedding dimension and produce
    the hidden one; the down projection contracts the other way round.
    """
    return (seq_tile, embedding_tile, hidden_tile), (
        seq_tile,
        hidden_tile,
        embedding_tile,
    )


def _placements(seq_tile, embedding_tile, hidden_tile):
    gate_up, down = gemm_tiles(seq_tile, embedding_tile, hidden_tile)

    def gemm(tiles):
        m, k, n = tiles
        return {"utilization": 61.8, "m": m, "k": k, "n": n, "layout": "default"}

    elementwise = {"utilization": 50.0, "layout": "default"}
    return {
        GATE: Placement(_CORES[GATE], _GEMM_SPLIT, gemm(gate_up)),
        UP: Placement(_CORES[UP], _GEMM_SPLIT, gemm(gate_up)),
        SILU: Placement(_CORES[SILU], _ELEMENTWISE_SPLIT, elementwise),
        MUL: Placement(_CORES[MUL], _ELEMENTWISE_SPLIT, elementwise),
        DOWN: Placement(_CORES[DOWN], _GEMM_SPLIT, gemm(down)),
    }


def _groups(seq_tile, embedding_tile, hidden_tile, split_groups):
    """Fusion groups: one fully fused design, or a front end plus down projection.

    Splitting makes stream-dse emit one design per group, which IRON then deploys
    as a single full-ELF. D0 is the sequence dimension, D1 the contraction and D2
    the output dimension of the group's leading GEMM.
    """
    if split_groups:
        tiling = [
            [
                (GATE, "D1", embedding_tile),
                (GATE, "D2", hidden_tile),
                (GATE, "D0", seq_tile),
            ],
            [
                (DOWN, "D1", hidden_tile),
                (DOWN, "D2", embedding_tile),
                (DOWN, "D0", seq_tile),
            ],
        ]
    else:
        tiling = [
            [
                (GATE, "D1", embedding_tile),
                (DOWN, "D2", embedding_tile),
                (GATE, "D2", hidden_tile),
                (GATE, "D0", seq_tile),
            ]
        ]
    return [
        FusedGroup(f"Fused_Group_{index + 1}", layers, group_tiling)
        for index, (layers, group_tiling) in enumerate(
            zip(GROUP_LAYERS[split_groups], tiling)
        )
    ]


def _check_shapes(
    seq_len, embedding_dim, hidden_dim, seq_tile, embedding_tile, hidden_tile
):
    """Reject shapes the fixed 4x8 placement cannot tile evenly."""
    rows, gemm_split = 4, 2
    if seq_len % rows or seq_len < seq_tile * rows:
        raise ValueError(
            f"seq_len ({seq_len}) must be a multiple of {rows} and at least {seq_tile * rows}"
        )
    if embedding_dim % (embedding_tile * gemm_split):
        raise ValueError(
            f"embedding_dim ({embedding_dim}) must be a multiple of "
            f"embedding_tile * {gemm_split} ({embedding_tile * gemm_split})"
        )
    if hidden_dim % (hidden_tile * gemm_split):
        raise ValueError(
            f"hidden_dim ({hidden_dim}) must be a multiple of "
            f"hidden_tile * {gemm_split} ({hidden_tile * gemm_split})"
        )


@lru_cache(maxsize=None)
def workload_for(seq_len, embedding_dim, hidden_dim):
    """The exported workload for one problem size."""
    module = swiglu_module(embedding_dim, hidden_dim)
    return export_workload(
        module,
        (torch.zeros(seq_len, embedding_dim, dtype=torch.bfloat16),),
        node_names=NODE_NAMES,
        result_names=RESULT_NAMES,
    )


def group_ports(seq_len, embedding_dim, hidden_dim, split_groups=False):
    """Per fused group, the tensor names it takes in and hands on.

    These are the operator's runtime arguments, including the tensor a split
    design passes from its front end to its down projection.
    """
    return group_boundaries(
        workload_for(seq_len, embedding_dim, hidden_dim), GROUP_LAYERS[split_groups]
    )


def build_inputs(
    seq_len,
    embedding_dim,
    hidden_dim,
    seq_len_tile_size,
    embedding_tile_size,
    hidden_tile_size,
    output_dir,
    split_groups=False,
):
    """Write the workload and mapping for one configuration; return their paths."""
    _check_shapes(
        seq_len,
        embedding_dim,
        hidden_dim,
        seq_len_tile_size,
        embedding_tile_size,
        hidden_tile_size,
    )
    workload = workload_for(seq_len, embedding_dim, hidden_dim)
    output_dir = Path(output_dir)
    return (
        workload.write(output_dir / "workload.onnx"),
        emit_mapping(
            workload,
            _placements(seq_len_tile_size, embedding_tile_size, hidden_tile_size),
            _groups(
                seq_len_tile_size, embedding_tile_size, hidden_tile_size, split_groups
            ),
            output_dir / "mapping.yaml",
        ),
    )


def _experiment_id(seq_len, embedding_dim, hidden_dim, rows, cols, suffix=""):
    hw_name = os.path.splitext(os.path.basename(_ACCELERATOR))[0]
    return f"{hw_name}-swiglu{suffix}_{seq_len}_{embedding_dim}_{hidden_dim}-{rows}_row_{cols}_col"


def _run_codegen(
    seq_len,
    embedding_dim,
    hidden_dim,
    rows,
    cols,
    npu,
    seq_len_tile_size,
    embedding_tile_size,
    hidden_tile_size,
    backend,
    trace_size=0,
    split_groups=False,
    output_root="outputs",
):
    """Run stream-dse's constraint-optimization + code generation once."""
    experiment_id = _experiment_id(
        seq_len, embedding_dim, hidden_dim, rows, cols, "_k2" if split_groups else ""
    )
    output_dir = os.path.join(output_root, experiment_id)
    workload_path, mapping_path = build_inputs(
        seq_len,
        embedding_dim,
        hidden_dim,
        seq_len_tile_size,
        embedding_tile_size,
        hidden_tile_size,
        output_dir,
        split_groups=split_groups,
    )
    ctx = optimize_allocation_co(
        hardware=_ACCELERATOR,
        workload=workload_path,
        mapping=mapping_path,
        experiment_id=experiment_id,
        output_path=output_root,
        skip_if_exists=False,
        enable_codegen=True,
        trace_size=trace_size,
        nb_cols_to_use=cols,
        npu=npu,
        backend=backend,
    )
    return ctx, output_dir


def run_main_aie_codegen_swiglu(
    seq_len,
    embedding_dim,
    hidden_dim,
    in_dtype="bf16",
    out_dtype="bf16",
    trace_size=0,
    rows=4,
    cols=8,
    npu="npu2",
    seq_len_tile_size=32,
    embedding_tile_size=32,
    hidden_tile_size=64,
    last_gemm_down=True,
    backend="ortools_gscip",
    func_prefix="",
):
    """Generate the fully fused SwiGLU-prefill MLIR module.

    Returns an ``aie`` MLIR module. ``func_prefix`` (injected by
    ``OperatorSequence``) prefixes the kernel symbols / ``link_with`` objects so
    the design can be deployed as one fusion group; see :func:`region_module`.

    The default ``ortools_gscip`` backend is the license-free OR-Tools GSCIP
    solver, so no Gurobi license is required.
    """
    ctx, _ = _run_codegen(
        seq_len,
        embedding_dim,
        hidden_dim,
        rows,
        cols,
        npu,
        seq_len_tile_size,
        embedding_tile_size,
        hidden_tile_size,
        backend,
        trace_size=trace_size,
    )
    return region_module(str(ctx.get("module")), func_prefix)


# ---------------------------------------------------------------------------
# k=2 variant: two fusion groups (gate/up/SiLU/mul -> h, then down-projection)
# ---------------------------------------------------------------------------
#
# stream-dse emits a separate ``aie.device`` design per fusion group (under
# ``<output>/group_i/codegen/final.mlir``). IRON fuses the two groups into one
# full-ELF via ``OperatorSequence``; each group is loaded below as a child design.


def _prefixed(mlir_text: str, func_prefix: str) -> str:
    """Apply a fused-operator ``func_prefix`` (``op<idx>_``) to a group's MLIR.

    ``OperatorSequence`` renames each child's kernel object files and symbols to
    ``op<idx>_...`` so the groups stay distinct inside one ELF; the group's MLIR
    must reference the same prefixed names. Prefix the ``link_with`` object files
    and every privately-declared kernel symbol (and its call sites).
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
    for sym in symbols:
        mlir_text = re.sub(rf"@{re.escape(sym)}\b", f"@{func_prefix}{sym}", mlir_text)
    return mlir_text


def region_module(mlir_text: str, func_prefix: str = ""):
    """Parse a stream group's MLIR text into an ``aie`` module for fusion.

    ``OperatorSequence`` consumes ``aie.DeviceOp`` objects, so the (xDSL-emitted)
    group text is re-parsed with the mlir-aie bindings, after ``func_prefix``
    rewriting.
    """
    from aie import ir
    from aie.extras.context import mlir_mod_ctx

    with mlir_mod_ctx():
        return ir.Module.parse(_prefixed(mlir_text, func_prefix))


def load_swiglu_k2_group(
    group_index,
    func_prefix="",
    *,
    seq_len,
    embedding_dim,
    hidden_dim,
    in_dtype="bf16",
    out_dtype="bf16",
    rows=4,
    cols=8,
    npu="npu2",
    seq_len_tile_size=32,
    embedding_tile_size=32,
    hidden_tile_size=64,
    backend="ortools_gscip",
):
    """Generate the two-group design (cached) and return one group's aie module.

    ``group_index`` 0 is the gate/up/SiLU/mul front end (``x, w_gate, w_up -> h``);
    1 is the down projection (``h, w_down -> y``). ``func_prefix`` is injected by
    ``OperatorSequence``. Both group loaders call this; the first generates the
    design, the second reuses the files on disk.
    """
    output_dir = os.path.join(
        "outputs", _experiment_id(seq_len, embedding_dim, hidden_dim, rows, cols, "_k2")
    )
    finals = [
        os.path.join(output_dir, f"group_{i}", "codegen", "final.mlir") for i in (0, 1)
    ]
    if not all(os.path.exists(f) for f in finals):
        _run_codegen(
            seq_len,
            embedding_dim,
            hidden_dim,
            rows,
            cols,
            npu,
            seq_len_tile_size,
            embedding_tile_size,
            hidden_tile_size,
            backend,
            split_groups=True,
        )
    return region_module(Path(finals[group_index]).read_text(), func_prefix)
