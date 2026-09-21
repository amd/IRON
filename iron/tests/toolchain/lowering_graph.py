# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the case table does not cover lowers too: graph-traced operators
with bound per-call values, flm/gemm's configuration and shapes, the
foreign mm_prebuilt sequence, and the swiglu graph functions' operators.
Same gate as ``lowering.py``: aiecc to an instruction stream, no Peano.
"""

import dataclasses
import sys
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2  # noqa: E402

from iron.tests.toolchain.lowering import AIECC, lower  # noqa: E402

pytestmark = pytest.mark.skipif(not AIECC.exists(), reason=f"no aiecc at {AIECC}")


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)


def _lower_all(traced, tmp_path):
    for i, op in enumerate(traced.operators):
        (tmp_path / str(i)).mkdir()
        lower(op, tmp_path / str(i), name=f"{i}_{type(op).__name__}")


def test_decode_graph_operators_lower_with_their_values(tmp_path):
    from iron.tests.common.graph import _Config

    sys.path.insert(0, str(Path("iron/applications/llama_3.2_1b").resolve()))
    from decode_graph import DecodeGraph

    cfg = _Config()
    traced = DecodeGraph(cfg, 256).trace(cfg)
    bound = {id(op) for op, _, _ in traced.bindings}
    assert bound, "the decode graph binds values"
    _lower_all(traced, tmp_path)


@pytest.mark.parametrize(
    "M,K,N",
    [(512, 1024, 1024), (512, 1024, 10240), (256, 512, 512)],
    ids=["unsplit", "c_split", "tn128"],
)
def test_flm_gemm_lowers_and_so_does_its_configuration_module(M, K, N, tmp_path):
    import iron.operators.flm.gemm.op as flm

    op = flm.GEMM(M=M, K=K, N=N)
    (tmp_path / "shape").mkdir()
    lower(op, tmp_path / "shape")
    tuned = op.tuned(aie_utils.get_current_device())
    rM, rK, rN = tuned._reference_shape
    reference = dataclasses.replace(
        tuned,
        M=rM,
        K=rK,
        N=rN,
        epilogue=flm.Epilogue.NONE,
        clamp=None,
        packed_bytes=None,
    )
    (tmp_path / "config").mkdir()
    lower(reference, tmp_path / "config", name=op.config_name)


def test_mm_prebuilt_foreign_sequence_lowers(tmp_path):
    from iron.operators.flm.mm_prebuilt.op import MMPrebuilt

    op = MMPrebuilt(M=256, K=1024, N=1152, epilogue="gelu", clamp=(-2.0, 2.0))
    lower(op, tmp_path)


def test_instructions_compile_alone_against_a_foreign_image(tmp_path):
    """The §11 instructions-only compile: mm_prebuilt's image is downloaded,
    so its link step lowers only the sequence. No kernel, no Peano, and the
    second request is a cache hit."""
    from iron.common.context import AIEContext
    from iron.operators.flm.mm_prebuilt.op import MMPrebuilt

    op = MMPrebuilt(M=256, K=1024, N=1152, context=AIEContext(build_dir=str(tmp_path)))
    op.link_xclbin()
    insts = Path(op._insts_path)
    assert insts.stat().st_size > 0
    assert not list(tmp_path.glob("*.xclbin")), "an instructions-only compile built an image"
    first = insts.stat().st_mtime_ns
    again = MMPrebuilt(M=256, K=1024, N=1152, context=AIEContext(build_dir=str(tmp_path)))
    again.link_xclbin()
    assert Path(again._insts_path).stat().st_mtime_ns == first, "the same sequence recompiled"


def test_swiglu_graphs_operators_lower(tmp_path):
    from iron.operators.swiglu_decode.op import swiglu_decode
    from iron.operators.swiglu_prefill.op import swiglu_prefill

    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    E, H = 2048, 8192
    (tmp_path / "decode").mkdir()
    _lower_all(
        swiglu_decode(z(H, E), z(H, E), z(E, H)).trace(x=(1, E)), tmp_path / "decode"
    )
    (tmp_path / "prefill").mkdir()
    _lower_all(
        swiglu_prefill(z(E, H), z(E, H), z(H, E)).trace(x=(256, E)),
        tmp_path / "prefill",
    )
