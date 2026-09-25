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
import torch

from iron.common.sequence import OperatorSequence
from iron.common.tracing_utils import dump_traces
from iron.operators.layer_norm.op import LayerNorm

SIZE = 2048
TRACE_SIZE = 8192


def _layer_norm_run(context, trace_size):
    """A dispatched one-step sequence, and its output."""
    layer_norm = LayerNorm(
        size=SIZE,
        num_aie_columns=1,
        num_channels=1,
        tile_size=SIZE,
        trace_size=trace_size,
        context=context,
    )
    seq = OperatorSequence(
        name="infra_trace_layer_norm",
        runlist=[(layer_norm, "x", "y")],
        input_args=["x"],
        output_args=["y"],
        dispatch="fused",
        trace_size=trace_size,
        context=context,
    )
    seq.compile()
    run = seq.get_callable()
    torch.manual_seed(0)
    run.get_buffer("x").torch_view()[:] = torch.randn(SIZE, dtype=torch.bfloat16)
    run()
    return run, run.get_buffer("y").torch_view()[:SIZE].clone()


@pytest.mark.supported_devices("npu2")
def test_dump_writes_raw_words_and_perfetto_json(aie_context, tmp_path):
    run, traced = _layer_norm_run(aie_context, TRACE_SIZE)
    _, untraced = _layer_norm_run(aie_context, 0)
    assert torch.equal(traced, untraced), "tracing changed the result"

    written = dump_traces(run, "layer_norm", out_dir=tmp_path, summary=False)

    words = run.trace_buffer.numpy().view(np.uint32).reshape(-1)
    assert words.any(), "the traced dispatch captured no trace data"
    # The raw text is the buffer's 32-bit words, unchanged by the int8 buffer.
    raw = (tmp_path / "layer_norm.txt").read_text().split()
    assert [int(w, 16) for w in raw] == words.tolist()

    assert written, "a buffer with trace data produced no Perfetto file"
    for path in written:
        assert path.parent == tmp_path and path.name.startswith("layer_norm_")
        assert json.loads(path.read_text()), f"{path.name} holds no events"
