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
never read. A call may start at any position, its first query mid-block.

Bidirectional attention bounds the same way: a key past ``n`` is masked
whether it lies before or after a query.
"""

import numpy as np
import pytest
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.operators.mha import MHA

# Llama 3.2 1B's heads, at half its context; eight pipelines as its profile.
HEADS, KV_HEADS, D, SEQ, PIPELINES = 32, 8, 64, 1024, 8


pytestmark = [
    pytest.mark.usefixtures("npu2"),  # a bound device, restored
    pytest.mark.supported_devices("npu2"),
]


@pytest.mark.parametrize(
    "heads,kv_heads,d,seq,scales,attention,calls",
    [
        (HEADS, KV_HEADS, D, SEQ, (1.0, 1.0, 1.0), {}, ((512, 13), (1024, 600))),
        # EmbeddingGemma 2's layers, unscaled, at a length that ends
        # mid-block: a sliding one sees every key within 512 positions,
        # before or after, at d=256; a global one every key, at d=512, its
        # P*V split over two cores. Unscaled, unit inputs would put every
        # score's spread at sqrt(d).
        (
            4,
            2,
            256,
            2048,
            (0.25, 0.25, 1.0),
            dict(causal=False, window=512, scale=1.0),
            ((512, 37), (2048, 1500)),
        ),
        (
            4,
            1,
            512,
            2048,
            (0.25, 0.25, 1.0),
            dict(causal=False, window=None, scale=1.0),
            ((512, 37), (2048, 1500)),
        ),
    ],
    ids=["causal", "sliding", "global"],
)
def test_rows_past_the_valid_length_are_zero(
    heads, kv_heads, d, seq, scales, attention, calls
):
    class Attend(iron.Graph):
        def body(self, q, k, v, *, rows: Scratchpad[np.int32], n: Scratchpad[np.int32]):
            q, k, v = q[:rows], k[:rows], v[:rows]
            return MHA.step(
                q,
                k,
                v,
                heads_interleaved=True,
                kv_interleaved=True,
                s_q=n,
                s_kv=n,
                num_pipelines=PIPELINES,
                **attention,
            )

    rng = np.random.default_rng(0)
    q, k, v = (
        (rng.standard_normal((seq, h, d)) * s).astype(bfloat16)
        for h, s in zip((heads, kv_heads, kv_heads), scales)
    )
    attend = Attend()
    net = attend.compile(q=q.shape, k=k.shape, v=v.shape)
    (mha,) = (s.op for s in net.recording.steps if isinstance(s.op, MHA))
    for rows, n in calls:
        o = np.asarray(net(q, k, v, rows=rows, n=n), dtype=np.float32)
        o = o.reshape(seq, heads, d)
        padding = o[n:rows]
        assert np.isfinite(padding).all(), f"{rows=} {n=}: non-finite padding rows"
        assert not padding.any(), f"{rows=} {n=}: padding rows are not zero"
        expected = attend.reference(q, k, v, rows=rows, n=n)
        expected = np.asarray(expected, dtype=np.float32).reshape(-1, heads, d)
        verdict = compare(
            o[:n],
            expected[:n],
            mha.resolved().tolerance(),
        )
        assert verdict, f"{rows=} {n=}: the valid elements differ: {verdict.detail}"


CHUNK, CACHE = 512, 2048


class Chunk(iron.Graph):
    def __init__(self, window: int | None = None, pipelines: int = PIPELINES):
        self.window, self.pipelines = window, pipelines

    def body(
        self,
        q,
        k,
        v,
        *,
        rows: Scratchpad[np.int32],
        position: Scratchpad[np.int32],
    ):
        return MHA.step(
            q[:rows],
            k[:, : position + 1],
            v[:, : position + 1],
            heads_interleaved=True,
            window=self.window,
            num_pipelines=self.pipelines,
        )


@pytest.mark.parametrize("full_elf", [None, False], ids=["full_elf", "xclbin"])
def test_a_chunk_attends_over_the_cache_before_it(full_elf):
    chunk = Chunk()

    rng = np.random.default_rng(0)
    q = rng.standard_normal((CACHE, HEADS, D)).astype(bfloat16)
    k = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    v = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    net = chunk.compile(q=(CHUNK, HEADS, D), k=k.shape, v=v.shape, full_elf=full_elf)
    # The whole prompt at once: each chunk's rows of it are what the chunk
    # computes.
    mha = MHA(
        num_heads=HEADS, num_KV_heads=KV_HEADS, seq_len=CACHE, heads_interleaved=True
    )
    whole = mha.reference(q, k, v)
    whole = np.asarray(whole, dtype=np.float32).reshape(CACHE, HEADS, D)
    for c, rows in ((0, 13), (1, CHUNK), (2, 100), (3, CHUNK)):
        start = c * CHUNK
        position = start + rows - 1
        o = net(q[start : start + CHUNK], k, v, rows=rows, position=position)
        o = np.asarray(o, dtype=np.float32).reshape(CHUNK, HEADS, D)
        verdict = compare(
            o[:rows],
            whole[start : start + rows],
            mha.resolved().tolerance(),
        )
        assert verdict, f"{c=} {rows=}: the valid elements differ: {verdict.detail}"


@pytest.mark.parametrize("window", [None, 511], ids=["causal", "sliding"])
def test_a_call_starts_its_queries_anywhere(window):
    """Run calls from positions no block divides, as a chat turn's.

    Each query attends over the keys before it, within Gemma 3's window
    if sliding.
    """
    chunk = Chunk(window)
    rng = np.random.default_rng(1)
    q = rng.standard_normal((CACHE, HEADS, D)).astype(bfloat16)
    k = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    v = rng.standard_normal((KV_HEADS, CACHE, D)).astype(bfloat16)
    net = chunk.compile(q=(CHUNK, HEADS, D), k=k.shape, v=v.shape)
    mha = MHA(
        num_heads=HEADS,
        num_KV_heads=KV_HEADS,
        seq_len=CACHE,
        heads_interleaved=True,
        window=window,
    )
    whole = mha.reference(q, k, v)
    whole = np.asarray(whole, dtype=np.float32).reshape(CACHE, HEADS, D)
    for start, rows in ((270, 40), (13, 100), (601, CHUNK), (1500, 77)):
        position = start + rows - 1
        o = net(q[start : start + CHUNK], k, v, rows=rows, position=position)
        o = np.asarray(o, dtype=np.float32).reshape(CHUNK, HEADS, D)
        verdict = compare(
            o[:rows],
            whole[start : start + rows],
            mha.resolved().tolerance(),
        )
        assert verdict, f"{start=} {rows=}: the valid elements differ: {verdict.detail}"


def test_what_lies_past_the_bound_does_not_reach_the_output():
    """Check that the valid rows are bit for bit the same whatever lies past the bound.

    Q past a chunk's rows holds whatever the step before left there, and
    the cache past its last position whatever an earlier prompt did; the
    last block's DMA reads both. Even NaN: P·V reads V's rows past the
    bound, and through bfp16 a row shares its exponent with the seven
    beside it.
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


