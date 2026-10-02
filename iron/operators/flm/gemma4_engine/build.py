# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Builds the IRON operators of Gemma 4 E2B's text path and stages them for FastFlowLM.

    python build.py --engine-xclbins <FastFlowLM's src/xclbins> --out <out dir>

Reads the model from $FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2. Writes:

    <out>/xclbins/Gemma4-E2B-IT-NPU2/   the engine's xclbins, six replaced by IRON's
    <out>/xclbins/.../iron/             instruction sequences and repacked weights
    <out>/gen/                          sequence generators the engine compiles in
"""

import argparse
import json
import os
import shutil
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import PerCall
from aie.iron.device import NPU2
from aie.iron.kernels import FLM_GEMMA4_E2B_DECODE

from iron import Precision
from iron.operators.flm import (
    DecodeLayer,
    DequantBFP,
    LMHead,
    PrefillAttention,
    PrefillSlidingAttention,
    ProjectionGEMM,
)
from iron.operators.flm.dequant.op import CT_K as DEQUANT_CT_K
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemma4_engine import pli_weights
from iron.operators.flm.layer.design import LayerType

MODEL = "Gemma4-E2B-IT-NPU2"

# FastFlowLM's longest prompt chunk starts up to 127 tokens early, then
# pads to 256 rows (512 for the per-layer-input projections).
MAX_M = 4352
PLI_MAX_M = 4608

# (K, N, gelu) of every projection GEMM of Gemma 4 E2B. Sliding-window and global layers
# differ in head size; some layers have an MLP twice as wide. v has k's shape.
GEMMS = [
    (1536, 2048, False),  # q, sliding window
    (1536, 4096, False),  # q, global
    (1536, 256, False),  # k and v, sliding window
    (1536, 512, False),  # k and v, global
    (2048, 1536, False),  # o, sliding window
    (4096, 1536, False),  # o, global
    (1536, 6144, True),  # gate
    (1536, 6144, False),  # up
    (6144, 1536, False),  # down
    (1536, 12288, True),  # gate, wide MLP
    (1536, 12288, False),  # up, wide MLP
    (12288, 1536, False),  # down, wide MLP
]
# (K, N) of every dequant step. A layer with its own KV cache dequantizes q, k
# and v in one dispatch.
DEQUANT = [
    (1536, 2048),
    (1536, 4096),
    (1536, 2048 + 2 * 256),
    (1536, 4096 + 2 * 512),
    (2048, 1536),
    (4096, 1536),
    (6144, 1536),
    (12288, 1536),
]
# The engine interleaves up and gate in runs of 512 out-features.
UPGATE = [(1536, 6144), (1536, 12288)]
UPGATE_RUN = 512


def gemm(M, K, N, gelu):
    """Build every GEMM of the model: floor rounding, bf16_steps gelu and MEDIUM's bfp16 macs.

    Reproduce the engine's arithmetic bit for bit. ``k_tile=256`` divides
    every K, so one configuration serves all shapes; B's k slice comes
    from DequantBFP's. One sequence generator serves every row count up to M.
    """
    op = ProjectionGEMM(
        M=M,
        K=K,
        N=N,
        epilogue=Epilogue.GELU if gelu else Epilogue.NONE,
        tile_n=64,
        k_tile=256,
        ct_k=DEQUANT_CT_K,
        rounding="floor",
        gelu="bf16_steps",
        precision=Precision.MEDIUM,
        bfp16_b=True,
    )
    op.use_value("valid")
    return op


def write_generator(artifacts, path, namespace):
    """Write the C++ that generates `artifacts`' instruction sequence, for the engine to compile in."""
    cpp = (artifacts.entry.directory / "dispatch_gen.cpp").read_text()
    # mlir-aie emits a dlopen shim after the generator. The engine links several
    # generators, so drop the shim and give each generator a namespace.
    includes, body = cpp[: cpp.index('extern "C"')].split("\ninline ", 1)
    path.write_text(
        f"{includes}\nnamespace iron::seq::{namespace} {{\ninline {body}}}\n"
    )


def write_gemm_generators(gemms, built, gen):
    """Export each GEMM's sequence with the engine's single row-count argument."""
    includes, entries = [], []
    m = PerCall("m", None, np.int32).affine()
    for op in gemms:
        op_resolved = op.resolved()
        gelu = op.epilogue == Epilogue.GELU
        name = f"gemm_K{op.K}_N{op.N}" + ("_gelu" if gelu else "")
        path = gen / f"{name}.h"
        write_generator(built[op], path, name)
        # The declaration supplies the row-bound words in generator order.
        # Their Affine expressions use integer +, *, and shifts: the same
        # spelling and arithmetic in Python and C++ for these positive rows.
        args = ", ".join(
            str(op_resolved.derived_at(v.name, valid=m)) if v.derive else "m"
            for v in op_resolved.values
        )
        with path.open("a") as f:
            f.write(
                f"namespace iron::seq::{name} {{\n"
                "inline std::optional<std::vector<uint32_t>> generate(int32_t m) {\n"
                f"    if (m < 256 || m > {op.M} || m % 256) return std::nullopt;\n"
                f"    return generate_txn_main_sequence({args});\n"
                "}\n}\n"
            )
        includes.append(f'#include "{name}.h"')
        entries.append(
            f"    {{{op.K}, {op.N}, {str(gelu).lower()}, {name}::generate}},"
        )
    (gen / "gemm.h").write_text(
        "\n".join(
            [
                "#pragma once",
                *includes,
                "namespace iron::seq {",
                "struct gemm_generator {",
                "    uint32_t k, n;",
                "    bool gelu;",
                "    std::optional<std::vector<uint32_t>> (*generate)(int32_t m);",
                "};",
                "inline const gemm_generator gemm_generators[] = {",
                *entries,
                "};",
                "} // namespace iron::seq",
                "",
            ]
        )
    )


