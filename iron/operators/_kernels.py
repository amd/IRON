# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How an iron/operators design declares the kernel it calls.

One declaration, not two. A design used to name a function *and* the object
file it lives in, while the operator separately described how to build that
object -- with the file name spelled out independently in both places and
nothing keeping them in step. ``ExternalFunction`` is both halves at once:
upstream compiles the source and names the object from its content.

Constructing it here, inside the design, is required rather than stylistic.
An ``ExternalFunction`` registers itself into a process-global set that
``CompilableDesign`` clears when it begins generating, so one built earlier --
in the operator, say -- is discarded and its object never compiled.
"""

from pathlib import Path

import aie.utils.config
from aie.iron import ExternalFunction, Kernel

from iron.common.device_utils import get_kernel_dir


def runtime_include_dirs() -> list[str]:
    """The aie_runtime_lib headers a kernel is compiled against."""
    return [
        str(
            Path(aie.utils.config.root_path())
            / "aie_runtime_lib"
            / get_kernel_dir().upper()
        )
    ]


def declare_kernel(
    name,
    arg_types,
    *,
    source=None,
    prebuilt=None,
    func_prefix="",
    compile_flags=(),
    include_dirs=None,
    object_file_name=None,
):
    """Declare the kernel a design calls, building it unless it is prebuilt.

    ``prebuilt`` names an object or archive that already exists and is linked
    by name -- the aie2 ``lut_based_ops`` case, whose tables are referenced
    from C++ with no MLIR call site, so nothing can discover them by tracing
    calls. Everywhere else ``source`` is compiled by upstream.

    ``object_file_name`` is for a source that defines more than one entry point
    the design calls. Left to default, each declaration is named for its own
    symbol and so gets its own object -- two compiles of one translation unit,
    each defining *both* symbols, which is a duplicate definition at link.
    Pointing them at one object name instead makes them share it: identical
    source and flags give an identical content digest, so upstream neither
    reports a collision nor compiles twice.

    ``func_prefix`` is IRON's fusion prefix and arrives with its trailing
    underscore ("op0_"). ``ExternalFunction`` joins with an underscore of its
    own, for the symbol name and for the rename pass alike, so it is stripped
    here; handing it over whole yields "op0__matvec".
    """
    if prebuilt is not None:
        return Kernel(f"{func_prefix}{name}", f"{func_prefix}{prebuilt}", arg_types)
    prefix = func_prefix.rstrip("_") or None
    if object_file_name is not None and prefix:
        # Upstream names a defaulted object after the prefixed symbol; an
        # explicit one is taken as given, so the prefix has to be applied here
        # or two fused operators would share one object.
        object_file_name = f"{prefix}_{object_file_name}"
    return ExternalFunction(
        name,
        object_file_name=object_file_name,
        source_file=str(source),
        arg_types=arg_types,
        include_dirs=runtime_include_dirs() if include_dirs is None else include_dirs,
        compile_flags=list(compile_flags),
        symbol_prefix=prefix,
    )
