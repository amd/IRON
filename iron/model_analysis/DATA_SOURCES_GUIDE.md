# Complete Data Sources Guide for IRON Operator Creation

**SLC: Simple. Lovable. Complete.**

This document answers the fundamental question:

> **"Where do I get ALL the data needed to write an unsupported IRON operator?"**

---

## The Complete Data Model

To implement ANY custom NPU operator for IRON, you need **6 categories of data**:

| # | Data Category | What It Tells You | Source |
|---|---------------|-------------------|--------|
| 1 | **Hyperparameters** | Layer configuration (hidden_size, num_heads, etc.) | Transformers config |
| 2 | **Tensor Signatures** | Input/output shapes and dtypes | forward() signature |
| 3 | **Computation Graph** | What operations are performed | forward() source |
| 4 | **IRON Base Class** | Which existing IRON operator to extend | Pattern matching |
| 5 | **AIE/MLIR Patterns** | How to structure NPU code | mlir-aie + examples |
| 6 | **Tiling Strategy** | How to tile for NPU memory | Manual analysis |

---

## Data Source 1: Hyperparameters

### What You Get
- `hidden_size`: Model dimension (e.g., 4096)
- `num_attention_heads`: Number of attention heads (e.g., 32)
- `num_key_value_heads`: KV heads for GQA (e.g., 8)
- `intermediate_size`: FFN expansion (e.g., 11008)
- `sliding_window`: Attention window size (e.g., 4096)
- `num_experts`: MoE expert count (e.g., 128)
- `rope_theta`: RoPE frequency base (e.g., 1000000)
- `rms_norm_eps`: Normalization epsilon (e.g., 1e-6)

### Where It Comes From
```
HuggingFace Hub → config.json → AutoConfig → Python dict
```

### How to Extract

**Method 1: CLI scan**
```bash
python -m iron.model_analysis scan meta-llama/Llama-2-7b-hf
```

**Method 2: Python API**
```python
from iron.model_analysis import scan_model

info = scan_model("meta-llama/Llama-2-7b-hf")
print(info.config_dict)
# {'hidden_size': 4096, 'num_attention_heads': 32, ...}
```

**Method 3: Direct from Transformers**
```python
from transformers import AutoConfig

config = AutoConfig.from_pretrained("meta-llama/Llama-2-7b-hf")
print(config.hidden_size)        # 4096
print(config.num_attention_heads)  # 32
```

### Used In Operator Code
```python
class AIELlamaAttention(AIEOperatorBase):
    def __init__(self, hidden_size=4096, num_heads=32, num_kv_heads=8, ...):
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.num_kv_heads = num_kv_heads
        # ... store all hyperparameters
```

---

## Data Source 2: Tensor Signatures

### What You Get
- **Input names**: `hidden_states`, `attention_mask`, `position_ids`
- **Input shapes**: `[batch, seq_len, hidden_size]`
- **Output shapes**: `[batch, seq_len, hidden_size]`
- **Dtypes**: `torch.float16`, `torch.bfloat16`

### Where It Comes From
```
Transformers Source → inspect.signature(forward) → Parameter analysis
```

### How to Extract

**Method 1: CLI spec command**
```bash
python -m iron.model_analysis spec meta-llama/Llama-2-7b-hf \
    --layer LlamaAttention \
    --output llama_attn_spec.md
```

**Method 2: Python inspection**
```python
import inspect
from transformers.models.llama.modeling_llama import LlamaAttention

sig = inspect.signature(LlamaAttention.forward)
print(sig)
# (self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor], ...)
```

**Method 3: Our spec generator**
```python
from iron.model_analysis import generate_operator_spec

spec = generate_operator_spec("meta-llama/Llama-2-7b-hf", "LlamaAttention")
print(spec.inputs)
# [TensorSpec(name='hidden_states', shape='[batch, seq_len, 4096]', ...)]
```

### Used In Operator Code
```python
def forward(self, hidden_states, attention_mask=None, position_embeddings=None):
    """
    Args:
        hidden_states: [batch, seq_len, hidden_size]
        attention_mask: [batch, seq_len] or [batch, heads, seq_len, seq_len]
        position_embeddings: (cos, sin) tuples for RoPE
    """
    batch_size, seq_len, _ = hidden_states.shape
    # ...
```

