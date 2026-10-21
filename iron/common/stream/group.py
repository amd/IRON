# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One stream-dse design as an ``OperatorSequence`` child. A concrete group supplies its
design module, dimensions and runtime ports, and inherits loading, keying, kernel
compilation and its argument spec."""

from pathlib import Path

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
)
from iron.common.compilation import KernelObjectArtifact
from iron.common.stream.design import group_dir


class StreamGroup(MLIROperator):
    group_index: int

    @property
    def _design_module(self):
        raise NotImplementedError

    def _dims(self) -> dict:
        """Everything that names one generated design, as ``load_group`` kwargs."""
        raise NotImplementedError

    def _ports(self):
        """(tensor shapes by name, (input names, output names)) for this group."""
        raise NotImplementedError

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}_{self.design_key()[:12]}.mlir",
            DesignGenerator(
                self.operator_dir / "stream_design.py",
                "load_group",
                (self.group_index,),
                self._dims(),
            ),
        )

    def get_kernel_artifacts(self):
        """The objects this group's generated design links, built from the bindings
        stream recorded for its calls."""
        from stream.compiler.kernels.binding import load_bindings

        self._design_module.load_group(self.group_index, **self._dims())
        path = Path(group_dir(self.design_root(), self.group_index), "kernels.json")
        return [KernelObjectArtifact.from_extern(b) for b in load_bindings(path)]

    def design_root(self) -> Path:
        """The directory stream wrote this group's design to, with its ``estimate.json``."""
        dims = self._dims()
        del dims["npu"]
        return Path(self._design_module.design_root(**dims))

    def design_key(self):
        """Groups whose generated design is byte-identical share it."""
        return self._design_module.group_digest(self.group_index, **self._dims())

    def get_arg_spec(self):
        """The group's runtime arguments, named, shaped and ordered by the exported
        workload, which is the order the generated design takes them in."""
        shapes, (inputs, outputs) = self._ports()
        return [AIERuntimeArgSpec("in", shapes[name]) for name in inputs] + [
            AIERuntimeArgSpec("out", shapes[name]) for name in outputs
        ]
