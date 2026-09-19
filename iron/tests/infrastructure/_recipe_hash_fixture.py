# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A stand-in design callback for mlir_recipe_hash.py.

Needs to be a real function in a real file: DesignGenerator.source_file falls
back to inspect.getfile(fn), and a function defined inline in a test has
nothing meaningful to report there. It is never called -- the tests only hash
its identity and kwargs -- so its body is unreachable.
"""


def design(size, func_prefix="", dev=None):
    raise NotImplementedError("never called; only its identity is hashed")
