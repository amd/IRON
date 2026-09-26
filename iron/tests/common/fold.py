# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folds, device-free: which movements go where, and that what each core
receives is unchanged.

The functional checks run the DMA on the host: a buffer's order says which
elements each slot carries, and the GEMV core is a matrix-vector product
per batch, so the arrays a folded and an unfolded graph compute can be
compared without a device. The hardware tests (iron/tests/infrastructure/
fold.py) run the same graphs on one.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.device import from_name

import iron
from iron.common.declare import Scratchpad
from iron.common.declare.refold import Reorder, Side
from iron.common.design.build import generator_for
from iron.common.graph.fold import Fold, FoldAll, Refused, apply, candidates
from iron.common.tiling import legalize
from iron.operators.gemv.op import GEMV
from iron.operators.repeat import Repeat
from iron.operators.strided_copy import StridedCopy

G, REP, L, D, COLS = 2, 4, 128, 64, 2
H = G * REP


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    dev = from_name("npu2", n_cols=8)
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


def _scores_graph(keys, *, write_between=None):
    """Grouped-query scores: each group's keys repeated per head, then a
    batched GEMV against the heads' queries."""

    @iron.graph
    def scores(q):
        k_all = Repeat(keys, repeat=REP, transfer_size=D)
        if write_between is not None:
            write_between(q)
        return GEMV(
            k_all.reshape(H, L, D),
            q,
            num_aie_columns=COLS,
            tile_size_input=4,
            tile_size_output=L // COLS,
        )

    return scores.trace(q=(H, D))


def _stream(values, order, slot, offset=0):
    return values[order.indices(slot) + offset]


def _gemv(op, a_values, b_values, c_out, c_offset=0):
    """The GEMV array on the host: per column, batch k's rows of A times
    batch k's vector, into batch k's rows of C, in the order streamed."""
    a, b, c = (op.issued_order(buf) for buf in (op.A, op.B, op.C))
    nb, K = op.num_batches, op.ov.K
    for col in range(op.ov.num_aie_columns):
        a_s = _stream(a_values, a, col).astype(np.float32)
        b_s = _stream(b_values, b, col).astype(np.float32)
        where = c.indices(col) + c_offset
        rows = where.size // nb
        for k in range(nb):
            m = a_s[k * rows * K : (k + 1) * rows * K].reshape(rows, K)
            c_out[where[k * rows : (k + 1) * rows]] = m @ b_s[k * K : (k + 1) * K]
    return c_out


def _dma(op, x_values, y_values, x_offset=0, y_offset=0):
    """A DMA-only movement on the host: slot by slot, element k in is element k out."""
    x, y = op.issued_order(op.x), op.issued_order(op.y)
    for slot in range(len(x.slots)):
        y_values[y.indices(slot) + y_offset] = x_values[x.indices(slot) + x_offset]
    return y_values


def test_a_repeat_folds_into_the_gemv_that_reads_it(npu2):
    keys = iron.state((G, L * D), name="keys")
    t = _scores_graph(keys)
    found = candidates(t, npu2)
    (read,) = [c for c in found if isinstance(c, Fold)]
    (write,) = [c for c in found if isinstance(c, Refused)]
    assert read.side is Side.READ and read.neighbours == (1,)
    # The zero-stride half of the heads can only be the iteration slot, so
    # the GEMV walks each group's heads outermost.
    assert read.reorders == (Reorder(G, REP),)
    assert write.side is Side.WRITE and "state" in write.reason

    folded = apply(t, [read], npu2)
    assert [type(s.op).__name__ for s in folded.steps] == ["GEMV"]
    (step,) = folded.steps
    assert step.slots[0].name == "keys"

    rng = np.random.default_rng(0)
    k = rng.standard_normal(G * L * D).astype(bfloat16)
    q = rng.standard_normal(H * D).astype(bfloat16)
    repeat, gemv = (s.op.tuned(npu2) for s in t.steps)
    k_all = _dma(repeat, k, np.zeros(H * L * D, dtype=bfloat16))
    want = _gemv(gemv, k_all, q, np.zeros(H * L, dtype=np.float32))
    got = _gemv(step.op.tuned(npu2), k, q, np.zeros(H * L, dtype=np.float32))
    np.testing.assert_array_equal(got, want)


def test_the_folded_gemv_issues_the_hand_written_repeat(npu2):
    # The descriptors ehunhoff/onnpu-gqa-stride0 wrote by hand into GEMV
    # (repeat=4): its MLIR was diffed identical to the fold's for every
    # Llama decode step. A: every matrix per pass, re-read in the iteration
    # slot; C: the same walk; B: its rows in that walk, legalized.
    t = _scores_graph(iron.state((G, L * D), name="keys"))
    (read,) = [c for c in candidates(t, npu2) if isinstance(c, Fold)]
    op = apply(t, [read], npu2).steps[0].op.tuned(npu2)
    M, K, run_hi, run_lo = L, D, 8, 512
    rows = M // COLS
    a, b, c = (op.issued_order(buf) for buf in (op.A, op.B, op.C))
    for col in range(COLS):
        (acc,) = a[col]
        assert (acc.elements, acc.offset) == (G * L * D, col * rows * K)
        assert acc.sizes == (REP, G, run_hi, run_lo)
        assert acc.strides == (0, M * K, run_lo, 1)
        (acc,) = c[col]
        assert acc.sizes == (REP, G, 1, rows)
        assert acc.strides == (M, REP * M, rows, 1)
        assert b[col] == tuple(
            legalize(H * K, 0, (REP, G, K), (K, REP * K, 1), bfloat16)
        )


