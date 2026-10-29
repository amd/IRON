# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Image(fusions=...)``: ``PACK`` (independent steps co-resident, issued
concurrently) and ``MERGE`` (consecutive steps sharing a configuration, run
back to back with no edge). No toolchain and no NPU below ``# On the
device``'s line, as ``test_fusion.py``'s own.
"""

import statistics
from pathlib import Path

import numpy as np
import pytest
from aie import ir
from aie.utils.verify import compare

from iron import Profile
from iron.common.graph.fusion import candidates
from iron.common.graph.record import Recording
from iron.common.image.compose import CoResidenceError, Composition, places
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import sequences
from iron.tests.support.llama_model import llama_1b, small
from iron.tune.measure import Timing, time_interleaved

pytestmark = pytest.mark.usefixtures("npu2")

LLAMA_NPU2_PROFILE = Profile.load(
    Path(__file__).resolve().parents[2] / "applications/llama/profiles/npu2.json"
)


def _qkv(num_aie_columns=(8, 8, 8)):
    """Llama decode's q/k/v GEMVs (M=2048/512/512, K=2048) over one normed
    row: independent, each only reading the row and writing its own output.
    The profile's own tunables (each the whole chip wide) co-fit packed.
    """
    qc, kc, vc = num_aie_columns
    q = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048, num_aie_columns=qc)
    k = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048, num_aie_columns=kc)
    v = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048, num_aie_columns=vc)
    return q, k, v


def _qkv_steps(q, k, v):
    """Each GEMV's own weight (``Aq``/``Ak``/``Av``), one shared row (``x``)."""
    return sequences.steps(
        (q, "Aq", "x", "oq"), (k, "Ak", "x", "ok"), (v, "Av", "x", "ov")
    )


def _qkv_recording(name, q, k, v):
    return Recording.of_steps(
        name, _qkv_steps(q, k, v), ["Aq", "Ak", "Av", "x"], ["oq", "ok", "ov"]
    )


def _qkv_pack() -> Fusion:
    return Fusion(FusionKind.PACK, (0, 1, 2))


def _short_decode(num_aie_columns=(1, 8, 2)):
    """A short decode run: RMSNorm -> GEMV -> ElementwiseAdd (Llama's own
    residual add), dependent through host memory. GEMV keeps the profile's
    own width (8); GEMV and ElementwiseAdd both the whole chip wide do not
    co-fit together, so ElementwiseAdd is narrowed.
    """
    rms_cols, gemv_cols, add_cols = num_aie_columns
    rms = RMSNorm(rows=1, tile_size=2048, weighted=True, num_aie_columns=rms_cols)
    gemv = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048, num_aie_columns=gemv_cols)
    add = LLAMA_NPU2_PROFILE.make(ElementwiseAdd, size=2048, num_aie_columns=add_cols)
    return rms, gemv, add


def _short_decode_steps(rms, gemv, add):
    return sequences.steps(
        (rms, "x", "w", "n"), (gemv, "A", "n", "c"), (add, "r", "c", "out")
    )


def _short_decode_recording(name, rms, gemv, add):
    return Recording.of_steps(
        name, _short_decode_steps(rms, gemv, add), ["x", "w", "A", "r"], ["out"]
    )


def _short_decode_merge() -> Fusion:
    return Fusion(FusionKind.MERGE, (0, 1, 2))


# ---------------------------------------------------------------------------
# Validation refusals.
# ---------------------------------------------------------------------------


def test_pack_fusion_takes_no_edges():
    with pytest.raises(ValueError, match="pack fusion takes no edges"):
        Fusion(FusionKind.PACK, (0, 1), (Edge(0, "y", 1, "a"),))


def test_merge_fusion_takes_no_edges():
    with pytest.raises(ValueError, match="merge fusion takes no edges"):
        Fusion(FusionKind.MERGE, (0, 1), (Edge(0, "y", 1, "a"),))


