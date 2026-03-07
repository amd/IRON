# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch


def generate_golden_reference(embedding_dim=2048, hidden_dim=8192, seed=42):
    """Generate golden reference for fused SwiGLU decode.

    Computes: output = Wdown @ (silu(Wgate @ x) * (Wup @ x))

    The full SwiGLU MLP in a single NPU design: dual-GEMV + SiLU + Mul
    feeds directly into a down-projection GEMV on-chip.

    Returns dict with all weight tensors, input, intermediates, and output.
    """
    torch.manual_seed(seed)
    val_range = 4
    x = torch.randn(embedding_dim, dtype=torch.bfloat16) * val_range
    w_gate = torch.randn(hidden_dim, embedding_dim, dtype=torch.bfloat16) * val_range
    w_up = torch.randn(hidden_dim, embedding_dim, dtype=torch.bfloat16) * val_range
    w_down = torch.randn(embedding_dim, hidden_dim, dtype=torch.bfloat16) * val_range

    gate = w_gate @ x
    up = w_up @ x
    intermediate = torch.nn.functional.silu(gate) * up
    output = w_down @ intermediate

    return {
        "x": x,
        "w_gate": w_gate,
        "w_up": w_up,
        "w_down": w_down,
        "gate": gate,
        "up": up,
        "intermediate": intermediate,
        "output": output,
    }
