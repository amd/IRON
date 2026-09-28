# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The descriptors Copy issues for the copies llama makes, pinned.

Each copy is built, and every shim task of its runtime sequence recorded as
(lane, offset, sizes, strides), exactly: the copies written as views must
issue them.
"""

from typing import Any

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern

from iron.common import Incompatible
from iron.operators.copy import Copy
from iron.tests.common.build import generated_sequence

pytestmark = pytest.mark.usefixtures("npu2")

G, D, L, E, N = 8, 64, 128, 2048, 16  # kv groups, head dim, context, embed, rows


def _permuted(n, g, d) -> TensorAccessPattern:
    """An (n, g, d) buffer read as (g, n, d): ``x.transpose(1, 0, 2)``."""
    return TensorAccessPattern((n, g, d), 0, [g, n, d], [d, g * d, 1])


# One token's (G, D) keys into row `pos` of the (G, L, D) cache:
# Copy(k, keys[:, pos]), the row a per-call value.
ROW_INTO_CACHE = dict(
    src=TensorAccessPattern.from_slice((G, D), ()),
    dst=TensorAccessPattern.from_slice((G, L, D), np.s_[:, 0]),
    input_buffer_size=G * D,
    output_buffer_size=G * L * D,
)
# N tokens' (N, G, D) keys, heads interleaved per token, into the first N
# rows: Copy(k.reshape(N, G, D).transpose(1, 0, 2), keys[:, :N]).
ROWS_INTO_CACHE = dict(
    src=_permuted(N, G, D),
    dst=TensorAccessPattern.from_slice((G, L, D), np.s_[:, 0:N]),
    input_buffer_size=N * G * D,
    output_buffer_size=G * L * D,
    tile_size=1024,
)
# The last prompt row of (4, E), selected by the per-call index `last`:
# Copy(x[last]).
LAST_ROW = dict(
    src=TensorAccessPattern.from_slice((4, E), np.s_[0]),
    input_buffer_size=4 * E,
    output_buffer_size=E,
)
# The same row at slot 5, on one channel and on two.
SLOT5 = dict(ROW_INTO_CACHE, dst=TensorAccessPattern.from_slice((G, L, D), np.s_[:, 5]))
SLOT5_TWO_CHANNELS = dict(SLOT5, num_channels=2)

PINNED: dict[str, tuple[dict[str, Any], list]] = {
    "row_into_cache": (
        ROW_INTO_CACHE,
        [
            ("fifo_in_0", 0, "1, 1, 8, 64", "0, 0, 64, 1"),
            ("fifo_out_0", 0, "1, 1, 8, 64", "0, 0, 8192, 1"),
        ],
    ),
    "rows_into_cache": (
        ROWS_INTO_CACHE,
        [
            ("fifo_in_0", 0, "1, 8, 16, 64", "0, 64, 512, 1"),
            ("fifo_out_0", 0, "1, 8, 16, 64", "0, 8192, 64, 1"),
        ],
    ),
    "last_row": (
        LAST_ROW,
        [
            ("fifo_in_0", 0, "1, 1, 1, 2048", "0, 0, 0, 1"),
            ("fifo_out_0", 0, "1, 1, 1, 2048", "0, 0, 0, 1"),
        ],
    ),
    "slot5": (
        SLOT5,
        [
            ("fifo_in_0", 0, "1, 1, 8, 64", "0, 0, 64, 1"),
            ("fifo_out_0", 320, "1, 1, 8, 64", "0, 0, 8192, 1"),
        ],
    ),
    "slot5_two_channels": (
        SLOT5_TWO_CHANNELS,
        [
            ("fifo_in_0", 0, "1, 1, 8, 32", "0, 0, 64, 1"),
            ("fifo_out_0", 320, "1, 1, 8, 32", "0, 0, 8192, 1"),
            ("fifo_in_1", 32, "1, 1, 8, 32", "0, 0, 64, 1"),
            ("fifo_out_1", 352, "1, 1, 8, 32", "0, 0, 8192, 1"),
        ],
    ),
}


def _bounded(op: Copy) -> Copy:
    """``op`` as a graph builds it, its per-call sizes bound."""
    op.use_value("src_valid")
    op.use_value("dst_valid")
    return op


@pytest.mark.parametrize("name", sorted(PINNED))
def test_copy_issues_these_descriptors(name):
    kwargs, tasks = PINNED[name]
    _, issued = generated_sequence(Copy(**kwargs))
    assert [(t.lane, t.offset, t.sizes, t.strides) for t in issued] == tasks


def test_a_bounded_axis_lands_on_d2_and_names_it():
    """A cache write of n rows, ``Copy(k.transpose(1, 0, 2), keys[:, :n])``:
    the bounded axis is one exact descriptor dimension per channel, D2 (the
    one a length patch bounds, with no wrap), the group axis iterating
    outside it; and the reference moves the bounded rows alone.
    """
    N, G, D, L = 16, 4, 8, 32
    op = Copy(
        src=_permuted(N, G, D),
        dst=TensorAccessPattern.from_slice((G, L, D), np.s_[:, 0:N]),
        src_bound=1,
        dst_bound=1,
        input_buffer_size=N * G * D,
        output_buffer_size=G * L * D,
    )
    _, (fill, drain) = generated_sequence(_bounded(op))
    assert (fill.sizes, fill.strides) == (f"{G}, {N}, 1, {D}", f"{D}, {G * D}, 0, 1")
    assert (drain.sizes, drain.strides) == (f"{G}, {N}, 1, {D}", f"{L * D}, {D}, 0, 1")
    assert fill.size_parameter.endswith("src_valid")
    assert drain.size_parameter.endswith("dst_valid")
    x = np.arange(N * G * D, dtype=np.float32).reshape(N, G, D)
    y = np.zeros((G, L, D), dtype=np.float32)
    op.reference(x, y, src_valid=5, dst_valid=5)
    assert (y[:, :5] == x[:5].transpose(1, 0, 2)).all() and not y[:, 5:].any()
    flat = Copy(
        src=TensorAccessPattern.from_slice((N,), ()),
        src_bound=0,
        input_buffer_size=N,
        num_channels=2,
    )
    with pytest.raises(Incompatible, match="channels split"):
        generated_sequence(_bounded(flat))


def test_a_bounded_axis_past_the_d1_wrap_still_packs():
    """Llama's prompt cache write, 2048 rows into a 2048-row cache: past
    D1's 1023 wrap, so the bounded axis packs only on D2.
    """
    N, G, D = 2048, 8, 64
    op = Copy(
        src=_permuted(N, G, D),
        dst=TensorAccessPattern.from_slice((G, N, D), np.s_[:, 0:N]),
        src_bound=1,
        dst_bound=1,
        input_buffer_size=N * G * D,
        output_buffer_size=G * N * D,
    )
    _, tasks = generated_sequence(_bounded(op))
    assert [t.sizes for t in tasks] == [f"{G}, {N}, 1, {D}"] * 2
