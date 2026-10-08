# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Golden data + wire packing for the int8-weight GEMV operator.

The kernel consumes ONE packed wire per weight tensor: per ``tile_m``-row block,
``[tile_m*K int8 weights | tile_m*(K/128) bf16 group scales]``, streamed column-major
over M (column ``c`` owns rows ``[c*M/cols, +M/cols)``).  Two payload domains exist,
selected by ``GEMVInt8.kernel_source``:

* ``mv_int8.cc`` (biased, default): byte = q + 128 as uint8, kernel computes
  ``(byte - 128) * s``.
* ``mv_int8_signed.cc``: byte = q as two's-complement int8, kernel computes
  ``q * s`` directly (one fewer vector op per block).

Both encode the SAME dequantized weight, so a single CPU reference serves both.
"""

import numpy as np
import torch

GROUP = 128


def reference(w_int8, scales, B):
    """CPU ground truth for the kernel's EXACT arithmetic.

    The kernel folds the group scale into the activations BEFORE the mac
    (``xs = bf16(x * s)`` -- that premul is what makes the loop cheap), so the
    golden must round ``x * s`` to bf16 the same way; comparing against an
    f32-exact dequantize instead would blame the kernel for the premul's own
    rounding on cancellation-heavy rows.
    """
    M, K = w_int8.shape
    s = scales.to(torch.float32)
    if s.shape[0] != M:
        s = s.t()
    s_exp = s.repeat_interleave(K // s.shape[1], dim=1)   # (M, K)
    xs = (B.to(torch.float32)[None, :] * s_exp).to(torch.bfloat16).to(torch.float32)
    return (w_int8.to(torch.float32) * xs).sum(dim=1)


def generate_golden_reference(M=2048, K=2048, seed=42, val_range=60):
    """Random int8 weights + per-(row, group-of-128) bf16 scales + bf16 vector."""
    rng = np.random.default_rng(seed)
    n_groups = K // GROUP
    w_int8 = rng.integers(-val_range, val_range + 1, size=(M, K), dtype=np.int8)
    scales = torch.from_numpy(rng.random((M, n_groups)).astype(np.float32) * 0.05 + 0.01)
    scales = scales.to(torch.bfloat16)
    B = torch.from_numpy(rng.standard_normal(K).astype(np.float32)).to(torch.bfloat16)
    return {
        "w_int8": w_int8,
        "scales": scales,
        "B": B,
        "C": reference(torch.from_numpy(w_int8), scales, B).to(torch.bfloat16),
    }


def pack_payload(w_int8, scales, cols, tile_m, domain="biased"):
    """Host-side wire packing (see the module docstring for the layout)."""
    M, K = w_int8.shape
    n_groups = K // GROUP
    if domain == "biased":
        w_bytes = (w_int8.astype(np.int16) + 128).astype(np.uint8)
    elif domain == "signed":
        w_bytes = w_int8.astype(np.int8).view(np.uint8)
    else:
        raise ValueError(f"unknown payload domain: {domain}")
    s_bytes = scales.contiguous().view(torch.uint8).numpy().reshape(M, n_groups * 2)

    per_col = M // cols
    chunks = []
    for c in range(cols):
        for r0 in range(c * per_col, (c + 1) * per_col, tile_m):
            chunks.append(np.concatenate([
                w_bytes[r0:r0 + tile_m].reshape(-1),
                s_bytes[r0:r0 + tile_m].reshape(-1),
            ]))
    flat = np.concatenate(chunks)
    return torch.from_numpy(flat.copy()).view(torch.bfloat16)
