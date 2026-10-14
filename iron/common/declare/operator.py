# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator: one class declaring the array, the buffers and the sequence.

The fields a tile names, plus those marked ``array=True``, configure the
array, which serves every extent; the rest reach only the runtime sequence.
"""

from __future__ import annotations

import copy
import dataclasses
import hashlib
import inspect
import math
from collections.abc import Iterable, Mapping
from contextvars import ContextVar
from enum import Enum
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
from aie.dialects.aie import AIEArch, AIETileType
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.hostruntime.tensor_class import NpuTensor
from aie.utils.trace import TraceConfig
from aie.utils.verify import Tolerance, Verdict, compare

from ..testing import Testing
from .chain import Chain, Link
from .declaration import Declaration
from .domain import Domain, Width
from .field import Auto, Param, Unresolvable
from .operand import In, Operand
from .profile import Profile
from .rtp import Rtp
from .value import ChainWord, Extent, ExtentWord, PlaceWord, Value

if TYPE_CHECKING:
    from ..graph.handle import Affine, Handle
    from ..image.artifacts import Artifacts
    from ..image.standalone import OperatorImage

_T = TypeVar("_T")

# The tables an AIE2 kernel gathering through lut_based_ops links, pinned to
# banks of core memory; AIE2P computes its activations and links none.
LUT_BYTES = 5248

graph_tracer: ContextVar[Any] = ContextVar("graph_tracer", default=None)


class _OperatorMeta(type):
    """``GEMV(w, h)`` inside a graph's body records a step; anything else constructs."""

    if TYPE_CHECKING:

        @overload
        def __call__(
            cls: type[_T], operand: Any, /, *operands: Any, **kwargs: Any
        ) -> Handle: ...
        @overload
        def __call__(cls: type[_T], **kwargs: Any) -> _T: ...

    def __call__(cls, *args, **kwargs):
        tracer = graph_tracer.get()
        if tracer is not None and args and tracer.accepts(args):
            return tracer.call(cls, args, kwargs)
        if args:
            raise TypeError(
                f"{cls.__name__} is constructed by keyword ({cls.__name__}(M=..., "
                f"K=...)); operands are given inside a graph's body"
            )
        kwargs.setdefault(
            "pinned",
            frozenset(
                k
                for k, v in kwargs.items()
                if k in cls.declaration.tunables and v is not None
            ),
        )
        profile = Profile.current()
        if profile is not None:
            kwargs = {**profile.tunables_for(cls, kwargs), **kwargs}
        # An Enum-domain tunable (GEMM's and MHA's placements) takes its own
        # Enum alone, or None (left for resolve() to fill): a string names
        # one in a profile's JSON, which Profile.load converts before it
        # reaches here.
        for name, domain in cls.declaration.domains.items():
            if (
                name in kwargs
                and isinstance(domain, type)
                and issubclass(domain, Enum)
                and kwargs[name] is not None
                and not isinstance(kwargs[name], domain)
            ):
                raise TypeError(
                    f"{cls.__name__}.{name} is a {domain.__name__}, not {kwargs[name]!r}"
                )
        return super().__call__(*args, **kwargs)


class _Fenced:
    """A field outside the array tier, as ``array()`` sees it: using it raises."""

    __slots__ = ("op", "name")

    def __init__(self, op: str, name: str) -> None:
        self.op = op
        self.name = name

    def refuse(self, *args):
        raise TypeError(
            f"{self.op}.array() reads {self.name}, which no tile names: "
            f"an array serves every extent. Declare it Param(..., array=True) "
            f"if the array does read it, or move the dependence into the "
            f"sequence or a Value"
        )

    __bool__ = __index__ = __int__ = __float__ = __hash__ = __iter__ = refuse
    __eq__ = __ne__ = __lt__ = __le__ = __gt__ = __ge__ = refuse
    __add__ = __radd__ = __sub__ = __rsub__ = __mul__ = __rmul__ = refuse
    __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ = refuse
    __mod__ = __rmod__ = __pow__ = __rpow__ = __neg__ = __abs__ = refuse
    __str__ = __format__ = __len__ = __getitem__ = __call__ = refuse

    def __repr__(self) -> str:
        return f"<{self.op}.{self.name} outside the array tier>"


@dataclasses.dataclass(frozen=True)
class CopyRun:
    """Where an operator writes its one input verbatim, as one contiguous
    run of its one output (``Operator.copies_to``).
    """

    # The elements of the output, and the one the run starts at.
    into: int
    start: int
    # The per-call value adding to ``start``, if any.
    offset: str | None = None


