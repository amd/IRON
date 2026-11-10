# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``MHAPrefillStream``: the head it hands stream-dse."""

import pytest

pytest.importorskip("stream", reason="stream-dse is not installed")
pytest.importorskip("onnxscript", reason="onnxscript is not installed")

from iron.operators.mha_prefill_stream.op import MHAPrefillStream  # noqa: E402

pytestmark = pytest.mark.usefixtures("npu2")


def test_a_head_matmul_pv_does_not_compile_is_refused():
    """mha.cc takes a head of a multiple of 16: 128 is one, 72 is not."""
    MHAPrefillStream(heads=2, seq_len=256, d_head=128).compatible()
    with pytest.raises(ValueError, match="d_head"):
        MHAPrefillStream(heads=2, seq_len=256, d_head=72).compatible()
