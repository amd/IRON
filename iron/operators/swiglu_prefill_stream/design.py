# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What stream-dse solves for the SwiGLU prefill block.

The torch module the workload is exported from, and the mappings, one per
partition and GEMM block, that stream-dse chooses between. Placement is
stream-dse's; a mapping gives each layer's kernel arguments and its fused
groups.
"""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

from functools import cache

import torch
from torch import nn

from iron.common.stream.hardware import ComputeArray
from iron.common.stream.mapping import FusedGroup
from iron.common.stream.workload import export_workload

from .op import DOWN, GATE, LAYERS, MUL, PARTITIONS, RESULTS, SILU, UP

# Each GEMM block a candidate seeds its tile search with, as
# (sequence, embedding, hidden), largest first.
GEMM_BLOCKS = ((64, 64, 64), (32, 32, 64))
# The widest piece of a row one elementwise core takes when it has a layer
# to itself.
ELEMENTWISE_WIDTH = 2048


class SwiGLU(nn.Module):
    """``(SiLU(input @ w_gate) * (input @ w_up)) @ w_down`` over ``(seq_len, embedding_dim)``."""

    def __init__(self, embedding_dim: int, hidden_dim: int):
        super().__init__()
        gate_up = (embedding_dim, hidden_dim)
        self.w_gate = nn.Parameter(torch.zeros(gate_up, dtype=torch.bfloat16))
        self.w_up = nn.Parameter(torch.zeros(gate_up, dtype=torch.bfloat16))
        self.w_down = nn.Parameter(
            torch.zeros((hidden_dim, embedding_dim), dtype=torch.bfloat16)
        )

    def forward(self, input):
        gate = input @ self.w_gate
        up = input @ self.w_up
        return (torch.nn.functional.silu(gate) * up) @ self.w_down


@cache
def workload(seq_len: int, embedding_dim: int, hidden_dim: int):
    """Return the workload exported at one problem size, named as ``op`` names it."""
    return export_workload(
        SwiGLU(embedding_dim, hidden_dim).eval(),
        (torch.zeros(seq_len, embedding_dim, dtype=torch.bfloat16),),
        node_names=list(LAYERS),
        result_names=RESULTS,
    )


def _row_width(hidden_dim: int) -> int:
    """Return how much of a row an elementwise core with a layer to itself takes at once."""
    if hidden_dim <= ELEMENTWISE_WIDTH:
        return hidden_dim
    return max(w for w in range(ELEMENTWISE_WIDTH, 0, -1) if hidden_dim % w == 0)


def mapping(k: int, block, hidden_dim: int) -> tuple[dict[str, dict], list[FusedGroup]]:
    """Return partition ``k``'s kernel arguments and fused groups at GEMM block ``block``.

    Split per layer, the elementwise kernels read whole rows so their
    transfers are contiguous; fused behind a GEMM they take its output
    block.
    """
    sequence, embedding, hidden = block

    def gemm(m, k, n):
        return dict(m=m, k=k, n=n, layout="default")

    if len(PARTITIONS[k]) == len(LAYERS):
        elementwise = dict(layout="contiguous", m=1, n=_row_width(hidden_dim))
    else:
        elementwise = dict(layout="default", m=sequence, n=hidden)
    kernels = {
        GATE: gemm(sequence, embedding, hidden),
        UP: gemm(sequence, embedding, hidden),
        SILU: elementwise,
        MUL: elementwise,
        DOWN: gemm(sequence, hidden, embedding),
    }
    groups = [
        FusedGroup(f"Fused_Group_{i + 1}", layers)
        for i, layers in enumerate(PARTITIONS[k])
    ]
    return kernels, groups


def fits(k: int, block, seq_len: int, embedding_dim: int, hidden_dim: int, grid):
    """Return why no core of ``grid`` can take ``block`` at this size, else None."""
    sequence, embedding, hidden = block
    split = grid.num_columns if len(PARTITIONS[k]) == len(LAYERS) else 2
    if seq_len % grid.num_rows or seq_len < sequence * grid.num_rows:
        return (
            f"seq_len ({seq_len}) must be a multiple of {grid.num_rows} and at "
            f"least {sequence * grid.num_rows}"
        )
    for name, size, tile in (
        ("embedding_dim", embedding_dim, embedding),
        ("hidden_dim", hidden_dim, hidden),
    ):
        if size % (tile * split):
            return f"{name} ({size}) must be a multiple of {tile * split}"
    return None


def candidates(seq_len, embedding_dim, hidden_dim, dev, k=None, gemm_block=None):
    """Return the mappings stream-dse chooses between, with the partition and block of each.

    Every partition and block that fits, or only those ``k`` and
    ``gemm_block`` name.

    Raises:
        ValueError: None fits.
    """
    grid = ComputeArray.from_device(dev)
    chosen, refused = [], []
    for partition in PARTITIONS if k is None else (k,):
        for block in GEMM_BLOCKS if gemm_block is None else (tuple(gemm_block),):
            why = fits(partition, block, seq_len, embedding_dim, hidden_dim, grid)
            if why is None:
                chosen.append(
                    ((partition, block), mapping(partition, block, hidden_dim))
                )
            else:
                refused.append(f"k={partition} block {block}: {why}")
    if not chosen:
        raise ValueError(f"no SwiGLU mapping fits: {refused}")
    return chosen