def test_one_pipeline_fills_k_and_v_past_the_task_queue():
    """Run Gemma 3's prompt chunk on one pipeline.

    K and V are re-read in eight fills per KV group, past the shim's
    queue of four. A fill past it waits for a free slot, which the cores
    free only while O drains.
    """
    heads, kv_heads, d, chunk, cache = 4, 1, 256, 2048, 4096
    rng = np.random.default_rng(2)
    q = rng.standard_normal((chunk, heads, d)).astype(bfloat16)
    k = rng.standard_normal((kv_heads, cache, d)).astype(bfloat16)
    v = rng.standard_normal((kv_heads, cache, d)).astype(bfloat16)
    net = Chunk(511, pipelines=1).compile(q=q.shape, k=k.shape, v=v.shape)
    mha = MHA(
        num_heads=heads,
        num_KV_heads=kv_heads,
        d=d,
        seq_len=chunk,
        heads_interleaved=True,
        window=511,
    )
    rows = 78
    whole = mha.reference(q, k[:, :chunk], v[:, :chunk])
    whole = np.asarray(whole, dtype=np.float32).reshape(chunk, heads, d)
    o = net(q, k, v, rows=rows, position=rows - 1)
    o = np.asarray(o, dtype=np.float32).reshape(chunk, heads, d)
    verdict = compare(o[:rows], whole[:rows], mha.resolved().tolerance())
    assert verdict, f"the valid elements differ: {verdict.detail}"
