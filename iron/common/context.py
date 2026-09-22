# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar
import os

import aie.utils.config


@dataclass
class AIEContext:
    """What a build is given besides the operator: where things go, how loud.

    ``build_dir`` holds what is fetched rather than built (a foreign
    overlay's image). Built artifacts live in mlir-aie's JIT cache, keyed on
    content; ``record`` says whether the :class:`~iron.common.artifacts.Artifacts`
    record of an image is also written beside it (``"disk"``) or only kept
    in memory (``"memory"``, the default).
    """

    # Repo root: iron/common/../../.. = three levels up from this file.
    base_dir: ClassVar[Path] = Path(__file__).parent.parent.parent
    _default: ClassVar["AIEContext | None"] = None

    build_dir: Path = field(default_factory=lambda: Path(os.getcwd()) / "build")
    mlir_verbose: bool = False
    record: str = "memory"
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
        self.build_dir = Path(self.build_dir)
        if self.record not in ("memory", "disk"):
            raise ValueError(f"record must be 'memory' or 'disk', got {self.record!r}")
        if self.compiler not in ("peano", "chess"):
            raise ValueError(
                f"compiler must be 'peano' or 'chess', got {self.compiler!r}"
            )

    @property
    def use_chess(self) -> bool:
        """Whether kernels are compiled with xchesscc rather than Peano."""
        return self.compiler == "chess"

    @classmethod
    def default(cls) -> "AIEContext":
        """The process-wide context an operator gets when given none."""
        if cls._default is None:
            cls._default = cls()
        return cls._default
