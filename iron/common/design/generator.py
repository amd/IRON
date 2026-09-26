# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""DesignGenerator: the callable a compile runs for one design's MLIR."""

from __future__ import annotations

import dataclasses
from pathlib import Path
from typing import Callable


@dataclasses.dataclass
class DesignGenerator:
    """A design function and the arguments it is generated with.

    ``fn`` is the function (an operator's design is ``build_design`` over the
    operator); a design loaded from a file names ``source_path`` and
    ``fn_name`` instead (swiglu_prefill_stream's exported text). Called for
    its MLIR text; ``resolve()`` hands ``CompilableDesign`` the function and
    its keyword arguments to run inside ``compile()``.
    """

    fn: Callable | None = None
    kwargs: dict = dataclasses.field(default_factory=dict)
    source_path: Path | None = None
    fn_name: str | None = None
    args: tuple = ()

    def resolve(self) -> tuple[Callable, tuple, dict]:
        if self.fn is not None:
            return self.fn, self.args, self.kwargs
        assert self.source_path is not None and self.fn_name is not None
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            self.source_path.name, self.source_path
        )
        assert spec is not None and spec.loader is not None, self.source_path
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, self.fn_name), self.args, self.kwargs

    def __call__(self) -> str:
        fn, args, kwargs = self.resolve()
        return str(fn(*args, **kwargs))
