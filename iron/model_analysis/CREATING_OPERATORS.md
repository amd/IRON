# Creating Custom NPU Operators for IRON

**SLC: Simple. Lovable. Complete.**

This guide shows you how to create new IRON operators for unsupported layers in new model architectures.

**Need to know where ALL the data comes from?** See the comprehensive reference:
[`DATA_SOURCES_GUIDE.md`](DATA_SOURCES_GUIDE.md) - Complete walkthrough of extracting hyperparameters, signatures, computation graphs, and AIE/MLIR patterns.

---

## The Complete Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  1. ANALYZE: What does the model need?                          │
│     → python -m iron.model_analysis analyze <model>             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  2. SPEC: What does the unsupported layer do?                   │
│     → python -m iron.model_analysis spec <model> --layer <X>    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  3. SKELETON: Generate starter code                             │
│     → Add --skeleton operator_name.py to spec command           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  4. IMPLEMENT: Fill in the AIE logic                            │
│     → Set up artifacts, runtime, forward()                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  5. REGISTER: Add to operator registry                          │
│     → Use @OperatorRegistry.register() decorator                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  6. TEST: Verify against Transformers reference                 │
│     → Compare outputs, check performance                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step 1: Analyze the Model

Run a gap analysis to see what's supported and what needs custom operators:

```bash
python -m iron.model_analysis analyze mistralai/Mistral-7B-v0.1
```

**Example output:**
```
SUMMARY
----------------------------------------
  Model Type: mistral
  Total Components: 9
  Supported: 8 (88.9%)
  Unsupported: 1

CRITICAL GAPS (Blocking)
----------------------------------------
  - MistralAttention with sliding window: UNSUPPORTED
    Impact: HIGH - Core attention mechanism
```

**What this tells you:**
- 88.9% of layers use existing IRON operators (AIEGEMM, AIERMSNorm, etc.)
- **MistralAttention** needs a custom operator due to sliding window

---

## Step 2: Generate Operator Specification

Get detailed specs for the unsupported layer:

```bash
python -m iron.model_analysis spec mistralai/Mistral-7B-v0.1 \
    --layer MistralAttention \
    --output mistral_attention_spec.md
```

**What you get:**
- Input/output tensor shapes
- Hyperparameters (hidden_size, num_heads, sliding_window, etc.)
- Operations used (softmax, transpose, apply_rotary_pos_emb, etc.)
- Suggested IRON base class
- Reference implementation (Transformers source code)
- Special handling requirements

**Example spec highlights:**
```markdown
## Hyperparameters
| Name | Value | Description |
|------|-------|-------------|
| hidden_size | 4096 | Model dimension |
| num_attention_heads | 32 | QKV heads |
| num_key_value_heads | 8 | GQA KV heads |
| sliding_window | 4096 | Window size |

## Special Handling Required
- CRITICAL: Sliding window attention requires custom implementation
```

---

## Step 3: Generate Skeleton Code

Generate starter code with the `--skeleton` flag:

```bash
python -m iron.model_analysis spec mistralai/Mistral-7B-v0.1 \
    --layer MistralAttention \
    --skeleton operators/mistral_attention.py
```

**Generated skeleton:**
```python
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""
Sliding Window Attention for Mistral

Generated skeleton for: AIESlidingWindowAttention
"""

from iron.common import AIEOperatorBase, AIEContext
from iron.common.compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from pathlib import Path


class AIESlidingWindowAttention(AIEOperatorBase):
    """
    Sliding window attention for models like Mistral.

    TODO: Implement the following methods:
    - set_up_artifacts
    - set_up_runtime
    - forward
    - _apply_sliding_mask
    """

    def __init__(
        self,
        hidden_size: int = 4096,
        num_heads: int = 32,
        num_kv_heads: int = 8,
        head_dim: int = 128,
        sliding_window: int = 4096,
        context=None,
    ):
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.num_kv_heads = num_kv_heads
        self.head_dim = head_dim
        self.sliding_window = sliding_window
        super().__init__(context=context)

    def set_up_artifacts(self):
        """Set up compilation artifacts."""
        operator_dir = Path(__file__).parent

        # TODO: Define MLIR generation
        pass

    def set_up_runtime(self):
        """Set up runtime buffers and kernels."""
        # TODO: Define buffers and kernel bindings
        pass

    def forward(self, hidden_states, attention_mask, position_embeddings):
        """
        Forward pass.

        Args:
            hidden_states: [batch, seq_len, hidden_size]
            attention_mask: Optional attention mask
            position_embeddings: (cos, sin) for RoPE

        Returns:
            Output tensor [batch, seq_len, hidden_size]
        """
        # TODO: Implement sliding window attention
        return hidden_states
```

