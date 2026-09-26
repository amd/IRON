# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device IRON generates for: mlir-aie's current device, bound."""

from __future__ import annotations

import aie.utils as aie_utils


def bound_device():
    """The device bound as the current one, binding the observed one first.

    Bound rather than merely inferred: the ``aie.iron.kernels`` factories
    read only a bound device, and fall back to aie2 without one, so a
    contract asked for before the first compile would otherwise describe
    aie2's kernel on an NPU2. Raises when no device is available at all.
    """
    dev = aie_utils.ensure_current_device()
    if dev is None:
        raise RuntimeError(
            "no NPU device is bound and none was found; bind one with "
            "aie.utils.set_current_device()"
        )
    return dev


def device_name(dev=None) -> str:
    """``"npu1"`` or ``"npu2"``: the name of ``dev``, or of the bound device."""
    dev = bound_device() if dev is None else dev
    # Upstream annotates Device.resolve() -> None; it returns the AIEDevice.
    return dev.resolve().name  # pyright: ignore
