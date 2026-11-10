# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's kernel library, the stream-dse ``KernelLibrary`` every solve is given.

One TOML per architecture, ``kernels/<arch>.toml``, named as
``resolve_target_arch`` names the device's (``"aie2p"``).
"""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

import hashlib
from dataclasses import replace
from functools import cache
from pathlib import Path

from aie.utils.compile.jit.operator import Unresolvable

KERNELS = Path(__file__).resolve().parent / "kernels"


def library_path(arch: str) -> Path:
    """Return the library file of ``arch``."""
    return KERNELS / f"{arch}.toml"


@cache
def load_library(arch: str):
    """Return the kernel library of ``arch``.

    Raises:
        Unresolvable: IRON has no library for ``arch``, or stream-dse is not
            installed.
    """
    path = library_path(arch)
    if not path.exists():
        raise Unresolvable(f"no stream-dse kernel library for {arch} ({path})")
    try:
        from stream.compiler.kernels.library import KernelLibrary
    except ImportError:
        raise Unresolvable(
            "stream-dse is not installed (requirements_stream.txt)"
        ) from None
    return KernelLibrary.load(path)


def pinned_to_block(arch: str, block: int):
    """Return ``arch``'s library with every block list narrowed to ``block``.

    The solve then builds the one design of those it would choose between.

    Raises:
        ValueError: A kernel is not compiled at ``block``.
    """
    source = load_library(arch)
    kernels = {}
    for symbol, spec in source.kernels.items():
        dims = []
        for dim in spec.dims:
            if dim.blocks and block not in dim.blocks:
                raise ValueError(
                    f"{symbol} compiles {dim.name} for {dim.blocks}, not {block}"
                )
            dims.append(replace(dim, blocks=(block,)) if dim.blocks else dim)
        kernels[symbol] = replace(spec, dims=tuple(dims))
    return replace(source, kernels=kernels)


def blocks(arch: str, symbol: str, dim: str) -> tuple[int, ...]:
    """Return the blocks ``symbol`` compiles ``dim`` for, finest first."""
    return tuple(sorted(load_library(arch).spec(symbol).dim(dim).blocks))


def library_revision(arch: str) -> str:
    """Return a token of ``arch``'s library file, so an edit to it solves anew."""
    return hashlib.sha256(library_path(arch).read_bytes()).hexdigest()[:12]
