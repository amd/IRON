# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Steps of sequences built by hand, over buffers named in the test."""

from iron.common.image.step import BufferRef, SequenceStep


def steps(*entries) -> list[SequenceStep]:
    """Return each ``(op, *buffers)`` as a step.

    A name is the whole of its buffer and a ``BufferRef`` a part.
    """
    return [
        SequenceStep(
            op, tuple(b if isinstance(b, BufferRef) else BufferRef(b) for b in buffers)
        )
        for op, *buffers in entries
    ]
