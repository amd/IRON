# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar
import os

from . import compilation as comp
import aie.utils.config


@dataclass
class AIEContext:
    """Context for managing AIE operator compilation state."""

    # Repo root: iron/common/../../.. = three levels up from this file.
    base_dir: ClassVar[Path] = Path(__file__).parent.parent.parent

    build_dir: Path = field(default_factory=lambda: Path(os.getcwd()) / "build")
    mlir_verbose: bool = False

    def __post_init__(self):
        self.build_dir = Path(self.build_dir)

    @property
    def compilation_rules(self):
        mlir_aie_dir = Path(aie.utils.config.root_path())
        peano_dir = Path(aie.utils.config.peano_install_dir())
        return [
            comp.FusePythonGeneratedMLIRCompilationRule(),
            comp.GenerateMLIRFromPythonCompilationRule(),
            comp.PeanoCompilationRule(peano_dir, mlir_aie_dir),
            comp.AieccXclbinInstsCompilationRule(
                self.build_dir, peano_dir, mlir_aie_dir
            ),
            comp.AieccFullElfCompilationRule(self.build_dir, peano_dir, mlir_aie_dir),
        ]
