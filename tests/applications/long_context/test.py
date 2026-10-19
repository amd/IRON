#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every decoder application serves its whole context from one compile,
a library guarantee: nothing a step runs grows with the context but the
state it holds a row of per position, and on the NPU the deepest decode
step (at ``max_seq_len - 1``) and the deepest prompt chunk (the one
holding that position) agree with the graph's own reference.

The context is the checkpoint's own (``max_position_embeddings``), or
``--max-seq-len``; ``--random-weights SEED`` runs it on weights drawn in
the checkpoint's shapes.
"""

import dataclasses
import importlib
import pkgutil
from pathlib import Path

import aie.utils as aie_utils
import pytest

import iron.applications
from iron.applications.granite import Granite
from iron.applications.idefics3 import SmolVLMText
from iron.applications.lfm2 import Lfm2
from iron.applications.llama import Llama
from iron.applications.phi3 import Phi4
from iron.applications.qwen2 import Qwen2
from iron.applications.qwen3 import Qwen3
from iron.applications.smollm2 import SmolLM2
from iron.applications.smollm3 import SmolLM3
from iron.lm import CausalLM, Checkpoint, EncoderDecoder
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
# Qwen3 1.7B's decode measured 0.0039 at 32767; Granite's 0.0033 at 4095
# and its prompt chunk 2.3e-6; LFM2's decode 0.0214 at 32767 and its prompt
# chunk 1.4e-6. None is yet measured at a native context past 32768.
DEEP_KL = 0.1


@dataclasses.dataclass(frozen=True)
class Application:
    """A decoder application, a checkpoint its test runs and the forms it
    is held to here: the full ELF on NPU2 where ``full_elf``, and an xclbin a
    step on the ``each_step`` devices; ``staged`` where CI holds the
    checkpoint, so its absence fails there rather than skips.
    """

    model: type[CausalLM]
    directory: str
    weights: str
    tokenizer: str
    full_elf: bool = True
    each_step: tuple[str, ...] = ()
    deep_kl: float = DEEP_KL
    staged: bool = True

    @property
    def path(self) -> Path:
        return weights_dir(self.directory) / self.weights


INDEX = "model.safetensors.index.json"

# Qwen 2.5's and Phi-4's full ELFs did not link within an hour (their own
# tests run each step its own xclbin).
APPLICATIONS = {
    "llama_3.2_1b": Application(
        Llama,
        "llama3.2-1b",
        "model.safetensors",
        "tokenizer.json",
        each_step=("npu1", "npu2"),
    ),
    "llama_3.2_3b": Application(Llama, "llama3.2-3b", INDEX, "tokenizer.json"),
    "smollm2_1.7b": Application(
        SmolLM2,
        "smollm2-1.7b-instruct",
        "model.safetensors",
        "tokenizer.json",
        each_step=("npu1", "npu2"),
        # Unmeasured deep in the caches: 24 layers, its shallow bounds above
        # Llama's.
        deep_kl=0.2,
    ),
    "qwen2.5_1.5b": Application(
        Qwen2,
        "qwen2.5-1.5b-instruct",
        "model.safetensors",
        "tokenizer.json",
        full_elf=False,
        each_step=("npu2",),
    ),
    "qwen3_1.7b": Application(
        Qwen3, "qwen3-1.7b", INDEX, "tokenizer.json", each_step=("npu1", "npu2")
    ),
    "qwen3_0.6b": Application(
        Qwen3, "qwen3-0.6b", "model.safetensors", "tokenizer.json", staged=False
    ),
    "granite_4.2_3b": Application(Granite, "granite-4.2-3b", INDEX, "tokenizer.json"),
    "phi4_mini": Application(
        Phi4,
        "phi-4-mini-instruct",
        INDEX,
        "tokenizer.json",
        full_elf=False,
        each_step=("npu2",),
    ),
    "lfm2_1.2b": Application(Lfm2, "lfm2-1.2b", "model.safetensors", "tokenizer.json"),
    "smolvlm_256m": Application(
        SmolVLMText, "smolvlm-256m-instruct", "model.safetensors", "tokenizer.json"
    ),
    "smollm3_3b": Application(
        SmolLM3, "smollm3-3b", INDEX, "tokenizer.json", staged=False
    ),
}

#: Decoder applications held to no context yet, and why.
UNHELD = {
    "granite_hybrid": "SelectiveScan and Experts have no kernel",
    "qwen3_moe": "Experts has no kernel",
    "ministral3": "its released checkpoints nest the text decoder, unread",
}


def test_every_decoder_application_is_held_to_its_context():
    """Each application whose package exports a ``CausalLM`` has a
    checkpoint here; an encoder-decoder's context follows the clip it
    encodes, not a text prompt's.
    """
    found = set()
    for package in pkgutil.iter_modules(iron.applications.__path__):
        module = importlib.import_module(f"iron.applications.{package.name}")
        for name in getattr(module, "__all__", ()):
            model = getattr(module, name)
            if issubclass(model, CausalLM) and not issubclass(model, EncoderDecoder):
                found.add(package.name)
    held = {a.model.__module__.split(".")[2] for a in APPLICATIONS.values()}
    assert found == held | UNHELD.keys()


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
    traces = []
    for chunks in (1, 2, 4):
        model = app.model(dataclasses.replace(config, max_seq_len=chunks * C), weights)
        traces.append(model.trace(**model.shapes()[0 if version == "decode" else 1]))

    def activations(t):
        return {
            h.ref(): h.nbytes
            for s in t.steps
            for h in s.inputs + s.outputs
            if h.role not in ("weight", "state")
        }

    one, two, four = traces
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
        a, b, c = (t.pinned[name] for t in traces)
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


@pytest.fixture(scope="module", params=FORMS)
def loaded(request):
    """An application's checkpoint and model, compiled and loaded once:
    a full ELF, or with ``_each_step`` an xclbin a step, the host starting
    each on the token the last one drew.
    """
    app = APPLICATIONS[request.param.removesuffix("_each_step")]
    load = load_from_flags(request, app.model, app.path, app.tokenizer, app.staged)
    each_step = request.param.endswith("_each_step")
    model = load(full_elf=False if each_step else None)
    assert model.device_loop is not each_step
    yield app, model
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


def test_decode_deep_in_the_cache(loaded, record_property):
    """The deepest step the caches hold, at ``max_seq_len - 1``."""
    app, model = loaded
    position = model.config.max_seq_len - 1
    check_deep_decode(model, position, app.deep_kl, record=record_property)


def test_prompt_deep_in_the_cache(loaded, record_property):
    """The chunk holding ``max_seq_len - 1``, its rows: the longest
    dispatch a prompt makes, over the whole context.
    """
    app, model = loaded
    rows = model.config.prefill_chunk
    check_deep_prompt(model, rows, app.deep_kl, record=record_property)


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
