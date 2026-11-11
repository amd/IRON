# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils
import numpy as np
from aie.iron import In, Out
from aie.iron.kernels import activation, eltwise
from aie.utils.compile.jit.params import param
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common.stream.operator import StreamOperator
from iron.common.testing import Case, Testing

# The workload's layers, in the order they run, and the tensor each produces
# for the next.
GATE, UP, SILU, MUL, DOWN = "Gemm_Left", "Gemm_Right", "Silu", "Elt_Mul", "Gemm_Down"
LAYERS = (GATE, UP, SILU, MUL, DOWN)
RESULTS = {GATE: "left", UP: "right", SILU: "left_swished", MUL: "intermediate"}
# The layers whose results each layer reads.
READS = {GATE: (), UP: (), SILU: (GATE,), MUL: (SILU, UP), DOWN: (MUL,)}
GEMMS = (GATE, UP, DOWN)


def _post_op_groups() -> tuple[tuple[str, ...], ...]:
    """Return each GEMM with the elementwise layers stream-dse runs on its cores as post-ops.

    An elementwise layer goes with the latest GEMM whose result it reads, the
    others it reads coming from before; a GEMM a post-op reads is the next
    group's own, and their groups are ``_handing_groups``'.
    """
    owner, groups = {}, {}
    for layer in LAYERS:
        if layer in GEMMS:
            owner[layer], groups[layer] = layer, [layer]
            continue
        owner[layer] = max((owner[r] for r in READS[layer]), key=LAYERS.index)
        groups[owner[layer]].append(layer)
    return tuple(tuple(group) for group in groups.values())


def _handing_groups(groups) -> tuple[tuple[str, ...], ...]:
    """Return ``groups`` with each one a post-op of the next reads merged into it."""
    merged = [list(groups[0])]
    for group in groups[1:]:
        reads = {r for layer in group if layer not in GEMMS for r in READS[layer]}
        if reads & set(merged[-1]):
            merged[-1] += group
        else:
            merged.append(list(group))
    return tuple(tuple(group) for group in merged)


# Each partition stream-dse may choose, by its number of fused groups.
PARTITIONS = {1: (LAYERS,), 5: tuple((layer,) for layer in LAYERS)}
# The partition whose elementwise layers run as post-ops of the GEMMs, a
# post-op reading what the GEMM beside it hands on core to core: a core
# reads two operands and the post-op's input over its DMA channels only from
# the core whose memory it shares.
POST_OP_PARTITIONS = {
    len(groups): groups for groups in (_handing_groups(_post_op_groups()),)
}
PARTITIONS = dict(sorted((PARTITIONS | POST_OP_PARTITIONS).items()))


def _bf16(x):
    return np.asarray(x, dtype=np.float32).astype(bfloat16).astype(np.float32)


def _contract(kernel, *inputs):
    """Return ``kernel``'s contract reference over the whole of ``inputs``, in float32."""
    flat = [
        np.asarray(x, dtype=np.float32).astype(bfloat16).reshape(-1) for x in inputs
    ]
    arch = resolve_target_arch(aie_utils.ensure_current_device())
    y = kernel.expected(flat, arch=arch)
    return np.asarray(y, dtype=np.float32).reshape(np.shape(inputs[0]))


def _silu(x):
    """Return the LUT SiLU the cores run, by its kernel's contract."""
    return _contract(activation.silu(np.size(x), use_lut=True), x)


def _mul(a, b):
    return _contract(eltwise.mul_sized(np.size(a)), a, b)


def _kernel_tolerance(kernel) -> Tolerance:
    return kernel.contract_for(
        resolve_target_arch(aie_utils.ensure_current_device())
    ).tolerance


GEMM_TOLERANCE = Tolerance(
    rtol=0.04,
    range_frac=0.05,
    note="the GEMMs round their inputs to bfp16, which the float32 reference "
    "leaves out: at most 0.036 of the output's range on npu2, 256 to 2048 rows "
    "of 512 to 2048, as upstream's MEDIUM GEMMs measure on the same reference",
)


class _SwiGLUStream(StreamOperator):
    """A fused group of stream-dse's design of the SwiGLU prefill block.

    ``k`` and ``gemm_block`` narrow what stream-dse chooses between: the
    partition, by its number of groups (``PARTITIONS``), and the
    ``(sequence, embedding, hidden)`` block its GEMM tile search starts
    from. None leaves the choice to stream-dse. Every group of one design
    shares its solve; see README.md.
    """

    seq_len: int = param()
    embedding_dim: int = param()
    hidden_dim: int = param()
    k: int | None = param(default=None)
    gemm_block: tuple[int, int, int] | None = param(default=None)

    def validate(self) -> None:
        if self.k is not None and self.k not in PARTITIONS:
            raise ValueError(
                f"{type(self).__name__}: k ({self.k}) must be one of {sorted(PARTITIONS)}"
            )

    def explored(self) -> list[tuple[int, tuple[int, int, int]]]:
        """Return the partition and GEMM block of each candidate stream-dse chooses between."""
        return [label for label, _ in self._candidates()]

    def workload(self):
        from .design import workload

        return workload(self.seq_len, self.embedding_dim, self.hidden_dim)

    def candidates(self):
        return [mapping for _, mapping in self._candidates()]

    def _candidates(self):
        from .design import candidates

        return candidates(
            self.seq_len,
            self.embedding_dim,
            self.hidden_dim,
            self.dev,
            self.k,
            self.gemm_block,
        )

    def solve_key(self):
        return "SwiGLUPrefillStream", (
            self.seq_len,
            self.embedding_dim,
            self.hidden_dim,
            self.k,
            self.gemm_block,
        )


