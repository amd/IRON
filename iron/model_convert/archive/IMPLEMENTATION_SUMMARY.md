# IRON Model Converter - Implementation Summary

## Overview

The IRON Model Converter (`iron.model_convert`) is a complete framework for converting HuggingFace models to run on AMD Ryzen AI NPUs. This document summarizes the implementation, with special focus on the **gap analysis** and **extensibility** features added to handle new model architectures.

---

## Motivation

The original IRON project supported a limited set of model architectures (Llama, Mistral, Phi, Gemma, Qwen) through hardcoded patterns. However, new model architectures are constantly being released (e.g., Qwen3.5-27B with novel features like MoE layers and sliding window attention).

The gap analysis and extensibility features were added to address:
1. **How do we know what a new model needs?** - Architecture Scanner
2. **How do we identify what's missing?** - Gap Analyzer
3. **How do we add support without modifying core code?** - Extensibility Framework

---

## Implementation Summary

### Core Converter Components (Original Request)

| File | Purpose | Key Classes |
|------|---------|-------------|
| `config_adapter.py` | Parse HF configs | `ConfigAdapter`, `NormalizedConfig`, `ModelArchitecture` |
| `weight_mapper.py` | Transform weights | `WeightMapper`, `QuantizedWeightMapper`, `WeightTransform` |
| `shape_manager.py` | NPU shape handling | `ShapeManager`, `TilingConfig`, `PaddedShape` |
| `operator_factory.py` | Create operators | `OperatorFactory`, `OperatorType`, `OperatorBuilder` |
| `layer_builder.py` | Build layers | `AttentionLayerBuilder`, `FeedForwardBuilder`, `TransformerBlockBuilder` |
| `model_assembler.py` | Assemble models | `ModelAssembler`, `ModelAssemblyConfig` |
| `converter.py` | Main API | `HuggingFaceConverter`, `ConversionConfig` |

### Gap Analysis Components (Added for New Architectures)

| File | Purpose | Key Classes/Functions |
|------|---------|----------------------|
| `architecture_scanner.py` | Scan model code | `ArchitectureScanner`, `ModelCodeAnalyzer`, `ArchitectureRequirements`, `LayerInfo` |
| `capability_registry.py` | Track support | `CapabilityRegistry`, `OperatorCapability`, `SupportLevel`, `FallbackStrategy` |
| `gap_analyzer.py` | Identify gaps | `GapAnalyzer`, `GapReport`, `GapItem`, `generate_gap_report`, `print_gap_summary` |

### Extensibility Components (Added for New Architectures)

| File | Purpose | Key Classes/Functions |
|------|---------|----------------------|
| `extensibility.py` | Plugin system | `CustomOperatorBase`, `OperatorRegistry`, `ArchitectureRegistry`, `ExtensionLoader`, `generate_operator_skeleton` |

---

## How It Works

### Workflow for New Model Architectures

