#!/usr/bin/env python3
"""Full-model W4A8 llama prefill on XDNA2 (part 30 follow-up).

NPU does the 7 heavy GEMMs per layer (attn q/k/v/o + ffn gate/up/down) as
asymmetric i8xi4 with INT4-packed weights (per-output-neuron scales) and
INT8 activations (per-tensor scale). Host does everything else (embedding,
rmsnorm, RoPE, attention scores/softmax/value, SiLU, residual, lm_head) in
bf16 — the small matmuls (scores: K=64, value: K=seq) don't justify NPU
dispatch overhead.

Validates against the bf16 CPU reference (llama_cpu.llama_forward_pass):
logits correlation, top-k, and greedy text.

Usage (iron-venv python):
  cd ~/amd-oss/iron
  PYTHONPATH=/usr/lib/python3/dist-packages \
    ~/amd-oss/iron-venv/bin/python llama_w4a8_npu.py "The capital of France is"
"""
import os
import sys
import math
import time

sys.path.insert(0, "/home/bcloud/amd-oss/iron")
sys.path.insert(0, "/home/bcloud/amd-oss/iron/iron/applications/llama_3.2_1b")

import numpy as np
import torch
import safetensors.torch as st

from iron.common.context import AIEContext
from iron.operators import GEMM
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

import llama_cpu
import llama_inference_harness as harness

WT = "/home/bcloud/llama3.2-1b/model.safetensors"
M_PAD = 256  # i8xi4 GEMM constraint: M % (tile_m*4) == 0
M_PAD_SEQ = 256  # padded sequence length (attention GEMM-free, host side)

CONFIG = dict(
    emb_dim=2048, hidden_dim=8192, n_heads=32, n_kv_groups=8,
    head_dim=64, n_layers=16, vocab_size=128256,
)


class NPU_W4A8_GEMM:
    """Compiled i8xi4 GEMM for one (K, N) shape. Each weight gets its own
    buffer set via bind(); the compiled op is shared (compile once per shape,
    buffers are per-weight — the B-binding overwrite bug made every op in a
    shape group use the last-bound weights)."""

    def __init__(self, K, N, build_dir="/tmp/w4a8-prefill", dtype_b="i4", groups=1):
        self.K, self.N, self.dtype_b = K, N, dtype_b
        self.groups = groups
        self.Kg = K // groups if (dtype_b == "i4" and groups > 1) else K
        assert N % 2 == 0 and N % 512 == 0 and self.Kg % 16 == 0
        ctx = AIEContext(build_dir=build_dir)
        self.op = (
            GEMM(M=M_PAD, K=self.Kg, N=N, tile_m=64, tile_k=64, tile_n=64,
                 num_aie_columns=8, dtype_in="i8", dtype_out="i32",
                 dtype_b=dtype_b, context=ctx)
            .compile()
            .get_callable()
        )

    def bind(self, B_ref, s_w):
        """Return a callable bound to this weight's own buffers."""
        if self.dtype_b == "i4" and self.groups > 1:
            return _BoundGroup(self, B_ref)
        return _Bound(self, B_ref, s_w)


