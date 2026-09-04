#!/usr/bin/env python3
"""W4A8 layer validation on real llama weights (task: thread i4 weights into
the IRON llama pipeline).

Quantizes a real llama-3.2-1B q_proj to INT4 (packed, per-output-neuron
scales), quantizes activations to INT8 (per-tensor scale), runs the NPU
i8xi4 GEMM (bit-exact int8 x int4), dequantizes with the two scales, and
compares against the bf16 reference.

Usage (iron-venv python — has torch/safetensors + ml_dtypes + mlir_aie):
  cd ~/amd-oss/iron
  PYTHONPATH=/usr/lib/python3/dist-packages \
    ~/amd-oss/iron-venv/bin/python llama_w4a8_validate.py [M] [layer]
"""
import sys
import numpy as np

sys.path.insert(0, "/home/bcloud/amd-oss/iron")

import safetensors.torch as st
import torch
from iron.common.context import AIEContext
from iron.operators import GEMM
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

M = int(sys.argv[1]) if len(sys.argv) > 1 else 256
LAYER = sys.argv[2] if len(sys.argv) > 2 else "0"
WT = f"/home/bcloud/llama3.2-1b/model.safetensors"
KEY = f"model.layers.{LAYER}.mlp.gate_proj.weight"

print(f"== W4A8 llama q_proj layer {LAYER}  (M={M}) ==")
w = st.load_file(WT)[KEY].to(torch.float32).numpy()  # [out, in]
OUT, INN = w.shape
B_ref = w.T  # [K=in, N=out] — the GEMM's B operand
rng = np.random.default_rng(7)
x = rng.normal(size=(M, INN)).astype(np.float32)  # activations ~ N(0,1)
ref = (x.astype(np.float64) @ B_ref.astype(np.float64))

# ---- W4A8 quantization ----
# weights: per-output-neuron (per B column) scale, int4 range [-8, 7]
s_w = np.max(np.abs(B_ref), axis=0) / 8.0
s_w = np.maximum(s_w, 1e-8)
q4 = np.rint(B_ref / s_w).clip(-8, 7).astype(np.int8)
# activations: per-tensor scale, int8 range [-127, 127]
s_x = np.max(np.abs(x)) / 127.0
q8 = np.rint(x / s_x).clip(-127, 127).astype(np.int8)

# exact int reference (what the NPU must reproduce)
exact_i = q8.astype(np.int32) @ q4.astype(np.int32)  # [M, N]
deq_exact = exact_i.astype(np.float64) * (s_x * s_w)[None, :]

# ---- NPU i8xi4 GEMM ----
K, N = INN, OUT
assert N % 2 == 0 and N % 32 == 0 and K % 16 == 0 and M % 8 == 0, "shape constraints"
ctx = AIEContext(build_dir="/tmp/w4a8-build")
op = (
    GEMM(M=M, K=K, N=N, tile_m=64, tile_k=64, tile_n=64,
         num_aie_columns=8, dtype_in="i8", dtype_out="i32",
         dtype_b="i4", context=ctx)
    .compile()
    .get_callable()
)
A = XRTTensor((M, K), dtype=np.int8)
B = XRTTensor((K, N // 2), dtype=np.int8)
C = XRTTensor((M, N), dtype=np.int32)
A.numpy()[:] = q8
B.numpy()[:] = GEMM.pack_i4(q4)
op(A, B, C)
C_npu = C.to_torch().numpy()

# ---- metrics ----
exact_ok = np.array_equal(C_npu, exact_i)
deq = C_npu.astype(np.float64) * (s_x * s_w)[None, :]
corr = float(np.corrcoef(deq.ravel(), ref.ravel())[0, 1])
mae = float(np.mean(np.abs(deq - ref)))
mre = float(np.mean(np.abs(deq - ref) / (np.abs(ref) + 1e-6)))
top5 = np.argsort(deq[0])[::-1][:5]
ref5 = np.argsort(ref[0])[::-1][:5]

print(f"exact i8xi4 on NPU == CPU int ref: {exact_ok}")
print(f"corr vs bf16 ref : {corr:.6f}")
print(f"MAE / MRE        : {mae:.4f} / {mre:.5f}")
print(f"top-5 (deq)      : {top5.tolist()}")
print(f"top-5 (ref)      : {ref5.tolist()}")
print(f"W scale range    : {s_w.min():.3e} .. {s_w.max():.3e}")
print(f"quant err (W)    : {np.mean(np.abs(B_ref - q4 * s_w)):.4f} "
      f"(rel {np.mean(np.abs(B_ref - q4*s_w)/(np.abs(B_ref)+1e-6)):.4f})")
