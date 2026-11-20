# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""DDR bandwidth: the device's read ceiling, and each weight-bound toy's share of it."""

from __future__ import annotations

import pytest

from iron.common.testing import time_call, vectors
from iron.operators.gemv import GEMV

pytestmark = [pytest.mark.extensive, pytest.mark.supported_devices("npu1", "npu2")]

# (columns, channels) requested per nominal stream count; GEMV.resolve clips
# each to what the bound device actually supports, so the achieved count
# (read back off the resolved operator) is what is recorded against, never
# the request.
_REQUESTED = {1: (1, 1), 2: (2, 1), 4: (4, 1), 8: (8, 1), 16: (8, 2)}


def _weight_bound_gemv(M, K, columns, channels):
    return GEMV(M=M, K=K, feed_b=True, num_aie_columns=columns, num_channels=channels)


@pytest.mark.parametrize("nominal_streams", sorted(_REQUESTED))
def test_ddr_read_ceiling_against_stream_count(
    nominal_streams, record_property, device
):
    """The ceiling: a large weight-bound GEMV's achieved read bandwidth at each stream count the device supports."""
    columns, channels = _REQUESTED[nominal_streams]
    op = _weight_bound_gemv(8192, 2048, columns, channels)
    resolved = op.resolved(device)
    streams = resolved.num_aie_columns * resolved.num_channels
    record_property("Requested streams", nominal_streams)
    record_property("Achieved streams", streams)
    A = vectors(op).inputs["A"]
    B = vectors(op, seed=3).inputs["B"]
    time_call(
        op,
        A,
        B,
        bytes_moved=A.nbytes,
        record=record_property,
        warmup=3,
        iters=20,
    )


@pytest.mark.parametrize("nominal_streams", [1, 4, 8])
def test_weight_bound_toy_reports_its_share_of_the_ceiling(
    nominal_streams, record_property, device
):
    """A smaller weight-bound GEMV, at the same stream count as a ceiling row, records its bandwidth as a fraction of that row's.

    The ceiling row runs first in this test (not shared across tests, so each
    is self-contained and device-free of ordering assumptions), then the
    toy; the ratio is recorded, never asserted, since it is a finding to
    attribute (IRON's access pattern, mlir-aie's defaults, or the hardware).
    """
    columns, channels = _REQUESTED[nominal_streams]
    ceiling_op = _weight_bound_gemv(8192, 2048, columns, channels)
    ceiling_A = vectors(ceiling_op).inputs["A"]
    ceiling_B = vectors(ceiling_op, seed=5).inputs["B"]
    ceiling_record = {}
    time_call(
        ceiling_op,
        ceiling_A,
        ceiling_B,
        bytes_moved=ceiling_A.nbytes,
        record=lambda name, value: ceiling_record.__setitem__(name, value),
        warmup=3,
        iters=20,
    )

    toy_op = _weight_bound_gemv(2048, 2048, columns, channels)
    toy_A = vectors(toy_op).inputs["A"]
    toy_B = vectors(toy_op, seed=7).inputs["B"]
    toy_record = {}
    time_call(
        toy_op,
        toy_A,
        toy_B,
        bytes_moved=toy_A.nbytes,
        record=lambda name, value: toy_record.__setitem__(name, value),
        warmup=3,
        iters=20,
    )
    record_property("Ceiling bandwidth GB/s", ceiling_record["Bandwidth"])
    record_property("Toy bandwidth GB/s", toy_record["Bandwidth"])
    record_property(
        "Toy share of ceiling", toy_record["Bandwidth"] / ceiling_record["Bandwidth"]
    )
