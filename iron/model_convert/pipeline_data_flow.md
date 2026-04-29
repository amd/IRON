================================================================================
  IRON NPU - MODEL CONVERSION & INFERENCE PIPELINE
  Production-Grade Data Flow Diagram
  Target Model: Llama-3.2-1B | AMD Ryzen AI NPU | dtype: bfloat16
================================================================================

================================================================================
  SECTION 1: HIGH-LEVEL ARCHITECTURE OVERVIEW
================================================================================

  +=========================================================================+
  |                         IRON NPU PIPELINE                                |
  +=========================================================================+
  |                                                                          |
  |   OFFLINE (Once)                           RUNTIME (Per Request)        |
  |   +---------------------------+            +--------------------------+  |
  |   |    CONVERSION PHASE       |            |     INFERENCE PHASE      |  |
  |   |                           |            |                          |  |
  |   |  HF Safetensors ---->     |            |  Prompt -> Tokenize      |  |
  |   |  .npy + JSON Manifest     |            |           -> Prefill     |  |
  |   |  ~2.4GB weight files*     |            |           -> Decode Loop |  |
  |   |                           |            |           -> Sample      |  |
  |   +---------------------------+            +--------------------------+  |
  |              |                                     |                      |
  |              v                                     v                      |
  |   +---------------------------+            +--------------------------+  |
  |   |  Weight Files (.npy)      | ---------> |  NPU Runtime (AIE)       |  |
  |   |  - layer_0.q_proj.npy     |            |  - 8 AIE Columns         |  |
  |   |  - layer_0.k_proj.npy     |            |  - Tile: 64x64x64        |  |
  |   |  - ... 240 operator files |            |  - KV Cache in RAM       |  |
  |   |  - manifest.json          |            |                          |  |
  |   +---------------------------+            +--------------------------+  |
  |                                                                          |
  +=========================================================================+

  MODEL SPEC (Llama-3.2-1B):
  +----------------------+------------+--------------------------------------+
  | Parameter            | Value      | Notes                                |
  +----------------------+------------+--------------------------------------+
  | hidden_size          | 2048       | Embedding / attention dimension      |
  | intermediate_size    | 8192       | MLP hidden dimension (4x hidden)     |
  | vocab_size           | 128256     | Tokenizer vocabulary                 |
  | num_hidden_layers    | 16         | Transformer blocks                   |
  | num_attention_heads  | 32         | Query heads                          |
  | num_kv_heads         | 8          | Key/Value heads (GQA)               |
  | head_dim             | 64         | Per-head dimension                   |
  | GQA groups           | 4          | 32/8 = 4 KV head repetitions        |
  | max_position_embeddings | 131072  | Maximum context length               |
  | rope_theta           | 500000     | RoPE frequency base (Llama 3.x)        |
  | dtype                | bfloat16   | 2 bytes per element                  |
  | num_aie_columns      | 8          | NPU parallel execution units         |
  | tile_size            | M=64,K=64,N=64 | AIE matrix multiply tile       |
  +----------------------+------------+--------------------------------------+


================================================================================
  SECTION 2: CONVERSION PIPELINE (9 Phases)
