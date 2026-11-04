# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A stream fusion in ``PerStep`` packaging.

Its steps link as one ``FusedDesign``, one xclbin dispatched once with every member's
buffers and per-call values; device-free below "On the device" and "npu1: device-free".
"""

from pathlib import Path

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron import Profile
from iron.applications.llama import Llama
from iron.common.graph.fusion import candidates
from iron.common.graph.record import Recording
from iron.common.image.callable import PerStepCallable
from iron.common.image.link import FusedDesign, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Fusion, FusionKind
from iron.common.testing import vectors
from iron.lm.testing import require
from iron.operators.copy import Copy
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU
from iron.tests.support import fusable, sequences
from iron.tests.support.graphs import Chain
from iron.tests.support.llama_model import llama_1b

LLAMA_1B_WEIGHTS = Path("/scratch/ehunhoff/iron-next/weights-220/llama3.2-1b")


# ---------------------------------------------------------------------------
# On the device, whichever is attached (npu1 or npu2): numpy and bit-equal
# to the same steps run unfused. No device fixture: the current device is
# whatever the runtime finds attached (aie_utils.get_current_device()'s
# probe_runtime=True), as iron/tests/operators/test_catalog.py's do; shapes
# are chosen to fit npu1's 4 columns as well as npu2's 8.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("size,cols", [(2048, 1), (4096, 4)])
def test_silu_mul_fused_matches_reference_and_unfused(size, cols):
    tile = 1024

    def build(name, fusions):
        silu, mul = fusable.silu_mul(size, tile, num_aie_columns=cols)
        img = Image(
            fusable.silu_mul_recording(name, silu, mul), PerStep(), fusions=fusions
        )
        img.compile()
        return img.get_callable(), silu, mul

    fused_run, silu, mul = build(
        f"perstep_fused_{size}_{cols}", (fusable.stream(0, "y", "a"),)
    )
    plain_run, _, _ = build(f"perstep_plain_{size}_{cols}", ())

    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(mul.reference(silu.reference(gate), up))

    def dispatch(run):
        run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
        run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)

    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="SiLU's 1 ulp through the multiply (2), plus both roundings",
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the fused and unfused per-step images differ"


@pytest.mark.supported_devices("npu1", "npu2")
def test_silu_mul_fused_per_call_bound_value():
    """Both operators' ``valid`` is a dispatch-time scalar written to each design's own symbol, both declared as ``dispatch_params``."""
    size, cols, tile = 2048, 1, 1024
    silu, mul = fusable.silu_mul(
        size, tile, num_aie_columns=cols, bound_values={"valid": None}
    )
    img = Image(
        fusable.silu_mul_recording("perstep_bound_valid", silu, mul),
        PerStep(),
        fusions=(fusable.stream(0, "y", "a"),),
    )
    img.compile()
    run = img.get_callable()
    assert isinstance(run, PerStepCallable)
    (kernel,) = [k for _, k, _, _ in run._steps]
    assert any(s.startswith("SiLU") for s in kernel.dispatch_params)
    assert any(s.startswith("ElementwiseMul") for s in kernel.dispatch_params)

    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
    run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
    values = {}
    for op in (silu.resolved(), mul.resolved()):
        for v in op.values:
            values[v.symbol] = np.int32(
                size if v.derive is None else op.derived_at(v.name, valid=size)
            )
    run.write_values(values)
    run()
    out = run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    y_ref = np.asarray(mul.reference(silu.reference(gate), up))
    tol = Tolerance.bf16_ulps(
        3, atol=mul.tolerance().atol, note="shared valid, every element live"
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail


# ---------------------------------------------------------------------------
# On the device, npu2: GEMV fusions.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_gemv_to_elementwiseadd_fused_matches_reference_and_unfused(npu2):
    """Llama decode's GEMV(M=2048, K=2048) -> ElementwiseAdd residual add, fused on one xclbin.

    Holds to the operators' references fused, bit-equal to the same steps unfused.
    """

    def build(name, fusions):
        gemv, add = fusable.gemv_add(2048, 2048)
        img = Image(
            fusable.gemv_add_recording(name, gemv, add), PerStep(), fusions=fusions
        )
        img.compile()
        return img.get_callable(), gemv, add

    fused_run, gemv, add = build("gemv_add_fused", (fusable.stream(0, "C", "b"),))
    plain_run, _, _ = build("gemv_add_plain", ())

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    r = vectors(add, seed=7).inputs["a"]
    y_ref = np.asarray(add.reference(gemv.reference(A, B), r))

    def dispatch(run):
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef("B")).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef("r")).numpy_view()[:] = r.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:2048].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)
    verdict = compare(out, y_ref, gemv.tolerance())
    assert verdict, verdict.detail
    assert np.array_equal(out.view(np.uint16), baseline.view(np.uint16))


@pytest.mark.supported_devices("npu2")
def test_three_step_fusion_matches_reference_and_unfused(npu2):
    """GEMV -> SiLU -> ElementwiseMul, all three fused into one xclbin.

    Holds to the operators' references fused, bit-equal to the same steps unfused.
    """

    def build(name, fusions):
        gemv, silu, mul = fusable.gemv_silu_mul(2048, 1, 2048)
        img = Image(
            fusable.gemv_silu_mul_recording(name, gemv, silu, mul),
            PerStep(),
            fusions=fusions,
        )
        img.compile()
        return img.get_callable(), gemv, silu, mul

    fused_run, gemv, silu, mul = build("three_step_fused", (fusable.three_step(),))
    plain_run, _, _, _ = build("three_step_plain", ())

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(mul.reference(silu.reference(gemv.reference(A, B)), up))

    def dispatch(run):
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef("B")).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:2048].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)
    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="GEMV's accumulation and SiLU's 1 ulp through the multiply, "
        "plus both roundings",
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(out.view(np.uint16), baseline.view(np.uint16))


# A pack of two Copies of one design, each writing its own row into its own
# buffer at one per-call offset: Llama decode's K- and V-cache writes.
ROW, SLOTS = 64, 4


def _cache_write():
    write = Copy(
        input_buffer_size=ROW,
        src=TensorAccessPattern((ROW,), 0, [1, 1, 1, ROW], [0, 0, 0, 1]),
        output_buffer_size=SLOTS * ROW,
        dst=TensorAccessPattern((SLOTS * ROW,), 0, [1, 1, 1, ROW], [0, 0, 0, 1]),
        dtype=np.int32,
    )
    write.use_value("out_offset")
    return write


def _cache_writes_recording(name, k, v):
    steps = sequences.steps((k, "xk", "ck"), (v, "xv", "cv"))
    return Recording.of_steps(name, steps, ["xk", "xv"], ["ck", "cv"])


def test_packed_members_of_one_design_take_their_own_dispatch_parameters(npu2):
    """Two Copies of one design share their per-call symbol, so a fused xclbin gives each member its own, written from it."""
    k, v = _cache_write().resolved(), _cache_write().resolved()
    (symbol,) = {val.symbol for op in (k, v) for val in op.values}
    design = FusedDesign(Fusion(FusionKind.PACK, (0, 1)), [k, v])
    assert design.symbols == {f"{symbol}_0": symbol, f"{symbol}_1": symbol}
    design.module(**{name: 0 for name in design.symbols})


def test_a_pack_of_projections_on_a_shared_xclbin_builds_per_step(npu2):
    """Llama 1B's prompt q/k/v projections (flm.ProjectionGEMM) each run their configuration's xclbin alone; packed.

    The fused design builds each one's own array, as a full ELF does.
    """
    model = llama_1b(num_hidden_layers=1)
    prompt = model.record(**model.shapes()[1])
    pack = next(
        f
        for f in candidates(prompt, (FusionKind.PACK,))
        if len(f.steps) == 3
        and all(type(prompt.steps[i].op).__name__ == "ProjectionGEMM" for i in f.steps)
    )
    ops = [prompt.steps[i].op.resolved() for i in pack.steps]
    assert all(op.xclbin_operator() is not op for op in ops)
    design = FusedDesign(Fusion(FusionKind.PACK, (0, 1, 2)), ops)
    design.module(**{name: 0 for name in design.symbols})


@pytest.mark.supported_devices("npu2")
def test_packed_cache_writes_match_reference_and_unfused(npu2):
    """The pack of two cache writes, one per-step dispatch, lands each row in its own buffer's slot at every offset, bit-equal to the writes apart."""

    def build(fusions):
        k, v = _cache_write(), _cache_write()
        image = Image(
            _cache_writes_recording("perstep_cache_writes", k, v),
            PerStep(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), k.resolved()

    packed_run, k = build((Fusion(FusionKind.PACK, (0, 1)),))
    plain_run, _ = build(())
    (symbol,) = {val.symbol for val in k.values}
    rng = np.random.default_rng(5)
    expected = {
        name: np.full((SLOTS, ROW), -1, dtype=np.int32) for name in ("ck", "cv")
    }
    for run in (packed_run, plain_run):
        for name in ("ck", "cv"):
            run.get_buffer(BufferRef(name)).numpy_view()[:] = -1
            run.get_buffer(BufferRef(name)).to("npu")
    for slot in (2, 0, 3):
        rows = {
            "xk": rng.integers(-(2**31), 2**31 - 1, ROW, dtype=np.int32),
            "xv": rng.integers(-(2**31), 2**31 - 1, ROW, dtype=np.int32),
        }
        expected["ck"][slot], expected["cv"][slot] = rows["xk"], rows["xv"]
        got = []
        for run in (packed_run, plain_run):
            for name, row in rows.items():
                run.get_buffer(BufferRef(name)).numpy_view()[:ROW] = row
            run.write_values({symbol: np.int32(slot * ROW)})
            run()
            got.append(
                {
                    name: run.get_buffer(BufferRef(name)).numpy()[: SLOTS * ROW]
                    for name in ("ck", "cv")
                }
            )
        packed, plain = got
        for name in ("ck", "cv"):
            assert np.array_equal(
                packed[name].reshape(SLOTS, ROW), expected[name]
            ), f"slot {slot}: {name} holds the wrong rows"
            assert np.array_equal(packed[name], plain[name]), f"{name} differs apart"


# ---------------------------------------------------------------------------
# On the device, whichever is attached: a graph, not just a hand-built Image.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
def test_small_graph_compiled_per_step_with_a_named_fusion_is_bit_equal():
    """``Chain`` compiled ``full_elf=False`` with a profile naming its silu -> mul fusion is bit-equal to the same graph compiled without one."""
    size, tile, cols = 2048, 2048, 1
    rng = np.random.default_rng(0)
    a = rng.standard_normal(size).astype(np.float32).astype(bfloat16)
    b = rng.standard_normal(size).astype(np.float32).astype(bfloat16)

    unfused = Chain(size=size, tile=tile, columns=cols).compile(
        full_elf=False, check=False, a=(size,), b=(size,)
    )
    assert unfused.sequence.fusions == ()
    out_unfused = np.asarray(unfused(a, b))

    profile = Profile()
    profile.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=size)), (ElementwiseMul, dict(size=size))],
        [(0, "y", 1, "a")],
    )
    graph = Chain(size=size, tile=tile, columns=cols)
    graph.profile = profile
    fused = graph.compile(full_elf=False, check=False, a=(size,), b=(size,))
    assert len(fused.sequence.fusions) == 1
    out_fused = np.asarray(fused(a, b))

    assert np.array_equal(
        out_fused.view(np.uint16), out_unfused.view(np.uint16)
    ), "a named fusion changed the per-step image's output"


