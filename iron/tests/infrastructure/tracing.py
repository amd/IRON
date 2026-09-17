# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Trace dumps use the upstream tensor's host interface without torch."""

import json
from types import SimpleNamespace

import numpy as np
import pytest
from aie.utils.hostruntime.tensor_class import CPUOnlyTensor

from iron.common import tracing_utils


@pytest.mark.parametrize("dtype", [np.int8, np.uint8])
def test_dump_preserves_raw_trace_bits(monkeypatch, tmp_path, dtype):
    words = np.array([0xFFFFFFFF, 0x80000000, 0x12345678, 0], dtype=np.uint32)
    buffer = CPUOnlyTensor(words.view(dtype), dtype=dtype)
    run = SimpleNamespace(trace_buffer=buffer)
    monkeypatch.setattr(
        tracing_utils, "lowered_mlir", lambda run: (tmp_path / "test.mlir", "mlir")
    )
    events = [{"name": "event"}]

    def parse(actual, mlir_text, colshift):
        np.testing.assert_array_equal(actual, words)
        assert mlir_text == "mlir"
        assert colshift == 2
        return [(None, events)]

    monkeypatch.setattr(tracing_utils, "parse_trace_buffer", parse)
    written = tracing_utils.dump_traces(
        run, "test", out_dir=tmp_path, colshift=2, summary=False
    )

    assert written == [tmp_path / "test_trace.json"]
    assert json.loads(written[0].read_text()) == events
    assert (tmp_path / "test.txt").read_text().splitlines() == [
        "ffffffff",
        "80000000",
        "12345678",
        "00000000",
    ]


def test_untraced_run_needs_no_buffer(tmp_path):
    assert tracing_utils.dump_traces(SimpleNamespace(), "test", tmp_path) == []