================================================================================

  INPUT: HuggingFace Model Directory
  +----------------------------------------------------------------+
  |  hf_model_dir/                                                 |
  |  +-- config.json                    [Architecture spec]        |
  |  +-- model-00001-of-00003.safetensors   [Weight shard 1]       |
  |  +-- model-00002-of-00003.safetensors   [Weight shard 2]       |
  |  +-- model-00003-of-00003.safetensors   [Weight shard 3]       |
  |  +-- tokenizer.json                   [Tokenizer spec]         |
  |  +-- tokenizer_config.json            [Tokenizer config]       |
  +----------------------------------------------------------------+
          |
          v
  +==========================================================================+
  | PHASE 1: INPUT RESOLUTION                                                |
  +==========================================================================+
  |  - Locate or download model from HF Hub                                  |
  |  - Verify safetensors integrity (checksums)                              |
  |  - Count shards, compute total weight size estimate                      |
  |  - Output: model_path, shard_list, total_files                           |
  +==========================================================================+
          |
          v
  +==========================================================================+
  | PHASE 2: ARCHITECTURE PARSE                                              |
  +==========================================================================+
  |  INPUT: config.json                                                      |
  |  EXTRACT:                                                                |
  |    hidden_size = 2048                                                    |
  |    intermediate_size = 8192                                              |
  |    vocab_size = 128256                                                   |
  |    num_hidden_layers = 16                                                |
  |    num_attention_heads = 32                                              |
  |    num_kv_heads = 8                                                      |
  |    head_dim = 64                                                         |
  |    max_position_embeddings = 131072                                      |
  |    rope_theta = 500000                                                   |
  |    dtype = bfloat16                                                      |
  |  COMPUTED:                                                               |
  |    GQA_groups = 32/8 = 4                                                 |
  |    hidden_per_head = 2048/32 = 64 = head_dim [CHECK: OK]                 |
  +==========================================================================+
          |
          v
  +==========================================================================+
  | PHASE 3: COMPATIBILITY CHECK                                             |
  +==========================================================================+
  |  VALIDATIONS:                                                            |
  |  [PASS] hidden_size % num_attention_heads == 0   (2048 % 32 = 0)        |
  |  [PASS] head_dim == hidden_size / num_heads      (64 == 2048/32)        |
  |  [PASS] num_kv_heads divides num_attn_heads      (8 divides 32)         |
  |  [PASS] intermediate_size aligned to tile_K      (8192 % 64 = 0)        |
  |  [PASS] hidden_size aligned to tile_M            (2048 % 64 = 0)        |
  |  [PASS] dtype supported (bfloat16)                                       |
  |  [INFO] GQA ratio = 4 (moderate KV cache savings)                       |
  |  [PASS] Max tokens within NPU memory budget                              |
  +==========================================================================+
          |
          v
  +==========================================================================+
  | PHASE 4: NPU CONFIGURATION                                               |
  +==========================================================================+
  |  AIE HARDWARE CONFIG:                                                    |
  |    num_aie_columns = 8                                                   |
  |    tile_M = 64, tile_K = 64, tile_N = 64                                 |
  |    dtype = bfloat16 (2 bytes)                                            |
  |  PADDED MINIMUM SHAPES:                                                   |
  |    min_M = 256   (activation batch dimension padding)                    |
  |    min_K = 64    (input feature dimension)                               |
  |    min_N = 512   (output feature dimension, e.g. K_proj=512)            |
  |  GEMM TILING STRATEGY:                                                    |
  |    Large GEMMs (2048x2048) -> 32x32 tiles = 1024 tiles                  |
  |    With 8 AIE columns -> 128 execution steps per large GEMM             |
  |    Small GEMMs (2048x512)  -> 32x8 tiles = 256 tiles                    |
  |    With 8 AIE columns -> 32 execution steps per small GEMM              |
  +==========================================================================+
          |
          v
  +==========================================================================+
  | PHASE 5: WEIGHT LOADING                                                  |
  +==========================================================================+
  |  LOAD: safetensors -> numpy arrays (bf16)                                |
  |  EXAMPLE WEIGHTS LOADED:                                                  |
  |    model.embed_tokens.weight          -> [128256, 2048]  (525MB)        |
  |    model.norm.weight                    -> [2048]         (4KB)         |
  |    lm_head.weight                       -> [128256, 2048] (525MB)        |
  |  Per Layer 0 (16 layers total):                                          |
  |    model.layers.0.input_layernorm.weight  -> [2048]       (4KB)         |
  |    model.layers.0.self_attn.q_proj.weight -> [2048, 2048] (8MB)         |
  |    model.layers.0.self_attn.k_proj.weight -> [512, 2048]  (2MB)         |
  |    model.layers.0.self_attn.v_proj.weight -> [512, 2048]  (2MB)         |
  |    model.layers.0.self_attn.o_proj.weight -> [2048, 2048] (8MB)         |
  |    model.layers.0.post_attention_layernorm.weight -> [2048] (4KB)       |
  |    model.layers.0.mlp.gate_proj.weight    -> [8192, 2048] (32MB)        |
  |    model.layers.0.mlp.up_proj.weight      -> [8192, 2048] (32MB)        |
  |    model.layers.0.mlp.down_proj.weight    -> [2048, 8192] (32MB)        |
  |  Per-layer total: ~116MB | 16 layers: ~1.86GB                           |
  +==========================================================================+
          |
          v
  +==========================================================================+
  | PHASE 6: WEIGHT MAPPING & TRANSFORMS                                     |
  +==========================================================================+
  |  MAP: HuggingFace names -> IRON names + apply transforms                |
  |  +-------------------------------------+----------------+---------------+ |
  |  | HF Name                             | IRON Name      | Transform     | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.embed_tokens.weight           | embedding      | NONE          | |
  |  |   [128256, 2048]                    | [128256, 2048] |               | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.self_attn.q_proj.w   | layer_0.q_proj | TRANSPOSE     | |
  |  |   [2048, 2048]                      | [2048, 2048]   | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.self_attn.k_proj.w   | layer_0.k_proj | TRANSPOSE     | |
  |  |   [512, 2048]                       | [2048, 512]    | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.self_attn.v_proj.w   | layer_0.v_proj | TRANSPOSE     | |
  |  |   [512, 2048]                       | [2048, 512]    | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.self_attn.o_proj.w   | layer_0.o_proj | TRANSPOSE     | |
  |  |   [2048, 2048]                      | [2048, 2048]   | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.mlp.gate_proj.w      | layer_0.g_proj | TRANSPOSE     | |
  |  |   [8192, 2048]                      | [2048, 8192]   | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.mlp.up_proj.w        | layer_0.u_proj | TRANSPOSE     | |
  |  |   [8192, 2048]                      | [2048, 8192]   | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.mlp.down_proj.w      | layer_0.d_proj | TRANSPOSE     | |
  |  |   [2048, 8192]                      | [8192, 2048]   | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  | model.layers.0.input_layernorm.w    | layer_0.rms_1  | NONE          | |
  |  | model.layers.0.post_attn_ln.w       | layer_0.rms_2  | NONE          | |
  |  | model.norm.weight                   | final_norm     | NONE          | |
  |  | lm_head.weight                      | lm_head        | TRANSPOSE     | |
  |  |   [128256, 2048]                    | [2048, 128256] | for GEMM(T)   | |
  |  +-------------------------------------+----------------+---------------+ |
  |  Total mapped weights: 9 per layer * 16 + 3 global = 147 weight files   |
  +==========================================================================+
          |
          v
  +==========================================================================+
  |  PHASE 7: IRON SHAPE ANALYSIS                                              |
  +==========================================================================+
  |  COMPUTE padded shapes for AIE tile alignment:                           |
  |  +------------------+------------+----------+----------+-----------------+ |
  |  | Weight           | HF Shape   | IRON M   | IRON K   | IRON N          | |
  |  +------------------+------------+----------+----------+-----------------+ |
  |  | q_proj           | 2048x2048| 2048     | 2048     | 2048            | |
  |  | k_proj           | 2048x512 | 2048     | 2048     | 512             | |
  |  | v_proj           | 2048x512 | 2048     | 2048     | 512             | |
  |  | o_proj           | 2048x2048| 2048     | 2048     | 2048            | |
  |  | gate_proj        | 2048x8192| 2048     | 2048     | 8192            | |
  |  | up_proj          | 2048x8192| 2048     | 2048     | 8192            | |
  |  | down_proj        | 8192x2048| 8192     | 8192     | 2048            | |
  |  | lm_head          | 2048x128K| 2048     | 2048     | 128256          | |
  |  +------------------+----------+----------+----------+-----------------+ |
  |  All shapes already aligned to tile boundaries (64). No zero-padding    |
  |  required for Llama-3.2-1B.                                             |
  +==========================================================================+
          |
          v
  +==========================================================================+
  | PHASE 8: MODEL ASSEMBLY                                                  |
  +==========================================================================+
  |  OPERATOR COUNT:                                                         |
  |    Per layer: 15 operators (2 RMSNorm + 4 GEMM attn + 1 RoPE +          |
  |              1 Attention + 3 GEMM mlp + 2 activation + 2 residual)      |
  |    16 layers * 15 = 240 operators                                        |
  |    + 3 global: embedding lookup + final norm + lm_head = 243 total      |
  |  MEMORY ESTIMATION:                                                      |
  |    Weights:     2.4GB (embedding 525MB + 16*116MB + lm_head 525MB)      |
  |    KV Cache:    128MB (at seq_len=4096) to 4GB (at max 131072)         |
  |    Activations: ~50MB (at T=100, per layer ~3.3MB)                      |
  |    TOTAL NPU RAM: ~2.6GB (typical) to ~6.5GB (max context)             |
  +==========================================================================+
          |
          v
  +==========================================================================+
  | PHASE 9: EXPORT                                                          |
  +==========================================================================+
  |  OUTPUT: iron_model/                                                     |
  |  +-- manifest.json                  [Metadata, shapes, operator list]    |
  |  +-- embedding.npy                  [128256, 2048] bf16   (525MB)        |
  |  +-- lm_head.npy                    [2048, 128256] bf16   (525MB)        |
  |  +-- final_norm.npy                 [2048] bf16         (4KB)            |
  |  +-- layer_0/                                                         |
  |  |   +-- q_proj.npy                 [2048, 2048] bf16   (8MB)            |
  |  |   +-- k_proj.npy                 [2048, 512]  bf16   (2MB)            |
  |  |   +-- v_proj.npy                 [2048, 512]  bf16   (2MB)            |
  |  |   +-- o_proj.npy                 [2048, 2048] bf16   (8MB)            |
  |  |   +-- g_proj.npy                 [2048, 8192] bf16   (32MB)           |
  |  |   +-- u_proj.npy                 [2048, 8192] bf16   (32MB)           |
  |  |   +-- d_proj.npy                 [8192, 2048] bf16   (32MB)           |
  |  |   +-- rms_1.npy                  [2048] bf16       (4KB)              |
  |  |   +-- rms_2.npy                  [2048] bf16       (4KB)              |
  |  +-- layer_1/                                                         |
  |  |   +-- ... (same structure)                                             |
  |  +-- ...                                                                  |
  |  +-- layer_15/                                                        |
  |      +-- ... (same structure)                                             |
  |                                                                           |
  |  Total files: 1 manifest + 3 global + 16*9 layer = 148 files            |
  |  Total size: ~2.4GB                                                       |
  +==========================================================================+