# ---------------------------------------------------------------------------
# npu1: device-free (bound, not attached): the same fusions compile.
# ---------------------------------------------------------------------------


def test_silu_mul_fusion_builds_an_xclbin_per_fused_step_on_npu1(npu1):
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    img = Image(
        fusable.silu_mul_recording("npu1_silu_mul", silu, mul),
        PerStep(),
        fusions=(fusable.stream(0, "y", "a"),),
    )
    img.compile()
    # One Design record per member (as a full ELF's fusion reports), both
    # naming the one xclbin the fused dispatch runs.
    assert len(img.artifacts.designs) == 2
    assert len({d.image for d in img.artifacts.designs}) == 1


def test_an_operator_fused_once_and_called_alone_is_labelled_and_linked_per_step(npu1):
    """An operator fused into one call and run alone in another is labelled and recorded per step, not shared."""
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    steps = sequences.steps(
        (silu, "x", "mid"), (mul, "mid", "up", "out"), (silu, "out", "again")
    )
    img = Image(
        Recording.of_steps("npu1_relabel", steps, ["x", "up"], ["again"]),
        PerStep(),
        fusions=(fusable.stream(0, "y", "a"),),
    )
    img.compile()
    first, second, alone = (s.design for s in img.artifacts.steps)
    assert first == second and first.split("+")[0] == alone and "+" not in alone

    recorded = {d.operators: (d.image, d.insts) for d in img.artifacts.designs}
    fused, alone_link = (
        (Path(link.kernel.xclbin_path), link.design.get_cache_entry().insts)
        for link in (img.packaging.step_links[i] for i in (0, 2))
    )
    assert fused != alone_link
    assert recorded[(silu.name,)] == alone_link and recorded[(mul.name,)] == fused


