# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar

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

from iron.operators.flm.prefill_attn.design import CAUSAL, SLIDING, Variant, kernel


@dataclass
class _PrefillAttentionBase(MLIROperator):
    """Causal prefill attention from a KV cache.

    ``max_context`` bounds the rows of the KV cache. ``num_heads`` and
    ``num_kv_heads`` count the query heads and the KV heads.
    """

    variant: ClassVar[Variant]
    # Keys per query, including the query's own key. None: every key up to the
    # query.
    window = None

    max_context: int
    num_heads: int
    num_kv_heads: int
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        dev = aie_utils.get_current_device()
        if dev.arch != AIEArch.AIE2p:
            raise NotImplementedError(
                f"the {self.variant.factory} kernel is AIE2P only"
            )
        if self.num_heads % self.num_kv_heads:
            raise ValueError(
                f"num_heads ({self.num_heads}) must be a multiple of "
                f"num_kv_heads ({self.num_kv_heads})"
            )
        num_cu = self.variant.num_cu
        if (self.num_heads // self.num_kv_heads) % num_cu:
            raise ValueError(
                f"each KV head must serve a multiple of {num_cu} query heads"
            )
        for name in ("max_context", "window"):
            value = getattr(self, name)
            if value is not None and value % 128:
                raise ValueError(f"{name} ({value}) must be a multiple of 128")
        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        dev = aie_utils.get_current_device().resolve().name
        window = "" if self.window is None else f"_w{self.window}"
        return (
            f"FLM_{type(self).__name__}_ctx{self.max_context}_h{self.num_heads}"
            f"_kv{self.num_kv_heads}{window}_{dev}"
        )

    def get_dispatch_params(self):
        """The token range and the KV cache's row count, set per call.

        The README describes each parameter.
        """
        return {"L_begin": np.int32, "L_end": np.int32, "max_l": np.int32}

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "prefill_attn",
                (
                    aie_utils.get_current_device(),
                    self.variant.name,
                    self.max_context,
                    self.num_heads,
                    self.num_kv_heads,
                    self.window,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        return [KernelObjectArtifact.from_extern(kernel(self.variant))]

    def get_arg_spec(self):
        # The runtime sequence's order: o, q, kv.
        rows = self.max_context * self.variant.dh
        return [
            AIERuntimeArgSpec("out", (rows * self.num_heads,), dtype=bfloat16),
            AIERuntimeArgSpec("in", (rows * self.num_heads,), dtype=bfloat16),
            AIERuntimeArgSpec("in", (2 * rows * self.num_kv_heads,), dtype=bfloat16),
        ]


@dataclass
class PrefillAttention(_PrefillAttentionBase):
    """Causal prefill attention with a head dim of 512, from a KV cache."""

    variant = CAUSAL


@dataclass
class PrefillSlidingAttention(_PrefillAttentionBase):
    """Sliding-window causal prefill attention with a head dim of 256, from a KV cache."""

    variant = SLIDING
    window: int = 512
