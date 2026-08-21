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
from xdsl.ir.affine import AffineMap
from stream.api import optimize_allocation_co
from stream.parser.onnx.operator_parser import OnnxOperatorParser
from stream.workload.workload import ComputationNode, Tensor

from iron.common.stream.hardware import ComputeArray
from iron.common.stream.mapping import (
    FusedGroup,
    Placement,
    emit_mapping,
    group_boundaries,
)
from iron.common.stream.workload import export_workload
from iron.operators.swiglu_prefill_stream_front_fused import reference
from iron.operators.swiglu_prefill_stream_front_fused.reference import swiglu_module

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
NAME_FRONT = "front"
NAME_DOWN = "down"
NODE_NAMES = [NAME_FRONT, NAME_DOWN]
RESULT_NAMES = {
    NAME_FRONT: reference.NAME_FRONT,
}

# Sequence positions an elementwise layer works at a time when it reads from and
# writes to memory. Its tile is then this many whole rows, which is contiguous in
# a row-major tensor, so each transfer runs the length of the rows rather than one
# MAC tile at a time.
ELEMENTWISE_ROWS = 1

GROUP_LAYERS = [[NAME_FRONT, NAME_DOWN]]


class SwigluFrontFusedParser(OnnxOperatorParser):
    def generate_node(self, name_to_tensor_dict: dict[str, Tensor]) -> ComputationNode:
        inputs = tuple(name_to_tensor_dict[name] for name in self.node.input)

        # check input and shape validness
        assert len(inputs) == 2
        input_data, input_weight = inputs
        assert len(input_data.shape) == 2 and len(input_weight.shape) == 3
        dm, dk = input_data.shape
        wk, two, wn = input_weight.shape
        assert dk == wk
        assert two == 2

        mappings = (
            AffineMap.from_callable(lambda m, k, t, n: (m, k)),
            AffineMap.from_callable(lambda m, k, t, n: (k, t, n)),
            AffineMap.from_callable(lambda m, k, t, n: (m, n)),
        )
        return ComputationNode(
            type=self.node.op_type,
            name=self.node.name,
            inputs=inputs,
            outputs=self.get_output_tensors(),
            operand_mapping=mappings,
        )


def tiles_for():
    """The kernel tile, as (sequence, embedding, hidden), for ``k`` fused groups."""
    # TODO tune this
    return (32, 32, 64)


def gemm_tiles():
    """Each GEMM layer's kernel tile, in the (m, k, n) order the kernel takes."""
    sequence, embedding, hidden = tiles_for()
    return {
        NAME_FRONT: (sequence, embedding, hidden),
        NAME_DOWN: (sequence, hidden, embedding),
    }


@lru_cache(maxsize=None)
def array() -> ComputeArray:
    """The compute grid of the device being built for."""
    import aie.utils as aie_utils

    return ComputeArray.from_device(aie_utils.get_current_device())


def _placements():
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
    sequence_tile, _, hidden_tile = tiles_for()
    tiles = gemm_tiles()

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

    # TODO rework/tune this
    columns = dict(zip(NODE_NAMES, grid.allocate([2, 2])))
    gemm_split = (("D0", grid.num_rows), ("D2", 2))
    return {
        NAME_FRONT: Placement(columns[NAME_FRONT], gemm_split, gemm(tiles[NAME_FRONT])),
        NAME_DOWN: Placement(columns[NAME_DOWN], gemm_split, gemm(tiles[NAME_DOWN])),
    }


def _layer_tiling(layer, hidden_dim, k):
    """Intra-core tiling of one layer, over the dimensions it iterates."""
    if layer not in (GATE, UP, DOWN):
        return [(layer, "D1", hidden_dim), (layer, "D0", ELEMENTWISE_ROWS)]
    sequence, contraction, output = gemm_tiles()[layer]
    return [
        (layer, "D1", contraction),
        (layer, "D2", output),
        (layer, "D0", sequence),
    ]


