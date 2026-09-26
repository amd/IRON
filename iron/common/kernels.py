# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How a design declares the kernel it calls.

One declaration, not two: ``ExternalFunction`` is the symbol and the object
at once, and upstream compiles the source and names the object from its
content, so no file name is spelled out twice.

Constructing it here, inside the design, is required rather than stylistic.
An ``ExternalFunction`` registers itself into a process-global set that
``CompilableDesign`` clears when it begins generating, so one built earlier --
in the operator, say -- is discarded and its object never compiled.
"""

import hashlib
from pathlib import Path

import aie.utils as aie_utils
import aie.utils.config
from aie.iron import ExternalFunction
from aie.utils.compile.utils import resolve_target_arch


def kernels_dir() -> Path:
    """C++ kernel sources the mlir-aie kernel factories build from.

    ``MLIR_AIE_KERNEL_SOURCES`` points this at a local mlir-aie checkout for
    kernel development. A fact about the install, not a per-build choice,
    which is why it is a function here rather than a field somewhere.
    """
    return Path(aie.utils.config.aie_kernels_dir())


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


def recipe_digest(name, source, compile_flags, include_dirs, bundled, symbol_prefix):
    """Eight hex digits naming what a kernel's object is built from.

    The sources by content, not path, so a checkout elsewhere names the same
    kernel the same way; everything else as given (``source`` is a path or
    the text itself). Two declarations that agree here build byte-identical
    objects, so they may share one.
    """
    h = hashlib.sha256()
    for path in bundled:
        h.update(Path(path).read_bytes())
    h.update(source.encode() if isinstance(source, str) else Path(source).read_bytes())
    h.update(
        repr((name, tuple(compile_flags), tuple(include_dirs), symbol_prefix)).encode()
    )
    return h.hexdigest()[:8]


def declare_kernel(
    name,
    arg_types,
    *,
    source=None,
    source_text=None,
    digest_prefix=True,
    compile_flags=(),
    include_dirs=None,
    object_file_name=None,
    bundled_sources=(),
    symbol_prefix=None,
):
    """Declare the kernel a design calls, and how it is built.

    ``source`` is the C++ file; ``source_text`` the C++ itself, for a kernel
    written in the operator's own file (a hello-world's ``vadd``). One or
    the other.

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

    ``digest_prefix`` prefixes the symbol and the object with a digest of the
    kernel's recipe (:func:`recipe_digest`). Designs fused into one ELF share
    one object directory and one registry, so two naming one kernel with
    different flags (two GEMV shapes) would otherwise collide. Keyed on the
    recipe rather than on anything about the design, equal recipes -- the
    same kernel in two designs, in two graphs, or standalone and fused --
    get one symbol, one object and one compile, and different ones never
    meet. Off only for a design whose MLIR names its kernels itself
    (stream's), which must then keep distinct recipes under distinct names.

    ``symbol_prefix`` distinguishes several objects built from one source in a
    single design -- stream's GEMMs, one per tile shape, all from mm.cc. The
    digest composes with it rather than replacing it:
    "<digest>_mm128_64_64_matmul_bf16_bf16".
    """
    if (source is None) == (source_text is None):
        raise TypeError(f"{name}: a kernel names its source, or gives its text")
    # The aie_runtime_lib headers a kernel is compiled against.
    dirs = list([str(runtime_dir())] if include_dirs is None else include_dirs)

    prefix = symbol_prefix
    if digest_prefix:
        digest = recipe_digest(
            object_file_name or name,
            source_text if source is None else Path(source),
            compile_flags,
            dirs,
            bundled_sources,
            symbol_prefix,
        )
        prefix = f"{digest}_{symbol_prefix}" if symbol_prefix else digest
        if object_file_name is not None:
            # Upstream names a defaulted object after the prefixed symbol; an
            # explicit one is taken as given, so the digest has to be applied
            # here or two recipes naming one object would collide.
            object_file_name = f"{digest}_{object_file_name}"
    if source_text is not None and not bundled_sources:
        return ExternalFunction(
            name,
            object_file_name=object_file_name,
            source_string=source_text,
            arg_types=arg_types,
            include_dirs=dirs,
            compile_flags=list(compile_flags),
            symbol_prefix=prefix,
        )
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
    units = bundled if source is None else [*bundled, Path(source)]
    for path in units:
        if str(path.parent) not in dirs:
            dirs.append(str(path.parent))
    includes = "".join(f'#include "{p.name}"\n' for p in units)
    return ExternalFunction(
        name,
        object_file_name=object_file_name,
        source_string=(
            "// Generated by iron.common.kernels.declare_kernel.\n"
            "// One translation unit: the kernel, plus the units it needs\n"
            "// linked but never calls through MLIR.\n" + includes + (source_text or "")
        ),
        arg_types=arg_types,
        include_dirs=dirs,
        compile_flags=list(compile_flags),
        symbol_prefix=prefix,
    )
