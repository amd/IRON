# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile designs through mlir-aie's CompilableDesign, which owns the cache.

Every build lands in the JIT cache, keyed on the content it was built from;
IRON names nothing on disk. What this module adds is the seam: how an
IRON design function becomes the generator ``CompilableDesign`` runs inside
``compile()`` (so the kernels a design declares are collected and built),
and how a fused sequence, a chained xclbin and an instructions-only stream
are each spelled as one design. Three things about the upstream API are
not guessable from its signature, and each is load-bearing here:

* ``compile_kwargs`` keys must appear in the generator's signature *and* carry
  a ``CompileTime[T]`` annotation.
* The generator must return an MLIR ``Module``. ``_generate_uncached`` calls
  ``module.operation.verify()`` on whatever comes back, so text raises
  ``AttributeError``.
* The cache key does not see closure contents, so two graphs whose generators
  share a code object collide. Each graph's identity is passed through
  ``compile_kwargs`` to give it a distinct key.
"""

import dataclasses
import functools
import hashlib
import inspect
import re
from pathlib import Path
from typing import Any

import aie
import aie.utils as aie_utils
from aie.ir import Module
from aie.iron import DispatchTime
from aie.utils.compile.jit._hash import _code_identity, _device_identity_key
from aie.utils.compile.jit.compilabledesign import (
    CacheEntry,
    CompilableDesign,
    compile_context,
)
from aie.utils.compile.jit.markers import CompileTime

# Flags the fused full-ELF build needs. --expand-load-pdis is what makes a
# multi-device runlist switch PDIs between steps; --get-scratchpad-parameters
# emits the parameter table the host writes through. Without them the ELF is
# smaller and not the same program.
FUSED_ELF_FLAGS = ("--expand-load-pdis", "--get-scratchpad-parameters")

# Only when tracing: the trace parser reads the lowered module for the buffer
# layout and each design's traced tiles and events.
TRACE_FLAG = "--get-input-with-addresses"


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
        # A per-call value a graph bound on an operator is part of what it
        # builds (a device parameter, a patched descriptor), but not a field,
        # so its repr leaves it out.
        used = getattr(value, "bound_values", None)
        if used:
            text += f" using {sorted(used.items())}"
        if _ADDRESS.search(text):
            raise ValueError(
                f"design parameter {name!r} stringifies to {text!r}, which "
                "embeds an object address. It would give this design a new "
                "compile-cache key in every process. Give the value a stable "
                "__str__, or pass the identity it stands for instead."
            )
        items.append((name, text))
    return repr(items)


def design_identity(generator) -> str:
    """What a design generates from: its function's code and its parameters.

    The two things :func:`_design_generator` puts in a standalone build's
    key, spelled once so a fused build can name and key each of its designs
    without running any of them.
    """
    design_fn, kwargs = _resolved(generator)
    h = hashlib.sha256(_code_identity(design_fn.__code__))
    h.update(_params_key(kwargs).encode())
    return h.hexdigest()[:24]


# What turns a design into MLIR text, beyond the design itself: IRON's
# common tree (the declaration layer, the build, the fusion) and mlir-aie's
# Python frontend and bindings.
_AIE = Path(inspect.getfile(aie)).resolve().parent
_GENERATOR_TREES = (
    Path(__file__).resolve().parents[1],
    _AIE / "iron",
    _AIE / "dialects",
)
_BINDINGS = _AIE / "_mlir_libs"


@functools.cache
def _file_digest(path: str) -> bytes:
    return hashlib.sha256(Path(path).read_bytes()).digest()


@functools.cache
def _generator_trees_digest() -> str:
    h = hashlib.sha256()
    for root in _GENERATOR_TREES:
        for path in sorted(root.rglob("*.py")):
            h.update(_file_digest(str(path)))
    # Compiled, and large: by size and time rather than by content.
    for path in sorted(_BINDINGS.glob("*.so")):
        stat = path.stat()
        h.update(f"{path.name}:{stat.st_size}:{stat.st_mtime_ns}".encode())
    return h.hexdigest()


def source_digest(files=()) -> str:
    """A digest of the source that generates MLIR: the trees every design
    shares (:data:`_GENERATOR_TREES`), and ``files`` besides.

    Read once per process: a process runs the code it imported, so an edit
    made while it runs is the next process's to see, in its key and its
    text alike.
    """
    h = hashlib.sha256(_generator_trees_digest().encode())
    for path in files:
        h.update(_file_digest(str(path)))
    return h.hexdigest()


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
        kw = inspect.signature(generate).bind(*positional, **kw).arguments
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

    P = inspect.Parameter
    parameters = [
        P("design", P.POSITIONAL_OR_KEYWORD, annotation=CompileTime[Any]),
        P("params", P.POSITIONAL_OR_KEYWORD, annotation=CompileTime[str]),
        P("chain", P.POSITIONAL_OR_KEYWORD, annotation=CompileTime[str], default=""),
    ] + [
        P(symbol, P.KEYWORD_ONLY, annotation=DispatchTime[dtype])
        for symbol, dtype in dispatch
    ]
    setattr(generate, "__signature__", inspect.Signature(parameters))
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
    and the device hangs at dispatch with ERT_CMD_STATE_TIMEOUT.
    """
    with compile_context(_iron_full_elf=False):
        return build_mlir()


