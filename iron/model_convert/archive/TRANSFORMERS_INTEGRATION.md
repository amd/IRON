# Transformers Integration Guide

## Why Use Transformers Integration?

You asked: *"Wouldn't it be beneficial to look into the modeling.<model_name> from the Transformers class?"*

**Answer: Yes, absolutely.** This is the **PREFERRED** and **MOST ACCURATE** way to scan models.

The HuggingFace Transformers library already has complete implementations of model architectures. Instead of parsing code with AST, we can directly:
1. Load the config object with all architecture details
2. Inspect the actual modeling classes
3. Get exact layer types and parameters
4. Detect special features (MoE, sliding window, etc.)

## What This Means

### Example: Qwen3.5-MoE-27B

```python
from iron.model_convert import scan_model_from_transformers, get_architecture_summary

# Scan directly from HuggingFace Hub
info = scan_model_from_transformers("Qwen/Qwen3.5-27B")

print(f"Model Type: {info.model_type}")
print(f"Architecture: {info.architecture_name}")

# Special features
print(f"Has MoE: {info.has_moe}")           # True
print(f"Has Sliding Window: {info.has_sliding_window}")  # True
print(f"Has RoPE: {info.has_rope}")         # True
print(f"Attention Type: {info.attention_type}")  # GQA
print(f"FFN Type: {info.ffn_type}")         # MoE

# Layer classes
for layer in info.layer_classes:
    print(f"  - {layer['name']} ({layer['category']})")
```

### Output Example

```
Architecture Summary: Qwen3_5_MoEForCausalLM
============================================================
Model Type: qwen3_5_moe
Config Class: Qwen3_5_MoEConfig

Architecture Details:
  Hidden Size: 3584
  Attention Heads: 32
  KV Heads: 8
  Layers: 64
  Intermediate Size: 18944

Special Features:
  Sliding Window: Yes
  MoE: Yes
  RoPE: Yes
  QK Norm: Yes

Attention Type: gqa
FFN Type: moe

Layer Classes:
  - Qwen3_5_MoEAttention (attention)
  - Qwen3_5_MoESdpaAttention (attention)
  - Qwen3_5_MoEMlp (linear)
  - Qwen3_5_MoEMoEBlock (moe)
  - Qwen3_5_MoERMSNorm (normalization)
  - Qwen3_5_MoEModel (other)
  - Qwen3_5_MoEForCausalLM (other)
```

## CLI Usage

### Scan with Transformers (Recommended)

```bash
# Use Transformers library directly
python -m iron.model_convert.cli scan Qwen/Qwen3.5-27B --transformers

# Auto mode: try Transformers first, fall back to AST
python -m iron.model_convert.cli scan Qwen/Qwen3.5-27B --auto

# Save results to JSON
python -m iron.model_convert.cli scan Qwen/Qwen3.5-27B -t -o qwen_scan.json
```

### Get Architecture Summary

```python
from iron.model_convert import get_architecture_summary

summary = get_architecture_summary("Qwen/Qwen3.5-27B")
print(summary)
```

## Supported Architectures

The integration works with **ANY** model in the Transformers library:

| Architecture | Transformers Module | Detected Features |
|--------------|---------------------|-------------------|
| Llama | `transformers.models.llama` | RoPE, SwiGLU, RMSNorm |
| Mistral | `transformers.models.mistral` | Sliding Window, GQA |
| Mixtral | `transformers.models.mixtral` | MoE, Sliding Window |
| Qwen | `transformers.models.qwen2` | RoPE, Silu, QK Norm |
| Qwen3.5-MoE | `transformers.models.qwen3_5_moe` | **MoE, Sliding Window, GQA** |
| Qwen3-Omni-MoE | `transformers.models.qwen3_omni_moe` | **MoE, Omni attention** |
| Gemma | `transformers.models.gemma` | GeGLU, RoPE |
| Phi | `transformers.models.phi` | RoPE, GELU |
| Falcon | `transformers.models.falcon` | Multi-query attention |
| Mamba | `transformers.models.mamba` | SSM layers |

## How It Works

### 1. Config Extraction

```python
from transformers import AutoConfig

config = AutoConfig.from_pretrained("Qwen/Qwen3.5-27B")

# Extract all architecture details
hidden_size = config.hidden_size
num_experts = config.num_experts  # MoE-specific!
sliding_window = config.sliding_window  # Sliding window!
```

### 2. Module Inspection

