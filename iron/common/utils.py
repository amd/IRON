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