---

## Data Source 3: Computation Graph

### What You Get
- The actual **sequence of operations** in forward()
- **Control flow**: if statements, loops
- **Function calls**: `apply_rotary_pos_emb`, `softmax`, etc.
- **Tensor manipulations**: transpose, reshape, matmul

### Where It Comes From
```
Transformers Source → modeling_<type>.py → inspect.getsource(forward)
```

### How to Extract

**Method 1: CLI spec with full source**
```bash
python -m iron.model_analysis spec mistralai/Mistral-7B-v0.1 \
    --layer MistralAttention \
    --output mistral_attn_spec.md
```

The output includes:
```markdown
## Reference Implementation (Transformers)

```python
def forward(self, hidden_states, attention_mask, position_embeddings):
    bsz, q_len, _ = hidden_states.size()

    # Project QKV
    query_states = self.q_proj(hidden_states)
    key_states = self.k_proj(hidden_states)
    value_states = self.v_proj(hidden_states)

    # Reshape for multi-head
    query_states = query_states.view(bsz, q_len, self.num_heads, self.head_dim).transpose(1, 2)

    # Apply RoPE
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)

    # Compute attention
    attn_weights = torch.matmul(query_states, key_states.transpose(2, 3)) / math.sqrt(self.head_dim)
    attn_weights = attn_weights + attention_mask
    attn_weights = nn.functional.softmax(attn_weights, dim=-1)

    # Output
    attn_output = torch.matmul(attn_weights, value_states)
    attn_output = attn_output.transpose(1, 2).reshape(bsz, q_len, self.hidden_size)
    attn_output = self.o_proj(attn_output)

    return attn_output
```
```

**Method 2: Manual inspection**
```python
import inspect
from transformers.models.mistral.modeling_mistral import MistralAttention

source = inspect.getsource(MistralAttention.forward)
print(source)
```

**Method 3: Operations analysis**
```python
spec = generate_operator_spec("mistralai/Mistral-7B-v0.1", "MistralAttention")
print(spec.operations)
# ['torch.matmul', 'torch.softmax', 'torch.transpose', 'apply_rotary_pos_emb']
```

### Used In Operator Design
```python
# design.py - MLIR generation
def generate_mlir(num_heads, head_dim, sliding_window):
    """
    MLIR must implement:
    1. QKV projection (GEMM)
    2. Reshape + transpose
    3. RoPE application
    4. Scaled dot-product attention
    5. Output projection
    """
    # Translate each operation to AIE dialect
    # ...
```

---

## Data Source 4: IRON Base Class

### What You Get
- Which **existing IRON operator** to extend
- Inheritance pattern
- Required methods to implement

### Where It Comes From
```
Pattern matching on layer name → IRON_BASE_CLASS_MAP
```

### How to Extract

**Method 1: CLI spec (automatic suggestion)**
```bash
python -m iron.model_analysis spec mistralai/Mistral-7B-v0.1 \
    --layer MistralAttention
```

Output includes:
```markdown
**Suggested Base Class:** `AIEGEMM + custom attention mask`
```

**Method 2: Manual lookup**
```python
# From operator_spec.py
IRON_BASE_CLASS_MAP = {
    "attention": "AIEGEMM + custom attention mask",
    "norm": "AIERMSNorm",
    "mlp": "AIEGEMM",
    "rope": "AIERoPE",
    "moe": "AIEGEMM + custom routing",
}
```

**Method 3: Browse existing operators**
```bash
ls iron/operators/
# gemm/          → AIEGEMM
# rms_norm/      → AIERMSNorm
# rope/          → AIERoPE
# mha/           → AIEMHA
```

### Used In Operator Code
```python
# Standard attention - extend GEMM
class AIEAttention(AIEGEMM):
    pass

# Normalization - extend RMSNorm
class AIERMSNorm(AIERMSNorm):
    pass

# Custom operator - extend base
class AIESlidingWindowAttention(AIEOperatorBase):
    pass
```

---

## Data Source 5: AIE/MLIR Patterns

