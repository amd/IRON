# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's side of tracing: the full-ELF sequence callable binds, fills and syncs
the trace buffer mlir-aie's lowering asks for, and dump_traces writes it out.

Trace insertion, the buffer layout and event decoding are mlir-aie's, and tested
there.
"""

import json

import numpy as np
import pytest
from aie.utils.trace import TraceConfig
from ml_dtypes import bfloat16

import iron
from iron.common.tracing import dump_traces
from iron.operators import LayerNorm

SIZE = 2048
TRACE_SIZE = 8192


def _layer_norm_run(name, trace_size):
    """A dispatched one-step fused sequence, and its output."""
    layer_norm = LayerNorm(
        size=SIZE,
        num_aie_columns=1,
        num_channels=1,
        tile_size=SIZE,
        trace_size=trace_size,
    )

    @iron.graph
    def f(x):
        return layer_norm(x)

    traced = f.trace(x=(SIZE,))
    seq = traced.sequence(name, dispatch="fused", trace_size=trace_size).compile()
    run = seq.get_callable()
    x = run.get_buffer("x")
    x.numpy_view()[:] = np.random.default_rng(0).standard_normal(SIZE).astype(bfloat16)
    run()
    return run, run.get_buffer(traced.output_args[0]).numpy()[:SIZE].copy()


@pytest.mark.supported_devices("npu2")
def test_dump_writes_raw_words_and_perfetto_json(npu_runtime, tmp_path):
    run, traced = _layer_norm_run("infra_trace_layer_norm", TRACE_SIZE)
    _, untraced = _layer_norm_run("infra_trace_layer_norm_off", 0)
    assert np.array_equal(
        traced.view(np.uint16), untraced.view(np.uint16)
    ), "tracing changed the result"

    written = dump_traces(run, "layer_norm", out_dir=tmp_path, summary=False)

    assert run.trace_buffer is not None
    words = run.trace_buffer.numpy().view(np.uint32).reshape(-1)
    assert words.any(), "the traced dispatch captured no trace data"
    # The text reads back as the buffer's 32-bit words, unchanged by the int8
    # buffer, so it can be reparsed without another dispatch.
    raw = TraceConfig(
        trace_size=words.nbytes, trace_file=str(tmp_path / "layer_norm.txt")
    )
    assert np.array_equal(raw.read_trace(), words)

    assert written, "a buffer with trace data produced no Perfetto file"
    for path in written:
        assert path.parent == tmp_path and path.name.startswith("layer_norm")
        assert json.loads(path.read_text()), f"{path.name} holds no events"
