# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import logging
from pathlib import Path
import os

from .device_manager import AIEDeviceManager, pyxrt
from . import compilation as comp
import aie.utils.config


class AIEContext:
    """Context for managing AIE operator compilation and runtime state"""

    def __init__(self, use_runlist=True, build_dir=None, mlir_verbose=None):
        self.operators = []
        self.static_data_pool = {}
        self.device_manager = AIEDeviceManager()
        self.base_dir = Path(__file__).parent.parent.parent
        self.build_dir = build_dir or Path(os.getcwd()) / "build"
        self.mlir_aie_dir = Path(aie.utils.config.root_path())
        self.peano_dir = Path(aie.utils.config.peano_install_dir())
        # Disable the XRT runlist sacrifices performance by executing kernels individually as separate xclbin invocations for easier debugging (can tell which part of runlist execution failed)
        self.use_runlist = use_runlist
        self.mlir_verbose = bool(mlir_verbose)
        self.compilation_rules = [
            comp.FusePythonGeneratedMLIRCompilationRule(),
            comp.GenerateMLIRFromPythonCompilationRule(),
            comp.PeanoCompilationRule(self.peano_dir, self.mlir_aie_dir),
            comp.ArchiveCompilationRule(self.peano_dir),
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
