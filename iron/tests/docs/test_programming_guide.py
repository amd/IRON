# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Runs the programming guide's examples, so the guide stays correct.

Each section's example is imported from ``programming_guide/`` by file path
(it lives outside the ``iron`` package, as mlir-aie's own guide's examples
do) and checked two ways: device-free, against its own numpy reference, and
end to end on a device, through its ``main()``. Every comparison goes
through ``aie.utils.verify.compare`` and an operator's own ``tolerance()``,
never a hand-picked number.
"""

import importlib.util
import tempfile
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron.common.graph.fusion import fusions

GUIDE = Path(__file__).resolve().parents[3] / "programming_guide"


def _example(section: str, name: str):
    path = GUIDE / section / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"guide_{section}_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pytestmark = pytest.mark.usefixtures("npu2")


def test_section1_axpy_matches_numpy():
    mod = _example("section-1", "axpy_example")
    op = mod.AXPY(size=256, num_aie_columns=1, tile_size=256, scalar_factor=1.5)
    rng = np.random.default_rng(0)
    a = rng.standard_normal(256).astype(bfloat16)
    b = rng.standard_normal(256).astype(bfloat16)
    reference = op.reference(a, b)
    expected = (1.5 * a.astype(np.float32) + b.astype(np.float32)).astype(bfloat16)
    verdict = compare(reference, expected, op.resolved().tolerance())
    assert verdict, verdict.detail


@pytest.mark.supported_devices("npu2")
def test_section1_axpy_on_device():
    mod = _example("section-1", "axpy_example")
    mod.main(["--size", "256"])


def test_section2_first_graph_matches_numpy():
    mod = _example("section-2", "first_graph")
    graph = mod.ReluThenAxpy(scalar_factor=2.0)
    rng = np.random.default_rng(0)
    x = rng.standard_normal(256).astype(bfloat16)
    y = rng.standard_normal(256).astype(bfloat16)
    reference = graph.reference(x, y)
    expected = (
        np.maximum(x.astype(np.float32), 0) * 2.0 + y.astype(np.float32)
    ).astype(bfloat16)
    recording = graph.record(x=(256,), y=(256,))
    (axpy,) = (s.op for s in recording.steps if type(s.op).__name__ == "AXPY")
    verdict = compare(reference, expected, axpy.resolved().tolerance())
    assert verdict, verdict.detail


@pytest.mark.supported_devices("npu2")
def test_section2_first_graph_on_device():
    mod = _example("section-2", "first_graph")
    mod.main(["--size", "256"])


def test_section3_bounded_graph_matches_numpy():
    mod = _example("section-3", "bounded_graph")
    graph = mod.BoundedRelu()
    recording = graph.record(x=(256,))
    (relu,) = (s.op for s in recording.steps)
    tolerance = relu.resolved().tolerance()
    rng = np.random.default_rng(0)
    x = rng.standard_normal(256).astype(bfloat16)
    for n in (16, 100, 256):
        got = graph.reference(x, n=n)
        expected = np.maximum(x.astype(np.float32), 0)[:n].astype(bfloat16)
        assert got.shape == (n,)
        verdict = compare(got, expected, tolerance)
        assert verdict, verdict.detail


def test_section3_bounded_graph_rejects_an_out_of_range_call():
    mod = _example("section-3", "bounded_graph")
    graph = mod.BoundedRelu()
    x = np.zeros(256, dtype=bfloat16)
    with pytest.raises(IndexError, match="outside"):
        graph.reference(x, n=300)


@pytest.mark.supported_devices("npu2")
def test_section3_bounded_graph_on_device():
    mod = _example("section-3", "bounded_graph")
    mod.main(["--size", "256"])


def test_section4_weights_and_state_matches_numpy():
    mod = _example("section-4", "weights_and_state")
    rng = np.random.default_rng(0)

    weight = rng.standard_normal(64).astype(bfloat16)
    scale = mod.Scale(weight)
    x = rng.standard_normal(64).astype(bfloat16)
    reference = scale.reference(x)
    expected = (x.astype(np.float32) * weight.astype(np.float32)).astype(bfloat16)
    (mul,) = (s.op for s in scale.record(x=(64,)).steps)
    verdict = compare(reference, expected, mul.resolved().tolerance())
    assert verdict, verdict.detail

    accumulate = mod.Accumulate(4, 64)
    recording = accumulate.record(x=(64,))
    (add,) = (s.op for s in recording.steps if type(s.op).__name__ == "ElementwiseAdd")
    tolerance = add.resolved().tolerance()
    expected = np.zeros((4, 64), dtype=bfloat16)
    for pos in (0, 1, 0, 2):
        x = rng.standard_normal(64).astype(bfloat16)
        # expected tracks the same op's own reference(), so it rounds to
        # bf16 the same way the graph's body does, each call - not a
        # separately-invented float32 running sum.
        expected[pos] = add.reference(expected[pos], x)
        got = accumulate.reference(x, pos=pos)
        verdict = compare(got, expected[pos], tolerance)
        assert verdict, verdict.detail


def test_section4_subtraction_exercise_selects_arithmetic(monkeypatch, capsys):
    mod = _example("section-4", "weights_and_state")

    def subtract(self, x, *, pos: mod.Scratchpad[np.int32]):
        old = mod.Copy.step(self.total[pos])
        new = old - x
        mod.Copy.step(new, self.total[pos])
        return new

    monkeypatch.setattr(mod.Accumulate, "body", subtract)
    # Exercise main's recording and tolerance selection without a device.
    reference = iron.Graph.reference
    results = {}

    def remember_reference(self, *args, **kwargs):
        results[self] = reference(self, *args, **kwargs)
        return results[self]

    monkeypatch.setattr(iron.Graph, "reference", remember_reference)
    monkeypatch.setattr(
        iron.Graph,
        "compile",
        lambda self, **shapes: SimpleNamespace(recording=self.record(**shapes)),
    )
    monkeypatch.setattr(iron.Graph, "__call__", lambda self, *args, **kw: results[self])

    mod.main(["--width", "64"])
    assert "PASS!" in capsys.readouterr().out


@pytest.mark.supported_devices("npu2")
def test_section4_weights_and_state_on_device():
    mod = _example("section-4", "weights_and_state")
    mod.main(["--width", "64"])


def _linked_list(seed: int, n: int, steps: int):
    rng = np.random.default_rng(seed)
    successor = rng.permutation(n).astype(np.int32)
    start = int(rng.integers(n))
    trail = [start]
    for _ in range(steps):
        trail.append(int(successor[trail[-1]]))
    return successor, trail


def test_section5_walk_matches_numpy_host_driven():
    mod = _example("section-5", "carried_loop")
    successor, trail = _linked_list(0, mod.N, steps=20)
    walk = mod.Walk(successor, len(trail) - 1)
    node, steps = trail[0], 0
    for expected in trail[1:]:
        nxt = walk.reference(node=node, steps=steps)
        node, steps = int(nxt["node"]), int(nxt["steps"])
        assert node == expected
    np.testing.assert_array_equal(walk.trail.host, trail[1:])


@pytest.mark.supported_devices("npu2")
def test_section5_carried_loop_on_device():
    mod = _example("section-5", "carried_loop")
    mod.main(["--steps", str(3 * mod.N)])


def test_section6_reference_matches_its_operators_chained_by_hand():
    mod = _example("section-6", "reference_and_check")
    rng = np.random.default_rng(0)
    x = rng.standard_normal(256).astype(bfloat16)
    y = rng.standard_normal(256).astype(bfloat16)
    graph = mod.Pipeline()
    got = graph.reference(x, y)
    silu = mod.SiLU(size=256, num_aie_columns=1, tile_size=256)
    mul = mod.ElementwiseMul(size=256, num_aie_columns=1, tile_size=256)
    want = mul.reference(silu.reference(x), y)
    verdict = compare(got, want, Tolerance.exact())
    assert verdict, verdict.detail


@pytest.mark.supported_devices("npu2")
def test_section6_check_mode_on_device():
    mod = _example("section-6", "reference_and_check")
    mod.main(["--size", "256"])


def test_section7_profile_sets_tunables_by_shape():
    mod = _example("section-7", "profiles")
    profile = iron.Profile()
    profile.add(mod.AXPY, size=256, tile_size=128, num_aie_columns=2)
    graph = mod.Scaled()
    graph.profile = profile
    recording = graph.record(x=(256,), y=(256,))
    op = recording.steps[0].op
    assert (op.tile_size, op.num_aie_columns) == (128, 2)


def test_section7_a_calls_own_value_wins_over_the_profile():
    mod = _example("section-7", "profiles")

    class CallWins(iron.Graph):
        def body(self, x, y):
            return mod.AXPY.step(x, y, scalar_factor=1.5, num_aie_columns=1)

    profile = iron.Profile()
    profile.add(mod.AXPY, size=256, tile_size=128, num_aie_columns=2)
    graph = CallWins()
    graph.profile = profile
    op = graph.record(x=(256,), y=(256,)).steps[0].op
    assert (op.tile_size, op.num_aie_columns) == (128, 1)


@pytest.mark.supported_devices("npu2")
def test_section7_profile_on_device():
    mod = _example("section-7", "profiles")
    # The profile's tile_size=1024 only divides the default size (2048).
    mod.main([])


def test_section8_toy_decoder_matches_numpy():
    mod = _example("section-8", "toy_decoder")
    with tempfile.TemporaryDirectory() as directory:
        checkpoint = mod.toy_checkpoint(mod.TOY, directory)
        model = mod.Llama(mod.TOY, checkpoint.tree("random", seed=0))
        rng = np.random.default_rng(1)
        tokens = rng.integers(0, mod.TOY.vocab_size, 8).astype(np.int64)
        ids = np.zeros(mod.TOY.prefill_chunk, dtype=np.int32)
        ids[:8] = tokens
        values = dict(token=int(tokens[-1]), position=7, start=0, rows=8, rope_start=0)
        _, carry = model.reference(ids, **values)
        assert dict(carry) == {"token": 825, "position": 8}


@pytest.mark.supported_devices("npu2")
def test_section8_toy_decoder_on_device():
    mod = _example("section-8", "toy_decoder")
    mod.main([])


def _section9_graph(mod, profile):
    rng = np.random.default_rng(0)
    scale = 1 / np.sqrt(mod.HIDDEN)
    shape = (mod.INTERMEDIATE, mod.HIDDEN)
    w_gate = (rng.standard_normal(shape) * scale).astype(bfloat16)
    w_up = (rng.standard_normal(shape) * scale).astype(bfloat16)
    graph = mod.SwiGLU(w_gate, w_up)
    graph.profile = profile
    return graph, w_gate, w_up


def test_section9_profile_names_the_mlp_fusion():
    mod = _example("section-9", "swiglu_fusion")
    fused, _, _ = _section9_graph(mod, mod.fused_profile())
    recording = fused.record(x=(mod.HIDDEN,))
    (fusion,) = fusions(recording, fused.profile)
    assert fusion.kind is iron.FusionKind.STREAM
    assert fusion.steps == (0, 1, 2, 3)
    wiring = [(e.producer, e.output, e.consumer, e.input) for e in fusion.edges]
    assert wiring == mod.MLP_EDGES

    apart, _, _ = _section9_graph(mod, mod.tuned_profile())
    assert fusions(apart.record(x=(mod.HIDDEN,)), apart.profile) == ()


def test_section9_reference_matches_numpy():
    mod = _example("section-9", "swiglu_fusion")
    graph, w_gate, w_up = _section9_graph(mod, mod.fused_profile())
    x = np.random.default_rng(1).standard_normal(mod.HIDDEN).astype(bfloat16)
    reference = graph.reference(x)
    f32 = np.float32
    gate = (w_gate.astype(f32) @ x.astype(f32)).astype(bfloat16).astype(f32)
    up = (w_up.astype(f32) @ x.astype(f32)).astype(bfloat16).astype(f32)
    silu = (gate / (1 + np.exp(-gate))).astype(bfloat16).astype(f32)
    expected = (silu * up).astype(bfloat16)
    gemv = graph.record(x=(mod.HIDDEN,)).steps[0].op
    verdict = compare(reference, expected, gemv.resolved().tolerance())
    assert verdict, verdict.detail


@pytest.mark.supported_devices("npu2")
def test_section9_swiglu_fusion_on_device():
    mod = _example("section-9", "swiglu_fusion")
    mod.main(["--rounds", "2", "--calls", "5"])
