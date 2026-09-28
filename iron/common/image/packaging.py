# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How a traced graph is packaged: the image and the boundaries.

Two arguments, both optional, and everything else derived and reported:

    net = decode.compile(dev)                          # full ELF on NPU2, per-step xclbin on NPU1
    net = decode.compile(dev, boundaries=each_step)    # one dispatch per step

The rules, in order: a ``DispatchTime`` value anywhere forces ``xclbin``
(its sequence is generated per call); NPU1 forces ``xclbin`` (no full-ELF
dispatch); more than one boundary forces ``xclbin`` (one image, N
kernels); otherwise ``elf``. Asking for ``elf`` where a rule forbids it is
an error naming the member, the boundaries or the device.

What the lowering builds today: ``elf`` is the fused ELF, ``xclbin``
with ``each_step`` is the chained per-operator xclbin. A fused sequence
in an xclbin (and dispatches of several steps on it) has no proven
construction and is refused rather than built wrong; a draft is shelved on
the branch ``claude/iron-pr215-step5-extras``. An xclbin run has no
parameter scratchpad (XRT's ``get_ctrl_scratchpad_bo`` serves a module run
only), so on that image every per-call value is a dispatch-time scalar of
its kernel: an offset use regenerates the kernel's stream per call, a
core-read use is written into the array by the sequence (an ``rtp_write``
of the scalar).
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


def plan(dev, traced, boundaries=None, image: str | None = None) -> Plan:
    """Derive the image and the dispatch policy for ``traced`` on the device."""
    if image not in (None, ELF, XCLBIN):
        raise ValueError(f"image must be {ELF!r} or {XCLBIN!r}, got {image!r}")
    if boundaries not in (None, each_step):
        raise ValueError(f"boundaries must be None or each_step, got {boundaries!r}")

    forced: list[str] = []
    dispatch_values = [v for v in traced.values if v.kind == "dispatch"]
    if dispatch_values:
        names = ", ".join(v.name for v in dispatch_values)
        forced.append(
            f"{names}: a DispatchTime value; the sequence is generated per call"
        )
    if dev.arch is not AIEArch.AIE2p:
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
