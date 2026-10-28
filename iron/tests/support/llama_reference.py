# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder's graph on the host, judged against transformers' model."""

import dataclasses
from types import SimpleNamespace

import numpy as np
import pytest

from iron.lm import (
    DecoderConfig,
    OnHost as Host,
    accuracy,
    determinism,
)
from iron.lm.generation import greedy
from iron.lm.golden import Golden, HuggingFace
from iron.lm.testing import assert_close
from iron.applications.llama import Llama
from iron.tests.support.llama_model import PROFILE, checkpoint, shapes


class OnHost(Host, Llama):
    profile = PROFILE


@dataclasses.dataclass
class Case:
    config: DecoderConfig
    weights: SimpleNamespace
    golden: Golden
    prompt: np.ndarray
    first: np.ndarray
    expected: list


def _greedy(model, tokens, logits, n):
    """The logits of ``n`` greedy decode steps after ``tokens``, whose own
    are ``logits``.
    """
    history, out = list(tokens), []
    for _ in range(n):
        history.append(greedy(logits))
        logits = model.logits(history)
        out.append(logits)
    return out


def prompt(model, tokens, **values):
    """Each prompt chunk's reference over ``tokens`` in turn, its states
    carried to the next and ``values`` given to each: the last chunk's
    logits and carry. A ``Multimodal`` model's chunk holding a placeholder
    runs ``placed``, given the count of each placeholder before it.
    """
    text = getattr(model, "text", model)
    towers = list(getattr(model, "towers", {}))
    C = text.config.prefill_chunk
    for begin in range(0, tokens.size, C):
        chunk = tokens[begin : begin + C]
        inputs = (text.session.prompt_ids(chunk),)
        if np.isin(chunk, towers).any():
            before = [np.count_nonzero(tokens[:begin] == t) for t in towers]
            unfed = (None,) * (len(model.text_inputs) + len(towers))
            inputs = (*unfed, *inputs, np.array(before, np.int32))
        out = model.reference(
            *inputs,
            token=int(chunk[-1]),
            position=begin + chunk.size - 1,
            start=begin,
            rope_start=begin,
            rows=chunk.size,
            **values,
        )
    return out