def test_gemv_fusions_build_an_xclbin_per_fused_step_on_npu1(npu1):
    def build(fused_steps, recording_fn, ops):
        img = Image(recording_fn("npu1_gemv", *ops), PerStep(), fusions=fused_steps)
        img.compile()
        return img

    build(
        (fusable.stream(0, "C", "b"),),
        fusable.gemv_add_recording,
        fusable.gemv_add(2048, 2048),
    )
    build(
        (fusable.three_step(),),
        fusable.gemv_silu_mul_recording,
        fusable.gemv_silu_mul(2048, 1, 2048),
    )


# ---------------------------------------------------------------------------
# npu1: Llama 3.2 1B's own fusion candidates, device-free.
# ---------------------------------------------------------------------------


def test_llama_1b_finds_its_fusion_candidates_on_npu1(npu1, record_property):
    """Finds one SiLU -> Mul per layer in both the decode step and the prompt chunk, and the prompt chunk's also a Copy -> RMSNorm.

    Random weights drawn in the real checkpoint's shapes (only its header is read).
    """
    require(
        LLAMA_1B_WEIGHTS / "config.json",
        LLAMA_1B_WEIGHTS / "model.safetensors",
        staged=False,
    )

    def load():
        model = Llama.from_checkpoint(str(LLAMA_1B_WEIGHTS), random_weights=0)
        decode_shapes, prompt_shapes = model.shapes()
        return model.record(**decode_shapes), model.record(**prompt_shapes)

    decode, prompt = load()

    def pairs(recording):
        return [
            (
                type(recording.steps[f.steps[0]].op.resolved()).__name__,
                f.edges[0].output,
                type(recording.steps[f.steps[1]].op.resolved()).__name__,
                f.edges[0].input,
            )
            for f in candidates(recording)
            if len(f.steps) == 2
        ]

    decode_pairs, prompt_pairs = pairs(decode), pairs(prompt)
    decode_silu_mul = [p for p in decode_pairs if p[0] == "SiLU"]
    prompt_silu_mul = [p for p in prompt_pairs if p[0] == "SiLU"]
    record_property("decode SiLU->Mul candidates", len(decode_silu_mul))
    record_property("prompt SiLU->Mul candidates", len(prompt_silu_mul))
    record_property(
        "decode GEMV->Add candidates", len([p for p in decode_pairs if p[0] == "GEMV"])
    )
    assert all(p == ("SiLU", "y", "ElementwiseMul", "a") for p in decode_silu_mul)
    assert len(decode_silu_mul) == 16  # Llama 3.2 1B's num_hidden_layers
    assert len(prompt_silu_mul) == 16
    assert ("Copy", "RMSNorm") in {
        (
            type(prompt.steps[f.steps[0]].op.resolved()).__name__,
            type(prompt.steps[f.steps[1]].op.resolved()).__name__,
        )
        for f in candidates(prompt)
        if len(f.steps) == 2
    }

    # One decode candidate builds to a per-step xclbin on npu1: compile, no
    # dispatch (no NPU attached here).
    pair = next(f for f in candidates(decode) if len(f.steps) == 2)
    Image(decode, PerStep(), fusions=(pair,)).compile()
