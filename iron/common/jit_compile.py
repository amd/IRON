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
* The cache key does not see closure contents, so two graphs whose generators
  share a code object collide. The MLIR's own digest is passed through
  ``compile_kwargs`` to give each graph a distinct key.
"""

import hashlib
import re
import shutil
from pathlib import Path
from typing import Any

import aie.utils as aie_utils
from aie.ir import Module
from aie.utils.compile.jit._hash import _device_identity_key
from aie.utils.compile.jit.compilabledesign import CompilableDesign, compile_context
from aie.utils.compile.jit.markers import CompileTime


def _digest(text: str) -> str:
    """Identity for a graph: the content of the MLIR it generated."""
    return hashlib.sha256(text.encode()).hexdigest()[:24]


# An object address in a parameter's str() would re-key the cache every process.
_ADDRESS = re.compile(r"0x[0-9a-f]{6,}")


def _is_device(value) -> bool:
    """Whether a design parameter is an IRON device.

    Duck-typed on exactly the attributes ``_device_identity_key`` reads, rather
    than on the parameter being called ``dev``: the name a design gives it is
    not what makes it a device, and keying on the name would both miss a design
    that spells it differently and drop a non-device parameter that happens to
    share the name.
    """
    return all(hasattr(value, attr) for attr in ("arch", "cols", "rows"))


def _params_key(kwargs: dict) -> str:
    """The design's bound parameters, spelled so the cache key can hash them.

    ``_compute_recipe_hash`` hashes a callable ``compile_kwargs`` value by its
    code identity, but every other value by ``str()``. A parameter whose
    ``str()`` embeds an object address therefore produces a different key in
    each process, and the failure is silent: not an error, just a cache that
    never hits and an aiecc run on every call.

    A device is exactly that -- ``<abc.NPU2 object at 0x7f...>``. Upstream
    splits identity into a recipe (generator, parameters, flags) and an
    artifact (sources, objects, tools, device), so a device is spelled here the
    same way ``_compute_artifact_hash`` spells it, via ``_device_identity_key``:
    (type, arch, cols, rows), which is stable across processes and still
    distinguishes NPU1 from NPU2. Anything else carrying an address is an
    operator bug, and is rejected rather than quietly degraded.
    """
    items = []
    for name, value in sorted(kwargs.items()):
        if _is_device(value):
            items.append((name, repr(_device_identity_key(value))))
            continue
        text = str(value)
        if _ADDRESS.search(text):
            raise ValueError(
                f"design parameter {name!r} stringifies to {text!r}, which "
                "embeds an object address. It would give this design a new "
                "compile-cache key in every process. Give the value a stable "
                "__str__, or pass the identity it stands for instead."
            )
        items.append((name, text))
    return repr(items)


def _design_generator(call_kwargs: dict):
    """Adapt an IRON design function to the generator CompilableDesign wants.

    Handing over the *design function* rather than MLIR text is what puts
    generation inside ``compile()``: under its lock, and inside the window
    where ``ExternalFunction._instances`` is collected. Kernels declared by the
    design are therefore compiled by upstream rather than by a separate rule.

    The signature is only identity, never data: ``compile_kwargs`` keys must
    appear in it and carry ``CompileTime[T]``, so each one exists to reach the
    cache key. The design is hashed by its code, its parameters by their text,
    and ``chain`` by the predecessor xclbin a separate-dispatch operator links
    onto. The values the design is actually called with are closed over, which
    is safe only because ``params`` already spells them -- closure contents are
    invisible to the cache key, the trap pinned by
    ``iron/tests/infrastructure/compilable_design_contract.py``.

    An IRON design returns ``ctx.module`` from its own ``mlir_mod_ctx``, not a
    module built into the ambient one. That is accepted: the module keeps its
    context alive, and ``_generate_uncached`` only calls ``verify()`` on it.
    A few designs return that module's text instead, which is parsed here --
    upstream calls ``.operation.verify()`` on whatever comes back, so a string
    reaches it as "AttributeError: 'str' object has no attribute 'operation'",
    which names neither the design nor the cause.
    """

    def generate(
        design: CompileTime[Any],
        params: CompileTime[str],
        chain: CompileTime[str] = "",
    ):
        kwargs = dict(call_kwargs)
        bound = aie_utils.get_current_device()
        for name, value in kwargs.items():
            if _is_device(value):
                # Re-read rather than reuse what the operator resolved: by the
                # time the generator runs, compile() has called
                # ensure_current_device(), which can bind a device that was
                # merely inferred before. Generating against a different one
                # than the cache keys on is how a design silently ends up built
                # for the wrong target.
                kwargs[name] = bound
        module = design(**kwargs)
        return Module.parse(module) if isinstance(module, str) else module

    return generate


def _fuse_as_children(build_mlir) -> str:
    """Fuse the operator designs, with none of them a full ELF in its own right.

    ``_iron_full_elf`` makes a design's runtime sequence load its own PDI,
    because on that path no xclbin configures the device
    (``aie/iron/program.py``). Exactly one program in a fused build needs that,
    and it is not the children: ``fuse_mlir`` inlines each child's device --
    runtime sequence included -- and drives PDI switching itself, alternating
    between two PDIs per configure point under ``--expand-load-pdis``, with
    ``needs_additional_reset`` keeping the count even.

    Generated inside ``compile()`` without this, every child also emits a
    ``load_pdi`` and the two schemes fight: the build succeeds, the ELF links,
    and the device hangs at dispatch with ERT_CMD_STATE_TIMEOUT. Shadowing the
    flag for the children is what the old code got for free by generating
    outside ``compile()`` altogether.
    """
    with compile_context(_iron_full_elf=False):
        return build_mlir()


def _fused_generator(build_mlir):
    """Fuse a sequence's designs into one module, inside ``compile()``.

    ``graph`` and ``trace`` are never read; they exist so the fused text's
    digest and the trace size have somewhere to live in ``compile_kwargs``,
    which is what the cache key hashes.

    Staging happens here rather than before ``compile()``, because a cache miss
    calls ``_cleanup_failed_compilation`` on the work directory first and wipes
    anything already put there. The generator runs after that and before aiecc,
    which is the only window where staged objects survive.
    """

    def generate(
        graph: CompileTime[str],
        trace: CompileTime[int] = 0,
        chain: CompileTime[str] = "",
    ):
        # Fused and parsed here so the designs' ExternalFunctions register into
        # the set compile() collects, and the module lands in the mlir_mod_ctx
        # it opened.
        return Module.parse(_fuse_as_children(build_mlir))

    return generate


def _compile_if_changed(design, *output_paths: Path) -> tuple[bool, str, Path]:
    """Whether ``design``'s current recipe already produced ``output_paths``.

    ``CompilableDesign.compile()`` bypasses its own on-disk cache entirely
    whenever explicit output paths are given -- its own docstring says the
    caller "is presumed to manage their own dependency tracking". Without
    this, an unchanged recipe recompiles through aiecc every time a fresh
    ``CompilableDesign``/``OperatorSequence``/operator instance asks for it,
    not just on an actual edit -- measured directly: two independently
    constructed but identical fused sequences each rebuilt the ELF (mtime
    changed both times).

    Reuses ``CompilableDesign``'s own content hash (recipe + kernel object
    content + device + flags) rather than inventing a second one -- already
    relied on by ``iron/tests/infrastructure/compilable_design_contract.py``
    -- and stamps it next to the first output.
    """
    # Bind the device before hashing. _compute_artifact_hash reads
    # get_current_device(probe_runtime=False), which is None until something
    # binds one -- and compile() binds it moments later, from inside. So the
    # stamp for the first build in a process records a "no device" hash that
    # the next identical build can never match, and every process silently
    # rebuilds once. Binding here makes both sides agree.
    #
    # Guarded exactly as CompilableDesign._bind_generation_device guards it:
    # binding probes the runtime, which a compile-only host without one cannot
    # do. Failing to bind is not an error -- it leaves the device unset on both
    # sides, which still agrees with itself.
    try:
        aie_utils.ensure_current_device()
    except (ImportError, RuntimeError, AttributeError, ValueError, TypeError):
        pass
    stamp = output_paths[0].with_suffix(output_paths[0].suffix + ".cache_hash")
    current = design._compute_cache_hash()
    hit = (
        all(p.exists() for p in output_paths)
        and stamp.exists()
        and stamp.read_text() == current
    )
    return hit, current, stamp


# Flags the artifact-graph rule passes for a full ELF, and which a fused
# sequence does not work without. --expand-load-pdis is what makes a multi-
# device runlist switch PDIs between steps; --get-scratchpad-parameters emits
# the parameter table the host writes through. Compiling without them produces
# a smaller ELF that is not the same program -- 70,936 bytes against 99,768 on
# a two-step graph -- so they are not optional tuning.
FUSED_ELF_FLAGS = ("--expand-load-pdis", "--get-scratchpad-parameters")

# Only when tracing. The trace parser reads the lowered module to find the
# buffer layout and each design's traced tiles and events, so without this a
# traced build compiles cleanly and then has nothing to parse.
TRACE_FLAG = "--get-input-with-addresses"


def fused_work_dir(elf_path) -> Path:
    """Directory aiecc writes a fused ELF's build outputs into.

    The fused MLIR stopped being an artifact when fuse_mlir() became a plain
    generator, so there is no MLIR filename left to derive this from the way
    ``comp._aiecc_work_dir`` does for the artifact-graph paths. The ELF path is
    the only stable name, and callers that need aiecc's graph outputs
    afterwards -- ``params.txt`` for the runtime-parameter scratchpad,
    ``input_with_addresses.mlir`` for the trace layout -- must derive it from
    here rather than re-deriving the convention.
    """
    elf_path = Path(elf_path)
    return elf_path.parent / f"{elf_path.stem}.prj"


def compile_fused_elf(build_mlir, elf_path, extra_flags=(), trace_size=0) -> Path:
    """Compile a fused sequence to a full ELF, returning its path.

    ``build_mlir`` is called, not passed text: fusing several designs into one
    module runs each operator's design, and a design that declares
    ``ExternalFunction`` kernels only has them built if it runs inside
    ``compile()``. Fusing outside and handing over the result registers those
    kernels into a set ``compile()`` then clears, so the objects are never
    built and the core fails to link.

    It is called twice, and deliberately: once here for the cache key, which is
    still the fused text's own digest -- the most precise identity available,
    and a call this path already paid -- and once inside the generator, where
    the kernels survive. Only the second is on the cache-miss path; generation
    is Python building MLIR, against an aiecc run.

    Both calls go through :func:`_fuse_as_children`, so both see the same
    ``_iron_full_elf`` and the key describes the text that is actually
    compiled. Keying under one value and building under the other produces a
    cache entry for a different program -- which is not a build failure, so
    nothing reports it.

    """
    elf_path = Path(elf_path)
    work_dir = fused_work_dir(elf_path)

    identity = _digest(_fuse_as_children(build_mlir))

    design = CompilableDesign(
        _fused_generator(build_mlir),
        full_elf=True,
        aiecc_flags=list(FUSED_ELF_FLAGS)
        + ([TRACE_FLAG] if trace_size else [])
        + list(extra_flags),
        compile_kwargs={"graph": identity, "trace": int(trace_size)},
    )
    hit, current_hash, stamp = _compile_if_changed(design, elf_path)
    if not hit:
        design.compile(full_elf_path=elf_path)
        stamp.write_text(current_hash)
    return elf_path


def compile_sequence(seq, elf_path) -> Path:
    """Compile an already-set-up OperatorSequence's fused MLIR to an ELF.

    The fused MLIR is generated fresh here: build_fused_mlir is a plain
    function, not an on-disk artifact, and running it inside compile() is what
    lets each child design's ExternalFunction kernels be collected and built.
    """
    return compile_fused_elf(
        lambda: seq._dispatch.build_fused_mlir(seq),
        elf_path,
        extra_flags=getattr(seq, "extra_flags", ()) or (),
        trace_size=getattr(seq, "trace_size", 0) or 0,
    )


def compile_xclbin_insts(
    generator,
    xclbin_path,
    insts_path,
    kernel_name: str,
    xclbin_input=None,
    extra_flags=(),
):
    """Compile one operator's design to an xclbin and its instruction stream.

    The separate-dispatch counterpart to :func:`compile_fused_elf`. Chaining
    looks like it needs more than CompilableDesign offers -- each operator's
    xclbin links onto the previous one's via ``--xclbin-input`` so a sequence
    lands in one loadable image -- but that and the kernel name are both aiecc
    flags, which it already forwards. No local subclass is needed.

    ``generator`` is the operator's ``DesignGenerator``. It is resolved but not
    called here: the design function runs inside ``compile()``, which is what
    lets a design declare ``ExternalFunction`` kernels and have upstream build
    them.
    """
    xclbin_path, insts_path = Path(xclbin_path), Path(insts_path)

    flags = [f"--xclbin-kernel-name={kernel_name}"]
    if xclbin_input is not None:
        flags.append(f"--xclbin-input={Path(xclbin_input).resolve()}")
    flags += list(extra_flags)

    design_fn, args, kwargs = generator.resolve()
    if args:
        raise ValueError(
            f"design {design_fn.__qualname__} takes positional arguments "
            f"{args!r}; the cache key only spells keyword parameters."
        )

    design = CompilableDesign(
        _design_generator(kwargs),
        aiecc_flags=flags,
        compile_kwargs={
            "design": design_fn,
            "params": _params_key(kwargs),
            # The predecessor is part of what this image is: two operators with
            # identical designs chained onto different xclbins differ.
            "chain": str(xclbin_input or ""),
        },
    )
    hit, current_hash, stamp = _compile_if_changed(design, xclbin_path, insts_path)
    if not hit:
        design.compile(xclbin_path=xclbin_path, inst_path=insts_path)
        stamp.write_text(current_hash)
    return xclbin_path, insts_path
