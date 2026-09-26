# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the case table does not cover lowers too: graph-traced operators
with bound per-call values, flm/gemm's configuration and shapes, the
external shipped-overlay sequence, and the swiglu graph functions' operators.
Same gate as ``lowering.py``: aiecc to an instruction stream, no Peano.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils

from iron.tests.toolchain.lowering import lower
from iron.tests.toolchain.tools import requires, swiglu_decode

pytestmark = [*requires("aiecc"), pytest.mark.usefixtures("npu2")]


def _lower_all(traced, tmp_path):
    for i, op in enumerate(traced.operators):
        (tmp_path / str(i)).mkdir()
        lower(op, tmp_path / str(i), name=f"{i}_{type(op).__name__}")


def test_decode_graph_operators_lower_with_their_values(tmp_path):
    from iron.tests.common.llama_model import Config as _Config

    from iron.applications.llama_3_2_1b.graphs import LlamaGraph

    cfg = _Config()
    traced = LlamaGraph(cfg, 256).trace(cfg, 1)
    bound = {id(b.op) for b in traced.bindings}
    assert bound, "the decode graph binds values"
    _lower_all(traced, tmp_path)


def test_prefill_graph_operators_lower_with_their_value(tmp_path):
    from iron.tests.common.llama_model import Config as _Config

    from iron.applications.llama_3_2_1b.graphs import LlamaGraph

    cfg = _Config()
    L = cfg.context_length
    graph = LlamaGraph(cfg, L, num_aie_columns=4, num_of_pipelines=1, tile_m=16)
    traced = graph.trace(cfg, L)
    # The last row's copy, and the draw row and record of its token.
    assert [b.value.name for b in traced.bindings] == ["position"] * 3
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
        packed_blocks=None,
    )
    (tmp_path / "config").mkdir()
    lower(reference, tmp_path / "config", name=op.config_name)


def _shipped(**kwargs):
    from iron.operators.flm.gemm.op import GEMM
    from iron.operators.flm.gemm.shipped import Shipped

    return GEMM(Shipped(), **kwargs)


def test_shipped_external_sequence_lowers(tmp_path):
    lower(_shipped(M=256, K=1024, N=1152, epilogue="gelu", clamp=(-2.0, 2.0)), tmp_path)


def test_instructions_compile_alone_against_an_external_image():
    """The §11 instructions-only compile: the shipped image is downloaded,
    so its link step lowers only the sequence. No kernel, no Peano, and the
    second request is a cache hit."""

    op = _shipped(M=256, K=1024, N=1152)
    op.compile()
    insts = op.artifacts.insts
    assert insts.stat().st_size > 0
    # The image is the download, so nothing was built beside the stream.
    assert op.artifacts.entry.xclbin is None
    assert op.artifacts.image.suffix == ".xclbin"
    first = insts.stat().st_mtime_ns
    again = _shipped(M=256, K=1024, N=1152)
    again.compile()
    assert again.artifacts.insts == insts
    assert insts.stat().st_mtime_ns == first, "the same sequence recompiled"


def test_swiglu_graphs_operators_lower(tmp_path):
    from iron.operators.swiglu_prefill.op import swiglu_prefill

    fn, E = swiglu_decode()
    H = 8192
    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    (tmp_path / "decode").mkdir()
    _lower_all(fn.trace(x=(1, E)), tmp_path / "decode")
    (tmp_path / "prefill").mkdir()
    _lower_all(
        swiglu_prefill(z(E, H), z(E, H), z(H, E)).trace(x=(256, E)),
        tmp_path / "prefill",
    )


PREFILL = dict(
    S=2048, E=2048, F=8192, H=32, G=8, D=64
)  # Llama 3.2 1B's prefill at the maximum length


def _reorder(sizes, in_strides, out_strides, **kw):
    from iron.operators.strided_copy import StridedCopy

    n = int(np.prod(sizes))
    return StridedCopy(
        input_sizes=sizes,
        input_strides=in_strides,
        input_offset=0,
        input_buffer_size=n,
        output_sizes=sizes,
        output_strides=out_strides,
        output_offset=0,
        output_buffer_size=n,
        **kw,
    )


@pytest.mark.parametrize(
    "make",
    [
        pytest.param(
            lambda p: __import__("iron.operators.gemm.op", fromlist=["GEMM"]).GEMM(
                M=p["S"],
                K=p["F"],
                N=p["E"],
                num_aie_columns=8,
                tile_m=64,
                tile_k=64,
                tile_n=64,
                b_col_maj=True,
            ),
            id="down_projection_checkpoint_layout",
        ),
        pytest.param(
            lambda p: _reorder(
                (p["G"], p["S"], p["D"]),
                (p["D"], p["G"] * p["D"], 1),
                (p["S"] * p["D"], p["D"], 1),
                transfer_size=1024,
            ),
            id="kv_into_cache",
        ),
        pytest.param(
            lambda p: __import__("iron.operators.mha.op", fromlist=["MHA"]).MHA(
                num_heads=p["H"],
                seq_len=p["S"],
                d=p["D"],
                num_KV_heads=p["G"],
                num_of_pipelines=8,
                heads_interleaved=True,
            ),
            id="mha_in_the_projections_layout",
        ),
    ],
)
def test_prefill_steps_lower_at_llama_size(make, tmp_path):
    """The steps a prefill graph needs that a small case does not exercise: the
    down projection's column-major weight (its column-block stride is past the
    descriptor's 20-bit step, so B unrolls), the cache write's 2048-wide
    reorder (legalized), and MHA reading (seq, heads, d)."""
    op = make(PREFILL)
    op.tuned(aie_utils.get_current_device())
    lower(op, tmp_path)
