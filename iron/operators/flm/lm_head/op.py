# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    KernelObjectArtifact,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
)
from iron.operators.flm.lm_head.design import check_shape, lm_head_kernel
from iron.operators.flm.q4nx import packed_bytes


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
        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        dev = aie_utils.get_current_device().resolve().name
        # The name keys the build cache. The softcap changes the runtime
        # sequence, so the name includes it.
        cap = f"{float(self.softcap):g}".replace(".", "p").replace("-", "n")
        return f"FLM_LMHead_d{self.dim}_v{self.vocab}_c{cap}_{dev}"

    def quantized_size(self) -> int:
        """Bytes of q4nx vocabulary the operator reads."""
        return packed_bytes(self.vocab * self.dim)

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
            ),
        )

    def get_kernel_artifacts(self):
        return [KernelObjectArtifact.from_extern(lm_head_kernel(self.dim))]

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
