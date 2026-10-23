# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Autotuning on the NPU: settings timed, cached and written to a profile a
graph then runs bit-identically with. What needs no device is checked in
``iron/tests/toolchain/test_autotune.py``.
"""

import dataclasses
import math
import os
import re
import subprocess
import sys
import time

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.benchmark import other_npu_users
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.operators import GEMV, MHA, ElementwiseAdd, SiLU, Softmax
from iron.tests.support.graphs import Chain, FeedForward
from iron.tune.autotune import Timed, autotune, settings
from iron.tune.measure import (
    CONTEXTS,
    Cache,
    Standalone,
    Timing,
    measure,
    platform,
    time_interleaved,
)

SIZE = 8192
TILE = 256

pytestmark = pytest.mark.supported_devices("npu2")


class Masked(iron.Graph):
    """A softmax over each row's first `n` entries, `n` given per call."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return Softmax.step(x[:, :n])


class Attend(iron.Graph):
    """One query's heads over the first `n` rows of a key and value cache."""

    def body(self, q, k, v, *, n: Scratchpad[np.int32]):
        return MHA.step(q, k[:n], v[:n], heads_interleaved=True, kv_interleaved=True)


def quiet(_):
    pass


def ops(op):
    """``op`` at each of its settings, the recorded one first."""
    dev = aie_utils.ensure_current_device()
    return [op._with_tunables(**s).resolved(dev) for s in settings(op, dev)]


def _cache(tmp_path):
    report = platform()
    return Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")


@pytest.mark.extensive
def test_a_value_derived_from_a_bound_extent_follows_the_call():
    # MHA's KV block count follows the context, which the call gives alone.
    recording = Attend().record(q=(1, 32, 64), k=(2048, 8, 64), v=(2048, 8, 64))
    [op] = {s.op for s in recording.steps}
    t_step = {
        n: measure(
            [op.resolved()],
            full_elf=True,
            timing=Timing(rounds=2, calls=10),
            values=Timed(recording, dict(n=n)).op_values(op),
            log=quiet,
        )[0].t_step_us
        for n in (64, 2048)
    }
    assert t_step[2048] > 3 * t_step[64], t_step


@pytest.mark.extensive
def test_measures_more_settings_than_one_batch_of_contexts():
    # A run that writes a per-call value loads its context when it is built.
    found = ops(Masked().record(x=(256, 256)).steps[0].op)
    assert len(found) > CONTEXTS // 2
    ran = measure(
        found,
        full_elf=True,
        timing=Timing(rounds=1, calls=5),
        values={"length": 200, "valid_cols": 200},
        log=quiet,
    )
    assert ran.keys() == set(range(len(found)))


@pytest.mark.extensive
def test_a_setting_far_behind_the_fastest_is_timed_no_further():
    # GEMV at one column is several times its widest's step.
    found = ops(GEMV(M=2048, K=2048))
    timing = Timing(rounds=4, calls=10, settle=1)
    cut = measure(found, full_elf=True, timing=timing, log=quiet)
    full = measure(
        found,
        full_elf=True,
        timing=dataclasses.replace(timing, cutoff=math.inf),
        log=quiet,
    )
    assert all(len(m.round_us) == timing.rounds for m in full.values())
    stopped = {i for i, m in cut.items() if len(m.round_us) < timing.rounds}
    assert stopped and 0 not in stopped
    # Timed in full, what was stopped is still well behind the fastest.
    best = min(m.t_step_us for m in full.values())
    assert all(full[i].t_step_us > 1.2 * best for i in stopped)


@pytest.mark.extensive
def test_a_cached_setting_is_not_timed_again(tmp_path):
    found = ops(ElementwiseAdd(size=SIZE, tile_size=TILE))
    cache = _cache(tmp_path)
    timing = Timing(rounds=3, calls=5)
    first = measure(found, full_elf=True, timing=timing, cache=cache, log=quiet)
    logged = []
    again = measure(found, full_elf=True, timing=timing, cache=cache, log=logged.append)
    assert again == first and not logged
    # Each pairs round for round with the default timed in its own batch.
    for i, m in first.items():
        assert len(m.default_round_us) == (0 if i == 0 else len(m.round_us))
        assert i == 0 or m.against_default()[1] is not None


