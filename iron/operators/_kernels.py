# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How an iron/operators design declares the kernel it calls.

One declaration, not two: ``ExternalFunction`` is the symbol and the object
at once, and upstream compiles the source and names the object from its
content, so no file name is spelled out twice.

Constructing it here, inside the design, is required rather than stylistic.
An ``ExternalFunction`` registers itself into a process-global set that
``CompilableDesign`` clears when it begins generating, so one built earlier --
in the operator, say -- is discarded and its object never compiled.
"""

import os
from pathlib import Path

import aie.utils as aie_utils
import aie.utils.config
from aie.iron import ExternalFunction
from aie.utils.compile.utils import resolve_target_arch

# The IRON checkout: iron/operators/../.. = two levels up from this file.
_REPO = Path(__file__).parent.parent.parent


def kernels_dir() -> Path:
    """C++ kernel sources bundled with the installed mlir-aie package.

    ``IRON_AIE_KERNELS_DIR`` points this at a local mlir-aie checkout for
    kernel development. A fact about the install, not a per-build choice,
    which is why it is a function here rather than a field somewhere.
    """
    override = os.environ.get("IRON_AIE_KERNELS_DIR")
    if override:
        return Path(override)
    return Path(aie.utils.config.root_path()) / "include" / "aie_kernels"


def iron_kernels_dir() -> Path:
    """The kernels IRON still hosts: gemm's ``mm.cc``, flm's ``mm_fused.cc``."""
    return _REPO / "aie_kernels"


def target_arch(dev=None) -> str:
    """``"aie2p"`` for NPU2 (Strix, Krackan), ``"aie2"`` for NPU1 (Phoenix)."""
    return resolve_target_arch(
        dev if dev is not None else aie_utils.get_current_device()
    )


def runtime_dir(dev=None) -> Path:
    """This architecture's ``aie_runtime_lib``: its headers and its tables."""
    return (
        Path(aie.utils.config.root_path())
        / "aie_runtime_lib"
        / target_arch(dev).upper()
    )


def lut_sources(dev=None):
    """``lut_based_ops.cpp`` when this arch's kernels need it, else nothing.

    aie2's exp/log kernels reference its tables; aie2p's do not. Returned as a
    bundle for :func:`declare_kernel` rather than as an object to link: the
    tables have no MLIR call site, so an object carrying them can never be
    discovered by tracing calls, and compiling them into the kernel's own
    translation unit is what removes the problem rather than working around it.
    """
    if target_arch(dev) != "aie2":
        return ()
    return (runtime_dir(dev) / "lut_based_ops.cpp",)


def declare_kernel(
    name,
    arg_types,
    *,
    source=None,
    func_prefix="",
    compile_flags=(),
    include_dirs=None,
    object_file_name=None,
    bundled_sources=(),
    symbol_prefix=None,
):
    """Declare the kernel a design calls, and how it is built.

    ``bundled_sources`` names translation units the kernel needs linked but
    never calls through MLIR -- ``lut_based_ops.cpp``, whose exp/log tables
    aie2's kernels reach from C++ with no call site. ``aie-assign-core-link-files``
    finds objects by tracing ``func.call`` edges, so it can never discover
    that one. Compiling it into the same translation unit removes the orphan
    object entirely: one source, one object, nothing to discover.

    The bundle is a generated source rather than ``-include``: clang processes
    ``-include`` files before the arch macros are established, and aie_api
    rejects that with "'__AIE_ARCH__' macro is required".

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

    ``symbol_prefix`` distinguishes several objects built from one source in a
    single design -- stream's GEMMs, one per tile shape, all from mm.cc. It
    composes with the fusion prefix rather than replacing it, so a fused
    stream group gets "op0_mm128_64_64_matmul_bf16_bf16": both the group it
    belongs to and the shape it was built for.
    """
    prefix = f"{func_prefix}{symbol_prefix or ''}".rstrip("_") or None
    if object_file_name is not None and func_prefix:
        # Upstream names a defaulted object after the prefixed symbol; an
        # explicit one is taken as given, so the fusion prefix has to be applied
        # here or two fused operators would share one object.
        #
        # The fusion prefix only. symbol_prefix distinguishes symbols *within*
        # one design, where the object name is already distinct -- adding it
        # here would rename the file out from under a generated design that
        # names it, which is exactly stream's case.
        object_file_name = f"{func_prefix.rstrip('_')}_{object_file_name}"

    source = Path(source)
    # The aie_runtime_lib headers a kernel is compiled against.
    dirs = list([str(runtime_dir())] if include_dirs is None else include_dirs)
    if not bundled_sources:
        return ExternalFunction(
            name,
            object_file_name=object_file_name,
            source_file=str(source),
            arg_types=arg_types,
            include_dirs=dirs,
            compile_flags=list(compile_flags),
            symbol_prefix=prefix,
        )

    # Included by bare name against the search path rather than by absolute
    # path, so the digest upstream takes of this text does not move with the
    # checkout and split the cache per install.
    bundled = [Path(s) for s in bundled_sources]
    for path in (*bundled, source):
        if str(path.parent) not in dirs:
            dirs.append(str(path.parent))
    includes = "".join(f'#include "{p.name}"\n' for p in (*bundled, source))
    return ExternalFunction(
        name,
        object_file_name=object_file_name,
        source_string=(
            "// Generated by iron.operators._kernels.declare_kernel.\n"
            "// One translation unit: the kernel, plus the units it needs\n"
            "// linked but never calls through MLIR.\n" + includes
        ),
        arg_types=arg_types,
        include_dirs=dirs,
        compile_flags=list(compile_flags),
        symbol_prefix=prefix,
    )
