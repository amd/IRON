# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One operator built and run on its own, outside a graph."""

from __future__ import annotations

from typing import Self

import aie.utils as aie_utils
from aie.utils.npukernel import NPUKernel

from ..declare import Operator
from ..design import OperatorDesign
from .artifacts import Artifacts, Design, Step


class OperatorImage:
    """An operator's own xclbin and instruction stream, and a call of them.

    ``OperatorImage(op).compile()`` builds once; the image is then called
    with the operator's buffers as device tensors, in declaration order.
    The xclbin is the operator's ``Operator.configuration``'s, so an
    operator whose array serves every shape (flm's GEMM) compiles only an
    instruction stream per shape; on a shipped image (``image=``) it is the
    download, and only the stream is built.
    """

    def __init__(self, op: Operator) -> None:
        self.op = op
        self._artifacts: Artifacts | None = None
        self._kernel: NPUKernel | None = None

    def compile(self, record: str = "memory") -> Self:
        """Build the image, once. ``record="disk"`` also writes its
        ``Artifacts`` record beside it; by default it is kept in memory.
        """
        if self._artifacts is None:
            self._artifacts = self._build()
            if record == "disk":
                self._artifacts.dump()
        return self

    @property
    def artifacts(self) -> Artifacts:
        """The record of what ``compile`` produced."""
        if self._artifacts is None:
            raise RuntimeError(f"{self.op!r} is not compiled; compile() first")
        return self._artifacts

    def __call__(self, *args, **scalars):
        """Run the image on ``args``, loading it into the shared runtime
        unless it is there already. ``scalars`` are the call's
        ``DispatchTime`` values, by device symbol.
        """
        self.compile()
        _, result = aie_utils.DefaultNPURuntime.load_and_run(
            self._kernel, list(args), dispatch_scalars=scalars or None
        )
        return result

    def _build(self) -> Artifacts:
        op = self.op.resolved()
        if op.external is not None:
            # A shipped image: only the stream is built, against the download.
            config = op
            image = op.external.fetch()
            own = OperatorDesign(op, "xclbin").compile(insts_only=True)
            entry = own.get_cache_entry()
            kernel_name = op.external.kernel_name
        else:
            config = op.configuration()
            built = OperatorDesign(config, "xclbin").compile()
            entry = built.get_cache_entry()
            assert entry is not None and entry.xclbin is not None
            image = entry.xclbin
            # A stream generated per call has no insts_only build: its
            # dispatch library comes with a full one.
            per_call = any(v.kind == "dispatch" for v in op.values)
            own = (
                built
                if config is op
                else OperatorDesign(op, "xclbin").compile(insts_only=not per_call)
            )
            kernel_name = "MLIR_AIE"
        stream = own.get_cache_entry()
        # A design with DispatchTime values generates its stream per call.
        assert stream is not None and (
            stream.insts is not None or own.dispatch_params
        )
        self._kernel = NPUKernel(
            image,
            stream.insts,
            kernel_name=kernel_name,
            dispatch_params=own.dispatch_params,
            dispatch_lib_path=own.get_dispatch_lib_path(),
        )
        buffers = op.buffers
        return Artifacts(
            kind="xclbin",
            image=image,
            insts=stream.insts,
            entry=stream,
            designs=(
                Design(
                    name=config.name,
                    operators=(op.name,),
                    entry=entry,
                    image=image,
                    insts=stream.insts,
                ),
            ),
            steps=(Step(0, op.name, config.name, tuple(b.name for b in buffers)),),
            buffers={b.name: ("arg", i, b.nbytes) for i, b in enumerate(buffers)},
        )
