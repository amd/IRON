#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Builds the IRON operators of Gemma 4 E2B's text path and stages them for FastFlowLM.

    python build.py <FastFlowLM's src/xclbins> <out dir>

Reads the model from $FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2. Writes:

    <out>/xclbins/Gemma4-E2B-IT-NPU2/   the engine's xclbins, six of them replaced by IRON's
    <out>/xclbins/.../iron/             instruction sequences and repacked weights
    <out>/gen/                          sequence generators the engine compiles in
"""

import json
import os
import shutil
import sys
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import NPU2

from iron.common import AIEContext
from iron.operators.flm import (
    GEMM,
    DecodeLayer,
    DequantBFP,
    LMHead,
    PrefillAttention,
    PrefillSlidingAttention,
)
from iron.operators.flm.gemm.design import Epilogue

import pli_weights

MODEL = "Gemma4-E2B-IT-NPU2"

# The longest prompt chunk, flm's --prefill-chunk-len. The engine starts a
# chunk up to 127 tokens early and pads it to a multiple of 256 rows. Each row
# count M needs its own GEMM instruction sequence.
CHUNK = 512
# M=768 occurs only for a chunk that starts at an offset that is not a multiple
# of 128. The current flm clears the context each turn and never dispatches it.
WIDTHS = range(256, (CHUNK + 127 + 255) // 256 * 256 + 1, 256)
# The per-layer-input projections pad M to a multiple of 512.
PLI_WIDTHS = sorted({(m + 511) // 512 * 512 for m in WIDTHS})

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


def gemm(M, K, N, gelu, ctx):
    """Every GEMM of the model.

    floor rounding and bf16_steps gelu reproduce the engine's arithmetic bit for
    bit. k_tile=256 divides every K, so all shapes share one configuration, and
    so one xclbin.
    """
    return GEMM(
        M=M,
        K=K,
        N=N,
        epilogue=Epilogue.GELU if gelu else Epilogue.NONE,
        tile_n=64,
        k_tile=256,
        rounding="floor",
        gelu="bf16_steps",
        context=ctx,
    )


def write_generator(op, path, namespace):
    """Writes the C++ that generates `op`'s instruction sequence, for the engine to compile in."""
    cpp = Path(op.dispatch_artifact.cpp_filename).read_text()
    # IRON emits a dlopen shim after the generator. The engine links several
    # generators, so drop the shim and give each generator a namespace.
    includes, body = cpp[: cpp.index('extern "C"')].split("\ninline ", 1)
    path.write_text(
        f"{includes}\nnamespace iron::seq::{namespace} {{\ninline {body}}}\n"
    )


def compile_all(ops):
    for i, op in enumerate(ops, 1):
        print(f"[{i}/{len(ops)}] {op.name}", flush=True)
        op.compile()


def one_xclbin(ops):
    """The xclbin all `ops` share. The engine registers one xclbin per operator."""
    xclbins = {op.xclbin_artifact.filename for op in ops}
    assert len(xclbins) == 1, f"expected one configuration, got {sorted(xclbins)}"
    return xclbins.pop()


def main(engine_xclbins, out):
    model_dir = Path(os.environ["FLM_MODEL_PATH"]) / "models" / MODEL
    config = json.loads((model_dir / "config.json").read_text())
    aie_utils.set_current_device(NPU2())
    ctx = AIEContext(build_dir=out / "ops")

    layers = {
        t: DecodeLayer(model="GEMMA4_E2B", layer_type=t, context=ctx)
        for t in ("global", "swa", "global_skip", "swa_skip")
    }
    heads = dict(
        max_context=32768,  # bounds the KV cache rows; the stride is a dispatch parameter
        num_heads=config["num_attention_heads"],
        num_kv_heads=config["num_key_value_heads"],
        context=ctx,
    )
    attn = PrefillAttention(**heads)
    swa = PrefillSlidingAttention(window=config["sliding_window"], **heads)
    lm_head = LMHead(
        dim=config["hidden_size"],
        vocab=config["vocab_size"],
        softcap=config["final_logit_softcapping"],
        context=ctx,
    )
    dequants = [DequantBFP(K=k, N=n, context=ctx) for k, n in DEQUANT]
    dequants += [
        DequantBFP(
            K=k,
            N=n,
            run_out_features=UPGATE_RUN,
            run_period_out_features=2 * UPGATE_RUN,
            context=ctx,
        )
        for k, n in UPGATE
    ]
    gemms = [gemm(m, k, n, gelu, ctx) for m in WIDTHS for k, n, gelu in GEMMS]
    d, pli_d = config["hidden_size"], config["hidden_size_per_layer_input"]
    pli_shapes = [
        (d, pli_d * config["num_hidden_layers"], False),
        (d, pli_d, True),
        (pli_d, d, False),
    ]
    gemms += [gemm(m, k, n, gelu, ctx) for m in PLI_WIDTHS for k, n, gelu in pli_shapes]

    compile_all([*layers.values(), attn, swa, lm_head, *dequants, *gemms])

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
    for name, xclbin in {
        "layer": layers["global"].xclbin_artifact.filename,
        "attn": attn.xclbin_artifact.filename,
        "swa": swa.xclbin_artifact.filename,
        "lm_head": lm_head.xclbin_artifact.filename,
        "mm": one_xclbin(gemms),
        "dequant": one_xclbin(dequants),
    }.items():
        shutil.copyfile(xclbin, stage / f"{name}.xclbin")

    # Static instruction sequences, named by the shape the header looks them up by.
    shutil.copyfile(lm_head.insts_artifact.filename, iron / "lm_head.bin")
    for op in dequants:
        shutil.copyfile(
            op.insts_artifact.filename, iron / f"dequant_K{op.K}_N{op.N}.bin"
        )
    for op in gemms:
        gelu = "_gelu" if op.epilogue == Epilogue.GELU else ""
        shutil.copyfile(
            op.insts_artifact.filename, iron / f"gemm_M{op.M}_K{op.K}_N{op.N}{gelu}.bin"
        )
    pli_weights.write(model_dir, config, gemms[0], iron)

    # Dynamic instruction sequences.
    gen = out / "gen"
    gen.mkdir(exist_ok=True)
    for t, op in layers.items():
        write_generator(op, gen / f"layer_{t}.h", f"layer_{t}")
    write_generator(attn, gen / "attn.h", "attn")
    write_generator(swa, gen / "swa.h", "swa")
    print(f"staged {stage}")


if __name__ == "__main__":
    main(sys.argv[1], Path(sys.argv[2]).resolve())
