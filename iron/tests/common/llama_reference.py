# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The graph's reference against the model's plain forward pass.

Hugging Face's own model in float32 over the same random weights, its
logits recorded in ``goldens/`` (``iron.lm.golden``), judges the
application. ``OnHost`` stands the model's images in by
``Graph.reference``, which runs the graph operator by operator on host
tensors with the caches as state: that checks the graph's wiring (layouts,
reshapes, head grouping, the caches a prompt leaves for decode) without a
device, leaving only the kernels' arithmetic for hardware. The graph
computes in bfloat16 and the reference in float32, so the logits agree to
bf16 tolerance and the argmax exactly.
"""

import dataclasses
import datetime
import itertools
import json
import math
import struct

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.lm import (
    Sampler,
    Session,
    Tokenizer,
    TokenizerJson,
    generate_on_host,
)
from iron.lm.checkpoint import leaves
from iron.lm.testing import assert_close
from iron.applications.llama import Llama
from iron.applications.llama.model import Llama3RopeScaling
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.rope import RoPE
from iron.tests.support.llama_model import PROFILE, SMALL
from iron.tests.support.llama_reference import Decoder, OnHost

pytestmark = pytest.mark.usefixtures("npu2")  # MHA decode on any host


#: ``SMALL`` with Llama 3's RoPE scaling from a 64-position original
#: context, so its toy prompts reach every band of frequencies.
SCALED = dataclasses.replace(
    SMALL,
    rope_scaling=Llama3RopeScaling(
        factor=8.0,
        low_freq_factor=1.0,
        high_freq_factor=4.0,
        original_max_position_embeddings=64,
    ),
)


class TestLlama(Decoder):
    model, config, model_type, name, profile = Llama, SCALED, "llama", "small", PROFILE


@pytest.fixture(scope="module")
def cpu(golden):
    """``TestLlama``'s case, for the tests of the graph Llama alone needs."""
    return TestLlama.case(golden)


def _decoded(model, tokens, steps):
    """The logits after ``tokens``, its last ``steps`` tokens decoded one at
    a time over the caches the prompt before them left.
    """
    model.logits(tokens[:-steps])
    for n in range(len(tokens) - steps + 1, len(tokens) + 1):
        logits = model.logits(tokens[:n])
    return logits


@pytest.mark.parametrize("outside", [-1, SMALL.vocab_size])
def test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch(cpu, outside):
    """A prompt that differs from the history in its first chunk and holds
    an id no row embeds in its second: refused whole, the caches and the
    history as the last call left them.
    """
    config = dataclasses.replace(cpu.config, prefill_chunk=64)
    model = OnHost(config, cpu.weights)
    tokens = np.random.default_rng(6).integers(0, config.vocab_size, 100)
    model.logits(tokens)
    broken = tokens.copy()
    broken[3] = (broken[3] + 1) % config.vocab_size
    broken[70] = outside
    with pytest.raises(IndexError, match=rf"\[{outside}\] are outside"):
        model.logits(broken)
    np.testing.assert_array_equal(model.session._seen, tokens)
    # The same calls on a model that refused nothing: its last token again.
    fresh = OnHost(config, cpu.weights)
    fresh.logits(tokens)
    np.testing.assert_array_equal(model.logits(tokens), fresh.logits(tokens))


def test_a_model_runs_only_the_versions_it_loaded(cpu):
    """Before ``load_versions()`` a call compiles nothing on its own: that would build
    an untuned version past the tuner and packaging ``load_versions`` is given.
    """
    model = Llama(cpu.config, cpu.weights)
    with pytest.raises(RuntimeError, match=r"load_versions\(\) first"):
        model.logits(cpu.prompt)
    with pytest.raises(RuntimeError, match=r"load_versions\(\) first"):
        model(start=0, rows=1, rope_start=0, token=0, position=0)
    assert not model._versions