def test_composition_refuses_a_dependent_pack():
    """GEMV.C -> ElementwiseAdd.b through host memory is a stream candidate,
    not an independent one; packing the same two steps anyway is a hazard
    Composition refuses rather than silently racing.
    """
    gemv = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=256)
    add = ElementwiseAdd(size=2048, tile_size=256)
    steps = sequences.steps((gemv, "A", "B", "mid"), (add, "r", "mid", "out"))
    recording = Recording.of_steps("dep_pack", steps, ["A", "B", "r"], ["out"])
    image = Image(recording, FullELF(), fusions=(Fusion(FusionKind.PACK, (0, 1)),))
    image._prepare()
    with pytest.raises(CoResidenceError, match="not independent"):
        Composition(image).text()


def test_pack_refuses_when_columns_cannot_co_reside():
    """q/k/v plus a fourth, independent full-width GEMV (gate_proj) cannot
    share one device: too many shim DMA channels between four designs each
    the whole chip wide. Fit is decided by placing, not refused up front;
    q/k/v alone (``_qkv``'s default) co-fit at the profile's own tunables.
    """
    q, k, v = _qkv()
    gate = LLAMA_NPU2_PROFILE.make(GEMV, M=8192, K=2048, num_aie_columns=8)
    steps = sequences.steps(
        (q, "Aq", "x", "oq"),
        (k, "Ak", "x", "ok"),
        (v, "Av", "x", "ov"),
        (gate, "Ag", "x", "og"),
    )
    recording = Recording.of_steps(
        "pack_too_wide", steps, ["Aq", "Ak", "Av", "Ag", "x"], ["oq", "ok", "ov", "og"]
    )
    image = Image(
        recording, FullELF(), fusions=(Fusion(FusionKind.PACK, (0, 1, 2, 3)),)
    )
    image._prepare()
    text = Composition(image).text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(text))
    assert diagnostic is not None and "ShimNOCTile" in diagnostic


# ---------------------------------------------------------------------------
# Device-free: the composed module.
# ---------------------------------------------------------------------------


def test_pack_of_independent_gemvs_is_one_device_configuration():
    q, k, v = _qkv()
    fused = Image(
        _qkv_recording("pack_struct", q, k, v), FullELF(), fusions=(_qkv_pack(),)
    )
    fused._prepare()
    fused_text = Composition(fused).text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(fused_text))
    assert diagnostic is None, diagnostic

    q2, k2, v2 = _qkv()
    unfused = Image(_qkv_recording("pack_struct_unfused", q2, k2, v2), FullELF())
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    # k and v share one shape (M=512, K=2048), so unfused they share one
    # design and its array (two aie.devices: that design's and q's); packed,
    # each gets its own build (one aie.device, all three): one dropped.
    assert (
        unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 1
    ), "a pack sharing no design with its unfused baseline should drop one aie.device"


def test_merge_of_a_short_decode_run_is_one_device_configuration():
    rms, gemv, add = _short_decode()
    merged = Image(
        _short_decode_recording("merge_struct", rms, gemv, add),
        FullELF(),
        fusions=(_short_decode_merge(),),
    )
    merged._prepare()
    merged_text = Composition(merged).text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(merged_text))
    assert diagnostic is None, diagnostic

    rms2, gemv2, add2 = _short_decode()
    unfused = Image(
        _short_decode_recording("merge_struct_unfused", rms2, gemv2, add2), FullELF()
    )
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    assert (
        unfused_text.count("aie.device(") - merged_text.count("aie.device(") == 2
    ), "a three-step merge should drop two aie.devices"


# ---------------------------------------------------------------------------
# candidates(): a recording's admissible packs and merges.
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def llama_recordings():
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    return model.record(**decode_shapes), model.record(**prompt_shapes)


def _kinds(recording, fusion) -> tuple[str, ...]:
    return tuple(type(recording.steps[i].op.resolved()).__name__ for i in fusion.steps)


