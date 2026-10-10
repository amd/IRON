# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Numpy reference of one Gemma 4 decode layer, as the flm_gemma4_decode
kernels compute it.

The reference takes the five buffers of DecodeLayer and returns x and the kv
cache as the device leaves them:

    x_out, kv_out = reference(
        FLM_GEMMA4_E2B_DECODE, "swa", x, proj, rms, rope_rms, kv,
        context_len=37, max_l=1024)

It reproduces the kernels' rounding, accumulation order and lookup tables with
aie2p_math_emulation. A product or an inverse square root can still differ
from the device's in the last fp32 bit. Near a bf16 boundary that difference
changes the bf16 result by one ulp.

generate_inputs() draws synthetic buffers with a fixed seed.
"""

import dataclasses

import numpy as np
from aie.iron.kernels import bf16_exp_lut_ref

from iron.operators.flm.aie2p_math_emulation import (
    bfp16,
    f32,
    fast_rsqrt,
    fmul,
    gelu_kernel,
    inv_kernel,
    rb,
    to_bf16,
    tree_sum,
)
from iron.operators.flm.layer.design import (
    LAYER_TYPES,
    LK,
    MIN_BF16_PAD,
    SLIDING_WINDOW,
)
from iron.operators.flm.q4nx import (
    BLOCK_BYTES,
    GROUP,
    K_TILE,
    M_TILE,
    bf16_to_f32,
    packed_bytes,
)

# The epsilon of aie_kernels/flm_gemma4/rms_norm.h.
RMS_EPS = 1e-6
# The block of a bf16 projection, from aie_kernels/flm_gemma4/decode_bf16_proj.h.
BF16_M, BF16_K = 32, 256


def layer_dims(geometry, layer_type):
    """The dimensions of one layer type, in elements, by geometry field name.

    geometry is aie.iron.kernels.FLM_GEMMA4_E2B_DECODE or FLM_GEMMA4_E4B_DECODE.
    dh is the head dim of this layer type. A skip layer with double_wide_mlp has
    twice the intermediate size.
    """
    if layer_type not in LAYER_TYPES:
        raise ValueError(f"layer_type must be one of {LAYER_TYPES}")
    g = dataclasses.asdict(geometry)
    g["swa"] = layer_type.startswith("swa")
    g["skip"] = layer_type.endswith("_skip")
    if g["swa"]:
        g["dh"] = g["swa_dh"]
    g["dq"] = g["num_attn_heads"] * g["dh"]
    g["dk"] = g["num_kv_heads"] * g["dh"]
    if g["skip"] and g["double_wide_mlp"]:
        g["intermediate_size"] *= 2
    return g


# ---------------------------------------------------------------------------
# Buffer layout
# ---------------------------------------------------------------------------


def proj_layout(geometry, layer_type):
    """Weight name -> (byte offset, format, rows, cols) in proj.

    The weights lie back to back: q, k and v (absent on a skip layer), o, the
    interleaved up/gate and down in q4nx, then the per-layer-input down, gate
    and up projections in blocked bf16. rows are output features.
    """
    g = layer_dims(geometry, layer_type)
    D, F, P = g["model_dim"], g["intermediate_size"], g["pli_d"]
    items = [("q", "q4nx", g["dq"], D)]
    if not g["skip"]:
        items += [("k", "q4nx", g["dk"], D), ("v", "q4nx", g["dk"], D)]
    items += [
        ("o", "q4nx", D, g["dq"]),
        ("up_gate", "q4nx", 2 * F, D),
        ("down", "q4nx", D, F),
        ("pli_down", "bf16", P, D),
        ("pli_gate", "bf16", P, D),
        ("pli_up", "bf16", D, P),
    ]
    out, off = {}, 0
    for name, fmt, rows, cols in items:
        out[name] = (off, fmt, rows, cols)
        off += _size(fmt, rows, cols)
    return out


def _size(fmt, rows, cols):
    """Bytes of a weight in q4nx or in bf16."""
    return packed_bytes(rows * cols) if fmt == "q4nx" else 2 * rows * cols


def rope_rms_layout(geometry, layer_type):
    """Element offsets in rope_rms: cos and sin of this token's position, the q
    and k norm weights, the per-layer embedding of this token, the per-layer
    norm weight, the post-per-layer-input norm weight and the layer scale.
    """
    g = layer_dims(geometry, layer_type)
    dh, P, D = g["dh"], g["pli_d"], g["model_dim"]
    lay = dict(cos=0, sin=dh // 2, q_norm=dh, k_norm=2 * dh, pli_embed=3 * dh)
    lay["pli_norm"] = lay["pli_embed"] + P
    lay["post_pli_norm"] = lay["pli_norm"] + P
    lay["layer_scale"] = lay["post_pli_norm"] + D
    lay["size"] = lay["layer_scale"] + 1 + MIN_BF16_PAD
    return lay


def kv_rows(geometry, layer_type, max_l):
    """Rows of each half (K, then V) of the kv cache."""
    return SLIDING_WINDOW if layer_dims(geometry, layer_type)["swa"] else max_l


def kv_row(geometry, layer_type, context_len):
    """The cache row of the token at position context_len."""
    if layer_dims(geometry, layer_type)["swa"]:
        return context_len % SLIDING_WINDOW
    return context_len


def _attention_rows(g, context_len):
    """Cache rows in the order the attention core reads them, and how many hold
    keys. The core reads whole rounds and masks the rows past the keys. A
    sliding-window ring of L >= 512 tokens holds them in time order from row
    L % 512.
    """
    L = context_len + 1
    if g["swa"] and L >= SLIDING_WINDOW:
        lb = L % SLIDING_WINDOW
        return (
            np.concatenate([np.arange(lb, SLIDING_WINDOW), np.arange(lb)]),
            SLIDING_WINDOW,
        )
    return np.arange(-(-L // LK) * LK), L


# ---------------------------------------------------------------------------
# RMS norm
# ---------------------------------------------------------------------------


def rms_norm(x, w):
    """rms_norm.h: bf16(x * w * rsqrt(mean(x^2) + eps)). w is None for the v
    norm.
    """
    x = np.asarray(x, np.float64)
    s = f32(
        fmul(tree_sum(x * x, 16)[..., None], np.float32(1.0 / x.shape[-1]))
        + np.float32(RMS_EPS)
    )
    return rb(fmul(x if w is None else f32(x * w), fast_rsqrt(s)))


# ---------------------------------------------------------------------------
# Weights and projections
# ---------------------------------------------------------------------------


# The bytes of a q4nx block's bf16 scales and minima.
_SM_BYTES = 2 * 2 * M_TILE * K_TILE // GROUP


def parse_q4nx(proj_u8, offset, rows, cols):
    """A q4nx weight in natural order: (codes [rows, cols], scales and mins
    [rows, cols / 32]). The weight is min + scale * code.

    A block holds 32 rows by 256 columns in 5120 bytes: 256 bf16 scales, 256 bf16
    minima at index g * 32 + r, then 8192 4-bit codes at nibble
    (r // 16) * 4096 + c * 16 + r % 16, low nibble first. Blocks go by pairs of
    32-row bands: column block c of band 2p, then of band 2p + 1.
    """
    nb_r, nb_c = rows // M_TILE, cols // K_TILE
    blk = proj_u8[offset : offset + nb_r * nb_c * BLOCK_BYTES]
    blk = blk.reshape(nb_r // 2, nb_c, 2, BLOCK_BYTES).transpose(0, 2, 1, 3)
    blk = blk.reshape(nb_r, nb_c, BLOCK_BYTES)
    sm = blk[..., :_SM_BYTES].copy().view("<u2")
    sm = bf16_to_f32(sm.reshape(nb_r, nb_c, 2, K_TILE // GROUP, M_TILE))
    sm = sm.transpose(2, 0, 4, 1, 3).reshape(2, rows, cols // GROUP)
    qs = blk[..., _SM_BYTES:]
    codes = np.empty(qs.shape[:-1] + (M_TILE * K_TILE,), np.uint8)
    codes[..., 0::2] = qs & 0x0F
    codes[..., 1::2] = qs >> 4
    codes = codes.reshape(nb_r, nb_c, 2, K_TILE, 16).transpose(0, 2, 4, 1, 3)
    return codes.reshape(rows, cols), sm[0], sm[1]


def parse_bf16_blocked(proj_u8, offset, rows, cols):
    """A bf16 weight in 32 x 256 blocks, row-block major. Element k * 32 + m of
    block (i, j) is W[32 i + m, 256 j + k].
    """
    w = bf16_to_f32(proj_u8[offset : offset + 2 * rows * cols].view("<u2"))
    w = w.reshape(rows // BF16_M, cols // BF16_K, BF16_K, BF16_M).transpose(0, 3, 1, 2)
    return w.reshape(rows, cols)


def q4_matvec(x, codes, scales, mins, chunk=2048):
    """W x for a q4nx weight, in the kernel's order.

    Per row and group of 32 inputs the kernel adds code * x in fp32 in column
    order and rounds the sum t to bf16. It rounds the group sum s_x of x to bf16
    once. It accumulates t * scale, then min * s_x, in fp32 over the groups.
    """
    x = np.asarray(x, np.float64)
    rows, cols = codes.shape
    G = cols // GROUP
    xg = x.reshape(G, GROUP)
    sx = rb(tree_sum(xg, 32))
    y = np.empty(rows)
    for r0 in range(0, rows, chunk):
        c = codes[r0 : r0 + chunk].reshape(-1, G, GROUP).astype(np.float64)
        s, m = scales[r0 : r0 + chunk], mins[r0 : r0 + chunk]
        t = np.zeros(c.shape[:2], np.float32)
        for ci in range(GROUP):
            t = f32(t + c[..., ci] * xg[:, ci])
        t = rb(t)
        acc = np.zeros(c.shape[0], np.float32)
        for gi in range(G):
            acc = f32(acc + t[:, gi] * s[:, gi])
            acc = f32(acc + m[:, gi] * sx[gi])
        y[r0 : r0 + chunk] = acc
    return rb(y)


def bf16_matvec(x, w):
    """W x for a bf16 weight: fp32 multiply-accumulate over the inputs in order."""
    acc = np.zeros(w.shape[0], np.float32)
    for k in range(w.shape[1]):
        acc = f32(acc + w[:, k].astype(np.float64) * x[k])
    return rb(acc)


# ---------------------------------------------------------------------------
# Layer stages
# ---------------------------------------------------------------------------


def rope_head(x, w_norm, cos, sin):
    """Per-head RMS norm, then rotate-half RoPE. A global layer rotates the first
    64 pairs only: the engine passes cos 1 and sin 0 for the others.
    """
    xn = rms_norm(x, w_norm)
    h = xn.shape[-1] // 2
    x1, x2 = xn[..., :h], xn[..., h:]
    return np.concatenate(
        [rb(f32(x1 * cos - x2 * sin)), rb(f32(x1 * sin + x2 * cos))], -1
    )


def attention(q, K, V, valid, n_kv):
    """One query against the cache rows K, V [rows, n_kv, dh] in read order.

    Scale 1.0: q and k are RMS normalized. Per head the kernel runs an online
    softmax over rounds of 16 keys:
        s     = bf16(q . k)
        mx    = max(m, max(s))
        p     = bf16(exp(bf16(s - mx))), 0 for rows past `valid`
        c     = exp(bf16(m - mx))
        denom = denom * c + bf16(sum(p))
        y     = y * c + p . V
    and returns bf16(bf16(y) * inv(denom)). q . k and p . V run on bfp16 operands.
    """
    H, dh = q.shape
    n_rows = K.shape[0]
    kv_of = np.arange(H) // (H // n_kv)
    Kh = bfp16(K[:, kv_of, :], 2)
    parts = np.einsum(
        "hcd,rhcd->hrc", bfp16(q, 1).reshape(H, -1, 8), Kh.reshape(n_rows, H, -1, 8)
    )
    s_acc = np.zeros((H, n_rows), np.float32)
    for ci in range(parts.shape[-1]):
        s_acc = f32(s_acc + parts[..., ci])
    s_all = rb(s_acc)
    Vh = bfp16(V, 0)[:, kv_of, :]

    neg_max = -3.3895313892515355e38  # the bf16 lowest value
    m = np.full(H, neg_max)
    denom = np.zeros(H, np.float32)
    y = np.zeros((H, dh), np.float32)
    for r0 in range(0, n_rows, LK):
        sr = s_all[:, r0 : r0 + LK]
        mask = (np.arange(r0, r0 + LK) < valid)[None, :]
        vmax = np.maximum(np.max(np.where(mask, sr, neg_max), 1), m)
        # The kernel clamps the exponent to [-87, 88]. bf16_exp_lut_ref
        # equals FastFlowLM's table on that range.
        d = np.clip(rb(f32(sr - vmax[:, None])), -87.0, 88.0)
        p = np.where(mask, rb(bf16_exp_lut_ref(d)), 0.0)
        c = bf16_exp_lut_ref(np.clip(rb(f32(m - vmax)), -87.0, 88.0))
        m = vmax
        denom = f32(fmul(denom, c) + rb(tree_sum(p, 16)))
        y = fmul(y, c[:, None])
        pb = bfp16(p, 1)
        vr = Vh[r0 : r0 + LK]
        for k0 in (0, 8):
            y = f32(y + np.einsum("hk,khd->hd", pb[:, k0 : k0 + 8], vr[k0 : k0 + 8]))
    return rb(rb(y) * inv_kernel(denom)[:, None])


def glu(up_gate, glu_slice):
    """bf16(gelu(gate) * up). Each glu_slice-row slice of the up/gate output
    holds glu_slice / 2 up values, then glu_slice / 2 gate values.
    """
    u = up_gate.reshape(-1, 2, glu_slice // 2)
    return rb(gelu_kernel(u[:, 1]) * u[:, 0]).reshape(-1)


def _u8(buf):
    return np.ascontiguousarray(buf).reshape(-1).view(np.uint8)


def reference(geometry, layer_type, x, proj, rms, rope_rms, kv, context_len, max_l):
    """One decode-layer dispatch on DecodeLayer's five buffers.

    The buffers are numpy arrays of any dtype (bf16, uint16 or uint8) and may be
    longer than the layer needs. Returns copies of x and kv as uint16 bf16 bit
    patterns: the layer output in x[:D], and on a non-skip layer this token's K
    and V rows in kv.
    """
    g = layer_dims(geometry, layer_type)
    D, dh, H, n_kv, P, dk = (
        g["model_dim"],
        g["dh"],
        g["num_attn_heads"],
        g["num_kv_heads"],
        g["pli_d"],
        g["dk"],
    )
    x16, rms16, rr16 = (_u8(b).view("<u2") for b in (x, rms, rope_rms))
    proj_u8 = _u8(proj)
    W = proj_layout(geometry, layer_type)
    lay = rope_rms_layout(geometry, layer_type)

    def vec(buf, off, n):
        return bf16_to_f32(buf[off : off + n]).astype(np.float64)

    def q4(name, v):
        off, _, rows, cols = W[name]
        return q4_matvec(v, *parse_q4nx(proj_u8, off, rows, cols))

    def bf(name, v):
        off, _, rows, cols = W[name]
        return bf16_matvec(v, parse_bf16_blocked(proj_u8, off, rows, cols))

    h0, emb = vec(x16, 0, D), vec(x16, 2 * D, D)
    w_in, w_post_attn, w_pre_ff, w_post_ff = (vec(rms16, i * D, D) for i in range(4))
    cos, sin = vec(rr16, lay["cos"], dh // 2), vec(rr16, lay["sin"], dh // 2)
    layer_scale = vec(rr16, lay["layer_scale"], 1)[0]

    xn = rms_norm(h0, w_in)
    q = rope_head(q4("q", xn).reshape(H, dh), vec(rr16, lay["q_norm"], dh), cos, sin)

    kv_out = _u8(kv).view("<u2").copy()
    rows = kv_rows(geometry, layer_type, max_l)
    v_off = rows * dk
    if not g["skip"]:
        k_new = rope_head(
            q4("k", xn).reshape(n_kv, dh), vec(rr16, lay["k_norm"], dh), cos, sin
        )
        v_new = rms_norm(q4("v", xn).reshape(n_kv, dh), None)
        r = kv_row(geometry, layer_type, context_len)
        kv_out[r * dk : (r + 1) * dk] = to_bf16(k_new.reshape(-1))
        kv_out[v_off + r * dk : v_off + (r + 1) * dk] = to_bf16(v_new.reshape(-1))

    # The attention reads the cache after this token's row lands in it.
    order, valid = _attention_rows(g, context_len)
    cache = bf16_to_f32(kv_out[: 2 * v_off]).astype(np.float64)
    K = cache[:v_off].reshape(rows, n_kv, dh)[order]
    V = cache[v_off:].reshape(rows, n_kv, dh)[order]
    o = attention(q, K, V, valid, n_kv)

    h1 = rb(h0 + rms_norm(q4("o", o.reshape(-1)), w_post_attn))
    act = glu(q4("up_gate", rms_norm(h1, w_pre_ff)), g["glu_slice"])
    h2 = rb(h1 + rms_norm(q4("down", act), w_post_ff))

    # The per-layer input of this layer, from the token embedding:
    # bf16(norm(bf16(W_down emb) / sqrt(D)) + per-layer embedding) / sqrt(2).
    pli = rb(bf("pli_down", emb) * rb(g["pli_input_scale"], "rne"))
    pli = rb(
        rms_norm(pli, vec(rr16, lay["pli_norm"], P)) + vec(rr16, lay["pli_embed"], P)
    )
    pli = rb(pli * rb(g["pli_projection_scale"], "rne"))
    gate = gelu_kernel(bf("pli_gate", h2))
    up = bf("pli_up", rb(pli * gate))
    out = rb(rb(h2 + rms_norm(up, vec(rr16, lay["post_pli_norm"], D))) * layer_scale)

    x_out = x16.copy()
    x_out[:D] = to_bf16(out)
    return x_out, kv_out


# ---------------------------------------------------------------------------
# Synthetic inputs
# ---------------------------------------------------------------------------


def pack_q4nx(codes, scales, mins):
    """The proj bytes of a q4nx weight; the inverse of parse_q4nx."""
    rows, cols = codes.shape
    nb_r, nb_c = rows // M_TILE, cols // K_TILE
    sm = np.stack([scales, mins]).reshape(2, nb_r, M_TILE, nb_c, K_TILE // GROUP)
    sm = sm.transpose(1, 3, 0, 4, 2).reshape(nb_r, nb_c, _SM_BYTES // 2)
    sm = to_bf16(sm, "rne").view(np.uint8).reshape(nb_r, nb_c, _SM_BYTES)
    c = (
        codes.reshape(nb_r, 2, 16, nb_c, K_TILE)
        .transpose(0, 3, 1, 4, 2)
        .reshape(nb_r, nb_c, M_TILE * K_TILE)
    )
    qs = (c[..., 0::2] | (c[..., 1::2] << 4)).astype(np.uint8)
    blk = np.concatenate([sm, qs], -1).reshape(nb_r // 2, 2, nb_c, BLOCK_BYTES)
    return blk.transpose(0, 2, 1, 3).reshape(-1)


def pack_bf16_blocked(w):
    """The proj bytes of a bf16 weight; the inverse of parse_bf16_blocked."""
    rows, cols = w.shape
    b = w.reshape(rows // BF16_M, BF16_M, cols // BF16_K, BF16_K).transpose(0, 2, 3, 1)
    return to_bf16(b.reshape(-1), "rne").view(np.uint8)


def generate_inputs(geometry, layer_type, context_len, max_l, seed=0):
    """Random buffers (x, proj, rms, rope_rms, kv) for one dispatch, as uint16
    bf16 bit patterns (proj as uint8).

    The magnitudes follow the E2B checkpoint. The projections keep their
    outputs near unit RMS. The k norm weight and the cached K rows are near 0.1,
    so that the attention scores stay near unit size. With unit K rows the
    softmax is so peaked that a 1-ulp change of one score moves the layer
    output by 5e-3. The kv cache holds rows for every earlier token. A skip
    layer also finds this token's row, which the layer that owns the cache
    writes. _plant_needles makes the output depend strongly on which cache
    rows the layer reads.
    """
    rng = np.random.default_rng(seed)
    g = layer_dims(geometry, layer_type)
    D, P, dh, dk = g["model_dim"], g["pli_d"], g["dh"], g["dk"]
    W = proj_layout(geometry, layer_type)
    end = max(off + _size(fmt, rows, cols) for off, fmt, rows, cols in W.values())
    proj = np.zeros(end, np.uint8)
    for off, fmt, rows, cols in W.values():
        std = 1 / np.sqrt(cols)
        if fmt == "q4nx":
            scale = np.abs(rng.normal(std / 4.6, std / 20, (rows, cols // GROUP)))
            mins = -7.5 * scale + rng.normal(0, std / 10, scale.shape)
            codes = rng.integers(0, 16, (rows, cols), dtype=np.uint8)
            blob = pack_q4nx(codes, scale, mins)
        else:
            blob = pack_bf16_blocked(rng.normal(0, std, (rows, cols)))
        proj[off : off + blob.size] = blob

    x = np.concatenate(
        [rng.normal(0, 2, D), rng.normal(1, 0.1, D), rng.normal(0, 1, D)]
    )
    # The input, post-attention, pre-feedforward and post-feedforward norms.
    rms = (rng.normal(1, 0.2, (4, D)) * np.array([[20], [0.5], [4], [1]])).reshape(-1)

    lay = rope_rms_layout(geometry, layer_type)
    rr = np.zeros(lay["size"])
    if g["swa"]:
        inv_freq = 10000.0 ** (-np.arange(dh // 2) * 2 / dh)
    else:
        inv_freq = np.zeros(dh // 2)
        inv_freq[:64] = 1e6 ** (-np.arange(64) * 2 / dh)
    rr[lay["cos"] : lay["cos"] + dh // 2] = np.cos(inv_freq * context_len)
    rr[lay["sin"] : lay["sin"] + dh // 2] = np.sin(inv_freq * context_len)
    for name, n, mean, std in (
        ("q_norm", dh, 1, 0.2),
        ("k_norm", dh, 0.1, 0.02),
        ("pli_embed", P, 0, 1),
        ("pli_norm", P, 1, 0.2),
        ("post_pli_norm", D, 0.5, 0.1),
    ):
        rr[lay[name] : lay[name] + n] = rng.normal(mean, std, n)
    rr[lay["layer_scale"]] = 0.6

    rows = kv_rows(geometry, layer_type, max_l)
    kv = np.zeros((2, rows, dk))
    n = min(context_len + g["skip"], rows)
    kv[0, :n] = rng.normal(0, 0.1, (n, dk))
    kv[1, :n] = rng.normal(0, 1, (n, dk))
    x, rms, rr = to_bf16(x, "rne"), to_bf16(rms, "rne"), to_bf16(rr, "rne")
    _plant_needles(g, context_len, kv, _query(g, W, x, proj, rms, rr, lay), rng)
    return x, proj, rms, rr, to_bf16(kv.reshape(-1), "rne")


def _query(g, W, x, proj, rms, rope_rms, lay):
    """The rotated query heads [heads, dh] of the layer."""
    D, dh = g["model_dim"], g["dh"]
    off, _, rows, cols = W["q"]
    xn = rms_norm(bf16_to_f32(x[:D]), bf16_to_f32(rms[:D]))
    qp = q4_matvec(xn, *parse_q4nx(proj, off, rows, cols)).reshape(
        g["num_attn_heads"], dh
    )
    cos = bf16_to_f32(rope_rms[lay["cos"] : lay["cos"] + dh // 2])
    sin = bf16_to_f32(rope_rms[lay["sin"] : lay["sin"] + dh // 2])
    return rope_head(
        qp, bf16_to_f32(rope_rms[lay["q_norm"] : lay["q_norm"] + dh]), cos, sin
    )


NEEDLE_SCORE = 8.0


def _plant_needles(g, context_len, kv, q, rng):
    """Write needle rows into kv [K|V, rows, dk].

    A needle K row scores NEEDLE_SCORE with every query head of its kv head; the
    other keys score near 0. Each needle has its own random V row. V rows of
    +-1 would cancel in the attention output and make it ill-conditioned.
    The needles sit at the oldest and the newest cached key, at row 0, at the
    row that a non-skip layer overwrites and at the first row past the keys. The softmax splits its weight among the
    needles that the layer reads. A layer that reads one row too many or too
    few, or a wrong row, changes its attention output by a large fraction.
    """
    order, valid = _attention_rows(g, context_len)
    # A non-skip layer writes its own key at the newest position.
    newest = order[valid - 1 - (not g["skip"])]
    rows = {order[0], newest, 0}
    if not g["skip"]:
        # The layer overwrites this row with its own key.
        rows.add(order[valid - 1])
    if valid < kv.shape[1] and context_len + 1 < kv.shape[1]:
        rows.add(context_len + 1)
    n_kv, dh = g["num_kv_heads"], g["dh"]
    group = g["num_attn_heads"] // n_kv
    for h in range(n_kv):
        qh = q[h * group : (h + 1) * group]
        u = (qh / np.linalg.norm(qh, axis=1, keepdims=True)).sum(0)
        u /= np.linalg.norm(u)
        k = u * NEEDLE_SCORE / np.min(qh @ u)
        for r in sorted(rows):
            kv[0, r, h * dh : (h + 1) * dh] = k
    for r in sorted(rows):
        kv[1, r] = rng.normal(0, 1, kv.shape[2])
