#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for ``OperatorSequence``.

This is the first test module under ``iron/tests/`` and exercises the
sequencing infrastructure itself (dispatch-mode selection, fused-MLIR
generation, cross-packaging output parity and the check mode's self-check)
rather than any single operator.

The ``OperatorSequence`` packagings and modes covered here are:

* ``full_elf=None``     – a full ELF on NPU2 (Strix), an xclbin chain on
                          NPU1 (Phoenix).
* ``full_elf=True``     – single-ELF dispatch (``aiex.configure`` /
                          ``aiex.run``), NPU2 only.
* ``full_elf=False``    – one xclbin per operator, chained (works on all
                          platforms).
* ``check=True``        – the xclbin chain plus a per-step CPU-reference
                          check.
"""

import logging
import re
from typing import Any

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.kernels.sample import draw_row
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common.harness import verify_buffer
from iron.common.image import Fusion
from iron.common.image.sequence import OperatorSequence
from iron.common.graph.handle import PerCall
from iron.common.image.packaging import Kind, dispatches_full_elf
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.magnitude import Magnitude
from iron.operators.relu import ReLU
from iron.operators.sample import Sample
from iron.operators.tanh import Tanh

RELATIVE = Tolerance.relative(0.04, 1e-6)

PACKAGINGS = {
    "separate": dict(full_elf=False),
    "fused": dict(full_elf=True),
    "compare": dict(check=True),
}


def _centered(rng, n) -> Any:
    """``n`` bf16 values in [-2, 2), drawn as every test here draws them."""
    x: Any = rng.random(n).astype(bfloat16)
    return x * 4 - 2


def _set_input(run, name, data):
    """Write a host tensor into an input buffer and push it to the device.

    The explicit push is redundant, since every callable flushes host writes
    at dispatch (see test_non_input_buffers_sync_without_explicit_flush), and
    is kept for the reader.
    """
    buf = run.get_buffer(name)
    buf.numpy_view()[: data.size] = data.reshape(-1)
    buf.to("npu")


# ---------------------------------------------------------------------------
# Shared builders
# ---------------------------------------------------------------------------

_ADD_RELU_SIZE = 4096
_ADD_RELU_TILE = 1024
_ADD_RELU_COLS = 4


def _build_add_relu_sequence(name, input_args=("a", "b"), **packaging):
    """Out = relu(a + b), as a 2-step OperatorSequence."""
    add = ElementwiseAdd(
        size=_ADD_RELU_SIZE,
        tile_size=_ADD_RELU_TILE,
        num_aie_columns=_ADD_RELU_COLS,
    )
    relu = ReLU(
        size=_ADD_RELU_SIZE,
        num_aie_columns=_ADD_RELU_COLS,
        num_channels=1,
        tile_size=_ADD_RELU_TILE,
    )
    return OperatorSequence(
        name=name,
        runlist=[
            (add, "a", "b", "temp"),
            (relu, "temp", "out"),
        ],
        input_args=list(input_args),
        output_args=["out"],
        **packaging,
    )


# ---------------------------------------------------------------------------
# 1. The derived packaging is the platform default and runs correctly.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("size", [_ADD_RELU_SIZE])
def test_auto_dispatch_selects_platform_default(size):
    """``full_elf=None`` must resolve to a full ELF on Strix and to the
    xclbin chain on Phoenix, and produce the correct result on whichever
    platform the test runs on.
    """
    rng = np.random.default_rng(0)
    a = _centered(rng, size)
    b = _centered(rng, size)

    seq = _build_add_relu_sequence("infra_auto_add_relu")
    seq.compile()

    expected = dispatches_full_elf(aie_utils.get_current_device())
    assert (
        seq.full_elf == expected
    ), f"full_elf resolved to {seq.full_elf}, expected {expected} on this device"

    run = seq.get_callable()
    _set_input(run, "a", a)
    _set_input(run, "b", b)
    run()
    out = run.get_buffer("out").numpy()[:size].copy()

    expected = np.maximum(a + b, 0)
    verdict = verify_buffer(out, "out", expected, RELATIVE)
    assert verdict, f"auto-dispatch sequence: {verdict.detail}"


# ---------------------------------------------------------------------------
# 2. Compilation-only: the fused single-ELF MLIR is well formed.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("sequence", ["add_relu"])
def test_fused_mlir_contains_reconfiguration(sequence, npu2):
    """The single-dispatch (fused) path emits one ``aie.device`` per operator
    plus a top-level device whose runtime sequence reconfigures the array
    between operators via ``aiex.configure`` / ``aiex.run``.

    Only the *generated MLIR* is inspected here (no ELF backend is invoked),
    so it needs no device: it builds for NPU2, which the full fused dispatch
    itself requires.
    """
    seq = _build_add_relu_sequence("infra_fused_mlir", full_elf=True)

    # Generate the fused MLIR directly, bypassing the ELF backend (which is
    # NPU2-only). This mirrors what FusedImage.link() feeds to the compiler.
    seq.prepare()
    fusion = Fusion(seq)
    assert fusion.expands
    text = fusion.text()

    # Reconfiguration + dispatch ops between temporal steps.
    assert "aiex.configure" in text, "missing aiex.configure in fused MLIR"
    assert "aiex.run @sequence" in text, "missing aiex.run in fused MLIR"
    # Typed views of the byte arguments, handed to each operator's runtime sequence.
    assert "memref.view" in text, "missing buffer view in fused MLIR"
    # One inlined device per unique operator plus the top-level driver device,
    # each named for its class and its design, not its position.
    names = re.findall(r"aie\.device\(\w+\) @(\w+)", text)
    assert any(re.fullmatch(r"ElementwiseAdd_[0-9a-f]{8}", n) for n in names) and any(
        re.fullmatch(r"ReLU_[0-9a-f]{8}", n) for n in names
    ), f"operator devices not inlined into fused module: {names}"
    assert (
        text.count("aie.device") >= 3
    ), "expected two operator devices plus a top-level device"


# ---------------------------------------------------------------------------
# 3. Every NPU dispatch mode produces bit-identical output.
# ---------------------------------------------------------------------------


def _run_add_relu(a, b, name, **packaging):
    """Out = relu(a + b), returned as a host bf16 tensor."""
    seq = _build_add_relu_sequence(name, **packaging)
    seq.compile()
    run = seq.get_callable()
    _set_input(run, "a", a)
    _set_input(run, "b", b)
    run()
    return run.get_buffer("out").numpy()[:_ADD_RELU_SIZE].copy()


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("dispatch", PACKAGINGS)
def test_dispatch_modes_bit_identical(dispatch):
    """Add -> relu must yield byte-for-byte identical output across every NPU
    dispatch mode: the compiled kernels are the same, so only the dispatch
    mechanism differs. The ``separate`` mode is the baseline (it runs on every
    platform).
    """
    if dispatch == "fused" and not dispatches_full_elf(aie_utils.get_current_device()):
        pytest.skip("fused dispatch needs a full ELF, which this device lacks")

    rng = np.random.default_rng(0)
    a = _centered(rng, _ADD_RELU_SIZE)
    b = _centered(rng, _ADD_RELU_SIZE)

    baseline = _run_add_relu(a, b, "infra_addrelu_parity_separate", full_elf=False)
    out = _run_add_relu(
        a, b, f"infra_addrelu_parity_{dispatch}", **PACKAGINGS[dispatch]
    )

    assert np.array_equal(
        out, baseline
    ), f"{PACKAGINGS[dispatch]} output is not bit-identical to the separate baseline"


# ---------------------------------------------------------------------------
# 4. Check mode holds each step to its one tolerance(). A step outside it
#    raises; iron/tests/common/checking.py induces that device-free, from a
#    real wrong weight.
#
#    Magnitude's kernel comes within 2e-7 of hypot, about a float32 ulp, on
#    every device: within its contract, but not correctly rounded.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
def test_check_mode_judges_each_step_by_its_tolerance():
    """check=True runs the NPU pipeline and, per step, re-runs the
    operator's ``reference()`` on the same NPU inputs. Under its kernel's
    contract the step runs cleanly.
    """
    rows, width = 8, 640
    rng = np.random.default_rng(0)
    x = (rng.standard_normal((rows, width)) * 10.0).astype(np.float32)

    op = Magnitude(rows=rows, width=width, num_aie_columns=1)
    seq = OperatorSequence(
        name="infra_check_magnitude",
        runlist=[(op, "x", "out")],
        input_args=["x"],
        output_args=["out"],
        check=True,
    )
    seq.compile()
    assert seq.check and seq.full_elf is False

    run: Any = seq.get_callable()
    _set_input(run, "x", x)
    run()  # must not raise


@pytest.mark.supported_devices("npu1", "npu2")
def test_check_mode_judges_every_output_at_the_calls_values(caplog):
    """Sample writes two buffers, its record in place and the token, at a row
    and slot that are per-call values. Check mode runs its reference at
    the values the step was dispatched with and judges both buffers, exactly
    (Sample's tolerance()), so a draw from any row but ``position``'s, or a
    record in any other slot, raises.
    """
    steps, position = 4, 2
    op = Sample(vocab=4096, cores=4, steps=steps)
    op.use_value("row", PerCall("row", Kind.SCRATCHPAD, np.int32).affine())
    op.use_value("at", PerCall("position", Kind.SCRATCHPAD, np.int32).affine())
    seq = OperatorSequence(
        name="infra_check_sample",
        runlist=[(op, "logits", "draws", "tokens", "token")],
        input_args=["logits", "draws", "tokens"],
        output_args=["token"],
        check=True,
    )
    seq.compile()
    run: Any = seq.get_callable()
    rng = np.random.default_rng(3)
    _set_input(run, "logits", rng.normal(0, 3, op.vocab).astype(bfloat16))
    rows = [(0.0, 1), (0.0, 1), (1.0, 64), (0.0, 1)]
    draws = np.stack([draw_row(t, k, int(rng.integers(0, 1 << 53))) for t, k in rows])
    _set_input(run, "draws", draws)
    _set_input(run, "tokens", np.full(steps, -1, dtype=np.int32))
    run.write_values(
        {
            op.value("row").symbol: np.int32(4 * position),
            op.value("at").symbol: np.int32(position),
        }
    )
    with caplog.at_level(logging.INFO, logger="iron.common.image.callable"):
        run()
    judged = re.findall(r"Sample -> (\w+)", caplog.text)
    assert judged == ["tokens", "token"], caplog.text


# ---------------------------------------------------------------------------
# 5. Buffers that are neither inputs nor outputs (weights, KV caches,
#    intermediates) sync like the rest in every NPU dispatch mode. The full-ELF
#    callable places them in its scratch buffer, and NPU access to it is not
#    cache-coherent: an unflushed host write is a race, not an error, so each
#    dispatch below writes different data than the one before.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("dispatch", ["separate", "fused"])
def test_non_input_buffers_sync_without_explicit_flush(dispatch):
    """Host writes through get_buffer() to a non-input buffer reach the NPU at
    the next dispatch, and reads of a non-output buffer after a dispatch see
    what the NPU wrote there, with no explicit ``to()`` from the caller.
    """
    if dispatch == "fused" and not dispatches_full_elf(aie_utils.get_current_device()):
        pytest.skip("fused dispatch needs a full ELF, which this device lacks")

    # b is not an input, so it is held like a weight (in scratch, when fused).
    seq = _build_add_relu_sequence(
        f"infra_add_weight_relu_{dispatch}", input_args=["a"], **PACKAGINGS[dispatch]
    )
    seq.compile()
    run = seq.get_callable()

    rng = np.random.default_rng(0)
    for rep in range(4):
        a = _centered(rng, _ADD_RELU_SIZE)
        b = _centered(rng, _ADD_RELU_SIZE)
        run.get_buffer("a").numpy_view()[:] = a
        run.get_buffer("b").numpy_view()[:] = b
        run()

        temp = run.get_buffer("temp").numpy()[:_ADD_RELU_SIZE]
        out = run.get_buffer("out").numpy()[:_ADD_RELU_SIZE]
        verdict = verify_buffer(temp, "temp", a + b, RELATIVE)
        assert verdict, f"rep {rep}: temp: {verdict.detail}"
        verdict = verify_buffer(out, "out", np.maximum(a + b, 0), RELATIVE)
        assert verdict, f"rep {rep}: out: {verdict.detail}"


# ---------------------------------------------------------------------------
# 6. A full ELF of one design is configured by its first dispatch alone: its
#    load stays unexpanded, so it builds no empty PDIs and no empty
#    configuration.
# ---------------------------------------------------------------------------


def _build_one_design_sequence(op, name, reconfigure=False):
    """Out = op(a), as a 1-step fused OperatorSequence."""
    return OperatorSequence(
        name=name,
        runlist=[(op, "a", "out")],
        input_args=["a"],
        output_args=["out"],
        full_elf=True,
        reconfigure=reconfigure,
    )


def _relu():
    """ReLU at the add/relu sequence's size and tiling."""
    return ReLU(
        size=_ADD_RELU_SIZE,
        num_aie_columns=_ADD_RELU_COLS,
        num_channels=1,
        tile_size=_ADD_RELU_TILE,
    )


def _expanded_pdis(seq):
    """The PDIs only an expanded load builds: its empty ones and the empty
    configuration's.
    """
    return [
        p.name
        for p in seq.artifacts.entry.pdis
        if p.stem.startswith("empty_") or p.stem == Fusion.EMPTY
    ]


@pytest.mark.parametrize("reconfigure", [False, True])
def test_one_design_expands_only_to_reconfigure(reconfigure, npu2):
    """One design's fusion leaves its load unexpanded and adds no empty
    configuration, unless the sequence asks to reconfigure at every call, as a
    probe timing a design's entry does.
    """
    seq = _build_one_design_sequence(
        _relu(), f"infra_fused_relu_reconfigure_{reconfigure}", reconfigure
    )
    seq.prepare()
    fusion = Fusion(seq)
    assert fusion.expands == reconfigure
    devices = re.findall(r"aie\.device\(\w+\) @(\w+)", fusion.text())
    assert (Fusion.EMPTY in devices) == reconfigure, devices


def test_reconfigure_needs_a_full_elf():
    """Only a full ELF has a configure to repeat."""
    with pytest.raises(ValueError, match="reconfigure"):
        OperatorSequence(
            name="infra_separate_reconfigure",
            runlist=[(_relu(), "a", "out")],
            input_args=["a"],
            output_args=["out"],
            full_elf=False,
            reconfigure=True,
        )


@pytest.mark.supported_devices("npu1", "npu2")
def test_one_design_is_configured_once():
    """A fused sequence of one design builds no expanded load, and every
    dispatch after the first still computes on its new inputs.
    """
    if not dispatches_full_elf(aie_utils.get_current_device()):
        pytest.skip("fused dispatch needs a full ELF, which this device lacks")
    seq = _build_one_design_sequence(_relu(), "infra_fused_relu_once").compile()
    assert not _expanded_pdis(seq)

    run = seq.get_callable()
    rng = np.random.default_rng(0)
    for rep in range(4):
        a = _centered(rng, _ADD_RELU_SIZE)
        _set_input(run, "a", a)
        run()
        out = run.get_buffer("out").numpy()[:_ADD_RELU_SIZE]
        verdict = verify_buffer(out, "out", np.maximum(a, 0), RELATIVE)
        assert verdict, f"rep {rep}: out: {verdict.detail}"


@pytest.mark.supported_devices("npu1", "npu2")
def test_one_design_reconfigures_after_another_image():
    """Two one-design images dispatched in turn each configure the array
    again after the other ran, so each still computes its own operator.
    """
    if not dispatches_full_elf(aie_utils.get_current_device()):
        pytest.skip("fused dispatch needs a full ELF, which this device lacks")
    tanh = Tanh(
        size=_ADD_RELU_SIZE,
        num_aie_columns=_ADD_RELU_COLS,
        num_channels=1,
        tile_size=_ADD_RELU_TILE,
    )
    images = {"relu": _relu(), "tanh": tanh}
    runs = {}
    for name, op in images.items():
        seq = _build_one_design_sequence(op, f"infra_fused_{name}_turns").compile()
        assert not _expanded_pdis(seq), name
        runs[name] = seq.get_callable()

    rng = np.random.default_rng(0)
    for rep in range(3):
        for name, run in runs.items():
            op = images[name]
            a = _centered(rng, _ADD_RELU_SIZE)
            _set_input(run, "a", a)
            run()
            out = run.get_buffer("out").numpy()[:_ADD_RELU_SIZE]
            expected = op.reference(a)
            verdict = verify_buffer(out, "out", expected, op.resolved().tolerance())
            assert verdict, f"rep {rep}, {name}: out: {verdict.detail}"