================================================================================
  SECTION 3: MEMORY LAYOUT
================================================================================

  +==========================================================================+
  | WEIGHT MEMORY BREAKDOWN                                                  |
  +==========================================================================+
  |  Component          | Shape            | Elements     | Bytes   | %Total  |
  |  +------------------+------------------+-------------+---------+---------+ |
  |  embedding          | [128256, 2048]   | 262,668,288 | 525MB   |  21.8%  | |
  |  lm_head            | [2048, 128256]   | 262,668,288 | 525MB   |  21.8%  | |
  |  Per Layer (x16):   |                  |             |         |         | |
  |    q_proj           | [2048, 2048]     | 4,194,304   | 8MB     |   0.3%  | |
  |    k_proj           | [2048, 512]      | 1,048,576   | 2MB     |   0.08% | |
  |    v_proj           | [2048, 512]      | 1,048,576   | 2MB     |   0.08% | |
  |    o_proj           | [2048, 2048]     | 4,194,304   | 8MB     |   0.3%  | |
  |    gate_proj        | [2048, 8192]     | 16,777,216  | 32MB    |   1.3%  | |
  |    up_proj          | [2048, 8192]     | 16,777,216  | 32MB    |   1.3%  | |
  |    down_proj        | [8192, 2048]     | 16,777,216  | 32MB    |   1.3%  | |
  |    rms_norm (x2)    | [2048] * 2       | 4,096       | 8KB     |   ~0%   | |
  |    --- Layer Subtotal ---             |             | 116MB   |   4.8%  | |
  |  16 Layers Total    |                  |             | 1.86GB  |  77.3%  | |
  |  global norms       | [2048]           | 2,048       | 4KB     |   ~0%   | |
  |  +------------------+------------------+-------------+---------+---------+ |
  |  TOTAL WEIGHTS                        | ~1.3B params*| ~2.9GB  | 100%    | |
  +==========================================================================+
  * If lm_head weights are tied to embedding (common in Llama): ~1.07B params, ~2.4GB
  +==========================================================================+

  +==========================================================================+
  | KV CACHE MEMORY (grows during decode, bf16 = 2 bytes)                    |
  +==========================================================================+
  |  Per layer, per token: 2 * num_kv_heads * head_dim * 2 = 2*8*64*2 = 2KB |
  |  Per layer: 2048 * seq_len bytes                                         |
  |  16 layers: 32768 * seq_len bytes = 32KB * seq_len                       |
  |  +-------------+--------------+--------------+--------------+-----------+ |
  |  | seq_len     | Per Layer    | 16 Layers    | + Weights    | Total     | |
  |  +-------------+--------------+--------------+--------------+-----------+ |
  |  | 128         | 256KB        | 4MB          | 2.4GB        | 2.40GB    | |
  |  | 512         | 1MB          | 16MB         | 2.4GB        | 2.42GB    | |
  |  | 1024        | 2MB          | 32MB         | 2.4GB        | 2.43GB    | |
  |  | 2048        | 4MB          | 64MB         | 2.4GB        | 2.46GB    | |
  |  | 4096        | 8MB          | 128MB        | 2.4GB        | 2.53GB    | |
  |  | 8192        | 16MB         | 256MB        | 2.4GB        | 2.66GB    | |
  |  | 16384       | 32MB         | 512MB        | 2.4GB        | 2.91GB    | |
  |  | 32768       | 64MB         | 1GB          | 2.4GB        | 3.4GB     | |
  |  | 65536       | 128MB        | 2GB          | 2.4GB        | 4.4GB     | |
  |  | 131072      | 256MB        | 4GB          | 2.4GB        | 6.4GB     | |
  |  +-------------+--------------+--------------+--------------+-----------+ |
  |  Note: KV cache stored in SYSTEM RAM, DMA'd to NPU per decode step      |
  +==========================================================================+

  +==========================================================================+
  | ACTIVATION MEMORY (per layer during forward pass, batch=1)               |
  +==========================================================================+
  |  Buffer               | Shape (Prefill T=100)   | Size (bf16)            |
  |  +--------------------+-------------------------+-----------------------+ |
  |  hidden input         | [1, 100, 2048]          | 400KB                  | |
  |  Q projected         | [1, 32, 100, 64]        | 400KB                  | |
  |  K projected         | [1, 8, 100, 64]         | 100KB                  | |
  |  V projected         | [1, 8, 100, 64]         | 100KB                  | |
  |  attention scores     | [1, 32, 100, S]         | 40KB * S              | |
  |    (S = context len)  | S=100 -> 400KB           |                        | |
  |  attention output     | [1, 32, 100, 64]        | 400KB                  | |
  |  attention flattened  | [1, 100, 2048]          | 400KB                  | |
  |  gate_proj output     | [1, 100, 8192]          | 1.6MB                  | |
  |  up_proj output       | [1, 100, 8192]          | 1.6MB                  | |
  |  siLU(gate)           | [1, 100, 8192]          | 1.6MB                  | |
  |  elementwise mul      | [1, 100, 8192]          | 1.6MB                  | |
  |  mlp output           | [1, 100, 2048]          | 400KB                  | |
  |  +--------------------+-------------------------+-----------------------+ |
  |  Per-layer activations (T=100, S=100): ~8.8MB                            |
  |  16 layers: ~140MB (can be freed layer-by-layer in streaming mode)       |
  +==========================================================================+


================================================================================
  SECTION 4: INFERENCE PIPELINE - COMPLETE DATA FLOW
