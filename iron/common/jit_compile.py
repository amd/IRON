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

import dataclasses
import hashlib
import inspect
import re
import shutil
from pathlib import Path
from typing import Any

import aie.utils as aie_utils
import numpy as np
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

    # A design built for an xclbin declares its per-call values as dispatch-
    # time scalars: keyword-only DispatchTime[T] parameters of the generator,
    # which CompilableDesign hands in as dispatch parameters and the design
    # forwards to its Runtime. Declared by spelling the signature, since the
    # set is the operator's.
    dispatch = list(call_kwargs.pop("dispatch", None) or [])

    def generate(*positional, **kw):
        # CompilableDesign passes the compile parameters positionally and the
        # dispatch parameters by name; bind both through the spelled signature.
        kw = generate.__signature__.bind(*positional, **kw).arguments
        design = kw["design"]
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
        for symbol, _ in dispatch:
            kwargs[symbol] = kw[symbol]
        module = design(**kwargs)
        return Module.parse(module) if isinstance(module, str) else module

    from aie.iron import DispatchTime

    P = inspect.Parameter
    parameters = [
        P("design", P.POSITIONAL_OR_KEYWORD, annotation=CompileTime[Any]),
        P("params", P.POSITIONAL_OR_KEYWORD, annotation=CompileTime[str]),
        P("chain", P.POSITIONAL_OR_KEYWORD, annotation=CompileTime[str], default=""),
    ] + [
        P(symbol, P.KEYWORD_ONLY, annotation=DispatchTime[dtype])
        for symbol, dtype in dispatch
    ]
    generate.__signature__ = inspect.Signature(parameters)
    generate.__annotations__ = {p.name: p.annotation for p in parameters}
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

# A fused sequence as an xclbin kernel: the switches expanded, the dispatch
# device's xclbin and stream requested (their names are templates, see
# compile_fused_xclbin). No scratchpad: an xclbin run has none (spike S2).
FUSED_XCLBIN_FLAGS = (
    "--expand-load-pdis",
    "--device-name=main",
    "--get-xclbin",
    "--get-npu-insts",
)

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


