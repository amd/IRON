# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Modules that own their weights, device-free: ``Graph.load_state_dict`` binding each
``param`` or naming every tensor it cannot, and the leaf modules'
references against numpy.
"""

import dataclasses
from types import SimpleNamespace

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Precision
from iron.lm import Attention, Embedding, LayerNorm, Linear, RMSNorm
from iron.lm.blocks import KVCache, Rope
from iron.lm.checkpoint import nest, leaves
from iron.lm.golden import HuggingFace
from iron.lm.testing import assert_close, check_generation
from iron.operators.mha import MHA
from iron.operators.rms_norm import RMSNorm as RMSNormOp
from iron.operators.rope import RoPE
from iron.operators.sample import Sample
from iron.tests.support.llama_reference import OnHost
from iron.tests.support.llama_model import SMALL, checkpoint, small

pytestmark = pytest.mark.usefixtures("npu2")


class Block(iron.Graph):
    def __init__(self):
        self.embed = Embedding(512, 256)
        self.norm = RMSNorm(256, 1e-5)
        self.layers = [
            Linear(256, 128, precision=Precision.MEDIUM),
            Linear(128, 256, bias=False, precision=Precision.MEDIUM),
        ]
        self.out = LayerNorm(256)

    def body(self, ids):
        x = self.norm(self.embed(ids))
        return self.out(self.layers[1](self.layers[0](x)))


def tensors(under: str = "") -> dict[str, np.ndarray]:
    """Zeros for each of a ``Block``'s params, by dotted path under ``under``."""
    shapes = {
        "embed.weight": (512, 256),
        "norm.weight": (256,),
        "layers.0.weight": (128, 256),
        "layers.0.bias": (128,),
        "layers.1.weight": (256, 128),
        "out.weight": (256,),
        "out.bias": (256,),
    }
    return {under + n: np.zeros(s, bfloat16) for n, s in shapes.items()}


def test_load_state_dict_binds_each_param_to_its_tensor():
    named = {n: t.shape for n, t in tensors("model.").items()}
    tree = checkpoint(SMALL, named | {"lm_head.weight": (512, 256)}).tree()
    block = Block()
    block.load_state_dict(tree, path="model.")
    assert block.layers[0].bias is tree.model.layers[0].bias and block.held()


class Head(iron.Graph):
    def __init__(self):
        self.classifier = [
            None,
            Linear(256, 128, bias=False, precision=Precision.MEDIUM),
        ]


def test_an_index_a_checkpoint_skips_is_empty_and_no_leaf():
    """``nn.Sequential(nn.Flatten(), nn.Linear(...))`` names only ``1``."""
    tree = checkpoint(SMALL, {"classifier.1.weight": (128, 256)}).tree()
    with pytest.raises(AttributeError, match=r"classifier\.0\.weight is not in"):
        tree.classifier[0].weight
    assert [n for n, _ in leaves(tree)] == ["classifier.1.weight"]
    head = Head()
    head.load_state_dict(tree)
    assert head.classifier[1].weight is tree.classifier[1].weight


def test_tensors_at_indices_are_a_list_of_tensors():
    """``nn.ParameterList``'s tensors at ``0`` and ``1``, one a single zero:
    each kept as it is, none taken for an empty module.
    """
    zero, row = np.zeros(1, bfloat16), np.ones(4, bfloat16)
    tree = nest({"scales.0": zero, "scales.1": row})
    assert tree.scales[0] is zero and tree.scales[1] is row


def test_load_state_dict_names_every_missing_tensor():
    named = tensors()
    del named["norm.weight"], named["layers.1.weight"]
    with pytest.raises(ValueError, match=r"missing layers\.1\.weight, norm\.weight$"):
        Block().load_state_dict(named)


def test_load_state_dict_names_each_kind_in_one_error():
    named = tensors("model.") | {"model.norm.weight": np.zeros(4, bfloat16)}
    del named["model.out.bias"]
    named["model.extra"] = np.zeros(1, bfloat16)
    with pytest.raises(ValueError) as error:
        Block().load_state_dict(named, path="model.")
    assert str(error.value) == (
        "Block: cannot load: missing model.out.bias; extra model.extra; "
        "wrong shape model.norm.weight (4,), not (256,)"
    )


def test_a_param_never_bound_is_named_at_record():
    with pytest.raises(TypeError, match=r"embed\.weight was never loaded"):
        Block().record(ids=((4,), np.int32))


class Tied(iron.Graph):
    """An embedding and a head over one param, as a tied checkpoint has."""

    def __init__(self):
        self.embed = Embedding(512, 256)
        self.head = Linear(256, 512, bias=False, precision=Precision.MEDIUM)
        self.head.weight = self.embed.weight