================================================================================

  +==========================================================================+
  | PROMPT FLOW: User Input -> Generated Text                                |
  +==========================================================================+
  |                                                                          |
  |  USER: "What is machine learning?"                                       |
  |    |                                                                     |
  |    v                                                                     |
  |  TOKENIZER (128256 vocab)                                                |
  |    Input: "What is machine learning?"                                    |
  |    Output: token_ids = [151644, 791, 338, 37219, 2629, 1615, 13, 151645]|
  |    Shape: [1, 8] tokens (8 prompt tokens + special tokens)               |
  |    |                                                                     |
  |    v                                                                     |
  |  EMBEDDING LAYER                                                         |
  |    Input:  token_ids [1, 8]                                              |
  |    Weight: embedding [128256, 2048]                                      |
  |    Lookup: gather rows -> [1, 8, 2048]                                   |
  |    Size: 8 * 2048 * 2 = 32KB                                             |
  |    |                                                                     |
  |    v                                                                     |
  +==========================================================================+
  |  TRANSFORMER BLOCK (16 layers, each processes full sequence)            |
  +==========================================================================+
  |  LAYER 0:                                                                |
  |    Input: hidden [1, 8, 2048]                                            |
  |    |                                                                     |
  |    +---> RMSNorm(hidden) -> [1, 8, 2048]                                 |
  |    |                                                                     |
  |    +---> Q_proj: GEMM([1,8,2048] @ [2048,2048]^T) -> [1,8,2048]         |
  |    |       Reshape -> [1,32,8,64] (32 heads, 8 tokens, 64 dim)          |
  |    |       RoPE -> [1,32,8,64] (rotary position encoding)               |
  |    |                                                                     |
  |    +---> K_proj: GEMM([1,8,2048] @ [2048,512]^T) -> [1,8,512]           |
  |    |       Reshape -> [1,8,8,64] (8 kv_heads, 8 tokens, 64 dim)         |
  |    |       RoPE -> [1,8,8,64]                                           |
  |    |       KV CACHE UPDATE: append K[1,8,8,64] -> cache has [1,8,8,64]  |
  |    |                                                                     |
  |    +---> V_proj: GEMM([1,8,2048] @ [2048,512]^T) -> [1,8,512]           |
  |    |       Reshape -> [1,8,8,64]                                        |
  |    |       KV CACHE UPDATE: append V[1,8,8,64] -> cache has [1,8,8,64]  |
  |    |                                                                     |
  |    +---> ATTENTION(Q, K_cache, V_cache):                                 |
  |    |       GQA: repeat K,V from 8->32 heads (groups=4)                   |
  |    |         K_expanded: [1,8,8,64] -> [1,32,8,64]                       |
  |    |         V_expanded: [1,8,8,64] -> [1,32,8,64]                       |
  |    |       QK^T: [1,32,8,64] @ [1,32,64,8] -> scores [1,32,8,8]         |
  |    |       Scale: scores / 8 (sqrt(64))                                  |
  |    |       Softmax: [1,32,8,8]                                           |
  |    |       Attend: softmax @ V[1,32,8,64] -> [1,32,8,64]                |
  |    |       Reshape+transpose -> [1,8,2048]                               |
  |    |                                                                     |
  |    +---> O_proj: GEMM([1,8,2048] @ [2048,2048]^T) -> [1,8,2048]         |
  |    |                                                                     |
  |    +---> Residual Add: attn_out + hidden -> [1,8,2048]                   |
  |    |                                                                     |
  |    +---> RMSNorm(residual) -> [1,8,2048]                                 |
  |    |                                                                     |
  |    +---> Gate_proj: GEMM([1,8,2048] @ [2048,8192]^T) -> [1,8,8192]      |
  |    |                                                                     |
  |    +---> Up_proj:   GEMM([1,8,2048] @ [2048,8192]^T) -> [1,8,8192]      |
  |    |                                                                     |
  |    +---> SiLU(gate) -> [1,8,8192]                                        |
  |    |                                                                     |
  |    +---> Mul: siLU(gate) * up_proj -> [1,8,8192]                         |
  |    |                                                                     |
  |    +---> Down_proj: GEMM([1,8,8192] @ [8192,2048]^T) -> [1,8,2048]      |
  |    |                                                                     |
  |    +---> Residual Add: mlp_out + hidden -> [1,8,2048] (LAYER 0 OUTPUT)   |
  |                                                                          |
  |    v                                                                     |
  |  LAYER 1...LAYER 15 (same structure, sequential)                         |
  |    Input: hidden from previous layer [1, 8, 2048]                        |
  |    Output: hidden [1, 8, 2048]                                           |
  |    KV Cache grows: each layer adds K[1,8,8,64], V[1,8,8,64]             |
  |    After 16 layers: KV cache = 16 * 2 * 8 * 8 * 64 * 2 = 256KB          |
  |                                                                          |
  |    v                                                                     |
  +==========================================================================+
  |  FINAL NORM + LM HEAD                                                    |
  +==========================================================================+
  |  FINAL NORM: RMSNorm(hidden[1,8,2048]) -> [1,8,2048]                     |
  |    |                                                                     |
  |    v                                                                     |
  |  LM HEAD: GEMM([1,8,2048] @ [2048,128256]^T) -> logits [1,8,128256]      |
  |    Size: 8 * 128256 * 2 = 2MB                                            |
  |    |                                                                     |
  |    v                                                                     |
  |  SAMPLING:                                                               |
  |    Only last token matters: logits[:, -1, :] -> [1, 128256]              |
  |    Temperature + Top-p + Top-k -> probability distribution               |
  |    Sample -> next_token_id (e.g., 4521 = "Machine")                      |
  |    |                                                                     |
  |    v                                                                     |
  |  APPEND: prompt_tokens + [next_token_id] -> new sequence [1, 9]          |
  |    |                                                                     |
  +==========================================================================+
  |  DECODE LOOP (repeat until EOS or max_tokens)                           |
  +==========================================================================+
  |  next_token_id = 4521                                                    |
  |    |                                                                     |
  |    v                                                                     |
  |  EMBEDDING: lookup 4521 -> [1, 1, 2048]  (single token embedding)        |
  |    |                                                                     |
  |    v                                                                     |
  |  16 LAYERS (DECODE MODE - T=1):                                         |
  |    Input: hidden [1, 1, 2048]                                            |
  |    Per layer:                                                            |
  |      Q_proj: [1,1,2048] -> Q[1,32,1,64] + RoPE                         |
  |      K_proj: [1,1,2048] -> K[1,8,1,64] + RoPE -> APPEND to KV cache     |
  |      V_proj: [1,1,2048] -> V[1,8,1,64] -> APPEND to KV cache            |
  |      Attention: Q[1,32,1,64] @ K_cache[1,32,S,64]^T -> [1,32,1,S]       |
  |        (S = growing context: 9, 10, 11, ...)                            |
  |        Softmax -> Attend -> [1,32,1,64] -> [1,1,2048]                   |
  |      MLP: [1,1,2048] -> gate[1,1,8192] * up[1,1,8192] -> down -> [1,1,2048]|
  |    Output: hidden [1, 1, 2048]                                           |
  |    KV Cache at step 5: 16 * 2 * 8 * 13 * 64 * 2 = 416KB                 |
  |    |                                                                     |
  |    v                                                                     |
  |  LM HEAD: [1,1,2048] @ [2048,128256]^T -> logits [1,1,128256]           |
  |  SAMPLE -> next_token_id (e.g., 1917 = "learning")                      |
  |  APPEND -> sequence [1, 10]                                              |
  |  |                                                                       |
  |  +---> Repeat DECODE loop until EOS token (151645) or max_tokens         |
  |                                                                          |
  |  Final output: "What is machine learning? Machine learning is..."        |
  |  Detokenize -> display to user                                           |
  +==========================================================================+


