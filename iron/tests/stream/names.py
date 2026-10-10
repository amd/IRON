#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The names the design is built from must be the golden reference's names.

Every tensor the operator builds, maps and wires is named once, in
``iron.operators.swiglu_prefill_stream.reference``, using the vocabulary its
golden reference uses for the same tensors. These tests pin that
correspondence, and pin that the mapping and the fused-group wiring take their
names from the workload's graph rather than restating them.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare

from iron.operators.swiglu_prefill_stream import reference

SHAPE = dict(M=8, K=8, N=16)


@pytest.fixture(scope="module")
def golden_keys():
    return set(reference.generate_golden_reference(**SHAPE))


@pytest.mark.parametrize("name", reference.TENSOR_NAMES)
def test_name_is_a_golden_reference_key(name, golden_keys):
    assert name in golden_keys


def test_the_operands_no_layer_produces_are_the_input_and_the_weights():
    produced = {result for result, _, _ in reference.LAYERS}
    operands = {name for _, _, names in reference.LAYERS for name in names}
    assert operands - produced == {reference.INPUT, *reference.WEIGHTS}


def test_layers_compute_swiglu():
    """The workload is built from these layers and the result is checked against
    their evaluation, so they have to be SwiGLU.
    """
    golden = reference.generate_golden_reference(**SHAPE)
    x, gate, up, down = (
        golden[name].astype(np.float64)
        for name in (reference.INPUT, *reference.WEIGHTS)
    )
    left = x @ gate
    expected = (left / (1 + np.exp(-left)) * (x @ up)) @ down
    # Four bfloat16 roundings between the input and the output.
    verdict = compare(
        golden[reference.OUTPUT], expected, Tolerance.relative(2**-6, range_frac=2**-7)
    )
    assert verdict, verdict.detail


DIMS = (256, 512, 2048)


@pytest.fixture(scope="module")
def stream_design():
    pytest.importorskip(
        "stream", reason="stream-dse not installed (see requirements_stream.txt)"
    )
    # Optional dependency: the design's modules import onnx and stream-dse.
    from iron.operators.swiglu_prefill_stream import stream_design

    return stream_design


@pytest.mark.parametrize("k", [1, 2, 5])
def test_group_ports_are_named_by_the_exported_graph(k, stream_design):
    workload = stream_design.workload_for(*DIMS)
    known = set(workload.buffers) | set(reference.TENSOR_NAMES)
    for inputs, outputs in stream_design.group_ports(*DIMS, k):
        assert set(inputs) | set(outputs) <= known


def test_split_design_hands_on_the_hidden_state(stream_design):
    (_, front_outputs), (down_inputs, _) = stream_design.group_ports(*DIMS, k=2)
    assert front_outputs == (reference.HIDDEN,)
    assert down_inputs[0] == reference.HIDDEN


def test_external_arguments_match_the_runtime_buffers(stream_design):
    workload = stream_design.workload_for(*DIMS)
    boundaries = stream_design.group_ports(*DIMS, k=2)
    produced = {name for _, outputs in boundaries for name in outputs}
    consumed = {name for inputs, _ in boundaries for name in inputs}
    external = [
        name for inputs, _ in boundaries for name in inputs if name not in produced
    ] + [name for _, outputs in boundaries for name in outputs if name not in consumed]
    assert set(external) == set(workload.buffers)