def _fused_generator(build_mlir):
    """Fuse a sequence's designs into one module, inside ``compile()``.

    ``graph`` and ``trace`` are never read; they exist so the sequence's
    identity and the trace size have somewhere to live in ``compile_kwargs``,
    which is what the cache key hashes.
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


def _bind_device() -> None:
    # _compute_cache_hash reads the current device, which compile() binds
    # from inside; binding first makes a key computed before and after agree.
    try:
        aie_utils.ensure_current_device()
    except (ImportError, RuntimeError, AttributeError, ValueError, TypeError):
        pass


def fused_design(
    build_mlir, identity: str, extra_flags=(), trace_size=0
) -> CompilableDesign:
    """A sequence's fused full ELF, compiled (or found) in the JIT cache.

    ``build_mlir`` is called, not passed text: fusing several designs into
    one module runs each operator's design, and a design that declares
    ``ExternalFunction`` kernels only has them built if it runs inside
    ``compile()``. It runs only there, and only on a miss: the key is
    ``identity``, what the text is a function of
    (:func:`~iron.common.image.fused.fused_identity`), so a hit generates
    nothing. Keying on the text itself fused every design once more on
    every call, hit or miss -- three quarters of a warm compile.
    """
    design = CompilableDesign(
        _fused_generator(build_mlir),
        full_elf=True,
        aiecc_flags=list(FUSED_ELF_FLAGS)
        + ([TRACE_FLAG] if trace_size else [])
        + list(extra_flags),
        compile_kwargs={"graph": identity, "trace": int(trace_size)},
    )
    _bind_device()
    design.compile()
    return design


def _resolved(generator):
    design_fn, args, kwargs = generator.resolve()
    if args:
        raise ValueError(
            f"design {design_fn.__qualname__} takes positional arguments "
            f"{args!r}; the cache key only spells keyword parameters."
        )
    return design_fn, kwargs


def insts_design(generator, extra_flags=()) -> CompilableDesign:
    """One design's instruction stream alone, against an image built elsewhere.

    The instructions-only compile of OPERATOR_MODEL_PLAN.md §11: an operator
    whose array is already built (a configuration's image at the reference
    shape, a shipped image's download) needs only its runtime
    sequence lowered. No core is compiled, so no kernel and no Peano.
    """
    design_fn, kwargs = _resolved(generator)
    design = CompilableDesign(
        _design_generator(kwargs),
        insts_only=True,
        aiecc_flags=list(extra_flags),
        compile_kwargs={
            "design": design_fn,
            "params": _params_key(kwargs),
            "chain": "",
        },
    )
    _bind_device()
    design.compile()
    return design


@dataclasses.dataclass(frozen=True)
class DispatchStream:
    """What a dispatch-time design has instead of a static instruction stream:
    the host library that generates one per call, and the scalars it takes.
    """

    lib_path: Path
    params: tuple


def xclbin_design(
    generator, kernel_name: str, xclbin_input=None, extra_flags=()
) -> CompilableDesign:
    """One operator's design as an xclbin and its instruction stream.

    The separate-dispatch counterpart to :func:`fused_design`. Chaining --
    each operator's xclbin linked onto the previous one's via
    ``--xclbin-input`` so a sequence lands in one loadable image -- and the
    kernel name are both aiecc flags, which CompilableDesign forwards. A
    design with dispatch-time parameters has no static stream; its bridge
    library is :meth:`CompilableDesign.get_dispatch_lib_path`, and
    :func:`dispatch_stream` spells it for the runtime.
    """
    flags = [f"--xclbin-kernel-name={kernel_name}"]
    if xclbin_input is not None:
        flags.append(f"--xclbin-input={Path(xclbin_input).resolve()}")
    flags += list(extra_flags)
    design_fn, kwargs = _resolved(generator)
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
    _bind_device()
    design.compile()
    return design


def dispatch_stream(design: CompilableDesign) -> "DispatchStream | None":
    """The per-call stream generator of a dispatch-time design, else ``None``."""
    if not design.dispatch_params:
        return None
    lib = design.get_dispatch_lib_path()
    assert lib is not None, "a dispatch-time design compiles its stream library"
    return DispatchStream(Path(lib), tuple(design.dispatch_params))


def cache_entry(design: CompilableDesign) -> CacheEntry:
    """What ``design``'s compile left in the cache; it has compiled."""
    entry = design.get_cache_entry()
    if entry is None:
        raise RuntimeError(f"{design} has not compiled")
    return entry
