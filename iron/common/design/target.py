# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Target: the device, the kernel tree and the fusion prefix, as one handle."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from aie.iron import Buffer, WorkerRuntimeBarrier

from ..kernels import declare_kernel, target_arch


class Target:
    """What an overlay's ``design()`` is given besides the overlay itself.

    Carries the device, the kernel tree and the fusion prefix, and applies
    the prefix inside :meth:`kernel`, so an overlay never handles it.
    """

    def __init__(
        self,
        dev,
        kernels_dir,
        func_prefix: str = "",
        trace_size: int = 0,
        image: str = "elf",
    ):
        self.dev = dev
        self.kernels_dir = Path(kernels_dir)
        self.arch = target_arch(dev)  # "aie2" | "aie2p"
        self.func_prefix = func_prefix
        self.trace_size = trace_size
        # "elf": per-call values reach the array through the parameter
        # scratchpad. "xclbin": there is none (spike S2); they are dispatch-
        # time scalars of the sequence, and a core-read value is a resident
        # the sequence writes (bind it to the runtime-parameter buffer).
        self.image = image
        self.barriers: list[Any] = []

    def kernel_source(self, name: str):
        """``<kernels_dir>/<arch>/<name>.cc``: the per-architecture kernel tree."""
        return self.kernels_dir / self.arch / f"{name}.cc"

    def kernel(
        self,
        name: str,
        arg_types,
        *,
        source=None,
        compile_flags=(),
        bundled_sources=(),
        include_dirs=None,
        object_file_name=None,
        symbol_prefix=None,
    ):
        """Declare a kernel the array calls; the fusion prefix is applied here."""
        return declare_kernel(
            name,
            arg_types,
            source=source,
            func_prefix=self.func_prefix,
            compile_flags=list(compile_flags),
            include_dirs=include_dirs,
            object_file_name=object_file_name,
            bundled_sources=bundled_sources,
            symbol_prefix=symbol_prefix,
        )

    def barrier(self, initial_value: int = 0):
        """A worker/runtime barrier the preamble sets to 1 after writing residents."""
        b = WorkerRuntimeBarrier(initial_value)
        self.barriers.append(b)
        return b

    def rtp(self, arr_type, name: str | None = None, initial_value=None):
        """A runtime-parameter buffer a core reads and the preamble writes."""
        return Buffer(
            arr_type, name=name, initial_value=initial_value, use_write_rtp=True
        )