class _Bound:
    def __init__(self, gemm, B_ref, s_w):
        self.gemm = gemm
        if gemm.dtype_b == "i4":
            q = np.rint(B_ref / s_w).clip(-8, 7).astype(np.int8)
            self.B = XRTTensor((gemm.K, gemm.N // 2), dtype=np.int8)
            self.B.numpy()[:] = GEMM.pack_i4(q)
        else:  # i8
            q = np.rint(B_ref / s_w).clip(-127, 127).astype(np.int8)
            self.B = XRTTensor((gemm.K, gemm.N), dtype=np.int8)
            self.B.numpy()[:] = q
        self.A = XRTTensor((M_PAD, gemm.K), dtype=np.int8)
        self.C = XRTTensor((M_PAD, gemm.N), dtype=np.int32)
        self.s_w = s_w.astype(np.float64)
        self._warmed = False

    def __call__(self, x, real_m):
        # overwrite() marks the write in the runtime coherence map. A raw
        # .numpy() write is unmediated, so run()'s to('npu') skips the upload
        # and the kernel computes on the STALE previous A — the root cause of
        # the stale C bug (ab47c82's double-call was a workaround; this is
        # the real fix, so a single call is correct).
        out = self._compute(x, real_m)
        return torch.from_numpy(out.astype(np.float32)).to(torch.bfloat16)

    def _compute(self, x, real_m):
        xf = x.float().numpy().reshape(M_PAD, -1)  # drop batch dim if present
        # Per-token (per-row) activation scale: each input row quantized with
        # its own s_x (Q8_0-style). Naive per-tensor scales lose too much over
        # 16 layers (corr ~0.55-0.75); per-row holds up much better.
        sx = np.max(np.abs(xf[:real_m]), axis=1, keepdims=True) / 127.0
        sx = np.maximum(sx, 1e-12)
        q8 = np.zeros_like(xf, dtype=np.int8)
        q8[:real_m] = np.rint(xf[:real_m] / sx).clip(-127, 127).astype(np.int8)
        with self.A.overwrite() as buf:
            buf[:] = q8
        res = self.gemm.op(self.A, self.B, self.C)
        _ = res.npu_time  # force the dispatch to complete before reading C
        c = self.C.to_torch().numpy().astype(np.float32)
        # float32 + real rows only: the full [M_PAD, N] float64 multiply was
        # ~10 ms/call (and xG for the group path); decode has real_m=1 so the
        # dequant is now a 256x cut. Return the full [M_PAD, N] buffer (rows
        # beyond real_m stay zero).
        out = np.zeros((M_PAD, self.gemm.N), dtype=np.float32)
        out[:real_m] = c[:real_m] * (sx.astype(np.float32) * self.s_w.astype(np.float32))[None, :]
        return out




class _BoundGroup:
    """Group-wise i4 weights (Q4_K-style): K split into `groups` chunks, each
    chunk gets its own per-column scales, run as per-group GEMMs, dequantized
    per group and summed. Finer weight quantization without touching the
    exact int8xint4 path."""

    def __init__(self, gemm, B_ref):
        self.gemm = gemm
        G, Kg = gemm.groups, gemm.Kg
        self.parts = []
        for g in range(G):
            Bg = B_ref[g * Kg:(g + 1) * Kg]
            s_wg = np.max(np.abs(Bg), axis=0) / 8.0
            s_wg = np.maximum(s_wg, 1e-8).astype(np.float64)
            # Asymmetric (zero-point) i4 when W4A8_ZP=1: recenter each group
            # at its midpoint so biased weights quantize tighter. The GEMM is
            # unchanged (signed int4); the zero-point correction is a host
            # post-term: out += (s_w*z) * rowsum(x over the group).
            zpg = None
            if os.environ.get("W4A8_ZP"):
                half = (np.max(Bg, axis=0) + np.min(Bg, axis=0)) / 2.0
                zpg = half / 8.0  # q = round((B - s_w*z)/s_w) ~ round(B/s_w) - z
            q4g = np.rint(Bg / s_wg - (zpg if zpg is not None else 0.0)).clip(-8, 7).astype(np.int8)
            B = XRTTensor((Kg, gemm.N // 2), dtype=np.int8)
            B.numpy()[:] = GEMM.pack_i4(q4g)
            # One A/C pair PER GROUP: the shared-buffer version read stale C
            # when the same op was called back-to-back with different B.
            A = XRTTensor((M_PAD, Kg), dtype=np.int8)
            C = XRTTensor((M_PAD, gemm.N), dtype=np.int32)
            self.parts.append((B, s_wg, zpg, A, C))
        self._warmed = False

    def __call__(self, x, real_m):
        out = self._compute(x, real_m)
        return torch.from_numpy(out.astype(np.float32)).to(torch.bfloat16)

    def _compute(self, x, real_m):
        xf = x.float().numpy().reshape(M_PAD, -1)
        Kg = self.gemm.Kg
        out = np.zeros((M_PAD, self.gemm.N), dtype=np.float32)
        for g, (B, s_wg, zpg, A, C) in enumerate(self.parts):
            xg = xf[:real_m, g * Kg:(g + 1) * Kg]
            # Per-group activation scale (per-token x per-K-group): finer than
            # one scale over the full row. W4A8_GROUP_ACTS=1 enables it.
            if os.environ.get("W4A8_GROUP_ACTS"):
                sxg = np.max(np.abs(xg), axis=1, keepdims=True) / 127.0
            else:
                sxg = np.max(np.abs(xf[:real_m]), axis=1, keepdims=True) / 127.0
            sxg = np.maximum(sxg, 1e-12)
            q8 = np.zeros((M_PAD, Kg), dtype=np.int8)
            q8[:real_m] = np.rint(xg / sxg).clip(-127, 127).astype(np.int8)
            with A.overwrite() as buf:
                buf[:] = q8
            res = self.gemm.op(A, B, C)
            _ = res.npu_time
            c = C.to_torch().numpy().astype(np.float32)[:real_m]
            sw = s_wg.astype(np.float32)[None, :]
            contrib = c * sxg.astype(np.float32) * sw
            if zpg is not None:
                # asymmetric correction: B ~ s_w*(q+z) -> out += s_w*z*rowsum(x)
                contrib += xg.astype(np.float32).sum(1, keepdims=True) * (sw * zpg[None, :].astype(np.float32))
            out[:real_m] += contrib
        return out

def quantize_weight(W, dtype="i4"):
    """W: torch [out, in] bf16 -> (B_ref [in, out] f32, s_w [out] f32)."""
    B_ref = W.float().t().numpy()
    peak = 8.0 if dtype == "i4" else 127.0
    s_w = np.max(np.abs(B_ref), axis=0) / peak
    s_w = np.maximum(s_w, 1e-8).astype(np.float32)
    return B_ref, s_w


def build_npu_layers(weights, build_dir):
    """Return per-layer dict of NPU W4A8 GEMMs (cache by K,N)."""
    pool = {}
    mix = int(__import__("os").environ.get("W4A8_MIX_LEN", "0"))  # first N layers i8 weights
    groups = int(__import__("os").environ.get("W4A8_GROUPS", "1"))  # i4 K-groups

    def get(K, N, dtype):
        key = (K, N, dtype, groups if dtype == "i4" else 1)
        if key not in pool:
            pool[key] = NPU_W4A8_GEMM(K, N, build_dir, dtype_b=dtype, groups=groups)
        return pool[key]

    layers = []
    for i in range(CONFIG["n_layers"]):
        L = {}
        for name, (Wkey, K, N) in {
            "q": (f"model.layers.{i}.self_attn.q_proj.weight", CONFIG["emb_dim"], CONFIG["emb_dim"]),
            "k": (f"model.layers.{i}.self_attn.k_proj.weight", CONFIG["emb_dim"], CONFIG["n_kv_groups"] * CONFIG["head_dim"]),
            "v": (f"model.layers.{i}.self_attn.v_proj.weight", CONFIG["emb_dim"], CONFIG["n_kv_groups"] * CONFIG["head_dim"]),
            "o": (f"model.layers.{i}.self_attn.o_proj.weight", CONFIG["emb_dim"], CONFIG["emb_dim"]),
            "gate": (f"model.layers.{i}.mlp.gate_proj.weight", CONFIG["emb_dim"], CONFIG["hidden_dim"]),
            "up": (f"model.layers.{i}.mlp.up_proj.weight", CONFIG["emb_dim"], CONFIG["hidden_dim"]),
            "down": (f"model.layers.{i}.mlp.down_proj.weight", CONFIG["hidden_dim"], CONFIG["emb_dim"]),
        }.items():
            ops_mix = __import__("os").environ.get("W4A8_OPS_MIX", "")
            attn_i8 = set(__import__("os").environ.get("W4A8_ATTN_I8", "").split(","))
            is_attn = name in ("q", "k", "v", "o")
            if ops_mix == "attn_i8":   # attention weights i8, FFN i4
                dt = "i8" if is_attn else "i4"
            elif ops_mix == "ffn_i8":  # FFN weights i8, attention i4
                dt = "i8" if not is_attn or name in attn_i8 else "i4"
            else:
                dt = "i8" if i < mix else "i4"
            B_ref, s_w = quantize_weight(weights[Wkey], dt)
            L[name] = get(K, N, dt).bind(B_ref, s_w)  # per-weight buffers
        layers.append(L)
    print(f"[w4a8] built {len(pool)} compiled NPU GEMM shapes ({len(layers)} layers)", flush=True)
    return layers


def forward_w4a8_npu(layers, weights, token_ids, rope_angles, build_dir):
    """token_ids: [1, seq] int64. Returns logits bf16 [1, seq, vocab] (padded seq)."""
    seq = token_ids.shape[1]
    assert seq <= M_PAD
    batch = 1
    emb = weights["model.embed_tokens.weight"]
    x = torch.nn.functional.embedding(token_ids, emb)  # [1, seq, emb]
    x = torch.nn.functional.pad(x, (0, 0, 0, M_PAD - seq))  # [1, M_PAD, emb]

    mask = torch.triu(torch.ones(M_PAD, M_PAD, dtype=torch.bool), diagonal=1)
    if seq < M_PAD:
        mask[:, seq:] = True
        mask[seq:, :] = True

    kv_caches = [None] * CONFIG["n_layers"]
    for i in range(CONFIG["n_layers"]):
        L = layers[i]
        x_norm = llama_cpu.rms_norm_forward(
            x, weights[f"model.layers.{i}.input_layernorm.weight"])
        # projections on NPU (W4A8)
        q = L["q"](x_norm, seq).view(batch, M_PAD, CONFIG["n_heads"], CONFIG["head_dim"])
        k = L["k"](x_norm, seq).view(batch, M_PAD, CONFIG["n_kv_groups"], CONFIG["head_dim"])
        v = L["v"](x_norm, seq).view(batch, M_PAD, CONFIG["n_kv_groups"], CONFIG["head_dim"])
        kv_caches[i] = {
            "k": k[0, :seq].transpose(0, 1),  # [G, seq, hd]
            "v": v[0, :seq].transpose(0, 1),
        }
        q = llama_cpu.rope_forward(q, rope_angles[:M_PAD])
        k = llama_cpu.rope_forward(k, rope_angles[:M_PAD])
        q = q.transpose(1, 2)  # [b, H, M, hd]
        k = k.transpose(1, 2)  # [b, G, M, hd]
        v = v.transpose(1, 2)
        gsz = CONFIG["n_heads"] // CONFIG["n_kv_groups"]
        k = k.repeat_interleave(gsz, dim=1)
        v = v.repeat_interleave(gsz, dim=1)
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(CONFIG["head_dim"])
        scores = scores.masked_fill(mask, float("-inf"))
        scores[:, :, seq:, :] = 0.0  # padded query rows: finite (uniform), zeroed below
        aw = torch.nn.functional.softmax(scores, dim=-1)
        aw[:, :, seq:, :] = 0.0  # padded query rows attend to nothing
        ctx_out = torch.matmul(aw, v).transpose(1, 2).contiguous().view(
            batch, M_PAD, -1)
        attn_out = L["o"](ctx_out, seq)  # NPU
        x = x + attn_out
        x_norm = llama_cpu.rms_norm_forward(
            x, weights[f"model.layers.{i}.post_attention_layernorm.weight"])
        gate = L["gate"](x_norm, seq)  # NPU
        up = L["up"](x_norm, seq)  # NPU
        hidden = torch.nn.functional.silu(gate) * up
        ffn_out = L["down"](hidden, seq)  # NPU
        x = x + ffn_out
        if i in (0, 1, 5):
            print(f"[w4a8] layer {i}: x[0,{seq-1},:4] = "
                  f"{x[0, seq-1, :4].float().tolist()}", flush=True)

    x = llama_cpu.rms_norm_forward(x, weights["model.norm.weight"])
    logits = torch.nn.functional.linear(x, emb)  # host, tied lm_head
    return logits, kv_caches




def decode_w4a8_npu(layers, weights, token, kv_caches, pos, rope_angles):
    """One decode step: token (int) at position pos. Returns (next_token, kvs)."""
    emb = weights["model.embed_tokens.weight"]
    x = torch.nn.functional.embedding(torch.tensor([[token]]), emb)  # [1, 1, emb]
    x = torch.nn.functional.pad(x, (0, 0, 0, M_PAD - 1))  # [1, M_PAD, emb]
    for i, L in enumerate(layers):
        xn = llama_cpu.rms_norm_forward(x, weights[f"model.layers.{i}.input_layernorm.weight"])
        q = L["q"](xn, 1)[:1].view(1, 1, CONFIG["n_heads"], CONFIG["head_dim"])
        k = L["k"](xn, 1)[:1].view(1, 1, CONFIG["n_kv_groups"], CONFIG["head_dim"])
        v = L["v"](xn, 1)[:1].view(1, 1, CONFIG["n_kv_groups"], CONFIG["head_dim"])
        q = llama_cpu.rope_forward(q, rope_angles[pos:pos + 1]).squeeze(0).squeeze(0)  # [H, hd]
        k = llama_cpu.rope_forward(k, rope_angles[pos:pos + 1]).squeeze(0).squeeze(0)  # [G, hd]
        kv_caches[i]["k"] = torch.cat([kv_caches[i]["k"], k.unsqueeze(1)], dim=1)  # [G, S, hd]
        kv_caches[i]["v"] = torch.cat([kv_caches[i]["v"], v.squeeze(0).squeeze(0).unsqueeze(1)], dim=1)
        gsz = CONFIG["n_heads"] // CONFIG["n_kv_groups"]
        K = kv_caches[i]["k"].repeat_interleave(gsz, dim=0)  # [H, S, hd]
        V = kv_caches[i]["v"].repeat_interleave(gsz, dim=0)
        scores = torch.matmul(q.unsqueeze(1), K.transpose(-2, -1)).squeeze(1) / math.sqrt(CONFIG["head_dim"])  # [H, S]
        aw = torch.nn.functional.softmax(scores, dim=-1)
        ctx = torch.matmul(aw.unsqueeze(1), V).squeeze(1).reshape(1, 1, -1)  # [1, 1, H*hd]
        ctx = torch.nn.functional.pad(ctx, (0, 0, 0, M_PAD - 1))
        x = x + L["o"](ctx, 1)
        xn = llama_cpu.rms_norm_forward(x, weights[f"model.layers.{i}.post_attention_layernorm.weight"])
        gate = L["gate"](xn, 1)
        up = L["up"](xn, 1)
        hidden = torch.nn.functional.silu(gate) * up
        x = x + L["down"](hidden, 1)
    xn = llama_cpu.rms_norm_forward(x, weights["model.norm.weight"])
    logits = torch.nn.functional.linear(xn[:1], emb).squeeze(0).squeeze(0)
    return int(logits.argmax()), kv_caches


def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else "The capital of France is"
    build_dir = sys.argv[2] if len(sys.argv) > 2 else "/tmp/w4a8-prefill"

    weights = st.load_file(WT)
    for k, v in weights.items():
        weights[k] = v.to(torch.bfloat16)

    tok_path = "/home/bcloud/llama3.2-1b/original/tokenizer.model"
    config, state = harness.init(WT, tok_path, prompt=prompt)
    token_ids = state.token_ids  # torch [1, seq]
    seq = token_ids.shape[1]
    rope_angles = harness.compute_rope_angles(
        CONFIG["head_dim"], M_PAD + 16, rope_base=500000.0)

    # bf16 CPU reference
    t0 = time.time()
    ref_logits, _ = llama_cpu.llama_forward_pass(config, state)
    t_ref = time.time() - t0

    # W4A8 NPU
    layers = build_npu_layers(weights, build_dir)
    t0 = time.time()
    logits, kv_caches = forward_w4a8_npu(layers, weights, token_ids, rope_angles, build_dir)
    t_npu = time.time() - t0

    # compare at the last REAL token
    ref_last = ref_logits[0, seq - 1].float()
    npu_last = logits[0, seq - 1].float()
    corr = float(torch.corrcoef(torch.stack([ref_last, npu_last]))[0, 1])
    diff = (npu_last - ref_last).abs()
    print(f"\nprompt: '{prompt}' ({seq} tokens, padded {M_PAD})")
    print(f"bf16 ref : {t_ref:.2f}s cpu | W4A8 NPU: {t_npu:.2f}s (GEMM-heavy path)")
    print(f"logits corr : {corr:.6f}")
    print(f"max |dlogit| : {diff.max():.4f}")
    print(f"top1 : ref {ref_last.argmax().item():>6}  npu {npu_last.argmax().item():>6}  "
          f"{'OK' if ref_last.argmax()==npu_last.argmax() else 'MISMATCH'}")
    rk, nk = torch.topk(ref_last, 5).indices.tolist(), torch.topk(npu_last, 5).indices.tolist()
    print(f"top5 ref: {rk}")
    print(f"top5 npu: {nk}")
    print(f"overlap  : {len(set(rk) & set(nk))}/5")

    # W4A8 decode (KV-cached, NPU i4 GEMMs, real_m=1)
    print("\nW4A8 decode (KV-cached):")
    pos = seq
    nxt = int(logits[0, seq - 1].argmax())
    out_ids = []
    for _ in range(24):
        if nxt == 2:
            break
        out_ids.append(nxt)
        nxt, kv_caches = decode_w4a8_npu(layers, weights, nxt, kv_caches, pos, rope_angles)
        pos += 1
    print(f"token ids: {out_ids}")
    print(f"text: {config.tokenizer.decode(out_ids)}")

if __name__ == "__main__":
    main()