@pytest.mark.extensive
def test_a_tuned_profile_runs_bit_identically(tmp_path):
    recording = Chain(SIZE, TILE).record(a=(SIZE,), b=(SIZE,))
    dev = aie_utils.ensure_current_device()
    profile = autotune(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=10),
        cache=_cache(tmp_path),
        log=quiet,
    )
    assert len(profile)
    tuned = Chain(SIZE, TILE).compile(
        full_elf=True, profile=profile, a=(SIZE,), b=(SIZE,)
    )
    plain = Chain(SIZE, TILE).compile(full_elf=True, a=(SIZE,), b=(SIZE,))
    rng = np.random.default_rng(0)
    a = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    b = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(a, b).numpy()[:SIZE])
    got = np.array(tuned(a, b).numpy()[:SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()


@pytest.mark.extensive
def test_one_operator_is_timed_from_the_command_line(tmp_path):
    run = subprocess.run(
        [
            sys.executable,
            "-m",
            "iron.tune.cli",
            "ElementwiseAdd",
            f"size={SIZE}",
            f"tile_size={TILE}",
            "--rounds=1",
            "--calls=5",
        ],
        env=os.environ | {"NPU_CACHE_HOME": str(tmp_path / "cache")},
        capture_output=True,
        text=True,
    )
    assert run.returncode == 0, run.stderr
    printed = [line for line in run.stdout.splitlines() if " us" in line]
    assert len(printed) == len(ops(ElementwiseAdd(size=SIZE, tile_size=TILE)))
    assert sum("(recorded)" in line for line in printed) == 1


HOLD = """
import sys
import time

import aie.utils as aie_utils
from iron.tune.measure import Standalone
from iron.operators import ElementwiseAdd

aie_utils.ensure_current_device()
run = Standalone("held", [ElementwiseAdd(size=8192, tile_size=256)])
run.callable()
print("held", flush=True)
time.sleep(float(sys.argv[1]))
# Its context goes with its kernel handles; the runtime then lets the NPU go.
del run
aie_utils.cleanup_npu_runtime()
print("released", time.monotonic(), flush=True)
"""


def test_timing_waits_for_another_process_to_leave_the_npu():
    """No timed call overlaps another process's hold on the NPU: under
    NPU_LOCK the hold blocks this process's first call, without it timing
    waits until the holder is gone (``wait_idle``). Either way the timing
    ends after the holder lets go, though it began while it held.
    """
    child = subprocess.Popen(
        [sys.executable, "-c", HOLD, "3"], stdout=subprocess.PIPE, text=True
    )
    assert child.stdout.readline().strip() == "held"
    # In a container xrt-smi reports the child by its host pid, not child.pid.
    assert len(other_npu_users()) == 1
    began = time.monotonic()
    run = Standalone("waits", [SiLU(size=SIZE, tile_size=TILE)])
    time_interleaved([run.callable], Timing(rounds=2, calls=5), log=lambda _: None)
    ended = time.monotonic()
    word, released = child.stdout.readline().split()
    assert child.wait() == 0 and word == "released"
    assert began < float(released) < ended


STARVE = """
import os
import subprocess
import sys

import aie.utils as aie_utils
from aie.utils.benchmark import CompletionCores
from iron.tune.measure import Standalone, Timing, time_interleaved
from iron.operators import SiLU

SPIN = (
    "import os, sys\\n"
    "os.sched_setaffinity(0, {int(sys.argv[1])})\\n"
    "print('spinning', flush=True)\\n"
    "while True: pass\\n"
)

aie_utils.ensure_current_device()
run = Standalone("starved", [SiLU(size=8192, tile_size=256)])
before = CompletionCores.interrupts()
run.callable()
# The cores timing holds the thread on, or where no completion interrupt is
# visible (/proc/interrupts in some containers) one core it is left on.
cores = CompletionCores(before).cpus or {min(os.sched_getaffinity(0))}
os.sched_setaffinity(0, cores)
spinners = [
    subprocess.Popen([sys.executable, "-c", SPIN, str(cpu)], stdout=subprocess.PIPE, text=True)
    for cpu in sorted(cores)
]
try:
    assert all(s.stdout.readline().strip() == "spinning" for s in spinners), cores
    os.setpriority(os.PRIO_PROCESS, 0, 19)
    time_interleaved([run.callable], Timing(rounds=4, calls=5))
finally:
    for s in spinners:
        s.kill()
        s.wait()
"""


@pytest.mark.extensive
def test_timing_refuses_a_figure_its_calls_waited_for_a_cpu_through():
    # At nice 19 beside nice-0 spinners on the cores the completions
    # interrupt, the timing thread waits for a CPU every call.
    starved = subprocess.run(
        [sys.executable, "-c", STARVE], capture_output=True, text=True
    )
    assert starved.returncode != 0
    assert re.search(r"waited \d+ us for a CPU", starved.stderr), starved.stderr


@pytest.mark.extensive
def test_a_step_costs_alike_however_long_the_run():
    # A host core woken from deep idle by a long run's completion, and not
    # by a short one's, would price a step above a short run's.
    E = 2048
    weights = [np.zeros((E, E), bfloat16) for _ in range(3)]
    recording = FeedForward(*weights).record(x=(1, E))
    gemv = next(s.op for s in recording.steps if isinstance(s.op, GEMV))
    runs = [Standalone(f"long{k}", [gemv] * k) for k in (1, 6, 12)]
    one, six, twelve = (
        t.median_us
        for t in time_interleaved(
            [r.callable for r in runs], Timing(rounds=4, calls=20)
        )
    )
    short, long = (six - one) / 5, (twelve - six) / 6
    assert abs(long - short) < 0.05 * short, (short, long)
