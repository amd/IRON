#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for :class:`OperatorSequence`.

This is the first test module under ``iron/tests/`` and exercises the
sequencing infrastructure itself (dispatch-mode selection, fused-MLIR
generation, cross-mode output parity and the pure-reference path) rather than
any single operator.

The ``OperatorSequence`` dispatch modes covered here are:

* ``"auto"``     – picks ``"fused"`` on NPU2 (Strix) and ``"separate"`` on
                   NPU1 (Phoenix).
* ``"fused"``    – single-ELF dispatch (``aiex.configure`` / ``aiex.run``),
                   NPU2 only.
* ``"separate"`` – one xclbin per operator, chained (works on all platforms).
* ``"compare"``  – ``"separate"`` NPU path plus a per-step CPU-reference check.
* ``"reference"``– pure-CPU evaluation via each operator's ``reference()``.
"""

from pathlib import Path

import pytest
import torch

import aie.utils as aie_utils
from aie.iron.device import NPU2

from iron.common.fusion import OperatorSequence
from iron.common.compilation.fusion import fuse_mlir
from iron.common.test_utils import verify_buffer
from iron.operators.elementwise_add.op import ElementwiseAdd
from iron.operators.relu.op import ReLU
from iron.operators.gemv.op import GEMV


def _is_npu2():
    return isinstance(aie_utils.get_current_device(), NPU2)


def _set_input(run, name, data):
    """Write a host tensor into an input buffer and push it to the device.

    Mirrors the caller contract for the fused single-ELF callable: after
    writing a get_buffer() sub-view via torch_view(), the caller is responsible
    for calling .to("npu") so the write reaches the NPU (a no-op sync for the
    separate/reference callables, whose __call__ syncs inputs themselves).
    """
    buf = run.get_buffer(name)
    buf.torch_view()[: data.numel()] = data.reshape(-1)
    buf.to("npu")


# ---------------------------------------------------------------------------
# Shared builders
# ---------------------------------------------------------------------------

_ADD_RELU_SIZE = 4096
_ADD_RELU_TILE = 1024
_ADD_RELU_COLS = 4


def _build_add_relu_sequence(context, dispatch, name):
    """out = relu(a + b), as a 2-step OperatorSequence."""
    add = ElementwiseAdd(
        size=_ADD_RELU_SIZE,
        tile_size=_ADD_RELU_TILE,
        num_aie_columns=_ADD_RELU_COLS,
        context=context,
    )
    relu = ReLU(
        size=_ADD_RELU_SIZE,
        num_aie_columns=_ADD_RELU_COLS,
        num_channels=1,
        tile_size=_ADD_RELU_TILE,
        context=context,
    )
    return OperatorSequence(
        name=name,
        runlist=[
            (add, "a", "b", "temp"),
            (relu, "temp", "out"),
        ],
        input_args=["a", "b"],
        output_args=["out"],
        dispatch=dispatch,
        context=context,
    )


# ---------------------------------------------------------------------------
# 1. Auto dispatch selects the platform default and runs correctly.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("size", [_ADD_RELU_SIZE])
def test_auto_dispatch_selects_platform_default(size, aie_context):
    """``dispatch="auto"`` must resolve to the full-ELF mode on Strix and to
    the separate-xclbin mode on Phoenix, and produce the correct result on
    whichever platform the test runs on."""
    torch.manual_seed(0)
    a = torch.rand(size, dtype=torch.bfloat16) * 4 - 2
    b = torch.rand(size, dtype=torch.bfloat16) * 4 - 2

    seq = _build_add_relu_sequence(aie_context, "auto", "infra_auto_add_relu")
    seq.compile()

    expected_mode = "fused" if _is_npu2() else "separate"
    assert seq._mode == expected_mode, (
        f"auto dispatch resolved to {seq._mode!r}, expected {expected_mode!r} "
        f"on this device"
    )

    run = seq.get_callable()
    _set_input(run, "a", a)
    _set_input(run, "b", b)
    run()
    out = run.get_buffer("out").torch_view()[:size].clone()

    expected = torch.nn.functional.relu(a + b)
    errors = verify_buffer(out, "out", expected, rel_tol=0.04, abs_tol=1e-6)
    assert not errors, f"auto-dispatch sequence produced {len(errors)} mismatches"


# ---------------------------------------------------------------------------
# 2. Compilation-only: the fused single-ELF MLIR is well formed.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("sequence", ["add_relu"])
def test_fused_mlir_contains_reconfiguration(sequence, aie_context, tmp_path):
    """The single-dispatch (fused) path emits one ``aie.device`` per operator
    plus a top-level device whose runtime sequence reconfigures the array
    between operators via ``aiex.configure`` / ``aiex.run``.

    Only the *generated MLIR* is inspected here (no ELF backend is invoked),
    so the check is device-agnostic and runs on all platforms even though the
    full fused dispatch itself requires NPU2.
    """
    seq = _build_add_relu_sequence(aie_context, "fused", "infra_fused_mlir")

    # Generate the fused MLIR directly, bypassing the ELF backend (which is
    # NPU2-only). This mirrors what set_up_artifacts() feeds to the compiler.
    seq.subbuffer_layout, seq.buffer_sizes, seq.slice_info = (
        seq._calculate_buffer_layout()
    )
    mlir_artifact = seq.get_mlir_artifact()
    mlir_artifact.filename = str(tmp_path / mlir_artifact.filename)
    fuse_mlir(mlir_artifact)

    text = Path(mlir_artifact.filename).read_text()

    # Reconfiguration + dispatch ops between temporal steps.
    assert "aiex.configure" in text, "missing aiex.configure in fused MLIR"
    assert "aiex.run @sequence" in text, "missing aiex.run in fused MLIR"
    # Buffer sub-views handed to each operator's runtime sequence.
    assert (
        "memref.reinterpret_cast" in text
    ), "missing buffer reinterpret in fused MLIR"
    # One inlined device per unique operator plus the top-level driver device.
    assert (
        "op0_ElementwiseAdd" in text and "op1_ReLU" in text
    ), "operator devices not inlined into fused module"
    assert (
        text.count("aie.device") >= 3
    ), "expected two operator devices plus a top-level device"


# ---------------------------------------------------------------------------
# 3. Every NPU dispatch mode produces bit-identical output.
# ---------------------------------------------------------------------------

_PARITY_M = 128
_PARITY_K = 128


def _run_gemv_relu(context, dispatch, mat, vec, name):
    """out = relu(mat @ vec), returned as a host bf16 tensor."""
    gemv = GEMV(
        M=_PARITY_M,
        K=_PARITY_K,
        num_aie_columns=1,
        tile_size_input=32,
        tile_size_output=128,
        context=context,
    )
    relu = ReLU(
        size=_PARITY_M,
        num_aie_columns=1,
        num_channels=1,
        tile_size=128,
        context=context,
    )
    seq = OperatorSequence(
        name=name,
        runlist=[
            (gemv, "mat", "vec", "hidden"),
            (relu, "hidden", "out"),
        ],
        input_args=["mat", "vec"],
        output_args=["out"],
        dispatch=dispatch,
        context=context,
    )
    seq.compile()
    run = seq.get_callable()
    _set_input(run, "mat", mat)
    _set_input(run, "vec", vec)
    run()
    return run.get_buffer("out").torch_view()[:_PARITY_M].clone()


@pytest.mark.parametrize("dispatch", ["separate", "fused", "compare"])
def test_dispatch_modes_bit_identical(dispatch, aie_context):
    """GEMV -> ReLU must yield byte-for-byte identical output across every NPU
    dispatch mode: the compiled kernels are the same, so only the dispatch
    mechanism differs. The ``separate`` mode is the baseline (it runs on every
    platform)."""
    if dispatch == "fused" and not _is_npu2():
        pytest.skip("fused (single-ELF) dispatch requires NPU2")

    torch.manual_seed(0)
    mat = torch.rand(_PARITY_M, _PARITY_K, dtype=torch.bfloat16)
    vec = torch.rand(_PARITY_K, dtype=torch.bfloat16)

    baseline = _run_gemv_relu(
        aie_context, "separate", mat, vec, "infra_parity_separate"
    )
    out = _run_gemv_relu(aie_context, dispatch, mat, vec, f"infra_parity_{dispatch}")

    assert torch.equal(out, baseline), (
        f"dispatch={dispatch!r} output is not bit-identical to the separate "
        f"baseline"
    )


# ---------------------------------------------------------------------------
# 4. Reference mode runs each operator's CPU reference; a wrong reference is
#    detectable, a correct one is not.
# ---------------------------------------------------------------------------


class _CorrectAdd(ElementwiseAdd):
    """ElementwiseAdd whose reference matches ground truth (a + b)."""

    def reference(self, a, b):
        return a + b


class _WrongAdd(ElementwiseAdd):
    """ElementwiseAdd whose reference is deliberately wrong (a + b + 1)."""

    def reference(self, a, b):
        return a + b + 1.0


@pytest.mark.parametrize(
    "op_cls,reference_is_correct",
    [(_CorrectAdd, True), (_WrongAdd, False)],
)
def test_reference_mode_detects_wrong_reference(
    op_cls, reference_is_correct, aie_context
):
    """dispatch="reference" evaluates the sequence purely on the CPU using each
    operator's ``reference()``. Comparing that output to independent ground
    truth must pass for a correct reference and fail (trigger) for a wrong
    one."""
    size = 256
    torch.manual_seed(0)
    a = torch.rand(size, dtype=torch.bfloat16)
    b = torch.rand(size, dtype=torch.bfloat16)

    op = op_cls(size=size, tile_size=256, num_aie_columns=1, context=aie_context)
    seq = OperatorSequence(
        name=f"infra_ref_{op_cls.__name__}",
        runlist=[(op, "a", "b", "out")],
        input_args=["a", "b"],
        output_args=["out"],
        dispatch="reference",
        context=aie_context,
    )
    seq.compile()
    assert seq._mode == "reference"

    run = seq.get_callable()
    run.get_buffer("a").torch_view()[:size] = a
    run.get_buffer("b").torch_view()[:size] = b
    run()
    out = run.get_buffer("out").torch_view()[:size].clone()

    ground_truth = a + b
    errors = verify_buffer(out, "out", ground_truth, rel_tol=0.04, abs_tol=1e-6)

    if reference_is_correct:
        assert not errors, "correct reference should match ground truth"
    else:
        assert errors, "wrong reference should be detected by the comparison"