def test_a_tied_param_needs_only_its_first_path():
    table = np.ones((512, 256), bfloat16)
    tied = Tied()
    tied.load_state_dict({"embed.weight": table})
    assert tied.head.weight is tied.embed.weight
    assert tied.embed.weight.base is table


def test_a_tied_param_ignores_a_tensor_at_its_other_path():
    first, second = np.ones((512, 256), bfloat16), np.zeros((512, 256), bfloat16)
    tied = Tied()
    tied.load_state_dict({"embed.weight": first, "head.weight": second})
    assert tied.head.weight is tied.embed.weight
    assert tied.embed.weight.base is first


def test_a_graph_held_at_two_paths_skips_the_second_paths_tensors():
    class Shared(iron.Graph):
        def __init__(self):
            self.a = self.b = Linear(4, 4, bias=False, precision=Precision.MEDIUM)
            self.c = self.d = [iron.param(2)]

    tensors = {
        n: np.zeros(s, bfloat16) for n, s in [("a.weight", (4, 4)), ("c.0", (2,))]
    }
    shared = Shared()
    shared.load_state_dict(tensors | {"b.weight": np.ones((4, 4), bfloat16)})
    assert shared.b.weight.base is tensors["a.weight"]
    assert shared.d[0].base is tensors["c.0"]


def test_load_state_dict_binds_params_in_lists_dicts_and_namespaces():
    class Held(iron.Graph):
        def __init__(self):
            self.items = [iron.param(2)]
            self.named = {"a": iron.param(2)}
            self.space = SimpleNamespace(b=iron.param(2))

    held = Held()
    held.load_state_dict(
        {n: np.zeros(2, bfloat16) for n in ("items.0", "named.a", "space.b")}
    )
    assert len(held.held()) == 3


def test_load_state_dict_refuses_a_param_in_a_tuple():
    class Held(iron.Graph):
        def __init__(self):
            self.pair = (iron.param(2), iron.param(2))

    with pytest.raises(TypeError, match=r"pair\.0 is in a tuple"):
        Held().load_state_dict({})


def test_load_state_dict_refuses_a_param_in_a_frozen_dataclass():
    @dataclasses.dataclass(frozen=True)
    class Pair:
        first: np.ndarray

    class Held(iron.Graph):
        def __init__(self):
            self.pair = Pair(iron.param(2))

    with pytest.raises(TypeError, match=r"pair\.first is in a tuple or a frozen"):
        Held().load_state_dict({})


@pytest.mark.parametrize("dtype", [np.float32, np.float16])
def test_load_state_dict_casts_to_the_params_dtype(dtype):
    named = {n: t.astype(dtype) for n, t in tensors().items()}
    block = Block()
    block.load_state_dict(named)
    assert block.norm.weight.dtype == bfloat16


def test_load_state_dict_keeps_a_tensor_of_the_params_dtype_as_the_view_it_is():
    named = tensors()
    block = Block()
    block.load_state_dict(named)
    assert block.norm.weight.base is named["norm.weight"]


def test_load_state_dict_refuses_a_change_of_kind():
    named = tensors() | {"norm.weight": np.ones(256, np.int32)}
    with pytest.raises(
        ValueError, match=r"wrong kind norm\.weight int32, not bfloat16"
    ):
        Block().load_state_dict(named)


def test_a_second_bind_is_refused():
    block = Block()
    block.load_state_dict(tensors())
    with pytest.raises(ValueError, match="already loaded"):
        block.load_state_dict(tensors())


def test_a_path_without_its_trailing_dot_is_refused():
    with pytest.raises(ValueError, match="'model' must end in a dot"):
        Block().load_state_dict(tensors("model."), path="model")


def test_leaf_modules_match_numpy():
    named = {n: t.shape for n, t in tensors().items()}
    block = Block()
    block.load_state_dict(checkpoint(SMALL, named).tree("random", 0))
    ids = np.array([3, 17, 511, 0], np.int32)
    f32 = {path: np.asarray(x, np.float32) for path, x in block.held().values()}

    def norm(x, w, b=0.0, centre=False):
        x = x - x.mean(-1, keepdims=True) if centre else x
        return x / np.sqrt((x * x).mean(-1, keepdims=True) + 1e-5) * w + b

    x = norm(f32["embed.weight"][ids], f32["norm.weight"])
    x = x @ f32["layers.0.weight"].T + f32["layers.0.bias"]
    x = x @ f32["layers.1.weight"].T
    want = norm(x, f32["out.weight"], f32["out.bias"], centre=True)
    got = np.asarray(block.reference(ids), np.float32)
    assert np.abs(got - want).max() < 0.05 * np.abs(want).max()


