#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for :class:`OperatorSequence`.

This is the first test module under ``iron/tests/`` and exercises the
sequencing infrastructure itself (dispatch-mode selection, fused-MLIR
generation, cross-mode output parity and the compare-mode self-check) rather
than any single operator.

The ``OperatorSequence`` dispatch modes covered here are:

* ``"auto"``     – picks ``"fused"`` on NPU2 (Strix) and ``"separate"`` on
                   NPU1 (Phoenix).
* ``"fused"``    – single-ELF dispatch (``aiex.configure`` / ``aiex.run``),
                   NPU2 only.
* ``"separate"`` – one xclbin per operator, chained (works on all platforms).
* ``"compare"``  – ``"separate"`` NPU path plus a per-step CPU-reference check.
* ``"reference"``– pure-CPU evaluation via each operator's ``reference()``.
"""

import re
from typing import Any

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.device import NPU2
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common.harness import verify_buffer
from iron.common.image import OperatorSequence, build_fused_mlir
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.relu import ReLU
from iron.operators.tanh import Tanh


def _centered(rng, n) -> Any:
    """``n`` bf16 values in [-2, 2), drawn as every test here draws them."""
    x: Any = rng.random(n).astype(bfloat16)
    return x * 4 - 2


def _set_input(run, name, data):
    """Write a host tensor into an input buffer and push it to the device.

    The explicit push is redundant, since every callable flushes host writes
    at dispatch (see test_non_input_buffers_sync_without_explicit_flush), and
    is a no-op sync for the reference callable.
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


def _build_add_relu_sequence(dispatch, name, input_args=("a", "b")):
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
        dispatch=dispatch,
    )


# ---------------------------------------------------------------------------
# 1. Auto dispatch selects the platform default and runs correctly.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("size", [_ADD_RELU_SIZE])
def test_auto_dispatch_selects_platform_default(size, npu_runtime):
    """``dispatch="auto"`` must resolve to the full-ELF mode on Strix and to
    the separate-xclbin mode on Phoenix, and produce the correct result on
    whichever platform the test runs on.
    """
    rng = np.random.default_rng(0)
    a = _centered(rng, size)
    b = _centered(rng, size)

    seq = _build_add_relu_sequence("auto", "infra_auto_add_relu")
    seq.compile()

    expected_mode = (
        "fused" if isinstance(aie_utils.get_current_device(), NPU2) else "separate"
    )
    assert seq.mode == expected_mode, (
        f"auto dispatch resolved to {seq.mode!r}, expected {expected_mode!r} "
        "on this device"
    )

    run = seq.get_callable()
    _set_input(run, "a", a)
    _set_input(run, "b", b)
    run()
    out = run.get_buffer("out").numpy_view()[:size].copy()

    expected = np.maximum(a + b, 0)
    errors = verify_buffer(out, "out", expected, rel_tol=0.04, abs_tol=1e-6)
    assert not errors, f"auto-dispatch sequence produced {len(errors)} mismatches"


# ---------------------------------------------------------------------------
# 2. Compilation-only: the fused single-ELF MLIR is well formed.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("sequence", ["add_relu"])
def test_fused_mlir_contains_reconfiguration(sequence, npu_runtime):
    """The single-dispatch (fused) path emits one ``aie.device`` per operator
    plus a top-level device whose runtime sequence reconfigures the array
    between operators via ``aiex.configure`` / ``aiex.run``.

    Only the *generated MLIR* is inspected here (no ELF backend is invoked),
    so the check is device-agnostic and runs on all platforms even though the
    full fused dispatch itself requires NPU2.
    """
    seq = _build_add_relu_sequence("fused", "infra_fused_mlir")

    # Generate the fused MLIR directly, bypassing the ELF backend (which is
    # NPU2-only). This mirrors what FusedImage.link() feeds to the compiler.
    seq.subbuffer_layout, seq.buffer_sizes, seq.slice_info = (
        seq.calculate_buffer_layout()
    )
    text = build_fused_mlir(seq)

    # Reconfiguration + dispatch ops between temporal steps.
    assert "aiex.configure" in text, "missing aiex.configure in fused MLIR"
    assert "aiex.run @sequence" in text, "missing aiex.run in fused MLIR"
    # Buffer sub-views handed to each operator's runtime sequence.
    assert "memref.reinterpret_cast" in text, "missing buffer reinterpret in fused MLIR"
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


