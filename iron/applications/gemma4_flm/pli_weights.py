# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Repacks the per-layer-input (PLI) projection weights for IRON's GEMM.

model.q4nx stores these bf16 weights in the block order of the engine's
vision_mm.xclbin. IRON's GEMM reads B in another order, as bfp16. The weights
are static, so the build repacks them once.
"""

import numpy as np
from ml_dtypes import bfloat16

from iron.applications.gemma4_flm import dequantize

# vision_mm.xclbin's B tiling.
K_TILE, N_TILE, CT_K, S, T = 256, 64, 256, 8, 8


def unblock(buf, K, N):
    """vision_mm's block order to a row-major (K, N) matrix."""
    x = buf.reshape(
        N // N_TILE, K // K_TILE, K_TILE // CT_K, N_TILE // T, S, CT_K // S, T
    )
    return x.transpose(1, 2, 5, 6, 0, 3, 4).reshape(K, N)


def write(model_dir, config, op, out_dir):
    """Writes pli_{down,gate,up}.weights, packed for GEMM `op`; gate and up hold one layer after another."""
    d, pli_d = config["hidden_size"], config["hidden_size_per_layer_input"]
    layers = range(config["num_hidden_layers"])
    files = {
        "down": [("model.per_layer_model_proj.weight_prefill", d, pli_d * len(layers))],
        "gate": [
            (f"model.layers.{i}.inp_gate.weight_prefill", d, pli_d) for i in layers
        ],
        "up": [
            (f"model.layers.{i}.per_layer_projection.weight_prefill", pli_d, d)
            for i in layers
        ],
    }
    q4nx = model_dir / "model.q4nx"
    header, data_start = dequantize.read_header(q4nx)
    for stem, tensors in files.items():
        with open(out_dir / f"pli_{stem}.weights", "wb") as out:
            for name, K, N in tensors:
                raw, _ = dequantize.read_tensor(q4nx, header, data_start, name)
                B = unblock(dequantize.bf16_to_f32(raw.view(np.uint16)), K, N)
                out.write(op.pack_B(B.astype(bfloat16)).tobytes())