def test_leaf_modules_take_torch_nn_s_names_and_defaults():
    linear, embedding = Linear(4, 8, precision=Precision.MEDIUM), Embedding(16, 4)
    rms, layer = RMSNorm(4), LayerNorm(4)
    assert (linear.in_features, linear.out_features) == (4, 8)
    assert (
        linear.bias.shape == (8,)
        and Linear(4, 8, bias=False, precision=Precision.MEDIUM).bias is None
    )
    assert (embedding.num_embeddings, embedding.embedding_dim) == (16, 4)
    assert (rms.normalized_shape, rms.eps) == ((4,), None)
    assert (layer.normalized_shape, layer.eps) == ((4,), 1e-5)
    assert RMSNorm((4,)).normalized_shape == LayerNorm([4]).normalized_shape == (4,)


def test_attention_refuses_a_norm_of_other_than_q_k_and_v():
    with pytest.raises(ValueError, match="'qo' names other than q, k and v"):
        Attention(SMALL, 0, norms="qo")


def test_a_cache_attends_within_its_window():
    """Each layer's cache attends within the config's ``sliding_window``, the
    query's own position not counted; one built with no window attends to
    every position before the query.
    """
    model = small(sliding_window=65)
    model.model.layers[1].cache = KVCache(model.config)
    t = model.record(**model.shapes()[1])
    assert [s.op.window for s in t.steps if type(s.op) is MHA] == [64, None]


def test_a_ring_restarts_at_the_chunk_while_it_holds_the_window_before():
    """A ring of 128 positions, a window of 7 and a chunk of 64: positions
    from 70 change after 185 ran restart at 64, whose window from 57 the
    ring still holds, and after 186 at the first.
    """
    cache = KVCache(dataclasses.replace(SMALL, prefill_chunk=64, max_seq_len=512), 7)
    assert cache.ring == 128
    assert [cache.restart(70, ran) for ran in (70, 185, 186)] == [70, 64, 0]


def test_a_window_keeps_every_position_where_a_ring_takes_as_many_rows():
    """A ring and its staging take three rings' rows: at a context of three
    rings or fewer the cache keeps every position, at any chunk, a short
    context's whole one among them.
    """
    for L, C in ((384, 64), (200, 200)):
        config = dataclasses.replace(SMALL, prefill_chunk=C, max_seq_len=L)
        cache = KVCache(config, 7)
        assert cache.ring is None and cache.keys.shape[0] == L


def test_a_ring_s_chunk_attends_from_its_valid_rows_alone():
    """A chunk's queries over a ring are its whole chunk, the rows past
    ``rows`` masked; the output is bounded to ``rows`` again, so ``o_proj``
    runs on them alone.
    """
    model = small(sliding_window=8, max_seq_len=4096)
    assert model.model.layers[0].cache.ring == 512
    t = model.record(**model.shapes()[1])
    bounded = {id(b.op) for b in t.bindings if b.member.bounds is not None}
    after = [s.op for s in t.steps][[type(s.op) for s in t.steps].index(MHA) + 1 :]
    assert id(next(op for op in after if "GEMM" in type(op).__name__)) in bounded


def test_each_layer_reads_the_rows_of_its_own_rope():
    """A layer holding another ``Rope`` turns q and k by its table's rows,
    copied once a call however many layers hold it; one holding none turns
    nothing.
    """
    model = small(num_hidden_layers=3)
    layers = model.model.layers
    other = Rope(dataclasses.replace(model.config, rope_theta=1e4))
    layers[1].rope = layers[2].rope = other
    t = model.record(**model.shapes()[1])
    assert {id(model.rotary_emb.table.array), id(other.table.array)} <= t.weights.keys()
    assert sum(type(s.op) is RoPE for s in t.steps) == 6
    layers[0].rope = None
    t = model.record(**model.shapes()[1])
    assert id(model.rotary_emb.table.array) not in t.weights
    assert sum(type(s.op) is RoPE for s in t.steps) == 4


def test_a_q_table_scaled_by_two_doubles_the_logits_scale():
    """q's own table, twice k's, gives exactly the logits of attention
    scaled twice as much: every factor is a power of two.
    """
    config = dataclasses.replace(SMALL, max_seq_len=256)
    weights = checkpoint(config).tree("random", 3)
    scaled, doubled = (OnHost(config, weights) for _ in range(2))
    rope = Rope(config, q_scale=np.full(config.max_seq_len, 2.0))
    for layer in scaled.model.layers:
        layer.rope = rope
    for layer in doubled.model.layers:
        layer.self_attn.scaling = 2 / np.sqrt(config.head_dim)
    tokens = np.random.default_rng(1).integers(0, config.vocab_size, 20)
    np.testing.assert_array_equal(scaled.logits(tokens), doubled.logits(tokens))


