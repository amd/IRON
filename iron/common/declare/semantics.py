# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an overlay computes, as a fusion pass needs to know it.

:meth:`Overlay.semantics` returns one of these. It is stated per fifo
object, which is extent-free; where those objects sit in a host buffer is
each buffer's :class:`~iron.common.declare.order.Order`, so the two
together say what an output element depends on in buffer terms.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Local:
    """Output object ``k`` depends only on input object ``k`` of each input
    stream, and within it each output element only on its aligned block of
    ``block`` elements (counted in output elements; a dtype-changing kernel
    reads the same block's inputs in its own packing). ``block == 1`` is
    elementwise; a norm, a softmax, RoPE are a row.
    """

    block: int


@dataclass(frozen=True)
class Contraction:
    """A reduction over an axis the output does not have (GEMV's and GEMM's
    K). ``final_at_release``: an output object is complete when the core
    releases it, so an epilogue may run on it there."""

    final_at_release: bool


@dataclass(frozen=True)
class Movement:
    """Re-indexing only: every output element is an input element, and the
    orders (with, on a core, a permutation inside each object) say which.
    ``has_cores`` is False for a DMA-only overlay, which has no core to host
    another kernel."""

    has_cores: bool


@dataclass(frozen=True)
class Composite:
    """A multi-stage pipeline with dataflow of its own (attention)."""


@dataclass(frozen=True)
class Undeclared:
    """Neither declared nor derivable; ``reason`` says why."""

    reason: str


Semantics = Local | Contraction | Movement | Composite | Undeclared
