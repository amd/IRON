# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A text model whose placeholder tokens take its towers' soft tokens, as
Hugging Face's ``masked_scatter`` places them: the j-th of a token's
placeholders takes its tower's j-th soft token.
"""

import inspect

import aie.utils as aie_utils
import numpy as np

import iron
from iron.operators.copy import Copy
from iron.operators.merge import Merge

from .base import Model
from .causal import CausalLM
from .encoder import Encoder, Tower
from .generation import Sampler


class Multimodal(Model):
    """A text model and its towers, keyed by placeholder token, as one graph.

    Its versions are the text model's own, one per tower, and ``placed``. A
    tower's takes its input and writes its soft tokens into ``merged`` from
    its own row. ``placed``, the ids with their placeholders, writes the
    text's rows into ``merged`` from its first row; ``Merge`` then gives each
    position its row of ``merged``, and the text model runs over those rows.
    A causal text model runs a prompt in chunks: its placed version is a
    prompt chunk, and takes ``before`` too, the count of each placeholder
    before the chunk, so a run of placeholders may cross chunks. A version
    is one dispatch with its own scratchpad, which all of them in one would
    overrun. A tower's per-call values are named after its input: a vision
    tower's ``n`` on input ``rgb`` is ``rgb_n``.

    Args:
        text: The text model.
        towers: Each tower, by the token its placeholders are.

    Raises:
        TypeError: Two inputs or values share a name, or a tower takes other
            than one input.
    """

    def __init__(self, text: Encoder | CausalLM, towers: dict[int, Tower]):
        self.text = text
        self.towers = towers
        P = inspect.Parameter
        parameters = list(text.signature().parameters.values())
        self.text_inputs = [p.name for p in parameters if p.kind is not P.KEYWORD_ONLY]
        self.text_values = [p.name for p in parameters if p.kind is P.KEYWORD_ONLY]
        self.tower_inputs, self.tower_values = {}, {}
        for token, tower in towers.items():
            parameters = list(tower.signature().parameters.values())
            inputs = [p.name for p in parameters if p.kind is not P.KEYWORD_ONLY]
            if len(inputs) != 1:
                raise TypeError(f"Multimodal: a tower takes one input, not {inputs}")
            self.tower_inputs[token] = inputs[0]
            self.tower_values[token] = [
                p.name for p in parameters if p.kind is P.KEYWORD_ONLY
            ]
        (ids,) = [s["ids"] for s in text.shapes() if "ids" in s]
        (rows,), _ = ids
        self.at = {}
        for token, tower in towers.items():
            self.at[token] = rows
            rows += tower.soft_rows
        self.merged = iron.state((rows, text.config.hidden_size))
        # What each tower ran on last, so a causal model's caches outlive a
        # call with the same.
        self._last_raw: dict[int, tuple] = {}
        self.signature()

    def signature(self) -> inspect.Signature:
        P = inspect.Parameter
        inputs, values = [], []
        owners = [(self.text, "")] + [
            (tower, f"{self.tower_inputs[token]}_")
            for token, tower in self.towers.items()
        ]
        for owner, prefix in owners:
            for p in owner.signature().parameters.values():
                if p.kind is P.KEYWORD_ONLY:
                    values.append(p.replace(name=prefix + p.name))
                else:
                    inputs.append(p.replace(default=None))
        placed = ["placed", "before"] if isinstance(self.text, CausalLM) else ["placed"]
        inputs += [P(n, P.POSITIONAL_OR_KEYWORD, default=None) for n in placed]
        parameters = inputs + values
        names = [p.name for p in parameters]
        if len(set(names)) != len(names):
            raise TypeError(f"Multimodal: inputs and values {names} repeat a name")
        return inspect.Signature(parameters)

    def body(self, *inputs, **values):
        given = {n: x for n, x in zip(self._inputs, inputs) if x is not None}
        if len(set(given) - {"before"}) > 1:
            raise TypeError(f"a version takes one input, got {sorted(given)}")
        text = {v: values[v] for v in self.text_values}
        for token, tower in self.towers.items():
            name = self.tower_inputs[token]
            if name in given:
                own = {v: values[f"{name}_{v}"] for v in self.tower_values[token]}
                soft = tower(given[name], **own)
                at = self.at[token]
                Copy.step(soft, self.merged[at : at + soft.shape[0]])
                # A text model's carried values pass through unchanged.
                if self._carried:
                    return iron.carry(**{n: values[n] for n in self._carried})
                return None
        if "placed" not in given:
            inputs = [given.get(n) for n in self.text_inputs]
            return self.text.inline(self.text.body, *inputs, **text)
        placed, n = given["placed"], text[self.text.bound]
        # An input's gather is encoded on the host into its buffer, which Merge
        # reads as the ids: gather by the device's copy of them.
        ids = Copy.step(placed, dtype=np.int32)[:n]
        x = self.text.inline(self.text.lookup, ids)
        counted = {"before": given["before"]} if "before" in given else {}
        merge = Merge.step(placed, placeholders=tuple(self.at.items()), **counted)
        Copy.step(x, self.merged[: x.shape[0]])
        rows = Copy.step(self.merged[merge])[:n]
        return self.text.inline(self.text.from_rows, rows, **text)

    def shapes(self) -> list[dict]:
        """The input shapes of each version: the text model's, each tower's,
        and the ids with their placeholders (and a causal model's counts).
        """
        text = self.text.shapes()
        (ids,) = [s["ids"] for s in text if "ids" in s]
        towers = [s for t in self.towers.values() for s in t.shapes()]
        placed = dict(placed=ids)
        if isinstance(self.text, CausalLM):
            placed["before"] = ((len(self.towers),), np.int32)
        return [*text, *towers, placed]

    def load(
        self,
        *,
        release=None,
        tuner=None,
        full_elf: bool | None = None,
        dev=None,
    ) -> "Multimodal":
        """Compile and load every version before the first call, in one
        arena, each version taking ids feeding the decode step a causal text
        model has, and hand a causal text model its versions (``use``).

        Args:
            release: Given each piece of each weight once it is on the device.
            tuner: Folds, narrows and packs each version's designs by cost.
            full_elf: Each version's packaging (``Graph.compile``).
            dev: The device every version compiles for, else the current one.
        """
        if dev is None:
            dev = aie_utils.ensure_current_device()
        compiled, decode = [], None
        for shapes in self.shapes():
            prompt = "ids" in shapes or "placed" in shapes
            version = self.compile(
                dev=dev,
                feeds=decode if prompt else None,
                tuner=tuner,
                full_elf=full_elf,
                **shapes,
            )
            version.load(release=release)
            if not shapes and version.emit is not None:
                decode = version
            compiled.append(version)
        if isinstance(self.text, CausalLM):
            decode_step, prompt_chunk, *_, placed = compiled
            self.text.use(decode_step, prompt_chunk, placed, tuple(self.at))
        return self

    def longest(self) -> dict:
        """The per-call values of the longest call: the text model's and each
        tower's.
        """
        values = dict(self.text.longest())
        for token, tower in self.towers.items():
            name = self.tower_inputs[token]
            values |= {f"{name}_{v}": x for v, x in tower.longest().items()}
        return values

    def tower_calls(self, tokens, raw: dict[int, tuple]) -> tuple[list[tuple], dict]:
        """The inputs of each tower version ``raw`` runs, and every tower's
        per-call values, zero for a tower left out.

        Args:
            tokens: The token ids, each placeholder run as long as its
                tower's soft tokens.
            raw: Each tower's raw input, as its ``inputs`` takes it, by
                placeholder token.

        Raises:
            ValueError: A placeholder's count is not its tower's soft tokens.
        """
        tokens = np.asarray(tokens)
        names = list(self._inputs)
        calls, values = [], {}
        for token, tower in self.towers.items():
            name = self.tower_inputs[token]
            own = {v: 0 for v in self.tower_values[token]}
            soft = 0
            if token in raw:
                buffer, own = tower.inputs(*raw[token])
                soft = tower.soft(own)
                calls.append(tuple(buffer if n == name else None for n in names))
            values |= {f"{name}_{v}": x for v, x in own.items()}
            places = np.count_nonzero(tokens == token)
            if places != soft:
                raise ValueError(
                    f"{places} placeholders {token} for {soft} soft tokens"
                )
        return calls, values

    def calls(self, tokens, raw: dict[int, tuple]) -> tuple[list[tuple], dict]:
        """An encoder text model's call: the inputs of each version it runs,
        in the order they run, and its per-call values (``tower_calls``).

        Raises:
            TypeError: The text model is causal: ``logits``, ``generate``.
        """
        if not isinstance(self.text, Encoder):
            raise TypeError(f"{type(self.text).__name__} runs logits() or generate()")
        ids, values = self.text.inputs(tokens)
        calls, towers = self.tower_calls(tokens, raw)
        values |= towers
        names = list(self._inputs)
        if not calls:
            return [tuple(ids if n == "ids" else None for n in names)], values
        return [*calls, tuple(ids if n == "placed" else None for n in names)], values

    def run(self, tokens, raw: dict[int, tuple]):
        """An encoder text model's output for ``tokens`` with ``raw`` at their
        placeholders (as ``calls`` takes them), each version run in turn.
        """
        calls, values = self.calls(tokens, raw)
        for inputs in calls:
            out = self(*inputs, **values)
        return out

    def place(self, tokens, raw: dict[int, tuple]) -> None:
        """Run each tower ``raw`` names, so a causal text model's prompt
        chunks find its soft tokens in ``merged``, unless each ran on the
        same last time. Otherwise its caches are stale from the first
        placeholder on, and it forgets them from there.
        """
        tokens = np.asarray(tokens)
        calls, values = self.tower_calls(tokens, raw)
        same = raw.keys() == self._last_raw.keys() and all(
            len(raw[t]) == len(self._last_raw[t])
            and all(np.array_equal(a, b) for a, b in zip(raw[t], self._last_raw[t]))
            for t in raw
        )
        if same:
            return
        values |= {v: 0 for v in self.text_values}
        for inputs in calls:
            self(*inputs, **values)
        self._last_raw = {t: tuple(np.array(a) for a in raw[t]) for t in raw}
        places = np.flatnonzero(np.isin(tokens, list(self.towers)))
        self.text.forget(int(places[0]) if places.size else tokens.size)

    def logits(self, tokens, raw: dict[int, tuple]) -> np.ndarray:
        """A causal text model's logits after ``tokens``, ``raw`` at their
        placeholders (``CausalLM.logits``).
        """
        self.place(tokens, raw)
        return self.text.logits(tokens)

    def generate(
        self, tokens, num_tokens: int, sample: Sampler, raw: dict[int, tuple]
    ) -> tuple[list[int], float, float]:
        """A causal text model's draws after ``tokens``, ``raw`` at their
        placeholders (``CausalLM.generate``).
        """
        self.place(tokens, raw)
        return self.text.generate(tokens, num_tokens, sample)
