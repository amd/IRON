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
from iron.common.device_utils import get_kernel_dir
from iron.common.stream.ops import artifacts_for_object, linked_objects


class StreamGroup(MLIROperator):
    group_index: int

    @property
    def _design(self):
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
        """The objects this group's generated design links, built at the shapes it names;
        stream-dse chooses the tile and names the object, and IRON builds that."""
        kernels_dir, kernel_dir = self.context.kernels_dir, get_kernel_dir()
        text = str(self._design.load_group(self.group_index, **self._dims()))
        produced: dict[str, object] = {}
        deferred: list[str] = []
        for name in linked_objects(text):
            # An object one builder makes beside another, like mha.cc's passThrough copy,
            # has no library entry of its own.
            try:
                artifacts = artifacts_for_object(name, kernels_dir, kernel_dir)
            except ValueError:
                deferred.append(name)
                continue
            for artifact in artifacts:
                produced.setdefault(Path(artifact.filename).name, artifact)
        missing = [name for name in deferred if name not in produced]
        if missing:
            raise ValueError(f"no rule builds the kernel objects {missing}")
        return list(produced.values())

    def design_root(self) -> Path:
        """The directory stream wrote this group's design to, with its ``estimate.json``."""
        return Path(self._design.design_root(**self._dims()))

    def design_key(self):
        """Groups whose generated design is byte-identical share it."""
        return self._design.group_digest(self.group_index, **self._dims())

    def get_arg_spec(self):
        """The group's runtime arguments, named, shaped and ordered by the exported
        workload, which is the order the generated design takes them in."""
        shapes, (inputs, outputs) = self._ports()
        return [AIERuntimeArgSpec("in", shapes[name]) for name in inputs] + [
            AIERuntimeArgSpec("out", shapes[name]) for name in outputs
        ]