================================================================================
  SECTION 5: PREFILL vs DECODE COMPARISON
================================================================================

  +==========================================================================+
  |  METRIC              | PREFILL              | DECODE                     |
  +==========================================================================+
  |  Sequence length (T) | T = prompt_len (e.g. 100) | T = 1               |
  |  Context (S)         | S = T = 100          | S = prompt_len + gen_steps|
  |  Input hidden        | [1, 100, 2048]       | [1, 1, 2048]               |
  |  Q_proj output       | [1, 100, 2048]       | [1, 1, 2048]               |
  |  K_proj output       | [1, 100, 512]        | [1, 1, 512]                |
  |  V_proj output       | [1, 100, 512]        | [1, 1, 512]                |
  |  Q reshaped          | [1, 32, 100, 64]     | [1, 32, 1, 64]             |
  |  K reshaped          | [1, 8, 100, 64]      | [1, 8, 1, 64]              |
  |  KV cache per step   | CREATE [1,8,100,64]  | APPEND [1,8,1,64]          |
  |  Attention QK^T      | [1,32,100,100]       | [1,32,1,S]                 |
  |  Attention output    | [1,32,100,64]        | [1,32,1,64]                |
  |  Gate_proj output    | [1,100,8192]         | [1,1,8192]                 |
  |  Up_proj output      | [1,100,8192]         | [1,1,8192]                 |
  |  Down_proj output    | [1,100,2048]         | [1,1,2048]                 |
  |  LM Head output      | [1,100,128256]       | [1,1,128256]               |
  |  GEMM efficiency     | HIGH (fully utilized) | LOW (under-utilized)      |
  |  Bottleneck          | COMPUTE (MAC ops)    | MEMORY (KV cache BW)       |
  |  MACs per layer      | ~6.1B                | ~61M                       |
  |  KV cache read       | None (creating)      | Full cache per step        |
  |  Runs                | ONCE per request     | N times (gen tokens)       |
  +==========================================================================+

  GEMM SIZE COMPARISON (Per Layer):
  +--------------------------------------------------------------------------+
  |  Operation       | PREFILL MxKxN (T=100)      | DECODE MxKxN (T=1,S=100) |
  +--------------------------------------------------------------------------+
  |  Q_proj          | 100 x 2048 x 2048          | 1 x 2048 x 2048          |
  |  K_proj          | 100 x 2048 x 512           | 1 x 2048 x 512           |
  |  V_proj          | 100 x 2048 x 512           | 1 x 2048 x 512           |
  |  O_proj          | 100 x 2048 x 2048          | 1 x 2048 x 2048          |
  |  Gate_proj       | 100 x 2048 x 8192          | 1 x 2048 x 8192          |
  |  Up_proj         | 100 x 2048 x 8192          | 1 x 2048 x 8192          |
  |  Down_proj       | 100 x 8192 x 2048          | 1 x 8192 x 2048          |
  |  Attention QK^T  | 32 x 100 x 64 x 100        | 32 x 1 x 64 x 100        |
  |  Attention AV    | 32 x 100 x 100 x 64        | 32 x 1 x 100 x 64        |
  |  LM Head         | 100 x 2048 x 128256        | 1 x 2048 x 128256        |
  +--------------------------------------------------------------------------+
  |  PREFILL: 100x more output tokens processed per GEMM                     |
  |  DECODE: AIE columns under-utilized (only 1 row vs 64 tile height)       |
  +--------------------------------------------------------------------------+

  AIE TILE UTILIZATION:
  +--------------------------------------------------------------------------+
  |  Mode     | Rows  | Tile Rows Used | Utilization | Efficiency              |
  +--------------------------------------------------------------------------+
  |  PREFILL  | 100   | ceil(100/64)=2 | ~78%        | Good (2 tiles active)  |
  |  DECODE   | 1     | ceil(1/64)=1   | ~1.6%       | Poor (1/64 tile used)  |
  +--------------------------------------------------------------------------+
  |  DECODE is inherently inefficient on matrix hardware - this is why       |
  |  KV cache management and memory bandwidth are the critical bottlenecks.  |
  +--------------------------------------------------------------------------+


================================================================================
  SECTION 6: PER-LAYER OPERATOR SEQUENCE WITH SHAPES