### What You Get
- **MLIR dialect structure**: `aie.*`, `affine.*`, `linalg.*`
- **ObjectFIFO patterns**: Data movement between tiles
- **Kernel structure**: Compute core code
- **DMA transfer patterns**: Host ↔ NPU communication

### Where It Comes From
```
mlir-aie library + iron/operators/*/design.py examples
```

### How to Extract

**Method 1: Study existing operators**
```bash
# View a complete design.py example
cat iron/operators/rms_norm/design.py
cat iron/operators/gemm/design.py
cat iron/operators/rope/design.py
```

**Method 2: mlir-aie documentation**
```
https://github.com/Xilinx/mlir-aie/tree/main/docs
```

**Method 3: Generate from template**
```bash
python -m iron.model_analysis spec mistralai/Mistral-7B-v0.1 \
    --layer MistralAttention \
    --skeleton mistral_attn.py
```

This generates `design.py` template:
```python
# design.py
from aie.iron import Kernel, ObjectFifo, Program, Buffer, Runtime
from aie.iron.placers import SequentialPlacer

def generate_mlir(num_heads, head_dim, sliding_window):
    device_type = aie.device.XC35
    rt = Runtime()

    # Define buffers
    # Define ObjectFifos
    # Define kernels
    # Build program

    program = Program(device_type, rt)
    module = program.resolve_program(SequentialPlacer())
    return module
```

### Key AIE/MLIR Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| `aie.core` | Compute tile | `with core(tile):` |
| `aie.buffer` | On-chip memory | `Buffer(dtype, shape)` |
| `ObjectFifo` | Data movement | `ObjectFifo(inputs, outputs)` |
| `aie.external` | DRAM interface | `ExternalBuffer` |
| `Runtime` | Execution control | `rt.sequence()` |

---

## Data Source 6: Tiling Strategy

### What You Get
- **Tile sizes**: How to chunk tensors for NPU memory
- **Memory layout**: Row-major vs column-major
- **Ping-pong buffering**: Double-buffering for throughput

### Where It Comes From
```
Manual analysis of tensor sizes vs NPU memory constraints
```

### How to Determine

**Step 1: Calculate tensor sizes**
```python
# Example: Llama-2-7B attention
hidden_size = 4096
num_heads = 32
head_dim = 128
seq_len = 128  # context length

# Weight matrix: 4096 x 4096 x 2 bytes = 32 MB (too big for NPU SRAM)
# Must tile!

# NPU SRAM is ~1 MB per tile
# Tile size: 128 x 128 = 32 KB (fits comfortably)
```

**Step 2: Design tiling pattern**
```python
# Tile the GEMM operation
def tile_gemm(A, B, tile_size=128):
    M, K = A.shape
    K, N = B.shape

    for i in range(0, M, tile_size):
        for j in range(0, N, tile_size):
            for k in range(0, K, tile_size):
                # Load tile into SRAM
                # Compute partial result
                # Accumulate
                pass
```

**Step 3: Consult existing patterns**
```bash
# Study how existing operators handle tiling
cat iron/operators/gemm/design.py  # Look for tiling logic
```

---

## Complete Walkthrough: Llama Attention

Let's compile ALL data for implementing `LlamaAttention`:

### Step 1: Run Analysis
```bash
# Scan the model
python -m iron.model_analysis scan meta-llama/Llama-2-7b-hf

# Generate full spec
python -m iron.model_analysis spec meta-llama/Llama-2-7b-hf \
    --layer LlamaAttention \
    --output llama_attn_spec.md \
    --skeleton llama_attention.py
```

### Step 2: Extract Hyperparameters
```python
from iron.model_analysis import scan_model

info = scan_model("meta-llama/Llama-2-7b-hf")
config = info.config_dict

# Extracted values:
hidden_size = 4096
num_attention_heads = 32
num_key_value_heads = 8  # GQA!
head_dim = hidden_size // num_attention_heads  # 128
intermediate_size = 11008
rms_norm_eps = 1e-6
max_position_embeddings = 4096
rope_theta = 10000
```

### Step 3: Extract Signatures
```python
from iron.model_analysis import generate_operator_spec

spec = generate_operator_spec("meta-llama/Llama-2-7b-hf", "LlamaAttention")

# Inputs:
# - hidden_states: [batch, seq_len, 4096]
# - attention_mask: Optional [batch, heads, seq_len, seq_len]
# - position_embeddings: (cos, sin) for RoPE

# Output:
# - attn_output: [batch, seq_len, 4096]
```

