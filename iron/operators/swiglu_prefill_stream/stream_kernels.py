# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON-authored operand layouts for the stream-dse SwiGLU-prefill kernels.

stream-dse selects an AIE kernel per computation node and uses each kernel's
``operand_layouts()`` to drive the DMA tiling emitted into the design MLIR.
:func:`iron_kernels` returns the ``optimize_allocation_co(kernels=...)`` override
that keeps every kernel stream would build but replaces its operand layouts with
the ones defined here -- the single source of truth -- converted to stream's
tiled-strided layout via :meth:`iron.common.TiledStridedLayout.to_snaxc`. IRON
owns the layouts; stream owns construction, symbol names and the MLIR rewrite.

Each override is stream's own kernel, re-typed to a subclass that overrides only
``operand_layouts()``: the kernel is still built by stream's ``AIEKernels``
factory (so its constructor signature is inherited, not re-declared here), then
its ``__class__`` is swapped. The subclasses are module-level so the kernels stay
picklable (stream stores them on the mapping).

stream / snaxc / xdsl are imported at module load, so this module is only
importable where the AIE codegen toolchain is installed; it is imported only from
``stream_design.py``.
"""

from __future__ import annotations

from typing import Any, Callable

from stream.compiler.kernels.eltwise_mul import EltwiseMulKernel
from stream.compiler.kernels.gemm import GemmKernel
from stream.compiler.kernels.silu import SiluKernel

from iron.common import TiledStridedLayout, tiled_2d

# Intrinsic MAC tile dimensions of the aie2p kernels stream-dse targets; the
# operand layouts below are the contract the generated DMAs and the compiled
# kernel objects must agree on.
R, S, T = 4, 8, 8


def _gemm_layouts(m: int, k: int, n: int) -> tuple[TiledStridedLayout, ...]:
    return (tiled_2d(m, k, R, S), tiled_2d(k, n, S, T), tiled_2d(m, n, R, T))


def _elementwise_layouts(
    count: int, tile: tuple[int, int] = (32, 64)
) -> tuple[TiledStridedLayout, ...]:
    return (tiled_2d(*tile, R, T),) * count


class _IronGemmKernel(GemmKernel):
    def operand_layouts(self):
        return [tsl.to_snaxc() for tsl in _gemm_layouts(self.m, self.k, self.n)]


class _IronSiluKernel(SiluKernel):
    def operand_layouts(self):
        return [tsl.to_snaxc() for tsl in _elementwise_layouts(2)]


class _IronEltwiseMulKernel(EltwiseMulKernel):
    def operand_layouts(self):
        return [tsl.to_snaxc() for tsl in _elementwise_layouts(3)]


# stream AIEKernels name -> IRON subclass overriding operand_layouts().
_OVERRIDES: dict[str, type] = {
    "gemm": _IronGemmKernel,
    "silu": _IronSiluKernel,
    "eltwise_mul": _IronEltwiseMulKernel,
}


def iron_kernels() -> dict[str, Callable[..., Any]]:
    """Return the ``optimize_allocation_co(kernels=...)`` override registry.

    Only kernels for which IRON defines layouts are overridden; any other kernel
    stream needs falls through to its built-in ``AIEKernels`` entry.
    """
    from stream.compiler.kernels import AIEKernels

    def override(factory: Callable[..., Any], cls: type) -> Callable[..., Any]:
        def make(*args: Any, **kwargs: Any) -> Any:
            kernel = factory(*args, **kwargs)
            kernel.__class__ = cls
            return kernel

        return make

    return {
        name: override(AIEKernels[name], cls)
        for name, cls in _OVERRIDES.items()
        if name in AIEKernels
    }