================================================================================

  INPUT: hidden [batch=1, T, 2048] (from embedding or previous layer)
  |
  v
  +==========================================================================+
  | ATTENTION SUB-BLOCK                                                       |
  +==========================================================================+
  |                                                                          |
  |  (1) RMSNorm_1                                                           |
  |      Input:  hidden [1, T, 2048]                                         |
  |      Param:  rms_1.weight [2048]                                         |
  |      Output: normed [1, T, 2048]                                         |
  |      Op:     x * weight / RMS(x)                                         |
  |                                                                          |
  |  (2) Q_proj GEMM                                                         |
  |      Input:  normed [1, T, 2048]                                         |
  |      Weight: q_proj [2048, 2048] (TRANSPOSED, loaded from .npy)          |
  |      Op:     GEMM(T=transpose, M=T, K=2048, N=2048)                     |
  |      Output: Q_flat [1, T, 2048]                                         |
  |      MACs:   T * 2048 * 2048 = 4.2M * T                                  |
  |      T=100: 419M MACs | T=1: 4.2M MACs                                   |
  |                                                                          |
  |  (3) K_proj GEMM                                                         |
  |      Input:  normed [1, T, 2048]                                         |
  |      Weight: k_proj [2048, 512] (TRANSPOSED)                             |
  |      Op:     GEMM(T, M=T, K=2048, N=512)                                 |
  |      Output: K_flat [1, T, 512]                                          |
  |      MACs:   T * 2048 * 512 = 1.05M * T                                  |
  |                                                                          |
  |  (4) V_proj GEMM                                                         |
  |      Input:  normed [1, T, 2048]                                         |
  |      Weight: v_proj [2048, 512] (TRANSPOSED)                             |
  |      Op:     GEMM(T, M=T, K=2048, N=512)                                 |
  |      Output: V_flat [1, T, 512]                                          |
  |      MACs:   T * 2048 * 512 = 1.05M * T                                  |
  |                                                                          |
  |  (5) Reshape + RoPE                                                      |
  |      Q: [1,T,2048] -> [1,T,32,64] -> transpose -> [1,32,T,64]           |
  |      K: [1,T,512] -> [1,T,8,64]  -> transpose -> [1,8,T,64]             |
  |      V: [1,T,512] -> [1,T,8,64]  -> transpose -> [1,8,T,64]             |
  |      RoPE(Q): apply rotary embeddings -> [1,32,T,64]                    |
  |      RoPE(K): apply rotary embeddings -> [1,8,T,64]                     |
  |                                                                          |
  |  (6) Multi-Head Attention (GQA)                                         |
  |      KV Cache READ: K_cache[1,8,S,64], V_cache[1,8,S,64]               |
  |      KV Cache WRITE: append K[1,8,T,64], V[1,8,T,64]                   |
  |      GQA Expand: K[1,8,S,64] -> repeat(4) -> [1,32,S,64]              |
  |                V[1,8,S,64] -> repeat(4) -> [1,32,S,64]              |
  |      QK^T: [1,32,T,64] @ [1,32,64,S] -> scores [1,32,T,S]              |
  |      Scale: scores / sqrt(64) = scores / 8                              |
  |      Softmax: [1,32,T,S] (over S dimension)                             |
  |      Attend: softmax @ V[1,32,S,64] -> attn_out [1,32,T,64]            |
  |      Transpose: [1,32,T,64] -> [1,T,32,64] -> [1,T,2048]              |
  |      MACs: 2 * 32 * T * 64 * S = 4096 * T * S                          |
  |      T=100,S=100: 41M MACs | T=1,S=100: 0.41M MACs                      |
  |                                                                          |
  |  (7) O_proj GEMM                                                         |
  |      Input:  attn_out [1, T, 2048]                                       |
  |      Weight: o_proj [2048, 2048] (TRANSPOSED)                            |
  |      Op:     GEMM(T, M=T, K=2048, N=2048)                                |
  |      Output: o_out [1, T, 2048]                                          |
  |      MACs:   T * 2048 * 2048 = 4.2M * T                                  |
  |                                                                          |
  |  (8) Residual Add                                                        |
  |      Input:  o_out [1, T, 2048] + hidden [1, T, 2048]                    |
  |      Output: residual_1 [1, T, 2048]                                     |
  |      Op:     element-wise addition                                       |
  |                                                                          |
  +==========================================================================+
  |  MLP SUB-BLOCK                                                           |
  +==========================================================================+
  |                                                                          |
  |  (9) RMSNorm_2                                                           |
  |      Input:  residual_1 [1, T, 2048]                                     |
  |      Param:  rms_2.weight [2048]                                         |
  |      Output: normed2 [1, T, 2048]                                        |
  |                                                                          |
  |  (10) Gate_proj GEMM                                                     |
  |      Input:  normed2 [1, T, 2048]                                        |
  |      Weight: g_proj [2048, 8192] (TRANSPOSED)                            |
  |      Op:     GEMM(T, M=T, K=2048, N=8192)                                |
  |      Output: gate [1, T, 8192]                                           |
  |      MACs:   T * 2048 * 8192 = 16.8M * T                                 |
  |      T=100: 1.68B MACs | T=1: 16.8M MACs                                 |
  |                                                                          |
  |  (11) Up_proj GEMM                                                       |
  |      Input:  normed2 [1, T, 2048]                                        |
  |      Weight: u_proj [2048, 8192] (TRANSPOSED)                            |
  |      Op:     GEMM(T, M=T, K=2048, N=8192)                                |
  |      Output: up [1, T, 8192]                                             |
  |      MACs:   T * 2048 * 8192 = 16.8M * T                                 |
  |                                                                          |
  |  (12) SiLU Activation                                                    |
  |      Input:  gate [1, T, 8192]                                           |
  |      Op:     x * sigmoid(x) (element-wise)                               |
  |      Output: silu_out [1, T, 8192]                                       |
  |                                                                          |
  |  (13) Element-wise Multiply                                              |
  |      Input:  silu_out [1, T, 8192] * up [1, T, 8192]                     |
  |      Output: mlp_intermediate [1, T, 8192]                               |
  |                                                                          |
  |  (14) Down_proj GEMM                                                     |
  |      Input:  mlp_intermediate [1, T, 8192]                               |
  |      Weight: d_proj [8192, 2048] (TRANSPOSED)                            |
  |      Op:     GEMM(T, M=T, K=8192, N=2048)                                |
  |      Output: mlp_out [1, T, 2048]                                        |
  |      MACs:   T * 8192 * 2048 = 16.8M * T                                 |
  |                                                                          |
  |  (15) Residual Add                                                       |
  |      Input:  mlp_out [1, T, 2048] + residual_1 [1, T, 2048]              |
  |      Output: layer_output [1, T, 2048] -> input to next layer            |
  |                                                                          |
  +==========================================================================+

  MACs PER LAYER SUMMARY:
  +--------------------------------------------------------------------------+
  |  Operation       | MACs Formula           | T=100        | T=1            |
  +--------------------------------------------------------------------------+
  |  Q_proj          | T * 2048 * 2048        | 419M         | 4.2M           |
  |  K_proj          | T * 2048 * 512         | 105M         | 1.0M           |
  |  V_proj          | T * 2048 * 512         | 105M         | 1.0M           |
  |  Attention       | 2 * 32 * T * 64 * S    | 41M (S=100)  | 0.4M (S=100)   |
  |  O_proj          | T * 2048 * 2048        | 419M         | 4.2M           |
  |  Gate_proj       | T * 2048 * 8192        | 1.68B        | 16.8M          |
  |  Up_proj         | T * 2048 * 8192        | 1.68B        | 16.8M          |
  |  Down_proj       | T * 8192 * 2048        | 1.68B        | 16.8M          |
  |  Elementwise     | ~T * 8192 * 3          | 2.5M         | 25K            |
  |  Residual+Norm   | ~T * 2048 * 5          | 10M          | 10K            |
  +--------------------------------------------------------------------------+
  |  TOTAL per layer |                       | ~6.1B        | ~61M           |
  |  16 layers total |                       | ~98B         | ~976M          |
  +--------------------------------------------------------------------------+
  |  Note: MLP dominates (~83% of compute) due to intermediate_size=8192     |
  +--------------------------------------------------------------------------+


================================================================================
  SECTION 7: NPU EXECUTION MODEL (AIE TILING)
