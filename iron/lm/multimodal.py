# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A text model whose placeholder tokens take its towers' soft tokens, as
Hugging Face's ``masked_scatter`` places them: the j-th of a token's
placeholders takes its tower's j-th soft token.
"""

import inspect

import numpy as np

import iron
from iron.operators.copy import Copy
from iron.operators.merge import Merge

from .base import Model
from .encoder import Encoder, Tower


class Multimodal(Model):
    """A text model and its towers, keyed by placeholder token, as one graph.

    Each version takes one input. The text model's own take its inputs. A
    tower's takes its input and writes its soft tokens into ``merged`` from
    its own row. ``placed``, the ids with their placeholders, writes the
    text's rows into ``merged`` from its first row; ``Merge`` then gives each
    position its row of ``merged``, and the text model runs over those rows.
    A version is one dispatch with its own scratchpad, which all of them in
    one would overrun. A tower's per-call values are named after its input:
    a vision tower's ``n`` on input ``rgb`` is ``rgb_n``.

    Args:
        text: The text model.
        towers: Each tower, by the token its placeholders are.

    Raises:
        TypeError: Two inputs or values share a name, or a tower takes other
            than one input.
    """

    def __init__(self, text: Encoder, towers: dict[int, Tower]):
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
        self.merged = iron.state((rows, text.config.emb_dim))
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
        parameters = [*inputs, P("placed", P.POSITIONAL_OR_KEYWORD, default=None)]
        parameters += values
        names = [p.name for p in parameters]
        if len(set(names)) != len(names):
            raise TypeError(f"Multimodal: inputs and values {names} repeat a name")
        return inspect.Signature(parameters)

    def body(self, *inputs, **values):
        given = {n: x for n, x in zip(self._inputs, inputs) if x is not None}
        if len(given) > 1:
            raise TypeError(f"a version takes one input, got {sorted(given)}")
        text = {v: values[v] for v in self.text_values}
        for token, tower in self.towers.items():
            name = self.tower_inputs[token]
            if name in given:
                own = {v: values[f"{name}_{v}"] for v in self.tower_values[token]}
                soft = tower(given[name], **own)
                at = self.at[token]
                Copy.step(soft, self.merged[at : at + soft.shape[0]])
                return None
        if "placed" not in given:
            return self.text(*(given.get(n) for n in self.text_inputs), **text)
        placed, n = given["placed"], text["n"]
        # An input's gather is encoded on the host into its buffer, which Merge
        # reads as the ids: gather by the device's copy of them.
        x = self.text.lookup(Copy.step(placed, dtype=np.int32)[:n])
        merge = Merge.step(placed, placeholders=tuple(self.at.items()))
        Copy.step(x, self.merged[: x.shape[0]])
        rows = Copy.step(self.merged[merge])[:n]
        return self.text.forward(rows, n, self.text.angles(n))

    def shapes(self) -> list[dict]:
        """The input shapes of each version: the text model's, each tower's,
        and the ids with their placeholders.
        """
        text = self.text.shapes()
        (ids,) = [s["ids"] for s in text if "ids" in s]
        towers = [s for t in self.towers.values() for s in t.shapes()]
        return [*text, *towers, dict(placed=ids)]

    def longest(self) -> dict:
        """The per-call values of the longest call: the text model's and each
        tower's.
        """
        values = dict(self.text.longest())
        for token, tower in self.towers.items():
            name = self.tower_inputs[token]
            values |= {f"{name}_{v}": x for v, x in tower.longest().items()}
        return values

    def calls(self, tokens, raw: dict[int, tuple]) -> tuple[list[tuple], dict]:
        """The inputs of each version a call runs, in the order they run, and
        the call's per-call values.

        Args:
            tokens: The token ids, each placeholder run as long as its
                tower's soft tokens.
            raw: Each tower's raw input, as its ``inputs`` takes it, by
                placeholder token; a tower left out runs no version.

        Raises:
            ValueError: A placeholder's count is not its tower's soft tokens.
        """
        tokens = np.asarray(tokens)
        ids, values = self.text.inputs(tokens)
        names = list(self._inputs)
        calls = []
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
        if not calls:
            return [tuple(ids if n == "ids" else None for n in names)], values
        return [*calls, tuple(ids if n == "placed" else None for n in names)], values

    def run(self, tokens, raw: dict[int, tuple]):
        """The text model's output for ``tokens`` with ``raw`` at their
        placeholders (as ``calls`` takes them), each version run in turn.
        """
        calls, values = self.calls(tokens, raw)
        for inputs in calls:
            out = self(*inputs, **values)
        return out