def compile_fused_xclbin(
    build_mlir,
    build_dir,
    label,
    *,
    kernel_id,
    xclbin_input=None,
    extra_flags=(),
    scalars=(),
):
    """Compile a fused sequence as one xclbin kernel; return (xclbin, insts).

    With ``scalars`` (the dispatch-time scalars the fused sequence takes,
    filled in by ``build_mlir``) there is no static stream: the second
    element would be a :class:`DispatchStream` over the bridge library, built
    as ``CompilableDesign`` builds it, after the callee sequences are pruned
    from the lowered module. Today that ends in a named refusal: the stream's
    PDI preloads are beyond upstream's Python dispatch bridge (see below), so
    the xclbin and the lowered module are built and the library is not.

    The chunked image (OPERATOR_MODEL_PLAN.md §8, spike S1): the fused
    module's dispatch device becomes a kernel named ``label`` whose
    instruction stream carries every configuration switch expanded inline
    (``--expand-load-pdis``), and links onto ``xclbin_input`` so a sequence
    of chunks lands in one loadable image. A multi-device module needs the
    ``{0}`` name templates, which ``CompilableDesign`` does not allow, so
    this goes to ``compile_mlir_module`` directly; it builds the kernels the
    designs declare into the work directory, where aiecc links them.
    """
    from aie.iron.kernel import ExternalFunction
    from aie.utils.compile import compile_mlir_module

    build_dir = Path(build_dir)
    work_dir = build_dir / f"{label}.prj"
    xclbin_path = build_dir / f"{label}_main.xclbin"
    insts_path = build_dir / f"{label}_main_sequence.bin"
    ExternalFunction._instances.clear()
    text = _fuse_as_children(build_mlir)
    scalars = list(scalars)
    flags = [f for f in FUSED_XCLBIN_FLAGS if not (scalars and f == "--get-npu-insts")]
    flags += [
        f"--xclbin-kernel-name={label}",
        f"--xclbin-instance-name={label}",
        f"--xclbin-kernel-id={kernel_id}",
        f"--xclbin-name={build_dir / (label + '_{0}.xclbin')}",
        f"--npu-insts-name={build_dir / (label + '_{0}.bin')}",
    ]
    if xclbin_input is not None:
        flags.append(f"--xclbin-input={Path(xclbin_input).resolve()}")
    if scalars:
        flags.append("--get=npu_lowered.mlir")
    flags += list(extra_flags)
    current = _digest(text + "\n".join(flags))
    stamp = xclbin_path.with_suffix(xclbin_path.suffix + ".cache_hash")
    if scalars:
        from aie.utils.compile.jit import _manifest

        lib = _manifest.resolve_dispatch_library(work_dir)
        if (
            xclbin_path.exists()
            and lib is not None
            and stamp.exists()
            and stamp.read_text() == current
        ):
            return xclbin_path, DispatchStream(Path(lib), tuple(scalars))
    elif (
        xclbin_path.exists()
        and insts_path.exists()
        and stamp.exists()
        and stamp.read_text() == current
    ):
        return xclbin_path, insts_path
    work_dir.mkdir(parents=True, exist_ok=True)
    compile_mlir_module(
        text,
        work_dir=work_dir,
        options=flags,
        device=aie_utils.get_current_device(),
        npu_cpp_path=work_dir / "dispatch_gen.cpp" if scalars else None,
        npu_cpp_emit_dispatch_shim=bool(scalars),
    )
    if not xclbin_path.exists():
        raise RuntimeError(f"aiecc produced no {xclbin_path.name} in {build_dir}")
    if scalars:
        from aie.utils.compile.jit._dispatch_compile import (
            DispatchCompileError,
            compile_dispatch_bridge,
        )

        # The materialisation inlines each step's sequence into the dispatch
        # device's but leaves the callees in theirs, and the bridge accepts
        # exactly one; prune them (§11). What the bridge then refuses is the
        # stream itself: expanding the PDI loads preloads an empty PDI before
        # each configuration's writes (AIEExpandLoadPdi), so a multi-
        # configuration stream always carries load_pdi ops, and the Python
        # dispatch runtime cannot supply their resources. A native host can
        # (aiecc --get-npu-cpp); here it is a named limit.
        _prune_callee_sequences(work_dir / "npu_lowered.mlir")
        try:
            lib = compile_dispatch_bridge(work_dir, scalars, [np.int32] * len(scalars))
        except DispatchCompileError as e:
            if "load_pdi" not in str(e):
                raise
            raise NotImplementedError(
                f"{label}: a fused sequence with per-call values ({', '.join(scalars)}) "
                f"cannot be dispatched from Python: its stream preloads a PDI at every "
                f"configuration switch and upstream's Python dispatch bridge cannot "
                f"supply PDI loads (aiecc: use --get-npu-cpp with a native host). "
                f"Package at each_step, or fix the values at compile time."
            ) from e
        stamp.write_text(current)
        return xclbin_path, DispatchStream(Path(lib), tuple(scalars))
    if not insts_path.exists():
        raise RuntimeError(f"aiecc produced no {insts_path.name} in {build_dir}")
    stamp.write_text(current)
    return xclbin_path, insts_path


def _prune_callee_sequences(lowered: Path) -> None:
    """Keep only the dispatch device's runtime sequence in aiecc's lowered module.

    ``aie-materialize-runtime-sequences`` inlines every ``aiex.run`` callee
    into the dispatch device's sequence but leaves the callees' own
    ``aie.runtime_sequence`` ops in their devices, and the dispatch bridge
    refuses a module with more than one (OPERATOR_MODEL_PLAN.md §11). The
    dispatch device is the fusion's ``main``; every other device's sequence
    is a callee.
    """
    import aie.dialects.aie  # noqa: F401  registers the dialect for parsing
    import aie.dialects.aiex  # noqa: F401
    from aie.ir import Context, Module, StringAttr

    with Context() as ctx:
        ctx.allow_unregistered_dialects = True
        module = Module.parse(lowered.read_text())
        kept = 0
        for device in list(module.body.operations):
            if device.operation.name != "aie.device":
                continue
            attrs = device.operation.attributes
            name = StringAttr(attrs["sym_name"]).value if "sym_name" in attrs else ""
            for op in list(device.operation.regions[0].blocks[0].operations):
                if op.operation.name != "aie.runtime_sequence":
                    continue
                if name == "main":
                    kept += 1
                else:
                    op.operation.erase()
        if kept != 1:
            raise RuntimeError(
                f"{lowered}: expected the dispatch device's one runtime sequence, "
                f"found {kept}"
            )
        lowered.write_text(str(module))


