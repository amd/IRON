# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Image(fusions=...)``.

``PACK`` (independent steps co-resident, issued concurrently) and ``MERGE`` (consecutive steps run back to back, no edge). No device below "On the device".
"""

import re
import statistics
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from aie import ir
from aie.utils.verify import compare

from iron import Profile
from iron.common.design import OperatorDesign
from iron.common.graph.compiled import apply_profile
from iron.common.graph.fusion import candidates
from iron.common.graph.packing import HOST_BUFFERS, merges
from iron.common.graph.record import Recording
from iron.common.image.compose import Composition, fits, places
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import fusable, hang, llama_model, sequences
from iron.tests.support.llama_model import llama_1b
from iron.tune.measure import Timing, time_interleaved

pytestmark = pytest.mark.usefixtures("npu2")

# A fixture is found by its name in the test module.
llama_recordings = llama_model.llama_recordings

LLAMA_NPU2_PROFILE = Profile.load(
    Path(__file__).resolve().parents[2] / "applications/llama/profiles/npu2.json"
)


@pytest.mark.parametrize(
    "kind, shared", [(FusionKind.PACK, False), (FusionKind.MERGE, True)]
)
def test_a_concurrent_fusion_s_scratch_shares_no_bytes_a_merge_s_may(kind, shared):
    """Step 1 last reads ``t`` as step 2 first writes ``u``: apart they may share bytes, at once not."""
    add = ElementwiseAdd(size=2048, num_aie_columns=1, tile_size=2048)
    steps = sequences.steps(
        (add, "x", "x", "t"),
        (add, "t", "x", "y1"),
        (add, "x", "x", "u"),
        (add, "u", "x", "y2"),
    )
    image = Image(
        Recording.of_steps("lifetimes", steps, ["x"], ["y1", "y2"]),
        FullELF(),
        fusions=(Fusion(kind, (1, 2)),),
    ).prepare()
    assert image.layout is not None
    (_, t, n), (_, u, _) = image.layout["t"], image.layout["u"]
    assert (t < u + n and u < t + n) == shared


def _qkv(num_aie_columns=(8, 4, 4)):
    """Llama decode's q/k/v GEMVs (M=2048/512/512, K=2048) over one normed row.

    Packed, each runs its own array, so k and v are narrowed to four columns: the three at the chip's width take 24 shim channels of npu2's 16.
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
    """Return a short decode run: RMSNorm -> GEMV -> ElementwiseAdd (Llama's own residual add), dependent through host memory.

    GEMV keeps the profile's own width (8); both the whole chip wide do not co-fit, so ElementwiseAdd is narrowed.
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


@pytest.mark.parametrize("packaging", [FullELF, PerStep])
def test_an_image_refuses_a_dependent_pack(packaging):
    """GEMV.C -> ElementwiseAdd.b through host memory is a stream candidate, not an independent one; packing them anyway is a hazard every packaging refuses."""
    gemv = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=256)
    add = ElementwiseAdd(size=2048, tile_size=256)
    steps = sequences.steps((gemv, "A", "B", "mid"), (add, "r", "mid", "out"))
    recording = Recording.of_steps("dep_pack", steps, ["A", "B", "r"], ["out"])
    with pytest.raises(ValueError, match="not independent"):
        Image(recording, packaging(), fusions=(Fusion(FusionKind.PACK, (0, 1)),))


def test_pack_refuses_when_columns_cannot_co_reside():
    """q/k/v plus a fourth, full-width GEMV (gate_proj) cannot share one device: too many shim DMA channels between four designs the whole chip wide.

    Fit is decided by placing, not refused up front; q/k/v alone co-fit at ``_qkv``'s default widths.
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
    # each gets its own array (one aie.device, all three): one dropped.
    assert (
        unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 1
    ), "a pack sharing no design with its unfused baseline should drop one aie.device"


def test_a_pack_issues_every_member_before_awaiting_any():
    """GEMV's sequence awaits its own drains; packed, those awaits follow every member's transfers."""
    q, k, v = _qkv()
    image = Image(
        _qkv_recording("pack_order", q, k, v), FullELF(), fusions=(_qkv_pack(),)
    )
    image._prepare()
    lines = Composition(image).text().splitlines()
    starts = [n for n, line in enumerate(lines) if "aiex.dma_start_task" in line]
    awaits = [n for n, line in enumerate(lines) if "aiex.dma_await_task" in line]
    assert starts and awaits and max(starts) < min(awaits)


