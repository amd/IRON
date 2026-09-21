# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How a traced graph is packaged: the image and the boundaries.

Two arguments, both optional, and everything else derived and reported
(OPERATOR_MODEL_PLAN.md §8):

    net = decode.compile(dev)                          # full ELF on NPU2, per-step xclbin on NPU1
    net = decode.compile(dev, image="xclbin")          # one fused sequence in an xclbin (spike S1)
    net = decode.compile(dev, boundaries=chunks(8))    # dispatches of eight steps (spike S1)
    net = decode.compile(dev, boundaries=each_step)    # one dispatch per step

The rules, in order: a ``DispatchTime`` value anywhere forces ``xclbin``
(its sequence is generated per call); NPU1 forces ``xclbin`` (no full-ELF
dispatch); more than one boundary forces ``xclbin`` (one image, N
kernels); otherwise ``elf``. Asking for ``elf`` where a rule forbids it is
an error naming the member, the boundaries or the device.

What the lowering builds: ``elf`` is the fused ELF; ``xclbin`` with
``each_step`` is the chained per-operator xclbin; ``xclbin`` with
``chunks(n)``, or alone, is the chained chunked xclbin (a fused
sub-sequence per kernel, its configuration switches expanded), which is
spike S1's construction: it builds, and whether it runs is S1's question.
An xclbin run has no parameter scratchpad (spike S2, from XRT's source),
so on that image every per-call value is a dispatch-time scalar of its
kernel (§6): an offset use regenerates the kernel's stream per call, a
core-read use is written into the array by the sequence (spike S3). Built
for ``each_step``; a chunked image with values waits on the fused
sequence forwarding its chunks' scalars.
"""

from __future__ import annotations

import dataclasses

ELF = "elf"
XCLBIN = "xclbin"

each_step = "each_step"


@dataclasses.dataclass(frozen=True)
class Chunks:
    """A boundary every ``n`` steps."""

    n: int

    def __post_init__(self):
        if self.n < 1:
            raise ValueError("chunks(n) needs n >= 1")


def chunks(n: int) -> Chunks:
    return Chunks(n)


@dataclasses.dataclass
class Plan:
    """What ``compile`` decided, and why."""

    image: str
    dispatch: object  # a dispatch name, or a SequenceDispatch instance
    reasons: list
    values: list  # (name, kind, lowering)

    def report(self, name: str) -> str:
        spelled = getattr(self.dispatch, "name", self.dispatch)
        if getattr(self.dispatch, "n", None):
            spelled = f"{spelled}({self.dispatch.n})"
        lines = [f"{name}: image {self.image}, dispatch {spelled!r}"]
        lines += [f"  {r}" for r in self.reasons]
        for vname, kind, lowering in self.values:
            lines.append(f"  {vname}: {kind}; {lowering}")
        return "\n".join(lines)


def plan(device_name: str, traced, boundaries=None, image: str | None = None) -> Plan:
    """Derive the image and the dispatch policy for ``traced`` on the device."""
    if image not in (None, ELF, XCLBIN):
        raise ValueError(f"image must be {ELF!r} or {XCLBIN!r}, got {image!r}")
    if boundaries not in (None, each_step) and not isinstance(boundaries, Chunks):
        raise ValueError(
            f"boundaries must be None, each_step or chunks(n), got {boundaries!r}"
        )

    forced: list[str] = []
    dispatch_values = [v for v in traced.values if v.kind == "dispatch"]
    if dispatch_values:
        names = ", ".join(v.name for v in dispatch_values)
        forced.append(
            f"{names}: a DispatchTime value; the sequence is generated per call"
        )
    if device_name == "npu1":
        forced.append("npu1 has no full-ELF dispatch")
    if boundaries is not None:
        forced.append(f"boundaries={_spell(boundaries)}: more than one dispatch")

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
        from .sequence import ChunkedDispatch

        dispatch = ChunkedDispatch(None if boundaries is None else boundaries.n)

    values = []
    for v in traced.values:
        if v.kind == "scratchpad" and chosen == ELF:
            lowering = "patched through the parameter scratchpad"
        elif v.kind == "scratchpad":
            lowering = (
                "no scratchpad on an xclbin (spike S2): a dispatch-time scalar; "
                "an offset use regenerates the stream, a core-read use is "
                "written into the array by the sequence (spike S3)"
            )
        else:
            lowering = "sizes, strides and offsets regenerated per call"
        values.append((v.name, v.kind, lowering))
    if values and chosen == XCLBIN and boundaries != each_step:
        raise NotImplementedError(
            f"{traced.name}: per-call values on a chunked image are not built "
            f"yet (the fused sequence must forward its chunks' dispatch scalars); "
            f"pass boundaries=each_step"
        )
    return Plan(chosen, dispatch, reasons, values)


def _spell(boundaries) -> str:
    return f"chunks({boundaries.n})" if isinstance(boundaries, Chunks) else boundaries