### Step 4: Extract Computation Graph
```python
print(spec.forward_source)
```

```python
def forward(self, hidden_states, attention_mask, position_embeddings):
    bsz, q_len, _ = hidden_states.size()

    # QKV projection
    query_states = self.q_proj(hidden_states)
    key_states = self.k_proj(hidden_states)
    value_states = self.v_proj(hidden_states)

    # Reshape for multi-head attention
    query_states = query_states.view(bsz, q_len, self.num_heads, self.head_dim).transpose(1, 2)
    key_states = key_states.view(bsz, q_len, self.num_kv_heads, self.head_dim).transpose(1, 2)
    value_states = value_states.view(bsz, q_len, self.num_kv_heads, self.head_dim).transpose(1, 2)

    # Apply RoPE
    cos, sin = position_embeddings
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)

    # Repeat KV for GQA
    key_states = repeat_kv(key_states, self.num_key_value_groups)
    value_states = repeat_kv(value_states, self.num_key_value_groups)

    # Scaled dot-product attention
    attn_weights = torch.matmul(query_states, key_states.transpose(2, 3)) / math.sqrt(self.head_dim)
    attn_weights = attn_weights + attention_mask
    attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32)
    attn_weights = attn_weights.to(query_states.dtype)

    # Compute output
    attn_output = torch.matmul(attn_weights, value_states)
    attn_output = attn_output.transpose(1, 2).reshape(bsz, q_len, self.hidden_size)
    attn_output = self.o_proj(attn_output)

    return attn_output
```

### Step 5: Determine Base Class
```python
print(spec.suggested_base_class)
# "AIEGEMM + custom attention mask"
```

### Step 6: Analyze Operations
```python
print(spec.operations)
# ['torch.matmul', 'torch.softmax', 'torch.transpose',
#  'torch.view', 'apply_rotary_pos_emb', 'repeat_kv']
```

### Step 7: Generate Skeleton
```bash
python -m iron.model_analysis spec meta-llama/Llama-2-7b-hf \
    --layer LlamaAttention \
    --skeleton llama_attention.py
```

Generates `llama_attention.py`:
```python
# SPDX-FileCopyrightText: Copyright (C) 2025 AMD
# SPDX-License-Identifier: Apache-2.0

from iron.common import AIEOperatorBase, AIEContext
from iron.common.compilation import (
    XclbinArtifact, InstsBinArtifact,
    KernelObjectArtifact, KernelArchiveArtifact,
    PythonGeneratedMLIRArtifact,
)
from pathlib import Path


class AIELlamaAttention(AIEOperatorBase):
    """
    Llama-style grouped query attention with RoPE.
    """

    def __init__(
        self,
        hidden_size: int = 4096,
        num_heads: int = 32,
        num_kv_heads: int = 8,
        head_dim: int = 128,
        rope_theta: float = 10000.0,
        context=None,
    ):
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.num_kv_heads = num_kv_heads
        self.head_dim = head_dim
        self.rope_theta = rope_theta
        super().__init__(context=context)

    def set_up_artifacts(self):
        """Set up compilation artifacts."""
        operator_dir = Path(__file__).parent

        self.mlir_artifact = PythonGeneratedMLIRArtifact.new(
            "llama_attention.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="generate_mlir",
            callback_kwargs={
                "num_heads": self.num_heads,
                "num_kv_heads": self.num_kv_heads,
                "head_dim": self.head_dim,
            },
        )

        self.xclbin_artifact = XclbinArtifact.new(
            "llama_attention.xclbin",
            mlir_artifact=self.mlir_artifact,
        )

        self.insts_bin_artifact = InstsBinArtifact.new(
            "llama_attention.insts.bin",
            xclbin_artifact=self.xclbin_artifact,
        )

        self.kernel_obj_artifact = KernelObjectArtifact.new(
            "llama_attention.o",
            xclbin_artifact=self.xclbin_artifact,
        )

        self.kra_artifact = KernelArchiveArtifact.new(
            "llama_attention.kra",
            kernel_obj_artifacts=[self.kernel_obj_artifact],
        )

    def set_up_runtime(self):
        """Set up runtime buffers and kernels."""
        # Input: hidden_states [batch, seq_len, hidden_size]
        self.add_buffer("hidden_states", self.hidden_size * 2)  # bytes

        # QKV weights
        self.add_buffer("q_weight", self.hidden_size * self.hidden_size * 2)
        self.add_buffer("k_weight", self.hidden_size * self.num_kv_heads * self.head_dim * 2)
        self.add_buffer("v_weight", self.hidden_size * self.num_kv_heads * self.head_dim * 2)

        # Output
        self.add_buffer("output", self.hidden_size * 2)

        # Kernels
        self.add_kernel("qkv_proj", input_buffers=["hidden_states"], output_buffers=["query", "key", "value"])
        self.add_kernel("rope", input_buffers=["query", "key", "cos", "sin"], output_buffers=["query", "key"])
        self.add_kernel("attention", input_buffers=["query", "key", "value", "mask"], output_buffers=["attn_out"])
        self.add_kernel("o_proj", input_buffers=["attn_out", "o_weight"], output_buffers=["output"])

    def forward(self, hidden_states, attention_mask=None, position_embeddings=None):
        """
        Llama attention forward pass.

        Args:
            hidden_states: [batch, seq_len, hidden_size]
            attention_mask: Optional attention mask
            position_embeddings: (cos, sin) for RoPE

        Returns:
            Output tensor [batch, seq_len, hidden_size]
        """
        batch_size, seq_len, _ = hidden_states.shape

        # Write input
        self.write_buffer("hidden_states", hidden_states)

        # Execute
        self.run_runlist()

        # Read output
        output_shape = (batch_size, seq_len, self.hidden_size)
        result = self.read_buffer_as_torch("output", shape=output_shape)

        return result
```

