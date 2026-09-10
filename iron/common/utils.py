# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.dialects.aie import get_target_model, WireBundle


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


# Widest wrap a DMA buffer descriptor's size field can encode. Not exposed by
# the Python bindings (AIETargetModel::getDmaBdWrapSizeBits is unbound), so it
# is written down here rather than in each design; gemv, repeat and mha all
# hardcoded the same 1023 independently.
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
