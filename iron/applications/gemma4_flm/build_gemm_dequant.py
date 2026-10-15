#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Builds IRON GEMM and dequant operators and stages them for FastFlowLM.

    python build_gemm_dequant.py --engine-xclbins <FastFlowLM's src/xclbins> --out <out dir>

Writes:

    <out>/xclbins/Gemma4-E2B-IT-NPU2/   the engine's xclbins, with mm and dequant replaced
    <out>/xclbins/.../iron/             GEMM and dequant instruction sequences
"""

import argparse
import shutil
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import NPU2

from iron.operators.flm import GEMM, DequantBFP
from iron.operators.flm.gemm.design import Epilogue

MODEL = "Gemma4-E2B-IT-NPU2"

# The longest prompt chunk, flm's --prefill-chunk-len. The engine starts a
# chunk up to 127 tokens early and pads it to a multiple of 256 rows. Each row
# count M needs its own GEMM instruction sequence.
CHUNK = 512
# M=768 occurs only for a chunk that starts at an offset that is not a multiple
# of 128. The current flm clears the context each turn and never dispatches it.
WIDTHS = range(256, (CHUNK + 127 + 255) // 256 * 256 + 1, 256)
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
    )


def compile_all(ops):
    built = {}
    for i, op in enumerate(ops, 1):
        print(f"[{i}/{len(ops)}] {op.name}", flush=True)
        built[op] = op.compile()
    return built


def one_xclbin(built):
    """The xclbin all of `built` share. The engine registers one xclbin per operator."""
    xclbins = {artifacts.image for artifacts in built}
    assert len(xclbins) == 1, f"expected one configuration, got {sorted(xclbins)}"
    return xclbins.pop()


def main(engine_xclbins, out):
    aie_utils.set_current_device(NPU2())

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
    gemms = [gemm(m, k, n, gelu) for m in WIDTHS for k, n, gelu in GEMMS]

    built = compile_all([*dequants, *gemms])

    # Stage the engine's xclbins with IRON's under the engine's file names.
    stage = out / "xclbins" / MODEL
    shutil.rmtree(stage, ignore_errors=True)
    shutil.copytree(Path(engine_xclbins) / MODEL, stage, symlinks=True)
    iron = stage / "iron"
    iron.mkdir()
    for name, xclbin in {
        "mm": one_xclbin(built[op] for op in gemms),
        "dequant": one_xclbin(built[op] for op in dequants),
    }.items():
        shutil.copyfile(xclbin, stage / f"{name}.xclbin")

    for op in dequants:
        shutil.copyfile(built[op].insts, iron / f"dequant_K{op.K}_N{op.N}.bin")
    for op in gemms:
        gelu = "_gelu" if op.epilogue == Epilogue.GELU else ""
        shutil.copyfile(
            built[op].insts, iron / f"gemm_M{op.M}_K{op.K}_N{op.N}{gelu}.bin"
        )
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