def _run_add_relu(dispatch, a, b, name):
    """Out = relu(a + b), returned as a host bf16 tensor."""
    seq = _build_add_relu_sequence(dispatch, name)
    seq.compile()
    run = seq.get_callable()
    _set_input(run, "a", a)
    _set_input(run, "b", b)
    run()
    return run.get_buffer("out").numpy_view()[:_ADD_RELU_SIZE].copy()


@pytest.mark.parametrize("dispatch", ["separate", "fused", "compare"])
def test_dispatch_modes_bit_identical(dispatch, npu_runtime):
    """Add -> relu must yield byte-for-byte identical output across every NPU
    dispatch mode: the compiled kernels are the same, so only the dispatch
    mechanism differs. The ``separate`` mode is the baseline (it runs on every
    platform).
    """
    if dispatch == "fused" and not isinstance(aie_utils.get_current_device(), NPU2):
        pytest.skip("fused (single-ELF) dispatch requires NPU2")

    rng = np.random.default_rng(0)
    a = _centered(rng, _ADD_RELU_SIZE)
    b = _centered(rng, _ADD_RELU_SIZE)

    baseline = _run_add_relu("separate", a, b, "infra_addrelu_parity_separate")
    out = _run_add_relu(dispatch, a, b, f"infra_addrelu_parity_{dispatch}")

    assert np.array_equal(
        out, baseline
    ), f"dispatch={dispatch!r} output is not bit-identical to the separate baseline"


# ---------------------------------------------------------------------------
# 3b. dispatch="reference" resolves slice-notation buffers the same way the
#     NPU dispatch paths do: via NpuTensor.subview() on the CPU backend,
#     rather than a hand-rolled numpy view. Not covered by
#     test_dispatch_modes_bit_identical above, since reference() is a CPU
#     re-implementation and only expected to match the NPU output within
#     tolerance, not bit-for-bit (see SequenceCompareCallable's tolerance).
# ---------------------------------------------------------------------------

_SLICE_SIZE = 1024
_SLICE_BYTES = _SLICE_SIZE * 2  # bf16


def _build_packed_output_sequence(dispatch, name):
    """Two independent adds writing into disjoint halves of one explicitly
    sized buffer via slice notation ("packed[start:end]"). Unlike
    _build_add_relu_sequence's "temp" hand-off (a whole-buffer alias), this
    exercises slice_info/explicit_buffer_sizes resolution directly.
    """
    add0 = ElementwiseAdd(size=_SLICE_SIZE, tile_size=_SLICE_SIZE, num_aie_columns=1)
    add1 = ElementwiseAdd(size=_SLICE_SIZE, tile_size=_SLICE_SIZE, num_aie_columns=1)
    return OperatorSequence(
        name=name,
        runlist=[
            (add0, "a0", "b0", f"packed[0:{_SLICE_BYTES}]"),
            (add1, "a1", "b1", f"packed[{_SLICE_BYTES}:{2 * _SLICE_BYTES}]"),
        ],
        input_args=["a0", "b0", "a1", "b1"],
        output_args=["packed"],
        buffer_sizes={"packed": 2 * _SLICE_BYTES},
        dispatch=dispatch,
    )