class Decoder:
    """What every decoder's graph does on the host as transformers' model
    does over the same random weights. A subclass names the ``model``
    class, its toy ``config``, transformers' ``model_type`` and the golden's
    ``name`` (``goldens/<name>.npz`` beside the subclass); and ``names``,
    ``weights``, ``json`` or ``profile`` where they are not Llama's or none.
    """

    pytestmark = pytest.mark.usefixtures("npu2")
    model: type
    config: DecoderConfig
    model_type: str
    name: str
    # transformers' config keys beyond the config's own.
    json: dict = {}
    # The prompt's seed: one whose greedy steps have no near-tie.
    seed = 7
    profile = None
    # The config's fields replaced where the toy, sized for the host, is
    # one the device's operators refuse: the shape every version records at.
    recorded: dict = {}

    @classmethod
    def names(cls) -> dict[str, tuple[int, ...]]:
        """Each tensor of the toy's checkpoint, by name: Llama's."""
        return shapes(cls.config)

    @classmethod
    def weights(cls) -> SimpleNamespace:
        """The toy's checkpoint tree, drawn (``Checkpoint.tree``)."""
        return checkpoint(cls.config, cls.names()).tree("random")

    @classmethod
    def case(cls, golden) -> Case:
        """The config, its weights, its golden logits, a prompt, the golden
        logits for it and six greedy tokens' logits.
        """
        config = cls.config
        weights = cls.weights()
        reference = golden(
            cls.name,
            lambda: HuggingFace.build(cls.model_type, config, weights, **cls.json),
            config,
            weights,
        )
        prompt = np.random.default_rng(cls.seed).integers(0, config.vocab_size, 8)
        tokens, expected = prompt, []
        first = logits = reference.logits(tokens)
        for _ in range(6):
            tokens = np.append(tokens, logits.argmax())
            logits = reference.logits(tokens)
            expected.append(logits)
        # Each step's top two lie further apart than bf16's resolution, 2^-8
        # of the largest logit, so rounding alone cannot swap them. The bf16
        # graphs' own error can exceed that floor, so the accuracy check's
        # strict top1 also rests on these seeds: a kernel change that flips
        # it needs a new seed, not a looser check.
        for step, logits in enumerate([first, *expected]):
            second, top = np.sort(logits)[-2:]
            assert (
                top - second > 2**-8 * np.abs(logits).max()
            ), f"{cls.name}: step {step} of seed {cls.seed}'s prompt is a near-tie"
        return Case(config, weights, reference, prompt, first, expected)

    def host(self, config, weights):
        """The model on ``config`` and ``weights`` with its images stood in
        by its graph's reference.
        """
        return type("OnHost", (Host, self.model), {"profile": self.profile})(
            config, weights
        )

    @pytest.fixture(scope="class")
    @classmethod
    def cpu(cls, golden):
        return cls.case(golden)

    def test_every_step_of_every_version_resolves(self, npu2):
        """Built on its checkpoint's names through its own loading, every
        version records and each step resolves on the device: no step hides
        host compute or a shape the device refuses.
        """
        toy = type(self)
        recorded = type(toy.__name__, (toy,), {})
        recorded.config = dataclasses.replace(toy.config, **toy.recorded)
        model = self.model(recorded.config, recorded.weights())
        for call in model.shapes():
            for step in model.record(**call).steps:
                step.op.resolved(npu2)

    def test_decode_from_an_empty_cache_matches_the_forward_token_by_token(self, cpu):
        """One token at a time only: the prompt fed a token at a time from an
        empty cache, then the generated tokens.
        """
        model = self.host(cpu.config, cpu.weights)
        last = model.logits(cpu.prompt[:1])
        for n in range(2, len(cpu.prompt) + 1):
            last = model.logits(cpu.prompt[:n])
        assert_close(last, cpu.first)
        got = _greedy(model, cpu.prompt, last, len(cpu.expected))
        for step, (a, b) in enumerate(zip(got, cpu.expected)):
            assert_close(a, b, f"step {step}")

    def test_the_prompt_matches_the_forward_and_leaves_decode_its_caches(self, cpu):
        """The prompt at its own rows: the padding rows are masked and past the
        prompt in the caches, and decode continues from the caches it wrote.
        """
        model = self.host(cpu.config, cpu.weights)
        first = model.logits(cpu.prompt)
        assert_close(first, cpu.first)
        got = _greedy(model, cpu.prompt, first, len(cpu.expected))
        for step, (a, b) in enumerate(zip(got, cpu.expected)):
            assert_close(a, b, f"step {step}")

    def test_a_prompt_longer_than_a_chunk_runs_in_chunks(self, cpu):
        """A prompt of several chunks, each attending over the caches the ones
        before it wrote, then a decode step, then a turn of several tokens,
        which reruns only the chunk holding its first token onwards.
        """
        C = cpu.config.prefill_chunk
        config = dataclasses.replace(cpu.config, max_seq_len=4 * C)
        model, reference = self.host(config, cpu.weights), cpu.golden
        tokens = np.random.default_rng(3).integers(0, config.vocab_size, C + 150)
        first = reference.logits(tokens)
        assert_close(model.logits(tokens), first)
        tokens = np.append(tokens, first.argmax())
        assert_close(model.logits(tokens), reference.logits(tokens))
        turn = np.random.default_rng(4).integers(0, config.vocab_size, 30)
        tokens = np.append(tokens, turn)
        assert_close(model.logits(tokens), reference.logits(tokens))

    def test_the_accuracy_check_scores_the_model_against_the_reference(self, cpu):
        """What ``--check-accuracy`` runs, the images stood in by the graph's
        reference: the model against its golden logits, teacher-forced.
        """
        model = self.host(cpu.config, cpu.weights)
        steps = len(cpu.expected) + 1
        results = accuracy(model, cpu.golden, cpu.prompt, steps)
        assert all(top1 for _, top1 in results), results
        # bf16 graphs against a float32 forward: close, not equal. The seven
        # toys measure at most 2.7e-4 (LFM2's), the rest at most 8e-5.
        assert all(0 <= kl < 1e-3 for kl, _ in results), results
        assert any(kl > 0 for kl, _ in results), results

    def test_the_determinism_check_finds_the_reference_deterministic(self, cpu):
        """What ``--check-determinism`` runs: two prompts, alternated, each
        rerun from a prefill; no run differs from the first.
        """
        model = self.host(cpu.config, cpu.weights)
        prompts = [cpu.prompt, cpu.prompt[::-1]]
        assert determinism(model, prompts, 3, 3) == 0