def test_pack_candidates_on_small_llama(llama_recordings):
    """Decode's q/k/v GEMVs (one three-way pack a layer: the MLP's gate/up
    is only a pair, down_proj depending on both) and the prompt chunk's same
    projections under ``ProjectionGEMM``, pack as 2- and 3-way runs,
    overlapping ones included; plain data movers (``Copy``, ``RoPE``) that
    merely run side by side pack too.
    """
    decode, prompt = llama_recordings
    for recording, projection in ((decode, "GEMV"), (prompt, "ProjectionGEMM")):
        packs = candidates(recording, (FusionKind.PACK,))
        assert len(packs) == 13
        triples = [f for f in packs if len(f.steps) == 3]
        assert all(_kinds(recording, f) == (projection,) * 3 for f in triples)
        # SMALL's two layers, one q/k/v pack each.
        assert len(triples) == 2


def test_merge_candidates_on_small_llama(llama_recordings):
    """Consecutive steps whose designs co-fit, dependent or not: RoPE's own
    pair merges. Exact counts, and which longer runs co-fit, are not
    asserted: ``fits()`` resolves every design's own tunables, which the
    GEMV and elementwise column-width logic this ports alongside is still
    settling.
    """
    decode, prompt = llama_recordings
    decode_merges = candidates(decode, (FusionKind.MERGE,))
    prompt_merges = candidates(prompt, (FusionKind.MERGE,))
    assert decode_merges and prompt_merges
    assert any(_kinds(decode, f) == ("RoPE", "RoPE") for f in decode_merges)


def test_pack_candidates_on_llama_1b_header():
    """The real 1B header (unread weights, the shapes ``candidates`` builds
    designs at): decode's q/k/v and gate/up GEMVs pack, as do the prompt
    chunk's same projections under ``ProjectionGEMM``.
    """
    model = llama_1b(num_hidden_layers=1)
    decode_shapes, prompt_shapes = model.shapes()
    decode, prompt = model.record(**decode_shapes), model.record(**prompt_shapes)
    for recording, projection in ((decode, "GEMV"), (prompt, "ProjectionGEMM")):
        packs = candidates(recording, (FusionKind.PACK,))
        assert len(packs) == 7
        assert any(
            len(f.steps) == 3 and _kinds(recording, f) == (projection,) * 3
            for f in packs
        )


def test_merge_candidates_on_llama_1b_header():
    """The real 1B header's decode step and prompt chunk: RoPE's own pair
    merges. Exact counts, and which other runs co-fit, are not asserted
    (``test_merge_candidates_on_small_llama``'s reasoning).
    """
    model = llama_1b(num_hidden_layers=1)
    decode_shapes, prompt_shapes = model.shapes()
    decode, prompt = model.record(**decode_shapes), model.record(**prompt_shapes)
    decode_merges = candidates(decode, (FusionKind.MERGE,))
    prompt_merges = candidates(prompt, (FusionKind.MERGE,))
    assert decode_merges and prompt_merges
    assert any(_kinds(decode, f) == ("RoPE", "RoPE") for f in decode_merges)