def test_a_model_places_every_version_before_loading_any(cpu, monkeypatch):
    """A version placed after the arena's buffers exist grows them, copying
    every weight once more, so ``load_versions`` compiles all before it
    loads one.
    """
    model, events = Llama(cpu.config, cpu.weights), []

    class Version:
        emit = None

        def __init__(self, shapes):
            self.shapes = shapes

        def load(self, release=None):
            events.append(("load", self.shapes))

    def compile(**kw):
        shapes = {k: v for k, v in kw.items() if k not in ("dev", "feeds", "full_elf")}
        events.append(("compile", shapes))
        return Version(shapes)

    monkeypatch.setattr(model, "compile", compile)
    monkeypatch.setattr(model, "loaded", lambda versions: None)
    model.load_versions(dev=object())
    shapes = model.shapes()
    assert events == [("compile", s) for s in shapes] + [("load", s) for s in shapes]


def test_a_model_reads_as_its_context_and_whether_it_is_loaded(cpu):
    model = Llama(cpu.config, cpu.weights)
    assert repr(model) == f"Llama(max_seq_len={cpu.config.max_seq_len}, not loaded)"


@pytest.mark.parametrize("temperature", [0.0, 0.7])
def test_the_carried_draws_are_the_host_loop_s_tokens(cpu, temperature):
    """What ``generate_on_host`` loops on the device, each call started from
    the last one's carry: from the same seed, the host loop's tokens. Every
    draw is the graph's own, from the rows the sampler gives it.
    """
    config, n, count = cpu.config, len(cpu.prompt), 6
    host = OnHost(config, cpu.weights)
    expected = generate_on_host(
        host, cpu.prompt, count, Sampler(temperature, 40, seed=5)
    )
    model = OnHost(config, cpu.weights)
    draws = np.zeros(model.draws.shape, dtype=np.int32)
    sampler = Sampler(temperature, 40, seed=5)
    draws[n - 1 : n - 1 + count] = sampler.rows(count, k_max=64)
    model.draws.host = draws
    ((inputs, values),) = model.session._chunks(np.asarray(cpu.prompt), 0)
    _, carry = model(*inputs, **values)
    drawn = [carry["token"]]
    for _ in range(count - 1):
        _, carry = model(start=0, rows=1, rope_start=0, **carry)
        drawn.append(carry["token"])
    assert drawn == expected


class Placed(OnHost):
    """``OnHost`` with no RoPE, its positions a held table's rows added to
    the embedding's.
    """

    def __init__(self, config, weights, table):
        super().__init__(config, weights)
        self.table = iron.weight(table)

    def positions(self, x, step):
        c = self.config
        C, E = c.prefill_chunk, c.hidden_size
        if step.prompt:
            rows = Copy.step(self.table[step.start : step.start + C][: step.rows])
        else:
            rows = Copy.step(self.table[step.position]).reshape(1, E)
        return ElementwiseAdd.step(x, rows)


def test_a_decoder_without_rope_places_its_positions_through_the_hook(cpu):
    """No ``rope_theta``: no table is held and nothing turns q and k; a
    model's ``positions`` adds its own rows instead, in each prompt chunk at
    the chunk's positions and in a decode step at its one: a prompt over
    chunks and the same tokens' last ones decoded give the same logits, and
    not those of RoPE. No Hugging Face model places a table so, so no
    golden judges it.
    """
    config = dataclasses.replace(
        cpu.config, rope_theta=None, max_seq_len=2 * cpu.config.prefill_chunk
    )
    assert config.angles() is None
    table = np.random.default_rng(9).standard_normal(
        (config.max_seq_len, config.hidden_size)
    )
    table = (table / 2).astype(bfloat16)
    model = Placed(config, cpu.weights, table)
    assert model.rotary_emb is None
    for version in model.shapes():
        steps = model.record(**version).steps
        assert not any(isinstance(s.op, RoPE) for s in steps)
    tokens = np.random.default_rng(10).integers(0, config.vocab_size, 300)
    prompted = model.logits(tokens)
    decoded = _decoded(Placed(config, cpu.weights, table), tokens, 4)
    assert_close(decoded, prompted)
    with pytest.raises(AssertionError):
        assert_close(prompted, cpu.golden.logits(tokens))