def _groups():
    """The fused groups, each with the intra-core tiling of its leading GEMM.

    Splitting makes stream-dse emit one design per group, which IRON then deploys
    as a single full ELF. D0 is the sequence dimension, D1 the contraction and D2
    the output dimension.
    """
    sequence_tile, embedding_tile, hidden_tile = tiles_for()
    # TODO what does this mean exactly?
    tiling = [
        [
            (NAME_FRONT, "D1", embedding_tile),
            (NAME_DOWN, "D2", embedding_tile),
        ]
    ]
    return [
        FusedGroup(f"Fused_Group_{index + 1}", layers, group_tiling)
        for index, (layers, group_tiling) in enumerate(zip(GROUP_LAYERS, tiling))
    ]


def _check_shapes(seq_len, embedding_dim, hidden_dim):
    """Reject a problem size the placement and the kernel tiles cannot divide."""
    grid = array()
    sequence_tile, embedding_tile, hidden_tile = tiles_for()
    gemm_split = 2
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


def group_ports(seq_len, embedding_dim, hidden_dim):
    """Per fused group, the tensor names it takes in and hands on.

    These are the operator's runtime arguments, including the tensors a split
    design passes from one group to the next.
    """
    return group_boundaries(
        workload_for(seq_len, embedding_dim, hidden_dim), GROUP_LAYERS
    )


def build_inputs(seq_len, embedding_dim, hidden_dim, output_dir):
    """Write the workload and mapping for one configuration; return their paths."""
    _check_shapes(seq_len, embedding_dim, hidden_dim)
    workload = workload_for(seq_len, embedding_dim, hidden_dim)
    output_dir = Path(output_dir)
    return (
        workload.write(output_dir / "workload.onnx"),
        emit_mapping(
            workload,
            _placements(),
            _groups(),
            array(),
            output_dir / "mapping.yaml",
        ),
    )


def _experiment_id(seq_len, embedding_dim, hidden_dim):
    grid = array()
    hardware = os.path.splitext(os.path.basename(ACCELERATOR))[0]
    return (
        f"{hardware}-swiglu_fused_front_{seq_len}_{embedding_dim}_{hidden_dim}"
        f"-{grid.num_rows}_row_{grid.num_columns}_col"
    )


def _design_paths(seq_len, embedding_dim, hidden_dim):
    """Where stream-dse writes each group's MLIR.

    A single fused group goes through stream-dse's single-design pipeline and lands
    in ``codegen/``; several groups each land in their own ``group_i/codegen/``.
    """
    output_dir = os.path.join(
        OUTPUT_ROOT, _experiment_id(seq_len, embedding_dim, hidden_dim)
    )
    return [os.path.join(output_dir, "codegen", "final.mlir")]


def _run_codegen(seq_len, embedding_dim, hidden_dim, npu):
    """Run stream-dse's constraint optimization and code generation once."""
    from stream.parser.onnx.model import register_onnx_parser

    register_onnx_parser("SwigluFrontFused", SwigluFrontFusedParser)

    grid = array()
    experiment_id = _experiment_id(seq_len, embedding_dim, hidden_dim)
    workload_path, mapping_path = build_inputs(
        seq_len,
        embedding_dim,
        hidden_dim,
        os.path.join(OUTPUT_ROOT, experiment_id),
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


def _group_text(group_index, *, seq_len, embedding_dim, hidden_dim, npu) -> str:
    """One group's generated MLIR, before any ``func_prefix`` rewriting."""
    finals = _design_paths(seq_len, embedding_dim, hidden_dim)
    if not all(os.path.exists(final) for final in finals):
        _run_codegen(seq_len, embedding_dim, hidden_dim, npu)
    return Path(finals[group_index]).read_text()


def group_digest(group_index, **dims) -> str:
    """Digest of a group's design, for recognising groups that share one."""
    return hashlib.sha256(_group_text(group_index, **dims).encode()).hexdigest()


def load_group(
    group_index, func_prefix="", *, seq_len, embedding_dim, hidden_dim, npu
):
    """Generate the ``k``-group design once and return one group's aie module.

    ``group_index`` selects the group, in the order :data:`GROUP_LAYERS` lists them.
    ``func_prefix`` is injected by ``OperatorSequence``. Every group loader calls
    this; the first generates the design and the rest reuse the files on disk.
    """
    text = _group_text(
        group_index,
        seq_len=seq_len,
        embedding_dim=embedding_dim,
        hidden_dim=hidden_dim,
        npu=npu,
    )
    return region_module(text, func_prefix)
