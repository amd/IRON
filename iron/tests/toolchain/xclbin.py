# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The other image: operators and separate-dispatch graphs build to xclbins.

The full ELF is NPU2's image; the xclbin is NPU1's, and what a graph
compiled at ``each_step`` boundaries chains one operator at a time. This
gate runs aiecc's xclbin pipeline (kernels with Peano, the PDI, then
``xclbinutil`` packaging) on each path the model lowers that way:

* a graph compiled at ``each_step`` boundaries, one xclbin per unique
  operator linked onto the previous one (``--xclbin-input``), on both
  device widths, with no runtime made until the first call;
* flm/gemm's two compiles, the configuration's xclbin at the reference
  shape and this shape's instruction stream;
* the shipped flm image's instruction stream against its pins (the xclbin
  itself is downloaded, not built, and is tried separately);
* one plain declared operator's ``compile()`` on NPU1.

Needs Peano and ``xclbinutil`` on the PATH (mlir-aie vendors a Boost-free
one under ``tools/hrx-xclbinutil``); no device.
"""

import urllib.error
from pathlib import Path

import aie.utils as aie_utils
import pytest

import iron
from iron.tests.toolchain.tools import DEVICES, requires, swiglu_decode

pytestmark = requires("xclbinutil", "peano")


def test_a_graph_compiles_to_one_xclbin_per_operator_chained(device):
    fn, E = swiglu_decode()
    net = fn.compile(
        device,
        boundaries=iron.each_step,
        image=iron.XCLBIN,
        x=(1, E),
    )
    assert net.plan.image == "xclbin" and net.plan.dispatch == "separate"
    assert net.image is not None
    assert Path(net.image).suffix == ".xclbin" and Path(net.image).stat().st_size > 0
    assert net._callable is None, "the runtime is made on first call, not at compile"
    seq = net.sequence
    dispatch = seq._image
    assert dispatch is not None
    ops = list(seq.unique_operators())
    assert len(ops) == 5 and len(seq.runlist) == 5
    # Five operators, four designs: the gate and up projections share one,
    # so they link one kernel instance and run one instruction stream.
    kernels = {dispatch.op_kernel_name_map[id(op)] for op in ops}
    assert len(kernels) == 4, kernels
    gate, up = ops[0], ops[1]
    assert type(gate).__name__ == type(up).__name__ == "GEMV"
    assert dispatch.op_insts_path_map[id(gate)] == dispatch.op_insts_path_map[id(up)]
    for op in ops:
        assert Path(dispatch.op_xclbin_path_map[id(op)]).stat().st_size > 0
        assert Path(dispatch.op_insts_path_map[id(op)]).stat().st_size > 0
    # The last link carries every instance: it is the largest of the chain,
    # and it is the image compile() handed back.
    sizes = [Path(dispatch.op_xclbin_path_map[id(op)]).stat().st_size for op in ops]
    assert Path(dispatch.combined_xclbin_path).stat().st_size == max(sizes)
    assert Path(net.image) == Path(dispatch.combined_xclbin_path)


def test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions(npu2):
    import iron.exports.flm.gemm.op as flm

    op = flm.GEMM(M=256, K=512, N=512)
    op.compile()
    artifacts = op.artifacts
    assert artifacts.image.stat().st_size > 0
    assert artifacts.insts is not None and artifacts.insts.stat().st_size > 0
    # The configuration's image is its own entry, named for the configuration;
    # the stream is this shape's, in another.
    (design,) = artifacts.designs
    assert design.name == op.config_name
    assert design.entry.directory != artifacts.entry.directory
    # The shape's own compile is instructions-only: its entry holds the
    # stream and nothing else: no second xclbin, no second kernel build.
    own = artifacts.entry
    assert own.xclbin is None and own.elf is None and own.objects == ()
    assert own.insts is not None
    # The configuration's entry is where the image and the kernels are.
    assert design.entry.xclbin == artifacts.image and design.entry.objects
    # Both entries are the cache's, which owns every path a build produces.
    from aie.utils.compile import NPU_CACHE_HOME

    for entry in (own, design.entry):
        assert entry.directory.is_relative_to(NPU_CACHE_HOME)


def _shipped(**kwargs):
    from iron.exports.flm.gemm.shipped import Shipped

    return Shipped(**kwargs)


def test_shipped_builds_its_instructions_for_the_external_image(npu2):
    op = _shipped(
        M=256,
        K=1024,
        N=1152,
        epilogue="gelu",
        clamp=(-2.0, 2.0),
    )
    op.compile()
    insts = op.artifacts.insts
    assert insts is not None and insts.stat().st_size > 0


def test_shipped_fetches_its_image(npu2):
    op = _shipped(M=256, K=1024, N=1152)
    try:
        op.compile()
    except (urllib.error.URLError, OSError) as e:  # no network here
        pytest.skip(f"the prebuilt xclbin could not be fetched: {e}")
    image = Path(op.artifacts.image)
    assert image.exists() and image.stat().st_size > 0


def test_a_declared_operator_compiles_to_an_xclbin_on_npu1():
    from iron.operators.gemv.op import GEMV

    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(DEVICES["npu1"]())
    try:
        op = GEMV(M=512, K=1024)
        op.compile()
        assert op.artifacts.image.stat().st_size > 0
        insts = op.artifacts.insts
        assert insts is not None and insts.stat().st_size > 0
    finally:
        aie_utils.set_current_device(previous)
