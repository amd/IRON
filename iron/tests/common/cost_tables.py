# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A checked-in cost table holds every design its model's tuner prices, and
nothing else: what ``measure_graph`` would run for it, found without a device.
"""

from pathlib import Path

import numpy as np

from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Designs
from iron.lm import SEED, Sampler
from iron.lm.llama3 import tune as llama_tune
from iron.lm.tune import CALIBRATION_PAIRS, calls
from iron.tests.common.llama_model import llama_1b


def test_llamas_table_holds_every_design_it_tunes(npu2):
    sample = Sampler(0.7, 50, np.random.default_rng(SEED))
    designs = Designs.of(calls(llama_1b(), sample, position=256, token=0), npu2)
    table = CostTable(Path(llama_tune.__file__).with_name("costs_npu2.json"))
    stale = designs.stale(table)
    missing = designs.missing(table, CALIBRATION_PAIRS)
    settings = {v.key: (vs[0], v) for vs in designs.settings.values() for v in vs}
    unmeasured = []
    for key in missing:
        if key not in settings:
            unmeasured.append(f"  calibration {key}")
            continue
        default, setting = settings[key]
        start = dict(default.tunables)
        moved = {n: x for n, x in setting.tunables if start[n] != x}
        unmeasured.append(
            f"  {key}: {type(setting.op).__name__} at {start}"
            + (f", moved to {moved}" if moved else ", its default")
        )
    assert not stale and not missing, (
        f"{table.path} is out of date; run `python -m iron.lm.llama3.tune` on "
        f"an idle NPU2. {len(missing)} to measure:\n"
        + "\n".join(unmeasured)
        + f"\n{len(stale)} the graph no longer has: {stale}"
    )