def test_reference_dispatch_resolves_sliced_buffer(npu_runtime):
    """dispatch="reference" must resolve slice-notation buffers via
    subview() on the CPU backend, matching SequenceXclbinCallable's behaviour,
    and each slice's write must be visible through the parent buffer name.
    """
    rng = np.random.default_rng(0)
    a0: Any = rng.random(_SLICE_SIZE).astype(bfloat16)
    b0: Any = rng.random(_SLICE_SIZE).astype(bfloat16)
    a1: Any = rng.random(_SLICE_SIZE).astype(bfloat16)
    b1: Any = rng.random(_SLICE_SIZE).astype(bfloat16)

    seq = _build_packed_output_sequence("reference", "infra_reference_sliced_packed")
    seq.compile()
    run = seq.get_callable()
    _set_input(run, "a0", a0)
    _set_input(run, "b0", b0)
    _set_input(run, "a1", a1)
    _set_input(run, "b1", b1)
    run()
    packed = run.get_buffer("packed").numpy_view()[: 2 * _SLICE_SIZE].copy()

    expected = np.concatenate([a0 + b0, a1 + b1])
    errors = verify_buffer(packed, "packed", expected, rel_tol=0.04, abs_tol=1e-6)
    assert (
        not errors
    ), f"reference-dispatch sliced buffer produced {len(errors)} mismatches"


# ---------------------------------------------------------------------------
# 4. Compare mode holds each step to its kernel's contract, and flags (and by
#    default raises on) a step that falls outside the tolerance it is judged by.
#
#    Tanh's kernel approximates np.tanh: within its contract, but not
#    bit-exact. So the same NPU output must pass under the default tolerance
#    and fail under an exact one.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("exact", [False, True])
def test_compare_mode_judges_each_step_by_its_tolerance(exact, npu_runtime):
    """dispatch="compare" runs the NPU pipeline and, per step, re-runs the
    operator's ``reference()`` on the same NPU inputs. Under its kernel's
    contract the step runs cleanly (no flagged step); held to exact equality it
    makes compare mode raise on its own (``raise_on_mismatch`` defaults to
    True).
    """
    size = 1024
    rng = np.random.default_rng(0)
    x: Any = rng.random(size).astype(bfloat16)
    x = x * 4

    op = Tanh(size=size, num_aie_columns=1, num_channels=1, tile_size=size)
    seq = OperatorSequence(
        name="infra_compare_tanh",
        runlist=[(op, "x", "out")],
        input_args=["x"],
        output_args=["out"],
        dispatch="compare",
    )
    seq.compile()
    assert seq.mode == "compare"

    run: Any = seq.get_callable()
    if exact:
        run.tolerance = Tolerance.exact()
    _set_input(run, "x", x)

    if exact:
        with pytest.raises(RuntimeError, match="deviates from reference"):
            run()
    else:
        run()  # must not raise
        flagged = any(step.get("mismatch") for step in run.last_step_stats)
        assert not flagged, "compare mode flagged a step within its kernel contract"


# ---------------------------------------------------------------------------
# 5. Buffers that are neither inputs nor outputs (weights, KV caches,
#    intermediates) sync like the rest in every NPU dispatch mode. The full-ELF
#    callable places them in its scratch buffer, and NPU access to it is not
#    cache-coherent: an unflushed host write is a race, not an error, so each
#    dispatch below writes different data than the one before.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("dispatch", ["separate", "fused"])
def test_non_input_buffers_sync_without_explicit_flush(dispatch, npu_runtime):
    """Host writes through get_buffer() to a non-input buffer reach the NPU at
    the next dispatch, and reads of a non-output buffer after a dispatch see
    what the NPU wrote there, with no explicit ``to()`` from the caller.
    """
    if dispatch == "fused" and not isinstance(aie_utils.get_current_device(), NPU2):
        pytest.skip("fused (single-ELF) dispatch requires NPU2")

    # b is not an input, so it is held like a weight (in scratch, when fused).
    seq = _build_add_relu_sequence(
        dispatch, f"infra_add_weight_relu_{dispatch}", input_args=["a"]
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
        errors = verify_buffer(temp, "temp", a + b, rel_tol=0.04, abs_tol=1e-6)
        assert not errors, f"rep {rep}: temp has {len(errors)} mismatches"
        errors = verify_buffer(
            out, "out", np.maximum(a + b, 0), rel_tol=0.04, abs_tol=1e-6
        )
        assert not errors, f"rep {rep}: out has {len(errors)} mismatches"