def _adds():
    """Three ElementwiseAdds of one design, one column each."""
    return [
        ElementwiseAdd(size=2048, num_aie_columns=1, tile_size=1024) for _ in range(3)
    ]


def _adds_recording(name, adds):
    steps = sequences.steps(
        *((add, f"a{i}", f"b{i}", f"y{i}") for i, add in enumerate(adds))
    )
    inputs = [f"{side}{i}" for i in range(3) for side in "ab"]
    return Recording.of_steps(name, steps, inputs, [f"y{i}" for i in range(3)])


def test_packed_steps_of_one_design_each_run_their_own_array():
    """Packed steps issue in one task group; each keeps an array of its own, its barrier set once.

    On one shared array, the second's and third's preambles would re-set the barrier before the first's core read it, so one pass never ran.
    """
    image = Image(
        _adds_recording("pack_same_design", _adds()),
        FullELF(),
        fusions=(Fusion(FusionKind.PACK, (0, 1, 2)),),
    )
    image._prepare()
    text = Composition(image).text()
    assert text.count("aie.core(") == 3
    sequence = text[text.index("aie.runtime_sequence") :]
    locks = re.findall(r"aiex\.set_lock\((%[^,]+),", sequence[: sequence.index("}")])
    assert len(locks) == 3 and len(set(locks)) == 3, locks


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
# candidates(): a recording's admissible packs; a packing's merges on an xclbin.
# ---------------------------------------------------------------------------


def test_pack_candidates_on_small_llama(llama_recordings):
    """Decode's q/k/v GEMVs and the prompt chunk's same projections (under ``ProjectionGEMM``) pack, as 2- and 3-way runs, overlapping ones included.

    Plain data movers (``Copy``, ``RoPE``) that merely run side by side pack too, but not a layer's K and V cache writes, into one paired buffer.
    """
    decode, prompt = llama_recordings
    for recording, projection in ((decode, "GEMV"), (prompt, "ProjectionGEMM")):
        packs = candidates(recording, (FusionKind.PACK,))
        assert len(packs) == 11
        triples = [f for f in packs if len(f.steps) == 3]
        assert all(fusable.kinds(recording, f) == (projection,) * 3 for f in triples)
        # SMALL's two layers, one q/k/v pack each.
        assert len(triples) == 2


def test_a_packing_runs_as_merges_on_an_xclbin(llama_recordings):
    """On an xclbin a packing's steps in a row are one merged dispatch (``merges``), joining every consecutive pair whose designs it groups.

    Not across a host step or into a fusion's step.
    """
    decode, _ = llama_recordings
    dev = aie_utils.ensure_current_device()
    profile = Profile()
    profile.add_packing([(RMSNorm, None), (GEMV, None)])
    recording, fused, packing = apply_profile(decode, profile, dev)
    grouped = [isinstance(s.op, (RMSNorm, GEMV)) for s in recording.steps]
    hosted = {h.at for h in recording.host}
    pairs = {
        (i, i + 1)
        for i in range(len(grouped) - 1)
        if grouped[i] and grouped[i + 1] and i + 1 not in hosted
    }
    runs = merges(recording, fused, packing, dev)
    assert all(f.kind is FusionKind.MERGE for f in runs)
    assert pairs and {(i, i + 1) for f in runs for i in f.steps[:-1]} == pairs
    taken = runs[0].steps[:2]
    rest = merges(recording, (Fusion(FusionKind.PACK, taken),), packing, dev)
    assert {(i, i + 1) for f in rest for i in f.steps[:-1]} == {
        (a, b) for a, b in pairs if a not in taken and b not in taken
    }


def test_each_merge_of_llama_s_npu2_packing_places():
    """Llama's decode packing groups more shim ends than one sequence has channels for; a full ELF's separate sequences share them.

    An xclbin's merge is one sequence, so its runs split where a design would not place, or its steps' host buffers would pass what one kernel takes.
    """
    dev = aie_utils.ensure_current_device()
    model = llama_1b(num_hidden_layers=1)
    decode = model.record(**model.shapes()[0])
    recording, fused, packing = apply_profile(decode, LLAMA_NPU2_PROFILE, dev)
    runs = merges(recording, fused, packing, dev)
    assert any(len(f.steps) > 2 for f in runs)
    for f in runs:
        hosted = [b for j in f.steps for b in recording.steps[j].op.buffers]
        assert sum(not b.on_chip for b in hosted) <= HOST_BUFFERS, f.steps
        firsts: dict[str, int] = {}
        for j in f.steps:
            firsts.setdefault(
                OperatorDesign(recording.steps[j].op.resolved(dev)).name, j
            )
        steps = tuple(firsts.values())
        designs = {
            str(j): OperatorDesign(recording.steps[j].op.resolved(dev)) for j in steps
        }
        assert fits(designs, fusion=Fusion(FusionKind.MERGE, steps)) is None, f.steps


