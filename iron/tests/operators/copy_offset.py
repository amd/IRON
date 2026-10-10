#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Copy's per-call index into the cache, on a device.

Decode drives the KV-cache write through ``out_offset`` bound to a per-call
value; every declared case bakes the offset in at compile time instead, so
the path the application runs had no coverage. This drives it across three
token positions on one compiled graph, checking the whole cache each time so
a mis-scaled addend (elements vs bytes) cannot land in the wrong slot
undetected.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.design import BdLimits
from iron.operators.copy import Copy

# Llama's KV-cache write, shrunk: (n_kv_groups, seq, head_dim), one token's
# keys landing in slot t of every group.
N_KV, HEAD_DIM, SEQ = 8, 64, 128


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_the_cache_offset_is_applied_per_call(npu_runtime):
    cache = iron.state((N_KV, SEQ, HEAD_DIM), name="cache")

    class Write(iron.Graph):
        def body(self, x, *, pos: Scratchpad[np.int32]):
            Copy(x, cache[:, pos])

    write = Write()

    net = write.compile(x=(N_KV, HEAD_DIM))
    assert net.plan.image == "elf", "only the full ELF carries a scratchpad"

    expected = np.zeros((N_KV, SEQ, HEAD_DIM), dtype=np.float32)
    net.write(cache, expected)
    rng = np.random.default_rng(0)
    for slot in (0, 5, SEQ - 1):
        x = rng.standard_normal((N_KV, HEAD_DIM)).astype(bfloat16)
        expected[:, slot, :] = x.astype(np.float32)
        # The value is the row; the library scales it to an element offset.
        write(x, pos=slot)
        got = np.asarray(net.read(cache), dtype=np.float32).reshape(expected.shape)
        wrong = np.argwhere(got != expected)
        assert not len(
            wrong
        ), f"slot {slot}: {len(wrong)} elements differ, first {wrong[:4]}"


# A prompt chunk's keys, heads interleaved per token as the projection
# writes them, into the chunk's rows of a four-chunk cache.
CHUNK, CHUNKS = 64, 4


@pytest.mark.supported_devices("npu2")
def test_a_chunk_lands_in_its_rows_of_the_cache(npu_runtime):
    cache = iron.state((N_KV, CHUNKS * CHUNK, HEAD_DIM), name="cache")

    class Write(iron.Graph):
        def body(self, x, *, chunk: Scratchpad[np.int32], rows: Scratchpad[np.int32]):
            x = x[:rows].reshape(CHUNK, N_KV, HEAD_DIM).transpose(1, 0, 2)
            Copy(x, cache.reshape(N_KV, CHUNKS, CHUNK, HEAD_DIM)[:, chunk, :rows])

    write = Write()
    net = write.compile(x=(CHUNK, N_KV * HEAD_DIM))

    expected = np.zeros((N_KV, CHUNKS * CHUNK, HEAD_DIM), dtype=np.float32)
    net.write(cache, expected)
    rng = np.random.default_rng(0)
    for chunk, rows in ((0, CHUNK), (1, 13), (2, 1), (3, 37), (1, 50)):
        x = rng.standard_normal((CHUNK, N_KV * HEAD_DIM)).astype(bfloat16)
        start = chunk * CHUNK
        rotated = x[:rows].reshape(rows, N_KV, HEAD_DIM).transpose(1, 0, 2)
        expected[:, start : start + rows] = rotated.astype(np.float32)
        write(x, chunk=chunk, rows=rows)
        got = np.asarray(net.read(cache), dtype=np.float32).reshape(expected.shape)
        wrong = np.argwhere(got != expected)
        assert not len(
            wrong
        ), f"{chunk=} {rows=}: {len(wrong)} elements differ, first {wrong[:4]}"


# Rows of 4 out of 6, two blocks of 1031 per group: a pattern no one
# descriptor holds, so the compiler splits it and the offset patches each piece.
GROUPS, SLOTS, BLOCKS, ROWS, WIDE, KEEP = 3, 4, 2, 1031, 6, 4


@pytest.mark.supported_devices("npu2")
def test_the_offset_moves_every_piece_of_a_split_pattern(npu_runtime):
    cache = iron.state((GROUPS, SLOTS, BLOCKS, ROWS, WIDE), name="cache")

    class Write(iron.Graph):
        def body(self, x, *, pos: Scratchpad[np.int32]):
            Copy(x, cache[:, pos, :, :, :KEEP])

    write = Write()
    net = write.compile(x=(GROUPS, BLOCKS, ROWS, KEEP))
    view = TensorAccessPattern.full((GROUPS, SLOTS, BLOCKS, ROWS, WIDE))
    shim = BdLimits.of(aie_utils.get_current_device(), 0, 0)
    assert not shim.fits(view[:, 0, :, :, :KEEP], bfloat16)

    expected = np.zeros((GROUPS, SLOTS, BLOCKS, ROWS, WIDE), dtype=np.float32)
    net.write(cache, expected)
    rng = np.random.default_rng(0)
    for slot in (0, 2, SLOTS - 1):
        x = rng.standard_normal((GROUPS, BLOCKS, ROWS, KEEP)).astype(bfloat16)
        expected[:, slot, :, :, :KEEP] = x.astype(np.float32)
        write(x, pos=slot)
        got = np.asarray(net.read(cache), dtype=np.float32).reshape(expected.shape)
        wrong = np.argwhere(got != expected)
        assert not len(
            wrong
        ), f"slot {slot}: {len(wrong)} elements differ, first {wrong[:4]}"