def test_a_turn_runs_from_its_first_new_token(cpu):
    """Decision 50: a turn changing the history at 270, past the boundary at
    256, calls from 270 alone; the caches' rows before it are the first
    prompt's, and its logits the golden ones.
    """
    config = dataclasses.replace(cpu.config, max_seq_len=1024)
    weights, reference = cpu.weights, cpu.golden
    model = OnHost(config, weights)
    rng = np.random.default_rng(9)
    tokens = rng.integers(0, config.vocab_size, 300)
    model.logits(tokens)
    before = np.array(model.model.layers[0].cache.keys.host)
    turn = np.concatenate([tokens[:270], rng.integers(0, config.vocab_size, 40)])
    session = model.session
    assert session.resume(session._held(turn)) == 270
    assert [(v["start"], v["rows"]) for _, v in session._chunks(turn, 270)] == [
        (270, 40)
    ]
    assert_close(model.logits(turn), reference.logits(turn))
    np.testing.assert_array_equal(
        model.model.layers[0].cache.keys.host[:270], before[:270]
    )


def test_two_sessions_share_one_model(cpu):
    """Two conversations over one model's versions, a ``Session`` each: the
    caches hold one session's tokens at a time, so the first, its tokens
    replaced by the second's, runs its history again, and each gives the
    logits a model of its own would.
    """
    model = OnHost(cpu.config, cpu.weights)
    rng = np.random.default_rng(11)
    first, second = (rng.integers(0, cpu.config.vocab_size, 40) for _ in range(2))
    a, b = Session(model), Session(model)
    a.logits(first)
    b.logits(second)
    for session, tokens in ((a, first), (b, second)):
        turn = np.append(tokens, 1)
        alone = OnHost(cpu.config, cpu.weights)
        np.testing.assert_array_equal(session.logits(turn), alone.logits(turn))


def test_a_context_no_chunk_divides_runs_to_its_last_position(cpu):
    """300 positions in 256-row chunks: a prompt whose second chunk is 43
    rows, then the decode step at the last position, 299, each the golden
    logits; the caches are 300 rows, exactly.
    """
    config = dataclasses.replace(cpu.config, max_seq_len=300)
    model, reference = OnHost(config, cpu.weights), cpu.golden
    tokens = np.random.default_rng(8).integers(0, config.vocab_size, 300)
    assert_close(model.logits(tokens[:299]), reference.logits(tokens[:299]))
    assert_close(model.logits(tokens), reference.logits(tokens))


def _repository(directory, weights):
    """A Hugging Face Llama repository's files at ``SCALED``'s shape: its
    ``config.json``, of a context of two prompt chunks so that loading fits
    it, ``weights``, and a tokenizer of every byte and enough two-byte
    pieces to fill the vocabulary, its last id the BOS.
    """
    V = SMALL.vocab_size
    config = SCALED.to_json() | {"max_position_embeddings": 4096, "bos_token_id": V - 1}
    (directory / "config.json").write_text(json.dumps(config))
    header, end = {}, 0
    for name, t in leaves(weights):
        header[name] = dict(
            dtype="BF16", shape=t.shape, data_offsets=[end, end + t.nbytes]
        )
        end += t.nbytes
    blob = json.dumps(header).encode()
    with open(directory / "model.safetensors", "wb") as f:
        f.write(struct.pack("<Q", len(blob)) + blob)
        for _, t in leaves(weights):
            f.write(t.tobytes())
    _tokenizer_json(directory / "tokenizer.json", V)


def _tokenizer_json(path, size=256, specials=()):
    """A byte-level ``tokenizer.json`` at ``path``: every byte, two-letter
    pieces up to ``size`` ids, then ``specials``; its encoding.
    """
    tokenizers = pytest.importorskip("tokenizers")
    alphabet = sorted(tokenizers.pre_tokenizers.ByteLevel.alphabet())
    letters = [chr(c) for c in range(33, 127)]
    pairs = list(itertools.product(letters[64:90], letters))[: size - 256]
    vocab = {c: i for i, c in enumerate(alphabet + [a + b for a, b in pairs])}
    hf = tokenizers.Tokenizer(tokenizers.models.BPE(vocab, pairs))
    hf.pre_tokenizer = tokenizers.pre_tokenizers.ByteLevel(add_prefix_space=False)
    hf.decoder = tokenizers.decoders.ByteLevel()
    hf.add_special_tokens(list(specials))
    hf.save(str(path))
    return TokenizerJson(path)


