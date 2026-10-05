# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import functools
from typing import ClassVar

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron import ExternalFunction
from ml_dtypes import bfloat16

from iron.common import DispatchTime, In, Operator, Out, Unresolvable, param
from iron.operators.flm.prefill_attn import reference
from iron.operators.flm.prefill_attn.design import (
    CAUSAL,
    IN_CONS_LOCK,
    IN_PROD_LOCK,
    SLIDING,
    Geometry,
    Variant,
    prefill_attn,
)


class _PrefillAttentionBase(Operator):
    """Causal prefill attention from a KV cache.

    ``max_context`` bounds the rows of the KV cache. ``num_heads`` and
    ``num_kv_heads`` count the query heads and the KV heads. The token range
    and the cache's row count are set per call; see README.md.
    """

    variant: ClassVar[Variant]
    # Keys per query, including the query's own key. None: every key up to the
    # query.
    window = None

    max_context: int = param()
    num_heads: int = param()
    num_kv_heads: int = param()
    head_dim: int = param(default=lambda op: Geometry.of(op.kernel()).dh, repr=False)
    qo_len: int = param(
        default=lambda op: op.max_context * op.num_heads * op.head_dim, repr=False
    )
    kv_len: int = param(
        default=lambda op: 2 * op.max_context * op.num_kv_heads * op.head_dim,
        repr=False,
    )

    # The runtime sequence's argument order.
    o = Out(qo_len, dtype=bfloat16)
    q = In(qo_len, dtype=bfloat16)
    kv = In(kv_len, dtype=bfloat16)
    L_begin = DispatchTime(np.int32)
    L_end = DispatchTime(np.int32)
    max_l = DispatchTime(np.int32)

    def kernel(self) -> ExternalFunction:
        """The variant's kernel, built with the k/v locks the design declares."""
        # The factory reads the architecture of the bound device.
        self.dev
        return self.variant.factory(
            in_prod_lock=IN_PROD_LOCK, in_cons_lock=IN_CONS_LOCK
        )

    def validate(self) -> None:
        for name in ("max_context", "num_heads", "num_kv_heads"):
            if getattr(self, name) <= 0:
                raise ValueError(f"{name} ({getattr(self, name)}) must be positive")
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
        self.check_derived("head_dim", "qo_len", "kv_len")

    def resolve(self, dev):
        if dev is None or dev.arch != AIEArch.AIE2p:
            raise Unresolvable(
                f"the {self.variant.factory.__name__} kernel is AIE2P only"
            )
        return dataclasses.replace(self)

    def value_symbol(self, value) -> str:
        # The design's own DispatchTime parameters carry these names.
        return value.name

    def exported_design(self, image: str):
        return functools.partial(
            prefill_attn,
            self.dev,
            self.variant.name,
            self.max_context,
            self.num_heads,
            self.num_kv_heads,
            self.window,
            0,
            kernel=self.kernel(),
        )

    def reference(self, q, kv, L_begin, L_end, max_l):
        """O's first ``L_end - L_begin`` token rows, flat, in float32."""
        return reference.reference(
            q,
            kv,
            L_begin,
            L_end,
            max_l,
            self.num_heads,
            self.num_kv_heads,
            self.head_dim,
            self.window,
        ).reshape(-1)


class PrefillAttention(_PrefillAttentionBase):
    """Causal prefill attention with a head dim of 512, from a KV cache."""

    variant = CAUSAL


class PrefillSlidingAttention(_PrefillAttentionBase):
    """Sliding-window causal prefill attention with a head dim of 256, from a KV cache."""

    variant = SLIDING
    window: int = param(default=512)
