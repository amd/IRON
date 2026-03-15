# IRON Model Analysis

**Simple. Lovable. Complete.**

Cross-platform model analysis tools that work on Windows, macOS, and Linux - **NO AIE/MLIR dependencies required**.

## Quick Start

```python
from iron.model_analysis import scan_model, get_architecture_summary, quick_check

# Quick check
if quick_check("meta-llama/Llama-2-7b-hf"):
    print("Model is likely supported")

# Scan a model (uses Transformers library)
info = scan_model("Qwen/Qwen3.5-27B")
print(get_architecture_summary(info))

# Analyze compatibility
from iron.model_analysis import analyze_model
report = analyze_model("Qwen/Qwen3.5-27B")
print(f"Support: {report.support_percentage}%")
```

## CLI Usage

```bash
# Quick check
python -m iron.model_analysis check meta-llama/Llama-2-7b-hf

# Scan model architecture
python -m iron.model_analysis scan Qwen/Qwen3.5-27B -o scan.json

# Analyze compatibility (gap analysis)
python -m iron.model_analysis analyze Qwen/Qwen3.5-27B -o report.json

# Generate operator specification (for creating custom operators)
python -m iron.model_analysis spec mistralai/Mistral-7B-v0.1 \
    --layer MistralAttention \
    --output mistral_attn_spec.md \
    --skeleton mistral_attn.py
```

**What each command does:**
- `check` → Quick yes/no compatibility check
- `scan` → Shows WHAT the model has (architecture details)
- `analyze` → Shows WHAT IRON CAN/CAN'T DO (gaps, support %, action items)
- `spec` → Generates detailed spec for implementing a custom operator

## Creating Custom Operators

**Complete guide:** [`CREATING_OPERATORS.md`](CREATING_OPERATORS.md)

**Data sources reference:** [`DATA_SOURCES_GUIDE.md`](DATA_SOURCES_GUIDE.md)

The workflow for creating custom NPU operators:

```
1. ANALYZE    → python -m iron.model_analysis analyze <model>
2. SPEC       → python -m iron.model_analysis spec <model> --layer <LayerName>
3. SKELETON   → Add --skeleton operator_name.py to spec command
4. IMPLEMENT  → Fill in AIE logic (see DATA_SOURCES_GUIDE.md for complete data flow)
5. REGISTER   → Use @OperatorRegistry.register() decorator
6. TEST       → Verify against Transformers reference
```

## What This Does

| Feature | Description |
|---------|-------------|
| **Scan** | Analyze model architecture from HuggingFace Hub |
| **Detect** | Identify special features (MoE, sliding window, GQA, etc.) |
| **Compare** | Check what's supported vs unsupported by IRON |
| **Report** | Generate gap analysis with feasibility assessment |
| **Extend** | Generate skeleton code for custom operators |

## Why This Package?

### Problem
The full `iron.model_convert` package requires:
- Linux with AMD Ryzen AI NPU drivers
- mlir-aie (AIE compiler)
- AIE runtime

This makes it impossible to **analyze** models on Windows/macOS.

### Solution
`iron.model_analysis` separates the analysis tools from the conversion tools:
- ✅ Works on Windows, macOS, Linux
- ✅ No AIE dependencies
- ✅ Uses HuggingFace Transformers directly
- ✅ Accurate architecture detection

## Supported Models

Works with **ANY** model in HuggingFace Transformers:

- Llama / Llama-2 / Llama-3 / Llama-3.2
- Mistral / Mixtral
- Qwen / Qwen2 / Qwen3.5 / Qwen3.5-MoE
- Gemma / Gemma2
- Phi / Phi-2 / Phi-3
- Falcon
- Mamba
- And more...

## What Detected

| Feature | Detection |
|---------|-----------|
| **Attention Type** | MHA, GQA, MQA |
| **Sliding Window** | Window size detection |
| **MoE** | Expert count, experts per token |
| **RoPE** | RoPE theta, scaling |
| **Normalization** | RMSNorm, LayerNorm, QK Norm |
| **FFN Type** | SwiGLU, GeGLU, SilU, GELU, MoE |

## Example Output

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
  Num Experts: 128
  Experts Per Token: 8

Special Features:
  Sliding Window: Yes (window=4096)
  MoE: Yes
  RoPE: Yes (theta=1000000)
  QK Norm: Yes

Attention Type: gqa
FFN Type: moe
```

## Package Structure

```
iron/model_analysis/
├── __init__.py              # Main exports
├── __main__.py              # CLI entry point
├── transformers_integration.py  # HF Transformers scanning (PREFERRED)
├── architecture_scanner.py  # AST scanning (fallback)
├── capability_registry.py   # Support tracking
├── gap_analyzer.py          # Gap analysis
├── operator_spec.py         # Operator specification generator
├── extensibility.py         # Plugin system
├── README.md                # This file
├── CREATING_OPERATORS.md    # Guide for creating custom operators
└── DATA_SOURCES_GUIDE.md    # Complete data extraction reference
```

## Relationship to model_convert

```
iron/model_analysis/          iron/model_convert/
- Analysis only               - Full conversion
- No AIE deps                 - Requires AIE/MLIR
- Works everywhere            - Linux (NPU) only
- Scan & Report               - Convert & Run
```

**Workflow:**
1. Use `model_analysis` on Windows/macOS to analyze models
2. Identify gaps and requirements
3. For unsupported layers, generate specs with `spec` command
4. Implement custom operators (see CREATING_OPERATORS.md)
5. Move to Linux with NPU for actual conversion using `model_convert`

## SLC Principles

### Simple
- Focused scope: analysis only
- Clean API: 3 main functions
- Preferred method: Transformers integration

### Lovable
- Works on your machine (Windows, macOS, or Linux)
- Fast: Direct HF library access
- Accurate: Uses actual model configs

### Complete
- Full architecture detection
- Gap analysis with feasibility
- Operator skeleton generation
- Extensibility framework

## License

Apache 2.0
