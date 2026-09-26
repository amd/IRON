# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator: one class declaring the array, the buffers and the sequence.

Its fields fall into two tiers by what a change rebuilds: the fields a tile
names, plus those marked ``array=True``, configure the array, and one array
serves every extent; the rest size the host buffers and reach only the
runtime sequence. Calling the class binds it:
:func:`~iron.common.declare.infer` turns operand shapes into the extents,
and the instance's buffer attributes report shapes in elements.
"""

from __future__ import annotations

import copy
import dataclasses
import inspect
from types import FunctionType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Self,
    TypeVar,
    dataclass_transform,
    overload,
)

import aie.utils as aie_utils
import numpy as np
from aie.utils.npukernel import NPUKernel
from aie.utils.verify import Tolerance

from ..device import device_name
from ..kernels import kernels_dir
from ..testing import Testing
from .bound import BoundBuffer, BoundStream, BoundValue
from .creation import declare
from .field import DeclarationError, Unresolvable, param
from .infer import infer, infer_kwargs
from .member import Extent, Value, _Buffer, _extent_reads, _Member, _Stream, _Value
from .naming import label_parts
from .profile import current as current_profile
from .shim import check_shim_columns, shim_columns

if TYPE_CHECKING:
    from ..graph.handle import Handle
    from ..image.artifacts import Artifacts

_T = TypeVar("_T")


class _OperatorMeta(type):
    """``GEMV(w, h)`` inside a graph function records a step; anything else constructs.

    A call with graph handles (or host tensors, which a graph closes over as
    weights) records a step; see :mod:`iron.common.graph`. Any other call
    constructs. The two overloads below tell a type checker the same: a
    call with operands yields a handle, a call by keyword constructs.
    """

    if TYPE_CHECKING:

        @overload
        def __call__(
            cls: type[_T], operand: Any, /, *operands: Any, **kwargs: Any
        ) -> Handle: ...
        @overload
        def __call__(cls: type[_T], **kwargs: Any) -> _T: ...

    def __call__(cls, *args, **kwargs):
        from .. import graph as _graph  # imports this package: a cycle at module scope

        tracer = _graph.current()
        if tracer is not None and args and all(_graph.is_operand(a) for a in args):
            return tracer.call(cls, args, kwargs)
        if args:
            raise TypeError(
                f"{cls.__name__} is constructed by keyword ({cls.__name__}(M=..., "
                f"K=...)); operands are given inside an @iron.graph function"
            )
        profile = current_profile()
        if profile is not None:
            # The knobs this call leaves open, where the profile names them.
            kwargs = {**profile.knobs_for(cls, kwargs), **kwargs}
        return super().__call__(*args, **kwargs)


def _check_shipped(cls: type) -> None:
    """Check a class declared with ``image=``: nothing builds it, so it must pin
    every endpoint itself.
    """
    if "array" in vars(cls):
        raise DeclarationError(
            f"{cls.__name__} runs a shipped image, so nothing builds its array(); "
            f"drop the override"
        )
    for m in cls._members:
        if isinstance(m, _Stream) and m.via is None:
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: a stream into a shipped image must be "
                f"pinned with via=; nothing else says which shim it uses"
            )
        if isinstance(m, Value) and m.derive is not None and m.address is None:
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: a value written into a shipped image "
                f"needs an address; the sequence writes it there"
            )


class _ArrayView:
    """The array tier of an operator, as :meth:`Operator.array` sees it.

    Reading a field no tile names and that does not declare ``array=True``
    raises, so an array cannot come to depend on an extent by accident
    (one array serves every extent). The operator's methods and properties
    run on the view too, so a ``kernel()`` reading an extent is caught as
    well.
    """

    __slots__ = ("_op",)

    def __init__(self, op: "Operator") -> None:
        object.__setattr__(self, "_op", op)

    @property
    def __class__(self):  # type: ignore[override]
        # super() and isinstance() inside a hook see the operator's class.
        return type(object.__getattribute__(self, "_op"))

    def __getattr__(self, name: str):
        op = object.__getattribute__(self, "_op")
        fields = {f.name for f in dataclasses.fields(op)}
        if name in fields and name not in op._array_fields:
            raise TypeError(
                f"{type(op).__name__}.array() reads {name}, which no tile names: "
                f"an array serves every extent. Declare it param(..., array=True) "
                f"if the array does read it, or move the dependence into the "
                f"sequence or a Value"
            )
        attr = inspect.getattr_static(type(op), name, None)
        if isinstance(attr, FunctionType):
            return attr.__get__(self, type(op))
        if isinstance(attr, property) and attr.fget is not None:
            return attr.fget(self)
        return getattr(op, name)

    def __setattr__(self, name: str, value) -> None:
        setattr(object.__getattribute__(self, "_op"), name, value)


# kw_only_default: every declared field is passed by keyword (at runtime a
# required field after one with a default is keyword-only too, see
# field._specifier). ``param`` is listed as a field specifier so a ``param()``
# without ``default=`` is a required constructor argument. ``auto`` is not
# listed: pyright reads a specifier's default only from a ``default=`` keyword,
# and ``auto(2)`` passes it positionally. Unlisted, an ``auto()`` field is one
# with a default of type Any, which is accurate.
class _ExtentWord(Value):
    """The tiles per lane of one operand under a bound: the word its
    transfers are patched with, derived from the extent as a ``Value`` is.
    """

    def __init__(self, owner: type, extent: Extent, buffer: str, axis: int) -> None:
        super().__init__(np.int32, derive=self._tiles)
        self.owner = owner
        self.name = f"{extent.name}_{buffer}"
        self.extent, self.buffer, self.axis = extent, buffer, axis

    def _tiles(self, op) -> int:
        from ..design.runtime import extent_unit  # the one definition of the unit

        b = op.value_buffer(self.buffer)
        lanes = 1 if b.lanes.replicate else b.lanes.count
        return getattr(op, self.extent.name) // (lanes * extent_unit(b, self.axis))

    def __repr__(self) -> str:
        return f"<tiles per lane of {self.buffer} under {self.extent.name}>"


@dataclass_transform(kw_only_default=True, field_specifiers=(param,))
@dataclasses.dataclass(eq=False, repr=True)
class Operator(metaclass=_OperatorMeta):
    """An operator. Subclass it.

    One class declares the whole thing: ``param()``/``auto()`` fields,
    ``In``/``Out`` operands (with ``tile=`` an operand is its own stream),
    ``Value`` members, :meth:`array` for the dataflow, :meth:`sequence` when
    the derived one is not wanted, :meth:`resolve`/:meth:`compatible` and
    :meth:`reference`. A class declared with ``image=`` runs a shipped
    binary instead of building an array. Every subclass is a dataclass and
    is checked as its body finishes (:mod:`.creation`).
    """

    _members: ClassVar[tuple[_Member, ...]] = ()
    _param_fields: ClassVar[tuple[str, ...]] = ()
    _derived_params: ClassVar[dict[str, Callable[[Any], Any]]] = {}
    _auto_fields: ClassVar[tuple[str, ...]] = ()
    _array_fields: ClassVar[tuple[str, ...]] = ()
    _external: ClassVar[Any] = None
    # The cases iron/operators/test.py runs this operator at; None for an
    # operator tested by its own test.py, or not on its own.
    test: ClassVar[Testing | None] = None

    def __init_subclass__(cls, image=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if image is not None:
            # A shipped image: ``class Shipped(GEMM, image=Xclbin(...))``.
            # Nothing builds its array, so it declares where every stream
            # enters and every value lives, and may not define array().
            cls._external = image
        declare(cls)
        if image is not None:
            _check_shipped(cls)

    def __post_init__(self) -> None:
        self._resolved = False
        self._derive_params()
        self.validate()
        self._bind()
        # Once every knob is known the extents can be checked, so the check
        # runs at construction rather than at resolution.
        if not any(getattr(self, n) is None for n in self._auto_fields):
            self.compatible()

    def _derive_params(self) -> None:
        """Compute each ``param(default=<callable>)`` a shape or the caller
        left open, in declaration order.
        """
        for name, derive in self._derived_params.items():
            if getattr(self, name) is None:
                value = derive(self)
                if value is None:
                    raise ValueError(
                        f"{type(self).__name__}.{name}: not given, and nothing "
                        f"to compute it from"
                    )
                setattr(self, name, value)

    def check_derived(self, *names: str) -> None:
        """Raise ``ValueError`` if a computed-default parameter was given a
        value its rule disagrees with. For a parameter a shape may bind but
        the other fields also determine (``out_rows = rows * repeat``).
        """
        for name in names:
            given, expected = getattr(self, name), self._derived_params[name](self)
            if given != expected:
                raise ValueError(
                    f"{type(self).__name__}.{name}={given!r} is not what its "
                    f"other fields make it ({expected!r})"
                )

    # -- declared surface --------------------------------------------------

    def validate(self) -> None:
        """Check the sequence-tier fields on their own. Runs at construction."""

    def compatible(self) -> None:
        """Check the extents against the resolved knobs; raise :class:`Incompatible`."""

    def resolve(self, dev) -> Self:
        """Return a copy resolved for ``dev``: every ``auto()`` filled, from
        the device and from this operator's extents; raise :class:`Unresolvable`.

        This is the only hook that sees both. The default fills nothing. A
        knob left ``None`` is an error once this returns::

            def resolve(self, dev):
                cols = self.columns or self.shim_columns(dev)
                return dataclasses.replace(self, columns=cols)

        Identity for sharing a build is taken after this runs, so two
        operators that describe one array resolve to one design.
        """
        return dataclasses.replace(self)

    def array(self, target) -> list:
        """Build the array for ``target`` and return its workers.

        ``target`` (:class:`iron.common.design.Target`) carries the device,
        the kernel tree, and ``kernel()``/``rtp()``/``barrier()``. Bind the
        shim end of a fifo to every operand's lane (``self.A.lane(i).bind(
        fifo.prod())``) and every ``Value`` to the buffer a core reads it
        from. Only the array tier is visible here: reading a field no tile
        names raises.
        """
        raise NotImplementedError(f"{type(self).__name__}.array() is not implemented")

    def build_array(self, target) -> list:
        """Run :meth:`array` for the build, through the array-tier view."""
        return type(self).array(_ArrayView(self), target)  # type: ignore[arg-type]

    def tolerance(self, target) -> Tolerance | None:
        """The contract of the kernel this array runs; ``None`` when the
        operator states its own (see :attr:`test`).
        """
        return None

    def device(self, target):
        """The device the Program is built for; the current device by default."""
        return target.dev

    @property
    def external(self):
        """The downloaded image this operator runs on, if IRON did not build it."""
        return type(self)._external

    def prebuilt(self):
        """The file the declared image names, fetched if it is not in the cache."""
        from ..external import fetch  # imports this package: a cycle at module scope

        return fetch(self.external)

    @classmethod
    def shim_columns(cls, dev, num_channels: int = 1) -> int:
        """How many of ``dev``'s columns this operator's shim budget allows."""
        return shim_columns(cls, dev, num_channels)

    def check_shim_columns(self, dev, cols: int, num_channels: int = 1) -> None:
        check_shim_columns(self, dev, cols, num_channels)

    def resolve_columns(
        self,
        dev,
        given: int | None,
        num_channels: int = 1,
        *,
        fits: Callable[[int], bool] | None = None,
    ) -> int:
        """The column count to resolve to: ``given``, checked against the
        shim budget, or the most the budget allows that ``fits``.

        ``fits(c)`` is the operator's own rule for ``c`` columns leaving
        whole tiles; when no count within the budget does, one column is
        returned and :meth:`compatible` names the rule. With no device
        bound and no count given, :class:`Unresolvable`.
        """
        if given is not None:
            if dev is not None:
                self.check_shim_columns(dev, given, num_channels)
            return given
        if dev is None:
            raise Unresolvable(
                f"{type(self).__name__}: the column count defaults from the "
                f"device; none is bound and none was given"
            )
        budget = self.shim_columns(dev, num_channels)
        return next((c for c in range(budget, 0, -1) if fits is None or fits(c)), 1)

    def reference(self, *inputs):
        raise NotImplementedError(
            f"{type(self).__name__}.reference() is not implemented"
        )

    def sequence(self, rt) -> None:
        """Override to write the runtime sequence by hand; otherwise it is derived.

        ``rt`` is an :class:`iron.common.design.Sequence`: ``rt.fill(stream,
        view)``, ``rt.drain(stream, view)``, ``rt.group()``. The preamble
        (residents, barriers, parameter sync) has already run.
        """
        raise NotImplementedError

    def resident_values(self) -> dict[str, Any]:
        """What the preamble writes once per build: every ``Value(derive=)``
        no graph bound per call, derived from this instance.
        """
        return {
            m.name: m.derive(self)
            for m in self._members
            if isinstance(m, Value)
            and m.derive is not None
            and not self.uses_value(m.name)  # bound per call: not a resident
        }

    @classmethod
    def has_sequence_override(cls) -> bool:
        return cls.sequence is not Operator.sequence

    # -- library surface ---------------------------------------------------

    def value_symbol(self, value: "BoundValue") -> str | None:
        """An explicit device symbol for a per-call value, or ``None`` for the default."""
        return None

    def design_key(self):
        """Identity for sharing a build: the class, the array's key, every compared field.

        Two operators with equal keys generate byte-identical MLIR, so a
        sequence builds, prefixes and configures the design once.
        """
        own = tuple(
            (f.name, getattr(self, f.name))
            for f in dataclasses.fields(self)
            if f.compare
        )
        # A per-call value a graph bound is built in (a device parameter, a
        # patched descriptor, a core that reads it), so it tells designs apart.
        if self.used_values:
            own += (("values", tuple(sorted(self.bound_values.items()))),)
        return (type(self).__qualname__, own)

    def array_key(self):
        """Identity for sharing an array: the class and its array-tier fields."""
        return (type(self).__qualname__,) + tuple(
            (name, getattr(self, name)) for name in self._array_fields
        )

    def resolved(self, dev) -> Self:
        """This operator resolved for ``dev``: itself if it already is, else
        :meth:`resolve`'s copy, every knob filled and :meth:`validate` and
        :meth:`compatible` checked. Nothing else calls :meth:`resolve`.
        """
        if self._resolved:
            return self
        new = self.resolve(dev)
        if new is self:
            raise TypeError(
                f"{type(self).__name__}.resolve() must return a copy, "
                f"dataclasses.replace(self, ...), not self"
            )
        if not isinstance(new, type(self)):
            raise TypeError(
                f"{type(self).__name__}.resolve() must return a {type(self).__name__}"
            )
        missing = [n for n in self._auto_fields if getattr(new, n) is None]
        if missing:
            raise Unresolvable(
                f"{type(self).__name__}.resolve() left {missing} unset for {dev}"
            )
        new.validate()
        # Values a graph bound on this instance live outside its fields, so
        # replace() does not carry them. The build works on the copy, and
        # losing them would silently drop the per-call value from the sequence.
        if self.used_values:
            vars(new)["_used_values"] = dict(self.bound_values)
        new.compatible()
        new._resolved = True
        return new

    def copy(self) -> Self:
        """A fresh instance for one build, so the streams a build binds are
        this build's alone; resolution state and the per-call values a graph
        bound are kept.
        """
        new = dataclasses.replace(self)
        if self.used_values:
            vars(new)["_used_values"] = dict(self.bound_values)
        new._resolved = self._resolved
        if self._resolved:
            # What compatible() records is part of a resolved instance; a
            # replace() resets an init=False field to its default, so the
            # copy records it again.
            new.compatible()
        return new

    @property
    def buffers(self) -> list[BoundBuffer]:
        return [self._bound[m.name] for m in self._members if isinstance(m, _Buffer)]

    @property
    def inputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction in ("in", "inout")]

    @property
    def outputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction in ("out", "inout")]

    @property
    def values(self) -> list[BoundValue]:
        """The per-call values this instance uses (see :meth:`uses_value`)."""
        return [
            self._bound[m.name] for m in self._value_members if self.uses_value(m.name)
        ]

    @property
    def streams(self) -> dict[str, BoundStream]:
        """Every operand's own stream, by the operand's name."""
        return {
            m.name: self._bound[m.name].lanes
            for m in self._members
            if isinstance(m, _Buffer) and m.stream is not None
        }

    @property
    def residents(self) -> dict[str, BoundValue]:
        """What the preamble writes once per build: every ``Value(derive=)``
        no graph bound per call.
        """
        return {
            m.name: self._bound[m.name]
            for m in self._members
            if isinstance(m, Value)
            and m.derive is not None
            and not self.uses_value(m.name)
        }

    def uses_value(self, name: str) -> bool:
        """Whether this instance drives the declared per-call value ``name``.

        A value an instance does not use gets no device parameter and no
        sync. The default is every declared value, except an ``Extent``,
        per call only when a graph bounds it, and a ``Value`` with a
        derivation, per call when a graph binds it (:meth:`use_value`) or
        its derivation reads a bound extent; an operator whose values are
        optional (a copy with or without a patched offset) overrides this.
        """
        member = next((m for m in self._value_members if m.name == name), None)
        if isinstance(member, Extent):
            return name in self.used_values
        if isinstance(member, Value) and member.derive is not None:
            return name in self.used_values or name in self._per_call_derived()
        return True

    @property
    def bound_extents(self) -> dict[str, str | None]:
        """Extent name -> the graph value bounding it, for the bound ones."""
        bound = self.bound_values
        return {
            m.name: bound[m.name]
            for m in self._members
            if isinstance(m, Extent) and m.name in bound
        }

    def _per_call_derived(self) -> frozenset[str]:
        """The derived values whose derivation reads a bound extent."""
        if not self.bound_extents:
            return frozenset()
        out = set()
        for m in self._value_members:
            if not (isinstance(m, Value) and m.derive is not None):
                continue
            reads: set[str] = set()
            token = _extent_reads.set(reads)
            try:
                m.derive(self)
            except Exception:
                pass  # unresolved: what it read before failing still counts
            finally:
                _extent_reads.reset(token)
            if reads & self.bound_extents.keys():
                out.add(m.name)
        return frozenset(out)

    def derived_at(self, name: str, **extents: int) -> Any:
        """The value ``name``'s derivation with the extents at the given
        bounds: the word the host writes for one call.
        """
        member = next((m for m in self._value_members if m.name == name), None)
        if not (isinstance(member, Value) and member.derive is not None):
            raise TypeError(f"{type(self).__name__}.{name} is not a derived value")
        unknown = set(extents) - {
            m.name for m in self._members if isinstance(m, Extent)
        }
        if unknown:
            raise TypeError(
                f"{type(self).__name__} declares no Extent {sorted(unknown)}"
            )
        at = copy.copy(self)
        vars(at)["_extents"] = {**self.__dict__.get("_extents", {}), **extents}
        return member.derive(at)

    def extent_unit(self, buffer: str) -> int | None:
        """The rows of operand ``buffer`` one lane takes at a time under a
        bound, when it is not the stream tile's rows (GEMV's A moves in
        output tiles, several input tiles each); ``None`` for the tile's;
        ``0`` when the operand is not shortened under a bound at all (GEMM
        and MHA stream every row and bound their compute), so no word of
        tiles per lane is made for it.
        """
        return None

    def value_buffer(self, name: str) -> BoundBuffer:
        """The bound operand ``name``."""
        b = self._bound.get(name)
        if not isinstance(b, BoundBuffer):
            raise TypeError(f"{type(self).__name__} declares no operand {name!r}")
        return b

    def value(self, name: str) -> BoundValue:
        """The device word of the value member ``name`` (an ``Extent`` reads
        as an integer on the instance, so this is how a sequence names its
        word).
        """
        try:
            return self._bound[name]
        except KeyError:
            raise TypeError(
                f"{type(self).__name__} declares no value {name!r}"
            ) from None

    def use_value(self, name: str, bound_to: str | None = None) -> None:
        """Record that a graph binds the per-call value ``name`` on this
        instance, to its own value ``bound_to``.

        The graph value is part of what is built: two instances alike in
        every field but reading different graph values are two designs with
        two device symbols.
        """
        if not any(isinstance(m, _Value) and m.name == name for m in self._members):
            raise TypeError(
                f"{type(self).__name__} declares no per-call value {name!r}"
            )
        vars(self).setdefault("_used_values", {})[name] = bound_to

    @property
    def used_values(self) -> frozenset:
        """The names of the per-call values a graph binds on this instance."""
        return frozenset(self.bound_values)

    @property
    def bound_values(self) -> dict[str, str | None]:
        """Per-call value name -> the graph value it is bound to."""
        return dict(self.__dict__.get("_used_values", {}))

    # -- graph functions ---------------------------------------------------

    @classmethod
    def resolve_class(cls, n_operands: int, kwargs: dict) -> type:
        """The class a graph call with ``n_operands`` operands constructs.

        The default is the class itself; a family that picks a subclass from
        its arguments (RMSNorm with a weight) overrides.
        """
        return cls

    def __call__(self, *args, **kwargs):
        """An explicit instance applied to graph handles records a step."""
        from .. import graph as _graph  # as above

        tracer = _graph.current()
        if tracer is None:
            raise TypeError(
                f"{type(self).__name__} instances are called on graph handles inside "
                f"an @iron.graph function; outside one, compile() and get_callable()"
            )
        return tracer.call(self, args, kwargs)

    def _bind(self) -> None:
        bound: dict[str, Any] = {}
        for m in self._members:
            if isinstance(m, _Buffer):
                bound[m.name] = BoundBuffer(m, self)  # its own stream with it
            elif isinstance(m, _Value):
                bound[m.name] = BoundValue(m, self)
        self._bound = bound
        # One word per (extent, operand it sizes): the tiles per lane a
        # bounded transfer is patched with. Made here, so a build finds it
        # among the values; per call only once the extent is bound.
        words = []
        for e in self._members:
            if not isinstance(e, Extent):
                continue
            for b in self._members:
                if isinstance(b, _Buffer) and b.stream is not None:
                    axis = bound[b.name].extent_axis(e)
                    if axis is not None and self.extent_unit(b.name) != 0:
                        word = _ExtentWord(type(self), e, b.name, axis)
                        bound[word.name] = BoundValue(word, self)
                        words.append(word)
        self._extent_words = tuple(words)

    @property
    def _value_members(self) -> list[_Value]:
        """The declared value members and the extent words made with them."""
        return [m for m in self._members if isinstance(m, _Value)] + list(
            self.__dict__.get("_extent_words", ())
        )

    # -- construction from operand shapes ----------------------------------

    @classmethod
    def from_operands(cls, *operand_shapes, **overrides) -> Self:
        """Construct an operator from operand shapes."""
        values = infer(cls, *operand_shapes, **infer_kwargs(cls, overrides))
        return cls(**{**overrides, **values})

    def reference_tolerance(self) -> Tolerance | None:
        """How close the NPU output must come to :meth:`reference`: the
        resolved operator's :meth:`tolerance` for this device, ``None`` when
        it states none.
        """
        from ..design.target import (
            Target,
        )  # imports this package: a cycle at module scope

        return self.resolved(self.dev).tolerance(Target(self.dev, kernels_dir()))

    # -- the image of one operator on its own -------------------------------

    @property
    def dev(self):
        """The device a design is generated for, bound as the current one
        (:func:`~iron.common.device.bound_device`); ``None`` on a host
        without one, where an operator can still be checked and lowered.
        """
        return aie_utils.ensure_current_device()

    # Bytes of trace buffer to emit; 0 disables tracing. A plain attribute
    # rather than a property: OperatorSequence and LayerNorm assign it.
    trace_size = 0

    @property
    def name(self) -> str:
        """This instance's label: the class, every shown field as resolved
        for the device, and the device. It names the per-call value symbols
        a host writes through and the kernel instances a chained image
        carries. Nothing on disk is keyed by it; the compile cache keys by
        content. The label describes what is built, so it comes from the
        resolved operator.
        """
        dev = aie_utils.get_current_device()
        if dev is None:
            raise RuntimeError(f"{type(self).__name__}.name needs a bound device")
        own = label_parts(self.resolved(dev))
        base = type(self).__name__ + "_" + "_".join(own)
        # Upstream annotates Device.resolve() -> None; it returns the AIEDevice.
        return f"{base}_{device_name(dev)}"

    def generator(self, image: str = "elf"):
        """The design generator :class:`CompilableDesign` runs for this operator.

        An operator whose design is exported text rather than derived from
        the declaration overrides this (see :func:`from_spec`, and
        swiglu_prefill_stream, which loads its group from the exported
        module). The default is ``build_design`` over the declaration.
        """
        from ..design import (
            generator_for,
        )  # reads this package: a cycle at module scope

        return generator_for(self, image=image)

    def compile(self, record: str = "memory") -> "Operator":
        """Build this operator's own image, once; sets :attr:`artifacts`.

        ``record="disk"`` also writes the :class:`~iron.common.image.artifacts.Artifacts`
        record beside the image; by default it is only kept in memory.
        """
        if getattr(self, "_artifacts", None) is None:
            self._artifacts = self._build()
            if record == "disk":
                self._artifacts.dump()
        return self

    @property
    def artifacts(self) -> "Artifacts":
        """The record of what :meth:`compile` produced."""
        artifacts = getattr(self, "_artifacts", None)
        if artifacts is None:
            raise RuntimeError(
                f"{type(self).__name__} is not compiled; compile() first"
            )
        return artifacts

    def _members_io(self):
        """The declared buffers, without resolving a shape: their names alone."""
        return [m for m in self._members if isinstance(m, _Buffer)]

    def buffer_map(self) -> dict[str, tuple[str, int, int]]:
        """Each buffer as ``(arena, position, nbytes)``, for an image's record.

        Taken from the resolved operator, since a shape may depend on a knob
        the device fills (flm/gemm's B layout) and the built image's buffers
        are the resolved ones. A standalone operator has no arena plan; its
        buffers are the kernel's positional arguments.
        """
        resolved = self.resolved(self.dev)
        return {b.name: ("arg", i, b.nbytes) for i, b in enumerate(resolved.buffers)}

    def _build(self):
        """Compile to an xclbin and an instruction stream, or, on a shipped
        image, to the stream alone against the download.
        """
        # image/ reads this package, so naming it at module scope would make
        # the two import each other.
        from ..image.artifacts import Artifacts, Design, Step
        from ..image.jit_compile import cache_entry, insts_design, xclbin_design

        image = self.external
        if image is None:
            picture = None
            design = xclbin_design(self.generator("xclbin"), kernel_name="MLIR_AIE")
        else:
            picture = self.prebuilt()
            design = insts_design(self.generator())
        entry = cache_entry(design)
        insts = entry.insts
        assert insts is not None, "no instruction stream"
        if picture is None:
            picture = entry.xclbin
            assert picture is not None, "no xclbin"
        self._design = design
        return Artifacts(
            kind="xclbin",
            image=picture,
            insts=insts,
            entry=entry,
            designs=(
                Design(
                    name=self.name,
                    operators=(self.name,),
                    entry=entry,
                    image=picture,
                    insts=insts,
                ),
            ),
            steps=(Step(0, self.name, self.name, tuple(b.name for b in self.buffers)),),
            buffers={b.name: ("arg", i, b.nbytes) for i, b in enumerate(self.buffers)},
        )

    def get_callable(self):
        """The loaded image, ready to call on device tensors."""
        artifacts = self.compile()._artifacts
        image = self.external
        npu_kernel = NPUKernel(
            xclbin_path=str(artifacts.image),
            kernel_name="MLIR_AIE" if image is None else image.kernel_name,
            insts_path=str(artifacts.insts),
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call

    def __repr__(self) -> str:
        own = ", ".join(
            f"{f.name}={getattr(self, f.name)!r}"
            for f in dataclasses.fields(self)
            if f.repr
        )
        return f"{type(self).__name__}({own})"

    def explain(self) -> str:
        """What a build of this operator compiles in and what it takes per call.

        One line per tier: the array's fields (every core is built from them;
        one array serves every operator with the same), the sequence's (the
        host's alone), then each value: written once per build, with its
        number once resolved; per call, as a scratchpad word or a regenerated
        instruction stream; or unused by this instance.
        """
        fields = {
            f.name: getattr(self, f.name) for f in dataclasses.fields(self) if f.compare
        }

        def spell(names):
            return ", ".join(f"{n}={fields[n]!r}" for n in names) or "nothing"

        array = [n for n in fields if n in self._array_fields]
        sequence = [n for n in fields if n not in self._array_fields]
        lines = [
            repr(self) + (" (resolved)" if self._resolved else " (unresolved)"),
            f"  array, compiled into every core: {spell(array)}",
            f"  sequence, the host's alone: {spell(sequence)}",
        ]
        per_call_derived = self._per_call_derived()
        for m in self._value_members:
            if isinstance(m, _ExtentWord) and m.name not in per_call_derived:
                continue  # a word only a bounded extent needs
            if isinstance(m, Extent):
                bound = self.bound_extents.get(m.name)
                how = (
                    f"per call, bounds {m.field.name} (graph value {bound})"
                    if m.name in self.bound_extents
                    else f"{m.field.name}, unbounded"
                )
            elif (
                isinstance(m, Value)
                and m.name in per_call_derived
                and m.name not in self.bound_values
            ):
                how = "per call, derived from a bounded extent"
            elif (
                isinstance(m, Value)
                and m.derive is not None
                and not self.uses_value(m.name)
            ):
                given = f", {m.derive(self)!r} here" if self._resolved else ""
                how = "written once per build" + given
            elif self.uses_value(m.name):
                how = "per call, " + (
                    "the instruction stream regenerated around it"
                    if m.kind == "dispatch"
                    else "a scratchpad word patched or read"
                )
            else:
                how = "unused here"
            lines.append(f"  {m.name}: {how}")
        return "\n".join(lines)
