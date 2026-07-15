# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Stream-dse MLIR generation launcher for the fused SwiGLU-prefill operator.

This is the in-IRON replacement for the previously hardcoded
``/home/micas/stream_aie/main_swiglu.py`` entry point. It calls the *installed*
``stream-dse`` package (``pip install stream-dse`` followed by ``stream-setup-aie``)
to produce a single fused MLIR module for the whole SwiGLU-prefill block, which
IRON then fuses into a single full-ELF via `OperatorSequence`.

The function signature mirrors ``run_main_aie_codegen_swiglu`` from stream-dse's
``scripts/main_swiglu.py`` reference entry point. Because ``scripts/`` is not
shipped in the stream-dse wheel, that logic is vendored here; the hardware-
description YAML is resolved from the installed ``stream`` package, where it ships
as package data (stream-dse >= 1.13.3).

This module is imported lazily (by ``DesignGenerator`` at compile time), so
importing the operator does not require ``stream-dse`` to be installed -- only
building it does.
"""

import os
import re
from pathlib import Path

import stream
from stream.api import optimize_allocation_co
from stream.inputs.aie.mapping.make_swiglu_mapping import make_swiglu_mapping
from stream.inputs.aie.workload.make_onnx_swiglu import make_swiglu_workload

from iron.operators.swiglu_prefill_stream.stream_kernels import iron_kernels

# Hardware description for the whole-array Strix (npu2) target, shipped as package
# data inside the installed stream package (stream-dse >= 1.13.3).
_ACCELERATOR = os.path.join(
    os.path.dirname(stream.__file__),
    "inputs",
    "aie",
    "hardware",
    "whole_array_strix.yaml",
)


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
    """Generate the fused SwiGLU-prefill MLIR module via stream-dse.

    Returns an ``aie`` MLIR module. ``func_prefix`` (injected by
    ``OperatorSequence``) prefixes the kernel symbols / ``link_with`` objects so
    the design can be deployed as one fusion group; see ``region_module``.

    The default ``ortools_gscip`` backend is the license-free OR-Tools GSCIP
    solver, so no Gurobi license is required.
    """
    workload_path = make_swiglu_workload(
        seq_len,
        embedding_dim,
        hidden_dim,
        in_dtype,
        out_dtype,
        last_gemm_down=last_gemm_down,
    )
    mapping_path = make_swiglu_mapping(
        seq_len,
        embedding_dim,
        hidden_dim,
        last_gemm_down,
        seq_len_tile_size,
        embedding_tile_size,
        hidden_tile_size,
    )

    hw_name = os.path.splitext(os.path.basename(_ACCELERATOR))[0]
    wl_name = re.split(r"/|\.", workload_path)[-1]
    if wl_name == "onnx":
        wl_name = re.split(r"/|\.", workload_path)[-2]
    experiment_id = f"{hw_name}-{wl_name}-{rows}_row_{cols}_col"

    ctx = optimize_allocation_co(
        hardware=_ACCELERATOR,
        workload=workload_path,
        mapping=mapping_path,
        experiment_id=experiment_id,
        output_path="outputs",
        skip_if_exists=False,
        enable_codegen=True,
        trace_size=trace_size,
        nb_cols_to_use=cols,
        npu=npu,
        backend=backend,
        kernels=iron_kernels(),  # IRON-authored operand layouts drive the DMA tiling
    )
    return region_module(str(ctx.get("module")), func_prefix)


# ---------------------------------------------------------------------------
# k=2 variant: two fusion groups (gate/up/SiLU/mul -> h, then down-projection)
# ---------------------------------------------------------------------------
#
# stream-dse emits a separate ``aie.device`` design per fusion group (under
# ``<output>/group_i/codegen/final.mlir``). IRON fuses the two groups into one
# full-ELF via ``OperatorSequence``; each group is loaded below as a child
# design. The split itself is expressed entirely in the stream mapping
# (``make_swiglu_mapping(split_groups=True)``); see that function.


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


def _swiglu_k2_experiment_id(seq_len, embedding_dim, hidden_dim, rows, cols):
    hw_name = os.path.splitext(os.path.basename(_ACCELERATOR))[0]
    return f"{hw_name}-swiglu_k2_{seq_len}_{embedding_dim}_{hidden_dim}-{rows}_row_{cols}_col"


def _run_swiglu_k2_codegen(
    seq_len,
    embedding_dim,
    hidden_dim,
    in_dtype,
    out_dtype,
    rows,
    cols,
    npu,
    seq_len_tile_size,
    embedding_tile_size,
    hidden_tile_size,
    backend,
    output_root="outputs",
):
    """Run the two-group SwiGLU codegen once (cached by output existence).

    Returns the experiment output directory containing ``group_0`` / ``group_1``.
    Both group loaders call this; the first generates, the rest reuse the files.
    """
    experiment_id = _swiglu_k2_experiment_id(
        seq_len, embedding_dim, hidden_dim, rows, cols
    )
    out_dir = os.path.join(output_root, experiment_id)
    finals = [
        os.path.join(out_dir, f"group_{i}", "codegen", "final.mlir") for i in (0, 1)
    ]
    if all(os.path.exists(f) for f in finals):
        return out_dir

    workload_path = make_swiglu_workload(
        seq_len, embedding_dim, hidden_dim, in_dtype, out_dtype, last_gemm_down=True
    )
    mapping_path = make_swiglu_mapping(
        seq_len,
        embedding_dim,
        hidden_dim,
        True,  # last_gemm_down
        seq_len_tile_size,
        embedding_tile_size,
        hidden_tile_size,
        split_groups=True,
    )
    optimize_allocation_co(
        hardware=_ACCELERATOR,
        workload=workload_path,
        mapping=mapping_path,
        experiment_id=experiment_id,
        output_path=output_root,
        skip_if_exists=False,
        enable_codegen=True,
        trace_size=0,
        nb_cols_to_use=cols,
        npu=npu,
        backend=backend,
        kernels=iron_kernels(),
    )
    return out_dir


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

    ``group_index`` 0 is the gate/up/SiLU/mul front end (``x, w1, w2 -> h``); 1 is
    the down-projection (``h, w3 -> y``). ``func_prefix`` is injected by
    ``OperatorSequence``.
    """
    out_dir = _run_swiglu_k2_codegen(
        seq_len,
        embedding_dim,
        hidden_dim,
        in_dtype,
        out_dtype,
        rows,
        cols,
        npu,
        seq_len_tile_size,
        embedding_tile_size,
        hidden_tile_size,
        backend,
    )
    text = Path(out_dir, f"group_{group_index}", "codegen", "final.mlir").read_text()
    return region_module(text, func_prefix)
