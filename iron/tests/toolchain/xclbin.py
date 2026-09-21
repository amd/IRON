# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The other image: operators and separate-dispatch graphs build to xclbins.

The full ELF is NPU2's image; the xclbin is NPU1's, and what a graph
compiled at ``each_step`` boundaries chains one operator at a time. This
gate runs aiecc's xclbin pipeline (kernels with Peano, the PDI, then
``xclbinutil`` packaging) on each path the model lowers that way:

* a graph's separate dispatch, one xclbin per unique operator linked onto
  the previous one (``--xclbin-input``), on both device widths;
* flm/gemm's two compiles, the configuration's xclbin at the reference
  shape and this shape's instruction stream;
* mm_prebuilt's instruction stream against its foreign overlay (the xclbin
  itself is downloaded, not built, and is tried separately);
* one plain declared operator's ``compile()`` on NPU1.

Needs Peano and ``xclbinutil`` on the PATH (mlir-aie vendors a Boost-free
one under ``tools/hrx-xclbinutil``); no device.
"""

import shutil
import urllib.error
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2, from_name  # noqa: E402

from iron.common.context import AIEContext  # noqa: E402
from iron.tests.toolchain.full_elf import PEANO  # noqa: E402

XCLBINUTIL = shutil.which("xclbinutil")

pytestmark = [
    pytest.mark.skipif(XCLBINUTIL is None, reason="no xclbinutil on the PATH"),
    pytest.mark.skipif(
        PEANO is None or not PEANO.exists(), reason="no Peano (llvm-aie) installed"
    ),
]

DEVICES = {"npu2": lambda: NPU2(), "npu1": lambda: from_name("npu1", n_cols=4)}


@pytest.fixture(params=sorted(DEVICES))
def device(request):
    previous = aie_utils.get_current_device()
    dev = DEVICES[request.param]()
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


@pytest.fixture
def npu2():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)


def _swiglu_decode():
    from iron.operators.swiglu_decode.op import swiglu_decode

    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    E, H = 2048, 8192
    return swiglu_decode(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))


def test_a_graph_chains_one_xclbin_per_operator(device, tmp_path):
    traced = _swiglu_decode()
    ctx = AIEContext(build_dir=str(tmp_path / "build"))
    seq = traced.sequence("swiglu_decode_sep", dispatch="separate", context=ctx)
    seq.compile()
    dispatch = seq._dispatch
    dispatch.link_xclbins(seq)
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
    # The last link carries every instance: it is the largest of the chain.
    sizes = [Path(dispatch.op_xclbin_path_map[id(op)]).stat().st_size for op in ops]
    assert Path(dispatch.combined_xclbin_path).stat().st_size == max(sizes)


def test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions(
    npu2, tmp_path
):
    import iron.operators.flm.gemm.op as flm

    op = flm.GEMM(M=256, K=512, N=512, context=AIEContext(build_dir=str(tmp_path)))
    op.compile()
    assert Path(op._xclbin_path).name == f"{op.config_name}.xclbin"
    assert Path(op._insts_path).name == f"{op.name}.bin"
    assert Path(op._xclbin_path).stat().st_size > 0
    assert Path(op._insts_path).stat().st_size > 0


def test_mm_prebuilt_builds_its_instructions_for_the_foreign_image(npu2, tmp_path):
    from iron.operators.flm.mm_prebuilt.op import MMPrebuilt

    op = MMPrebuilt(
        M=256,
        K=1024,
        N=1152,
        epilogue="gelu",
        clamp=(-2.0, 2.0),
        context=AIEContext(build_dir=str(tmp_path)),
    )
    op.link_xclbin()
    assert Path(op._insts_path).stat().st_size > 0


def test_mm_prebuilt_fetches_its_image(npu2, tmp_path):
    from iron.operators.flm.mm_prebuilt.op import MMPrebuilt

    op = MMPrebuilt(M=256, K=1024, N=1152, context=AIEContext(build_dir=str(tmp_path)))
    try:
        op.compile()
    except (urllib.error.URLError, OSError) as e:  # no network here
        pytest.skip(f"the prebuilt xclbin could not be fetched: {e}")
    image = Path(op.xclbin_artifact.filename)
    assert image.exists() and image.stat().st_size > 0


def test_a_declared_operator_compiles_to_an_xclbin_on_npu1(tmp_path):
    from iron.operators.gemv.op import GEMV

    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(DEVICES["npu1"]())
    try:
        op = GEMV(M=512, K=1024, context=AIEContext(build_dir=str(tmp_path)))
        op.compile()
        assert Path(op._xclbin_path).stat().st_size > 0
        assert Path(op._insts_path).stat().st_size > 0
    finally:
        aie_utils.set_current_device(previous)
