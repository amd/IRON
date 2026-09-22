# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.dialects.aie import get_target_model, WireBundle


# One bank of a core's local memory. AIE2 and AIE2P both have eight 8 KB
# banks, and a fifo object spanning more than one bank cannot be
# double-buffered in what is left; the target model exposes the total
# (get_local_memory_size) but not the banking, so the figure is named here
# rather than spelled at each use.
L1_BANK_BYTES = 8192


def bank_elements(dtype) -> int:
    """Elements of ``dtype`` in one local-memory bank: the largest line a core
    holds at a fifo depth of two."""
    import numpy as np

    return L1_BANK_BYTES // np.dtype(dtype).itemsize


def get_shim_dma_limit(dev) -> int:
    """Return the total number of ShimDMA output channels available on the device.

    Each shim tile exposes a fixed number of DMA source connections; summing
    across all shim tiles gives the device-wide ShimDMA budget.
    """
    tm = get_target_model(dev.resolve())
    return sum(
        tm.get_num_source_shim_mux_connections(col, row, WireBundle.DMA)
        for col in range(tm.columns())
        for row in range(tm.rows())
        if tm.is_shim_noc_or_pl_tile(col, row)
    )


def serialize_param(v: object) -> str:
    """A parameter value as a short, filesystem-safe token for labels."""
    if isinstance(v, bool):
        return str(int(v))
    if isinstance(v, float):
        return float_to_name(v)
    if isinstance(v, (list, tuple)):
        return "x".join(str(x) for x in v)
    return str(v)


def float_to_name(v: float) -> str:
    """Convert a float to a filesystem-safe string for use in operator names.

    Uses repr() for the shortest exact round-trip representation, then sanitizes
    characters that are problematic in filenames or shell scripts, for instance:
      '.' -> 'p'  (decimal point)
      '-' -> 'n'  (negative sign / negative exponent)
      '+' -> ''   (positive exponent, redundant)

    Examples:
      3.0   -> '3p0'
      0.01  -> '0p01'
      -0.5  -> 'n0p5'
      1e-10 -> '1en10'
    """
    return repr(v).replace(".", "p").replace("-", "n").replace("+", "")


# Widest wrap a shim or mem tile DMA buffer descriptor's size field can encode.
# Not exposed by the Python bindings (AIETargetModel::getDmaBdWrapBits is
# unbound), so it is written down here rather than in each design; gemv,
# repeat and mha all hardcoded the same 1023 independently.
#
# This is the same 10 bits on every target model this repo builds for --
# BaseNPU1TargetModel and BaseNPU2TargetModel both inherit it unmodified from
# AIE2TargetModel::getDmaBdWrapBits, which does not override it per device --
# so callers do not need to look it up per-device. It is NOT the same for
# every tile type, though: core tiles get an 8-bit wrap (max 255), not 10-bit.
# This constant is only valid for shim/mem tile descriptors, which is what
# every current caller (gemv, repeat, mha, flm.GEMM) uses it for.
DMA_BD_MAX_WRAP = (1 << 10) - 1


def split_run(run: int, max_wrap: int = DMA_BD_MAX_WRAP) -> list[tuple[int, int]]:
    """Encode a contiguous run of ``run`` elements as BD (size, stride) dims.

    One dimension suffices while the run fits the BD's size field; a longer run
    splits into two at the cost of one of the four available dimensions.

        >>> split_run(512)
        [(512, 1)]
        >>> split_run(2048)
        [(2, 1024), (1024, 1)]
    """
    if run <= max_wrap:
        return [(run, 1)]
    if run % 2:
        raise ValueError(f"cannot split an odd run ({run}) exceeding {max_wrap}")
    return [(2, run // 2), (run // 2, 1)]