@dataclass_transform(kw_only_default=True, field_specifiers=(Param, Auto))
@dataclasses.dataclass(eq=False, repr=True)
class Operator(metaclass=_OperatorMeta):
    """An operator. Subclass it; every subclass is a dataclass checked as its body finishes."""

    declaration: ClassVar[Declaration]
    _external: ClassVar[Any] = None
    test: ClassVar[Testing | None] = None
    # True when sequence() calls rt.preamble() itself, behind its first fills.
    own_preamble: ClassVar[bool] = False
    # A fused image lowers every operator's sequence under the union.
    aiecc_flags: ClassVar[tuple[str, ...]] = ()
    # Per leading operand that may be a view: the param holding its pattern
    # and the per-call value a dynamic index binds.
    accept_views: ClassVar[tuple[tuple[str, str], ...]] = ()
    # What a call on a view gathered by a graph input (``Copy(table[ids])``)
    # becomes: the class, built with ``rows``, ``table_rows``, ``row`` and
    # ``dtype``, and ``control_words(ids, address)`` encoding each call's ids.
    per_call_gather: ClassVar[type[Operator] | None] = None
    # An instance's operands beside the declared ones: its prologue's and
    # its finish's other inputs.
    _prepare_inputs: ClassVar[tuple[Operand, ...]] = ()
    _finish_inputs: ClassVar[tuple[Operand, ...]] = ()

    trace: TraceConfig | None = dataclasses.field(
        default=None, repr=False, kw_only=True
    )
    # The graph expressions bound to per-call values, by member name;
    # design_key adds their names, since a dict does not hash.
    bound_values: dict[str, Affine | None] = dataclasses.field(
        default_factory=dict, repr=False, compare=False, kw_only=True
    )
    # The tunables its caller gave, which the tuner holds; a profile's and
    # resolve()'s are starting points it may move.
    pinned: frozenset[str] = dataclasses.field(
        default=frozenset(), repr=False, compare=False, kw_only=True
    )
    # The steps each core applies to a tile of the output declared
    # Out(finish=True) before releasing it, and the finishes its array
    # applies; resolved, each step at that tile. The keys add them, since
    # operators compare by identity.
    finish: Chain = dataclasses.field(
        default=Chain(), repr=False, compare=False, kw_only=True
    )
    # The steps each core applies to a tile of the input declared
    # In(prepare=True) after acquiring it, and the prologues its array applies.
    prepare: Chain = dataclasses.field(
        default=Chain(), repr=False, compare=False, kw_only=True
    )
    # Per output a graph placed in a larger buffer (``placed``): its name,
    # that buffer's elements and the one it starts at; design_key adds them.
    placements: tuple[tuple[str, int, int], ...] = dataclasses.field(
        default=(), repr=False, compare=False, kw_only=True
    )

    def __init_subclass__(cls, image=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if image is not None:
            cls._external = image
        cls.declaration = Declaration(cls, Operator, shipped=image is not None)

    def __post_init__(self) -> None:
        self._resolved = False
        self._image: OperatorImage | None = None
        self._derive_params()
        # A graph's reference constructs at a bounded call's valid rows, a
        # shape no device runs, for reference() alone: it is not checked.
        tracer = graph_tracer.get()
        checked = tracer is None or tracer.checks
        if checked:
            self.validate()
        self._bind()
        if checked and not any(
            getattr(self, n) is None for n in self.declaration.autos
        ):
            self.compatible()

    def _derive_params(self) -> None:
        for name, derive in self.declaration.derived.items():
            if getattr(self, name) is None:
                value = derive(self)
                # A T | None field's formula may answer None itself (GEMV's
                # num_matrices, following num_batches): that is the computed
                # value, not an unset one.
                if value is None and name not in self.declaration.nullable:
                    raise ValueError(
                        f"{type(self).__name__}.{name}: not given, and nothing "
                        f"to compute it from"
                    )
                setattr(self, name, value)

    def check_derived(self, *names: str) -> None:
        """Raise ``ValueError`` if a given computed-default parameter disagrees with its rule.

        Only a `Param(derive=)` field an operator's own `validate()` names
        here is held to its formula: a plain computed default (MHA's
        ``num_KV_heads``, left to default to ``num_heads``) may be
        overridden to something the formula disagrees with on purpose.
        """
        for name in names:
            given, expected = getattr(self, name), self.declaration.derived[name](self)
            if given != expected:
                raise ValueError(
                    f"{type(self).__name__}.{name}={given!r} is not what its "
                    f"other fields make it ({expected!r})"
                )

    def validate(self) -> None:
        """Check the sequence-tier fields on their own. Runs at construction."""

    def compatible(self) -> None:
        """Check the extents against the resolved tunables; raise ``ValueError``."""

    def resolve(self, dev) -> Self:
        """Return a copy with every ``Auto()`` filled from ``dev`` and the extents.

        Raises:
            Unresolvable: No legal value exists on ``dev``.
        """
        return dataclasses.replace(self)

    def array(self) -> list:
        """Build the array for the bound device and return its workers.

        Bind every operand's lanes to fifos' shim ends, and give each core
        reading ``Value``s its runtime parameters (``rtp``).
        """
        raise NotImplementedError(f"{type(self).__name__}.array() is not implemented")

    def _build_array(self) -> list:
        """``array()`` on a copy whose fields outside the array tier are
        placeholders that raise on use; what it sets lands on this operator.
        """
        fenced = copy.copy(self)
        for f in dataclasses.fields(self):
            if isinstance(f, Param) and f.name not in self.declaration.array:
                vars(fenced)[f.name] = _Fenced(type(self).__name__, f.name)
        vars(fenced)["_unfenced"] = self
        before = dict(vars(fenced))
        built = fenced.array()
        vars(self).update(
            {
                k: v
                for k, v in vars(fenced).items()
                if k not in before or before[k] is not v
            }
        )
        return built

    def tolerance(self) -> Tolerance | None:
        """What each output of the resolved operator is judged by; None where
        nothing bounds it, which check mode refuses.

        An override returns the operator's own; this one carries it through a
        finish or a prologue, so an override that may have one returns
        ``super().tolerance()`` there.
        """
        # elementwise.py builds on this module.
        from ..elementwise import Finish, Prepare

        if self.finish:
            return Finish(self).tolerance()
        if self.prepare:
            return Prepare(self).tolerance()
        return None

    def ops(self) -> int:
        """The arithmetic operations one call performs, for its throughput."""
        return sum(b.elements for b in self.outputs)

    def fold(self, consumer: Operator, at: int = 0) -> Self | None:
        """This operator applying ``consumer`` to its output in its own cores:
        ``consumer`` appended to its ``finish``. The array keeps the
        finishes it had, unless a step of the chain takes inputs of its own,
        which stream into this array alone. Whether ``consumer`` runs on one
        of its tiles is asked when the result resolves (``at_line``).

        Args:
            consumer: The operator whose input ``at`` is this one's one output.
            at: The input of ``consumer`` the output enters; its others
                become this operator's ``finish_inputs``.

        Returns:
            The folded operator, or None where this one's one output is not
            declared ``finish=True``.
        """
        if len(self.outputs) != 1 or not self.outputs[0].finish:
            return None
        return dataclasses.replace(
            self, finish=self.finish.extended((*self.finish, Link(consumer, at)))
        )

    def prefold(self, producer: Operator, at: int = 0) -> Self | None:
        """This operator applying ``producer`` to its prepared input in its
        own cores: ``producer`` prepended to its ``prepare``, as ``fold``
        appends to a finish. Whether ``producer`` runs on one of its tiles
        is asked when the result resolves (``at_line``).

        Args:
            producer: The operator whose one output is this one's input
                declared ``In(prepare=True)``.
            at: The input of ``producer`` that tile takes the place of; its
                others become this operator's ``prepare_inputs``.

        Returns:
            The folded operator, or None where this one declares no
            prepared input.
        """
        if not any(m.prepare for m in self._members_io()):
            return None
        return dataclasses.replace(
            self, prepare=self.prepare.extended((Link(producer, at), *self.prepare))
        )

    def on_array(self, other: Operator) -> Self | None:
        """This operator declared to run on ``other``'s array, or None:
        one of its type, given its finishes and prologues.

        A graph's fold calls it after folding ``other``; the replacement is
        taken only where it resolves to ``other``'s array.
        """
        if type(other) is not type(self) or not (
            other.finish.shared or other.prepare.shared
        ):
            return None
        return dataclasses.replace(
            self,
            finish=Chain(self.finish.steps, other.finish.shared),
            prepare=Chain(self.prepare.steps, other.prepare.shared),
        )

    def copies_to(self) -> CopyRun | None:
        """Where this operator writes its one input verbatim, as one run of
        its one output; None where it does not, the default.
        """
        return None

    def placed(self, copy: Operator, operand: str) -> Self | None:
        """This operator writing its output ``operand`` where ``copy``
        writes it (``copies_to``), so a graph drops the copy: the operand is
        ``copy``'s output at runtime, every transfer of it moved to the run,
        and by the per-call value moving the run.

        Returns:
            The placed operator, or None where its transfers cannot move:
            a shipped image's, or one whose sequence moves them itself.
        """
        if self.external is not None:
            return None
        run = copy.copies_to()
        if run is None:
            return None
        values = dict(self.bound_values)
        if run.offset is not None:
            values[f"{operand}_offset"] = copy.bound_values[run.offset]
        return dataclasses.replace(
            self,
            bound_values=values,
            placements=(*self.placements, (operand, run.into, run.start)),
        )

    def at_line(self, line: int, dtype, dev, ordered: bool = True, at: int = 0) -> Self:
        """This operator applied by another's core to one tile of its output,
        a run of ``line`` elements of ``dtype``, resolved for ``dev``.
        ``ordered`` is False where the core holds the run in an order of its
        own (``Out(finish=block)``); the tile enters as its input ``at``.

        Raises:
            ValueError: It runs on cores of its own, or not at this line, in
                this order or with the tile at this input.
        """
        raise ValueError(f"{type(self).__name__} runs on cores of its own")

    def finish_step(self, link: Link, line: int, dtype, dev, ordered: bool) -> Link:
        """``link`` as this operator's cores apply it to a ``line``-element
        tile of its output: the step's own kernels, run at the tile
        (``Link.at_line``), unless the operator applies its finish another way.

        Raises:
            ValueError: The cores do not apply the step at the tile.
        """
        return link.at_line(line, dtype, dev, ordered)

    def finish_line(self, dev, lines: Iterable[int]) -> int:
        """The first of ``lines`` each chain of this operator's array
        finishes a tile of, for a ``resolve`` choosing its output's tile.

        Raises:
            Unresolvable: None of them.
        """
        links = [link for c in self.finish.chains for link in c]
        out = self.outputs[0]
        ordered = out.finish_block is None
        tried = []
        for line in lines:
            try:
                for link in links:
                    link.at_line(line, out.dtype, dev, ordered)
            except ValueError as e:
                tried.append(f"{line}: {e}")
                continue
            return line
        raise Unresolvable(
            f"{type(self).__name__}: no output tile its finish runs at; "
            + "; ".join(tried)
        )

    def finish_bytes(self, dev, line: int) -> int:
        """Core memory a core spends on this operator's finish at a
        ``line``-element output tile, beside its own buffers: the scratch
        line its chains alternate with and, on AIE2, the tables of each LUT
        kernel they link.

        Raises:
            ValueError: A step does not run at the line.
        """
        chains = self.finish.chains
        if not any(chains):
            return 0
        out = self.outputs[0]
        ordered = out.finish_block is None
        luts = {
            call.kernel.object_file_name
            for chain in chains
            for link in chain
            for call in link.at_line(line, out.dtype, dev, ordered).op.chain()
            if call.kernel.contract is not None and call.kernel.contract.uses_lut
        }
        tables = LUT_BYTES * len(luts) if dev.arch is AIEArch.AIE2 else 0
        return line * np.dtype(out.dtype).itemsize + tables

    def device(self):
        """The device the array's Program is built for: the bound device
        unless the array takes a part of it.
        """
        return self.dev

    @property
    def external(self):
        return type(self)._external

    def configuration(self) -> Self:
        """The operator whose xclbin this one runs when it runs alone."""
        return self

    def exported_design(self):
        """The design another tool exports for this operator; ``None`` derives it."""
        return None

    def check_shim_columns(self, dev, cols: int, num_channels: int = 1) -> None:
        allowed = self.declaration.shim_columns(
            dev, num_channels, vars(self), self._finish_inputs
        )
        if cols > allowed:
            raise Unresolvable(
                f"{type(self).__name__} with {cols} columns x {num_channels} "
                f"channels exceeds this device's shim DMA budget; "
                f"{allowed} columns fit"
            )

    def resolve_columns(
        self,
        dev,
        given: int | None,
        num_channels: int = 1,
        *,
        fits: Callable[[int], bool] | None = None,
    ) -> int:
        """``given``, checked against the shim budget, or the most columns that ``fits``.

        When no count fits, one column is returned and ``compatible`` names the rule.
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
        budget = self.declaration.shim_columns(
            dev, num_channels, vars(self), self._finish_inputs
        )
        return next((c for c in range(budget, 0, -1) if fits is None or fits(c)), 1)

    def addressed_inputs(
        self, addresses: Mapping[str, int], rng: np.random.Generator
    ) -> dict[str, np.ndarray]:
        """What the inputs that name device addresses hold, for a run alone.

        Random bytes in such an input would steer the operator's DMA
        anywhere; every other input is safe to fill at random.

        Args:
            addresses: Each of the operator's buffers' device addresses, by
                buffer name.
            rng: The generator any representative content is drawn from.

        Returns:
            Each such input's content, by buffer name.
        """
        return {}

    def reference(self, *inputs):
        raise NotImplementedError(
            f"{type(self).__name__}.reference() is not implemented"
        )

    def _call_reference(
        self,
        inputs: Mapping[str, np.ndarray],
        outputs: Mapping[str, np.ndarray] | None = None,
        values: Mapping[str, Any] | None = None,
    ) -> dict[str, np.ndarray]:
        """Run `reference` on buffers named as this operator declares them.

        The inputs are its positional arguments, in declaration order; a
        prologue and a finish run around it on the host, given their steps'
        other inputs. An output it names a parameter after (Copy's `y`) is
        given to it, to write in place what it touches.

        Args:
            inputs: Every input, an `inout` buffer among them, by buffer name.
            outputs: Outputs by buffer name; the reference is given those it
                names.
            values: Per-call values by name; the reference is given those it
                names that are not None.

        Returns:
            The reference's result for each buffer this operator writes, by
            buffer name.

        Raises:
            ValueError: `inputs` are not this operator's, `outputs` name a
                buffer that is not its output, or the reference returns
                another number of results than this operator writes, or None
                for one.
        """
        name = type(self).__name__
        declared = [b.name for b in self.inputs]
        if sorted(inputs) != sorted(declared):
            raise ValueError(
                f"{name} takes the inputs {declared}, not {sorted(inputs)}"
            )
        outputs = outputs or {}
        unknown = set(outputs) - {b.name for b in self.outputs}
        if unknown:
            raise ValueError(f"{name} has no output {sorted(unknown)}")
        # elementwise.py builds on this module.
        from ..elementwise import Finish, Prepare

        args = [inputs[n] for n in declared]
        own = len(args) - len(self.prepare_inputs) - len(self.finish_inputs)
        prologue = args[own : own + len(self.prepare_inputs)]
        finishing = args[own + len(self.prepare_inputs) :]
        args = args[:own]
        if self.prepare:
            at = next(i for i, b in enumerate(self.inputs) if b.prepare)
            args[at] = Prepare(self.resolved()).reference(args[at], *prologue)
        named = inspect.signature(self.reference).parameters
        result = self.reference(
            *args,
            **{k: v for k, v in outputs.items() if k in named},
            **{k: v for k, v in (values or {}).items() if k in named and v is not None},
        )
        if self.finish:
            result = Finish(self.resolved()).reference(result, *finishing)
        results = result if isinstance(result, tuple) else (result,)
        written = [b.name for b in self.outputs]
        if len(results) != len(written) or any(r is None for r in results):
            raise ValueError(
                f"{name}.reference returned {results!r:.80} for {written}; "
                f"it returns each buffer it writes, an output written in place "
                f"among them"
            )
        return dict(zip(written, results))

    def judge(
        self,
        inputs: Mapping[str, np.ndarray],
        written: Mapping[str, np.ndarray],
        tolerance: Tolerance,
        expected: Mapping[str, np.ndarray] | None = None,
    ) -> dict[str, Verdict]:
        """Each buffer this operator writes held to its reference result.

        Args:
            inputs: The inputs it was given, by buffer name; a bound
                tolerance is evaluated on them, in declaration order.
            written: What it wrote to each buffer it writes, by buffer name.
            tolerance: What every written buffer is judged by.
            expected: Each written buffer's reference result, by buffer
                name; `call_reference` on `inputs` where None.

        Returns:
            Each written buffer's verdict, by buffer name.

        Raises:
            ValueError: `written` or `expected` do not name every buffer this
                operator writes and no other, an expected result is None, or
                a written buffer holds another number of elements than its
                result.
        """
        if expected is None:
            expected = self._call_reference(inputs)
        names = [b.name for b in self.outputs]
        for given, what in ((written, "written"), (expected, "expected")):
            if sorted(given) != sorted(names):
                raise ValueError(
                    f"{type(self).__name__} writes {names}; the {what} "
                    f"buffers are {sorted(given)}"
                )
        unknown = [n for n in names if expected[n] is None]
        if unknown:
            raise ValueError(f"{type(self).__name__}: no expected result for {unknown}")
        bound = None
        if tolerance.kind == "bound":
            bound = tolerance.bound(*(inputs[b.name] for b in self.inputs))
        return {
            n: compare(
                np.reshape(written[n], np.shape(expected[n])),
                expected[n],
                tolerance,
                bound=bound,
            )
            for n in names
        }

    def sequence(self, rt) -> None:
        """Override to write the runtime sequence by hand; otherwise it is derived."""
        raise NotImplementedError

    @classmethod
    def has_sequence_override(cls) -> bool:
        return cls.sequence is not Operator.sequence

    def design_key(self):
        """Identity for sharing a build: equal keys generate byte-identical MLIR.

        An Enum field (GEMM's and MHA's placements) is its own value, not
        the member: a rename must not move a design's key.
        """
        own = tuple(
            (f.name, v.value if isinstance(v := getattr(self, f.name), Enum) else v)
            for f in dataclasses.fields(self)
            if f.compare
        )
        if self.bound_values:
            names = {
                k: None if v is None else v.name for k, v in self.bound_values.items()
            }
            own += (("values", tuple(sorted(names.items()))),)
        if self.placements:
            own += (("placements", self.placements),)
        if self.finish:
            own += (("finish", self.finish.array_key()),)
        if any(self.finish.shared):
            own += (("finishes", self.finish.keys()),)
        if self.prepare:
            own += (("prepare", self.prepare.array_key()),)
        if any(self.prepare.shared):
            own += (("prepares", self.prepare.keys()),)
        return (type(self), own)

    def _probed(self) -> Self:
        """This operator with each ``Param(probe=)`` field at its probe: the
        one its step time is measured as, for every value of those fields.
        Itself when they are there already, unresolved otherwise.
        """
        if all(getattr(self, n) == v for n, v in self.declaration.probes.items()):
            return self
        return dataclasses.replace(self, **self.declaration.probes)

    def array_key(self):
        key = (type(self),) + tuple(
            (name, v.value if isinstance(v := getattr(self, name), Enum) else v)
            for name in self.declaration.array
        )
        if self.trace is not None:
            key += (("trace", self.trace),)
        if any(self.finish.chains):
            key += (("finishes", self.finish.keys()),)
        if any(self.prepare.chains):
            key += (("prepares", self.prepare.keys()),)
        return key

    def resolved(self, dev=None) -> Self:
        """This operator resolved for ``dev`` (the bound device unless given), checked."""
        if self._resolved:
            return self
        new = self.resolve(dev if dev is not None else self.dev)
        if new is self:
            raise TypeError(
                f"{type(self).__name__}.resolve() must return a copy, "
                f"dataclasses.replace(self, ...), not self"
            )
        if not isinstance(new, type(self)):
            raise TypeError(
                f"{type(self).__name__}.resolve() must return a {type(self).__name__}"
            )
        missing = [n for n in self.declaration.autos if getattr(new, n) is None]
        if missing:
            raise Unresolvable(
                f"{type(self).__name__}.resolve() left {missing} unset for {dev}"
            )
        if any(new.prepare.chains):
            new._prepare_at(dev if dev is not None else self.dev)
        if any(new.finish.chains):
            new._finish_at(dev if dev is not None else self.dev)
        new.validate()
        new.compatible()
        new._resolved = True
        return new

    def _finish_at(self, dev) -> None:
        """Rebuild each finish at the output tile, the array's unique and in
        a fixed order.

        Raises:
            ValueError: No output is finished by the array that runs, or
                the chain does not rebuild at the tile (``Chain.rebuilt``).
            Unresolvable: Each core reads more streams, its own and the
                finish's inputs, than a core tile has input channels, a
                finish input would stream into a block held out of order,
                or the finish's inputs do not fit the tiles or the
                descriptors of the input they ride (`feed=True`).
        """
        out = self.outputs[0] if len(self.outputs) == 1 else None
        # A subclass replacing array() does not apply what its base's output declares.
        runs = next(k for k in type(self).__mro__ if "array" in vars(k))
        if out is None or not out.finish or runs not in out.owner.__mro__:
            raise ValueError(
                f"{type(self).__name__}: its cores finish no output, so it "
                f"applies no finish"
            )
        name = type(self).__name__
        ordered = out.finish_block is None
        finish = self.finish.rebuilt(
            lambda link: self.finish_step(
                link, out.finish_line, out.dtype, dev, ordered
            ),
            owner=name,
            what="finish",
        )
        if not ordered and any(len(link.op.inputs) > 1 for link in finish):
            raise Unresolvable(
                f"{name}: its cores hold each block of the output in an order "
                f"of their own, which a finish input does not stream in"
            )
        self.finish = finish
        self._bind()
        reads = sum(m.fills and m.tile_dims is not None for m in self._members_io())
        if reads > dev.core_dma_channels_in:
            raise Unresolvable(
                f"{name}: its cores read {reads} streams with the finish's "
                f"inputs, past a core tile's {dev.core_dma_channels_in} input "
                f"channels, and no input of its is declared feed=True for them "
                f"to ride"
            )
        riding = [b for b in self.finish_inputs if not b.streamed]
        if not riding:
            return
        feed = next(b for b in self.inputs if b.feed)
        carried, line = math.prod(feed.tile_shape), math.prod(out.tile_shape)
        # The rest of the tile re-reads the input's: a shim descriptor's iterations.
        repeats = carried // line
        if feed.bounded is not None or out.bounded is not None:
            raise Unresolvable(
                f"{name}: the finish's inputs ride {feed.name} an output tile at "
                f"a time, which a per-call bound does not move by"
            )
        if feed.count != out.count:
            raise Unresolvable(
                f"{name}: the finish's inputs ride {feed.name}'s {feed.count} "
                f"lanes, which are not {out.name}'s {out.count}"
            )
        if feed.dtype != out.dtype:
            raise Unresolvable(
                f"{name}: the finish's inputs, of {out.name}'s dtype, ride "
                f"{feed.name}, whose tiles are of another"
            )
        if carried % line or repeats > 1 << dev.get_dma_bd_iter_bits(0, 0):
            raise Unresolvable(
                f"{name}: a {line}-element tile of the finish's inputs fills a "
                f"{carried}-element tile of {feed.name} in at most "
                f"{1 << dev.get_dma_bd_iter_bits(0, 0)} whole reads, and does not"
            )
        if len(riding) > feed.depth:
            raise Unresolvable(
                f"{name}: the finish's {len(riding)} inputs ride {feed.name}, "
                f"whose cores hold {feed.depth} tiles of it at once"
            )
        # Every one is live until the drains: a shim tile's descriptors serve
        # both directions of each of its channels, a lane its share of them.
        transfers = (1 + len(riding)) * out.elements // (out.count * line)
        shims = sum(
            dev.get_tile_type(col, 0) is AIETileType.ShimNOCTile
            for col in range(dev.cols)
        )
        held = (
            dev.get_num_bds(AIETileType.ShimNOCTile)
            * shims
            // (dev.shim_dma_channels_in + dev.shim_dma_channels_out)
        )
        if transfers > held:
            raise Unresolvable(
                f"{name}: a lane of {feed.name} carrying the finish's inputs is "
                f"{transfers} transfers, one per tile of each, past the {held} "
                f"descriptors a lane of a shim tile holds"
            )

    def _prepare_at(self, dev) -> None:
        """Rebuild each prologue at the prepared input's tile, the array's
        unique and in a fixed order.

        Raises:
            ValueError: No input is prepared, or the chain does not rebuild
                at the tile (``Chain.rebuilt``).
            Unresolvable: A step's other input is not one tile, the
                prepared input brings a core more than one tile a call,
                beside which no other input's tile streams, or, untiled,
                its steps' inputs do not fit the tiles of the input they
                ride (`feed=True`).
        """
        into = next((b for b in self.inputs if b.prepare), None)
        if into is None:
            raise ValueError(
                f"{type(self).__name__}: its cores prepare no input, so it "
                f"applies no prologue"
            )
        name = type(self).__name__
        line = math.prod(into.tile_shape) if into.streamed else into.shape[-1]
        for link in self.prepare:
            for k, b in enumerate(link.op.inputs):
                if k != link.at and b.elements != line:
                    raise Unresolvable(
                        f"{name}: {type(link.op).__name__}.{b.name} "
                        f"is {b.elements} elements, not the {line}-element tile "
                        f"it streams in beside"
                    )
        riding = sum(len(link.op.inputs) - 1 for link in self.prepare)
        tiles = into.elements // (
            1 if not into.streamed or into.replicate else into.count
        )
        if riding and tiles != line:
            raise Unresolvable(
                f"{name}: each core takes {tiles // line} tiles of "
                f"{into.name} a call, and a prologue's inputs stream in beside one"
            )
        if riding and not into.streamed:
            feed = next(b for b in self.inputs if b.feed)
            if feed.dtype != into.dtype or math.prod(feed.tile_shape) < line:
                raise Unresolvable(
                    f"{name}: the prologue's inputs ride {feed.name}, whose "
                    f"tiles do not hold a {line}-element line of {into.name}'s type"
                )
            if riding > feed.depth:
                raise Unresolvable(
                    f"{name}: the prologue's {riding} inputs ride {feed.name}, "
                    f"whose cores hold {feed.depth} tiles of it at once"
                )
        self.prepare = self.prepare.rebuilt(
            lambda link: link.at_line(line, into.dtype, dev),
            owner=name,
            what="prologue",
        )
        self._bind()

    def copy(self) -> Self:
        """A fresh instance for one build, keeping resolution and bound values."""
        new = dataclasses.replace(self)
        new._resolved = self._resolved
        if self._resolved:
            # replace() resets the init=False fields compatible() records.
            new.compatible()
        return new

    def _with_tunables(self, **tunables: Any) -> Self:
        """This operator, unresolved, with the given ``Auto()`` fields set.

        Raises:
            TypeError: A name is not a settable tunable: not an ``Auto()``
                field, fixed with ``init=False``, or ``derived``.
        """
        unknown = [n for n in tunables if n not in self.declaration.tunables]
        if unknown:
            raise TypeError(f"{type(self).__name__} has no tunable {unknown}")
        return dataclasses.replace(self, **tunables)

    @property
    def _widths(self) -> dict[str, int | None]:
        """The tunables searched as a `Width`, and their values: those that
        declare one, and those a streamed ``per=`` names that declare no
        other domain.
        """
        found = {
            n: getattr(self, n)
            for n, domain in self.declaration.domains.items()
            if isinstance(domain, Width)
        }
        for b in self.buffers:
            for ref in b.per.dims if b.streamed and b.per else ():
                if (
                    isinstance(ref, Param)
                    and ref.name in self.declaration.tunables
                    and ref.name not in self.declaration.domains
                ):
                    found.setdefault(ref.name, getattr(self, ref.name))
        return found

    def _domains(self, dev) -> dict[str, tuple[Any, ...]]:
        """The values the tuner tries for each tunable it searches, asked of
        the resolved operator: the field's declared domain where its
        ``when`` flag holds, a `Width` for one of `widths`, and nothing for
        any other. A combination the operator cannot resolve at is left
        out by the tuner. A ``pinned`` tunable is not searched.

        A fixed tuple is the resolved value's own, the resolved one first if
        it is not already there; an `Enum`-annotated field with no domain is
        searched over that `Enum`'s members, the resolved one first (GEMM's
        and MHA's placements: a hand-found default tried before the rest).
        """
        widths = self._widths
        found = {}
        for name in dict.fromkeys([*widths, *self.declaration.tunables]):
            domain = self.declaration.domains.get(
                name, Width() if name in widths else None
            )
            if name in self.pinned or domain is None:
                continue
            when = domain.when if isinstance(domain, Domain) else None
            if when is not None and not when(self, dev):
                continue
            start = vars(self)[name]
            if isinstance(domain, tuple):
                found[name] = domain if start in domain else (start, *domain)
            elif isinstance(domain, type):  # an Enum, auto-detected
                found[name] = (start, *(m for m in domain if m != start))
            else:
                found[name] = domain.values(self, dev, start)
        return found

    @property
    def buffers(self) -> list[Operand]:
        return [self._bound[m.name] for m in self._members_io()]

    @property
    def inputs(self) -> list[Operand]:
        return [b for b in self.buffers if b.fills]

    @property
    def outputs(self) -> list[Operand]:
        return [b for b in self.buffers if b.drains]

    @property
    def prepare_inputs(self) -> list[Operand]:
        """The inputs of ``prepare``'s steps other than the tile, in order,
        each a tile filled into the prepared input's stream after it (an
        untiled one's ``feed=True`` input): the inputs after the declared
        ones.
        """
        return [self._bound[m.name] for m in self._prepare_inputs]

    @property
    def finish_inputs(self) -> list[Operand]:
        """The inputs of ``finish``'s steps other than the tile, in order,
        each streamed as the finished output is: the last of ``inputs``.
        """
        return [self._bound[m.name] for m in self._finish_inputs]

    @property
    def values(self) -> list[Value]:
        """The per-call values: each gets a device parameter."""
        values = [self._bound[m.name] for m in self._value_members]
        return [v for v in values if v.per_call]

    @property
    def residents(self) -> dict[str, Any]:
        """What the preamble writes once per build, by name."""
        fixed = self._derived_under_bound()
        return {
            m.name: m.derive(self) if fixed.get(m.name) is None else fixed[m.name]
            for m in (*self.declaration.members, *self._chain_words)
            if isinstance(m, Value)
            and m.derive is not None
            and not self._bound[m.name].per_call
        }

    def rtp(self, values: list[Value], cores: int = 1) -> list[Rtp]:
        """The runtime parameters of ``cores`` cores, each reading ``values``.

        Each is a Worker argument whose core reads its words once a call
        with ``Rtp.read``, keyed by value; the preamble writes them, syncs
        the scratchpad and opens each, before any DMA.

        Args:
            values: Values of this operator, in the order the core reads them.
            cores: How many cores read them, each its own block.

        Returns:
            One ``Rtp`` per core.
        """
        rtps = [Rtp(values) for _ in range(cores)]
        vars(self)["_rtps"] = [*self.rtps, *rtps]
        return rtps

    @property
    def rtps(self) -> list[Rtp]:
        """Every core's runtime parameters ``array()`` made (``rtp``)."""
        return vars(self).get("_rtps", [])

    @property
    def bound_extents(self) -> dict[str, Affine | None]:
        bound = self.bound_values
        return {
            m.name: bound[m.name]
            for m in self.declaration.members
            if isinstance(m, Extent) and m.name in bound
        }

    def _per_call_derived(self) -> frozenset[str]:
        return frozenset(k for k, v in self._derived_under_bound().items() if v is None)

    def _derived_under_bound(self) -> dict[str, int | None]:
        """Each derived value that reads a bound extent: the number it is at
        every bound (``n - n``, ``(4 * n) // n``), or None where it follows
        the call.
        """
        bound = self.bound_extents
        if not bound:
            return {}
        # From array(), derivations run on the operator: reading an extent here is not the array's.
        op = vars(self).get("_unfenced", self)
        probe = copy.copy(op)
        forms = None if None in bound.values() else bound
        out: dict[str, int | None] = {}
        for m in self._value_members:
            if not (isinstance(m, Value) and m.derive is not None):
                continue
            reads: set[str] = set()
            vars(probe)["_extent_reads"] = reads
            try:
                m.derive(probe)
            except Exception:
                pass  # unresolved: what it read before failing still counts
            if not reads & bound.keys():
                continue
            out[m.name] = None
            if forms is None:
                continue
            try:
                got = op.derived_at(m.name, **forms)
            except Exception:
                continue  # no form, or unresolved: per call either way
            if isinstance(got, (int, np.integer)) and not isinstance(got, bool):
                out[m.name] = int(got)
        return out

    def derived_at(self, name: str, **extents: int) -> Any:
        """The word the host writes for ``name`` with the extents at the given bounds."""
        member = next((m for m in self._value_members if m.name == name), None)
        if not (isinstance(member, Value) and member.derive is not None):
            raise TypeError(f"{type(self).__name__}.{name} is not a derived value")
        unknown = set(extents) - {
            m.name for m in self.declaration.members if isinstance(m, Extent)
        }
        if unknown:
            raise TypeError(
                f"{type(self).__name__} declares no Extent {sorted(unknown)}"
            )
        at = copy.copy(self)
        vars(at)["_extents"] = {**self.__dict__.get("_extents", {}), **extents}
        return member.derive(at)

    def extent_unit(self, buffer: str) -> int | None:
        """The rows of ``buffer`` one lane takes at a time under a bound.

        ``None`` for the stream tile's rows; ``0`` when a bound does not shorten it.
        """
        return None

    def value_buffer(self, name: str) -> Operand:
        b = self._bound.get(name)
        if not isinstance(b, Operand):
            raise TypeError(f"{type(self).__name__} declares no operand {name!r}")
        return b

    def value(self, name: str) -> Value:
        """The device word of value ``name`` (an ``Extent`` attribute reads as an integer)."""
        try:
            return self._bound[name]
        except KeyError:
            raise TypeError(
                f"{type(self).__name__} declares no value {name!r}"
            ) from None

    def use_value(self, name: str, bound_to: Affine | None = None) -> None:
        """Record that a graph binds the per-call value ``name`` to its expression ``bound_to``."""
        if not any(m.name == name for m in self._value_members):
            raise TypeError(
                f"{type(self).__name__} declares no per-call value {name!r}"
            )
        # Rebound, not updated: replace() hands a copy the same dict.
        self.bound_values = {**self.bound_values, name: bound_to}

    def compile(self) -> Artifacts:
        """Build the image this operator runs on outside a graph, once.

        Returns:
            What the build produced: the xclbin, the instruction stream and
            the cache entry holding them.
        """
        if self._image is None:
            # The image layer builds on this one: imported here to break the cycle.
            from ..image.standalone import OperatorImage

            self._image = OperatorImage(self)
        return self._image.compile().artifacts

    def __call__(self, *args, **kwargs):
        """Inside a graph's body, a step on its handles; outside one, a run
        of this operator's own image (``compile``) on device tensors, one per
        declared buffer in declaration order, ``kwargs`` its ``DispatchTime``
        values by device symbol.
        """
        tracer = graph_tracer.get()
        if tracer is not None:
            return tracer.call(self, args, kwargs)
        names = [b.name for b in self.buffers]
        if len(args) != len(names) or not all(isinstance(a, NpuTensor) for a in args):
            raise TypeError(
                f"{type(self).__name__} runs outside a graph's body on device "
                f"tensors, one per declared buffer {names}; got "
                f"{[type(a).__name__ for a in args]}"
            )
        self.compile()
        return self._image(*args, **kwargs)

    def _bind(self) -> None:
        self._prepare_inputs = ()
        self._finish_inputs = ()
        prepared = next((m for m in self._members_io() if m.prepare), None)
        extras = []
        for i, link in enumerate(self.prepare if prepared is not None else ()):
            line = (prepared.tile_dims or prepared.dims).dims[-1:]
            for k, b in enumerate(link.op.inputs):
                if k == link.at:
                    continue
                extra = In(*line, dtype=prepared.declared_dtype)
                extra.__set_name__(type(self), f"prepare{i}_{b.name}")
                extras.append(extra)
        self._prepare_inputs = tuple(extras)
        outs = [m for m in self._members_io() if m.drains]
        extras = []
        if len(outs) == 1 and outs[0].finish:
            (out,) = outs
            # Riding a feed, an input is no stream of its own (OperatorRuntime.fill).
            fed = any(m.feed for m in self._members_io())
            for i, link in enumerate(self.finish):
                for k, b in enumerate(link.op.inputs):
                    if k == link.at:
                        continue
                    extra = In(
                        *out.dims.dims,
                        dtype=out.declared_dtype,
                        tile=None if fed else out.tile_dims.dims,
                        per=None if fed or out.per is None else out.per.dims,
                        depth=out.depth,
                    )
                    extra.__set_name__(type(self), f"finish{i}_{b.name}")
                    extras.append(extra)
        self._finish_inputs = tuple(extras)
        bound: dict[str, Any] = {}
        for m in self._members_io():
            bound[m.name] = m.of(self)
        for m in self.declaration.members:
            if isinstance(m, Value):
                bound[m.name] = m.of(self)
        self._bound = bound
        words = []
        for e in self.declaration.members:
            if not isinstance(e, Extent):
                continue
            for b in self._members_io():
                # Asked first: an unshortened shape may Select on an Auto() field.
                if b.tile_dims is not None and self.extent_unit(b.name) != 0:
                    axis = bound[b.name].extent_axis(e)
                    if axis is not None:
                        word = ExtentWord(type(self), e, b.name, axis)
                        bound[word.name] = word.of(self)
                        words.append(word)
        self._extent_words = tuple(words)
        self._chain_words: tuple[ChainWord, ...] = ()
        for finish, chain in ((False, self.prepare), (True, self.finish)):
            if len(chain.shared) > 1:
                word = ChainWord(type(self), finish)
                bound[word.name] = word.of(self)
                self._chain_words += (word,)
        self._place_words = tuple(
            PlaceWord(type(self), m.name) for m in self._members_io()
        )
        for word in self._place_words:
            bound[word.name] = word.of(self)

    @property
    def _value_members(self) -> list[Value]:
        return [m for m in self.declaration.members if isinstance(m, Value)] + [
            *self.__dict__.get("_extent_words", ()),
            *self.__dict__.get("_chain_words", ()),
            *self.__dict__.get("_place_words", ()),
        ]

    @classmethod
    def from_operands(cls, *operand_shapes, **overrides) -> Self:
        """Construct from operand shapes, an optional input's by keyword."""
        inputs, outputs, overrides = cls.declaration.call_operands(
            operand_shapes, overrides
        )
        return cls(
            **{**overrides, **cls.declaration.infer(inputs, outputs, **overrides)}
        )

    @property
    def dev(self):
        return aie_utils.ensure_current_device()

    @property
    def name(self) -> str:
        """The label of the resolved operator: its class, shown fields and device."""
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                f"{type(self).__name__}: the label names the device; none is bound"
            )
        op = self.resolved(dev)
        own = []
        for f in dataclasses.fields(op):
            v = getattr(op, f.name)
            if not f.repr or v is None:
                continue
            if isinstance(v, bool):
                v = int(v)
            elif isinstance(v, float):
                # repr() round-trips; a symbol takes neither '.' nor '-'.
                v = repr(v).replace(".", "p").replace("-", "n").replace("+", "")
            elif isinstance(v, tuple) and all(
                isinstance(x, TensorAccessPattern) for x in v
            ):
                # A gather's rows, one pattern each: too many to spell out.
                digest = hashlib.sha256(repr(v).encode()).hexdigest()[:8]
                v = f"{len(v)}p{digest}"
            elif isinstance(v, (list, tuple)):
                v = "x".join(str(x) for x in v)
            elif isinstance(v, TensorAccessPattern):
                v = (
                    f"o{v.offset}s{'x'.join(map(str, v.sizes))}"
                    f"t{'x'.join(map(str, v.strides))}"
                )
            own.append(f"{f.name}{v}")
        if any(op.finish.chains):
            # A step's scalars and the array's other finishes change the build too.
            keys = (op.finish.array_key(), op.finish.keys())
            digest = hashlib.sha256(repr(keys).encode()).hexdigest()[:8]
            names = "".join(type(link.op).__name__ for link in op.finish)
            own.append(f"finish{names}{digest}")
        if any(op.prepare.chains):
            keys = (op.prepare.array_key(), op.prepare.keys())
            digest = hashlib.sha256(repr(keys).encode()).hexdigest()[:8]
            names = "".join(type(link.op).__name__ for link in op.prepare)
            own.append(f"prepare{names}{digest}")
        return "_".join([type(self).__name__, *own, dev.name])

    def _members_io(self) -> list[Operand]:
        return [
            m
            for m in self.declaration.members
            if isinstance(m, Operand) and (m.when is None or getattr(self, m.when.name))
        ] + [*self._prepare_inputs, *self._finish_inputs]

    def __repr__(self) -> str:
        own = ", ".join(
            f"{f.name}={getattr(self, f.name)!r}"
            for f in dataclasses.fields(self)
            if f.repr
        )
        return f"{type(self).__name__}({own})"
