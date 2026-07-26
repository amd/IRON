#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The names the design is built from must be the golden reference's names.

Every tensor the operator exports, maps and wires is named once, in
:mod:`iron.operators.swiglu_prefill_stream.reference`, using the vocabulary the
shared golden reference uses for the same tensors. These tests pin that
correspondence, and pin that the mapping and the fused-group wiring take their
names from the exported graph rather than restating them.
"""

import pytest

from iron.operators.swiglu_decode.reference import generate_golden_reference
from iron.operators.swiglu_prefill_stream import reference

SHAPE = dict(M=8, K=8, N=16)


@pytest.fixture(scope="module")
def golden_keys():
    return set(generate_golden_reference(**SHAPE))


@pytest.mark.parametrize("name", reference.TENSOR_NAMES)
def test_name_is_a_golden_reference_key(name, golden_keys):
    assert name in golden_keys


def test_module_parameters_cover_the_golden_weights():
    module = reference.swiglu_module(SHAPE["K"], SHAPE["N"])
    assert set(dict(module.named_parameters())) == set(reference.WEIGHTS.values())


def test_golden_weights_load_into_the_module():
    golden = generate_golden_reference(**SHAPE)
    module = reference.swiglu_module(SHAPE["K"], SHAPE["N"], golden)
    for name, parameter in reference.WEIGHTS.items():
        assert getattr(module, parameter).equal(golden[name])


stream = pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

from iron.operators.swiglu_prefill_stream import stream_design  # noqa: E402

DIMS = (256, 512, 2048)


@pytest.mark.parametrize("split_groups", [False, True])
def test_group_ports_are_named_by_the_exported_graph(split_groups):
    workload = stream_design.workload_for(*DIMS)
    known = set(workload.buffers) | set(reference.TENSOR_NAMES)
    for inputs, outputs in stream_design.group_ports(*DIMS, split_groups):
        assert set(inputs) | set(outputs) <= known


def test_split_design_hands_on_the_hidden_state():
    (_, front_outputs), (down_inputs, _) = stream_design.group_ports(
        *DIMS, split_groups=True
    )
    assert front_outputs == (reference.HIDDEN,)
    assert down_inputs[0] == reference.HIDDEN


def test_external_arguments_match_the_runtime_buffers():
    workload = stream_design.workload_for(*DIMS)
    boundaries = stream_design.group_ports(*DIMS, split_groups=True)
    produced = {name for _, outputs in boundaries for name in outputs}
    consumed = {name for inputs, _ in boundaries for name in inputs}
    external = [
        name for inputs, _ in boundaries for name in inputs if name not in produced
    ] + [name for _, outputs in boundaries for name in outputs if name not in consumed]
    assert set(external) == set(workload.buffers)
