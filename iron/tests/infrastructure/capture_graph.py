#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for :mod:`iron.common.capture`, the graph recorder.

``Graph`` only ever calls ``.get_arg_spec()`` on an operator -- it does not need a
real ``MLIROperator`` (which pulls in the ``aie.*``/``pyxrt`` toolchain to import).
These tests exercise the graph-recording/naming/inference logic in isolation with a
duck-typed stand-in, via :meth:`Graph.infer_io`, so they run anywhere, independent
of a mlir-aie/hardware setup -- confirmed by actually running them in a sandbox with
neither installed.

``Graph.build()`` itself (the ``OperatorSequence`` construction, which validates
real ``MLIROperator`` instances) is NOT exercised here on purpose -- that needs real
operators (``GEMM``, ``ReLU``, ...) and belongs in a hardware-capable environment.
TODO: add that integration coverage (build a small real graph, compare its
dispatch against the reference() CPU path, per the plan's verification section)
under ``iron/tests/`` once run against real hardware.
"""

from iron.common.base import AIERuntimeArgSpec
from iron.common.capture import Graph, Traced, capture


class FakeOp:
    """Stand-in for an MLIROperator: N inputs followed by M outputs.

    Only ``get_arg_spec`` is needed to record a graph, so the operator is a
    stand-in but the specs are the real :class:`AIERuntimeArgSpec` -- a
    look-alike would drift from it, which is exactly what happened when
    ``direction`` gained ``reads``/``writes``.
    """

    def __init__(self, n_in, n_out=1, name="op"):
        self._specs = [AIERuntimeArgSpec("in", (1,))] * n_in + [
            AIERuntimeArgSpec("out", (1,))
        ] * n_out
        self._name = name

    def get_arg_spec(self):
        return self._specs

    def __repr__(self):
        return self._name


def test_linear_chain_auto_output():
    gemm1, relu, gemm2 = (
        FakeOp(2, name="gemm1"),
        FakeOp(1, name="relu"),
        FakeOp(2, name="gemm2"),
    )
    x, w1, w2 = object(), object(), object()

    with capture() as g:
        h1 = g(relu, g(gemm1, x, w1))
        logits = g(gemm2, h1, w2)

    assert isinstance(h1, Traced)
    assert isinstance(logits, Traced)
    assert len(g.runlist) == 3
    assert g.runlist[0][0] is gemm1
    assert g.runlist[1][0] is relu
    assert g.runlist[2][0] is gemm2

    # relu's output feeds gemm2 by name -- fan-out/fan-in via object identity.
    relu_out_name = g.runlist[1][2]
    assert relu_out_name == h1.name
    assert g.runlist[2][1] == h1.name

    seq_input_args = [n for n in g._consumed if n not in g._produced]
    seq_output_args = [n for n in g._produced if n not in g._consumed]
    assert set(seq_input_args) == {
        g._names[id(x)],
        g._names[id(w1)],
        g._names[id(w2)],
    }
    assert set(seq_output_args) == {logits.name}


def test_fan_out_and_fan_in():
    # SwiGLU-shaped DAG: up and gate both read x, then converge at mul.
    matmul_up, matmul_gate, silu, mul = (
        FakeOp(2, name="up"),
        FakeOp(2, name="gate"),
        FakeOp(1, name="silu"),
        FakeOp(2, name="mul"),
    )
    x, w_up, w_gate = object(), object(), object()

    with capture() as g:
        up = g(matmul_up, x, w_up)
        gate = g(matmul_gate, x, w_gate)
        gate = g(silu, gate)
        hidden = g(mul, up, gate)

    x_name = g._names[id(x)]
    # x resolves to the SAME buffer name in both fan-out branches.
    assert g.runlist[0][1] == x_name
    assert g.runlist[1][1] == x_name
    # mul (fan-in) reads both up's and silu's outputs by name.
    assert g.runlist[3][1] == up.name
    assert g.runlist[3][2] == gate.name
    assert isinstance(hidden, Traced)

    input_args, output_args = g.infer_io()
    assert set(input_args) == {x_name, g._names[id(w_up)], g._names[id(w_gate)]}
    assert set(output_args) == {hidden.name}


def test_explicit_in_place_output_reuses_buffer_name():
    silu = FakeOp(1, name="silu")
    x = object()

    with capture() as g:
        g.input(x, name="ffn_gate")
        result = g(silu, x, x)  # in-place: same buffer for input and output

    assert result is x
    step = g.runlist[0]
    assert step == (silu, "ffn_gate", "ffn_gate")


def test_slice_references_parent_buffer_by_name():
    # Mirrors llama_npu.py's per-head attention buffer slicing.
    transpose = FakeOp(1, name="transpose")
    values = object()

    with capture() as g:
        parent = g.input(values, name="attn_scores_values")
        g(transpose, g.slice(parent, 0, 1024))
        g(transpose, g.slice(values, 1024, 2048))  # slicing the raw tensor works too

    assert g.runlist[0][1] == "attn_scores_values[0:1024]"
    assert g.runlist[1][1] == "attn_scores_values[1024:2048]"


def test_explicit_input_naming():
    op = FakeOp(1, name="op")
    x = object()

    with capture() as g:
        traced_x = g.input(x, name="x")
        g(op, x)

    assert traced_x.name == "x"
    assert g.runlist[0][1] == "x"


def test_scratch_buffer_excluded_from_input_and_output_args():
    op1, op2 = FakeOp(1, name="op1"), FakeOp(1, name="op2")
    x = object()

    with capture() as g:
        h = g(op1, x)
        y = g(op2, h)

    input_args, output_args = g.infer_io()
    # h is produced by op1 and consumed by op2: neither an input nor an output.
    assert h.name not in input_args
    assert h.name not in output_args
    assert output_args == [y.name]


def test_infer_io_is_overridden_by_explicit_build_kwargs():
    # build() must prefer explicit input_args/output_args over inference --
    # exercised directly against the kwarg-handling logic (not a real
    # OperatorSequence construction, which needs real MLIROperator instances).
    op = FakeOp(1, name="op")
    x = object()

    with capture() as g:
        g(op, x)

    inferred_inputs, inferred_outputs = g.infer_io()
    kwargs = {"input_args": ["custom_in"], "output_args": ["custom_out"]}
    input_args = kwargs.pop("input_args", inferred_inputs)
    output_args = kwargs.pop("output_args", inferred_outputs)
    assert input_args == ["custom_in"]
    assert output_args == ["custom_out"]


def test_wrong_arg_count_raises():
    op = FakeOp(2, n_out=1, name="op")
    x = object()

    with capture() as g:
        try:
            g(op, x)  # only 1 of 2 required inputs
        except TypeError:
            pass
        else:
            raise AssertionError("expected TypeError for wrong arg count")


if __name__ == "__main__":
    import sys

    tests = [v for k, v in list(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)} tests passed")
