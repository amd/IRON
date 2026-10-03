# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's kernel library, as the stream-dse KernelLibrary it hands to every solve."""

import hashlib
from dataclasses import replace
from functools import lru_cache
from pathlib import Path

from iron.common.device_utils import get_kernel_dir


def path(kernel_dir: str | None = None) -> Path:
    """The library file of a kernel directory, the current device's by default."""
    directory = kernel_dir or get_kernel_dir()
    return Path(__file__).resolve().parent / "kernels" / f"{directory}.toml"


def library(kernel_dir: str | None = None):
    """The kernel library of a kernel directory, the current device's by default."""
    return _load(path(kernel_dir))


@lru_cache(maxsize=None)
def _load(source: Path):
    from stream.compiler.kernels.library import KernelLibrary

    if not source.exists():
        raise FileNotFoundError(f"no stream-dse kernel library for {source.stem}")
    return KernelLibrary.load(source)


def with_block(block: int, kernel_dir: str | None = None):
    """The library with every block list narrowed to ``block``, so the solve builds the one
    design of those it would otherwise choose between."""
    source = library(kernel_dir)
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


def fixed_dims(symbol: str, kernel_dir: str | None = None) -> dict[str, int]:
    """The dimensions a source is compiled at and cannot vary: its -DDIM_*."""
    spec = library(kernel_dir).spec(symbol)
    return {d.name: d.fixed for d in spec.dims if d.fixed is not None}


def flash_blocks(kernel_dir: str | None = None) -> tuple[int, ...]:
    """Query blocks the online-softmax source compiles for, finest first."""
    return tuple(sorted(library(kernel_dir).spec("partial_softmax").dim("m").blocks))


def revision(kernel_dir: str | None = None) -> str:
    """Token for the library file, so an edit to it is not served a design solved before it."""
    return hashlib.sha256(path(kernel_dir).read_bytes()).hexdigest()[:6]
