# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The descriptors Copy issues for the copies llama makes, pinned.

The descriptors are recorded as (offset, sizes, strides) per channel,
exactly, and the copies written as views must issue them.
"""

from typing import Any

import aie.utils as aie_utils
import pytest

from iron.common import Incompatible
from iron.common.tiling import Walk
from iron.operators.copy import Copy, _kv_slot

pytestmark = pytest.mark.usefixtures("npu2")

G, D, L, E, N = 8, 64, 128, 2048, 16  # kv groups, head dim, context, embed, rows

# One token's (G, D) keys into row `pos` of the (G, L, D) cache:
# Copy(k, keys[:, pos]), the row a per-call value.
ROW_INTO_CACHE = dict(
    src=Walk.of((G, D)),
    dst=Walk.slice((G, L, D), (slice(None), 0)),
    input_buffer_size=G * D,
    output_buffer_size=G * L * D,
    num_channels=1,
)
# N tokens' (N, G, D) keys, heads interleaved per token, into the first N
# rows: Copy(k.reshape(N, G, D).transpose(1, 0, 2), keys[:, :N]).
ROWS_INTO_CACHE = dict(
    src=Walk.permuted((N, G, D), (1, 0, 2)),
    dst=Walk.slice((G, L, D), (slice(None), slice(0, N))),
    input_buffer_size=N * G * D,
    output_buffer_size=G * L * D,
    tile_size=1024,
    num_channels=1,
)
# The last prompt row of (4, E), selected by the per-call index `last`:
# Copy(x[last]).
LAST_ROW = dict(
    src=Walk.slice((4, E), (0,)),
    input_buffer_size=4 * E,
    output_buffer_size=E,
    num_channels=1,
)

PINNED: dict[str, tuple[dict[str, Any], list, list]] = {
    "row_into_cache": (
        ROW_INTO_CACHE,
        [[(0, (1, 1, 1, 512), (0, 0, 0, 1))]],
        [[(0, (1, 1, 8, 64), (0, 0, 8192, 1))]],
    ),
    "rows_into_cache": (
        ROWS_INTO_CACHE,
        [[(0, (1, 8, 16, 64), (0, 64, 512, 1))]],
        [[(0, (1, 8, 16, 64), (0, 8192, 64, 1))]],
    ),
    "last_row": (
        LAST_ROW,
        [[(0, (1, 1, 1, 2048), (0, 0, 0, 1))]],
        [[(0, (1, 1, 1, 2048), (0, 0, 0, 1))]],
    ),
    "kv_slot5": (
        _kv_slot(128, 5),
        [[(0, (1, 1, 1, 512), (0, 0, 0, 1))]],
        [[(320, (1, 1, 8, 64), (0, 0, 8192, 1))]],
    ),
    "kv_slot5_two_channels": (
        _kv_slot(128, 5, num_channels=2),
        [[(0, (1, 1, 8, 32), (0, 0, 64, 1))], [(32, (1, 1, 8, 32), (0, 0, 64, 1))]],
        [
            [(320, (1, 1, 8, 32), (0, 0, 8192, 1))],
            [(352, (1, 1, 8, 32), (0, 0, 8192, 1))],
        ],
    ),
}


def _taps(op, buffer, walk):
    return [
        [(a.offset, a.sizes, a.strides) for a, dim in channel if dim is None]
        for channel in op._taps(buffer, walk)
    ]


@pytest.mark.parametrize("name", sorted(PINNED))
def test_copy_issues_these_descriptors(name):
    kwargs, ins, outs = PINNED[name]
    op = Copy(**kwargs).resolved(aie_utils.get_current_device())
    assert _taps(op, op.x, op.src) == ins
    assert _taps(op, op.y, op.dst) == outs


def test_a_bounded_axis_keeps_its_slot_and_names_it():
    """A cache write of n rows, ``Copy(k.transpose(1, 0, 2), keys[:, :n])``:
    the bounded axis is one exact descriptor dimension per channel, the one
    a call patches, and the reference moves the bounded rows alone.
    """
    import dataclasses

    import numpy as np

    N, G, D, L = 16, 4, 8, 32
    src = dataclasses.replace(Walk.permuted((N, G, D), (1, 0, 2)), bounded=1)
    dst = dataclasses.replace(
        Walk.slice((G, L, D), (slice(None), slice(0, N))), bounded=1
    )
    op = Copy(
        src=src, dst=dst, input_buffer_size=N * G * D, output_buffer_size=G * L * D
    ).resolved(aie_utils.get_current_device())
    assert [
        [(a.sizes, a.strides, dim) for a, dim in ch] for ch in op._taps(op.x, src)
    ] == [[((1, G, N, D), (0, D, G * D, 1), 2)]]
    assert [[(a.sizes, dim) for a, dim in ch] for ch in op._taps(op.y, dst)] == [
        [((1, G, N, D), 2)]
    ]
    x = np.arange(N * G * D, dtype=np.float32).reshape(N, G, D)
    y = np.zeros((G, L, D), dtype=np.float32)
    op.reference(x, y, src_valid=5, dst_valid=5)
    assert (y[:, :5] == x[:5].transpose(1, 0, 2)).all() and not y[:, 5:].any()
    flat = Copy(
        src=dataclasses.replace(Walk.of((N,)), bounded=0),
        input_buffer_size=N,
        num_channels=2,
    ).resolved(aie_utils.get_current_device())
    with pytest.raises(Incompatible, match="channels split"):
        flat._taps(flat.x, flat.src)