def test_a_write_between_the_repeat_and_its_reader_refuses_the_fold(npu2):
    keys = iron.state((G, L * D), name="keys")

    def overwrite(q):
        StridedCopy(
            q,
            keys,
            input_sizes=(H * D,),
            input_strides=(1,),
            input_offset=0,
            output_sizes=(H * D,),
            output_strides=(1,),
            output_offset=0,
        )

    t = _scores_graph(keys, write_between=overwrite)
    read = next(c for c in candidates(t, npu2) if c.side is Side.READ)
    assert isinstance(read, Refused)
    assert "touches keys" in read.reason


def test_a_repeat_cannot_fold_into_the_write_before_it(npu2):
    w = np.zeros((G * D, 2 * D), dtype=bfloat16)

    @iron.graph
    def heads(x):
        k = GEMV(w, x, num_aie_columns=COLS, tile_size_output=D // 2)
        return Repeat(k.reshape(G, D), repeat=REP, transfer_size=D)

    t = heads.trace(x=(2 * D,))
    write = next(c for c in candidates(t, npu2) if c.side is Side.WRITE)
    assert isinstance(write, Refused)
    assert "more than once" in write.reason


def _cache_graph(cache, w):
    """One token's values: a projection, then its row copied into the cache."""

    @iron.graph
    def step(x, *, pos: Scratchpad[np.int32]):
        v = GEMV(w, x, num_aie_columns=COLS, tile_size_output=D // 2)
        StridedCopy(
            v.reshape(G, D),
            cache,
            out_offset=pos * D,
            input_sizes=(G, D),
            input_strides=(D, 1),
            input_offset=0,
            output_sizes=(1, G, D),
            output_strides=(0, L * D, 1),
            output_offset=0,
        )
        return GEMV(w, x, num_aie_columns=COLS, tile_size_output=D // 2)

    return step.trace(x=(2 * D,))


def test_a_cache_copy_folds_into_the_projection_before_it(npu2):
    cache = iron.state((G, L * D), name="cache")
    w = np.zeros((G * D, 2 * D), dtype=bfloat16)
    t = _cache_graph(cache, w)
    found = candidates(t, npu2)
    write = next(c for c in found if isinstance(c, Fold))
    assert write.side is Side.WRITE and write.neighbours == (0,)
    read = next(c for c in found if c.side is Side.READ)
    assert isinstance(read, Refused) and "state" in read.reason

    folded = apply(t, [write], npu2)
    assert [type(s.op).__name__ for s in folded.steps] == ["GEMV", "GEMV"]
    first = folded.steps[0]
    assert first.outputs[0].name == "cache"
    (binding,) = [b for b in folded.bindings if b.op is first.op]
    assert binding.member.name == "C_offset"
    assert binding.expression.evaluate({"pos": 3}) == 3 * D

    rng = np.random.default_rng(1)
    wv = rng.standard_normal(G * D * 2 * D).astype(bfloat16)
    x = rng.standard_normal(2 * D).astype(bfloat16)
    before = rng.standard_normal(G * L * D).astype(np.float32)
    gemv, copy = (s.op.tuned(npu2) for s in t.steps[:2])
    v = _gemv(gemv, wv, x, np.zeros(G * D, dtype=np.float32))
    want = _dma(copy, v, before.copy(), y_offset=3 * D)
    op = first.op.tuned(npu2)
    got = _gemv(op, wv, x, before.copy(), c_offset=3 * D)
    np.testing.assert_array_equal(got, want)
    assert op.issued_order(op.C).offset_by is op.values[0]


def test_fold_all_takes_one_fold_per_movement(npu2):
    keys = iron.state((G, L * D), name="keys")
    t = _scores_graph(keys)
    assert [type(s.op).__name__ for s in FoldAll().fold(t, npu2).steps] == ["GEMV"]
    only_writes = FoldAll(sides=(Side.WRITE,))
    assert len(only_writes.fold(t, npu2).steps) == 2


def test_folded_designs_generate(npu2):
    # The folds' operators as the build sees them: the cache offset a copy
    # carried becomes a scratchpad parameter of the projection.
    keys = iron.state((G, L * D), name="keys")
    cache = iron.state((G, L * D), name="cache")
    w = np.zeros((G * D, 2 * D), dtype=bfloat16)
    for t in (_scores_graph(keys), _cache_graph(cache, w)):
        for step in FoldAll().fold(t, npu2).steps:
            if step.op.refolds:
                text = str(generator_for(step.op.tuned(npu2))())
                assert "aie.runtime_sequence" in text
                if step.op.values:
                    assert "C_offset" in text
