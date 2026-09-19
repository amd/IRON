# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile a fused sequence through upstream's CompilableDesign.

IRON's artifact graph and ``CompilableDesign`` do the same job -- source to
kernel objects to MLIR to an ELF -- but the upstream one additionally keys its
cache on content, locks across processes, and validates Peano depfiles, none of
which the artifact graph does. This is the seam for moving onto it: it takes a
sequence that has already produced its fused MLIR and compiles that half the
new way, leaving everything else alone.

Four things about the upstream API are not guessable from its signature, and
each is load-bearing here:

* ``compile_kwargs`` keys must appear in the generator's signature *and* carry
  a ``CompileTime[T]`` annotation.
* The generator must return an MLIR ``Module``. ``_generate_uncached`` calls
  ``module.operation.verify()`` on whatever comes back, so text raises
  ``AttributeError``.
* ``object_files`` does **not** stage anything -- it feeds the artifact hash
  only. Kernel objects have to be copied into the work directory under their
  bare names, because the fused MLIR's ``link_with`` names them without a
  directory. This is what ``_link_build_outputs_into`` already does, and it is
  why that step has to survive the move rather than being deleted with the DAG.
* The cache key does not see closure contents, so two graphs whose generators
  share a code object collide. The MLIR's own digest is passed through
  ``compile_kwargs`` to give each graph a distinct key.
"""

import hashlib
import shutil
from pathlib import Path

from aie.ir import Module
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.compile.jit.markers import CompileTime


def _digest(text: str) -> str:
    """Identity for a graph: the content of the MLIR it generated."""
    return hashlib.sha256(text.encode()).hexdigest()[:24]


def _generator_for(mlir_text: str):
    """Wrap MLIR text as a generator CompilableDesign will accept.

    ``graph`` is never read. It exists so the digest has somewhere to live in
    ``compile_kwargs``, which is what the cache key actually hashes.
    """

    def generate(graph: CompileTime[str]):
        # Parsed here so it lands in the mlir_mod_ctx CompilableDesign opens.
        return Module.parse(mlir_text)

    return generate


def stage_objects(work_dir: Path, object_files) -> None:
    """Put kernel objects where aiecc will look for them.

    Copied under bare names: the fused MLIR asks for ``op0_add.o``, not a path.
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    for obj in object_files:
        obj = Path(obj)
        if obj.exists():
            shutil.copy2(obj, work_dir / obj.name)


# Flags the artifact-graph rule passes for a full ELF, and which a fused
# sequence does not work without. --expand-load-pdis is what makes a multi-
# device runlist switch PDIs between steps; --get-scratchpad-parameters emits
# the parameter table the host writes through. Compiling without them produces
# a smaller ELF that is not the same program -- 70,936 bytes against 99,768 on
# a two-step graph -- so they are not optional tuning.
FUSED_ELF_FLAGS = ("--expand-load-pdis", "--get-scratchpad-parameters")


def compile_fused_elf(mlir_text: str, object_files, elf_path, extra_flags=()) -> Path:
    """Compile fused MLIR to a full ELF, returning its path.

    ``object_files`` are the already-built, symbol-prefixed kernel objects the
    MLIR links against.
    """
    elf_path = Path(elf_path)
    object_files = [Path(o) for o in object_files]
    stage_objects(elf_path.with_suffix(".prj"), object_files)

    design = CompilableDesign(
        _generator_for(mlir_text),
        full_elf=True,
        object_files=object_files,
        aiecc_flags=list(FUSED_ELF_FLAGS) + list(extra_flags),
        compile_kwargs={"graph": _digest(mlir_text)},
    )
    design.compile(full_elf_path=elf_path)
    return elf_path


def compile_sequence(seq, elf_path) -> Path:
    """Compile an already-set-up OperatorSequence's fused MLIR to an ELF.

    The sequence must have run ``compile()`` first, which is what produces the
    fused MLIR and the kernel objects this consumes.
    """
    artifacts = list(seq.artifacts.bfs())
    mlir = next(
        a.filename for a in artifacts if str(a.filename).endswith("_fused.mlir")
    )
    objects = [a.filename for a in artifacts if str(a.filename).endswith(".o")]
    return compile_fused_elf(Path(mlir).read_text(), objects, elf_path)