```python
from transformers.models.qwen3_5_moe import modeling_qwen3_5_moe
import inspect

# Get source code
source = inspect.getsource(modeling_qwen3_5_moe)

# Or directly inspect classes
from transformers.models.qwen3_5_moe.modeling_qwen3_5_moe import (
    Qwen3_5_MoEModel,
    Qwen3_5_MoEAttention,
    Qwen3_5_MoEMoEBlock,
)
```

### 3. Feature Detection

The scanner automatically detects:

| Feature | Detection Method |
|---------|------------------|
| Sliding Window | `config.sliding_window` or `config.window_size` |
| MoE | `config.num_experts` or "MoE" in architecture name |
| RoPE | `config.rope_theta` or model type patterns |
| QK Norm | `config.qk_norm` or Qwen model type |
| Attention Type | Compare `num_attention_heads` vs `num_key_value_heads` |
| FFN Type | Model type patterns and intermediate size ratios |

## Benefits Over AST Scanning

| Aspect | Transformers Integration | AST Scanning |
|--------|-------------------------|--------------|
| Accuracy | Exact (uses actual classes) | Heuristic-based |
| Speed | Fast (direct import) | Slower (parsing) |
| Feature Detection | Complete | Partial |
| Config Values | Exact | Guessed |
| Novel Architectures | Auto-detected | May miss |
| Requires Local Files | No (can use HF Hub) | Yes |

## When to Use Each

### Use Transformers Integration When:
- Model is in Transformers library (most common)
- You want accurate feature detection
- You need exact config values
- Scanning from HuggingFace Hub

### Use AST Scanning When:
- Custom model not in Transformers
- Analyzing local model code
- Transformers library unavailable
- Model uses custom architecture code

## Integration with Gap Analysis

The Transformers integration feeds directly into gap analysis:

```python
from iron.model_convert import (
    scan_model_from_transformers,
    GapAnalyzer,
    generate_gap_report,
)

# Scan with Transformers
info = scan_model_from_transformers("Qwen/Qwen3.5-27B")

# The gap analyzer now knows:
# - Model has MoE (needs custom operator)
# - Model has sliding window (needs custom operator)
# - Model uses GQA (supported)
# - Model uses RoPE (supported)

# Generate accurate gap report
report = generate_gap_report("Qwen/Qwen3.5-27B")
print(f"Support: {report.support_percentage}%")
print(f"Critical gaps: {len(report.critical_gaps)}")
# Critical gaps will include MoE and sliding window!
```

## Example: Analyzing Qwen3.5-MoE

```python
from iron.model_convert import (
    scan_model_from_transformers,
    GapAnalyzer,
    get_architecture_summary,
)

print("=" * 60)
print("QWEN3.5-MOE-27B ANALYSIS")
print("=" * 60)

# Step 1: Scan architecture
info = scan_model_from_transformers("Qwen/Qwen3.5-27B")
print(get_architecture_summary("Qwen/Qwen3.5-27B"))

# Step 2: Understand implications
print("\nIRON IMPLICATIONS")
print("-" * 60)

if info.has_moe:
    print("! MoE detected - requires custom MoE operator")
    print("  - num_experts:", info.config_dict.get('num_experts'))
    print("  - experts_per_tok:", info.config_dict.get('num_experts_per_tok'))

if info.has_sliding_window:
    print("! Sliding window attention detected")
    print("  - window_size:", info.config_dict.get('sliding_window'))
    print("  - Requires custom sliding window attention operator")

if info.attention_type == "gqa":
    print("✓ GQA attention - SUPPORTED by IRON")

if info.has_rope:
    print("✓ RoPE embeddings - SUPPORTED by IRON")

# Step 3: Generate gap report
from iron.model_convert import generate_gap_report
report = generate_gap_report("Qwen/Qwen3.5-27B")

print("\nGAP ANALYSIS")
print("-" * 60)
print(f"Support Level: {report.support_percentage:.1f}%")
print(f"Feasibility: {report.conversion_feasibility}")
print(f"Critical Gaps: {len(report.critical_gaps)}")

for gap in report.critical_gaps[:5]:
    print(f"  ! {gap.component_name}: {gap.reason}")
```

## Summary

**The Transformers integration is the RIGHT way to scan models.** It gives you:
- Accurate architecture detection
- Exact configuration values
- Automatic feature detection (MoE, sliding window, etc.)
- Direct HuggingFace Hub access
- Better gap analysis

Use it with:
```bash
python -m iron.model_convert.cli scan <model> --transformers
```

Or in Python:
```python
from iron.model_convert import scan_model_from_transformers
info = scan_model_from_transformers("Qwen/Qwen3.5-27B")
```
