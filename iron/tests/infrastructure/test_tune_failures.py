# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The ledger of what tuning hit (``iron.tune.failures``).

One entry per signature, reopened when seen again, and rechecked with the current toolchain.
"""

import subprocess
import sys

import pytest
from aie.utils.hostruntime.hostruntime import HostRuntimeError

from iron.common.design import OperatorDesign
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.tanh import Tanh
from iron.tune.autotune import Shape, refused_hang
from iron.tune.failures import Kind, Ledger, device_timeout, place, signature
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


def test_device_timeout_recognizes_the_drivers_own_ends():
    """A timeout, and amdxdna 2.27's abort once its recovery takes the command."""
    assert device_timeout(
        RuntimeError(
            "fuse_rewritten1: the run ended in ert_cmd_state.ERT_CMD_STATE_TIMEOUT"
        )
    )
    assert device_timeout(
        HostRuntimeError("Kernel returned ert_cmd_state.ERT_CMD_STATE_ABORT")
    )


def test_device_timeout_is_false_for_an_ordinary_build_failure():
    assert not device_timeout(ValueError("GEMV: B is fed 1 lane(s), but ..."))
    assert not device_timeout(
        RuntimeError("[aiecc] Compilation failed with exit code 1")
    )


def test_a_batch_that_hangs_the_device_is_refused_and_recorded(npu2, tmp_path):
    """A tune's batch ending in the driver's abort refuses all but the recorded setting rather than ending the tune."""
    shape = Shape(ReLU(size=2048, num_aie_columns=1))
    found = [{"tile_size": 1024}, {"tile_size": 512}, {"tile_size": 256}]
    hung = HostRuntimeError("Kernel returned ert_cmd_state.ERT_CMD_STATE_ABORT")
    ledger = Ledger(tmp_path)
    trials = refused_hang(hung, shape, found, npu2, ledger, lambda _: None)
    assert [t.refused for t in trials] == [None, Kind.HANG.value, Kind.HANG.value]
    assert not any(t.gains for t in trials)
    [entry] = ledger.entries()
    assert entry.kind == Kind.HANG.value and "tile_size" in entry.context


def test_a_signature_drops_numbers_and_locations():
    a = signature(Kind.CRASH, "x.mlir:12:3: error: no tile 4 at 0x55aa")
    b = signature(Kind.CRASH, "y.mlir:99:1: error: no tile 7 at 0x1234")
    assert a == b


def test_a_failure_seen_twice_is_one_entry_reopened_once_fixed(tmp_path):
    ledger = Ledger(tmp_path)
    ledger.record(Kind.BUILD, "npu2", "error: no tile 3", "packing decode")
    entries = ledger.entries()
    entries[0].status = "fixed"
    ledger._write(entries)
    again = ledger.record(Kind.BUILD, "npu2", "error: no tile 5", "packing decode")
    assert len(ledger.entries()) == 1 and again.status == "open"


def test_recheck_marks_a_crash_the_current_toolchain_no_longer_hits_fixed(
    npu2, tmp_path
):
    """A crash recorded under an older toolchain whose repro now places, as the allocator's per-device reset fixed one (mlir-aie ac265b69b9d)."""
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


def test_processes_recording_at_once_lose_no_entry(tmp_path):
    """Eight tunes on one machine each record failures of their own into its ledger at once."""
    script = (
        "import string, sys\n"
        "from pathlib import Path\n"
        "from iron.tune.failures import Kind, Ledger\n"
        "ledger, worker = Ledger(Path(sys.argv[1])), sys.argv[2]\n"
        "for letter in string.ascii_lowercase:\n"
        "    ledger.record(Kind.BUILD, 'npu2', f'error: {worker} {letter}', 'x')\n"
    )
    workers = [
        subprocess.Popen([sys.executable, "-c", script, str(tmp_path), w])
        for w in ("alpha", "beta", "gamma", "delta", "eps", "zeta", "eta", "theta")
    ]
    assert all(w.wait() == 0 for w in workers)
    assert len(Ledger(tmp_path).entries()) == 8 * 26
