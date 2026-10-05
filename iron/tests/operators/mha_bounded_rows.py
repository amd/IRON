#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA under a row bound with fewer valid rows than the bound, on a device.

A prompt runs MHA over ``rows`` (the bound, a multiple of what its pipelines
take at once) of which the first ``n`` are the prompt: ``s_q = s_kv = n``.
A query row past ``n`` attends over nothing, so its row sum is 0, and it must
come out 0, not ``0 * (1 / 0)``: a NaN there reaches the next layer's K and
V through the residual, and from there every valid row. The padding holds
whatever the step before left, so here it is random rather than zeros.

A chunk of a longer prompt runs MHA over the cache it extends: its queries
are the last rows of ``k[:, :position + 1]``, so a chunk at any offset
attends causally over every key before it, and the keys past the bound are
never read.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.mha import MHA

# Llama 3.2 1B's heads, at half its context; eight pipelines as its profile.
HEADS, KV_HEADS, D, SEQ, PIPELINES = 32, 8, 64, 1024, 8


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_rows_past_the_valid_length_are_zero(npu_runtime):
    class Attend(iron.Graph):
        def body(self, q, k, v, *, rows: Scratchpad[np.int32], n: Scratchpad[np.int32]):
            q, k, v = q[:rows], k[:rows], v[:rows]
            return MHA(
                q,
                k,
                v,
                heads_interleaved=True,
                kv_interleaved=True,
                s_q=n,
                s_kv=n,
                num_pipelines=PIPELINES,
            )

    attend = Attend()

    rng = np.random.default_rng(0)
    q = rng.standard_normal((SEQ, HEADS, D)).astype(bfloat16)
    k = rng.standard_normal((SEQ, KV_HEADS, D)).astype(bfloat16)
    v = rng.standard_normal((SEQ, KV_HEADS, D)).astype(bfloat16)
    net = attend.compile(q=q.shape, k=k.shape, v=v.shape)
    reference = MHA(
        num_heads=HEADS,
        num_KV_heads=KV_HEADS,
        seq_len=SEQ,
        heads_interleaved=True,
        kv_interleaved=True,
    )
    for rows, n in ((512, 13), (1024, 600)):
        o = np.asarray(net(q, k, v, rows=rows, n=n), dtype=np.float32)
        o = o.reshape(SEQ, HEADS, D)
        padding = o[n:rows]
        assert np.isfinite(padding).all(), f"{rows=} {n=}: non-finite padding rows"
        assert not padding.any(), f"{rows=} {n=}: padding rows are not zero"
        expected = reference.reference(q, k, v, s_q=n, s_kv=n)
        expected = np.asarray(expected, dtype=np.float32).reshape(SEQ, HEADS, D)
        verdict = verify_buffer(
            o[:n],
            "O",
            expected[:n],
            tolerance=Tolerance.relative(0.04, 0.15, max_mismatch_frac=0.005),
        )
        assert verdict, f"{rows=} {n=}: the valid elements differ: {verdict.detail}"


CHUNK, CACHE = 512, 2048


class Chunk(iron.Graph):
    def body(
        self,
        q,
        k,
        v,
        *,
        rows: Scratchpad[np.int32],
        position: Scratchpad[np.int32],
    ):
        return MHA(
            q[:rows],
            k[:, : position + 1],
            v[:, : position + 1],
            heads_interleaved=True,
            num_pipelines=PIPELINES,
        )


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "boundaries", [None, iron.each_step], ids=["full_elf", "xclbin"]
)
def test_a_chunk_attends_over_the_cache_before_it(npu_runtime, boundaries):
    chunk = Chunk()

    rng = np.random.default_rng(0)
    q = rng.standard_normal((CACHE, HEADS, D)).astype(bfloat16)
    k = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    v = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    net = chunk.compile(
        q=(CHUNK, HEADS, D), k=k.shape, v=v.shape, boundaries=boundaries
    )
    # The whole prompt at once: each chunk's rows of it are what the chunk
    # computes.
    whole = MHA(
        num_heads=HEADS, num_KV_heads=KV_HEADS, seq_len=CACHE, heads_interleaved=True
    ).reference(q, k, v)
    whole = np.asarray(whole, dtype=np.float32).reshape(CACHE, HEADS, D)
    for c, rows in ((0, 13), (1, CHUNK), (2, 100), (3, CHUNK)):
        start = c * CHUNK
        position = start + rows - 1
        o = net(q[start : start + CHUNK], k, v, rows=rows, position=position)
        o = np.asarray(o, dtype=np.float32).reshape(CHUNK, HEADS, D)
        verdict = verify_buffer(
            o[:rows],
            "O",
            whole[start : start + rows],
            tolerance=Tolerance.relative(0.04, 0.15, max_mismatch_frac=0.005),
        )
        assert verdict, f"{c=} {rows=}: the valid elements differ: {verdict.detail}"


@pytest.mark.supported_devices("npu2")
def test_what_lies_past_the_bound_does_not_reach_the_output(npu_runtime):
    """Q past a chunk's rows holds whatever the step before left there, and
    the cache past its last position whatever an earlier prompt did; the
    last block's DMA reads both. The valid rows are bit for bit the same
    whatever they hold, even NaN: P·V reads V's rows past the bound, and
    through bfp16 a row shares its exponent with the seven beside it.
    """
    net = Chunk().compile(
        q=(CHUNK, HEADS, D), k=(KV_HEADS, CACHE, D), v=(KV_HEADS, CACHE, D)
    )
    rng = np.random.default_rng(0)
    q = rng.standard_normal((CHUNK, HEADS, D)).astype(bfloat16)
    k = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    v = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    rows = 101  # ends mid-block and mid-group of eight
    runs = {}
    for fill in (0, 1000, np.nan):
        stale = [t.copy() for t in (q, k, v)]
        for t in (stale[0][rows:], stale[1][:, rows:], stale[2][:, rows:]):
            t[...] = t.astype(np.float32) * fill if fill == 1000 else fill
        o = net(*stale, rows=rows, position=rows - 1)
        runs[fill] = np.asarray(o).view(np.uint16).reshape(CHUNK, -1)[:rows].copy()
    for fill in (1000, np.nan):
        differ = np.flatnonzero((runs[fill] != runs[0]).any(axis=1))
        assert not differ.size, f"{fill=}: valid rows {differ} differ"
