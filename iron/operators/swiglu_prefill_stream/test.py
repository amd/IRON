# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pytest
from aie.utils.verify import compare
from ml_dtypes import bfloat16

pytest.importorskip("stream", reason="stream-dse is not installed")
pytest.importorskip("onnxscript", reason="onnxscript is not installed")

from iron.common.testing import time_call  # noqa: E402
from iron.operators.swiglu_prefill_stream.graph import SwiGLUPrefillStream  # noqa: E402
from iron.operators.swiglu_prefill_stream.op import SwiGLUFusedStream  # noqa: E402

pytestmark = pytest.mark.supported_devices("npu2")


def _block(seq_len, embedding_dim, hidden_dim, seed=42):
    """Draw an input and weights whose projections stay of order one."""
    rng = np.random.default_rng(seed)
    scale = embedding_dim**-0.25

    def draw(*shape):
        return (rng.standard_normal(shape) * scale).astype(bfloat16)

    return (
        draw(seq_len, embedding_dim),
        draw(embedding_dim, hidden_dim),
        draw(embedding_dim, hidden_dim),
        draw(hidden_dim, embedding_dim),
    )


def _check(seq_len, embedding_dim, hidden_dim, k, record=None):
    x, w_gate, w_up, w_down = _block(seq_len, embedding_dim, hidden_dim)
    version = SwiGLUPrefillStream(w_gate, w_up, w_down, k=k).compile(
        x=(seq_len, embedding_dim)
    )
    out = np.asarray(version(x), dtype=np.float32)
    whole = SwiGLUFusedStream(
        seq_len=seq_len, embedding_dim=embedding_dim, hidden_dim=hidden_dim
    )
    verdict = compare(out, whole.reference(x, w_gate, w_up, w_down), whole.tolerance())
    assert verdict, verdict.detail
    if record is not None:
        time_call(version.callable, ops=whole.ops(), record=record)
    return version


@pytest.mark.parametrize("k", [pytest.param(None, marks=pytest.mark.bench), 1, 5])
def test_each_partition_computes_the_block(k, record_property):
    """None is the partition stream-dse prices cheapest; 1 and 5 are forced."""
    _check(256, 512, 2048, k, record_property)


def test_layer_by_layer_runs_a_step_per_group():
    version = _check(256, 512, 2048, k=5)
    assert len(version.recording.steps) == 5


@pytest.mark.extensive
def test_a_split_layer_takes_part_of_a_row():
    """At a hidden dimension of 4096 each elementwise core takes half a row."""
    _check(256, 1024, 4096, k=5)
