# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Kernel objects several operators compile out of mlir-aie's ``aie_kernels``.

A kernel shared by more than one operator is declared once here, because the
operator builds the object and its design names that object in ``link_with``:
the two have to agree on a file name, and they live in different files.
"""

from __future__ import annotations

from pathlib import Path

from .compilation import KernelObjectArtifact, SourceArtifact

# mlir-aie's generic/zero.cc exports one entry point, `zero`, specialized by
# -DZERO_TYPE/-DTILE_SIZE. The C spelling of each dtype IRON zeroes:
ZERO_CTYPES = {
    "i8": "int8_t",
    "i16": "int16_t",
    "i32": "int32_t",
    "bf16": "bfloat16",
    "f32": "float",
}


def zero_object_name(dtype_str: str, tile_size: int, scalar: bool = False) -> str:
    """Object file name of the zero kernel specialized this way.

    The specialization is baked in at compile time, so it belongs in the name:
    two designs zeroing different tiles need different objects.
    """
    return f"zero_{dtype_str}_{tile_size}{'_scalar' if scalar else ''}.o"


def zero_artifact(
    kernels_dir: Path, dtype_str: str, tile_size: int, scalar: bool = False
) -> KernelObjectArtifact:
    """The zero-fill kernel object for a ``tile_size``-element ``dtype_str`` tile.

    mm.cc used to carry `zero_<dtype>` alongside its matmuls, so a design got the
    two from one object. mlir-aie split zero.cc out into its own translation unit
    (#3732), which is why this is a separate artifact.
    """
    try:
        ctype = ZERO_CTYPES[dtype_str]
    except KeyError:
        raise ValueError(f"zero kernel: unsupported dtype {dtype_str}") from None
    flags = [f"-DZERO_TYPE={ctype}", f"-DTILE_SIZE={tile_size}"]
    if scalar:
        flags.append("-DZERO_SCALAR")
    return KernelObjectArtifact(
        zero_object_name(dtype_str, tile_size, scalar),
        dependencies=[SourceArtifact(kernels_dir / "generic" / "zero.cc")],
        extra_flags=flags,
    )
