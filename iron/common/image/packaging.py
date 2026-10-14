# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How a traced graph is packaged: one full ELF, or an xclbin per step.

``full_elf`` is mlir-aie's choice of the same name. ``None`` derives it: a
``DispatchTime`` value, NPU1 or ``check`` forces an xclbin, one dispatch per
step; otherwise the image is one full ELF.
"""

from __future__ import annotations

import dataclasses
import enum

from aie.dialects.aie import AIEArch


class Kind(enum.Enum):
    """How a graph's per-call value reaches the device: its annotation's marker."""

    SCRATCHPAD = "iron.scratchpad"
    CARRIED = "iron.carried"
    DISPATCH_TIME = "aie.dispatch_time"


@dataclasses.dataclass
class Plan:
    """What ``compile`` decided, and why."""

    full_elf: bool
    reasons: list
    values: list  # (name, kind, lowering)

    def report(self, name: str) -> str:
        image = "one full ELF" if self.full_elf else "an xclbin per step"
        lines = [f"{name}: {image}"]
        lines += [f"  {r}" for r in self.reasons]
        for vname, kind, lowering in self.values:
            lines.append(f"  {vname}: {kind}; {lowering}")
        return "\n".join(lines)


def dispatches_full_elf(dev) -> bool:
    """Whether ``dev``'s architecture dispatches a full ELF."""
    # Inferred from source, untested on npu1: XRT sends an ELF with .pdi
    # sections as ERT_START_NPU_PREEMPT_ELF (XRT 2.25 xrt_elf.cpp:1031), which
    # amdxdna refuses without AIE2_PREEMPT, absent from npu1_regs.c:68-72.
    return dev.arch is AIEArch.AIE2p


def plan(dev, traced, full_elf: bool | None = None, check: bool = False) -> Plan:
    """Derive the packaging for ``traced`` on the device.

    Args:
        check: Each step is checked against its reference on its own
            dispatch, which an xclbin per step gives.

    Raises:
        ValueError: ``full_elf`` is asked for where a value, the device or
            ``check`` forbids it, or the graph runs a shipped image.
    """
    shipped = [op for op in traced.operators if op.external is not None]
    if shipped:
        names = ", ".join(
            f"{type(op).__name__} ({op.external.filename})" for op in shipped
        )
        raise ValueError(
            f"{traced.name}: {names} runs a shipped image, which no graph image "
            f"builds; call it on its own, outside a graph"
        )

    forced: list[str] = []
    dispatch_values = [v for v in traced.values if v.kind is Kind.DISPATCH_TIME]
    if dispatch_values:
        names = ", ".join(v.name for v in dispatch_values)
        forced.append(
            f"{names}: a DispatchTime value; the sequence is generated per call"
        )
    if not dispatches_full_elf(dev):
        forced.append(f"{dev.name} ({dev.arch}) has no full-ELF dispatch")
    if check:
        forced.append("check=True: each step its own dispatch, checked")
    if full_elf and forced:
        raise ValueError(
            f"{traced.name}: full_elf=True is not possible here: " + "; ".join(forced)
        )

    if full_elf is None:
        full_elf = not forced
        reasons = forced or ["one sequence, one configuration set: a full ELF"]
    else:
        reasons = [f"full_elf={full_elf}: asked for", *forced]

    values = []
    for v in traced.values:
        if v.kind is Kind.DISPATCH_TIME:
            lowering = "sizes, strides and offsets regenerated per call"
        elif full_elf:
            lowering = "patched through the parameter scratchpad"
        else:
            lowering = (
                "no scratchpad on an xclbin: a dispatch-time scalar; "
                "an offset use regenerates the stream, a core-read use is "
                "written into the array by the sequence"
            )
        values.append((v.name, v.kind.value, lowering))
    return Plan(full_elf, reasons, values)
