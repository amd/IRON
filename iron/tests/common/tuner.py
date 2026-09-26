# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The tuner's choice of folds and packaging, device-free, from a made-up table.

What each packaging charges at a boundary is the table's (a calibration per
mode); what the tuner does with it is checked here: a mode the device does
not run or the table does not calibrate is never chosen, a fold is taken
where it lowers the modelled time, and a folded design is priced at its
unfolded twin.
"""

import numpy as np
import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name

import iron
from iron.common.graph.fold import Fold, candidates
from iron.common.graph.narrowing import (
    Calibration,
    CostTable,
    StepCost,
    cost_key,
    model_us,
    variants,
)
from iron.common.graph.tuner import Tuner
from iron.common.image.packaging import EACH_STEP, FUSED, modes
from iron.operators.gemv.op import GEMV
from iron.operators.repeat import Repeat

G, REP, L, D, COLS = 2, 4, 128, 64, 2
H = G * REP


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    dev = from_name("npu2", n_cols=8)
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


def _scores():
    keys = iron.state((G, L * D), name="keys")

    @iron.graph
    def scores(q):
        k_all = Repeat(keys, repeat=REP, transfer_size=D)
        return GEMV(
            k_all.reshape(H, L, D),
            q,
            num_aie_columns=COLS,
            tile_size_input=4,
            tile_size_output=L // COLS,
        )

    return scores.trace(q=(H, D))


def _table(path, traced, dev, *, t_step, load, elf=None, each_step=None):
    """Every width of every design at ``t_step[class]`` and ``load[class]``,
    and a calibration per mode given as (dispatch, reset, base)."""
    table = CostTable(path)
    elf_d, elf_r, elf_b = elf or (0.0, 0.0, 0.0)
    for step in traced.steps:
        name = type(step.op).__name__
        for v in variants(step.op, dev):
            alone = elf_d + elf_r + elf_b + load[name]
            table.record_step(
                v.key, StepCost(t_step[name], alone, True, "turbo", 1, 1, "-")
            )
    for mode, figures in ((FUSED, elf), (EACH_STEP, each_step)):
        if figures is not None:
            d, r, b = figures
            table.record_calibration(
                ("x", "y"), Calibration(d, r, b, b, "turbo", 1, 1, "-", mode.name)
            )
    return table


def test_modes_follow_the_device():
    t = _scores()
    assert modes("npu2", t) == [FUSED, EACH_STEP]
    assert modes("npu1", t) == [EACH_STEP]


def test_a_fold_is_taken_when_it_saves_its_step(tmp_path, npu2):
    t = _scores()
    table = _table(
        tmp_path / "t.json",
        t,
        npu2,
        t_step=dict(Repeat=500.0, GEMV=100.0),
        load=dict(Repeat=20.0, GEMV=40.0),
        elf=(50.0, 30.0, 30.0),
    )
    choice = Tuner(table).tune(t, npu2, [FUSED, EACH_STEP])
    assert choice.mode == FUSED  # the only calibrated one
    (fold,) = choice.folds
    assert isinstance(fold, Fold) and fold.removed == 0
    # The folded GEMV is priced at the GEMV it was: one step at 100 us,
    # one configure, the reset, the dispatch.
    assert choice.predicted_us == pytest.approx(50 + 100 + 30 + 40 + 30)
    assert len(choice.estimated) == len(variants(t.steps[1].op, npu2))
    unfolded = Tuner(table, fold=False).tune(t, npu2, [FUSED])
    assert unfolded.folds == ()
    assert unfolded.predicted_us > choice.predicted_us


def test_each_mode_charges_its_own_boundaries(tmp_path, npu2):
    t = _scores()
    keys = [cost_key(s.op) for s in t.steps]
    table = _table(
        tmp_path / "t.json",
        t,
        npu2,
        t_step=dict(Repeat=5.0, GEMV=10.0),
        load=dict(Repeat=20.0, GEMV=40.0),
        elf=(50.0, 30.0, 30.0),
        each_step=(200.0, 0.0, 70.0),
    )
    fused, n_fused = model_us(table, keys, mode=FUSED)
    assert (fused, n_fused) == (pytest.approx(50 + 5 + 10 + 2 * 30 + 20 + 40), 2)
    each, n_each = model_us(table, keys, mode=EACH_STEP)
    assert (each, n_each) == (pytest.approx(2 * 200 + 5 + 10 + 2 * 70), 2)
    with pytest.raises(ValueError, match="no packs"):
        model_us(table, keys, [keys], mode=EACH_STEP)
    choice = Tuner(table).tune(t, npu2, [FUSED, EACH_STEP])
    assert choice.mode == FUSED
    # Where the device offers only a dispatch per step, the fold removes one.
    only = Tuner(table).tune(t, npu2, [EACH_STEP])
    assert only.mode == EACH_STEP and len(only.folds) == 1
    assert only.predicted_us == pytest.approx(200 + 10 + 70)


def test_an_uncalibrated_device_is_an_error(tmp_path, npu2):
    t = _scores()
    table = _table(
        tmp_path / "t.json",
        t,
        npu2,
        t_step=dict(Repeat=5.0, GEMV=10.0),
        load=dict(Repeat=20.0, GEMV=40.0),
        elf=(50.0, 30.0, 30.0),
    )
    with pytest.raises(ValueError, match="each_step.*is calibrated"):
        Tuner(table).tune(t, npu2, [EACH_STEP])


def test_the_estimate_is_the_twin_width_by_width(tmp_path, npu2):
    t = _scores()
    table = _table(
        tmp_path / "t.json",
        t,
        npu2,
        t_step=dict(Repeat=500.0, GEMV=100.0),
        load=dict(Repeat=20.0, GEMV=40.0),
        elf=(50.0, 30.0, 30.0),
    )
    (fold,) = [c for c in candidates(t, npu2) if isinstance(c, Fold)]
    choice = Tuner(table).tune(t, npu2, [FUSED])
    twin = variants(t.steps[1].op, npu2)
    assert len(choice.estimated) == len(twin)
    assert np.all([k not in {v.key for v in twin} for k in choice.estimated])
