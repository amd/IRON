#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The root conftest.py's pytest_collection_modifyitems must not resolve a
device unless some collected test actually restricts itself to specific
devices via @pytest.mark.supported_devices.

Before this fix it called aie_utils.DefaultNPURuntime.device() unconditionally
at collection time, so a plain `pytest` in this tree opened the NPU
regardless of which test was selected -- contending with anything else
using the (single-tenant) device, and failing outright with no NPU present.

Loads the real root conftest.py by path (rather than depending on pytest's
own conftest-loading, which would defeat the point of testing it in
isolation) and calls its hook directly with fake items and a stubbed
aie_utils.DefaultNPURuntime that raises if .device() is ever called.
"""

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

_ROOT_CONFTEST = Path(__file__).resolve().parents[3] / "conftest.py"


def _load_root_conftest():
    spec = importlib.util.spec_from_file_location("_root_conftest_under_test", _ROOT_CONFTEST)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class _FakeMarker:
    def __init__(self, *args):
        self.args = args


class _FakeItem:
    def __init__(self, marker=None):
        self._marker = marker
        self.markers_added = []

    def get_closest_marker(self, name):
        assert name == "supported_devices"
        return self._marker

    def add_marker(self, marker):
        self.markers_added.append(marker)


class _DeviceCalledError(Exception):
    pass


def _stub_runtime_that_forbids_device_calls(root_conftest, monkeypatch):
    def _raise():
        raise _DeviceCalledError(
            "DefaultNPURuntime.device() was called with no marked test collected"
        )

    monkeypatch.setattr(
        root_conftest.aie_utils,
        "DefaultNPURuntime",
        SimpleNamespace(device=_raise),
    )


def test_no_device_probe_when_nothing_is_device_restricted(monkeypatch):
    root_conftest = _load_root_conftest()
    _stub_runtime_that_forbids_device_calls(root_conftest, monkeypatch)

    items = [_FakeItem(), _FakeItem(), _FakeItem()]
    # Must not raise _DeviceCalledError.
    root_conftest.pytest_collection_modifyitems(config=None, items=items)
    assert all(item.markers_added == [] for item in items)


def test_device_probed_and_marker_logic_preserved_when_a_test_is_restricted(monkeypatch):
    root_conftest = _load_root_conftest()

    class _FakeDevice:
        def resolve(self):
            return SimpleNamespace(name="npu2")

    monkeypatch.setattr(
        root_conftest.aie_utils,
        "DefaultNPURuntime",
        SimpleNamespace(device=lambda: _FakeDevice()),
    )

    unrestricted = _FakeItem()
    matches_device = _FakeItem(_FakeMarker("npu1", "npu2"))
    excludes_device = _FakeItem(_FakeMarker("npu1"))

    root_conftest.pytest_collection_modifyitems(
        config=None, items=[unrestricted, matches_device, excludes_device]
    )

    assert unrestricted.markers_added == []
    assert matches_device.markers_added == []
    assert len(excludes_device.markers_added) == 1
    assert excludes_device.markers_added[0].name == "skip"
