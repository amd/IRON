# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reading back the trace buffer layout the compiler recorded on the sequence."""

from iron.common.compilation import trace_buffer_layout

LOWERED = """
module {
  aie.device(npu1_1col) {
    aie.runtime_sequence @sequence(%arg0: memref<4xi32>, %arg1: memref<12288xi8>)
        attributes {aie.trace_slices = [
          {device = "dev_a", offset = 0 : i64, sequence = "seq", size = 8192 : i64},
          {device = "dev_b", offset = 8192 : i64, sequence = "seq", size = 4096 : i64}]} {
    }
  }
}
"""

UNTRACED = """
module {
  aie.device(npu1_1col) {
    aie.runtime_sequence @sequence(%arg0: memref<4xi32>) {
    }
  }
}
"""


def test_total_spans_every_slice():
    total, slices = trace_buffer_layout(LOWERED)
    assert total == 12288
    assert [s["offset"] for s in slices] == [0, 8192]
    assert [s["size"] for s in slices] == [8192, 4096]


def test_each_slice_names_the_design_that_wrote_it():
    _, slices = trace_buffer_layout(LOWERED)
    assert [s["device"] for s in slices] == ["dev_a", "dev_b"]


def test_untraced_build_has_no_trace_buffer():
    assert trace_buffer_layout(UNTRACED) == (0, [])
