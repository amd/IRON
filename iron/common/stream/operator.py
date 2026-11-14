# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``StreamOperator``: one fused group of a workload stream-dse solves, as an operator."""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Sequence

import aie.utils as aie_utils
from aie import ir
from aie.utils.compile.jit.operator import Unresolvable
from aie.utils.compile.utils import resolve_target_arch

from ..declare import Operator

if TYPE_CHECKING:
    from .mapping import FusedGroup
    from .runner import Solution
    from .workload import StreamWorkload

# Solutions this process has read, by the solve's identity.
_solutions: dict[str, Solution] = {}


class StreamOperator(Operator):
    """One fused group of the design stream-dse generates for a workload.

    A subclass declares its parameters and operands as any operator does,
    its operands in the order of the group's runtime sequence (each group's
    ``group_boundaries``: its inputs then its outputs, as its layers use
    them). It gives the workload (``workload``), the mappings stream-dse
    chooses between (``candidates``) and which group it is (``layers``).
    Every operator of one workload and candidate list shares one solve,
    cached on disk (``runner.solve``), and builds its group's design
    (``exported_design``): stream-dse's MLIR, with the kernels it calls.
    """

    def workload(self) -> StreamWorkload:
        """Return the exported workload this operator's group is a part of."""
        raise NotImplementedError(
            f"{type(self).__name__}.workload() is not implemented"
        )

    def candidates(self) -> Sequence[tuple[dict[str, dict], Sequence[FusedGroup]]]:
        """Return the mappings stream-dse chooses between: kernel arguments and groups."""
        raise NotImplementedError(
            f"{type(self).__name__}.candidates() is not implemented"
        )

    def layers(self) -> tuple[str, ...]:
        """Return the workload layers of this operator's fused group."""
        raise NotImplementedError(f"{type(self).__name__}.layers() is not implemented")

    def library(self):
        """Return the ``KernelLibrary`` the solve prices and binds kernels by."""
        from .kernel_library import load_library

        return load_library(resolve_target_arch(self.dev))

    def solve_key(self) -> tuple[str, Any]:
        """Return what names the solve, and what beside its candidates it is a function of.

        Operators whose keys are equal are groups of one design: a subclass
        leaves out the parameters that only pick its group.
        """
        cls, own = super().design_key()
        return cls.__name__, own

    def resolve(self, dev):
        try:
            import stream  # noqa: F401
        except ImportError:
            raise Unresolvable(
                f"{type(self).__name__}: stream-dse is not installed "
                f"(requirements_stream.txt)"
            ) from None
        from .runner import accelerator

        accelerator(dev)
        return self.replace()

    def solution(self) -> Solution:
        """Return stream-dse's design of the workload, solving it on the first call."""
        from .runner import solve

        dev = self.dev
        if dev is None:
            raise Unresolvable(
                f"{type(self).__name__}: stream-dse solves for a device; none is bound"
            )
        name, key = self.solve_key()
        token = repr((name, key, dev.name))
        if token not in _solutions:
            _solutions[token] = solve(
                name, key, self.workload(), self.candidates(), dev, self.library()
            )
        return _solutions[token]

    def group(self) -> int:
        """Return this operator's group in the solution.

        Raises:
            Unresolvable: stream-dse chose a partition without this group.
        """
        layers = self.layers()
        groups = self.solution().groups
        if layers not in groups:
            raise Unresolvable(
                f"{type(self).__name__}: stream-dse fused the layers as {list(groups)}, "
                f"none of which is {list(layers)}"
            )
        return groups.index(layers)

    def design_key(self):
        """Add the revisions of stream-dse and of the kernel library to the identity."""
        from .kernel_library import library_revision
        from .runner import stream_revision

        cls, own = super().design_key()
        arch = resolve_target_arch(self.dev)
        return cls, (*own, ("stream", stream_revision(), library_revision(arch)))

    def exported_design(self):
        return self._design

    def _design(self):
        """Return the group's MLIR module, its kernels registered for the build.

        Raises:
            ValueError: The declared operands are not the group's arguments.
        """
        from stream.compiler.kernels.binding import load_bindings

        from .mapping import group_boundaries

        group = self.group()
        workload = self.workload()
        inputs, outputs = group_boundaries(workload, [self.layers()])[0]
        expected = [workload.shapes[name] for name in (*inputs, *outputs)]
        declared = [tuple(b.shape) for b in self.buffers]
        if declared != expected:
            raise ValueError(
                f"{type(self).__name__} declares operands {declared}; its group "
                f"takes {list(zip((*inputs, *outputs), expected))}"
            )
        codegen = self.solution().codegen(group)
        # Each binding constructs its ExternalFunction, which registers it with
        # this build; stream-dse's factories bind the device they build for.
        with aie_utils.set_current_device(self.dev):
            load_bindings(codegen / "kernels.json")
        return ir.Module.parse((codegen / "final.mlir").read_text())