class SwiGLUFusedStream(_SwiGLUStream):
    """The whole SwiGLU prefill block as one fused group.

    ``(SiLU(input @ w_gate) * (input @ w_up)) @ w_down``, every layer on
    the array at once and pipelined, its intermediates on chip.
    """

    test = Testing(
        [
            Case(
                dict(seq_len=256, embedding_dim=512, hidden_dim=2048, k=1), bench=True
            ),
            Case(
                dict(seq_len=2048, embedding_dim=512, hidden_dim=2048, k=1),
                extensive=True,
            ),
        ],
        draw=lambda op: dict(
            normal=(op.input, op.w_gate, op.w_up, op.w_down),
            scale=op.embedding_dim**-0.25,
        ),
    )

    input = In(_SwiGLUStream.seq_len, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    w_gate = In(_SwiGLUStream.embedding_dim, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    w_up = In(_SwiGLUStream.embedding_dim, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    w_down = In(_SwiGLUStream.hidden_dim, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    output = Out(_SwiGLUStream.seq_len, _SwiGLUStream.embedding_dim, dtype=bfloat16)

    def layers(self):
        return LAYERS

    def ops(self) -> int:
        return 6 * self.seq_len * self.embedding_dim * self.hidden_dim

    def reference(self, input, w_gate, w_up, w_down):
        """Return the block in float32, each intermediate rounded to bf16 as the cores hold it."""
        x = np.asarray(input, dtype=np.float32)
        gate = _bf16(x @ np.asarray(w_gate, dtype=np.float32))
        up = _bf16(x @ np.asarray(w_up, dtype=np.float32))
        hidden = _mul(_silu(gate), up)
        return hidden @ np.asarray(w_down, dtype=np.float32)

    def tolerance(self) -> Tolerance:
        return GEMM_TOLERANCE


class SwiGLUGatedStream(_SwiGLUStream):
    """The gate and up projections and their gated product as one fused group.

    ``SiLU(x @ w_gate) * (x @ w_up)`` over ``(seq_len, hidden_dim)``, the
    SiLU and the product run as post-ops on the GEMMs' cores.
    """

    x = In(_SwiGLUStream.seq_len, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    w_gate = In(_SwiGLUStream.embedding_dim, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    w_up = In(_SwiGLUStream.embedding_dim, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    y = Out(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)

    def layers(self):
        return next(g for gs in POST_OP_PARTITIONS.values() for g in gs if MUL in g)

    def ops(self) -> int:
        return 4 * self.seq_len * self.embedding_dim * self.hidden_dim

    def reference(self, x, w_gate, w_up):
        x = np.asarray(x, dtype=np.float32)
        gate = _bf16(x @ np.asarray(w_gate, dtype=np.float32))
        up = _bf16(x @ np.asarray(w_up, dtype=np.float32))
        return _mul(_silu(gate), up)

    def tolerance(self) -> Tolerance:
        return GEMM_TOLERANCE


class SwiGLUProjectionStream(_SwiGLUStream):
    """One of the block's GEMMs as a fused group of its own, ``y = x @ w``.

    ``layer`` names it: the gate or up projection, ``(seq_len,
    embedding_dim) @ (embedding_dim, hidden_dim)``, or the down projection,
    ``(seq_len, hidden_dim) @ (hidden_dim, embedding_dim)``.
    """

    layer: str = param()
    K: int = param(
        derive=lambda op: op.hidden_dim if op.layer == DOWN else op.embedding_dim,
        repr=False,
    )
    N: int = param(
        derive=lambda op: op.embedding_dim if op.layer == DOWN else op.hidden_dim,
        repr=False,
    )

    x = In(_SwiGLUStream.seq_len, K, dtype=bfloat16)
    w = In(K, N, dtype=bfloat16)
    y = Out(_SwiGLUStream.seq_len, N, dtype=bfloat16)

    def validate(self) -> None:
        super().validate()
        if self.layer not in (GATE, UP, DOWN):
            raise ValueError(
                f"SwiGLUProjectionStream: layer ({self.layer}) must be one of "
                f"{GATE}, {UP} or {DOWN}"
            )

    def layers(self):
        return (self.layer,)

    def ops(self) -> int:
        return 2 * self.seq_len * self.K * self.N

    def reference(self, x, w):
        return np.asarray(x, dtype=np.float32) @ np.asarray(w, dtype=np.float32)

    def tolerance(self) -> Tolerance:
        return GEMM_TOLERANCE


class SwiGLUSiLUStream(_SwiGLUStream):
    """The gate's SiLU as a fused group of its own, over ``(seq_len, hidden_dim)``."""

    x = In(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    y = Out(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)

    def layers(self):
        return (SILU,)

    def reference(self, x):
        return _silu(x)

    def tolerance(self) -> Tolerance:
        return _kernel_tolerance(activation.silu(self.hidden_dim, use_lut=True))


class SwiGLUMulStream(_SwiGLUStream):
    """The gated product ``a * b`` as a fused group of its own, over ``(seq_len, hidden_dim)``."""

    a = In(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    b = In(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    y = Out(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)

    def layers(self):
        return (MUL,)

    def reference(self, a, b):
        return _mul(a, b)

    def tolerance(self) -> Tolerance:
        return _kernel_tolerance(eltwise.mul_sized(self.hidden_dim))