================================================================================

  +==========================================================================+
  | AMD RYZEN AI NPU ARCHITECTURE                                            |
  +==========================================================================+
  |                                                                          |
  |  +--------------------------------------------------------------------+  |
  |  |  AIE ARRAY (8 Columns)                                              |  |
  |  |  +-------+-------+-------+-------+-------+-------+-------+------+  |  |
  |  |  | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |Col 7 |  |  |
  |  |  | 64x64 | 64x64 | 64x64 | 64x64 | 64x64 | 64x64 | 64x64 |64x64 |  |  |
  |  |  | MAC   | MAC   | MAC   | MAC   | MAC   | MAC   | MAC   | MAC  |  |  |
  |  |  +-------+-------+-------+-------+-------+-------+-------+------+  |  |
  |  |           ^              ^              ^              ^            |  |
  |  |           |              |              |              |            |  |
  |  |  +----------------------------------------------------------+      |  |
  |  |  | DMA Engine (system RAM <-> AIE local memory)             |      |  |
  |  |  +----------------------------------------------------------+      |  |
  |  |           ^                                                         |  |
  |  |           |                                                         |  |
  |  |  +----------------------------------------------------------+      |  |
  |  |  | System RAM (weights + KV cache + activations)             |      |  |
  |  |  |  Weights: 2.4GB (memory-mapped from .npy files)          |      |  |
  |  |  |  KV Cache: 128MB-4GB (dynamic)                           |      |  |
  |  |  |  Activations: ~140MB (temporary)                         |      |  |
  |  |  +----------------------------------------------------------+      |  |
  |  +--------------------------------------------------------------------+  |
  |                                                                          |
  +==========================================================================+

  LARGE GEMM EXECUTION (e.g., Q_proj: T=100, 2048x2048):
  +--------------------------------------------------------------------------+
  |  Input:  [1, 100, 2048] = 100 rows of 2048                               |
  |  Weight: [2048, 2048] (TRANSPOSED)                                       |
  |  Output: [1, 100, 2048] = 100 rows of 2048                               |
  |                                                                          |
  |  TILING STRATEGY:                                                        |
  |    Input rows: ceil(100/64) = 2 tile rows                                |
  |    Output cols: 2048/64 = 32 tile columns                                |
  |    K dim: 2048/64 = 32 tile reductions                                   |
  |    Total tiles: 2 * 32 * 32 = 2048 tiles                                 |
  |    With 8 AIE columns: 2048/8 = 256 tile execution batches               |
  |                                                                          |
  |  EXECUTION SCHEDULE (simplified):                                        |
  |    Batch 1: DMA input tiles [0:64, :] + weight tiles [0:64, 0:64]       |
  |             AIE Col 0-7 compute 8 tiles in parallel                      |
  |             Write output tiles [0:64, 0:64] to accumulation buffer       |
  |    Batch 2: DMA weight tiles [64:128, 0:64]                              |
  |             AIE Col 0-7 compute 8 tiles (accumulate)                     |
  |    ... (32 K-reduction batches per input-output tile pair)               |
  |    Batch 256: Final output written to activation buffer                  |
  +--------------------------------------------------------------------------+

  DECODE GEMM EXECUTION (e.g., Q_proj: T=1, 2048x2048):
  +--------------------------------------------------------------------------+
  |  Input:  [1, 1, 2048] = 1 row of 2048                                    |
  |  Weight: [2048, 2048] (TRANSPOSED)                                       |
  |  Output: [1, 1, 2048] = 1 row of 2048                                    |
  |                                                                          |
  |  TILING STRATEGY:                                                        |
  |    Input rows: ceil(1/64) = 1 tile row (only 1/64 utilized)             |
  |    Output cols: 2048/64 = 32 tile columns                                |
  |    K dim: 2048/64 = 32 tile reductions                                   |
  |    Total tiles: 1 * 32 * 32 = 1024 tiles                                 |
  |    With 8 AIE columns: 1024/8 = 128 tile execution batches               |
  |                                                                          |
  |  Inefficiency: Only 1 of 64 rows in each tile is used = 1.6% utilization |
  |  This is the fundamental decode bottleneck on NPU hardware.              |
  +--------------------------------------------------------------------------+

  KV CACHE DATA FLOW (Decode step):
  +--------------------------------------------------------------------------+
  |  Step N: generating token N (context S = prompt_len + N - 1)            |
  |                                                                          |
  |  1. DMA READ: Load K_cache[16, 8, S, 64] from system RAM                |
  |     Size: 16 * 8 * S * 64 * 2 = 16384 * S bytes                         |
  |     At S=100: 1.6MB | At S=1000: 16MB                                    |
  |                                                                          |
  |  2. DMA READ: Load V_cache[16, 8, S, 64] from system RAM                |
  |     Size: same as K_cache                                                |
  |                                                                          |
  |  3. AIE COMPUTE: Attention with single-token Q                           |
  |     Q[1,32,1,64] @ K_cache[1,32,S,64]^T -> [1,32,1,S]                  |
  |     Softmax -> attend with V_cache -> [1,32,1,64]                       |
  |                                                                          |
  |  4. DMA WRITE: Append new K[16, 8, 1, 64] to KV cache                   |
  |     Size: 16 * 8 * 1 * 64 * 2 = 16KB per decode step                    |
  |                                                                          |
  |  5. DMA WRITE: Append new V[16, 8, 1, 64] to KV cache                   |
  |     Size: 16KB per decode step                                           |
  |                                                                          |
  |  Total DMA per decode step: 2 * 16384 * S + 32KB                        |
  |  At S=100: ~3.3MB | At S=1000: ~33MB | At S=4096: ~128MB                |
  |                                                                          |
  |  CRITICAL: KV cache bandwidth dominates decode latency                   |
  +--------------------------------------------------------------------------+


================================================================================
  SECTION 8: COMPLETE PIPELINE DATA FLOW (END-TO-END)