```
┌─────────────────────────────────────────────────────────────────┐
│                    User Submits New Model                        │
│              (e.g., Qwen3.5-27B, Custom Model)                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. ArchitectureScanner - Analyzes model code using AST         │
│     - Parses config.json                                         │
│     - Scans modeling_*.py files                                  │
│     - Extracts ALL layer types and their parameters              │
│     - Outputs: ArchitectureRequirements                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. CapabilityRegistry - Checks what's supported                │
│     - Compares discovered layers vs known operators              │
│     - Applies pattern matching for variants                      │
│     - Determines support level (FULL/PARTIAL/FALLBACK/UNSUPPORTED)│
│     - Outputs: Support assessment per layer                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. GapAnalyzer - Identifies and categorizes gaps               │
│     - Groups gaps by impact (HIGH/MEDIUM/LOW)                    │
│     - Estimates effort to add support                            │
│     - Assesses overall conversion feasibility                    │
│     - Generates action items and recommendations                 │
│     - Outputs: GapReport                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. User Reviews Report                                          │
│     - If feasible: proceed with conversion                       │
│     - If challenging: implement custom operators                 │
│     - If not feasible: run on CPU or contribute operators        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. Extensibility Framework - Add missing support               │
│     - quick_register_operator() for simple cases                 │
│     - generate_operator_skeleton() for complex operators         │
│     - ExtensionLoader auto-discovers implementations             │
│     - Re-run gap analysis to verify support                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Design Decisions

### 1. AST-Based Code Analysis

Instead of just parsing `config.json`, the `ArchitectureScanner` uses Python's `ast` module to analyze the actual model code (`modeling_*.py`). This ensures:
- Discovery of custom layer classes even if not in config
- Understanding of inheritance patterns
- Extraction of layer-specific parameters

### 2. Pattern Matching for Support

The `CapabilityRegistry` uses pattern matching (regex) to determine if a layer is supported:
```python
LLAMA_PATTERNS = [".*LlamaAttention.*", ".*LlamaRMSNorm.*"]
```
This allows flexible matching across model variants without exact name matching.

### 3. Support Levels and Fallbacks

Four support levels provide granularity:
- **FULL**: Complete NPU support
- **PARTIAL**: NPU support with limitations
- **FALLBACK**: Use CPU/GPU fallback
- **UNSUPPORTED**: No implementation available

Fallback strategies:
- **CPU_FALLBACK**: Run on CPU
- **DECOMPOSE**: Break into simpler operations
- **APPROXIMATE**: Use approximate computation
- **CUSTOM_NEEDED**: Requires new implementation

### 4. Plugin Architecture

The extensibility framework uses:
- **Registries** for dynamic operator/handler registration
- **Extension points** for pipeline hooks
- **Auto-discovery** for loading extensions from directories

### 5. Skeleton Generation

The `generate_operator_skeleton()` function creates starter implementations with:
- Proper class structure
- Method stubs with docstrings
- Example MLIR generation template
- Comments guiding implementation

---

## File Structure

```
iron/model_convert/
├── __init__.py                    # Package exports (all classes)
├── README.md                      # Core converter documentation
├── EXTENSIBILITY_GUIDE.md         # Gap analysis & extensibility guide
├── usage_example.py               # Usage examples
│
├── config_adapter.py              # HF config parsing
├── weight_mapper.py               # Weight transformation
├── shape_manager.py               # NPU shape calculations
├── operator_factory.py            # NPU operator creation
├── layer_builder.py               # Layer construction
├── model_assembler.py             # Model orchestration
├── converter.py                   # Main converter API
│
├── architecture_scanner.py        # NEW: Model code analysis
├── capability_registry.py         # NEW: Support tracking
├── gap_analyzer.py                # NEW: Gap identification
└── extensibility.py               # NEW: Plugin system
```

---

## Usage Examples

### Quick Check
```python
from iron.model_convert import quick_check

if quick_check("meta-llama/Llama-2-7b-hf"):
    print("Model is likely supported")
else:
    print("Model needs review")
```

### Generate Gap Report
```python
from iron.model_convert import generate_gap_report

report = generate_gap_report("path/to/Qwen3.5-27B")
print(f"Support: {report.support_percentage:.1f}%")
print(f"Feasibility: {report.conversion_feasibility}")
```

### Register Custom Operator
```python
from iron.model_convert import quick_register_operator

quick_register_operator(
    name="CustomAttention",
    module_patterns=["mymodel.CustomAttention"],
    category="attention",
    support_level="partial",
)
```

### Generate Operator Skeleton
```python
from iron.model_convert import generate_operator_skeleton

skeleton = generate_operator_skeleton(
    operator_name="SlidingWindowAttention",
    output_path="./extensions/sliding_window.py",
)
```

---

## Testing Recommendations

To fully test the implementation:

1. **Architecture Scanner Test**
   ```python
   from iron.model_convert import ArchitectureScanner
   scanner = ArchitectureScanner("path/to/model")
   requirements = scanner.scan()
   ```

2. **Gap Analysis Test**
   ```python
   from iron.model_convert import GapAnalyzer
   analyzer = GapAnalyzer()
   report = analyzer.analyze(requirements)
   ```

3. **Extensibility Test**
   ```python
   from iron.model_convert import ExtensionLoader
   loader = ExtensionLoader(search_paths=["./extensions"])
   results = loader.load_all()
   ```

---

## Dependencies

The model converter depends on:
- `aie` (mlir-aie) - AMD's MLIR-AIE dialect for NPU operators
- `transformers` - HuggingFace transformers for model loading
- `torch` - PyTorch for tensor operations
- `safetensors` - For loading model weights

---

## Future Enhancements

Potential additions:
1. **GUI Tool**: Visual gap analysis dashboard
2. **Auto-decomposition**: Automatically decompose unsupported layers
3. **Performance estimation**: Predict NPU performance for new architectures
4. **Operator zoo**: Repository of community-contributed operators
5. **Automated testing**: CI/CD for verifying operator correctness

---

## License

Apache 2.0 - See LICENSE file in the root directory.
