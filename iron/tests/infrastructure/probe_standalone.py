# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The tuner's probe, a design run alone on buffers of its own, on the NPU."""

import numpy as np
import pytest

import iron
from iron.common.graph.probe import Standalone
from iron.operators.copy import Copy

pytestmark = pytest.mark.usefixtures("npu2")


class Ids(iron.Graph):
    def body(self, ids):
        return Copy(ids, dtype=np.int32)


@pytest.mark.supported_devices("npu2")
def test_repeats_on_buffers_off_the_coherence_line_are_read_back(npu_runtime):
    # 15 ids are 60 bytes: slot 0's end inside a 64-byte line slot 1's share.
    op = Ids().trace(ids=((15,), np.int32)).steps[0].op
    alone = Standalone("probe_ids15x2", [op, op], distinct=True)
    ids = [
        alone.callable.get_storage(f"s{k}_x").numpy_view()[:15].copy() for k in range(2)
    ]
    got = np.frombuffer(alone.output_bytes(), np.int32)
    np.testing.assert_array_equal(got, np.concatenate(ids))
