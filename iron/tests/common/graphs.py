# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graphs more than one test module traces, tunes or runs."""

import numpy as np

import iron
from iron.common import Carried, Scratchpad
from iron.operators import GEMM, ElementwiseAdd, ElementwiseMul, RoPE, SiLU
from iron.operators.copy import Copy


class Rotate(iron.Graph):
    """RoPE over the first `n` positions, `n` given per call."""

    def body(self, x, angles, *, n: Scratchpad[np.int32]):
        return RoPE(x[:n], angles[:n])


class Project(iron.Graph):
    """The first `n` rows of `x` projected by `w`."""

    def body(self, x, w, *, n: Scratchpad[np.int32]):
        return GEMM(x[:n], w, b_col_maj=True)


class Walk(iron.Graph):
    """Walks a linked list one node per call: the next node is gathered from
    the successor table on the device, the step count is an expression of
    the current one. It takes no tensor.
    """

    def __init__(self, successor):
        self.successor = iron.weight(successor)

    def body(self, *, node: Carried[np.int32], steps: Carried[np.int32]):
        nxt = Copy(self.successor[node], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)


class Trail(iron.Graph):
    """Walks a linked list and records each node at the step count, in a
    state of `steps` + 1 entries. The version with `jump` starts from a
    table the host gives, at a plain per-call value; the one without
    follows the list from `node`.
    """

    def __init__(self, successor, steps: int):
        self.successor = iron.weight(successor)
        self.trail = iron.state((steps + 1,), np.int32, name="trail")

    def body(
        self,
        jump=None,
        *,
        node: Carried[np.int32],
        steps: Carried[np.int32],
        skip: Scratchpad[np.int32],
    ):
        if jump is None:
            nxt = Copy(self.successor[node], dtype=np.int32)
        else:
            nxt = Copy(jump[skip], dtype=np.int32)
        Copy(nxt, self.trail[steps], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)


class Chain(iron.Graph):
    """add, silu, mul, add, silu: three designs, two recurring, each on
    `columns` columns, or as wide as it resolves to when None.
    """

    def __init__(self, size: int, tile: int, columns: int | None = None):
        super().__init__()
        shape = dict(size=size, tile_size=tile)
        if columns is not None:
            shape["num_aie_columns"] = columns
        self.add = ElementwiseAdd(**shape)
        self.silu = SiLU(**shape)
        self.mul = ElementwiseMul(**shape)

    def body(self, a, b):
        x = self.mul(self.silu(self.add(a, b)), b)
        return self.silu(self.add(x, b))


class Adds(iron.Graph):
    """`x` plus `w`, `n` times over, by one add."""

    def __init__(self, add, n: int):
        self.add = add
        self.n = n

    def body(self, x, w):
        for _ in range(self.n):
            x = self.add(x, w)
        return x