def test_pack_candidates_on_llama_1b_header():
    """The real 1B header: decode's q/k/v and gate/up GEMVs pack, as do the prompt chunk's same projections under ``ProjectionGEMM``."""
    model = llama_1b(num_hidden_layers=1)
    decode_shapes, prompt_shapes = model.shapes()
    decode, prompt = model.record(**decode_shapes), model.record(**prompt_shapes)
    for recording, projection in ((decode, "GEMV"), (prompt, "ProjectionGEMM")):
        packs = candidates(recording, (FusionKind.PACK,))
        assert len(packs) == 6
        assert any(
            len(f.steps) == 3 and fusable.kinds(recording, f) == (projection,) * 3
            for f in packs
        )


# ---------------------------------------------------------------------------
# On the device.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_pack_of_qkv_gemvs_matches_reference_and_unfused(record_property):
    """Llama decode's q/k/v GEMVs (M=2048/512/512, K=2048), packed to run concurrently on disjoint columns.

    Hold to GEMV's own reference and are bit-equal to the same steps unfused; also times both the tuner's way, min and median over interleaved rounds.
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

    # The profile may code A: each buffer holds the form its GEMV reads.
    held = [g.resolved().A.device_form(a) for g, a in ((q, Aq), (k, Ak), (v, Av))]

    def dispatch(run):
        for name, a in zip(("Aq", "Ak", "Av"), held):
            run.get_buffer(BufferRef(name)).numpy_view()[:] = a.reshape(-1)
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
    """RMSNorm -> GEMV -> ElementwiseAdd (Llama's own residual add), merged into one device configuration run back to back with no reconfigure.

    Holds to the references in turn and is bit-equal to the same steps run unfused; also times both.
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
    held = gemv.resolved().A.device_form(A)

    def dispatch(run):
        run.get_buffer(BufferRef("x")).numpy_view()[: x.size] = x.reshape(-1)
        run.get_buffer(BufferRef("w")).numpy_view()[: w.size] = w.reshape(-1)
        run.get_buffer(BufferRef("A")).numpy_view()[:] = held.reshape(-1)
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


def _run_adds() -> list:
    """Return the three adds' outputs packed, then apart."""
    outs = []
    for fusions in ((Fusion(FusionKind.PACK, (0, 1, 2)),), ()):
        adds = _adds()
        image = Image(_adds_recording("pack_adds", adds), FullELF(), fusions=fusions)
        image.compile()
        run = image.get_callable()
        for i, add in enumerate(adds):
            drawn = vectors(add, seed=10 + i).inputs
            for side in "ab":
                run.get_buffer(BufferRef(f"{side}{i}")).numpy_view()[:] = drawn[side]
        run()
        outs.append(
            [run.get_buffer(BufferRef(f"y{i}")).numpy()[:2048].copy() for i in range(3)]
        )
    return outs


# Two compiles and two dispatches.
_ADDS_TIMEOUT_S = 600


@pytest.mark.supported_devices("npu2")
def test_pack_of_three_steps_of_one_design_matches_reference_and_unfused():
    """Three adds of one design packed (on one shared array this lost a pass and hung) hold to numpy and are bit-equal apart.

    In a child process a hang cannot outlive.
    """
    packed, apart = hang.bounded(_ADDS_TIMEOUT_S, _run_adds)
    for i, add in enumerate(_adds()):
        drawn = vectors(add, seed=10 + i).inputs
        ref = np.asarray(add.reference(drawn["a"], drawn["b"])).reshape(-1)
        verdict = compare(packed[i], ref, add.resolved().tolerance())
        assert verdict, f"y{i}: {verdict.detail}"
        assert np.array_equal(packed[i].view(np.uint16), apart[i].view(np.uint16))
