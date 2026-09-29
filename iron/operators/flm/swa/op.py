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

from iron.operators.flm.swa.design import DH, NUM_CU, swa_kernel


@dataclass
class PrefillSlidingAttention(MLIROperator):
    """Sliding-window causal prefill attention with a head dim of 256, from a KV cache.

    ``max_context`` bounds the KV cache rows, ``num_heads`` and
    ``num_kv_heads`` the query and KV heads, and ``window`` the keys a query
    sees: those less than ``window`` tokens before it, and itself. The token
    range and the cache's row count are dispatch parameters; see
    :meth:`get_dispatch_params`.
    """

    max_context: int
    num_heads: int
    num_kv_heads: int
    window: int = 512
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        dev = aie_utils.get_current_device()
        if dev.arch != AIEArch.AIE2p:
            raise NotImplementedError("the swa_prefill kernel is AIE2P only")
        if self.num_heads % self.num_kv_heads:
            raise ValueError(
                f"num_heads ({self.num_heads}) must be a multiple of "
                f"num_kv_heads ({self.num_kv_heads})"
            )
        if (self.num_heads // self.num_kv_heads) % NUM_CU:
            raise ValueError(
                f"each KV head must serve a multiple of {NUM_CU} query heads"
            )
        for name in ("max_context", "window"):
            if getattr(self, name) % 128:
                raise ValueError(
                    f"{name} ({getattr(self, name)}) must be a multiple of 128"
                )
        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        dev = aie_utils.get_current_device().resolve().name
        return (
            f"FLM_PrefillSlidingAttention_ctx{self.max_context}_h{self.num_heads}"
            f"_kv{self.num_kv_heads}_w{self.window}_{dev}"
        )

    def get_dispatch_params(self):
        """``L_begin`` and ``L_end`` bound the query tokens, and ``max_l`` is
        the KV cache's row count, which sets where V starts. ``L_begin`` and
        ``L_end`` must be multiples of 128, and ``max_l`` at most
        ``max_context``."""
        return {"L_begin": np.int32, "L_end": np.int32, "max_l": np.int32}

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "swa",
                (
                    aie_utils.get_current_device(),
                    self.max_context,
                    self.num_heads,
                    self.num_kv_heads,
                    self.window,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        return [KernelObjectArtifact.from_extern(swa_kernel())]

    def get_arg_spec(self):
        # The order the design's runtime sequence takes: o, q, kv.
        rows = self.max_context * DH
        return [
            AIERuntimeArgSpec("out", (rows * self.num_heads,), dtype=bfloat16),
            AIERuntimeArgSpec("in", (rows * self.num_heads,), dtype=bfloat16),
            AIERuntimeArgSpec("in", (2 * rows * self.num_kv_heads,), dtype=bfloat16),
        ]
