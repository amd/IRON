# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's side of tracing.

The full-ELF sequence callable binds, fills and syncs the trace buffer
mlir-aie's lowering asks for, and dump_traces writes it out.

Trace insertion, the buffer layout and event decoding are mlir-aie's,
and tested there.
"""

import dataclasses
import json

import numpy as np
import pytest
from aie.utils.trace import TraceConfig
from ml_dtypes import bfloat16

import iron
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef
from iron.common.tracing import dump_traces
from iron.operators import LayerNorm

SIZE = 2048


def _layer_norm_run(name, trace):
    """Dispatch a one-step full-ELF sequence, and return it with its output."""
    layer_norm = LayerNorm(
        rows=1,
        num_aie_columns=1,
        num_channels=1,
        tile_size=SIZE,
        trace=trace,
    )

    class F(iron.Graph):
        def body(self, x):
            return layer_norm(x)

    f = F()

    recording = f.record(x=(1, SIZE))
    seq = Image(dataclasses.replace(recording, name=name), FullELF()).compile()
    run = seq.get_callable()
    x = run.get_buffer(BufferRef("x"))
    x.numpy_view()[:] = np.random.default_rng(0).standard_normal(SIZE).astype(bfloat16)
    run()
    return run, run.get_buffer(recording.outputs[0].ref()).numpy()[:SIZE].copy()


@pytest.mark.supported_devices("npu2")
def test_dump_writes_raw_words_and_perfetto_json(tmp_path):
    run, traced = _layer_norm_run("infra_trace_layer_norm", TraceConfig(8192))
    _, untraced = _layer_norm_run("infra_trace_layer_norm_off", None)
    assert np.array_equal(
        traced.view(np.uint16), untraced.view(np.uint16)
    ), "tracing changed the result"

    written = dump_traces(run, tmp_path / "layer_norm.txt", summary=False)

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