### Step 8: Create MLIR Design
```python
# design.py
from aie.iron import Kernel, ObjectFifo, Program, Buffer, Runtime
from aie.iron.placers import SequentialPlacer
import aie


def generate_mlir(num_heads, num_kv_heads, head_dim):
    """Generate MLIR for Llama attention."""

    device_type = aie.device.XC35
    rt = Runtime()

    # Define memory maps
    ShimDMA = aie.get_tile_type(aie.TileType.SHIM_DMA)

    # Input/Output buffers
    with rt.sequence(aie_dtype.s16, "in", "out") as (win, wout):
        # Load tiles for QKV projection
        # Compute attention with GQA
        # Apply RoPE
        # Output projection
        pass

    program = Program(device_type, rt)
    module = program.resolve_program(SequentialPlacer())

    return module
```

---

## Summary: The Complete Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATA COMPILATION WORKFLOW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. MODEL NAME                                                   │
│     ↓                                                            │
│  2. AutoConfig → Hyperparameters                                │
│     ↓                                                            │
│  3. scan_model() → Architecture info                            │
│     ↓                                                            │
│  4. generate_operator_spec() → Full spec                        │
│     ├── Tensor signatures                                        │
│     ├── forward() source                                         │
│     ├── Operations list                                          │
│     └── Suggested base class                                     │
│     ↓                                                            │
│  5. --skeleton flag → Starter code                              │
│     ├── op.py (operator interface)                               │
│     └── design.py (MLIR generation)                              │
│     ↓                                                            │
│  6. Manual analysis → Tiling strategy                           │
│     ↓                                                            │
│  7. Study examples → AIE/MLIR patterns                          │
│     ↓                                                            │
│  8. IMPLEMENT!                                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Reference: Commands

```bash
# 1. Scan model (get hyperparameters)
python -m iron.model_analysis scan <model_name>

# 2. Analyze compatibility (find gaps)
python -m iron.model_analysis analyze <model_name>

# 3. Generate operator spec (all data in one doc)
python -m iron.model_analysis spec <model_name> \
    --layer <LayerName> \
    --output spec.md

# 4. Generate skeleton code (starter implementation)
python -m iron.model_analysis spec <model_name> \
    --layer <LayerName> \
    --skeleton my_operator.py
```

---

## License

Apache 2.0
