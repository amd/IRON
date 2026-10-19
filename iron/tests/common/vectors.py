# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``vectors()`` and an operator's ``call_reference``/``judge``: the device
test's halves, host-side."""

import numpy as np
import pytest
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common.testing import vectors
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.relu import ReLU
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.sample import Sample

pytestmark = pytest.mark.usefixtures("npu2")


def test_vectors_draws_each_input_and_runs_the_reference_on_the_draw():
    op = ElementwiseAdd(size=64, num_aie_columns=1, tile_size=64)
    v = vectors(op, seed=1)
    assert set(v.inputs) == {"a", "b"} and set(v.outputs) == {"y"}
    assert v["a"].shape == (64,) and v["a"].dtype == bfloat16
    np.testing.assert_array_equal(v["y"], v["a"] + v["b"])
    assert np.array_equal(vectors(op, seed=1)["a"], v["a"])  # seeded
    assert not np.array_equal(vectors(op, seed=2)["a"], v["a"])


def test_vectors_takes_a_given_array_a_shape_or_a_centred_draw():
    op = ReLU(size=64, num_aie_columns=1, tile_size=64)
    given = np.arange(64, dtype=bfloat16)
    assert vectors(op, given={op.x: given})["x"] is given
    # The declared 64, as given; the class's declared operand keys it too.
    assert vectors(op, given={ReLU.x: (2, 32)})["x"].shape == (2, 32)
    plain, centred = vectors(op)["x"], vectors(op, centered=(op.x,))["x"]
    assert plain.dtype == centred.dtype == bfloat16
    assert 0 <= plain.min() and plain.max() < 4.0 and not (plain == plain.round()).all()
    assert (centred < 0).any() and (centred > 0).any()  # both signs, as ReLU asks
    other = ElementwiseAdd(size=64, num_aie_columns=1, tile_size=64)
    with pytest.raises(ValueError, match=r"has no input \['a'\]"):
        vectors(op, given={other.a: given})


def test_tolerance_is_the_operators_own_else_its_kernels_contract():
    assert RoPE(rows=8, cols=64).resolved().tolerance().rtol == 0.05
    relu = ReLU(size=64, num_aie_columns=1, tile_size=64).resolved()
    contract = relu.layout().kernel().contract_for(resolve_target_arch(relu.dev))
    assert relu.tolerance() == contract.tolerance is not None


def _sample():
    op = Sample(vocab=4096, cores=4, steps=3)
    return op, vectors(op, **Sample.test.draw(op))


def test_call_reference_pairs_buffers_by_name_not_by_order():
    op, v = _sample()
    reordered = dict(reversed(v.inputs.items()))
    got = op._call_reference(reordered, values={"row": 4, "at": 1})
    assert list(got) == ["tokens", "token"]
    np.testing.assert_array_equal(got["tokens"][1], got["token"][0])
    assert op.judge(reordered, dict(reversed(got.items())), Tolerance.exact(), got)
    with pytest.raises(ValueError, match="takes the inputs"):
        misspelled = {("logit" if k == "logits" else k): t for k, t in v.inputs.items()}
        op._call_reference(misspelled)


def test_judge_names_each_output_and_refuses_a_missing_one():
    op, v = _sample()
    verdicts = op.judge(v.inputs, v.outputs, Tolerance.exact())
    assert list(verdicts) == ["tokens", "token"] and all(verdicts.values())
    wrong = {**v.outputs, "token": v.outputs["token"] + 1}
    assert not op.judge(v.inputs, wrong, Tolerance.exact())["token"]
    with pytest.raises(ValueError):
        op.judge(v.inputs, {"tokens": v.outputs["tokens"]}, Tolerance.exact())


def test_call_reference_gives_an_output_only_to_a_reference_that_names_it():
    op = RMSNorm(rows=2, tile_size=64)
    x = vectors(op, seed=3)["x"]
    given = {"y": np.zeros_like(x)}
    got = op._call_reference({"x": x}, given)
    np.testing.assert_array_equal(got["y"], op.reference(x))
    with pytest.raises(ValueError, match=r"has no output \['out'\]"):
        op._call_reference({"x": x}, {"out": given["y"]})


class InPlaceReLU(ReLU):
    def reference(self, x, y):
        y[:] = np.maximum(x, 0)


def test_call_reference_refuses_a_reference_that_returns_nothing():
    op = InPlaceReLU(size=64, num_aie_columns=1, tile_size=64)
    x = np.arange(-32, 32, dtype=bfloat16)
    with pytest.raises(ValueError, match=r"returned \(None,\) for \['y'\]"):
        op._call_reference({"x": x}, {"y": np.zeros_like(x)})
