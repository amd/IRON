# IRON Model Tools

**SLC: Simple. Lovable. Complete.**

Two packages for model conversion workflow:

| Package | Platform | Purpose |
|---------|----------|---------|
| `iron.model_analysis` | Windows, macOS, Linux | **Analysis** - Scan models, detect features, gap analysis |
| `iron.model_convert` | Linux (NPU only) | **Conversion** - Full model conversion to NPU format |

---

## Quick Start

### Step 1: Analyze (Any Platform)

```python
from iron.model_analysis import scan_model, analyze_model, quick_check

# Quick check
if quick_check("meta-llama/Llama-2-7b-hf"):
    print("Model is likely supported")

# Scan architecture
info = scan_model("Qwen/Qwen3.5-27B")
print(f"MoE: {info.has_moe}, Sliding Window: {info.has_sliding_window}")

# Gap analysis
report = analyze_model("Qwen/Qwen3.5-27B")
print(f"Support: {report.support_percentage}%")
```

**CLI:**
```bash
python -m iron.model_analysis check Qwen/Qwen3.5-27B
python -m iron.model_analysis scan Qwen/Qwen3.5-27B -o scan.json
python -m iron.model_analysis analyze Qwen/Qwen3.5-27B -o report.json
```

### Step 2: Convert (Linux with NPU)

```python
from iron.model_convert import HuggingFaceConverter

converter = HuggingFaceConverter("meta-llama/Llama-2-7b-hf")
model = converter.create_npu_model(compile_artifacts=True)
```

**CLI:**
```bash
python -m iron.model_convert.cli convert meta-llama/Llama-2-7b-hf -o ./iron_model --compile
```

---

## Package Structure

```
iron/
├── model_analysis/          # Cross-platform analysis (NO AIE deps)
│   ├── __init__.py          # Main exports
│   ├── __main__.py          # CLI entry point
│   ├── transformers_integration.py  # HF Transformers scanning
│   ├── architecture_scanner.py      # AST fallback scanning
│   ├── capability_registry.py       # Support tracking
│   ├── gap_analyzer.py              # Gap analysis
│   ├── extensibility.py             # Plugin system
│   └── README.md
│
└── model_convert/           # Linux NPU conversion (REQUIRES AIE)
    ├── __init__.py          # Main exports
    ├── __main__.py          # Module entry point
    ├── cli.py               # Full conversion CLI
    ├── converter.py         # HuggingFaceConverter
    ├── config_adapter.py    # Config parsing
    ├── weight_mapper.py     # Weight transformation
    ├── shape_manager.py     # Shape/tiling management
    ├── operator_factory.py  # Operator creation (AIE)
    ├── layer_builder.py     # Layer building (AIE)
    ├── model_assembler.py   # Model assembly (AIE)
    ├── architecture_scanner.py      # Also available here
    ├── capability_registry.py       # Also available here
    ├── gap_analyzer.py              # Also available here
    ├── extensibility.py             # Also available here
    ├── transformers_integration.py  # Also available here
    ├── setup.py
    ├── usage_example.py
    ├── README.md
    └── archive/             # Deprecated files
```

---

## What Got Archived

The following files were moved to `model_convert/archive/` to reduce clutter:

| File | Reason |
|------|--------|
| `analysis.py` | Replaced by `model_analysis` package |
| `analyze_model.py` | Replaced by `model_analysis` CLI |
| `test_converter.py` | Didn't work without AIE |
| `IMPLEMENTATION_SUMMARY.md` | Internal dev doc |
| `PLATFORM_GUIDE.md` | Consolidated into this README |
| `EXTENSIBILITY_GUIDE.md` | Available in repo docs |
| `TRANSFORMERS_INTEGRATION.md` | Available in repo docs |

---

## Detected Features

The analysis tools automatically detect:

| Feature | Detection Method |
|---------|------------------|
| **Attention Type** | MHA, GQA, MQA (from head counts) |
| **Sliding Window** | `config.sliding_window` |
| **MoE** | `config.num_experts`, architecture name |
| **RoPE** | `config.rope_theta`, model patterns |
| **QK Norm** | `config.qk_norm`, model type |
| **FFN Type** | SwiGLU, GeGLU, SilU, GELU, MoE |
| **Normalization** | RMSNorm, LayerNorm, etc. |

---

## Example: Qwen3.5-MoE-27B Analysis

```python
from iron.model_analysis import scan_model, get_architecture_summary

info = scan_model("Qwen/Qwen3.5-27B")

print(get_architecture_summary(info))
```

**Output:**
```
Architecture Summary: Qwen3_5_MoEForCausalLM
============================================================
Model Type: qwen3_5_moe

Architecture Details:
  Hidden Size: 3584
  Attention Heads: 32
  KV Heads: 8
  Layers: 64
  Num Experts: 128
  Experts Per Token: 8

Special Features:
  Sliding Window: Yes
  MoE: Yes
  RoPE: Yes
  QK Norm: Yes

Attention Type: gqa
FFN Type: moe
```

**Implications for IRON:**
- ✓ GQA attention - SUPPORTED
- ✓ RoPE - SUPPORTED
- ✗ MoE - NEEDS CUSTOM OPERATOR
- ✗ Sliding Window - NEEDS CUSTOM OPERATOR

---

## Supported Models

Works with **ANY** model in HuggingFace Transformers:

| Architecture | Examples |
|--------------|----------|
| Llama | Llama-2, Llama-3, Llama-3.2 |
| Mistral | Mistral, Mixtral (MoE) |
| Qwen | Qwen, Qwen2, Qwen3.5, Qwen3.5-MoE |
| Gemma | Gemma, Gemma2 |
| Phi | Phi, Phi-2, Phi-3 |
| Other | Falcon, Mamba, StarCoder2 |

---

## License

Apache 2.0