def test_an_odd_vocabulary_pads_the_head_with_a_row_no_draw_takes():
    """An odd vocabulary's logits end mid-word: the head gains a zero row,
    Sample draws from the vocabulary's logits alone, and a session's logits
    are the vocabulary's.
    """
    config = dataclasses.replace(SMALL, vocab_size=SMALL.vocab_size - 1)
    V = config.vocab_size
    model = OnHost(config, checkpoint(config).tree("random", 3))
    head = np.asarray(model.lm_head.weight)
    assert head.shape == (V + 1, config.hidden_size) and not head[V].any()
    t = model.record(**model.shapes()[1])
    (sample,) = [s.op for s in t.steps if type(s.op) is Sample]
    assert (sample.vocab, sample.drawable) == (V + 1, V)
    tokens = np.random.default_rng(1).integers(0, V, 20)
    assert model.logits(tokens).shape == (V,)


def test_each_generation_check_prefills_its_whole_prompt():
    """A module's model holds the last check's tokens; a check that
    resumed from them would time part of its prompt as the whole.
    """

    class Starts(OnHost):
        def __call__(self, *tensors, **values):
            if tensors:
                self.starts.append(values["start"])
            return super().__call__(*tensors, **values)

    model = Starts(SMALL, checkpoint(SMALL).tree("random", 3))
    model.random_weights, model.starts = 3, []
    for _ in range(2):
        check_generation(model, 64, 1, record=lambda *_: None)
    assert model.starts == [0, 0]


def test_attention_turns_only_the_rotary_columns():
    """Under partial rotary, as Phi-4's, RoPE turns the first ``rotary_dim``
    columns of each head of q and k alone.
    """
    model = small(rotary_dim=32)
    t = model.record(**model.shapes()[1])
    turned = [s.op.cols for s in t.steps if type(s.op) is RoPE]
    assert turned == [32] * 4 and model.config.head_dim == 64


def test_a_v_norm_is_one_unweighted_rms_norm_a_layer():
    model = small()
    for i, layer in enumerate(model.model.layers):
        v = Attention(model.config, i, norms="v")
        v.q_proj, v.k_proj, v.v_proj, v.o_proj = (
            layer.self_attn.q_proj,
            layer.self_attn.k_proj,
            layer.self_attn.v_proj,
            layer.self_attn.o_proj,
        )
        layer.self_attn = v
    t = model.record(**model.shapes()[1])
    norms = [s for s in t.steps if type(s.op) is RMSNormOp]
    assert len(norms) == 7 and sum(len(s.inputs) == 1 for s in norms) == 2


class SharedKeys(HuggingFace):
    """transformers' Llama, its layer 1 attending over layer 0's keys and
    values: layer 1's k and v projections return layer 0's, which RoPE
    turns at the same positions.
    """

    @classmethod
    def build(cls, config, weights) -> "SharedKeys":
        import torch

        model = super().build("llama", config, weights).model
        first, second = (layer.self_attn for layer in model.model.layers)

        class Held(torch.nn.Module):
            def __init__(self, source):
                super().__init__()
                source.register_forward_hook(lambda _, x, y: vars(self).update(y=y))

            def forward(self, x):
                return self.y

        second.k_proj, second.v_proj = Held(first.k_proj), Held(first.v_proj)
        return cls(model)


def test_a_layer_reading_another_s_cache_projects_and_writes_no_keys(golden):
    """A layer holding layer 0's ``KVCache``, without k and v projections,
    attends over the keys layer 0 wrote and writes none: within bf16's
    tolerance of transformers' Llama sharing them the same way.
    """
    model = small()
    first, second = model.model.layers
    base = model.record(**model.shapes()[1])
    second.cache = first.cache
    second.self_attn.k_proj = second.self_attn.v_proj = None
    t = model.record(**model.shapes()[1])
    # The k and v projections, k's RoPE, and the two cache writes.
    dropped = 5
    assert len(t.steps) == len(base.steps) - dropped
    keys = [s.inputs[1].name for s in t.steps if type(s.op) is MHA]
    assert keys[0] == keys[1]
    host = OnHost(model.config, model.weights)
    host.model.layers[1].cache = host.model.layers[0].cache
    host.model.layers[1].self_attn.k_proj = None
    host.model.layers[1].self_attn.v_proj = None
    reference = golden(
        "shared_keys",
        lambda: SharedKeys.build(model.config, model.weights),
        model.config,
        model.weights,
    )
    tokens = np.arange(9)
    assert_close(host.logits(tokens), reference.logits(tokens))


def test_a_random_tree_draws_a_scalar_as_an_array():
    """A 0-d tensor drawn at random is a 0-d array, as ``iron.param`` takes
    it (a clipped linear's clamp bound), not a bare numpy scalar.
    """
    tree = checkpoint(SMALL, {"linear.input_min": (), "norm.weight": (8,)})
    bound = tree.tree("random").linear.input_min
    assert isinstance(bound, np.ndarray) and bound.shape == ()
