# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GEMV's ``B`` fed on-chip from another operator's output: ``feed_b=True``
(``iron/operators/gemv.py``) makes it a real stream of its own, every lane
holding a ``.cons()`` of its single broadcast fifo, rather than riding a
head tile on ``A``'s, so ``feed()`` applies to it like any other streamed
input. ``feed_b`` defaults to False (the head-tile layout, byte-identical
to every pre-fusion catalog case) and costs a shim channel only where set,
so every call below gives it explicitly.

A fed ``B`` needs a source with exactly as many lanes as GEMV has cores,
since every one of its dot products reads the whole vector, not a share
of it: today that means one lane on both sides, which caps the producer
and GEMV alike at ``num_aie_columns=1``. Broadcasting one producer lane to
GEMV's several needs a source's underlying fifo, not just its bound
handles, which ``Operand.feed()`` does not yet expose (a staged,
memtile-gather kind of broadcast, not this change's scope); these two
tests are the mechanism proven at the smallest config it is feasible, not
Llama decode's own (column-parallel) tunables.
"""

import statistics

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare

from iron.common.graph.record import Recording
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import sequences
from iron.tune.measure import Timing, time_interleaved

pytestmark = pytest.mark.usefixtures("npu2")


def _fuse(producer: int, output: str, consumer_input: str) -> Fusion:
    return Fusion(
        FusionKind.STREAM,
        (producer, producer + 1),
        (Edge(producer, output, producer + 1, consumer_input),),
    )


@pytest.mark.supported_devices("npu2")
def test_rmsnorm_to_gemv_b_matches_reference_and_unfused(record_property):
    """RMSNorm(rows=1, weighted) -> GEMV(M=2048, K=2048).B, fed on-chip,
    holds to the operators' references fused and is bit-equal to the same
    two steps run unfused; also times both, min and median over
    interleaved rounds.
    """
    M = K = 2048
    rms = RMSNorm(rows=1, tile_size=K, weighted=True, num_aie_columns=1)
    gemv = GEMV(M=M, K=K, num_aie_columns=1, num_channels=1, feed_b=True)

    def build(fusions):
        steps = sequences.steps((rms, "x", "weight", "mid"), (gemv, "A", "mid", "out"))
        recording = Recording.of_steps(
            "rmsnorm_gemv_b", steps, ["x", "weight", "A"], ["out"]
        )
        img = Image(recording, FullELF(), fusions=fusions)
        img.compile()
        return img.get_callable()

    fused_run = build((_fuse(0, "y", "B"),))
    plain_run = build(())

    x = vectors(rms).inputs["x"]
    weight = vectors(rms).inputs["weight"]
    A = vectors(gemv).inputs["A"]
    b = rms.reference(x, weight).reshape(-1)
    y_ref = gemv.reference(A, b)

    def dispatch(run):
        run.get_buffer(BufferRef("x")).numpy_view()[:] = x.reshape(-1)
        run.get_buffer(BufferRef("weight")).numpy_view()[:] = weight.reshape(-1)
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:M].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)

    # RMSNorm's own admitted error in B, carried through GEMV's dot products
    # (worst case, |A| times B's error), plus GEMV's own relative tolerance.
    b_err = np.abs(np.asarray(rms.tolerance().bound(x, weight), np.float32)).reshape(-1)
    propagated = np.abs(A.astype(np.float32)) @ b_err
    gemv_tol = gemv.tolerance()
    own = np.maximum(
        gemv_tol.atol or 0.0,
        gemv_tol.rtol * (np.abs(out.astype(np.float32)) + np.abs(y_ref.astype(np.float32))),
    )
    tol = Tolerance.bounded(
        lambda *_: own + propagated,
        note="RMSNorm's own bound through GEMV's dot products, plus GEMV's own",
    )
    verdict = compare(out, y_ref, tol, bound=own + propagated)
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the fused and unfused devices differ"

    fused_stats, unfused_stats = time_interleaved(
        [fused_run, plain_run], Timing(rounds=20), log=lambda _: None
    )
    record_property("Fused min us", min(fused_stats.samples_us))
    record_property("Fused median us", statistics.median(fused_stats.samples_us))
    record_property("Unfused min us", min(unfused_stats.samples_us))
    record_property("Unfused median us", statistics.median(unfused_stats.samples_us))


@pytest.mark.supported_devices("npu2")
def test_elementwisemul_to_gemv_b_matches_reference_and_unfused(record_property):
    """ElementwiseMul -> GEMV(M=2048).B, fed on-chip, holds to the
    operators' references fused and is bit-equal to the same two steps run
    unfused; also times both, min and median over interleaved rounds.

    Llama decode's down projection feeds GEMV.B from a 8192-element,
    8-column ElementwiseMul; a column holds at most 4096 elements
    (``Elementwise.tile_cap``), so even one producer lane already needs two
    columns there, which a fed GEMV.B cannot yet take (see module
    docstring). 4096 is the largest size one column holds, so the largest
    this mechanism reaches today.
    """
    M, K = 2048, 4096
    mul = ElementwiseMul(size=K, num_aie_columns=1, tile_size=K)
    gemv = GEMV(M=M, K=K, num_aie_columns=1, num_channels=1, feed_b=True)

    def build(fusions):
        steps = sequences.steps((mul, "a", "b", "mid"), (gemv, "A", "mid", "out"))
        recording = Recording.of_steps(
            "elementwisemul_gemv_b", steps, ["a", "b", "A"], ["out"]
        )
        img = Image(recording, FullELF(), fusions=fusions)
        img.compile()
        return img.get_callable()

    fused_run = build((_fuse(0, "y", "B"),))
    plain_run = build(())

    a = vectors(mul).inputs["a"]
    b_in = vectors(mul).inputs["b"]
    A = vectors(gemv).inputs["A"]
    b = mul.reference(a, b_in)
    y_ref = gemv.reference(A, b)

    def dispatch(run):
        run.get_buffer(BufferRef("a")).numpy_view()[:] = a.reshape(-1)
        run.get_buffer(BufferRef("b")).numpy_view()[:] = b_in.reshape(-1)
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:M].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)

    # ElementwiseMul's kernel is exact; the sum's error is GEMV's own.
    tol = gemv.tolerance()
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the fused and unfused devices differ"

    fused_stats, unfused_stats = time_interleaved(
        [fused_run, plain_run], Timing(rounds=20), log=lambda _: None
    )
    record_property("Fused min us", min(fused_stats.samples_us))
    record_property("Fused median us", statistics.median(fused_stats.samples_us))
    record_property("Unfused min us", min(unfused_stats.samples_us))
    record_property("Unfused median us", statistics.median(unfused_stats.samples_us))
