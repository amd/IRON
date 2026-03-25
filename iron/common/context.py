# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import os

from .device_manager import AIEDeviceManager, pyxrt
from . import compilation as comp
import aie.utils.config


class AIEContext:
    """Context for managing AIE operator compilation and runtime state"""

    def __init__(self, build_dir=None, mlir_verbose=None):
        self.operators = []
        self.device_manager = AIEDeviceManager()
        # base_dir points to the repo root: iron/common/../../.. = three levels up from this file
        self.base_dir = Path(__file__).parent.parent.parent
        self.build_dir = build_dir or Path(os.getcwd()) / "build"
        self.mlir_aie_dir = Path(aie.utils.config.root_path())
        self.peano_dir = Path(aie.utils.config.peano_install_dir())
        self.mlir_verbose = bool(mlir_verbose)
        self.compilation_rules = [
            comp.FusePythonGeneratedMLIRCompilationRule(),
            comp.GenerateMLIRFromPythonCompilationRule(),
            comp.PeanoCompilationRule(self.peano_dir, self.mlir_aie_dir),
            comp.AieccXclbinInstsCompilationRule(
                self.build_dir, self.peano_dir, self.mlir_aie_dir
            ),
            comp.AieccFullElfCompilationRule(
                self.build_dir, self.peano_dir, self.mlir_aie_dir
            ),
        ]

    def register_operator(self, operator):
        """Register an operator with this context"""
        operator.context = self
        self.operators.append(operator)

    def compile_all(self):
        """Compile all registered operators"""
        self.build_dir.mkdir(parents=True, exist_ok=True)
        for op in self.operators:
            op.compile()
