#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Modules that own their weights, device-free: ``Graph.load`` binding each
``param`` or naming every tensor it cannot, ``draw`` and ``unread``, and
the leaf modules' references against numpy.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.lm import Embedding, LayerNorm, Linear, RMSNorm
from iron.tests.common.llama_model import SMALL, checkpoint

pytestmark = pytest.mark.usefixtures("npu2")


class Block(iron.Graph):
    def __init__(self):
        self.embed = Embedding(512, 256)
        self.norm = RMSNorm(256, 1e-5)
        self.layers = [Linear(256, 128, bias=True), Linear(128, 256)]
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


def test_load_binds_each_param_to_its_tensor():
    named = {n: t.shape for n, t in tensors("model.").items()}
    tree = checkpoint(SMALL, named | {"lm_head.weight": (512, 256)}).tree()
    block = Block()
    block.load(tree, "model.")
    assert block.layers[0].bias is tree.model.layers[0].bias and block.held()


def test_load_names_every_missing_tensor():
    named = tensors()
    del named["norm.weight"], named["layers.1.weight"]
    with pytest.raises(ValueError, match=r"missing layers\.1\.weight, norm\.weight$"):
        Block().load(named)


def test_load_names_every_extra_tensor():
    named = tensors() | {"rotary.inv_freq": np.zeros(8, np.float32)}
    with pytest.raises(ValueError, match=r"extra rotary\.inv_freq$"):
        Block().load(named)


def test_load_names_every_wrong_shaped_tensor():
    named = tensors() | {"layers.1.weight": np.zeros((128, 256), bfloat16)}
    with pytest.raises(
        ValueError,
        match=r"wrong shape layers\.1\.weight \(128, 256\), not \(256, 128\)",
    ):
        Block().load(named)


def test_load_names_each_kind_in_one_error():
    named = tensors("model.") | {"model.norm.weight": np.zeros(4, bfloat16)}
    del named["model.out.bias"]
    named["model.extra"] = np.zeros(1, bfloat16)
    with pytest.raises(ValueError) as error:
        Block().load(named, "model.")
    assert str(error.value) == (
        "Block: cannot load: missing model.out.bias; extra model.extra; "
        "wrong shape model.norm.weight (4,), not (256,)"
    )


def test_a_param_never_loaded_is_named_at_trace():
    with pytest.raises(TypeError, match=r"embed\.weight was never loaded"):
        Block().trace(ids=((4,), np.int32))


def test_draw_is_the_random_tree_of_a_checkpoint_in_the_same_order():
    """``Checkpoint.tree("random")`` draws in the file's order, ``draw`` in
    the graph's: the same tensors where the two orders agree.
    """
    block = Block()
    block.draw(3)
    named = {n: t.shape for n, t in tensors().items()}
    tree = checkpoint(SMALL, named).tree("random", 3)
    for path, x in block.held().values():
        want = tree
        for key in path.split("."):
            want = want[int(key)] if key.isdigit() else getattr(want, key)
        assert np.array_equal(x.view(np.uint16), want.view(np.uint16)), path


def test_unread_allocates_each_param():
    block = Block()
    block.unread()
    assert all(x.flags.owndata for _, x in block.held().values())


def test_leaf_modules_match_numpy():
    block = Block()
    block.draw(0)
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
