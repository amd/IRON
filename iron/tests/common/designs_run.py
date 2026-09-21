# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every overlay's design() and every operator's sequence execute, device-free.

The upstream API is stubbed to no-ops, so what runs is IRON's own code: the
fifo and worker construction in each ``design(target)``, the binding of
every stream and resident (the build refuses an unbound one), the preamble
writing every resident, and the sequence issuing its transfers. What it
cannot check is that the calls are what upstream accepts; that is the
toolchain's job.

With the real mlir-aie package installed the probe is skipped: its fakes
would have to stand in for the runtime the package refuses to run outside
a placed program, and ``iron/tests/toolchain/lowering.py`` already runs
the same case table through the real one, to an instruction stream.
"""

import importlib
import importlib.util
from pathlib import Path

import pytest

pytestmark = pytest.mark.skipif(
    importlib.util.find_spec("aie._mlir_libs") is not None,
    reason="the real mlir-aie package is installed; iron/tests/toolchain covers these cases",
)

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
    """Holds the sequence; ProbeProgram runs it, as resolve_program does upstream."""

    def __init__(self, fn, args):
        self._fifos = set()
        self.fn, self.n_args = fn, len(args)


class ProbeProgram:
    def __init__(self, dev, rt, workers=None):
        self.rt = rt

    def resolve_program(self):
        self.rt.fn(*[f"arg{i}" for i in range(self.rt.n_args)])
        return "module"


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
    monkeypatch.setattr(aie.iron, "Program", ProbeProgram, raising=False)
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


def test_llama_decode_operators_build_with_their_values(device):
    """Every operator the decode graph traced builds: the batched GEMVs and
    transpose, the strided copies with a bound offset, the dynamic softmax."""
    import sys

    from iron.common.declare import Incompatible, Untunable
    from iron.tests.common.graph import _Config

    if device.resolve().name != "npu2":
        pytest.skip("the decode graph is tuned for the 8-column array")
    sys.path.insert(0, "iron/applications/llama_3.2_1b")
    from decode_graph import DecodeGraph

    cfg = _Config()
    traced = DecodeGraph(cfg, 256).trace(cfg)
    bound = {id(op) for op, _, _ in traced.bindings}
    built = 0
    for op in traced.operators:
        build_design(device, Path("/kernels"), op)
        built += 1
        if id(op) in bound:
            # The build works on a tuned copy; the binding must survive it, or
            # the sequence silently drops the value (build_design would have
            # raised on an offset with no parameter otherwise).
            tuned = op.tuned(device)
            assert list(tuned.values) + list(tuned.ov.values), op
    assert built == len(traced.operators)


@pytest.mark.parametrize(
    "M,K,N",
    [(512, 1024, 1024), (512, 1024, 10240), (256, 512, 512)],
    ids=["unsplit", "c_split", "tn128"],
)
def test_flm_gemm_design_and_sequence_run(device, monkeypatch, M, K, N):
    """The configuration's array and the shape's sequence, on both paths."""
    import iron.operators.flm.gemm.op as flm

    if device.resolve().name != "npu2":
        pytest.skip("flm/gemm's L1 budget is faked for the aie2p B layout")

    class _Arch:
        AIE2p = "aie2p"
        AIE2 = "aie2"

    monkeypatch.setattr(flm, "AIEArch", _Arch)
    monkeypatch.setattr(flm, "get_target_model", lambda d: _TargetModel(device.cols))
    monkeypatch.setattr(
        flm.dsg, "get_target_model", lambda d: _TargetModel(device.cols)
    )
    op = flm.GEMM(M=M, K=K, N=N)
    build_design(device, Path("/kernels"), op)
    # The configuration-only module the xclbin is built from, at the
    # reference shape, builds too.
    tuned = op.tuned(device)
    rM, rK, rN = tuned._reference_shape
    import dataclasses

    reference = dataclasses.replace(
        tuned,
        M=rM,
        K=rK,
        N=rN,
        epilogue=flm.Epilogue.NONE,
        clamp=None,
        packed_bytes=None,
    )
    build_design(device, Path("/kernels"), reference)
