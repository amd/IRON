# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The ledger of what tuning hit (``iron.tune.failures``): one entry per
signature, reopened when seen again, and rechecked with the current
toolchain. Device-free: placing runs aie-opt alone."""

import pytest

from iron.common.design import OperatorDesign
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.tanh import Tanh
from iron.tune.failures import Kind, Ledger, place, signature
from iron.tune.fusions import _composed_module

pytestmark = pytest.mark.usefixtures("npu2")


def _module(*ops):
    designs = {str(i): OperatorDesign(op) for i, op in enumerate(ops)}
    return str(_composed_module(designs))


def test_place_tells_a_fit_from_a_refusal(npu2):
    small = ReLU(size=2048, num_aie_columns=1).resolved(npu2)
    assert place(_module(small)) == ("fits", None)
    wide = [
        cls(size=8192, num_aie_columns=8, num_channels=2, tile_size=256).resolved(npu2)
        for cls in (ReLU, Tanh, Sigmoid)
    ]
    verdict, diagnostic = place(_module(*wide))
    assert verdict == "refused" and "no available compute tiles" in diagnostic


def test_a_signature_drops_numbers_and_locations():
    a = signature(Kind.CRASH, "x.mlir:12:3: error: no tile 4 at 0x55aa")
    b = signature(Kind.CRASH, "y.mlir:99:1: error: no tile 7 at 0x1234")
    assert a == b


def test_a_failure_seen_twice_is_one_entry_reopened_once_fixed(tmp_path):
    ledger = Ledger(tmp_path)
    first = ledger.record(Kind.BUILD, "npu2", "error: no tile 3", "packing decode")
    entries = ledger.entries()
    entries[0].status = "fixed"
    ledger._write(entries)
    again = ledger.record(Kind.BUILD, "npu2", "error: no tile 5", "packing decode")
    assert len(ledger.entries()) == 1 and again.status == "open"


def test_recheck_marks_a_crash_the_current_toolchain_no_longer_hits_fixed(
    npu2, tmp_path
):
    """A crash recorded under an older toolchain whose repro now places, as
    the allocator's per-device reset fixed one (mlir-aie ac265b69b9d)."""
    ledger = Ledger(tmp_path)
    ledger.record(
        Kind.CRASH,
        "npu2",
        "aie-opt: STLExtras.h: Assertion `isa<To>(Val)' failed.",
        "placing a pack beside a second device",
        module=_module(ReLU(size=2048, num_aie_columns=1).resolved(npu2)),
    )
    [(entry, verdict)] = ledger.recheck()
    assert verdict != "crash"
    assert entry.status == "fixed" and entry.fixed_by is not None
