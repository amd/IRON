# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A device's cost model beyond its steps' times (``iron.tune.costmodel``):
its prior, its fit to samples, and its file."""

import pytest

from iron.tune.costmodel import PRIOR, CostModel


def test_a_model_without_samples_predicts_by_its_prior():
    features = {"switches": 10, "switch_cores": 40, "packed_steps": 5}
    assert CostModel().predict(features) == pytest.approx(
        10 * PRIOR["switches"] + 40 * PRIOR["switch_cores"]
    )


def test_samples_pull_the_terms_from_the_prior_to_what_was_measured():
    model = CostModel()
    for n in range(1, 30):
        change = {"switches": -n, "switch_cores": -8 * n, "packed_steps": 3 * n}
        model.add(change, -n * 60.0 - 8 * n * 4.0 + 3 * n * 2.0)
    assert model.terms["switches"] < PRIOR["switches"] * 2
    predicted = model.predict(
        {"switches": -10, "switch_cores": -80, "packed_steps": 30}
    )
    assert predicted == pytest.approx(-10 * 60.0 - 80 * 4.0 + 30 * 2.0, rel=0.1)


def test_a_model_round_trips_through_its_file(tmp_path):
    model = CostModel()
    model.add({"switches": -4, "switch_cores": -20, "packed_steps": 8}, -300.0)
    model.save("npu2", tmp_path)
    loaded = CostModel.load("npu2", tmp_path)
    assert loaded == model
    assert CostModel.load("npu1", tmp_path) is None


def test_a_calibrated_model_is_pulled_toward_its_measured_switch():
    model = CostModel.calibrated(40.0, 3.0)
    assert model.predict({"switches": 2, "switch_cores": 10}) == pytest.approx(110.0)
    model.add({"switches": -1, "switch_cores": -1, "packed_steps": 0}, -43.0)
    assert model.terms["switches"] == pytest.approx(40.0, rel=0.2)
