# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One operator built and run on its own, outside a graph."""

from __future__ import annotations

from typing import Self

from ..declare import Operator
from ..graph.record import Recording
from .artifacts import Artifacts
from .link import PerStep
from .sequence import Image


class OperatorImage:
    """An operator's own xclbin and instruction stream, and a call of them:
    what ``Operator.compile`` builds once and a call outside a graph runs,
    with the operator's buffers as device tensors, in declaration order.

    It is the one-step sequence of the operator as an xclbin chain
    (``PerStep``), so the xclbin is the operator's
    ``Operator.configuration``'s: an operator whose array serves every
    shape (flm.ProjectionGEMM) compiles only an instruction stream per shape, and
    on a shipped image (``image=``) it is the download.
    """

    def __init__(self, op: Operator) -> None:
        self.op = op
        self._sequence: Image | None = None
        self._chain = PerStep()

    def compile(self) -> Self:
        """Build the image, once."""
        if self._sequence is None:
            self._sequence = Image(
                Recording.of_step(self.op.resolved()), self._chain
            ).compile()
        return self

    @property
    def artifacts(self) -> Artifacts:
        """The record of what ``compile`` produced."""
        if self._sequence is None:
            raise RuntimeError(f"{self.op!r} is not compiled; compile() first")
        return self._sequence.artifacts

    def __call__(self, *args, **scalars):
        """Run the image on ``args``, loading it into the shared runtime
        unless it is there already. ``scalars`` are the call's
        ``DispatchTime`` values, by device symbol.
        """
        self.compile()
        (step,) = self._sequence.steps
        _, result = self._chain.links[id(step.op)].kernel(*args, **scalars)
        return result