---

## Step 4: Implement the AIE Logic

Fill in the TODO sections. Here's what each method needs:

### 4a. set_up_artifacts()

Define the MLIR generation and compilation dependencies:

```python
def set_up_artifacts(self):
    """Set up compilation artifacts for sliding window attention."""
    operator_dir = Path(__file__).parent

    # Create MLIR artifact
    self.mlir_artifact = PythonGeneratedMLIRArtifact.new(
        "sliding_window_attention.mlir",
        import_path=operator_dir / "design.py",
        callback_fn="generate_mlir",
        callback_kwargs={
            "num_heads": self.num_heads,
            "num_kv_heads": self.num_kv_heads,
            "head_dim": self.head_dim,
            "sliding_window": self.sliding_window,
        },
    )

    # Create compilation artifacts
    self.xclbin_artifact = XclbinArtifact.new(
        "sliding_window_attention.xclbin",
        mlir_artifact=self.mlir_artifact,
    )

    self.insts_bin_artifact = InstsBinArtifact.new(
        "sliding_window_attention.insts.bin",
        xclbin_artifact=self.xclbin_artifact,
    )

    self.kernel_obj_artifact = KernelObjectArtifact.new(
        "sliding_window_attention.o",
        xclbin_artifact=self.xclbin_artifact,
    )

    self.kra_artifact = KernelArchiveArtifact.new(
        "sliding_window_attention.kra",
        kernel_obj_artifacts=[self.kernel_obj_artifact],
    )
```

### 4b. set_up_runtime()

Define buffers and kernel bindings:

```python
def set_up_runtime(self):
    """Set up runtime buffers and kernels."""
    # Input/output buffers
    self.add_buffer("query", self.batch_size * self.seq_len * self.num_heads * self.head_dim)
    self.add_buffer("key", self.batch_size * self.seq_len * self.num_kv_heads * self.head_dim)
    self.add_buffer("value", self.batch_size * self.seq_len * self.num_kv_heads * self.head_dim)
    self.add_buffer("output", self.batch_size * self.seq_len * self.num_heads * self.head_dim)

    # Kernel for QKV projection
    self.add_kernel(
        "qkv_proj",
        input_buffers=["input"],
        output_buffers=["query", "key", "value"],
    )

    # Kernel for sliding window attention
    self.add_kernel(
        "sliding_window_attn",
        input_buffers=["query", "key", "value", "sliding_mask"],
        output_buffers=["output"],
    )

    # Build runlist
    self.add_to_runlist("qkv_proj", "input", "query", "key", "value")
    self.add_to_runlist("sliding_window_attn", "query", "key", "value", "output")
```

### 4c. forward()

Implement the actual computation:

```python
def forward(self, hidden_states, attention_mask=None, position_embeddings=None):
    """
    Sliding window attention forward pass.

    Args:
        hidden_states: [batch, seq_len, hidden_size]
        attention_mask: Optional attention mask
        position_embeddings: (cos, sin) for RoPE

    Returns:
        Output tensor [batch, seq_len, hidden_size]
    """
    batch_size, seq_len, _ = hidden_states.shape

    # Validate input
    if hidden_states.shape[-1] != self.hidden_size:
        raise ValueError(f"Expected hidden_size {self.hidden_size}, got {hidden_states.shape[-1]}")

    # Write input to buffer
    self.write_buffer("input", hidden_states)

    # Execute runlist
    self.run_runlist()

    # Read output
    output_shape = (batch_size, seq_len, self.num_heads * self.head_dim)
    result = self.read_buffer_as_torch("output", shape=output_shape)

    return result
```

### 4d. Create the MLIR Design (design.py)

```python
"""
MLIR generation for Sliding Window Attention
"""

from aie.iron import Kernel, ObjectFifo, Program, Buffer, Runtime
from aie.iron.placers import SequentialPlacer


def generate_mlir(num_heads, num_kv_heads, head_dim, sliding_window):
    """Generate MLIR for sliding window attention."""

    # Define device type
    device_type = aie.device.XC35

    # Create runtime
    rt = Runtime()

    # Define memory maps
    ShimDMA = aie.get_tile_type(aie.TileType.SHIM_DMA)

    # Input/Output buffers
    with rt.sequence(aie_dtype.s16, "in", "out") as (win, wout):
        # Load tiles for processing
        ...

    # Create program
    program = Program(device_type, rt)

    # Place with sequential placer
    module = program.resolve_program(SequentialPlacer())

    return module
```

