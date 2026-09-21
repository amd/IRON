# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import dataclasses
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, ClassVar

import aie.utils as aie_utils

from . import compilation as comp
from .context import AIEContext
from .utils import float_to_name
from .compilation import CompilationArtifact


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    _default_context: ClassVar[AIEContext | None] = None

    def __init__(self, context: AIEContext | None = None) -> None:
        self.artifacts = comp.CompilationArtifactGraph()
        if context is None:
            context = self.get_default_context()
        self.context = context

    @abstractmethod
    def set_up_artifacts(self) -> None:
        """
        Declare the artifact dependency graph for this operator.

        Subclasses must implement this method and call add_artifacts() to register
        the artifacts they require. This method should only *describe* dependencies;
        it must not perform any computation or compilation.  Compilation is triggered
        separately via compile().
        """
        pass

    @abstractmethod
    def get_callable(self) -> Callable[..., Any]:
        pass

    @classmethod
    def get_default_context(cls) -> AIEContext:
        """Return the process-wide default AIEContext, creating it on first call (lazy singleton)."""
        if AIEOperatorBase._default_context is None:
            AIEOperatorBase._default_context = AIEContext()
        return AIEOperatorBase._default_context

    def compile(self, dry_run: bool = False) -> AIEOperatorBase:
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up_artifacts(); they may register any
        artifacts that they need to be compiled there.
        """
        if not self.artifacts:
            self.set_up_artifacts()
        comp.compile(
            self.context.compilation_rules,
            self.artifacts,
            self.context.build_dir,
            dry_run=dry_run,
        )
        return self

    def add_artifacts(self, artifacts: list[CompilationArtifact]) -> None:
        for artifact in artifacts:
            self.artifacts.add(artifact)

    # Parameters every design takes but no operator stores. Exposing them as
    # attributes is what lets bind() fill a design's signature whole, instead
    # of each operator keeping a dict to splice them in by hand.

    @property
    def dev(self):
        """The device a design is generated for."""
        return aie_utils.get_current_device()

    @property
    def kernels_dir(self):
        """Where a design finds the C++ its kernels are compiled from.

        Taken from the context rather than resolved in the design, so that
        IRON_AIE_KERNELS_DIR still redirects it -- and so that pointing IRON at
        a different kernel tree changes the compile cache key, which it should.
        """
        return self.context.kernels_dir

    # Bytes of trace buffer to emit; 0 disables tracing, which is what every
    # hand-written kwargs dict passed. Deliberately a plain class attribute
    # rather than a property: OperatorSequence and LayerNorm both assign
    # self.trace_size, and a property without a setter cannot be shadowed by
    # an instance attribute -- it raises instead. Left unannotated so that
    # dataclass subclasses do not pick it up as a field.
    trace_size = 0

    @property
    def verbose(self) -> bool:
        """Whether a design should log while generating.

        Read off the context, which is where the setting already lived; every
        operator that passed this spelled it ``mlir_verbose`` by hand.
        """
        return getattr(self.context, "mlir_verbose", False)


def _serialize_param(v: object) -> str:
    """Convert a parameter value to a filesystem-safe string for operator names."""
    if isinstance(v, bool):
        return str(int(v))
    if isinstance(v, float):
        return float_to_name(v)
    if isinstance(v, (list, tuple)):
        return "x".join(str(x) for x in v)
    return str(v)
