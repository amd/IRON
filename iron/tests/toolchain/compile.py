# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``GraphFunction.compile`` on a host without an NPU produces the image.

The packaging surface end to end: ``compile(dev, boundaries=, image=)``
derives the dispatch by the rules in ``iron.common.packaging``, traces,
builds the sequence and links the image, and the runtime that would load
it is not made until the first call. So a build host with the toolchain
and no device can compile ahead of time and hand the image on, which is
what this checks for both images: the fused ELF on npu2 and the chained
xclbins at ``each_step`` boundaries on npu1.
"""

from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2, from_name  # noqa: E402

import iron  # noqa: E402
from iron.common.context import AIEContext  # noqa: E402
from iron.tests.toolchain.full_elf import PEANO  # noqa: E402
from iron.tests.toolchain.full_elf import AIEBU  # noqa: E402
from iron.tests.toolchain.xclbin import XCLBINUTIL  # noqa: E402

pytestmark = pytest.mark.skipif(
    PEANO is None or not PEANO.exists(), reason="no Peano (llvm-aie) installed"
)


@pytest.fixture(autouse=True)
def restore_device():
    previous = aie_utils.get_current_device()
    yield
    aie_utils.set_current_device(previous)


def _swiglu_decode():
    from iron.operators.swiglu_decode.op import swiglu_decode

    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    E, H = 2048, 8192
    return swiglu_decode(z(H, E), z(H, E), z(E, H)), E


@pytest.mark.skipif(AIEBU is None, reason="no aiebu-asm on the PATH")
def test_compile_for_npu2_links_the_fused_elf_without_a_runtime(tmp_path):
    fn, E = _swiglu_decode()
    net = fn.compile(
        NPU2(), image=iron.ELF, context=AIEContext(build_dir=str(tmp_path)), x=(1, E)
    )
    assert net.plan.image == "elf" and net.plan.dispatch == "fused"
    assert Path(net.image).suffix == ".elf" and Path(net.image).stat().st_size > 0
    assert net._callable is None, "the runtime is made on first call, not at compile"


@pytest.mark.skipif(XCLBINUTIL is None, reason="no xclbinutil on the PATH")
def test_compile_for_npu1_at_each_step_links_the_chained_xclbins(tmp_path):
    fn, E = _swiglu_decode()
    net = fn.compile(
        from_name("npu1", n_cols=4),
        boundaries=iron.each_step,
        image=iron.XCLBIN,
        context=AIEContext(build_dir=str(tmp_path)),
        x=(1, E),
    )
    assert net.plan.image == "xclbin" and net.plan.dispatch == "separate"
    assert Path(net.image).suffix == ".xclbin" and Path(net.image).stat().st_size > 0
    assert net._callable is None
    # Four designs for five steps: the chain has four links.
    assert len(list(tmp_path.glob("f*_op*.xclbin"))) == 4


@pytest.mark.skipif(XCLBINUTIL is None, reason="no xclbinutil on the PATH")
def test_compile_at_chunks_links_one_fused_kernel_per_chunk(tmp_path):
    """boundaries=chunks(2) on five steps: three kernels (2, 2, 1 steps) in one
    chained xclbin, each a fused sub-sequence with its switches expanded, run
    over the three arenas. Spike S1's construction; the run is its question."""
    fn, E = _swiglu_decode()
    net = fn.compile(
        NPU2(),
        boundaries=iron.chunks(2),
        context=AIEContext(build_dir=str(tmp_path)),
        x=(1, E),
    )
    dispatch = net.sequence._dispatch
    assert net.plan.image == "xclbin" and dispatch.name == "chunked"
    assert [n for *_, n in dispatch.chunks] == [2, 2, 1]
    for label, xclbin_path, insts_path, _ in dispatch.chunks:
        assert Path(xclbin_path).stat().st_size > 0
        assert Path(insts_path).stat().st_size > 0
        assert label in Path(xclbin_path).name
    assert Path(net.image) == dispatch.chunks[-1][1]
    # A chunk of two GEMV steps carries two configurations' writes: its stream
    # is much larger than a per-operator one (the separate dispatch's ~3 KB).
    assert Path(dispatch.chunks[0][2]).stat().st_size > 20_000


@pytest.mark.skipif(XCLBINUTIL is None, reason="no xclbinutil on the PATH")
def test_compile_for_xclbin_alone_is_one_fused_kernel(tmp_path):
    fn, E = _swiglu_decode()
    net = fn.compile(
        NPU2(), image=iron.XCLBIN, context=AIEContext(build_dir=str(tmp_path)), x=(1, E)
    )
    dispatch = net.sequence._dispatch
    assert dispatch.name == "chunked" and [n for *_, n in dispatch.chunks] == [5]
    assert Path(net.image).stat().st_size > 0
