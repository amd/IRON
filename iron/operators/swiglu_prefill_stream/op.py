# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import Any, Optional

import aie.utils as aie_utils

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from iron.common.device_utils import get_kernel_dir
from iron.common.sequence import OperatorSequence
from iron.common.stream.ops import ELTWISE_MUL, GEMM, SILU


@dataclass
class _SwiGLUStreamGroup(MLIROperator):
    """One stream-dse design, used as an ``OperatorSequence`` child.

    ``group_index`` selects the design: ``None`` is the whole SwiGLU block
    (``x, w1, w2, w3 -> y``); ``0`` is the gate/up/SiLU/mul front end
    (``x, w1, w2 -> h``); ``1`` is the down projection (``h, w3 -> y``).
    """

    seq_len: int
    embedding_dim: int
    hidden_dim: int
    group_index: Optional[int] = None
    seq_len_tile_size: int = 32
    embedding_tile_size: int = 32
    hidden_tile_size: int = 64
    in_dtype: str = field(default="bf16", repr=False)
    out_dtype: str = field(default="bf16", repr=False)
    rows: int = field(default=4, repr=False)
    num_aie_columns: int = field(default=8, repr=False)
    backend: str = field(default="ortools_gscip", repr=False)
    context: Any = field(default=None, repr=False, compare=False)

    def __post_init__(self):
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        npu = aie_utils.get_current_device().resolve().name
        kwargs = {
            "seq_len": self.seq_len,
            "embedding_dim": self.embedding_dim,
            "hidden_dim": self.hidden_dim,
            "in_dtype": self.in_dtype,
            "out_dtype": self.out_dtype,
            "rows": self.rows,
            "cols": self.num_aie_columns,
            "npu": npu,
            "seq_len_tile_size": self.seq_len_tile_size,
            "embedding_tile_size": self.embedding_tile_size,
            "hidden_tile_size": self.hidden_tile_size,
            "backend": self.backend,
        }
        if self.group_index is None:
            fn, args = "run_main_aie_codegen_swiglu", ()
            kwargs["last_gemm_down"] = True
        else:
            fn, args = "load_swiglu_k2_group", (self.group_index,)
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(self.operator_dir / "stream_design.py", fn, args, kwargs),
        )

    def get_kernel_artifacts(self):
        # Each kernel's source, compile flags and symbol names come from the
        # stream op registry, so they stay in step with the design stream-dse
        # generates against IRON's aie_kernels library.
        from iron.operators.swiglu_prefill_stream.stream_design import gemm_tiles

        base_dir, kernel_dir = self.context.base_dir, get_kernel_dir()
        gate_up, down = gemm_tiles(
            self.seq_len_tile_size, self.embedding_tile_size, self.hidden_tile_size
        )
        kernels = {
            0: [(GEMM, gate_up), (SILU, None), (ELTWISE_MUL, None)],
            1: [(GEMM, down)],
            None: [(GEMM, gate_up), (GEMM, down), (SILU, None), (ELTWISE_MUL, None)],
        }[self.group_index]
        return [
            artifact
            for kernel, tiles in kernels
            for artifact in kernel.kernel_artifacts(
                base_dir, kernel_dir, **(dict(zip("mkn", tiles)) if tiles else {})
            )
        ]

    def get_arg_spec(self):
        m, e, h = self.seq_len, self.embedding_dim, self.hidden_dim
        if self.group_index == 0:
            return [
                AIERuntimeArgSpec("in", (m, e)),  # x
                AIERuntimeArgSpec("in", (e, h)),  # w_gate
                AIERuntimeArgSpec("in", (e, h)),  # w_up
                AIERuntimeArgSpec("out", (m, h)),  # h
            ]
        if self.group_index == 1:
            return [
                AIERuntimeArgSpec("in", (m, h)),  # h
                AIERuntimeArgSpec("in", (h, e)),  # w_down
                AIERuntimeArgSpec("out", (m, e)),  # y
            ]
        return [
            AIERuntimeArgSpec("in", (m, e)),  # x
            AIERuntimeArgSpec("in", (e, h)),  # w_gate
            AIERuntimeArgSpec("in", (e, h)),  # w_up
            AIERuntimeArgSpec("in", (h, e)),  # w_down
            AIERuntimeArgSpec("out", (m, e)),  # y
        ]


def _name(kind, m, e, h, st, et, ht):
    return f"{kind}_m{m}_e{e}_h{h}_st{st}_et{et}_ht{ht}"


