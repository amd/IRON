# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every decoder application serves its whole context from one compile,
a library guarantee: nothing a step runs grows with the context but the
state it holds a row of per position, and on the NPU the deepest decode
step (at ``max_seq_len - 1``) and the deepest prompt chunk (the one
holding that position) agree with the graph's own reference, at 4096,
16384, 32768, 65536 and the whole context the host fits (or
``--max-seq-len``).
``--random-weights SEED`` runs on weights drawn in the checkpoint's shapes.
"""

import dataclasses
import importlib
import pkgutil
from pathlib import Path

import aie.utils as aie_utils
import pytest

import iron.applications
from iron.applications.gemma4 import Gemma4
from iron.applications.granite import Granite
from iron.applications.granite_hybrid import GraniteHybrid
from iron.applications.llama import Llama
from iron.applications.qwen3 import Qwen3
from iron.applications.qwen3_embedding import Qwen3Embedding
from iron.applications.qwen3_moe import Qwen3Moe
from iron.applications.qwen3_reranker import Qwen3Reranker
from iron.applications.smollm2 import SmolLM2
from iron.applications.smollm3 import SmolLM3
from iron.lm import CausalLM, Checkpoint
from iron.lm.testing import (
    check_deep_decode,
    check_deep_prompt,
    check_prompt_time,
    load_from_flags,
    require,
    weights_dir,
)

# KL(graph reference || NPU) of one step deep in the caches. Llama 3.2 1B's
# decode measured 0.002 to 0.015 just past the prompt, 0.009 to 0.033 at
# 16k and 0.030 to 0.038 at 32k: it grows with the keys the step sums over.
DEEP_KL = 0.1
# Qwen3-Embedding's row is its final hidden state, held by its cosine to the
# reference, not its KL.
COSINE = 0.97


@dataclasses.dataclass(frozen=True)
class Application:
    """A decoder application, a checkpoint its test runs and the forms it
    is held to here: the full ELF on NPU2 where ``full_elf``, and an xclbin a
    step on the ``each_step`` devices. CI holds every checkpoint, so one
    missing there fails rather than skips, but where not ``staged``. A model
    whose row is a hidden state, not logits, is held deep by its cosine, at
    least ``deep_cosine``.
    """

    model: type[CausalLM]
    directory: str
    weights: str
    tokenizer: str
    full_elf: bool = True
    each_step: tuple[str, ...] = ()
    deep_kl: float = DEEP_KL
    deep_cosine: float | None = None
    staged: bool = True

    @property
    def path(self) -> Path:
        return weights_dir(self.directory) / self.weights


INDEX = "model.safetensors.index.json"

APPLICATIONS = {
    "llama_3.2_1b": Application(
        Llama,
        "llama3.2-1b",
        "model.safetensors",
        "tokenizer.json",
        each_step=("npu1", "npu2"),
    ),
    "llama_3.2_3b": Application(
        Llama, "llama3.2-3b", INDEX, "tokenizer.json", each_step=("npu1", "npu2")
    ),
    # SmolLM2 is Llama's layer at its own, narrower shape (full attention, no
    # KV groups): unmeasured deep in the caches, its shallow bounds above
    # Llama's.
    "smollm2_1.7b": Application(
        SmolLM2,
        "smollm2-1.7b-instruct",
        "model.safetensors",
        "tokenizer.json",
        each_step=("npu1", "npu2"),
        deep_kl=0.2,
    ),
    # Granite's decode measured 0.0010 to 0.0022 on npu2, 4k to the whole
    # context; npu1 still unmeasured. Each size fills the cache with its
    # own content up to max_seq_len - 1, not a continuation of the last,
    # so sizes aren't directly comparable.
    "granite_4.2_3b": Application(
        Granite, "granite-4.2-3b", INDEX, "tokenizer.json", each_step=("npu1", "npu2")
    ),
    # Gemma 4 E2B's decode measured 0.0002 to 0.072 on npu2 and 0.0009 to
    # 0.0256 on npu1, each 4k to the whole context: each size fills the
    # cache with its own content up to max_seq_len - 1, not a continuation
    # of the last, so sizes aren't directly comparable.
    "gemma4_e2b": Application(
        Gemma4,
        "gemma-4-e2b-it",
        "model.safetensors",
        "tokenizer.json",
        each_step=("npu1", "npu2"),
    ),
    # Granite 4.0-H 1B's decode measured 0.0007 to 0.0069 on npu2, 4k to
    # the whole context; its deepest prompt chunk 4.1e-5 to 0.0052; npu1
    # still unmeasured.
    "granite_4.0_h_1b": Application(
        GraniteHybrid,
        "granite-4.0-h-1b",
        "model.safetensors",
        "tokenizer.json",
        each_step=("npu1", "npu2"),
    ),
    # Qwen3's decode measured 0.0020 (0.6B, native 32768) to 0.0385 (1.7B,
    # native 32768), its deepest prompt chunk 0.0021 to 0.0565, on npu2.
    "qwen3_0.6b": Application(
        Qwen3, "qwen3-0.6b", "model.safetensors", "tokenizer.json", staged=False
    ),
    "qwen3_1.7b": Application(
        Qwen3, "qwen3-1.7b", INDEX, "tokenizer.json", each_step=("npu1", "npu2")
    ),
    # Qwen3-Embedding's row is its final hidden state, held by its cosine:
    # measured 0.98611 at its decode step at 32767 and 0.99859 over its
    # deepest prompt chunk, the bound twice the decode's distance from 1.
    "qwen3_embedding_0.6b": Application(
        Qwen3Embedding,
        "qwen3-embedding-0.6b",
        "model.safetensors",
        "tokenizer.json",
        deep_cosine=COSINE,
    ),
    # Qwen3-Reranker's decode measured 0.0212 at 32767, its deepest prompt
    # chunk 0.0038, well under DEEP_KL: it uses Qwen3's own head, not a
    # cosine-held hidden state.
    "qwen3_reranker_0.6b": Application(
        Qwen3Reranker,
        "qwen3-reranker-0.6b",
        "model.safetensors",
        "tokenizer.json",
        staged=False,
    ),
    # 30B, its experts paged from the checkpoint; staged as decoders stages
    # it. Its decode measured 0.069 at 40959 (top-1 swapped at a near tie,
    # pre-#222's numeric fixes, not yet re-verified), its deepest prompt
    # chunk 1.5e-5: twice the decode's, rounded up.
    "qwen3_moe_30b_a3b": Application(
        Qwen3Moe,
        "qwen3-30b-a3b",
        INDEX,
        "tokenizer.json",
        staged=False,
        deep_kl=0.2,
    ),
    # SmolLM3 skips RoPE on every fourth layer (NoPE): unmeasured deep in the
    # caches, its shallow bounds above Llama 3B's.
    "smollm3_3b": Application(
        SmolLM3,
        "smollm3-3b",
        INDEX,
        "tokenizer.json",
        each_step=("npu1", "npu2"),
        deep_kl=0.2,
    ),
}


def test_every_decoder_application_is_held_to_its_context():
    """Each application whose package exports a ``CausalLM`` has a
    checkpoint here.
    """
    found = set()
    for package in pkgutil.iter_modules(iron.applications.__path__):
        module = importlib.import_module(f"iron.applications.{package.name}")
        for name in getattr(module, "__all__", ()):
            model = getattr(module, name)
            if issubclass(model, CausalLM):
                found.add(package.name)
    held = {a.model.__module__.split(".")[2] for a in APPLICATIONS.values()}
    assert found == held


@pytest.mark.parametrize("version", ["decode", "prompt"])
@pytest.mark.parametrize("application", list(APPLICATIONS))
def test_nothing_grows_with_the_context(application, version):
    """At three contexts, every activation, every array and every input of
    a step is the same, and each piece of held state that differs holds a
    row per position: its size is affine in the context.
    """
    app = APPLICATIONS[application]
    require(app.path, app.path.with_name("config.json"), staged=app.staged)
    config = app.model.default_config(app.path)
    weights = Checkpoint(app.path).tree("unread")
    C = config.prefill_chunk
    records = []
    for chunks in (1, 2, 4):
        model = app.model(dataclasses.replace(config, max_seq_len=chunks * C), weights)
        records.append(model.record(**model.shapes()[0 if version == "decode" else 1]))

    def activations(t):
        return {
            h.ref(): h.nbytes
            for s in t.steps
            for h in s.inputs + s.outputs
            if h.role not in ("weight", "state")
        }

    one, two, four = records
    for t in (two, four):
        assert [h.name for h in t.inputs] == [h.name for h in one.inputs]
        assert activations(t) == activations(one)
        assert [op.array_key() for op in t.operators] == [
            op.array_key() for op in one.operators
        ]
        assert t.pinned.keys() == one.pinned.keys()
    grown = {name for name in one.pinned if four.pinned[name] != one.pinned[name]}
    assert grown, "no state holds the context"
    for name in grown:
        a, b, c = (t.pinned[name] for t in records)
        assert c - b == 2 * (b - a), f"{name}: {a}, {b}, {c} bytes is no row a position"


FORMS = [
    pytest.param(name, marks=pytest.mark.supported_devices("npu2"))
    for name, app in APPLICATIONS.items()
    if app.full_elf
] + [
    pytest.param(
        f"{name}_each_step", marks=pytest.mark.supported_devices(*app.each_step)
    )
    for name, app in APPLICATIONS.items()
    if app.each_step
]


# The context sizes each form is loaded at; None is the host's whole one
# (``Model.fit``, or ``--max-seq-len``).
CONTEXTS = (4096, 16384, 32768, 65536, None)

SWEEP = [
    pytest.param(
        (form.values[0], context),
        marks=form.marks,
        id=f"{form.values[0]}-{context or 'whole'}",
    )
    for form in FORMS
    for context in CONTEXTS
]


@pytest.fixture(scope="module", params=SWEEP)
def loaded(request):
    """An application's checkpoint and model, compiled and loaded once at
    a context size: a full ELF, or with ``_each_step`` an xclbin a step, the
    host starting each on the token the last one drew.
    """
    form, context = request.param
    app = APPLICATIONS[form.removesuffix("_each_step")]
    load = load_from_flags(
        request, app.model, app.path, app.tokenizer, staged=app.staged
    )
    fitted = app.model.fit(app.model.default_config(app.path), app.path).max_seq_len
    if context is not None and context >= fitted:
        pytest.skip(f"{app.directory} holds {fitted} positions on this host")
    each_step = form.endswith("_each_step")
    sized = {} if context is None else {"max_seq_len": context}
    model = load(full_elf=False if each_step else None, **sized)
    # The packaging, not device_loop: a full ELF with a host step (Qwen3-MoE's
    # paged experts) is one but does not loop on the device.
    assert model.decode_step.plan.full_elf is not each_step
    yield app, model
    model.release()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


@pytest.mark.extensive
def test_decode_deep_in_the_cache(loaded, record_property):
    """The deepest step the caches hold, at ``max_seq_len - 1``."""
    app, model = loaded
    position = model.config.max_seq_len - 1
    if app.deep_cosine is None:
        check_deep_decode(model, position, app.deep_kl, record=record_property)
    else:
        check_deep_decode(
            model, position, app.deep_cosine, cosine=True, record=record_property
        )


@pytest.mark.extensive
def test_prompt_deep_in_the_cache(loaded, record_property):
    """The chunk holding ``max_seq_len - 1``, its rows: the longest
    dispatch a prompt makes, over the whole context.
    """
    app, model = loaded
    rows = model.config.prefill_chunk
    if app.deep_cosine is None:
        check_deep_prompt(model, rows, app.deep_kl, record=record_property)
    else:
        check_deep_prompt(
            model, rows, app.deep_cosine, cosine=True, record=record_property
        )


@pytest.mark.extensive
@pytest.mark.bench
def test_prompt_time_at_8k(loaded, record_property):
    """Time to the first token after an 8192-token prompt, four whole
    chunks, each timed run a fresh prompt.
    """
    app, model = loaded
    if model.config.max_seq_len < 8192:
        pytest.skip(f"the context served here is {model.config.max_seq_len}")
    check_prompt_time(model, 8192, record=record_property)


@pytest.mark.extensive
def test_prompt_time_at_the_whole_context(loaded, record_property):
    """Time to the first token after a prompt filling the whole context
    served, once: the longest a prompt takes.
    """
    app, model = loaded
    check_prompt_time(model, model.config.max_seq_len, 1, record=record_property)