def compile_all(ops):
    built = {}
    for i, op in enumerate(ops, 1):
        print(f"[{i}/{len(ops)}] {op.name}", flush=True)
        built[op] = op.compile()
    return built


def one_xclbin(built):
    """Return the xclbin all of `built` share. The engine registers one xclbin per operator."""
    xclbins = {artifacts.image for artifacts in built}
    assert len(xclbins) == 1, f"expected one configuration, got {sorted(xclbins)}"
    return xclbins.pop()


def main(engine_xclbins, out):
    model_dir = Path(os.environ["FLM_MODEL_PATH"]) / "models" / MODEL
    config = json.loads((model_dir / "config.json").read_text())
    with aie_utils.set_current_device(NPU2()):
        layers = [
            DecodeLayer(geometry=FLM_GEMMA4_E2B_DECODE, layer_type=t) for t in LayerType
        ]
        # Bounds the KV cache rows; the stride is a dispatch parameter.
        max_context = 32768
        num_heads = config["num_attention_heads"]
        num_kv_heads = config["num_key_value_heads"]
        attn = PrefillAttention(
            max_context=max_context, num_heads=num_heads, num_kv_heads=num_kv_heads
        )
        swa = PrefillSlidingAttention(
            window=config["sliding_window"],
            max_context=max_context,
            num_heads=num_heads,
            num_kv_heads=num_kv_heads,
        )
        lm_head = LMHead(
            dim=config["hidden_size"],
            vocab=config["vocab_size"],
            softcap=config["final_logit_softcapping"],
        )
        dequants = [DequantBFP(K=k, N=n) for k, n in DEQUANT]
        dequants += [
            DequantBFP(
                K=k,
                N=n,
                run_out_features=UPGATE_RUN,
                run_period_out_features=2 * UPGATE_RUN,
            )
            for k, n in UPGATE
        ]
        gemms = [gemm(MAX_M, k, n, gelu) for k, n, gelu in GEMMS]
        d, pli_d = config["hidden_size"], config["hidden_size_per_layer_input"]
        pli_shapes = [
            (d, pli_d * config["num_hidden_layers"], False),
            (d, pli_d, True),
            (pli_d, d, False),
        ]
        gemms += [gemm(PLI_MAX_M, k, n, gelu) for k, n, gelu in pli_shapes]

        groups = {
            "layer": layers,
            "attn": [attn],
            "swa": [swa],
            "lm_head": [lm_head],
            "mm": gemms,
            "dequant": dequants,
        }
        built = compile_all([op for ops in groups.values() for op in ops])

        # Stage the engine's xclbins with IRON's under the engine's file names. The
        # engine registers each xclbin by its path, and overrides.hpp registers the
        # same paths, so IRON's operators take no hardware context of their own.
        # The four layer types configure the array identically, so one xclbin
        # serves all four.
        stage = out / "xclbins" / MODEL
        shutil.rmtree(stage, ignore_errors=True)
        shutil.copytree(Path(engine_xclbins) / MODEL, stage, symlinks=True)
        iron = stage / "iron"
        iron.mkdir()
        for name, ops in groups.items():
            shutil.copyfile(
                one_xclbin(built[op] for op in ops), stage / f"{name}.xclbin"
            )

        # Static instruction sequences, named by the shape the header looks them up by.
        shutil.copyfile(built[lm_head].insts, iron / "lm_head.bin")
        for op in dequants:
            shutil.copyfile(built[op].insts, iron / f"dequant_K{op.K}_N{op.N}.bin")
        pli_weights.write(model_dir, config, gemms[0], iron)

        # Dynamic instruction sequences.
        gen = out / "gen"
        gen.mkdir(exist_ok=True)
        for op in layers:
            t = op.layer_type
            write_generator(built[op], gen / f"layer_{t}.h", f"layer_{t}")
        for name, op in (("attn", attn), ("swa", swa)):
            write_generator(built[op], gen / f"{name}.h", name)
        write_gemm_generators(gemms, built, gen)
        print(f"staged {stage}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--engine-xclbins", type=Path, required=True, help="FastFlowLM's src/xclbins"
    )
    parser.add_argument("--out", type=Path, required=True, help="the staging directory")
    args = parser.parse_args()
    main(args.engine_xclbins, args.out.resolve())
