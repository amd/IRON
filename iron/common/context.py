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
    """Context for managing AIE operator compilation state.

    Attributes:
        base_dir: Repository root directory (three levels above this file).
        build_dir: Directory where compiled artifacts are written.
        mlir_verbose: Enable verbose MLIR output during compilation.
        compiler: Kernel compiler to use: "peano" (default) or "chess".
                  When "chess", all kernels and aiecc linking use xchesscc.
                  Requires Vitis/aietools in PATH.
    """

    # Repo root: iron/common/../../.. = three levels up from this file.
    base_dir: ClassVar[Path] = Path(__file__).parent.parent.parent

    build_dir: Path = field(default_factory=lambda: Path(os.getcwd()) / "build")
    mlir_verbose: bool = False
    compiler: str = "peano"

    @property
    def kernels_dir(self) -> Path:
        """C++ kernel sources bundled with the installed mlir-aie package.

        IRON_AIE_KERNELS_DIR overrides this to point at a local mlir-aie
        checkout for kernel development.
        """
        # Lazy: root_path() needs the package importable at call time.
        override = os.environ.get("IRON_AIE_KERNELS_DIR")
        if override:
            return Path(override)
        return Path(aie.utils.config.root_path()) / "include" / "aie_kernels"

    def __post_init__(self) -> None:
        """Normalize build_dir to a Path object."""
        self.build_dir = Path(self.build_dir)
        if self.compiler not in ("peano", "chess"):
            raise ValueError(
                f"compiler must be 'peano' or 'chess', got {self.compiler!r}"
            )

    @property
    def compilation_rules(self):
        """Return the ordered list of compilation rules for this context.

        Returns:
            List of ``CompilationRule`` instances configured for the current
            mlir-aie and peano installation paths.
        """
        mlir_aie_dir = Path(aie.utils.config.root_path())
        peano_dir = Path(aie.utils.config.peano_install_dir())
        use_chess = self.compiler == "chess"

        return [
            comp.FusePythonGeneratedMLIRCompilationRule(),
            comp.GenerateMLIRFromPythonCompilationRule(),
            comp.DownloadCompilationRule(),
            comp.KernelCompilationRule(peano_dir, mlir_aie_dir, use_chess=use_chess),
            comp.ArchiveCompilationRule(peano_dir, mlir_aie_dir),
            comp.AieccXclbinInstsCompilationRule(use_chess=use_chess),
            comp.AieccFullElfCompilationRule(use_chess=use_chess),
        ]