# ---------------------------------------------------------------------------
# On the device.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_pack_of_qkv_gemvs_matches_reference_and_unfused(record_property):
    """Llama decode's q/k/v GEMVs (M=2048/512/512, K=2048), packed to run
    concurrently on disjoint columns, hold to GEMV's own reference and are
    bit-equal to the same three steps run unfused; also times both the
    tuner's way (``time_interleaved``: each image's calls run in turn
    within a round, so a round pays one hardware-context load per image
    rather than one per call), min and median over interleaved rounds.
    """

    def build(fusions):
        q, k, v = _qkv()
        img = Image(_qkv_recording("pack_device", q, k, v), FullELF(), fusions=fusions)
        img.compile()
        return img.get_callable(), q, k, v

    packed_run, q, k, v = build((_qkv_pack(),))
    plain_run, _, _, _ = build(())

    Aq = vectors(q).inputs["A"]
    Ak = vectors(k, seed=7).inputs["A"]
    Av = vectors(v, seed=11).inputs["A"]
    x = vectors(q, seed=3).inputs["B"]
    oq_ref = np.asarray(q.reference(Aq, x))
    ok_ref = np.asarray(k.reference(Ak, x))
    ov_ref = np.asarray(v.reference(Av, x))

    def dispatch(run):
        run.get_buffer(BufferRef("Aq")).numpy_view()[:] = Aq.reshape(-1)
        run.get_buffer(BufferRef("Ak")).numpy_view()[:] = Ak.reshape(-1)
        run.get_buffer(BufferRef("Av")).numpy_view()[:] = Av.reshape(-1)
        run.get_buffer(BufferRef("x")).numpy_view()[: x.size] = x.reshape(-1)
        run()
        return (
            run.get_buffer(BufferRef("oq")).numpy()[:2048].copy(),
            run.get_buffer(BufferRef("ok")).numpy()[:512].copy(),
            run.get_buffer(BufferRef("ov")).numpy()[:512].copy(),
        )

    oq, ok, ov = dispatch(packed_run)
    boq, bok, bov = dispatch(plain_run)

    tol = q.tolerance()
    for out, ref, baseline, label in (
        (oq, oq_ref, boq, "q"),
        (ok, ok_ref, bok, "k"),
        (ov, ov_ref, bov, "v"),
    ):
        verdict = compare(out, ref, tol)
        assert verdict, f"{label}: {verdict.detail}"
        assert np.array_equal(
            out.view(np.uint16), baseline.view(np.uint16)
        ), f"{label}: the packed and unpacked devices differ"

    packed_stats, unfused_stats = time_interleaved(
        [packed_run, plain_run], Timing(rounds=20), log=lambda _: None
    )
    record_property("Packed min us", min(packed_stats.samples_us))
    record_property("Packed median us", statistics.median(packed_stats.samples_us))
    record_property("Unfused min us", min(unfused_stats.samples_us))
    record_property("Unfused median us", statistics.median(unfused_stats.samples_us))


@pytest.mark.supported_devices("npu2")
def test_merge_of_a_short_decode_run_matches_reference_and_unfused(record_property):
    """RMSNorm -> GEMV -> ElementwiseAdd (Llama's own residual add), merged
    into one device configuration run back to back with no reconfigure
    between them, holds to the operators' own references in turn and is
    bit-equal to the same three steps run unfused; also times both.
    """

    def build(fusions):
        rms, gemv, add = _short_decode()
        img = Image(
            _short_decode_recording("merge_device", rms, gemv, add),
            FullELF(),
            fusions=fusions,
        )
        img.compile()
        return img.get_callable(), rms, gemv, add

    merged_run, rms, gemv, add = build((_short_decode_merge(),))
    plain_run, _, _, _ = build(())

    x = vectors(rms).inputs["x"]
    w = vectors(rms, seed=5).inputs["weight"]
    A = vectors(gemv, seed=7).inputs["A"]
    r = vectors(add, seed=11).inputs["a"]
    n_ref = np.asarray(rms.reference(x, w))
    c_ref = np.asarray(gemv.reference(A, n_ref))
    y_ref = np.asarray(add.reference(c_ref, r))

    def dispatch(run):
        run.get_buffer(BufferRef("x")).numpy_view()[: x.size] = x.reshape(-1)
        run.get_buffer(BufferRef("w")).numpy_view()[: w.size] = w.reshape(-1)
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef("r")).numpy_view()[:] = r.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:2048].copy()

    out = dispatch(merged_run)
    baseline = dispatch(plain_run)

    verdict = compare(out, y_ref, gemv.tolerance())
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the merged and unfused devices differ"

    merged_stats, unfused_stats = time_interleaved(
        [merged_run, plain_run], Timing(rounds=20), log=lambda _: None
    )
    record_property("Merged min us", min(merged_stats.samples_us))
    record_property("Merged median us", statistics.median(merged_stats.samples_us))
    record_property("Unfused min us", min(unfused_stats.samples_us))
    record_property("Unfused median us", statistics.median(unfused_stats.samples_us))
