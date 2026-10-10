# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How a traced graph is packaged: the image and the boundaries.

A ``DispatchTime`` value, NPU1, or more than one boundary forces ``xclbin``,
one per step; otherwise the image is one full ELF. A fused sequence in an
xclbin has no proven construction and is refused.
"""

from __future__ import annotations

import dataclasses

from aie.dialects.aie import AIEArch

ELF = "elf"
XCLBIN = "xclbin"

each_step = "each_step"


@dataclasses.dataclass
class Plan:
    """What ``compile`` decided, and why."""

    image: str
    dispatch: str
    reasons: list
    values: list  # (name, kind, lowering)

    def report(self, name: str) -> str:
        lines = [f"{name}: image {self.image}, dispatch {self.dispatch!r}"]
        lines += [f"  {r}" for r in self.reasons]
        for vname, kind, lowering in self.values:
            lines.append(f"  {vname}: {kind}; {lowering}")
        return "\n".join(lines)


def full_elf(dev) -> bool:
    """Whether ``dev``'s architecture dispatches a full ELF."""
    # Inferred from source, untested on npu1: XRT sends an ELF with .pdi
    # sections as ERT_START_NPU_PREEMPT_ELF (XRT 2.25 xrt_elf.cpp:1031), which
    # amdxdna refuses without AIE2_PREEMPT, absent from npu1_regs.c:68-72.
    return dev.arch is AIEArch.AIE2p


def plan(dev, traced, boundaries=None, image: str | None = None) -> Plan:
    """Derive the image and the dispatch policy for ``traced`` on the device."""
    if image not in (None, ELF, XCLBIN):
        raise ValueError(f"image must be {ELF!r} or {XCLBIN!r}, got {image!r}")
    if boundaries not in (None, each_step):
        raise ValueError(f"boundaries must be None or each_step, got {boundaries!r}")
    shipped = [op for op in traced.operators if op.external is not None]
    if shipped:
        names = ", ".join(
            f"{type(op).__name__} ({op.external.filename})" for op in shipped
        )
        raise ValueError(
            f"{traced.name}: {names} runs a shipped image, which no graph image "
            f"builds; run it on its own with OperatorImage(op)"
        )

    forced: list[str] = []
    dispatch_values = [v for v in traced.values if v.kind == "dispatch"]
    if dispatch_values:
        names = ", ".join(v.name for v in dispatch_values)
        forced.append(
            f"{names}: a DispatchTime value; the sequence is generated per call"
        )
    if not full_elf(dev):
        forced.append(f"{dev.name} ({dev.arch}) has no full-ELF dispatch")
    if boundaries is not None:
        forced.append(f"boundaries={boundaries}: more than one dispatch")

    chosen = XCLBIN if forced else ELF
    if image == ELF and forced:
        raise ValueError(
            f"{traced.name}: image=elf is not possible here: " + "; ".join(forced)
        )
    if image is not None:
        chosen = image
    reasons = forced or ["one sequence, one configuration set: a full ELF"]

    # A forced xclbin takes the one xclbin form that is built.
    if chosen == XCLBIN and boundaries is None and forced:
        boundaries = each_step
        reasons = forced + [f"boundaries={each_step}: the xclbin form that is built"]

    if chosen == ELF:
        dispatch = "fused"
    elif boundaries == each_step:
        dispatch = "separate"
    else:
        raise NotImplementedError(
            f"{traced.name}: one fused sequence in an xclbin has no proven "
            f"construction yet; pass "
            f"boundaries=each_step, or package for NPU2 as an ELF"
        )

    values = []
    for v in traced.values:
        if v.kind == "scratchpad" and chosen == ELF:
            lowering = "patched through the parameter scratchpad"
        elif v.kind == "scratchpad":
            lowering = (
                "no scratchpad on an xclbin: a dispatch-time scalar; "
                "an offset use regenerates the stream, a core-read use is "
                "written into the array by the sequence"
            )
        else:
            lowering = "sizes, strides and offsets regenerated per call"
        values.append((v.name, v.kind, lowering))
    return Plan(chosen, dispatch, reasons, values)
