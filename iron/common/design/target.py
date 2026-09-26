# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Target: the device and the kernel tree, as one handle."""

from __future__ import annotations

from functools import partial
from pathlib import Path
from typing import Any

from aie.iron import Buffer, WorkerRuntimeBarrier

from ..kernels import declare_kernel, target_arch


class Target:
    """What an operator's ``array()`` is given besides the operator itself.

    Carries the device and the kernel tree. ``kernel`` is
    :func:`~iron.common.kernels.declare_kernel`, whose digest prefix keeps
    kernels apart when designs are fused, whatever else is fused with them;
    ``rtp`` is a runtime-parameter :class:`~aie.iron.Buffer`.
    """

    def __init__(
        self,
        dev,
        kernels_dir,
        trace_size: int = 0,
        image: str = "elf",
    ):
        self.dev = dev
        self.kernels_dir = Path(kernels_dir)
        self.arch = target_arch(dev)  # "aie2" | "aie2p"
        self.trace_size = trace_size
        # "elf": per-call values reach the array through the parameter
        # scratchpad. "xclbin": there is none (spike S2); they are dispatch-
        # time scalars of the sequence, and a core-read value is a resident
        # the sequence writes (bind it to the runtime-parameter buffer).
        self.image = image
        # The function itself rather than a method: a method would restate
        # every declare_kernel parameter, and would have to track them.
        self.kernel = declare_kernel
        self.rtp = partial(Buffer, use_write_rtp=True)
        self.barriers: list[Any] = []

    def kernel_source(self, name: str):
        """``<kernels_dir>/<arch>/<name>.cc``: the per-architecture kernel tree."""
        return self.kernels_dir / self.arch / f"{name}.cc"

    def barrier(self, initial_value: int = 0):
        """A worker/runtime barrier the preamble sets to 1 after writing residents."""
        b = WorkerRuntimeBarrier(initial_value)
        self.barriers.append(b)
        return b
