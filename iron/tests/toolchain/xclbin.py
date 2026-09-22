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
* the shipped flm image's instruction stream against its foreign overlay (the xclbin
  itself is downloaded, not built, and is tried separately);
* one plain declared operator's ``compile()`` on NPU1.

Needs Peano and ``xclbinutil`` on the PATH (mlir-aie vendors a Boost-free
one under ``tools/hrx-xclbinutil``); no device.
"""

import urllib.error
from pathlib import Path

import pytest
import aie.utils as aie_utils

import iron
from iron.common.context import AIEContext
from iron.tests.toolchain.tools import DEVICES, requires, swiglu_decode

pytestmark = requires("xclbinutil", "peano")


def test_a_graph_compiles_to_one_xclbin_per_operator_chained(device, tmp_path):
    fn, E = swiglu_decode()
    net = fn.compile(
        device,
        boundaries=iron.each_step,
        image=iron.XCLBIN,
        context=AIEContext(build_dir=str(tmp_path)),
        x=(1, E),
    )
    assert net.plan.image == "xclbin" and net.plan.dispatch == "separate"
    assert Path(net.image).suffix == ".xclbin" and Path(net.image).stat().st_size > 0
    assert net._callable is None, "the runtime is made on first call, not at compile"
    seq = net.sequence
    dispatch = seq._image
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


def test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions(
    npu2, tmp_path
):
    import iron.operators.flm.gemm.op as flm

    op = flm.GEMM(M=256, K=512, N=512, context=AIEContext(build_dir=str(tmp_path)))
    op.compile()
    artifacts = op.artifacts
    assert artifacts.image.stat().st_size > 0
    assert artifacts.insts.stat().st_size > 0
    # The configuration's image is its own entry, named for the configuration;
    # the stream is this shape's, in another.
    (design,) = artifacts.designs
    assert design.name == op.config_name
    assert design.entry.directory != artifacts.entry.directory
    # The shape's own compile is instructions-only: no second xclbin, no
    # second kernel build.
    assert not (tmp_path / f"{op.name}.xclbin").exists()
    assert sorted(p.name for p in tmp_path.glob("*.xclbin")) == [
        f"{op.config_name}.xclbin"
    ]


def _shipped(**kwargs):
    from iron.operators.flm.gemm.op import GEMM
    from iron.operators.flm.gemm.shipped import Shipped

    return GEMM(Shipped(), **kwargs)


def test_shipped_builds_its_instructions_for_the_foreign_image(npu2, tmp_path):
    op = _shipped(
        M=256,
        K=1024,
        N=1152,
        epilogue="gelu",
        clamp=(-2.0, 2.0),
        context=AIEContext(build_dir=str(tmp_path)),
    )
    op.compile()
    assert op.artifacts.insts.stat().st_size > 0


def test_shipped_fetches_its_image(npu2, tmp_path):
    op = _shipped(M=256, K=1024, N=1152, context=AIEContext(build_dir=str(tmp_path)))
    try:
        op.compile()
    except (urllib.error.URLError, OSError) as e:  # no network here
        pytest.skip(f"the prebuilt xclbin could not be fetched: {e}")
    image = Path(op.artifacts.image)
    assert image.exists() and image.stat().st_size > 0


def test_a_declared_operator_compiles_to_an_xclbin_on_npu1(tmp_path):
    from iron.operators.gemv.op import GEMV

    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(DEVICES["npu1"]())
    try:
        op = GEMV(M=512, K=1024, context=AIEContext(build_dir=str(tmp_path)))
        op.compile()
        assert op.artifacts.image.stat().st_size > 0
        assert op.artifacts.insts.stat().st_size > 0
    finally:
        aie_utils.set_current_device(previous)