def compile_insts(generator, insts_path, extra_flags=()) -> Path:
    """Compile one design's instruction stream only, against an image built elsewhere.

    The instructions-only compile of OPERATOR_MODEL_PLAN.md §11: an operator
    whose array is already built (flm/gemm's configuration xclbin at the
    reference shape, mm_prebuilt's downloaded image, any operator sharing an
    overlay) needs only its runtime sequence lowered. ``aiecc
    --get-npu-insts`` does exactly that, without compiling a core, so no
    kernel object and no Peano are involved. ``CompilableDesign.compile()``
    refuses an instructions-only request (its xclbin and insts paths must be
    set together), so this goes to ``compile_mlir_module`` directly, keyed on
    the generated text like the fused path.
    """
    from aie.iron.kernel import ExternalFunction
    from aie.utils.compile import compile_mlir_module

    insts_path = Path(insts_path)
    design_fn, args, kwargs = generator.resolve()
    if args:
        raise ValueError(
            f"design {design_fn.__qualname__} takes positional arguments "
            f"{args!r}; the cache key only spells keyword parameters."
        )
    # No core is compiled, so the kernels a design declares are not built;
    # clearing the registry keeps one process's designs from colliding on a
    # kernel name, as CompilableDesign does before generating.
    ExternalFunction._instances.clear()
    module = design_fn(**kwargs)
    text = module if isinstance(module, str) else str(module)
    flags = list(extra_flags)
    current = _digest(text + "\n".join(flags))
    stamp = insts_path.with_suffix(insts_path.suffix + ".cache_hash")
    if insts_path.exists() and stamp.exists() and stamp.read_text() == current:
        return insts_path
    work_dir = insts_path.parent / f"{insts_path.stem}.prj"
    work_dir.mkdir(parents=True, exist_ok=True)  # aiecc's input is written into it
    compile_mlir_module(text, insts_path=insts_path, work_dir=work_dir, options=flags)
    if not insts_path.exists():
        raise RuntimeError(f"aiecc produced no instruction stream at {insts_path}")
    stamp.write_text(current)
    return insts_path


@dataclasses.dataclass(frozen=True)
class DispatchStream:
    """What a dispatch-time design has instead of a static instruction stream:
    the host library that generates one per call, and the scalars it takes."""

    lib_path: Path
    params: tuple


def compile_xclbin_insts(
    generator,
    xclbin_path,
    insts_path,
    kernel_name: str,
    xclbin_input=None,
    extra_flags=(),
):
    """Compile one operator's design to an xclbin and its instruction stream.

    A design with dispatch-time parameters has no static stream: the second
    element is then a :class:`DispatchStream`, the bridge library aiecc's
    ``--get-npu-cpp`` output compiles to, from which the runtime generates
    each call's stream.

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
    if design.dispatch_params:
        from aie.utils.compile.jit import _manifest

        hit, current_hash, stamp = _compile_if_changed(design, xclbin_path)
        kernel_dir = xclbin_path.parent / f"{xclbin_path.stem}.prj"
        lib = _manifest.resolve_dispatch_library(kernel_dir) if hit else None
        if lib is None:
            design.compile(xclbin_path=xclbin_path)
            lib = design.get_dispatch_lib_path()
            stamp.write_text(current_hash)
        return xclbin_path, DispatchStream(Path(lib), tuple(design.dispatch_params))
    hit, current_hash, stamp = _compile_if_changed(design, xclbin_path, insts_path)
    if not hit:
        design.compile(xclbin_path=xclbin_path, inst_path=insts_path)
        stamp.write_text(current_hash)
    return xclbin_path, insts_path
