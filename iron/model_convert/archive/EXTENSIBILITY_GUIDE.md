# Gap Analysis and Extensibility Guide

This guide covers the **gap analysis** and **extensibility** features of the IRON Model Converter, which enable you to:
- Analyze new model architectures for NPU compatibility
- Identify unsupported components and their impact
- Extend IRON with custom operators
- Register new architecture handlers

## Table of Contents

1. [Architecture Scanning](#architecture-scanning)
2. [Gap Analysis](#gap-analysis)
3. [Extensibility Framework](#extensibility-framework)
4. [Custom Operator Implementation](#custom-operator-implementation)
5. [Architecture Handlers](#architecture-handlers)

---

## Architecture Scanning

The `ArchitectureScanner` analyzes a model's code to understand what layers and operations it uses.

### Basic Scanning

```python
from iron.model_convert import ArchitectureScanner, get_model_info_summary

# Scan a model
scanner = ArchitectureScanner("path/to/model")
requirements = scanner.scan()

# Print summary
print(get_model_info_summary(requirements))
```

### What Gets Scanned

The scanner analyzes:
- `config.json` - Model configuration and hyperparameters
- `modeling_*.py` - Model architecture code using AST parsing
- Layer classes and their inheritance patterns
- Attention mechanisms (MHA, GQA, MQA)
- Feed-forward network types (SwiGLU, GeGLU, MLP)
- Normalization layers (RMSNorm, LayerNorm)
- Positional embeddings (RoPE, ALiBi, learned)

### LayerInfo Structure

Each discovered layer is represented as a `LayerInfo` object:

```python
@dataclass
class LayerInfo:
    name: str                    # Layer name (e.g., "LlamaAttention")
    module_path: str             # Full module path
    category: LayerCategory      # Category (ATTENTION, NORMALIZATION, etc.)
    is_supported: bool           # Whether IRON supports it
    parameters: Dict[str, Any]   # Layer parameters
```

---

## Gap Analysis

The `GapAnalyzer` compares model requirements against IRON capabilities to identify what's missing.

### Quick Check

For a quick assessment of whether a model is likely supported:

```python
from iron.model_convert import quick_check

is_supported = quick_check("meta-llama/Llama-2-7b-hf")
print(f"Supported: {is_supported}")
```

### Detailed Gap Report

```python
from iron.model_convert import generate_gap_report

report = generate_gap_report("path/to/model")

# Access report data
print(f"Support Level: {report.support_percentage:.1f}%")
print(f"Feasibility: {report.conversion_feasibility}")
print(f"Total Components: {report.total_components}")
print(f"Supported: {report.supported_components}")
print(f"Unsupported: {report.unsupported_components}")
```

### Human-Readable Summary

```python
from iron.model_convert import print_gap_summary

summary = print_gap_summary("path/to/model")
print(summary)
```

### Example Output

```
============================================================
GAP ANALYSIS REPORT: Qwen3.5-27B
============================================================

SUMMARY
----------------------------------------
  Model Type: qwen3.5
  Total Components: 12
  Supported: 9 (75.0%)
  Unsupported: 3
  Feasibility: challenging

CRITICAL GAPS (Blocking)
----------------------------------------
  ! SlidingWindowAttention: sliding window not supported
    Impact: high, Effort: high
  ! MoEGate: MoE routing not yet supported
    Impact: high, Effort: high

MODERATE GAPS (Performance Impact)
----------------------------------------
  ~ QwenRMSNorm: Use cpu_fallback fallback

RECOMMENDED APPROACH
----------------------------------------
  Implement custom NPU operators for: SlidingWindowAttention, MoEGate
  Priority: 3 custom components needed

ACTION ITEMS
----------------------------------------
=== CRITICAL (Blocking Conversion) ===
  - Implement NPU operator for SlidingWindowAttention
  - Implement NPU operator for MoEGate
=== MODERATE (Performance Impact) ===
  - Use cpu_fallback fallback for QwenRMSNorm
=== GENERAL ===
  - Support level: 75.0%
  - Feasibility: challenging
```

### Comparing Multiple Models

```python
from iron.model_convert import GapAnalyzer, ArchitectureScanner

models = ["Llama-2-7b", "Mistral-7B", "Gemma-7B"]
scanners = [ArchitectureScanner(m) for m in models]
requirements_list = [s.scan() for s in scanners]

analyzer = GapAnalyzer()
comparison = analyzer.compare_models(requirements_list)

print("Support Percentages:")
for model, pct in comparison.support_percentages.items():
    print(f"  {model}: {pct:.1f}%")

print("\nCommon Gaps:")
for gap in comparison.common_gaps:
    print(f"  - {gap}")
```

---

## Extensibility Framework

The extensibility framework allows you to add support for new operators and architectures without modifying core IRON code.

### Registering a Custom Operator (Quick)

For simple cases where you just need to mark an operator as supported:

```python
from iron.model_convert import quick_register_operator

quick_register_operator(
    name="CustomAttention",
    module_patterns=[
        "mymodel.modeling.CustomAttention",
        "mymodel.layers.Attention",
    ],
    category="attention",
    support_level="partial",  # or "full", "fallback", "unsupported"
)
```

### Registering an Architecture (Quick)

```python
from iron.model_convert import quick_register_architecture

quick_register_architecture(
    name="MyModel",
    model_types=["my_model", "my_custom_arch"],
    supported_layers=["RMSNorm", "GEMM", "Attention"],
)
```

---

## Custom Operator Implementation

For operators that need full NPU implementations, use the extensibility framework.

### Using Operator Templates

Pre-built templates are available for common custom operators:

```python
from iron.model_convert import get_operator_template, TEMPLATES

# List available templates
print("Available templates:")
for name in TEMPLATES.keys():
    print(f"  - {name}")

# Get a template
template = get_operator_template("sliding_window_attention")
print(f"Template: {template.name}")
print(f"Required methods: {template.required_methods}")
```

### Generating Operator Skeleton

```python
from iron.model_convert import generate_operator_skeleton

# Generate skeleton file
skeleton_path = generate_operator_skeleton(
    operator_name="SlidingWindowAttention",
    output_path="./extensions/sliding_window_attention.py",
)
print(f"Generated: {skeleton_path}")
```

This creates a file with:
- Class structure inheriting from `AIEOperatorBase`
- Stub methods for `set_up_artifacts()`, `set_up_runtime()`, and `forward()`
- Example MLIR generation template
- Comments guiding implementation

### Implementing a Custom Operator

Here's a complete example:

```python
# extensions/sliding_window_attention.py
from iron.common import AIEOperatorBase, AIEContext
from iron.common.compilation import (
    PythonGeneratedMLIRArtifact,
    XclbinArtifact,
)
from pathlib import Path


class AIESlidingWindowAttention(AIEOperatorBase):
    """
    Sliding Window Attention for models like Mistral.

    Implements attention with a local window instead of full attention.
    """

    def __init__(
        self,
        window_size: int,
        num_heads: int,
        head_dim: int,
        context=None,
    ):
        self.window_size = window_size
        self.num_heads = num_heads
        self.head_dim = head_dim
        super().__init__(context=context)

    def set_up_artifacts(self):
        """Set up compilation artifacts."""
        operator_dir = Path(__file__).parent

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"sliding_window_attention.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="generate_mlir",
            callback_kwargs={
                "window_size": self.window_size,
                "num_heads": self.num_heads,
                "head_dim": self.head_dim,
            },
        )
        self.set_compilation_artifacts([mlir_artifact])

    def set_up_runtime(self):
        """Set up runtime buffers and kernels."""
        # Define buffers
        self.add_buffer("query", self.num_heads * self.head_dim)
        self.add_buffer("key", self.num_heads * self.head_dim)
        self.add_buffer("value", self.num_heads * self.head_dim)
        self.add_buffer("output", self.num_heads * self.head_dim)

        # Add kernel
        self.add_kernel(
            "sliding_window_attention",
            inputs=["query", "key", "value"],
            outputs=["output"],
        )

    def forward(self, q, k, v):
        """
        Forward pass with sliding window attention.

        Args:
            q: Query tensor (batch, seq_len, hidden)
            k: Key tensor (batch, seq_len, hidden)
            v: Value tensor (batch, seq_len, hidden)

        Returns:
            Output tensor (batch, seq_len, hidden)
        """
        # Validate input
        if len(q.shape) < 2 or q.shape[-1] != self.num_heads * self.head_dim:
            raise ValueError(f"Incompatible input shape: {q.shape}")

        # Execute on NPU
        self.write_buffer("query", q)
        self.write_buffer("key", k)
        self.write_buffer("value", v)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=q.shape)
        return result
```

### MLIR Generation (design.py)

```python
# extensions/design.py
from aie.iron import Kernel, ObjectFifo, Program, Buffer, Runtime
from aie.iron.placers import SequentialPlacer


def generate_mlir(window_size, num_heads, head_dim, **kwargs):
    """Generate MLIR for sliding window attention."""

    # Define runtime
    rt = Runtime()

    # Define sequence for sliding window attention
    with rt.sequence(...) as (...):
        # Implement sliding window attention logic
        # ...
        pass

    # Create program
    program = Program(device_type, rt)
    module = program.resolve_program(SequentialPlacer())
    return module
```

### Auto-Loading Extensions

```python
from iron.model_convert import ExtensionLoader

# Create loader with search paths
loader = ExtensionLoader(
    search_paths=["./extensions", "./custom_operators"]
)

# Load all extensions
results = loader.load_all()
print(f"Loaded operators: {results['operators']}")
print(f"Loaded handlers: {results['handlers']}")
```

---

## Architecture Handlers

For models with architecture-specific quirks, you can register custom handlers.

### Creating an Architecture Handler

```python
from iron.model_convert import ArchitectureHandler, ArchitectureRegistry

# Create handler
handler = ArchitectureHandler(
    architecture_name="CustomModel",
    model_types=["custom_model", "my_arch"],
    layer_mappings={
        "CustomAttention": "attention",
        "CustomNorm": "normalization",
        "CustomFFN": "linear",
    },
    custom_handlers={
        "special_layer": lambda layer: handle_special_layer(layer),
    },
    default_config={
        "use_custom_kernel": True,
        "optimization_level": "O3",
    },
)

# Register
ArchitectureRegistry.register_handler(handler)
```

### Using Architecture Handlers

```python
from iron.model_convert import ArchitectureRegistry

handler = ArchitectureRegistry.get_handler("custom_model")
if handler:
    print(f"Found handler for: {handler.architecture_name}")
    print(f"Layer mappings: {handler.layer_mappings}")
```

---

## Extension Points

Extension points allow you to hook into the conversion pipeline at key moments.

### Available Extension Points

- `before_conversion` - Before starting model conversion
- `after_weight_load` - After weights are loaded
- `before_compile` - Before artifact compilation
- `after_convert` - After conversion is complete

### Registering a Hook

```python
from iron.model_convert import register_extension_point, invoke_extension_point


def my_pre_conversion_hook(requirements):
    """Custom logic before conversion."""
    print(f"Converting {requirements.model_name}...")

    # Modify settings, log, validate, etc.
    return {
        "custom_config": {"optimization": "O3"},
    }


register_extension_point("before_conversion", my_pre_conversion_hook)
```

---

## Complete Workflow Example

Here's a complete example of analyzing and extending support for a new model:

```python
from iron.model_convert import (
    ArchitectureScanner,
    GapAnalyzer,
    generate_gap_report,
    quick_register_operator,
    generate_operator_skeleton,
    ExtensionLoader,
)

# Step 1: Scan the new model
model_path = "path/to/Qwen3.5-27B"
scanner = ArchitectureScanner(model_path)
requirements = scanner.scan()

# Step 2: Analyze gaps
report = generate_gap_report(model_path)
print(f"Support Level: {report.support_percentage:.1f}%")
print(f"Feasibility: {report.conversion_feasibility}")

# Step 3: Review critical gaps
print("\nCritical Gaps:")
for gap in report.critical_gaps:
    print(f"  - {gap.component_name}: {gap.reason}")

# Step 4: Register quick fallbacks for minor components
quick_register_operator(
    name="QwenRMSNorm",
    module_patterns=["Qwen.modeling.QwenRMSNorm"],
    category="normalization",
    support_level="fallback",
)

# Step 5: Generate skeleton for major missing operators
if report.critical_gaps:
    for gap in report.critical_gaps[:2]:
        skeleton_path = generate_operator_skeleton(
            operator_name=gap.component_name,
            output_path=f"./extensions/{gap.component_name.lower()}.py",
        )
        print(f"Generated skeleton: {skeleton_path}")

# Step 6: Load extensions
loader = ExtensionLoader(search_paths=["./extensions"])
results = loader.load_all()
print(f"\nLoaded extensions: {results['operators']}")

# Step 7: Re-analyze after extensions
report = generate_gap_report(model_path)
print(f"\nUpdated Support Level: {report.support_percentage:.1f}%")
```

---

## Best Practices

### For Adding New Operators

1. **Check if fallback is acceptable**: For minor components, CPU fallback may be sufficient
2. **Use templates**: Start from existing templates when available
3. **Implement incrementally**: Get a basic version working, then optimize
4. **Test thoroughly**: Verify numerical correctness against reference implementation

### For Architecture Handlers

1. **Map all layers**: Ensure all layer types have mappings
2. **Handle special cases**: Document any architecture-specific quirks
3. **Provide defaults**: Include sensible default configurations

### For Extension Points

1. **Keep hooks lightweight**: Extension points should be fast
2. **Return dicts**: Extension hooks should return dictionaries for merging
3. **Handle errors gracefully**: Failed hooks shouldn't break conversion

---

## Troubleshooting

### "No matching NPU operator available"

This means the operator isn't in the capability registry. Options:
1. Use `quick_register_operator()` to mark as fallback
2. Use `generate_operator_skeleton()` to create implementation
3. Check if it's a known unsupported category

### "Custom implementation needed"

The operator requires a full NPU implementation. Use the extensibility framework to create it.

### Gap analysis shows 0% support

Verify the model path is correct and `modeling_*.py` files are present for AST analysis.

---

## License

Apache 2.0 - See LICENSE file in the root directory.
