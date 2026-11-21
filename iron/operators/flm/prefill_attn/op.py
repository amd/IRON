# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import functools
from typing import ClassVar

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron import ExternalFunction, In, Out
from aie.utils.compile.jit.params import param, per_call
from ml_dtypes import bfloat16

from iron.common import Operator, Unresolvable
from iron.operators.flm.prefill_attn import reference
from iron.operators.flm.prefill_attn.design import (
    CAUSAL,
    SLIDING,
    Variant,
    prefill_attn,
)


class _PrefillAttentionBase(Operator):
    """Causal prefill attention from a KV cache: ``max_context`` bounds its rows.

    ``num_heads``/``num_kv_heads`` the query and KV heads. The token range
    and the cache's row count are set per call; see README.md.
    """

    # The head dims the operator builds; the first is the default.
    head_dims: ClassVar[tuple[int, ...]]
    # Keys per query, including the query's own key. None: every key up to the
    # query.
    window = None

    max_context: int = param()
    num_heads: int = param()
    num_kv_heads: int = param()
    head_dim: int = param(default=lambda op: op.head_dims[0])
    qo_len: int = param(
        derive=lambda op: op.max_context * op.num_heads * op.head_dim, repr=False
    )
    kv_len: int = param(
        derive=lambda op: 2 * op.max_context * op.num_kv_heads * op.head_dim,
        repr=False,
    )

    # The runtime sequence's argument order.
    o = Out(qo_len, dtype=bfloat16)
    q = In(qo_len, dtype=bfloat16)
    kv = In(kv_len, dtype=bfloat16)
    L_begin = per_call(np.int32)
    L_end = per_call(np.int32)
    max_l = per_call(np.int32)

    @property
    def variant(self) -> Variant:
        """Return the design the head dim runs on."""
        raise NotImplementedError

    def kernel(self) -> ExternalFunction:
        """Return the variant's kernel, built for the head dim."""
        # The factory reads the architecture of the bound device.
        self.dev
        if self.variant.windowed:
            return self.variant.factory(head_dim=self.head_dim)
        return self.variant.factory()

    def validate(self) -> None:
        if self.head_dim not in self.head_dims:
            dims = " or ".join(map(str, self.head_dims))
            raise ValueError(
                f"{type(self).__name__}: head_dim ({self.head_dim}) must be {dims}"
            )
        for name in ("max_context", "num_heads", "num_kv_heads"):
            if vars(self)[name] <= 0:
                raise ValueError(
                    f"{type(self).__name__}: {name} ({vars(self)[name]}) must be positive"
                )
        if self.num_heads % self.num_kv_heads:
            raise ValueError(
                f"{type(self).__name__}: num_heads ({self.num_heads}) must be a multiple of "
                f"num_kv_heads ({self.num_kv_heads})"
            )
        num_cu = self.variant.num_cu
        if (self.num_heads // self.num_kv_heads) % num_cu:
            raise ValueError(
                f"{type(self).__name__}: each KV head must serve a multiple of {num_cu} query heads"
            )
        for name, value in (("max_context", self.max_context), ("window", self.window)):
            if value is not None and value % 128:
                raise ValueError(
                    f"{type(self).__name__}: {name} ({value}) must be a multiple of 128"
                )

    def resolve(self, dev):
        if dev is None or dev.arch != AIEArch.AIE2p:
            raise Unresolvable(
                f"{type(self).__name__}: the {self.variant.factory.__name__} kernel is AIE2P only"
            )
        return self.replace()

    def exported_design(self):
        return functools.partial(
            prefill_attn,
            self.dev,
            self.variant.name,
            self.max_context,
            self.num_heads,
            self.num_kv_heads,
            self.window,
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
    """Causal prefill attention with a head dim of 512 or 128, from a KV cache.

    128 runs on the sliding-window design with a window of the whole cache.
    """

    head_dims = (512, 128)

    @property
    def variant(self) -> Variant:
        """Return the global design at 512, else the sliding-window one."""
        return CAUSAL if self.head_dim == 512 else SLIDING

    @property
    def window(
        self,
    ) -> int | None:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Return None at 512; at 128, the cache's rows, which no query sees past."""
        return None if self.head_dim == 512 else self.max_context


class PrefillSlidingAttention(_PrefillAttentionBase):
    """Sliding-window causal prefill attention with a head dim of 256 or 128, from a KV cache."""

    head_dims = (256, 128)
    window: int = param(default=512)

    @property
    def variant(self) -> Variant:
        """Return the sliding-window design."""
        return SLIDING
