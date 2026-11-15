# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What stream-dse solves for the SwiGLU prefill block.

The torch module the workload is exported from, which gives stream-dse the
graph and its shapes, and the mappings, one per partition and GEMM block,
that stream-dse chooses between. Placement is
stream-dse's; a mapping gives each layer's kernel arguments and its fused
groups.
"""

from functools import cache

from iron.common.stream.hardware import ComputeArray
from iron.common.stream.mapping import FusedGroup, StreamMapping

from .op import (
    DOWN,
    FUSED_PARTITION,
    GATE,
    GEMMS,
    LAYERS,
    MUL,
    PARTITIONS,
    POST_OP_PARTITION,
    SILU,
    UP,
)

# The GEMM blocks a candidate seeds its tile search with, as
# (sequence, embedding, hidden), largest first. Only the one-group partition
# is offered each block that fits; the others take the largest, as
# stream-dse's tile search tries every call shape the kernel library measures
# for a group with one GEMM kernel.
GEMM_BLOCKS = ((64, 64, 64), (32, 32, 64))
# The widest embedding a GEMM with post-ops takes per call: beside its float
# accumulator, a core has room for the tile its post-ops read only below the
# 64 block.
POST_OP_EMBEDDING = 32
# The most of a row an elementwise core takes per call when its layer is
# alone in its group: the smallest call the kernel library measures for the
# elementwise kernels.
ELEMENTWISE_WIDTH = 2048
# The fewest columns a GEMM is split over when it shares the array with
# another GEMM of its group.
SHARED_GEMM_COLUMNS = 2


def swiglu_module(embedding_dim: int, hidden_dim: int):
    """Return the block as a ``torch.nn.Module`` with zero ``(out, in)`` weights.

    ``(SiLU(input @ w_gate.T) * (input @ w_up.T)) @ w_down.T`` over
    ``(seq_len, embedding_dim)``. torch is imported here, when a workload
    is exported, and not with the operator.
    """
    import torch  # pyright: ignore[reportMissingImports]
    from torch import nn  # pyright: ignore[reportMissingImports]

    class SwiGLU(nn.Module):
        def __init__(self):
            super().__init__()
            gate_up = (hidden_dim, embedding_dim)
            self.w_gate = nn.Parameter(torch.zeros(gate_up, dtype=torch.bfloat16))
            self.w_up = nn.Parameter(torch.zeros(gate_up, dtype=torch.bfloat16))
            self.w_down = nn.Parameter(
                torch.zeros((embedding_dim, hidden_dim), dtype=torch.bfloat16)
            )

        def forward(self, input):
            linear = nn.functional.linear
            gate = linear(input, self.w_gate)
            up = linear(input, self.w_up)
            return linear(nn.functional.silu(gate) * up, self.w_down)

    return SwiGLU().eval()


@cache
def workload(seq_len: int, embedding_dim: int, hidden_dim: int):
    """Return the workload exported at one problem size, its nodes named ``op.LAYERS``."""
    import torch  # pyright: ignore[reportMissingImports]

    from iron.common.stream.workload import export_workload

    return export_workload(
        swiglu_module(embedding_dim, hidden_dim),
        (torch.zeros(seq_len, embedding_dim, dtype=torch.bfloat16),),
        node_names=LAYERS,
    )


def _row_width(hidden_dim: int) -> int:
    """Return the widest divisor of a row an elementwise core takes per call."""
    return max(
        width
        for width in range(min(hidden_dim, ELEMENTWISE_WIDTH), 0, -1)
        if hidden_dim % width == 0
    )


def mapping(partition: int, block, hidden_dim: int) -> StreamMapping:
    """Return ``partition``'s mapping, its GEMMs seeded at ``block``.

    Alone in their groups, the elementwise kernels read whole rows, so their
    transfers are contiguous; fused with a GEMM they take its output block.
    """
    sequence, embedding, hidden = block
    groups = PARTITIONS[partition]
    post_ops = partition == POST_OP_PARTITION

    def gemm(m, k, n):
        return dict(m=m, k=k, n=n, layout="default", b_col_maj=True)

    if all(len(group) == 1 for group in groups):
        elementwise = dict(layout="contiguous", m=1, n=_row_width(hidden_dim))
    else:
        elementwise = dict(layout="default", m=sequence, n=hidden)
    projection = gemm(
        sequence, min(embedding, POST_OP_EMBEDDING) if post_ops else embedding, hidden
    )
    kernels = {
        GATE: projection,
        UP: projection,
        SILU: elementwise,
        MUL: elementwise,
        DOWN: gemm(sequence, hidden, embedding),
    }
    return StreamMapping(
        kernels,
        [
            FusedGroup(
                group,
                post_ops=[layer for layer in group if post_ops and layer not in GEMMS],
            )
            for group in groups
        ],
    )


def refusal(
    partition: int, block, seq_len: int, embedding_dim: int, hidden_dim: int, grid
) -> str | None:
    """Return why ``grid`` cannot run ``partition`` at ``block`` and this size, else None.

    Each row of cores takes a sequence block, and each GEMM splits its
    embedding and hidden tiles over its columns: all of them where it is
    the only GEMM of its group.
    """
    sequence, embedding, hidden = block
    alone = all(len(set(group) & set(GEMMS)) <= 1 for group in PARTITIONS[partition])
    columns = grid.num_columns if alone else SHARED_GEMM_COLUMNS
    if seq_len % grid.num_rows or seq_len < sequence * grid.num_rows:
        return (
            f"seq_len ({seq_len}) must be a multiple of {grid.num_rows} and at "
            f"least {sequence * grid.num_rows}"
        )
    for name, size, tile in (
        ("embedding_dim", embedding_dim, embedding),
        ("hidden_dim", hidden_dim, hidden),
    ):
        if size % (tile * columns):
            return f"{name} ({size}) must be a multiple of {tile * columns}"
    return None


def candidates(
    seq_len, embedding_dim, hidden_dim, dev, partition=None, gemm_block=None
) -> list[StreamMapping]:
    """Return the mappings stream-dse chooses between.

    Every partition at the GEMM blocks that fit, or only the ``partition``
    and ``gemm_block`` named.

    Raises:
        ValueError: None fits.
    """
    grid = ComputeArray.from_device(dev)
    blocks = GEMM_BLOCKS if gemm_block is None else (tuple(gemm_block),)
    chosen, refused = [], []
    for number in PARTITIONS if partition is None else (partition,):
        fitting = []
        for block in blocks:
            why = refusal(number, block, seq_len, embedding_dim, hidden_dim, grid)
            if why is None:
                fitting.append(block)
            else:
                refused.append(f"partition {number}, block {block}: {why}")
        if number != FUSED_PARTITION:
            fitting = fitting[:1]
        chosen += [mapping(number, block, hidden_dim) for block in fitting]
    if not chosen:
        raise ValueError(f"no SwiGLU mapping fits: {refused}")
    return chosen
