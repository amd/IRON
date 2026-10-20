# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A runtime sequence as a real build generates it, and its shim tasks."""

import re
from typing import NamedTuple

from aie.iron import Program

from iron.common import Operator
from iron.common.design import BuiltArray, OperatorDesign, OperatorRuntime


class Task(NamedTuple):
    """One shim task of a generated sequence, as its text gives it. The fifos
    are unnamed (mlir-aie's DeviceConfiguration names them), so a test finds
    a task by the handle it was built from, or by its argument and offset.
    """

    ssa: int
    lane: str
    arg: int
    offset: int | str  # a runtime offset's SSA name
    sizes: str
    strides: str
    length_parameter: str  # the patched length's symbol, or ""
    length_unit: str  # the elements per unit of it, or ""
    offset_parameter: str  # the patched offset's symbol, or ""
    attributes: str


_TASK = re.compile(
    r"%(\d+) = aiex\.dma_configure_task_for @(\w+) (?:repeat %\w+ : \w+ )?\{\s*"
    r"aie\.dma_bd\(%arg(\d+) : \S+ offset = (\d+|%\w+ : i64) (?:len = %?\w+ )?"
    r"sizes = \[([^\]]*)\] strides = \[([^\]]*)\]\)"
    r"(?: \{(?:length_parameter = @(\w+), length_unit = (\d+) : i32)?(?:, )?"
    r"(?:offset_parameter = @(\w+))?\})?"
    r"\s*aie\.end\s*\}(?: \{([^}]*)\})?"
)


def _tasks(module) -> tuple[str, list[Task]]:
    """``module``'s runtime sequence and its shim tasks in order."""
    text = str(module)
    text = text[text.index("aie.runtime_sequence") :]
    return text, [
        Task(
            int(ssa), lane, int(arg), int(offset) if offset.isdigit() else offset, *rest
        )
        for ssa, lane, arg, offset, *rest in _TASK.findall(text)
    ]


def generated_sequence(op, full_elf=True) -> tuple[str, list[Task]]:
    """The runtime sequence ``op`` builds to, and its shim tasks in order.

    An xclbin's per-call values are its dispatch parameters, which only the
    design's generator declares, so it is generated as it would be compiled.
    """
    if full_elf:
        return _tasks(OperatorDesign(op).module())
    return _tasks(OperatorDesign(op, full_elf=False).compilable().generate_mlir())


def built(op) -> tuple[str, list[Task], Operator]:
    """``generated_sequence``'s full ELF build, alongside the resolved copy
    of ``op`` whose operands' lanes were bound to build it, to match a
    task's ``lane`` back to the handle that moved it.
    """
    array = BuiltArray(OperatorDesign(op))
    prog = Program(
        array.op.array_device(),
        OperatorRuntime(array.op, array.built),
        workers=array.workers,
    )
    return *_tasks(prog.resolve_program()), array.op
