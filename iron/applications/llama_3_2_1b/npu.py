# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 on the NPU: one graph function over one set of weights and
caches, and the forward pass that calls it.

:class:`LlamaGraph` holds ``forward(x, angles, *, cache_offset, vector_size,
last)``: ``x`` is the embedded tokens, ``(rows, emb_dim)``, and the function
branches on its static shape. One row is a decode step: GEMV projections,
attention against the KV caches, the row written into them at
``cache_offset``, the softmax masked to ``vector_size`` keys. Many rows are
a prompt: GEMM projections, causal MHA over the rows, the caches written in
full from row zero, and the final norm and output head for row ``last``
alone. Both end in the same norm and head.

Each shape compiles its own version of the one function, and every version
runs in the function's one scratch arena (:mod:`iron.common.graph.compiled`):
the weights (closed over from ``config.weights``) and the caches
(:func:`iron.state`) sit at one offset in every image and are uploaded
once, so the caches a prompt writes are the ones the next decode step
reads, and there is nothing to hand over.

The knobs the operators run with are a :class:`Profile`, the graph
function's own, applied whenever its body runs: ``profiles/<device>.json``
(:func:`device_profile`), keyed by operator shape at Llama 3.2 1B's shape
and :data:`MAX_SEQ_LEN`. They are the tile choices decode and prefill were
tuned with, none re-measured since; a tuner rewrites the file. Another
shape or length needs its own file. A call site gives a knob only where
two operators of one shape want different ones.

``config`` is the model's shape (``n_heads``, ``n_kv_groups``, ``head_dim``,
``emb_dim``, ``hidden_dim``) with the parameters as ``config.weights``
(:class:`.weights.LlamaWeights`); the depth is the number of layers it
holds. Each array is closed over as-is, so the tracer names and pins it by
identity. Traced here on handles; compiled by :meth:`AIELlama.compile`
against a device, or by a test against nothing.

:class:`AIELlama` is the forward pass the runner calls: the prompt in the
``max_seq_len``-row version, bounded per call to the rows it needs, and a
decode step at one row. The embedding is a numpy gather and the logits are
numpy.
"""

import math
from collections.abc import Callable
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.common import Profile, Scratchpad
from iron.common.design import has_size_kind
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm.op import GEMM
from iron.operators.gemv.op import GEMV
from iron.operators.mha.op import MHA
from iron.operators.repeat import Repeat
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope.op import RoPE
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.operators.transpose import Transpose


def _device_columns() -> int:
    """The bound device's width: eight on NPU2, four on NPU1; eight unbound."""
    dev = aie_utils.get_current_device()
    return dev.cols if dev is not None else 8


MAX_SEQ_LEN = 2048

PROFILES = Path(__file__).with_name("profiles")


def device_profile() -> Profile:
    """The profile for the bound device, ``profiles/<device>.json``: NPU2's
    unbound, as the graph's widths are.
    """
    dev = aie_utils.get_current_device()
    name = type(dev).__name__.lower() if dev is not None else "npu2"
    path = PROFILES / f"{name}.json"
    if not path.exists():
        raise ValueError(f"no Llama profile for {name}: {path} does not exist")
    return Profile.load(path)