QUESTION = "The capital of France is"

# The ChatML template Qwen 2.5's and SmolLM2's checkpoints follow.
CHATML = (
    "{% for message in messages %}{{'<|im_start|>' + message['role'] + '\\n' + "
    "message['content'] + '<|im_end|>' + '\\n'}}{% endfor %}"
    "{% if add_generation_prompt %}{{ '<|im_start|>assistant\\n' }}{% endif %}"
)


def test_the_quick_start_script_runs_on_a_toy_repository(cpu, tmp_path):
    """The quick start's calls on a toy repository, the host standing in for
    the NPU: the BOS and the text's ids, and from seed 0 the text of the
    tokens the host loop draws from the model on the same weights.
    """
    _repository(tmp_path, cpu.weights)
    model = OnHost.load(tmp_path)
    out = model.generate(QUESTION, max_tokens=8, sampler=Sampler(seed=0))
    tokens = model.tokenizer(QUESTION)
    assert tokens[0] == SMALL.vocab_size - 1
    assert model.tokenizer.decode(tokens[1:]) == QUESTION
    host = OnHost(cpu.config, cpu.weights)
    want = generate_on_host(host, tokens, 8, Sampler(seed=0))
    assert out == model.tokenizer.decode(want)


@pytest.fixture(scope="module")
def toy(cpu, tmp_path_factory):
    """The model of a toy repository whose ``tokenizer_config.json`` holds
    ``CHATML``, loaded, the host standing in for the NPU.
    """
    directory = tmp_path_factory.mktemp("repository")
    _repository(directory, cpu.weights)
    settings = {"chat_template": CHATML}
    (directory / "tokenizer_config.json").write_text(json.dumps(settings))
    return OnHost.load(directory)


def test_generate_gives_text_for_text_and_ids_for_ids(toy):
    text = toy.generate(QUESTION, 4)
    ids = toy.generate(toy.tokenizer(QUESTION), 4)
    assert len(ids) == 4 and all(type(t) is int for t in ids)
    assert isinstance(text, str) and text == toy.tokenizer.decode(ids)


def test_stream_s_pieces_joined_are_what_generate_gives(toy):
    pieces = list(toy.stream(QUESTION, 6, Sampler(seed=3)))
    assert all(isinstance(p, str) for p in pieces)
    assert "".join(pieces) == toy.generate(QUESTION, 6, Sampler(seed=3))


def test_no_sampler_is_greedy(toy):
    tokens = toy.tokenizer(QUESTION)
    assert toy.generate(tokens, 6) == toy.generate(tokens, 6, Sampler(temperature=0))


def test_generation_stops_at_an_eos_and_includes_it(cpu, tmp_path):
    """As Hugging Face's ``generate``: the first of the checkpoint's eos ids
    drawn is the last token, ``generation_config.json``'s list over
    ``config.json``'s.
    """
    _repository(tmp_path, cpu.weights)
    model = OnHost.load(tmp_path)
    tokens = model.tokenizer(QUESTION)
    drawn = model.generate(tokens, 6)
    end = drawn.index(drawn[3]) + 1
    (tmp_path / "generation_config.json").write_text(
        json.dumps({"eos_token_id": [-1, drawn[3]]})
    )
    model = OnHost.load(tmp_path)
    assert model.generate(tokens, 6) == drawn[:end]
    assert list(model.stream(tokens, 6)) == drawn[:end]


def test_a_run_that_draws_no_eos_draws_max_tokens(cpu, tmp_path):
    """``config.json``'s eos, with no ``generation_config.json``."""
    _repository(tmp_path, cpu.weights)
    config = json.loads((tmp_path / "config.json").read_text())
    model = OnHost.load(tmp_path)
    tokens = model.tokenizer(QUESTION)
    drawn = model.generate(tokens, 6)
    unseen = next(t for t in range(SMALL.vocab_size) if t not in drawn)
    config["eos_token_id"] = unseen
    (tmp_path / "config.json").write_text(json.dumps(config))
    model = OnHost.load(tmp_path)
    assert model.eos == {unseen} and model.generate(tokens, 6) == drawn


