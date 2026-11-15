# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The SwiGLU prefill block's fused groups, each an operator stream-dse generates."""

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

# The workload's layers, in the order they run.
GATE, UP, SILU, MUL, DOWN = "gate", "up", "silu", "mul", "down"
LAYERS = (GATE, UP, SILU, MUL, DOWN)
GEMMS = (GATE, UP, DOWN)

# The partitions stream-dse chooses between, by their number of fused groups:
# the whole block as one design, the gated product and the down projection,
# or a design per layer.
PARTITIONS = {
    1: (LAYERS,),
    2: ((GATE, SILU, UP, MUL), (DOWN,)),
    5: tuple((layer,) for layer in LAYERS),
}
FUSED_PARTITION = 1
# The partition whose SiLU and product run as post-ops on the cores of the
# gate and up GEMMs, so its first group needs no elementwise cores.
POST_OP_PARTITION = 2


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
    "of 512 to 2048, as IRON's Precision.MEDIUM GEMMs measure on the same "
    "reference",
)


class _SwiGLUStream(StreamOperator):
    """A fused group of stream-dse's design of the SwiGLU prefill block.

    ``partition`` and ``gemm_block`` narrow what stream-dse chooses between:
    the partition, by its number of groups (``PARTITIONS``), and the
    ``(sequence, embedding, hidden)`` block its GEMM tile search starts
    from. None leaves the choice to stream-dse. Every group of one design
    shares its solve, and a group of a partition stream-dse did not choose is
    unresolvable; see README.md.
    """

    seq_len: int = param()
    embedding_dim: int = param()
    hidden_dim: int = param()
    partition: int | None = param(default=None)
    gemm_block: tuple[int, int, int] | None = param(default=None)

    def validate(self) -> None:
        if self.partition is not None and self.partition not in PARTITIONS:
            raise ValueError(
                f"{type(self).__name__}: partition ({self.partition}) must be one "
                f"of {sorted(PARTITIONS)}"
            )

    def compatible(self) -> None:
        self.candidates()

    def workload(self):
        from .design import workload

        return workload(self.seq_len, self.embedding_dim, self.hidden_dim)

    def candidates(self):
        from .design import candidates

        return candidates(
            self.seq_len,
            self.embedding_dim,
            self.hidden_dim,
            self.dev,
            self.partition,
            self.gemm_block,
        )

    def solve_key(self):
        return "SwiGLUPrefillStream", (
            self.seq_len,
            self.embedding_dim,
            self.hidden_dim,
            self.partition,
            self.gemm_block,
        )


def solution(seq_len, embedding_dim, hidden_dim, partition=None, gemm_block=None):
    """Return stream-dse's design of the block at one size, solving it on the first call."""
    return (
        _SwiGLUStream(
            seq_len=seq_len,
            embedding_dim=embedding_dim,
            hidden_dim=hidden_dim,
            partition=partition,
            gemm_block=gemm_block,
        )
        .resolved()
        .solution()
    )


class SwiGLUFusedStream(_SwiGLUStream):
    """The whole SwiGLU prefill block as one fused group.

    ``(SiLU(input @ w_gate.T) * (input @ w_up.T)) @ w_down.T``, every layer on
    the array at once and pipelined, its intermediates on chip.
    """

    test = Testing(
        [
            Case(
                dict(seq_len=256, embedding_dim=512, hidden_dim=2048, partition=1),
                bench=True,
            ),
            Case(
                dict(seq_len=2048, embedding_dim=512, hidden_dim=2048, partition=1),
                extensive=True,
            ),
        ],
        draw=lambda op: dict(
            normal=(op.input, op.w_gate, op.w_up, op.w_down),
            scale=op.embedding_dim**-0.25,
        ),
    )

    input = In(_SwiGLUStream.seq_len, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    w_gate = In(_SwiGLUStream.hidden_dim, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    w_up = In(_SwiGLUStream.hidden_dim, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    w_down = In(_SwiGLUStream.embedding_dim, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    output = Out(_SwiGLUStream.seq_len, _SwiGLUStream.embedding_dim, dtype=bfloat16)

    def layers(self):
        return PARTITIONS[FUSED_PARTITION][0]

    def ops(self) -> int:
        return 6 * self.seq_len * self.embedding_dim * self.hidden_dim

    def reference(self, input, w_gate, w_up, w_down):
        """Return the block in float32, each intermediate rounded to bf16 as the cores hold it."""
        x = np.asarray(input, dtype=np.float32)
        gate = _bf16(x @ np.asarray(w_gate, dtype=np.float32).T)
        up = _bf16(x @ np.asarray(w_up, dtype=np.float32).T)
        hidden = _mul(_silu(gate), up)
        return hidden @ np.asarray(w_down, dtype=np.float32).T

    def tolerance(self) -> Tolerance:
        return GEMM_TOLERANCE


class SwiGLUGatedStream(_SwiGLUStream):
    """The gate and up projections and their gated product as one fused group.

    ``SiLU(x @ w_gate.T) * (x @ w_up.T)`` over ``(seq_len, hidden_dim)``, the
    SiLU and the product run as post-ops on the GEMMs' cores.
    """

    x = In(_SwiGLUStream.seq_len, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    w_gate = In(_SwiGLUStream.hidden_dim, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    w_up = In(_SwiGLUStream.hidden_dim, _SwiGLUStream.embedding_dim, dtype=bfloat16)
    y = Out(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)

    def layers(self):
        return PARTITIONS[POST_OP_PARTITION][0]

    def ops(self) -> int:
        return 4 * self.seq_len * self.embedding_dim * self.hidden_dim

    def reference(self, x, w_gate, w_up):
        x = np.asarray(x, dtype=np.float32)
        gate = _bf16(x @ np.asarray(w_gate, dtype=np.float32).T)
        up = _bf16(x @ np.asarray(w_up, dtype=np.float32).T)
        return _mul(_silu(gate), up)

    def tolerance(self) -> Tolerance:
        return GEMM_TOLERANCE


class SwiGLUProjectionStream(_SwiGLUStream):
    """One of the block's GEMMs alone in its fused group, ``y = x @ w.T``.

    ``layer`` names it: the gate or up projection, ``(seq_len,
    embedding_dim)`` by a ``(hidden_dim, embedding_dim)`` weight, or the down
    projection, ``(seq_len, hidden_dim)`` by an ``(embedding_dim, hidden_dim)``
    weight.
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
    w = In(N, K, dtype=bfloat16)
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
        return np.asarray(x, dtype=np.float32) @ np.asarray(w, dtype=np.float32).T

    def tolerance(self) -> Tolerance:
        return GEMM_TOLERANCE


class SwiGLUSiLUStream(_SwiGLUStream):
    """The gate's SiLU alone in its fused group, over ``(seq_len, hidden_dim)``."""

    x = In(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    y = Out(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)

    def layers(self):
        return (SILU,)

    def reference(self, x):
        return _silu(x)

    def tolerance(self) -> Tolerance:
        return _kernel_tolerance(activation.silu(self.hidden_dim, use_lut=True))


class SwiGLUMulStream(_SwiGLUStream):
    """The gated product ``a * b`` alone in its fused group, over ``(seq_len, hidden_dim)``."""

    a = In(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    b = In(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)
    y = Out(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)

    def layers(self):
        return (MUL,)

    def reference(self, a, b):
        return _mul(a, b)

    def tolerance(self) -> Tolerance:
        return _kernel_tolerance(eltwise.mul_sized(self.hidden_dim))
