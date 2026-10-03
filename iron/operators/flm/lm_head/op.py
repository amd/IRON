# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.kernels import flm_gemma4

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    KernelObjectArtifact,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
)
from iron.common.utils import float_to_name
from iron.operators.flm.lm_head.design import check_shape
from iron.operators.flm.q4nx import GROUP, K_TILE, M_TILE, packed_bytes


@dataclass
class LMHead(MLIROperator):
    """Softcapped logits from a q4nx vocabulary, with the RMS norm folded in.

    ``dim`` in-features, ``vocab`` out-features, ``softcap`` the tanh bound.
    X holds the token followed by its RMS weight. W holds the q4nx vocabulary.
    Y receives the logits.
    """

    dim: int
    vocab: int
    softcap: float
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        check_shape(aie_utils.get_current_device(), self.dim, self.vocab)
        if not (np.isfinite(self.softcap) and self.softcap > 0):
            raise ValueError(f"softcap ({self.softcap}) must be finite and positive")
        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        dev = aie_utils.get_current_device().resolve().name
        # The name keys the build cache. The softcap is part of the runtime
        # sequence. The name therefore includes the softcap.
        cap = float_to_name(float(self.softcap))
        return f"FLM_LMHead_d{self.dim}_v{self.vocab}_c{cap}_{dev}"

    def quantized_size(self) -> int:
        """Bytes of q4nx vocabulary the operator reads."""
        return packed_bytes(self.vocab * self.dim)

    def _kernel(self):
        """The flm_gemma4_q4nx_lm_head kernel for dim, which the design and the
        kernel artifact both take."""
        return flm_gemma4.flm_gemma4_q4nx_lm_head(
            dim=self.dim, m_tile=M_TILE, k_tile=K_TILE, group=GROUP
        )

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "lm_head",
                (
                    aie_utils.get_current_device(),
                    self.dim,
                    self.vocab,
                    self.softcap,
                ),
                {"lm_head_kernel": self._kernel()},
            ),
        )

    def get_kernel_artifacts(self):
        return [KernelObjectArtifact.from_extern(self._kernel())]

    def get_arg_spec(self):
        # The runtime sequence's argument order: y, w, x.
        return [
            AIERuntimeArgSpec("out", (self.vocab,), dtype=bfloat16),
            AIERuntimeArgSpec(
                "in",
                (self.quantized_size() // np.dtype(np.uint32).itemsize,),
                dtype=np.uint32,
            ),
            AIERuntimeArgSpec("in", (2 * self.dim,), dtype=bfloat16),
        ]

    def reference(self, w, x):
        """CPU reference, in float64: the softcapped logits of X for W."""
        from iron.operators.flm.lm_head.reference import dequantize, reference

        dev = aie_utils.get_current_device()
        weights = dequantize(w, self.dim, self.vocab, dev.cols, len(dev.core_rows))
        return reference(weights, np.asarray(x, np.float64), self.softcap)
