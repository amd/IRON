# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a design becomes once it is built, and how it is called.

``sequence`` drives one run: ``packaging`` picks the image, ``allocator``
places its buffers, ``compose`` and ``coresidence`` compose the designs,
``link`` compiles them and ``callable`` runs the result; ``standalone`` is
one operator on its own (``Operator.compile``).
"""

from .coresidence import AdjacentPacking

__all__ = [
    "AdjacentPacking",
]
