# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Image(chains=...)``: a producer step's output streamed on-chip into the
next step's input, the two running as one device configuration with no host
transfer between them. No toolchain and no NPU below ``test_chain_device.py``'s
line.
"""

import numpy as np
import pytest
from aie import ir
from aie.utils.verify import Tolerance, compare

from iron.common.graph.record import Recording
from iron.common.image.compose import Composition, places
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Chain
from iron.common.testing import vectors
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU
from iron.tests.support import sequences

pytestmark = pytest.mark.usefixtures("npu2")


def _steps(silu, mul, mid):
    """SiLU's ``y`` and ElementwiseMul's ``a`` name ``mid``, the one chained."""
    return sequences.steps((silu, "x", mid), (mul, mid, "up", "out"))


def _silu_mul(size, cols, tile, **extra):
    silu = SiLU(size=size, num_aie_columns=cols, tile_size=tile, **extra)
    mul = ElementwiseMul(size=size, num_aie_columns=cols, tile_size=tile, **extra)
    return silu, mul


def _recording(name, silu, mul):
    return Recording.of_steps(name, _steps(silu, mul, "mid"), ["x", "up"], ["out"])


# ---------------------------------------------------------------------------
# Device-free: the composed module.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("size,cols", [(2048, 1), (8192, 8)])
def test_chained_pair_is_one_device_configuration(size, cols):
    """A chained pair places as one device, which is one fewer ``aie.device``
    than the same two steps unchained; its identity differs too.
    """
    tile = 1024
    silu, mul = _silu_mul(size, cols, tile)
    chained = Image(
        _recording(f"chain_struct_{size}_{cols}", silu, mul),
        FullELF(),
        chains=(Chain(0, "y", "a"),),
    )
    chained._prepare()
    chained_composition = Composition(chained)
    chained_text = chained_composition.text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(chained_text))
    assert diagnostic is None, diagnostic

    silu2, mul2 = _silu_mul(size, cols, tile)
    unchained = Image(
        _recording(f"unchain_struct_{size}_{cols}", silu2, mul2), FullELF()
    )
    unchained._prepare()
    unchained_text = Composition(unchained).text()

    assert (
        unchained_text.count("aie.device(") - chained_text.count("aie.device(") == 1
    ), "a chained pair should drop exactly one aie.device"


def test_chained_identity_differs_from_unchained():
    silu, mul = _silu_mul(2048, 1, 1024)
    chained = Image(
        _recording("chain_identity_chained", silu, mul),
        FullELF(),
        chains=(Chain(0, "y", "a"),),
    )
    chained._prepare()
    silu2, mul2 = _silu_mul(2048, 1, 1024)
    unchained = Image(_recording("chain_identity_unchained", silu2, mul2), FullELF())
    unchained._prepare()
    assert Composition(chained).identity != Composition(unchained).identity


# ---------------------------------------------------------------------------
# Refusals.
# ---------------------------------------------------------------------------


def test_bad_producer_index_refused():
    silu, mul = _silu_mul(2048, 1, 1024)
    recording = _recording("chain_bad_index", silu, mul)
    with pytest.raises(ValueError, match="names no step"):
        Image(recording, FullELF(), chains=(Chain(1, "y", "a"),))


def test_wrong_buffer_names_refused():
    silu, mul = _silu_mul(2048, 1, 1024)
    with pytest.raises(ValueError, match="no drained buffer"):
        Image(
            _recording("chain_bad_output", silu, mul),
            FullELF(),
            chains=(Chain(0, "nope", "a"),),
        )
    silu, mul = _silu_mul(2048, 1, 1024)
    with pytest.raises(ValueError, match="no filled buffer"):
        Image(
            _recording("chain_bad_input", silu, mul),
            FullELF(),
            chains=(Chain(0, "y", "nope"),),
        )
    silu, mul = _silu_mul(2048, 1, 1024)
    split = Recording.of_steps(
        "chain_split_roots",
        sequences.steps((silu, "x", "mid_a"), (mul, "mid_b", "up", "out")),
        ["x", "up"],
        ["out"],
    )
    with pytest.raises(ValueError, match="do not name one whole buffer"):
        Image(split, FullELF(), chains=(Chain(0, "y", "a"),))


def test_step_in_two_chains_refused():
    silu, mul = _silu_mul(2048, 1, 1024)
    recording = _recording("chain_double_claim", silu, mul)
    with pytest.raises(ValueError, match="is in two chains"):
        Image(recording, FullELF(), chains=(Chain(0, "y", "a"), Chain(0, "y", "a")))


def test_perstep_chains_refused():
    silu, mul = _silu_mul(2048, 1, 1024)
    recording = _recording("chain_perstep", silu, mul)
    with pytest.raises(ValueError, match="FullELF"):
        Image(recording, PerStep(), chains=(Chain(0, "y", "a"),))


# ---------------------------------------------------------------------------
# On the device.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_chained_matches_reference_and_unchained():
    """silu(gate) * up fused on-chip holds to the operators' references chained,
    and is bit-equal to the same two steps run unfused.
    """
    size, cols, tile = 2048, 1, 1024

    def build(chains):
        silu, mul = _silu_mul(size, cols, tile)
        img = Image(_recording("chain_device", silu, mul), FullELF(), chains=chains)
        img.compile()
        return img.get_callable(), silu, mul

    chained_run, silu, mul = build((Chain(0, "y", "a"),))
    plain_run, _, _ = build(())

    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(mul.reference(silu.reference(gate), up))

    def dispatch(run):
        run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
        run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    out = dispatch(chained_run)
    baseline = dispatch(plain_run)

    # A 1-ulp intermediate becomes at most 2 ulps of the product, plus half an
    # ulp for each of the device's and the reference's rounding.
    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="SiLU's 1 ulp through the multiply (2), plus both roundings",
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the chained and unchained devices differ"


@pytest.mark.supported_devices("npu2")
def test_chained_per_call_shared_value():
    """Both operators' ``valid`` bound to one graph value share one scratchpad
    word (``FullELF.shared_words``), which the device still reads correctly.
    """
    size, cols, tile = 2048, 1, 1024
    silu, mul = _silu_mul(size, cols, tile, bound_values={"valid": None})
    # "valid" bounds each core's trip count only through "count", derived from
    # it; that is the word a core reads, and the one the two operators share.
    shared = {
        silu.value("count").symbol: "chain_count",
        mul.value("count").symbol: "chain_count",
    }
    img = Image(
        _recording("chain_device_per_call", silu, mul),
        FullELF(shared_words=shared),
        chains=(Chain(0, "y", "a"),),
    )
    img.compile()
    assert (
        sum(p.name == "chain_count" for p in img.artifacts.parameter_table) == 1
    ), "both operators' count should share one scratchpad word"

    # Every per-call word both operators declare, not just the shared one: a
    # bounded call still writes each buffer's own tile count.
    declared = img.artifacts.parameters
    words = {
        shared.get(v.symbol, v.symbol): np.int32(
            size if v.derive is None else op.derived_at(v.name, valid=size)
        )
        for op in (silu, mul)
        for v in op.values
    }

    run = img.get_callable()
    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
    run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
    run.write_values({k: w for k, w in words.items() if k in declared})
    run()
    out = run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    y_ref = np.asarray(mul.reference(silu.reference(gate), up))
    tol = Tolerance.bf16_ulps(
        3, atol=mul.tolerance().atol, note="shared valid, every element live"
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