def prompt_rows(n: int, max_seq_len: int) -> int:
    """The rows a prompt of ``n`` tokens runs at: ``n`` rounded up to what
    MHA's pipelines take at once (64 rows each, eight of them at full
    length), which the GEMMs' row block divides, at most the context
    length. What the graph's ``rows`` takes.
    """
    unit = 64 * min(8, max_seq_len // 64)
    return min(-(-n // unit) * unit, max_seq_len)


class LlamaGraph:
    """The graph function and the state it closes over.

    ``keys[i]`` and ``values[i]`` are the layer caches, each ``(n_kv_groups,
    max_seq_len, head_dim)``: the per-group layout both phases write and
    decode's repeat reads. ``scale`` is the attention scale as a tensor,
    since the elementwise multiply takes one.

    The prompt version is traced at ``max_seq_len`` rows and, when
    ``bounded``, bounded per call: ``rows`` (:func:`prompt_rows`) is how
    many of them a call runs, so the work follows the prompt; ``vector_size``
    is the true length, which MHA masks to. A bounded prompt's full ELF
    needs mlir-aie's size kind, so ``bounded`` defaults to whether the
    toolchain has it; unbounded, a prompt runs every row, as it did before
    the bound, and ``rows`` and ``vector_size`` are unread: a prompt row
    attends causally, so the padding rows after it never reach it.

    A decode step reads the caches in full: the context GEMV's reduction is
    the cache length and array-tier, so the value side cannot shorten, and
    the key side alone would leave the CPU reference nothing faithful to
    compute.

    ``profile`` is the knobs' :class:`Profile`: :func:`device_profile`'s
    unless given, as a test at another shape gives its own.
    """

    def __init__(self, config, max_seq_len, *, profile=None, bounded=None):
        W = config.weights
        H, G, D = config.n_heads, config.n_kv_groups, config.head_dim
        E = config.emb_dim
        L = max_seq_len
        self.max_seq_len = L
        self.bounded = has_size_kind() if bounded is None else bounded
        bounded = self.bounded
        self.profile = device_profile() if profile is None else profile
        cols = _device_columns()
        self.keys = [
            iron.state((G, L, D), name=f"keys_cache_{i}") for i in range(len(W.layers))
        ]
        self.values = [
            iron.state((G, L, D), name=f"values_cache_{i}")
            for i in range(len(W.layers))
        ]
        # 1/sqrt(head_dim) over every score, as the elementwise multiply wants it.
        self.scale = np.full((H, L), 1.0 / math.sqrt(D), dtype=bfloat16)
        keys, values, scale = self.keys, self.values, self.scale

        # -- one row: a decode step ------------------------------------------

        def decode_block(i, lw, x, angles, cache_offset, vector_size):
            h = RMSNorm(x, lw.norm1)
            # <grouped query attention>
            # Matrices are read as the checkpoint ships them, (out, in):
            # GEMV's (M, K). The projections into heads write half a head
            # per tile; q's shape is o's when H * D == E, so it is given here.
            q, k, v = (GEMV(w, h, tile_size_output=D // 2) for w in (lw.q, lw.k, lw.v))
            q = RoPE(q.reshape(H, D), angles)
            k = RoPE(k.reshape(G, D), angles)
            Copy(k, keys[i][:, cache_offset])
            Copy(v.reshape(G, D), values[i][:, cache_offset])
            # Every head sees its group's keys and values.
            k_all = Repeat(keys[i], repeat=H // G)
            v_all = Repeat(values[i], repeat=H // G)
            scores = GEMV(k_all, q)
            # One row of scores per column; its size is the FFN's when
            # H * L == F, so the tile is given here.
            scores = ElementwiseMul(scores, scale, tile_size=L // cols)
            # The valid row length is the context length: the kernel masks
            # every column from there on, so the cache's unwritten tail
            # contributes nothing.
            weights = Softmax(scores, vector_size=vector_size)
            v_t = Transpose(v_all)
            ctx = GEMV(v_t, weights)
            o = GEMV(lw.o, ctx.reshape(H * D))
            # </grouped query attention>
            x = ElementwiseAdd(x, o)
            h = RMSNorm(x, lw.norm2)
            gate = GEMV(lw.gate, h)
            up = GEMV(lw.up, h)
            act = ElementwiseMul(SiLU(gate), up)
            down = GEMV(lw.down, act)
            return ElementwiseAdd(x, down)

        # -- many rows: a prompt ---------------------------------------------

        def gemm(x, weight):
            # Every projection is read as the checkpoint ships it, (out, in):
            # GEMM's column-major B, the layout the GEMVs read too.
            return GEMM(x, weight, b_col_maj=True)

        def prefill_block(i, lw, x, angles, rows, vector_size):
            n = x.shape[0]
            h = RMSNorm(x, lw.norm1)
            # <grouped query attention>
            q = gemm(h, lw.q)  # (n, H*D)
            k = gemm(h, lw.k)  # (n, G*D)
            v = gemm(h, lw.v)
            # One angle row per position, applied to that position's heads.
            q = RoPE(q.reshape(n * H, D), angles)
            k = RoPE(k.reshape(n * G, D), angles)
            # (n, G, D), the heads interleaved per token as the projection
            # wrote them, into the first n rows of the cache's (G, L, D).
            Copy(
                k.reshape(n, G, D).transpose(1, 0, 2),
                keys[i][:, :rows],
                tile_size=1024,
            )
            Copy(
                v.reshape(n, G, D).transpose(1, 0, 2),
                values[i][:, :rows],
                tile_size=1024,
            )
            # Attention over the rows the call runs, masked to its true length
            # when bounded. Unbounded, MHA reads its lengths from its build,
            # and the causal mask alone keeps the padding rows out of the
            # prompt's.
            masks = dict(s_q=vector_size, s_kv=vector_size) if bounded else {}
            o = MHA(
                q.reshape(n, H, D),
                k.reshape(n, G, D),
                v.reshape(n, G, D),
                heads_interleaved=True,
                **masks,
            )
            o = gemm(o.reshape(n, H * D), lw.o)
            # </grouped query attention>
            x = ElementwiseAdd(x, o)
            h = RMSNorm(x, lw.norm2)
            gate = gemm(h, lw.gate)
            up = gemm(h, lw.up)
            act = ElementwiseMul(SiLU(gate), up)
            down = gemm(act, lw.down)
            return ElementwiseAdd(x, down)

        @iron.graph(names_from=W, profile=self.profile)
        def forward(
            x,
            angles,
            *,
            rows: Scratchpad[np.int32],
            cache_offset: Scratchpad[np.int32],
            vector_size: Scratchpad[np.int32],
            last: Scratchpad[np.int32],
        ):
            prompt = x.shape[0] > 1
            if prompt and bounded:
                # The first rows of the padded prompt are the ones this call
                # runs; every operator below is bounded by them.
                x, angles = x[:rows], angles[:rows]
            for i, lw in enumerate(W.layers):
                if prompt:
                    span = rows if bounded else x.shape[0]
                    x = prefill_block(i, lw, x, angles, span, vector_size)
                else:
                    x = decode_block(i, lw, x, angles, cache_offset, vector_size)
            if prompt:
                # The last prompt row alone: its logits are all the host reads.
                x = Copy(x[last]).reshape(1, E)
            x = RMSNorm(x, W.norm)
            return GEMV(W.out_head, x)

        self.graph = forward

    def shapes(self, config, rows):
        """The input shapes of the version that runs ``rows`` tokens."""
        return dict(x=(rows, config.emb_dim), angles=(rows, config.head_dim))

    def trace(self, config, rows):
        return self.graph.trace(**self.shapes(config, rows))

    def compile(self, config, rows, **kwargs):
        return self.graph.compile(**self.shapes(config, rows), **kwargs)


# Running it
# ##########################################################################


class AIELlama:
    """The model as one graph function called at the prompt's and a token's shape.

    ``forward_graph`` is that function -- a compiled
    :class:`~iron.common.graph.compiled.GraphFunction`, or anything called
    the same way and returning a buffer with ``numpy()``. :meth:`forward`
    is the ``forward_pass`` the runner calls.
    """

    def __init__(self, config, forward_graph: Callable, max_seq_len: int):
        self.config = config
        self.forward_graph = forward_graph
        self.max_seq_len = max_seq_len
        # The RoPE table as the images read it, as far as they reach. A
        # float32 table would be another input signature, and so another
        # compile.
        self.angles = config.angles[:max_seq_len].astype(bfloat16)

    @classmethod
    def compile(cls, config, max_seq_len=MAX_SEQ_LEN) -> "AIELlama":
        """Trace, compile and load both versions, weights uploaded.

        Both before the first call, so the shared arena is made once at its
        final size. The checkpoint's pages are dropped a piece at a time as
        they reach the device, so the process holds at most one piece of it
        beside the buffers; the embedding's rows fault back in as it is read.
        """
        model = LlamaGraph(config, max_seq_len)
        for rows in (1, max_seq_len):
            model.compile(config, rows)
        for version in model.graph.versions.values():
            version.load(release=config.weights.release)
        return cls(config, model.graph, max_seq_len)

    # -- the forward pass ----------------------------------------------------

    def forward(self, config, state):
        """``state.token_ids`` through the model; the logits after the last, ``(1, 1, vocab)``."""
        batch, seq_len = state.token_ids.shape
        assert batch == 1
        if seq_len > 1:
            logits = self._prefill(state.token_ids[0])
            state.num_preceding_tokens = seq_len
        else:
            logits = self._decode(
                int(state.token_ids[0, 0]), state.num_preceding_tokens
            )
            state.num_preceding_tokens += 1
        # A copy: the image's output buffer is rewritten by the next call.
        return np.array(logits).reshape(1, 1, config.vocab_size), state

    def _prefill(self, token_ids):
        config, rows = self.config, self.max_seq_len
        n = token_ids.shape[0]
        assert 0 < n <= rows
        # The prompt fills the first rows; the rest are never read (attention is
        # causal, and decode masks the cache's tail by its vector size).
        x = np.zeros((rows, config.emb_dim), dtype=bfloat16)
        x[:n] = config.weights.embed(token_ids)
        # Every call passes every per-call value; a version reads the ones
        # its operators bind. Here: the rows the prompt runs at, its true
        # length for the masks, and the last prompt row's logits, selected
        # by its row.
        return self.forward_graph(
            x,
            self.angles[:rows],
            rows=prompt_rows(n, rows),
            cache_offset=0,
            vector_size=n,
            last=n - 1,
        ).numpy()

    def _decode(self, token_id, position):
        config = self.config
        assert position < self.max_seq_len
        # The softmax's valid row length is the context length: the kernel masks
        # every column from there on before the softmax, so the cache's unwritten
        # tail contributes nothing. A running sum of context lengths is wrong
        # here: iron/tests/common/llama_reference.py shows it drifting from
        # the CPU reference from the second token on.
        return self.forward_graph(
            config.weights.embed([token_id]).reshape(1, config.emb_dim),
            self.angles[position : position + 1],
            rows=1,
            cache_offset=position,
            vector_size=position + 1,
            last=0,
        ).numpy()
