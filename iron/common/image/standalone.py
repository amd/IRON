# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One operator built and run on its own, outside a graph."""

from __future__ import annotations

from typing import Self

import aie.utils as aie_utils
from aie.utils.npukernel import NPUKernel

from ..declare import Operator
from ..design import generator_for
from .artifacts import Artifacts, Design, Step
from .jit_compile import cache_entry, insts_design, xclbin_design


class OperatorImage:
    """An operator's own xclbin and instruction stream, and a call of them.

    ``OperatorImage(op).compile()`` builds once; the image is then called
    with the operator's buffers as device tensors, in declaration order.
    The xclbin is the operator's :meth:`~Operator.configuration`'s, so an
    operator whose array serves every shape (flm's GEMM) compiles only an
    instruction stream per shape; on a shipped image (``image=``) it is the
    download, and only the stream is built.
    """

    def __init__(self, op: Operator) -> None:
        self.op = op
        self._artifacts: Artifacts | None = None
        self._handle = None

    def compile(self, record: str = "memory") -> Self:
        """Build the image, once. ``record="disk"`` also writes its
        :class:`Artifacts` record beside it; by default it is kept in memory.
        """
        if self._artifacts is None:
            self._artifacts = self._build()
            if record == "disk":
                self._artifacts.dump()
        return self

    @property
    def artifacts(self) -> Artifacts:
        """The record of what :meth:`compile` produced."""
        if self._artifacts is None:
            raise RuntimeError(f"{self.op!r} is not compiled; compile() first")
        return self._artifacts

    def __call__(self, *args):
        """Run the image on ``args``, loading it on the first call."""
        if self._handle is None:
            artifacts = self.compile().artifacts
            external = self.op.external
            self._handle = aie_utils.DefaultNPURuntime.load(
                NPUKernel(
                    xclbin_path=str(artifacts.image),
                    kernel_name=(
                        "MLIR_AIE" if external is None else external.kernel_name
                    ),
                    insts_path=str(artifacts.insts),
                )
            )
        return aie_utils.DefaultNPURuntime.run(self._handle, list(args))

    def _build(self) -> Artifacts:
        op = self.op.resolved()
        if op.external is not None:
            config = op
            entry = own = cache_entry(insts_design(generator_for(op, "xclbin")))
            image = op.external.fetch()
        else:
            config = op.configuration()
            entry = cache_entry(
                xclbin_design(generator_for(config, "xclbin"), kernel_name="MLIR_AIE")
            )
            own = (
                entry
                if config is op
                else cache_entry(insts_design(generator_for(op, "xclbin")))
            )
            image = entry.xclbin
        assert image is not None and own.insts is not None
        buffers = op.buffers
        return Artifacts(
            kind="xclbin",
            image=image,
            insts=own.insts,
            entry=own,
            designs=(
                Design(
                    name=config.name,
                    operators=(op.name,),
                    entry=entry,
                    image=image,
                    insts=own.insts,
                ),
            ),
            steps=(Step(0, op.name, config.name, tuple(b.name for b in buffers)),),
            buffers={b.name: ("arg", i, b.nbytes) for i, b in enumerate(buffers)},
        )
