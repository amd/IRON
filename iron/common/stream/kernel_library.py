# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's kernel library, the stream-dse ``KernelLibrary`` every solve is given.

One TOML per architecture, ``kernels/<arch>.toml``, named as
``resolve_target_arch`` names the device's (``"aie2p"``).
"""

import tomllib
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
        from stream.compiler.kernels.library import (  # pyright: ignore[reportMissingImports]
            KernelLibrary,
        )
    except ImportError:
        raise Unresolvable(
            "stream-dse is not installed (requirements_stream.txt)"
        ) from None
    return KernelLibrary.from_dict(tomllib.loads(path.read_text()))


def kernel_spec(arch: str, symbol: str):
    """Return ``arch``'s library entry of ``symbol``.

    Raises:
        KeyError: The library has no such kernel.
    """
    spec = load_library(arch).spec(symbol)
    if spec is None:
        raise KeyError(f"{library_path(arch).name} has no kernel {symbol}")
    return spec


def call_dim(arch: str, symbol: str, dim: str):
    """Return what ``symbol`` compiles its dimension ``dim`` for.

    Raises:
        KeyError: The kernel has no such dimension.
    """
    found = kernel_spec(arch, symbol).dim(dim)
    if found is None:
        raise KeyError(f"{symbol} has no dimension {dim}")
    return found


def pinned_to_block(arch: str, block: int):
    """Return ``arch``'s library with every kernel's query rows, ``m``, narrowed to ``block``.

    The solve then builds the one query block of those it would choose
    between; the other blocks stay its choice.

    Raises:
        ValueError: A kernel is not compiled at ``block``.
    """
    source = load_library(arch)
    kernels = {}
    for symbol, spec in source.kernels.items():
        dims = []
        for dim in spec.dims:
            pinned = dim.name == "m" and dim.blocks
            if pinned and block not in dim.blocks:
                raise ValueError(
                    f"{symbol} compiles {dim.name} for {dim.blocks}, not {block}"
                )
            dims.append(replace(dim, blocks=(block,)) if pinned else dim)
        kernels[symbol] = replace(spec, dims=tuple(dims))
    return replace(source, kernels=kernels)


def blocks(arch: str, symbol: str, dim: str) -> tuple[int, ...]:
    """Return the blocks ``symbol`` compiles ``dim`` for, finest first."""
    return tuple(sorted(call_dim(arch, symbol, dim).blocks))