================================================================================

  +==========================================================================+
  |                        COMPLETE IRON NPU PIPELINE                        |
  +==========================================================================+
  |                                                                          |
  |  OFFLINE CONVERSION                                     RUNTIME          |
  |  =================                                    =========          |
  |                                                                          |
  |  [HF Model Dir]                                         [User Prompt]   |
  |       |                                                      |           |
  |       v                                                      v           |
  |  +----------------+                             +------------------+     |
  |  | Phase 1-2:     |                             | Tokenizer        |     |
  |  | Resolve+Parse  |                             | "What is ML?"    |     |
  |  | config.json -> |                             | -> [151644,...]  |     |
  |  | spec dict      |                             | [1, 8]           |     |
  |  +----------------+                             +------------------+     |
  |       |                                                      |           |
  |       v                                                      v           |
  |  +----------------+                             +------------------+     |
  |  | Phase 3:       |                             | Embedding Layer  |     |
  |  | Compatibility  |                             | [1,8] lookup ->  |     |
  |  | [PASS x6]      |                             | [1,8,2048]       |     |
  |  +----------------+                             +------------------+     |
  |       |                                                      |           |
  |       v                                                      v           |
  |  +----------------+                             +==================+     |
  |  | Phase 4:       |          .npy files         |  PREFILL PHASE   |     |
  |  | NPU Config     |      +----------------+     |  [1,100,2048] -> |     |
  |  | AIE cols=8     |      | Weight Files   |     |  16 layers       |     |
  |  | Tile 64x64x64  |----->| layer_0/*.npy  |     |  Build KV cache  |     |
  |  +----------------+  |   | ...            |     |  [1,32,100,64]  |     |
  |                      |   | layer_15/*.npy |     +==================+     |
  |       v              |   | manifest.json  |              |                 |
  |  +----------------+  |   +----------------+              v                 |
  |  | Phase 5-7:     |  |                               +==================+ |
  |  | Load+Map+Shape |  |   KV Cache (System RAM)        |  DECODE PHASE    | |
  |  | safetensors->  |--+  +----------------+            |  [1,1,2048] ->   | |
  |  | .npy + TRANSPOSE|   | K[16,8,S,64]   |            |  16 layers       | |
  |  +----------------+    | V[16,8,S,64]   |            |  Grow KV cache   | |
  |                        +----------------+            |  Sample token    | |
  |       v                                              +==================+ |
  |  +----------------+              ^                        |               |
  |  | Phase 8-9:     |              | DMA                    v               |
  |  | Assembly+Export|--------------+                       +------------+  |
  |  | manifest.json  |                                      | EOS? Done  |  |
  |  | 148 files      |                                      | No: loop   |  |
  |  | ~2.4GB         |                                      +------------+  |
  |  +----------------+                                                      |
  |                                                                          |
  +==========================================================================+

  PROMPT-TO-OUTPUT EXAMPLE (Llama-3.2-1B):
  +--------------------------------------------------------------------------+
  |  1. User types: "What is machine learning?"                              |
  |  2. Tokenize: [151644, 791, 338, 37219, 2629, 1615, 13, 151645] (8 toks)|
  |  3. Embed: [1, 8, 2048] (32KB of activation)                             |
  |  4. PREFILL: 16 layers * 15 ops = 240 operators                          |
  |     - ~7.8B MACs for prefill (8 prompt tokens * 16 layers)               |
  |     - KV cache: 16 * 2 * 8 * 8 * 64 * 2 = 256KB                         |
  |  5. LM Head: [1, 8, 128256] -> sample last token                         |
  |     -> next_token = 4521 ("Machine")                                     |
  |  6. DECODE step 1:                                                       |
  |     - Embed 4521 -> [1, 1, 2048]                                         |
  |     - 16 layers: ~976M MACs                                              |
  |     - KV cache read: 16 * 2 * 8 * 9 * 64 * 2 = 288KB                    |
  |     - KV cache write: 16 * 2 * 8 * 1 * 64 * 2 = 32KB                    |
  |     - LM Head: [1, 1, 128256] -> sample                                   |
  |     -> next_token = 1917 ("learning")                                    |
  |  7. DECODE step 2: ... (context S=10)                                    |
  |     -> next_token = 1890 ("is")                                          |
  |  8. DECODE step 3: ... (context S=11)                                    |
  |     -> next_token = 264 ("a")                                            |
  |  9. ... continue until EOS token (151645)                               |
  |  10. Detokenize: [4521, 1917, 1890, 264, ...] -> "Machine learning is..."|
  +--------------------------------------------------------------------------+


================================================================================
  SECTION 9: KEY METRICS & BOTTLENECKS
================================================================================

  +==========================================================================+
  | PERFORMANCE CHARACTERISTICS (Llama-3.2-1B, Ryzen AI NPU)                |
  +==========================================================================+
  |                                                                          |
  |  WEIGHT LOADING:                                                         |
  |    Total weight size: ~2.4GB                                             |
  |    Load time (typical SSD 500MB/s): ~4.8 seconds                         |
  |    Load time (NVMe 3GB/s): ~0.8 seconds                                  |
  |    Memory mapping (.npy): near-instant (OS page cache)                   |
  |                                                                          |
  |  PREFILL PERFORMANCE:                                                    |
  |    Compute: ~98B MACs (16 layers, T=100)                                |
  |    NPU peak: ~50 TOPS (bf16) theoretical                                 |
  |    Estimated: ~2 seconds (compute-bound)                                 |
  |    Dominated by: MLP GEMMs (gate, up, down projections)                 |
  |                                                                          |
  |  DECODE PERFORMANCE (per token):                                         |
  |    Compute: ~976M MACs (16 layers, T=1)                                 |
  |    KV cache bandwidth: 2 * 16KB * S bytes per step                      |
  |    At S=100: ~3.2MB KV cache traffic per token                           |
  |    At S=1000: ~32MB KV cache traffic per token                           |
  |    At S=4096: ~128MB KV cache traffic per token                          |
  |    Estimated: ~50-100ms per token (memory-bound)                         |
  |    Tokens/sec: ~10-20 tokens/sec                                         |
  |                                                                          |
  |  MEMORY BOUNDARIES:                                                      |
  |    Minimum RAM: 2.4GB (weights only, no context)                        |
  |    Typical RAM: 2.6GB (weights + 4K context)                            |
  |    Max RAM: ~6.5GB (weights + 128K context)                             |
  |    NPU local memory: limited by AIE tile size (64x64x64 bf16 = 512KB)   |
  |                                                                          |
  |  BOTTLENECK ANALYSIS:                                                    |
  |    +-------------------+------------------+------------------------------+|
  |    | Phase             | Bottleneck       | Mitigation                   ||
  |    +-------------------+------------------+------------------------------+|
  |    | Prefill           | AIE compute      | -                            ||
  |    | Decode (short)    | AIE utilization  | Batch tokens / continuous    ||
  |    |                   | (1.6% tile use)  | batching (future)            ||
  |    | Decode (long)     | KV cache BW      | Quantization, paging         ||
  |    | Weight loading    | Disk I/O         | Memory mapping, mmap         ||
  |    | KV cache growth   | System RAM       | Eviction, sliding window     ||
  |    +-------------------+------------------+------------------------------+|
  |                                                                          |
  +==========================================================================+


================================================================================
  END OF DATA FLOW DIAGRAM
  Model: Llama-3.2-1B | NPU: AMD Ryzen AI | dtype: bfloat16
  Total Parameters: ~1.3B* | Weight Files: 147 | Total Weight Size: ~2.9GB
  Operators: 243 (240 layer + 3 global) | AIE Columns: 8 | Tile: 64x64x64
  * With weight tying (lm_head shares embedding): ~1.07B params, ~2.4GB
================================================================================
