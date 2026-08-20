# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import Any

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

    ``k`` is how many fused groups the block is split into and ``group_index``
    which of them this is, in the order
    :data:`~iron.operators.swiglu_prefill_stream.stream_design.GROUP_LAYERS`
    lists them.
    """

    seq_len: int
    embedding_dim: int
    hidden_dim: int
    k: int
    group_index: int
    context: Any = field(default=None, repr=False, compare=False)

    def __post_init__(self):
        MLIROperator.__init__(self, context=self.context)

    @property
    def _design(self):
        from iron.operators.swiglu_prefill_stream import stream_design

        return stream_design

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "stream_design.py",
                "load_group",
                (self.group_index,),
                {
                    "k": self.k,
                    "seq_len": self.seq_len,
                    "embedding_dim": self.embedding_dim,
                    "hidden_dim": self.hidden_dim,
                    "npu": aie_utils.get_current_device().resolve().name,
                },
            ),
        )

    def get_kernel_artifacts(self):
        # The registry is the single place a kernel's source, compile flags and
        # symbol names are declared, so the object and the design agree.
        design = self._design
        gemm_tiles = design.gemm_tiles(self.k)
        per_layer = {
            design.GATE: (GEMM, gemm_tiles[design.GATE]),
            design.UP: (GEMM, gemm_tiles[design.UP]),
            design.DOWN: (GEMM, gemm_tiles[design.DOWN]),
            design.SILU: (SILU, None),
            design.MUL: (ELTWISE_MUL, None),
        }
        layers = design.GROUP_LAYERS[self.k][self.group_index]
        base_dir, kernel_dir = self.context.base_dir, get_kernel_dir()
        return [
            artifact
            for kernel, tiles in dict.fromkeys(per_layer[layer] for layer in layers)
            for artifact in kernel.kernel_artifacts(
                base_dir, kernel_dir, **(dict(zip("mkn", tiles)) if tiles else {})
            )
        ]

    def design_key(self):
        """Groups whose generated design is byte-identical share it."""
        return self._design.group_digest(
            self.group_index,
            k=self.k,
            seq_len=self.seq_len,
            embedding_dim=self.embedding_dim,
            hidden_dim=self.hidden_dim,
            npu=aie_utils.get_current_device().resolve().name,
        )

    def get_arg_spec(self):
        """The group's runtime arguments, shaped by the exported graph.

        Both the names and their order come from the workload, which is also the
        order the generated design takes its arguments in.
        """
        dims = (self.seq_len, self.embedding_dim, self.hidden_dim)
        shapes = self._design.workload_for(*dims).shapes
        inputs, outputs = self._design.group_ports(*dims, k=self.k)[self.group_index]
        return [AIERuntimeArgSpec("in", shapes[name]) for name in inputs] + [
            AIERuntimeArgSpec("out", shapes[name]) for name in outputs
        ]


def _wiring(seq_len, embedding_dim, hidden_dim, k):
    """Each group's arguments, and the operator's own inputs and outputs.

    A group's arguments are the tensors it consumes and produces, in the order the
    exported graph uses them. The operator's own arguments are what no group
    produces and what none consumes. Imported lazily, so only building the operator
    needs stream-dse, not importing it.
    """
    from iron.operators.swiglu_prefill_stream.stream_design import group_ports

    boundaries = group_ports(seq_len, embedding_dim, hidden_dim, k)
    produced = {name for _, outputs in boundaries for name in outputs}
    consumed = {name for inputs, _ in boundaries for name in inputs}
    ports = [inputs + outputs for inputs, outputs in boundaries]
    external_inputs = dict.fromkeys(
        name for inputs, _ in boundaries for name in inputs if name not in produced
    )
    external_outputs = dict.fromkeys(
        name for _, outputs in boundaries for name in outputs if name not in consumed
    )
    return ports, list(external_inputs), list(external_outputs)


def _trace_size():
    from iron.operators.swiglu_prefill_stream.stream_design import trace_size

    return trace_size()


class SwiGLUPrefillStream(OperatorSequence):
    """SwiGLU-prefill block generated by stream-dse and deployed as one full ELF.

    ``k`` is how many fused groups the block is split into: 1 keeps the whole block
    on the array at once, 2 splits after the elementwise multiply, and 5 runs layer
    by layer, each layer taking the whole array in turn as
    :mod:`iron.operators.swiglu_prefill` does. The split is decided by the mapping's
    fused groups, and the external buffers are the same either way.

    Runtime buffers (``get_callable().get_buffer(name)``) are named by the reference
    module: ``input``, ``w_gate``, ``w_up``, ``w_down``, ``output``. Building
    requires ``stream-dse`` (``pip install stream-dse`` + ``stream-setup-aie``);
    importing this module does not.
    """

    def __init__(
        self, seq_len, embedding_dim, hidden_dim, k=1, context=None, share_designs=True
    ):
        ports, inputs, outputs = _wiring(seq_len, embedding_dim, hidden_dim, k)
        groups = [
            _SwiGLUStreamGroup(
                seq_len=seq_len,
                embedding_dim=embedding_dim,
                hidden_dim=hidden_dim,
                k=k,
                group_index=index,
                context=context,
            )
            for index in range(len(ports))
        ]
        super().__init__(
            name=f"swiglu_prefill_stream_k{k}_m{seq_len}_e{embedding_dim}_h{hidden_dim}",
            runlist=[
                (group, *group_ports) for group, group_ports in zip(groups, ports)
            ],
            input_args=inputs,
            output_args=outputs,
            trace_size=_trace_size(),
            share_designs=share_designs,
            context=context,
        )
