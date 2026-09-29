# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    KernelObjectArtifact,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
)
from iron.operators.flm.lm_head.design import (
    K_TILE,
    lm_head_kernel,
    packed_bytes,
    vocab_per_round,
)


@dataclass
class LMHead(MLIROperator):
    """Softcapped logits from a q4nx vocabulary, with the RMS norm folded in.

    ``dim`` in-features, ``vocab`` out-features, ``softcap`` the tanh bound.
    X carries the token followed by its RMS weight; W is the packed q4nx
    vocabulary; Y is the logits.
    """

    dim: int
    vocab: int
    softcap: float
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        dev = aie_utils.get_current_device()
        if dev.arch != AIEArch.AIE2p:
            raise NotImplementedError("the q4nx_lm_head kernel is AIE2P only")
        if self.dim % K_TILE:
            raise ValueError(f"dim ({self.dim}) must be a multiple of {K_TILE}")
        per_round = vocab_per_round(dev)
        if self.vocab % per_round:
            raise ValueError(
                f"vocab ({self.vocab}) must be a multiple of {per_round}, "
                "the out-features one round produces"
            )
        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        dev = aie_utils.get_current_device().resolve().name
        # The softcap reaches only the runtime sequence, but the sequence is
        # part of this operator's instruction stream, so it keys the cache too.
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
        # The order the design's runtime sequence takes: y, w, x.
        return [
            AIERuntimeArgSpec("out", (self.vocab,), dtype=bfloat16),
            AIERuntimeArgSpec(
                "in",
                (self.quantized_size() // np.dtype(np.uint32).itemsize,),
                dtype=np.uint32,
            ),
            AIERuntimeArgSpec("in", (2 * self.dim,), dtype=bfloat16),
        ]
