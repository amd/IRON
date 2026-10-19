#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for ``Image``.

It exercises the
sequencing infrastructure itself (dispatch-mode selection, composed-MLIR
generation, cross-packaging output parity and the check mode's self-check)
rather than any single operator.

The ``Image`` packagings and modes covered here are:

* ``packaging.plan``     – a full ELF on NPU2 (Strix), an xclbin chain on
                           NPU1 (Phoenix).
* ``FullELF()``          – single-ELF dispatch (``aiex.configure`` /
                           ``aiex.run``), NPU2 only.
* ``PerStep()``          – one xclbin per operator, chained (works on all
                           platforms).
* ``PerStep(check=True)`` – the xclbin chain plus a per-step CPU-reference
                           check.
"""

import logging
import re
from typing import Any

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.kernels.sample import draw_row
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16
from aie.helpers.taplib import PerCall

from iron.common.graph.record import Recording
from iron.common.image.compose import Composition
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef
from iron.common.image.packaging import Kind, plan
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.magnitude import Magnitude
from iron.operators.relu import ReLU
from iron.operators.sample import Sample
from iron.operators.tanh import Tanh
from iron.tests.common import sequences

RELATIVE = Tolerance.relative(0.04, 1e-6)

PACKAGINGS = {
    "separate": PerStep,
    "composed": FullELF,
    "compare": lambda: PerStep(check=True),
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
    buf = run.get_buffer(BufferRef(name))
    buf.numpy_view()[: data.size] = data.reshape(-1)
    buf.to("npu")


# ---------------------------------------------------------------------------
# Shared builders
# ---------------------------------------------------------------------------

_ADD_RELU_SIZE = 4096
_ADD_RELU_TILE = 1024
_ADD_RELU_COLS = 4


def _build_add_relu_sequence(name, packaging=None, inputs=("a", "b")):
    """Out = relu(a + b), as a 2-step Image."""
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
    recording = Recording.of_steps(
        name,
        sequences.steps((add, "a", "b", "temp"), (relu, "temp", "out")),
        inputs,
        ["out"],
    )
    if packaging is None:
        full_elf = plan(aie_utils.get_current_device(), recording).full_elf
        packaging = FullELF() if full_elf else PerStep()
    return Image(recording, packaging)


# ---------------------------------------------------------------------------
# 1. The derived packaging is the platform default and runs correctly.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("size", [_ADD_RELU_SIZE])
def test_auto_dispatch_selects_platform_default(size):
    """``packaging.plan`` must pick a full ELF on Strix and the xclbin
    chain on Phoenix, and produce the correct result on whichever
    platform the test runs on.
    """
    rng = np.random.default_rng(0)
    a = _centered(rng, size)
    b = _centered(rng, size)

    seq = _build_add_relu_sequence("infra_auto_add_relu")
    seq.compile()

    expected = aie_utils.get_current_device().dispatches_full_elf
    assert seq.packaging.full_elf == expected

    run = seq.get_callable()
    _set_input(run, "a", a)
    _set_input(run, "b", b)
    run()
    out = run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    expected = np.maximum(a + b, 0)
    verdict = compare(out, expected, RELATIVE)
    assert verdict, f"auto-dispatch sequence: {verdict.detail}"


# ---------------------------------------------------------------------------
# 2. Compilation-only: the composed single-ELF MLIR is well formed.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("sequence", ["add_relu"])
def test_composed_mlir_contains_reconfiguration(sequence, npu2):
    """The single-dispatch (composed) path emits one ``aie.device`` per operator
    plus a top-level device whose runtime sequence reconfigures the array
    between operators via ``aiex.configure`` / ``aiex.run``.

    Only the *generated MLIR* is inspected here (no ELF backend is invoked),
    so it needs no device: it builds for NPU2, which the full composed dispatch
    itself requires.
    """
    seq = _build_add_relu_sequence("infra_full_elf_mlir", FullELF())

    # Generate the composed MLIR directly, bypassing the ELF backend (which is
    # NPU2-only). This mirrors what FullELF.link() feeds to the compiler.
    seq.prepare()
    composition = Composition(seq)
    assert composition.expands
    text = composition.text()

    # Reconfiguration + dispatch ops between temporal steps.
    assert "aiex.configure" in text, "missing aiex.configure in composed MLIR"
    assert "aiex.run @sequence" in text, "missing aiex.run in composed MLIR"
    # Typed views of the byte arguments, handed to each operator's runtime sequence.
    assert "memref.view" in text, "missing buffer view in composed MLIR"
    # One inlined device per unique operator plus the top-level driver device,
    # each named for its class and its design, not its position.
    names = re.findall(r"aie\.device\(\w+\) @(\w+)", text)
    assert any(re.fullmatch(r"ElementwiseAdd_[0-9a-f]{8}", n) for n in names) and any(
        re.fullmatch(r"ReLU_[0-9a-f]{8}", n) for n in names
    ), f"operator devices not inlined into composed module: {names}"
    assert (
        text.count("aie.device") >= 3
    ), "expected two operator devices plus a top-level device"


def test_commands_are_runtime_sequences_over_the_same_designs(npu2):
    """A full ELF cut into commands runs each as a runtime sequence of
    ``main`` over the uncut image's designs, byte for byte; only the cut
    image's key moves.
    """
    fusions = {}
    for commands in ((), (1,)):
        seq = _build_add_relu_sequence(
            "infra_full_elf_commands", FullELF(commands=commands)
        )
        seq.prepare()
        fusions[commands] = Composition(seq)
    whole, cut = (fusions[c].text() for c in ((), (1,)))
    device = re.compile(r"^  aie\.device\(\w+\) @(\w+) \{$.*?^  \}$", re.M | re.S)
    designs = {m.group(1): m.group(0) for m in device.finditer(whole)}
    assert len(designs) == 2
    assert {m.group(1): m.group(0) for m in device.finditer(cut)} == designs
    # The printer leaves out the default symbols, @main and @sequence.
    main = cut[cut.rindex("aie.device(") :]
    commands = re.split(r"aie\.runtime_sequence", main)[1:]
    names = [re.match(r" @(\w+)", text) for text in commands]
    assert names[0] is None and names[1].group(1) == Composition.sequence_name(1)
    assert whole[whole.rindex("aie.device(") :].count("aie.runtime_sequence") == 1
    assert fusions[()].identity != fusions[(1,)].identity


# ---------------------------------------------------------------------------
# 3. Every NPU dispatch mode produces bit-identical output.
# ---------------------------------------------------------------------------


def _run_add_relu(a, b, name, packaging):
    """Out = relu(a + b), returned as a host bf16 tensor."""
    seq = _build_add_relu_sequence(name, packaging)
    seq.compile()
    run = seq.get_callable()
    _set_input(run, "a", a)
    _set_input(run, "b", b)
    run()
    return run.get_buffer(BufferRef("out")).numpy()[:_ADD_RELU_SIZE].copy()


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("dispatch", PACKAGINGS)
def test_dispatch_modes_bit_identical(dispatch):
    """Add -> relu must yield byte-for-byte identical output across every NPU
    dispatch mode: the compiled kernels are the same, so only the dispatch
    mechanism differs. The ``separate`` mode is the baseline (it runs on every
    platform).
    """
    if (
        dispatch == "composed"
        and not aie_utils.get_current_device().dispatches_full_elf
    ):
        pytest.skip("composed dispatch needs a full ELF, which this device lacks")

    rng = np.random.default_rng(0)
    a = _centered(rng, _ADD_RELU_SIZE)
    b = _centered(rng, _ADD_RELU_SIZE)

    baseline = _run_add_relu(a, b, "infra_addrelu_parity_separate", PerStep())
    out = _run_add_relu(
        a, b, f"infra_addrelu_parity_{dispatch}", PACKAGINGS[dispatch]()
    )

    assert np.array_equal(
        out, baseline
    ), f"{dispatch} output is not bit-identical to the separate baseline"


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
    seq = Image(
        Recording.of_steps(
            "infra_check_magnitude", sequences.steps((op, "x", "out")), ["x"], ["out"]
        ),
        PerStep(check=True),
    )
    seq.compile()

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
    seq = Image(
        Recording.of_steps(
            "infra_check_sample",
            sequences.steps((op, "logits", "draws", "tokens", "token")),
            ["logits", "draws", "tokens"],
            ["token"],
        ),
        PerStep(check=True),
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
@pytest.mark.parametrize("dispatch", ["separate", "composed"])
def test_non_input_buffers_sync_without_explicit_flush(dispatch):
    """Host writes through get_buffer() to a non-input buffer reach the NPU at
    the next dispatch, and reads of a non-output buffer after a dispatch see
    what the NPU wrote there, with no explicit ``to()`` from the caller.
    """
    if (
        dispatch == "composed"
        and not aie_utils.get_current_device().dispatches_full_elf
    ):
        pytest.skip("composed dispatch needs a full ELF, which this device lacks")

    # b is not an input, so it is held like a weight (in scratch, when composed).
    seq = _build_add_relu_sequence(
        f"infra_add_weight_relu_{dispatch}", PACKAGINGS[dispatch](), inputs=["a"]
    )
    seq.compile()
    run = seq.get_callable()

    rng = np.random.default_rng(0)
    for rep in range(4):
        a = _centered(rng, _ADD_RELU_SIZE)
        b = _centered(rng, _ADD_RELU_SIZE)
        run.get_buffer(BufferRef("a")).numpy_view()[:] = a
        run.get_buffer(BufferRef("b")).numpy_view()[:] = b
        run()

        temp = run.get_buffer(BufferRef("temp")).numpy()[:_ADD_RELU_SIZE]
        out = run.get_buffer(BufferRef("out")).numpy()[:_ADD_RELU_SIZE]
        verdict = compare(temp, a + b, RELATIVE)
        assert verdict, f"rep {rep}: temp: {verdict.detail}"
        verdict = compare(out, np.maximum(a + b, 0), RELATIVE)
        assert verdict, f"rep {rep}: out: {verdict.detail}"


# ---------------------------------------------------------------------------
# 6. A full ELF of one design is configured by its first dispatch alone: its
#    load stays unexpanded, so it builds no empty PDIs and no empty
#    configuration.
# ---------------------------------------------------------------------------


def _build_one_design_sequence(op, name, reconfigure=False):
    """Out = op(a), as a 1-step composed Image."""
    return Image(
        Recording.of_steps(name, sequences.steps((op, "a", "out")), ["a"], ["out"]),
        FullELF(reconfigure=reconfigure),
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
    """The PDIs only an expanded load builds: its empty ones."""
    return [p.name for p in seq.artifacts.entry.pdis if p.stem.startswith("empty_")]


@pytest.mark.parametrize("reconfigure", [False, True])
def test_one_design_expands_only_to_reconfigure(reconfigure, npu2):
    """One design's composition leaves its load unexpanded, unless the sequence
    asks to reconfigure at every call, as a probe timing a design's entry does.
    """
    seq = _build_one_design_sequence(
        _relu(), f"infra_full_elf_relu_reconfigure_{reconfigure}", reconfigure
    )
    seq.prepare()
    composition = Composition(seq)
    assert composition.expands == reconfigure


@pytest.mark.supported_devices("npu1", "npu2")
def test_one_design_is_configured_once():
    """A full-ELF sequence of one design builds no expanded load, and every
    dispatch after the first still computes on its new inputs.
    """
    if not aie_utils.get_current_device().dispatches_full_elf:
        pytest.skip("composed dispatch needs a full ELF, which this device lacks")
    seq = _build_one_design_sequence(_relu(), "infra_full_elf_relu_once").compile()
    assert not _expanded_pdis(seq)

    run = seq.get_callable()
    rng = np.random.default_rng(0)
    for rep in range(4):
        a = _centered(rng, _ADD_RELU_SIZE)
        _set_input(run, "a", a)
        run()
        out = run.get_buffer(BufferRef("out")).numpy()[:_ADD_RELU_SIZE]
        verdict = compare(out, np.maximum(a, 0), RELATIVE)
        assert verdict, f"rep {rep}: out: {verdict.detail}"


@pytest.mark.supported_devices("npu1", "npu2")
def test_one_design_reconfigures_after_another_image():
    """Two one-design images dispatched in turn each configure the array
    again after the other ran, so each still computes its own operator.
    """
    if not aie_utils.get_current_device().dispatches_full_elf:
        pytest.skip("composed dispatch needs a full ELF, which this device lacks")
    tanh = Tanh(
        size=_ADD_RELU_SIZE,
        num_aie_columns=_ADD_RELU_COLS,
        num_channels=1,
        tile_size=_ADD_RELU_TILE,
    )
    images = {"relu": _relu(), "tanh": tanh}
    runs = {}
    for name, op in images.items():
        seq = _build_one_design_sequence(op, f"infra_full_elf_{name}_turns").compile()
        assert not _expanded_pdis(seq), name
        runs[name] = seq.get_callable()

    rng = np.random.default_rng(0)
    for rep in range(3):
        for name, run in runs.items():
            op = images[name]
            a = _centered(rng, _ADD_RELU_SIZE)
            _set_input(run, "a", a)
            run()
            out = run.get_buffer(BufferRef("out")).numpy()[:_ADD_RELU_SIZE]
            expected = op.reference(a)
            verdict = compare(out, expected, op.resolved().tolerance())
            assert verdict, f"rep {rep}, {name}: out: {verdict.detail}"