---

## Step 5: Register the Operator

Use the decorator to register your custom operator:

```python
from iron.model_analysis import OperatorRegistry

@OperatorRegistry.register("mistral_sliding_window_attention")
class AIESlidingWindowAttention(AIEOperatorBase):
    # ... implementation ...
    pass
```

Or register architecture support:

```python
from iron.model_analysis import (
    register_architecture_support,
    ArchitectureSupport,
    SupportLevel,
)

register_architecture_support(
    ArchitectureSupport(
        architecture_name="MistralForCausalLM",
        model_types=["mistral"],
        support_level=SupportLevel.PARTIAL,  # Due to sliding window
        custom_operators=["mistral_sliding_window_attention"],
    )
)
```

---

## Step 6: Test Your Operator

Create a test to verify correctness:

```python
import torch
from transformers import AutoModelForCausalLM
from iron.operators.mistral_attention import AIESlidingWindowAttention

def test_mistral_attention():
    """Test sliding window attention against Transformers reference."""

    # Load reference model
    ref_model = AutoModelForCausalLM.from_pretrained(
        "mistralai/Mistral-7B-v0.1",
        torch_dtype=torch.float16,
    )
    ref_layer = ref_model.model.layers[0].self_attn

    # Create NPU operator
    npu_op = AIESlidingWindowAttention(
        hidden_size=4096,
        num_heads=32,
        num_kv_heads=8,
        head_dim=128,
        sliding_window=4096,
    )
    npu_op.set_up_artifacts()
    npu_op.set_up_runtime()

    # Create test input
    batch_size = 1
    seq_len = 128
    hidden_states = torch.randn(batch_size, seq_len, 4096, dtype=torch.float16)

    # Get reference output
    with torch.no_grad():
        ref_output = ref_layer(hidden_states)

    # Get NPU output
    npu_output = npu_op(hidden_states)

    # Compare
    max_diff = (ref_output[0] - npu_output).abs().max()
    print(f"Max difference: {max_diff}")

    assert max_diff < 0.01, f"Output mismatch: {max_diff}"
    print("Test PASSED!")
```

---

## Quick Reference

### Common Operator Templates

| Layer Type | Template | Base Class |
|------------|----------|------------|
| Attention (standard) | `attention` | AIEGEMM |
| Attention (sliding window) | `sliding_window_attention` | AIEOperatorBase |
| Attention (QK norm) | `attention_qk_norm` | AIEGEMM + AIERMSNorm |
| MoE | `moe_layer` | AIEOperatorBase |
| MLP/FFN | `mlp` | AIEGEMM |
| Normalization | `norm` | AIERMSNorm |
| RoPE | `rope` | AIERoPE |

### CLI Commands

```bash
# Quick compatibility check
python -m iron.model_analysis check <model>

# Scan architecture
python -m iron.model_analysis scan <model> -o scan.json

# Gap analysis
python -m iron.model_analysis analyze <model> -o report.json

# Generate operator spec
python -m iron.model_analysis spec <model> --layer <LayerName> -o spec.md

# Generate operator skeleton
python -m iron.model_analysis spec <model> --layer <LayerName> --skeleton op.py
```

---

## Tips for Success

1. **Start with the spec**: Always run `spec` first to understand exactly what the layer does.

2. **Study the reference**: The Transformers source code in the spec is your ground truth.

3. **Use existing operators as examples**: Look at how similar operators are implemented in IRON.

4. **Test incrementally**: Verify each method (set_up_artifacts, set_up_runtime, forward) separately.

5. **Mind the shapes**: Tensor shapes and memory layout are critical for NPU operators.

6. **Consider tiling**: Large tensors may need to be tiled for NPU memory constraints.

---

## Example: Full Operator Implementation

See `iron/operators/` for complete examples:
- `sliding_window_attention.py` - Mistral-style attention
- `moe_layer.py` - Mixture of Experts
- `qk_norm_attention.py` - Attention with QK normalization

---

## License

Apache 2.0
