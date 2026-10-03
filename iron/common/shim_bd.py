# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""ShimNOC DMA BD field bounds, and the run-splitting they force on operators.

One hardware invariant, one implementation. `gemv` and `repeat` each derived their own
version of this split; they agreed on the objective and differed on the search direction and
on whether the granule came from the dtype, which is the kind of divergence that only shows
up as a BD verifier error on some shape nobody tried.
"""

import numpy as np

# verifyStridesWraps (AIEXDialect.cpp) computes these per tile type from the target model:
# ShimNOC wrap=10-bit/step=20-bit, MemTile wrap=10-bit/step=17-bit, CoreTile wrap=8-bit/
# step=13-bit (getDmaBdWrapBits/getDmaBdStepBits). These are scoped to ShimNOC on purpose --
# reusing them for a MemTile or CoreTile transfer would silently under- or over-shoot the
# real limit. Callers that only emit shim BDs (a runtime sequence's fill/drain moving
# L3<->L1 across the shim) are the ones this fits.
#
# Neither accessor reaches Python today: getDmaBdWrapBits/getDmaBdStepBits have no CAPI or
# nanobind binding, and getAddressGenGranularity has a CAPI entry
# (aieGetTargetModelAddressGenGranularity) but isn't bound into aie.dialects.aie.AIETargetModel
# either, so all three stay hard-coded here until one of those lands.
SHIM_MAX_WRAP = 1023  # (1 << 10) - 1
SHIM_MAX_STRIDE = (1 << 20) - 1
# getAddressGenGranularity(); same on every AIE1/AIE2 target model today.
SHIM_ADDR_GRAN_BITS = 32


def shim_gran_elems(dtype) -> int:
    """Elements per shim DMA address-generation granule.

    Accepts either a `np.dtype[T]` generic (as the operator designs carry it) or a plain
    dtype-like. Mirrors what verifyStridesWraps computes from getAddressGenGranularity() and
    the memref's actual element type, so callers get the granule for THEIR dtype instead of
    a hard-coded bf16 value.
    """
    args = getattr(dtype, "__args__", None)
    elem = np.dtype(args[0]) if args else np.dtype(dtype)
    elem_bits = elem.itemsize * 8
    if elem_bits >= SHIM_ADDR_GRAN_BITS:
        # One element is already a whole number of granules, so every count is aligned.
        assert elem_bits % SHIM_ADDR_GRAN_BITS == 0, (
            f"{dtype} is {elem_bits}-bit, which is not a whole number of "
            f"{SHIM_ADDR_GRAN_BITS}-bit shim address-generation granules"
        )
        return 1
    assert SHIM_ADDR_GRAN_BITS % elem_bits == 0, (
        f"{dtype} is {elem_bits}-bit, which does not evenly divide the "
        f"{SHIM_ADDR_GRAN_BITS}-bit shim address-generation granularity"
    )
    return SHIM_ADDR_GRAN_BITS // elem_bits


def split_run(run, lim=SHIM_MAX_WRAP, gran=2):
    """Factor a contiguous run into (hi, lo), both <= lim and lo a multiple of gran
    (the address-granularity-aligned inner size), lo maximal. None if no such split exists.

    Returning None rather than raising is deliberate: the callers disagree on what to do
    about it. gemv has a slower legal path and falls back to it; repeat does not and raises.
    """
    lo_start = (lim // gran) * gran
    for lo in range(lo_start, 0, -gran):
        if run % lo == 0 and (run // lo) <= lim:
            return (run // lo, lo)
    return None
