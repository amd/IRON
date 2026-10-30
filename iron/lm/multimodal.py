# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A text model whose placeholder tokens take its towers' soft tokens.

As Hugging Face's ``masked_scatter`` places them: the j-th of a token's
placeholders takes its tower's j-th soft token.
"""

import inspect
from collections.abc import Iterator

import numpy as np

import iron
from iron.operators.copy import Copy
from iron.operators.merge import Merge

from .causal import CausalLM
from .encoder import Encoder, Tower
from .generation import Sampler
from .model import Model


class Multimodal(Model):
    """A text model and its towers, keyed by placeholder token, as one graph.

    A tower writes its soft tokens into ``merged``, and ``placed`` scatters
    them into the text model's rows by placeholder position.

    Args:
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
        # Every tower's per-call values, zero: those of a call none runs.
        self.idle = {
            f"{self.tower_inputs[token]}_{v}": 0
            for token in towers
            for v in self.tower_values[token]
        }
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
        given = {n: x for n, x in zip(self._parameters.inputs, inputs) if x is not None}
        if len(set(given) - {"before"}) > 1:
            raise TypeError(f"a version takes one input, got {sorted(given)}")
        text = {v: values[v] for v in self.text_values}
        for token, tower in self.towers.items():
            name = self.tower_inputs[token]
            if name in given:
                own = {v: values[f"{name}_{v}"] for v in self.tower_values[token]}
                soft = tower(given[name], **own)
                at = self.at[token]
                self.merged[at : at + soft.shape[0]] = soft
                # A text model's carried values pass through unchanged.
                if self._parameters.carried:
                    return iron.carry(
                        **{n: values[n] for n in self._parameters.carried}
                    )
                return None
        if "placed" not in given:
            inputs = [given.get(n) for n in self.text_inputs]
            return self.text.inline(self.text.body, *inputs, **text)
        placed, n = given["placed"], text["rows"]
        # An input's gather is encoded on the host into its buffer, which Merge
        # reads as the ids: gather by the device's copy of them.
        ids = Copy.step(placed, dtype=np.int32)[:n]
        x = self.text.inline(self.text.lookup, ids)
        counted = {"before": given["before"]} if "before" in given else {}
        merge = Merge.step(placed, placeholders=tuple(self.at.items()), **counted)
        self.merged[: x.shape[0]] = x
        rows = Copy.step(self.merged[merge])[:n]
        return self.text.inline(self.text.from_rows, rows, ids, **text)

    def shapes(self) -> list[dict]:
        """Return the input shapes of each version.

        The text model's, first so its decode step leads (``Model.shapes``),
        each tower's, and the ids with their placeholders (and a causal
        model's counts).
        """
        text = self.text.shapes()
        (ids,) = [s["ids"] for s in text if "ids" in s]
        towers = [s for t in self.towers.values() for s in t.shapes()]
        placed = dict(placed=ids)
        if isinstance(self.text, CausalLM):
            placed["before"] = ((len(self.towers),), np.int32)
        return [*text, *towers, placed]

    def release(self) -> None:
        """Free the text model's loops, then every version's and the arena's memory."""
        self.text.release()
        super().release()

    def loaded(self, versions: list) -> None:
        """Hand a causal text model its versions (``use``)."""
        if isinstance(self.text, CausalLM):
            decode_step, prompt_chunk, *_, placed = versions
            self.text.use(decode_step, prompt_chunk, placed, tuple(self.at))

    def longest(self) -> dict:
        """Return the per-call values of the longest call.

        The text model's and each tower's.
        """
        assert isinstance(self.text, Encoder), "an encoder text model's"
        values = dict(self.text.longest())
        for token, tower in self.towers.items():
            name = self.tower_inputs[token]
            values |= {f"{name}_{v}": x for v, x in tower.longest().items()}
        return values

    def tower_calls(self, tokens, raw: dict[int, tuple]) -> list[tuple[tuple, dict]]:
        """Each tower version ``raw`` runs, in turn.

        Its inputs and every tower's per-call values, zero for a tower not
        running.

        Args:
            tokens: The token ids, each placeholder run as long as its
                tower's soft tokens.
            raw: Each tower's raw input, as its ``calls`` takes it, by
                placeholder token.

        Raises:
            ValueError: A placeholder's count is not its tower's soft tokens.
        """
        tokens = np.asarray(tokens)
        names = list(self._parameters.inputs)
        calls = []
        for token, tower in self.towers.items():
            name, soft = self.tower_inputs[token], 0
            for buffer, own in tower.calls(*raw[token]) if token in raw else []:
                soft += tower.soft(own)
                inputs = tuple(buffer if n == name else None for n in names)
                calls.append(
                    (inputs, self.idle | {f"{name}_{v}": x for v, x in own.items()})
                )
            places = np.count_nonzero(tokens == token)
            if places != soft:
                raise ValueError(
                    f"{places} placeholders {token} for {soft} soft tokens"
                )
        return calls

    def calls(self, tokens, raw: dict[int, tuple]) -> list[tuple[tuple, dict]]:
        """Build an encoder text model's call: each version it runs, in turn.

        Its inputs and per-call values (``tower_calls``).

        Raises:
            TypeError: The text model is causal: ``logits``, ``generate``.
        """
        if not isinstance(self.text, Encoder):
            raise TypeError(f"{type(self.text).__name__} runs logits() or generate()")
        ids, text = self.text.inputs(tokens)
        towers = [
            (inputs, values | text) for inputs, values in self.tower_calls(tokens, raw)
        ]
        names = list(self._parameters.inputs)
        last = "placed" if towers else "ids"
        return [
            *towers,
            (tuple(ids if n == last else None for n in names), text | self.idle),
        ]

    def run(self, tokens, raw: dict[int, tuple]):
        """Return an encoder text model's output for ``tokens``.

        ``raw`` at their placeholders (as ``calls`` takes them), each
        version run in turn.
        """
        for inputs, values in self.calls(tokens, raw):
            out = self(*inputs, **values)
        return out

    def place(self, tokens, raw: dict[int, tuple]) -> None:
        """Run each tower ``raw`` names.

        So a causal text model's prompt chunks find its soft tokens in
        ``merged``, unless each ran on the same last time, else forgetting
        its caches from the first stale placeholder.
        """
        tokens = np.asarray(tokens)
        calls = self.tower_calls(tokens, raw)
        same = raw.keys() == self._last_raw.keys() and all(
            len(raw[t]) == len(self._last_raw[t])
            and all(np.array_equal(a, b) for a, b in zip(raw[t], self._last_raw[t]))
            for t in raw
        )
        if same:
            return
        text = {v: 0 for v in self.text_values}
        for inputs, values in calls:
            self(*inputs, **values, **text)
        self._last_raw = {t: tuple(np.array(a) for a in raw[t]) for t in raw}
        places = np.flatnonzero(np.isin(tokens, list(self.towers)))
        assert isinstance(self.text, CausalLM), "a causal text model's"
        self.text.forget(int(places[0]) if places.size else tokens.size)

    def logits(self, tokens, raw: dict[int, tuple]) -> np.ndarray:
        """Return a causal text model's logits after ``tokens``.

        ``raw`` at their placeholders (``CausalLM.logits``).
        """
        self.place(tokens, raw)
        assert isinstance(self.text, CausalLM), "a causal text model's"
        return self.text.logits(tokens)

    def _draw(
        self,
        tokens,
        max_tokens: int,
        sampler: Sampler,
        each: bool = True,
        raw: dict[int, tuple] | None = None,
    ) -> Iterator[int]:
        """Yield a causal text model's draws after ``tokens``.

        ``raw`` at their placeholders (none by default): ``generate(...,
        raw=)`` and ``stream(..., raw=)``.
        """
        self.place(tokens, raw or {})
        assert isinstance(self.text, CausalLM), "a causal text model's"
        return self.text._draw(tokens, max_tokens, sampler, each)