def test_a_generation_s_timings_are_the_model_s_stats(toy):
    toy.generate(QUESTION, 3)
    assert toy.stats.ttft > 0 and toy.stats.tokens_per_s > 0
    toy.generate(QUESTION, 1)
    assert math.isnan(toy.stats.tokens_per_s)


HI = [{"role": "user", "content": "Hi"}]


def test_chat_messages_are_rendered_by_the_checkpoint_s_template(toy):
    """ChatML writes no BOS, so the chat has none."""
    pytest.importorskip("jinja2")
    text = "<|im_start|>user\nHi<|im_end|>\n<|im_start|>assistant\n"
    assert toy.tokenizer.chat(HI) == toy.tokenizer.encoding.encode(text)
    drawn = toy.generate(toy.tokenizer.chat(HI), 4)
    assert toy.generate(HI, 4) == toy.tokenizer.decode(drawn)


def test_a_chat_template_jinja_file_is_read_and_may_call_strftime_now(cpu, tmp_path):
    pytest.importorskip("jinja2")
    _repository(tmp_path, cpu.weights)
    template = "{{ strftime_now('%Y') }}" + CHATML
    (tmp_path / "chat_template.jinja").write_text(template)
    tokenizer = OnHost.load(tmp_path).tokenizer
    year = datetime.date.today().strftime("%Y")
    assert tokenizer.decode(tokenizer.chat(HI)).startswith(year + "<|im_start|>")


@pytest.mark.parametrize(
    "given, written", [(None, ""), ("<s>", "<s>"), ({"content": "<s>"}, "<s>")]
)
def test_a_chat_template_writes_tokenizer_config_s_bos_token(
    cpu, tmp_path, given, written
):
    pytest.importorskip("jinja2")
    _repository(tmp_path, cpu.weights)
    settings = {"chat_template": "{{ bos_token }}" + CHATML, "bos_token": given}
    (tmp_path / "tokenizer_config.json").write_text(json.dumps(settings))
    tokenizer = OnHost.load(tmp_path).tokenizer
    text = written + "<|im_start|>user\nHi<|im_end|>\n<|im_start|>assistant\n"
    assert tokenizer.chat(HI) == tokenizer.encoding.encode(text)


def test_a_chat_template_s_raise_exception_raises_its_message(tmp_path):
    jinja2 = pytest.importorskip("jinja2")
    template = "{{ raise_exception('roles must alternate') }}"
    encoding = _tokenizer_json(tmp_path / "tokenizer.json")
    with pytest.raises(jinja2.TemplateError, match="roles must alternate"):
        Tokenizer(encoding, 0, template).chat(HI)


# Chat turns opened and closed by added tokens, after a BOS the template
# writes as given.
TURNS = (
    "{% for m in messages %}<|turn|>{{ m['role'] }}<|role_end|>"
    "\n\n{{ m['content'] }}<|turn_end|>{% endfor %}"
    "{{ '<|turn|>assistant<|role_end|>\\n\\n' }}"
)


@pytest.mark.parametrize("bos", ["{{ bos_token }}", "<|bos|>", ""])
def test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s(
    tmp_path, bos
):
    """Each added token the template writes is its id in the
    ``tokenizer.json``, not split into bytes, and the BOS is there only
    where the template writes it.
    """
    pytest.importorskip("jinja2")
    path = tmp_path / "tokenizer.json"
    specials = ["<|bos|>", "<|turn|>", "<|role_end|>", "<|turn_end|>"]
    encoding = _tokenizer_json(path, specials=specials)
    hf = pytest.importorskip("tokenizers").Tokenizer.from_file(str(path))
    begin, start, end, eot = (hf.token_to_id(t) for t in specials)
    got = Tokenizer(encoding, begin, bos + TURNS).chat(HI)
    text = encoding.encode
    assert got == [begin] * bool(bos) + [
        start,
        *text("user"),
        end,
        *text("\n\nHi"),
        eot,
        start,
        *text("assistant"),
        end,
        *text("\n\n"),
    ]
