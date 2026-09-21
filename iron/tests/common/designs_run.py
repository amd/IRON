# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every overlay's design() and every operator's sequence execute, device-free.

The upstream API is stubbed to no-ops, so what runs is IRON's own code: the
fifo and worker construction in each ``design(target)``, the binding of
every stream and resident (the build refuses an unbound one), the preamble
writing every resident, and the sequence issuing its transfers. What it
cannot check is that the calls are what upstream accepts; that is the
toolchain's job.
"""

import importlib
from pathlib import Path

import pytest

from iron.common.build import build_design
from iron.tests.common.cases import CASES


class _Resolved:
    def __init__(self, name):
        self.name = name


class Dev:
    def __init__(self, name, cols, arch):
        self._name, self.cols, self.arch = name, cols, arch

    def resolve(self):
        return _Resolved(self._name)


class _TargetModel:
    def __init__(self, cols):
        self._cols = cols

    def rows(self):
        return 6

    def columns(self):
        return self._cols

    def get_num_mem_tile_rows(self):
        return 1

    def get_local_memory_size(self):
        return 65536

    def get_num_bds(self, col, row):
        return 16


class ProbeRuntime:
    """Calls the sequence at construction, as resolve_program would later."""

    def __init__(self, fn, args):
        self._fifos = set()
        fn(*[f"arg{i}" for i in range(len(args))])


DEVICES = {
    "npu2": (Dev("npu2", 8, "aie2p"), 16),
    "npu1": (Dev("npu1", 4, "aie2"), 8),
}


@pytest.fixture(params=sorted(DEVICES))
def device(request, monkeypatch):
    import aie.iron
    import aie.dialects.aie
    import aie.utils as aie_utils
    import aie.utils.config

    import iron.common.device_utils as du
    import iron.common.operator_bases as bases
    import iron.common.utils as utils
    import iron.operators._kernels as kernels
    import iron.operators.rms_norm.op as rms

    dev, limit = DEVICES[request.param]
    monkeypatch.setattr(aie.iron, "Runtime", ProbeRuntime, raising=False)
    monkeypatch.setattr(aie_utils, "get_current_device", lambda: dev, raising=False)
    monkeypatch.setattr(du, "resolve_target_arch", lambda d: d.arch)
    monkeypatch.setattr(aie.utils.config, "root_path", lambda: "/aie", raising=False)
    monkeypatch.setattr(kernels, "runtime_include_dirs", lambda: [])
    for module in (utils, bases, rms):
        monkeypatch.setattr(module, "get_shim_dma_limit", lambda d, limit=limit: limit)
    monkeypatch.setattr(
        aie.dialects.aie,
        "get_target_model",
        lambda r: _TargetModel(dev.cols),
        raising=False,
    )
    monkeypatch.setattr(utils, "get_target_model", lambda r: _TargetModel(dev.cols))
    return dev


def _cases():
    for module, cls_name, kwargs_list in CASES:
        for i, kwargs in enumerate(kwargs_list):
            yield pytest.param(module, cls_name, kwargs, id=f"{cls_name}-{i}")


@pytest.mark.parametrize("module,cls_name,kwargs", list(_cases()))
def test_design_and_sequence_run(device, module, cls_name, kwargs):
    cls = getattr(importlib.import_module(f"iron.operators.{module}.op"), cls_name)
    try:
        op = cls(**kwargs)
    except ValueError as e:
        pytest.skip(f"not constructible on {device.resolve().name}: {e}")
    try:
        build_design(device, Path("/kernels"), op)
    except Exception as e:  # noqa: BLE001
        from iron.common.declare import Untunable, Incompatible

        if isinstance(e, (Untunable, Incompatible)):
            pytest.skip(f"not for {device.resolve().name}: {e}")
        raise
