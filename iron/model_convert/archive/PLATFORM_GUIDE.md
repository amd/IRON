# IRON Model Converter - Platform Guide

## Platform Compatibility

The IRON Model Converter has different capabilities depending on your platform:

### Windows / macOS (Cross-Platform)

**AVAILABLE** - Model Analysis Tools:
- `analyze_model.py` - Standalone model analysis
- Architecture scanning
- Gap analysis
- Capability registry
- Extensibility framework
- Operator skeleton generation

These tools do NOT require the AIE/MLIR dependencies and work on any platform with Python 3.8+.

**Usage Example (Windows/macOS):**
```bash
# Quick check
python iron/model_convert/analyze_model.py check meta-llama/Llama-2-7b-hf

# Scan model (requires local model files)
python iron/model_convert/analyze_model.py scan path/to/model -o report.json

# Generate detailed report
python iron/model_convert/analyze_model.py report path/to/model -o analysis.json
```

**NOT AVAILABLE on Windows/macOS:**
- Actual model conversion (requires AIE compiler)
- NPU operator execution (requires Linux NPU drivers)
- Artifact compilation (requires mlir-aie)

---

### Linux (with NPU Support)

**FULL FUNCTIONALITY** - All features available:
- Model analysis tools
- Full model conversion
- AIE operator compilation
- NPU execution

**Requirements:**
- AMD Ryzen AI NPU hardware
- Linux drivers for Ryzen AI
- mlir-aie package installed
- AIE compiler toolchain

**Usage Example (Linux):**
```bash
# Full conversion
python -m iron.model_convert.cli convert meta-llama/Llama-2-7b-hf -o ./iron_model --compile

# Or use the Python API
from iron.model_convert import HuggingFaceConverter

converter = HuggingFaceConverter("meta-llama/Llama-2-7b-hf")
model = converter.create_npu_model(compile_artifacts=True)
```

---

## Analysis Tools (Works Everywhere)

### Quick Check

```bash
python iron/model_convert/analyze_model.py check <model_name>
```

Examples:
```bash
python iron/model_convert/analyze_model.py check meta-llama/Llama-2-7b-hf
python iron/model_convert/analyze_model.py check mistralai/Mistral-7B-v0.1
```

### Scan Model Architecture

```bash
python iron/model_convert/analyze_model.py scan <model_path> -o <output.json>
```

This requires the model files to be downloaded locally.

### Generate Report

```bash
python iron/model_convert/analyze_model.py report <model_path> -o <report.json>
```

Generates a detailed feasibility report.

---

## Python API (Analysis Only on Windows/macOS)

```python
# This works cross-platform for analysis
from iron.model_convert.analysis import (
    quick_check,
    generate_gap_report,
    scan_model_architecture,
)

# Check if model is likely supported
if quick_check("meta-llama/Llama-2-7b-hf"):
    print("Model is likely supported")

# Generate gap report (requires local model files)
report = generate_gap_report("path/to/model")
print(f"Support: {report.support_percentage}%")
print(f"Feasibility: {report.conversion_feasibility}")
```

**Note:** On Windows/macOS, the analysis modules work but the actual conversion classes (`HuggingFaceConverter`, `ModelAssembler`, etc.) will fail to import because they depend on the `aie` module which is only available on Linux.

---

## Conversion Workflow

### On Windows/macOS (Analysis Only)

1. **Download model** from HuggingFace:
   ```bash
   huggingface-cli download meta-llama/Llama-2-7b-hf --local-dir ./Llama-2-7b
   ```

2. **Analyze compatibility**:
   ```bash
   python iron/model_convert/analyze_model.py report ./Llama-2-7b -o analysis.json
   ```

3. **Review report** to understand:
   - Support percentage
   - Unsupported components
   - Conversion feasibility

4. **Plan conversion** on Linux system

### On Linux (Full Conversion)

1. **Analyze** (same as above)

2. **Convert**:
   ```bash
   python -m iron.model_convert.cli convert meta-llama/Llama-2-7b-hf \
       -o ./iron_model \
       --compile
   ```

3. **Run on NPU**:
   ```bash
   python -m iron.model_convert.cli infer ./iron_model \
       --prompt "Once upon a time" \
       --max-tokens 100
   ```

---

## File Structure

```
iron/model_convert/
├── analysis.py              # Cross-platform analysis imports
├── analyze_model.py         # Standalone analysis tool (works everywhere)
├── architecture_scanner.py  # Model scanning (no AIE deps)
├── capability_registry.py   # Capability tracking (no AIE deps)
├── gap_analyzer.py          # Gap analysis (no AIE deps)
├── extensibility.py         # Plugin system (no AIE deps)
│
├── converter.py             # Full conversion (NEEDS AIE - Linux only)
├── model_assembler.py       # Model assembly (NEEDS AIE - Linux only)
├── operator_factory.py      # Operator creation (NEEDS AIE - Linux only)
├── layer_builder.py         # Layer building (NEEDS AIE - Linux only)
│
├── cli.py                   # CLI interface
├── __main__.py              # Module entry point
└── setup.py                 # Package setup
```

---

## Troubleshooting

### "No module named 'aie'" on Windows/macOS

This is expected. The `aie` module (mlir-aie) is only available on Linux with NPU hardware.

**Solution:** Use the analysis tools only:
```bash
python iron/model_convert/analyze_model.py scan <model_path>
```

Or import only the analysis modules:
```python
from iron.model_convert.analysis import quick_check, generate_gap_report
# Don't import HuggingFaceConverter - it needs AIE
```

### Analysis tool says "Unknown - needs review"

The standalone analyzer uses pattern matching. If your model has novel layer types, they may not be recognized.

**Solution:** Use the full `gap_analyzer.py` on Linux for detailed analysis, or manually review the model's `modeling_*.py` files.

---

## Summary

| Feature | Windows/macOS | Linux (with NPU) |
|---------|---------------|------------------|
| Model scanning | ✓ | ✓ |
| Gap analysis | ✓ | ✓ |
| Quick check | ✓ | ✓ |
| Operator skeletons | ✓ | ✓ |
| Full conversion | ✗ | ✓ |
| AIE compilation | ✗ | ✓ |
| NPU execution | ✗ | ✓ |

For production use, develop and test your analysis on Windows/macOS, then run the actual conversion on a Linux system with NPU hardware.
