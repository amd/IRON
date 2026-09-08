# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reading back the trace buffer size the compiler recorded on the sequence."""

from iron.common.compilation import trace_buffer_size

LOWERED = """
module {
  aie.device(npu1_1col) @main {
    aie.runtime_sequence @sequence(%arg0: memref<4xi32>, %arg1: memref<12288xi8>)
        attributes {trace_slices = [
          #aie.trace_slice<device = "dev_a", sequence = "seq", offset = 0, size = 8192>,
          #aie.trace_slice<device = "dev_b", sequence = "seq", offset = 8192, size = 4096>]} {
    }
  }
}
"""

UNTRACED = """
module {
  aie.device(npu1_1col) @main {
    aie.runtime_sequence @sequence(%arg0: memref<4xi32>) {
    }
  }
}
"""


def test_size_spans_every_slice():
    assert trace_buffer_size(LOWERED) == 12288


def test_untraced_build_has_no_trace_buffer():
    assert trace_buffer_size(UNTRACED) == 0
