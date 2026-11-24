# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A tune's pre-flight (``iron.tune.cli.preflight``): what it refuses before any search."""

import subprocess
import sys

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.operators.relu import ReLU
from iron.tests.support.graphs import Chain
from iron.tune.autotune import Timed
from iron.tune.cli import preflight, watchdog_s
from iron.tune.measure import Cache, Timing, platform

LONG = 2**22


class Narrow(iron.Graph):
    """Two ReLUs over a long vector at one column: a millisecond and more a call."""

    def body(self, x):
        return ReLU.step(ReLU.step(x, num_aie_columns=1), num_aie_columns=1)


def narrow(profile: Profile) -> list[Timed]:
    graph = Narrow()
    graph.profile = profile
    return [Timed(graph.record(x=(LONG,)))]


def _cache(tmp_path) -> Cache:
    report = platform()
    return Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")


def test_a_watchdog_is_read_in_seconds_from_either_parameter(tmp_path):
    (tmp_path / "new").mkdir()
    (tmp_path / "new" / "tdr_timeout_ms").write_text("20000\n")
    (tmp_path / "old").mkdir()
    (tmp_path / "old" / "timeout_in_sec").write_text("10\n")
    assert watchdog_s(tmp_path / "new") == 20.0
    assert watchdog_s(tmp_path / "old") == 10.0
    assert watchdog_s(tmp_path) is None


def test_calls_that_do_not_record_stop_the_tune_before_any_search(npu2, tmp_path):
    def broken(profile: Profile) -> list[Timed]:
        return [Timed(Chain(8192, 256).record(a=(8192,), b=(4096,)))]

    with pytest.raises(SystemExit, match="do not record on this host: Chain"):
        preflight(
            broken,
            Profile(),
            npu2,
            timing=Timing(rounds=2, calls=5),
            repeats=5,
            cache=None,
            watchdog=tmp_path,
        )


# ---------------------------------------------------------------------------
# On the device
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("watchdog_ms, refused", [(1, True), (60000, False)])
def test_a_watchdog_under_twice_the_longest_command_stops_the_tune(
    tmp_path, watchdog_ms, refused
):
    dev = aie_utils.ensure_current_device()
    (tmp_path / "params").mkdir()
    (tmp_path / "params" / "tdr_timeout_ms").write_text(f"{watchdog_ms}\n")
    logged: list[str] = []
    run = dict(
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=_cache(tmp_path),
        log=logged.append,
        watchdog=tmp_path / "params",
    )
    if refused:
        with pytest.raises(SystemExit, match=r"watchdog is 0\.001 s .* echo \d+ >"):
            preflight(narrow, Profile(), dev, **run)
    else:
        preflight(narrow, Profile(), dev, **run)
        assert logged[-1].startswith("pre-flight: watchdog 60 s;"), logged


@pytest.mark.supported_devices("npu2")
def test_an_npu_another_process_holds_stops_the_tune(tmp_path):
    """Another process holds a context, loaded and verified, while the tune would start."""
    holder = subprocess.Popen(
        [
            sys.executable,
            "-c",
            "import time\n"
            "import numpy as np\n"
            "from ml_dtypes import bfloat16\n"
            "import iron\n"
            "from iron.operators.relu import ReLU\n"
            "class Once(iron.Graph):\n"
            "    def body(self, x):\n"
            "        return ReLU.step(x)\n"
            "x = np.linspace(-2, 2, 8192).astype(bfloat16)\n"
            "held = Once().compile(x=(8192,))\n"
            "out = np.asarray(held(x))\n"
            "assert np.array_equal(out, np.maximum(x, 0)), out\n"
            "print('held', flush=True)\n"
            "time.sleep(600)\n",
        ],
        stdout=subprocess.PIPE,
        text=True,
    )
    try:
        assert holder.stdout is not None
        assert holder.stdout.readline().strip() == "held"
        with pytest.raises(SystemExit, match=rf"pid \[{holder.pid}\] holds the NPU"):
            preflight(
                narrow,
                Profile(),
                aie_utils.ensure_current_device(),
                timing=Timing(rounds=2, calls=5),
                repeats=5,
                cache=_cache(tmp_path),
                watchdog=tmp_path,
            )
    finally:
        holder.kill()
        holder.wait()
    x = np.full(LONG, -1.0, bfloat16)
    assert not np.asarray(Narrow().compile(x=(LONG,))(x)).any()