def _boundaries(seq_len, embedding_dim, hidden_dim, split_groups=False):
    """Each fused group's (inputs, outputs), named as the exported graph names them.

    Imported lazily: the names come from the exported workload, so only building
    the operator needs stream-dse, not importing it.
    """
    from iron.operators.swiglu_prefill_stream.stream_design import group_ports

    return group_ports(seq_len, embedding_dim, hidden_dim, split_groups)


def _ports(seq_len, embedding_dim, hidden_dim, split_groups=False):
    """Each fused group's arguments in the order its design takes them."""
    return [
        inputs + outputs
        for inputs, outputs in _boundaries(
            seq_len, embedding_dim, hidden_dim, split_groups
        )
    ]


def _external(seq_len, embedding_dim, hidden_dim):
    """The operator's own arguments: what no group produces, and what none consumes."""
    boundaries = _boundaries(seq_len, embedding_dim, hidden_dim, split_groups=True)
    produced = {name for _, outputs in boundaries for name in outputs}
    consumed = {name for inputs, _ in boundaries for name in inputs}
    inputs = tuple(
        dict.fromkeys(
            name for group, _ in boundaries for name in group if name not in produced
        )
    )
    outputs = tuple(
        dict.fromkeys(
            name for _, group in boundaries for name in group if name not in consumed
        )
    )
    return inputs, outputs


class SwiGLUPrefillStream(OperatorSequence):
    """Fused SwiGLU-prefill block generated by stream-dse and deployed as a
    single full-ELF (``OperatorSequence`` default dispatch).

    Runtime buffers (``get_callable().get_buffer(name)``) are named by the
    reference module: ``input``, ``weights_1`` (gate), ``weights_2`` (up),
    ``weights_3`` (down), ``output``. Building requires
    ``stream-dse`` (``pip install stream-dse`` + ``stream-setup-aie``); importing
    this module does not.
    """

    def __init__(
        self,
        seq_len,
        embedding_dim,
        hidden_dim,
        seq_len_tile_size=32,
        embedding_tile_size=32,
        hidden_tile_size=64,
        context=None,
    ):
        block = _SwiGLUStreamGroup(
            seq_len=seq_len,
            embedding_dim=embedding_dim,
            hidden_dim=hidden_dim,
            seq_len_tile_size=seq_len_tile_size,
            embedding_tile_size=embedding_tile_size,
            hidden_tile_size=hidden_tile_size,
            context=context,
        )
        super().__init__(
            name=_name(
                "swiglu_prefill_stream",
                seq_len,
                embedding_dim,
                hidden_dim,
                seq_len_tile_size,
                embedding_tile_size,
                hidden_tile_size,
            ),
            runlist=[(block, *_ports(seq_len, embedding_dim, hidden_dim)[0])],
            input_args=list(_external(seq_len, embedding_dim, hidden_dim)[0]),
            output_args=list(_external(seq_len, embedding_dim, hidden_dim)[1]),
            extra_flags=["--dynamic-objFifos"],
            context=context,
        )


class SwiGLUPrefillStreamK2(OperatorSequence):
    """Two-fusion-group SwiGLU-prefill: a gate/up/SiLU/mul group and a separate
    down-projection group fused into one full-ELF, with the hidden state kept on
    device between them. Same external buffers as :class:`SwiGLUPrefillStream`;
    the split is decided by the mapping's fused groups.
    """

    def __init__(
        self,
        seq_len,
        embedding_dim,
        hidden_dim,
        seq_len_tile_size=32,
        embedding_tile_size=32,
        hidden_tile_size=64,
        context=None,
    ):
        common = dict(
            seq_len=seq_len,
            embedding_dim=embedding_dim,
            hidden_dim=hidden_dim,
            seq_len_tile_size=seq_len_tile_size,
            embedding_tile_size=embedding_tile_size,
            hidden_tile_size=hidden_tile_size,
            context=context,
        )
        front = _SwiGLUStreamGroup(group_index=0, **common)
        down = _SwiGLUStreamGroup(group_index=1, **common)
        super().__init__(
            name=_name(
                "swiglu_prefill_stream_k2",
                seq_len,
                embedding_dim,
                hidden_dim,
                seq_len_tile_size,
                embedding_tile_size,
                hidden_tile_size,
            ),
            runlist=[
                (group, *ports)
                for group, ports in zip(
                    (front, down),
                    _ports(seq_len, embedding_dim, hidden_dim, split_groups=True),
                )
            ],
            input_args=list(_external(seq_len, embedding_dim, hidden_dim)[0]),
            output_args=list(_external(seq_len, embedding_dim, hidden_dim)[1]),
            extra_flags=["--dynamic-objFifos"],
            context=context,
        )
