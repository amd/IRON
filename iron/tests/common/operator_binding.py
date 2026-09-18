#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``AIEOperatorBase.bind`` -- filling a function's parameters from an operator.

Each operator used to carry a hand-written kwargs dict that restated its own
field names to feed a function's signature, with nothing checking the two
against each other. A field renamed on one side and not the other produced a
TypeError from inside the callee, or -- worse, when the parameter had a
default -- a silently wrong value and a design compiled against it.

``bind`` matches by name and fails loudly at the boundary instead, naming both
the operator and the parameter it could not supply. These tests pin that
contract, including the failure, since the failure is the entire point.

Device-free: a device *description* is enough to construct an operator.
"""

import aie.utils as aie_utils
import pytest
from aie.iron.device import from_name

from iron.common import AIERuntimeArgSpec, MLIROperator
from iron.operators.gemm.op import GEMM
from iron.operators.mha.op import MHA
from iron.operators.softmax.op import Softmax


@pytest.fixture(autouse=True)
def device():
    """Operators read the ShimDMA limit at construction, so one must be set."""
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=4))
    yield
    aie_utils.set_current_device(previous)


def test_binds_dataclass_fields_by_name():
    operator = Softmax(rows=16, cols=64)
    assert operator.bind(lambda rows, cols: None) == {"rows": 16, "cols": 64}


def test_binds_a_property_not_just_a_field():
    """``size`` is a property over rows*cols, and must bind like a field."""
    operator = Softmax(rows=16, cols=64)
    assert operator.bind(lambda size: None) == {"size": 1024}


def test_parameter_with_a_default_and_no_attribute_is_left_alone():
    """Absent means "use the default", so the default must survive."""
    operator = Softmax(rows=16, cols=64)
    assert operator.bind(lambda rows, unrelated=7: None) == {"rows": 16}


def test_missing_parameter_names_both_sides():
    operator = Softmax(rows=16, cols=64)
    with pytest.raises(TypeError) as excinfo:
        operator.bind(lambda rows, no_such_field: None)
    message = str(excinfo.value)
    assert "Softmax" in message
    assert "no_such_field" in message


def test_var_kwargs_are_not_bound():
    """``**kwargs`` accepts anything, so there is nothing to supply for it."""
    operator = Softmax(rows=16, cols=64)
    assert operator.bind(lambda rows, **kwargs: None) == {"rows": 16}


def test_get_arg_spec_derives_from_the_declared_shape_function():
    operator = Softmax(rows=16, cols=64)
    assert operator.get_arg_spec() == Softmax.arg_spec(rows=16, cols=64)


@pytest.mark.parametrize(
    "operator, kwargs",
    [
        (GEMM, dict(M=256, K=64, N=512, b_col_maj=True)),
        (MHA, dict(num_heads=8, seq_len=100, d=64, num_KV_heads=2)),
    ],
)
def test_shape_functions_are_callable_without_an_operator(operator, kwargs):
    """A shape rule is a function of parameters, not of an instance.

    This is what lets a caller ask "what shape would this produce?" before
    committing to build the operator -- the property graph capture needs to
    place a value it has not constructed yet.
    """
    from_instance = operator(**kwargs).get_arg_spec()
    from_function = operator.arg_spec(**kwargs)
    assert from_instance == from_function


def test_operator_without_a_shape_function_says_so():
    """The base must not silently return an empty spec."""

    class Specless(MLIROperator):
        def set_up_artifacts(self):
            pass

        def get_callable(self):
            pass

        def get_mlir_artifact(self):
            pass

        def get_kernel_artifacts(self):
            return []

    with pytest.raises(NotImplementedError, match="Specless"):
        Specless().get_arg_spec()


def test_gemm_layout_flags_transpose_rather_than_resize():
    """The conditional the shape function exists to express."""
    plain = GEMM.arg_spec(M=256, K=64, N=512)
    b_major = GEMM.arg_spec(M=256, K=64, N=512, b_col_maj=True)
    c_major = GEMM.arg_spec(M=256, K=64, N=512, c_col_maj=True)

    assert plain[1].shape == (64, 512) and b_major[1].shape == (512, 64)
    assert plain[2].shape == (256, 512) and c_major[2].shape == (512, 256)
    # Transposing a layout must not change how many bytes move.
    assert plain[1].nbytes() == b_major[1].nbytes()
    assert plain[2].nbytes() == c_major[2].nbytes()


def test_mha_pads_the_sequence_and_groups_kv():
    """The helper call and the branch, both outside any declarative notation."""
    grouped = MHA.arg_spec(num_heads=8, seq_len=100, d=64, num_KV_heads=2)
    plain = MHA.arg_spec(num_heads=8, seq_len=100, d=64, num_KV_heads=0)

    # 100 rounds up to 128, so Q is 8 heads * 64 * 128.
    assert grouped[0].shape == (8 * 64 * 128,)
    # Grouped K/V are narrower than Q; plain K/V are exactly as wide.
    assert grouped[1].shape == (2 * 64 * 128,)
    assert plain[1].shape == plain[0].shape
    assert [spec.direction for spec in grouped] == ["in", "in", "in", "out"]


def test_arg_spec_returns_specs_not_tuples():
    """Callers read .direction/.shape/.dtype, so the type matters."""
    for spec in Softmax.arg_spec(rows=16, cols=64):
        assert isinstance(spec, AIERuntimeArgSpec)
