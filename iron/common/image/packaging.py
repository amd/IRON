# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How a traced graph is packaged: the image and the boundaries.

Two arguments, both optional, and everything else derived and reported:

    net = decode.compile(dev)                          # full ELF on NPU2, per-step xclbin on NPU1
    net = decode.compile(dev, boundaries=each_step)    # one dispatch per step

The rules, in order: a ``DispatchTime`` value anywhere forces ``xclbin``
(its sequence is generated per call); a device without full-ELF dispatch
(:class:`DeviceSupport`; NPU1) forces ``xclbin``; more than one boundary
forces ``xclbin`` (one image, N kernels); otherwise ``elf``. Asking for ``elf`` where a rule forbids it is
an error naming the member, the boundaries or the device.

What the lowering builds today: ``elf`` is the fused ELF, ``xclbin``
with ``each_step`` is the chained per-operator xclbin, and an xclbin a
rule forces (NPU1, a ``DispatchTime`` value) takes ``each_step`` when no
boundaries are given. A fused sequence in an xclbin (and dispatches of
several steps on it) has no construction proven on a device yet, and is
refused rather than built wrong; its construction is shelved on the branch
``claude/iron-pr215-step5-extras``. An xclbin run has no parameter
scratchpad (XRT implements ``get_ctrl_scratchpad_bo`` only for a full-ELF
module), so on that image every per-call value is a dispatch-time scalar
of its kernel: an offset use
regenerates the kernel's stream per call, a core-read use is written into
the array by the sequence.
"""

from __future__ import annotations

import dataclasses

from aie.dialects._aie_enum_gen import AIEArch

ELF = "elf"
XCLBIN = "xclbin"

each_step = "each_step"


@dataclasses.dataclass(frozen=True)
class Mode:
    """One way to package a runlist: its image, and how its steps dispatch.

    Each mode has its own boundary costs, measured per device (a
    :class:`~iron.common.graph.narrowing.Calibration` of this ``name``):
    under ``fused`` the whole runlist is one dispatch and a boundary is a
    configure; under ``separate`` every step is a dispatch of its own.
    """

    image: str
    dispatch: str

    @property
    def name(self) -> str:
        return {ELF: "elf", XCLBIN: each_step}[self.image]

    @property
    def packs(self) -> bool:
        """Whether designs may share a device configuration (co-residence):
        only inside one dispatch."""
        return self.dispatch == "fused"

    @property
    def boundaries(self) -> str | None:
        """What ``compile(boundaries=)`` takes for this mode."""
        return None if self.dispatch == "fused" else each_step


FUSED = Mode(ELF, "fused")
EACH_STEP = Mode(XCLBIN, "separate")


def modes(support: DeviceSupport, traced) -> list[Mode]:
    """The modes ``traced`` can be packaged in on the device, by the rules
    :func:`plan` applies."""
    out = []
    for mode in (FUSED, EACH_STEP):
        try:
            plan(support, traced, mode.boundaries, mode.image)
        except (ValueError, NotImplementedError):
            continue
        out.append(mode)
    return out


@dataclasses.dataclass(frozen=True)
class DeviceSupport:
    """What one device generation can dispatch, whatever its column count."""

    name: str
    full_elf: bool


# npu1's full_elf is INFERRED from source and has not been tested on
# hardware. IRON's npu1 ELF carries .pdi sections, and XRT sends any such
# ELF as ERT_START_NPU_PREEMPT_ELF (XRT 2.25 xrt_elf.cpp:1031-1041). The
# amdxdna driver refuses that opcode unless the firmware has AIE2_PREEMPT
# (2.25 aie2_message.c:1006-1009), and npu1's feature table never lists it
# (npu1_regs.c:68-72; npu4_regs.c:96 does, from firmware 6.12). To verify
# it: set True, then run a full-ELF test on an npu1 machine.
NPU1_SUPPORT = DeviceSupport("npu1", full_elf=False)
NPU2_SUPPORT = DeviceSupport("npu2", full_elf=True)

# Keyed on the architecture rather than the class or the name: NPU1Col1 is
# not an NPU1, and it resolves to "npu1_1col".
_SUPPORT = {AIEArch.AIE2: NPU1_SUPPORT, AIEArch.AIE2p: NPU2_SUPPORT}


def device_support(dev) -> DeviceSupport:
    """The :class:`DeviceSupport` for ``dev``, an ``aie.iron.device.Device``."""
    if dev is None:
        raise ValueError("no current device; call aie.utils.set_current_device")
    try:
        return _SUPPORT[dev.arch]
    except KeyError:
        raise ValueError(f"no dispatch support recorded for {dev.arch}") from None


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


def plan(
    support: DeviceSupport, traced, boundaries=None, image: str | None = None
) -> Plan:
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
    if not support.full_elf:
        forced.append(f"{support.name} has no full-ELF dispatch")
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

    # A forced xclbin with no boundary choice takes the one xclbin form that
    # is built; asking for an xclbin outright still names what is missing.
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
