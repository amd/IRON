# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``MHAPrefillStream``: the head and the mask it hands stream-dse."""

import pytest

pytest.importorskip("stream", reason="stream-dse is not installed")
pytest.importorskip("onnxscript", reason="onnxscript is not installed")

from stream.compiler.kernels.registry import AIE_KERNELS  # noqa: E402

from iron.common.stream.kernel_library import load_library  # noqa: E402
from iron.operators.mha_prefill_stream.op import (  # noqa: E402
    CONTEXT,
    SCORES,
    SOFTMAX,
    MHAPrefillStream,
)

pytestmark = pytest.mark.usefixtures("npu2")


@pytest.mark.parametrize("causal", [True, False])
def test_every_layer_is_given_the_mask(causal):
    """The score GEMM skips blocks past the diagonal only when the flash kernels mask them."""
    op = MHAPrefillStream(heads=2, seq_len=256, d_head=128, causal=causal)
    ((kernels, _),) = op.candidates()
    library = load_library("aie2p")
    built = {
        name: AIE_KERNELS[kind](**kernels[name], library=library)
        for name, kind in (
            (SCORES, "gemm"),
            (SOFTMAX, "partial_softmax"),
            (CONTEXT, "gemm"),
        )
    }
    assert type(built[SCORES]).__name__ == (
        "CausalGemmKernel" if causal else "GemmKernel"
    )
    assert built[SOFTMAX].causal is causal and built[CONTEXT].causal is causal
    assert (built[SCORES].k, built[CONTEXT].n, built[CONTEXT].k) == (128, 128, 64)


def test_the_score_gemm_multiplies_in_bf16_as_irons_mha_does():
    """IRON's MHA builds QK^T without bfp16 multiplies; the score GEMM is the library's bf16 entry, built so."""
    op = MHAPrefillStream(heads=2, seq_len=256, d_head=128)
    ((kernels, _),) = op.candidates()
    scores = AIE_KERNELS["gemm"](**kernels[SCORES], library=load_library("aie2p"))
    assert scores.spec.symbol == "matmul_bf16_bf16_high"
    assert scores.spec.options == {"bfp16": False}


def test_a_head_matmul_pv_does_not_compile_is_refused():
    """mha.cc takes a head of a multiple of 16: 128 is one, 72 is not."""
    MHAPrefillStream(heads=2, seq_len=256, d_head=128).compatible()
    with pytest.raises(ValueError, match="d_head"):
        MHAPrefillStream(heads=2, seq_len=256, d_head=72).compatible()
