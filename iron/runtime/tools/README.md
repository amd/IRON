# Discovery Phase Tools

**Purpose:** Technical investigation tools for the IRON-Lemonade integration Discovery Phase.

**Reference:** See `docs/TECHNICAL_DESIGN_DISCOVERY_PHASE.md` for complete technical specifications.

---

## Overview

This directory contains Python tools for analyzing FastFlowLM kernels, xclbin formats, and runtime APIs as part of the strategic discovery phase recommended by Dr. Sarah Kim's review.

### Key Questions We're Answering

1. **Can we use FastFlowLM pre-compiled kernels** as drop-in replacements for IRON's MLIR-compiled operators?
2. **Are .xclbin files cross-platform** (same file works on Linux XRT and Windows xDNA)?
3. **What is the kernel interface compatibility** between FastFlowLM and IRON operators?
4. **What are the xDNA runtime API capabilities** compared to XRT?

---

## Tools

### 1. xclbin_inspector.py

**Purpose:** Extract kernel interface information from .xclbin files.

**Usage:**
```bash
# Inspect a single .xclbin file
python iron/runtime/tools/xclbin_inspector.py path/to/kernel.xclbin

# Export to JSON for further analysis
python iron/runtime/tools/xclbin_inspector.py path/to/kernel.xclbin output.json
```

**Output:**
- Kernel names and count
- Argument lists (name, type, size, offset, direction)
- Work group sizes
- Memory connections
- Platform indicators

**Example Output:**
```
============================================================
=== .xclbin Kernel Inspector Report
============================================================

File: /path/to/attn.xclbin
Size: 2,458,112 bytes (2.34 MB)
UUID: a1b2c3d4e5f6...
Version: 1

--- Sections (8) ---
  BITSTREAM: 1.23 MB
  IP_LAYOUT: 45.2 KB
  KERNEL_LAYOUT: 12.1 KB
  CONNECTIVITY: 8.5 KB
  ...

--- Kernels (3) ---

  [0] Kernel: qkv_proj_kernel
      Language: C
      Work group size: [64, 1, 1]
      Arguments (8):
        [0] bfloat16* input
            offset=0, size=8, addr_qual=1
        [1] bfloat16* output_q
            offset=8, size=8, addr_qual=1
        [2] bfloat16* output_k
            offset=16, size=8, addr_qual=1
        [3] bfloat16* output_v
            offset=24, size=8, addr_qual=1
        [4] uint32_t batch_size
            offset=32, size=4, addr_qual=0
        ...
```

---

### 2. kernel_comparator.py

**Purpose:** Compare FastFlowLM kernel interfaces with IRON operator signatures.

**Usage:**
```bash
# Compare using default IRON signatures
python iron/runtime/tools/kernel_comparator.py ff_kernels.json

# Compare with custom IRON signatures
python iron/runtime/tools/kernel_comparator.py ff_kernels.json my_iron_sigs.json

# Generate Markdown report
python iron/runtime/tools/kernel_comparator.py ff_kernels.json my_iron_sigs.json compatibility_report.md
```

**Built-in IRON Operators:**
- AIEGEMM (General Matrix Multiplication)
- AIEGEMV (Matrix-Vector Multiplication)
- AIERMSNorm (RMS Normalization)
- AIERoPE (Rotary Position Embeddings)
- AIESoftmax (Softmax Activation)
- AIESwiGLU (SwiGLU MLP)
- AIELayerNorm (Layer Normalization)
- AIEDequant (Dequantization)
- AIEMHA (Multi-Head Attention)
- AIETranspose (Tensor Transpose)

**Output:**
- Compatibility scores (0-10)
- Match classification (EXACT, COMPATIBLE, INCOMPATIBLE, UNKNOWN)
- Detailed difference analysis
- GO/NO-GO recommendation

**Example Output:**
```
============================================================
SUMMARY
============================================================
Compatibility: 72.5%
Critical ops: 60.0% compatible

Recommendation: NO-GO
```

---

## Discovery Workflow

### Step 1: Locate FastFlowLM .xclbin Files

```bash
# Linux
find ~/.config/flm -name "*.xclbin" 2>/dev/null
find /opt/amd -name "*.xclbin" 2>/dev/null

# Windows (PowerShell)
Get-ChildItem -Path "C:\ProgramData\AMD\FastFlowLM" -Recurse -Filter "*.xclbin"
```

### Step 2: Copy Files for Analysis

```bash
mkdir -p discovery/fastflowlm/xclbins/
cp ~/.config/flm/models/*/src/xclbins/*.xclbin discovery/fastflowlm/xclbins/
```

### Step 3: Run Inspector on Each File

```bash
cd discovery/fastflowlm/

for xclbin in xclbins/*.xclbin; do
    python ../../iron/runtime/tools/xclbin_inspector.py \
        "$xclbin" \
        "kernels/$(basename ${xclbin%.xclbin}).json"
done
```

### Step 4: Run Compatibility Analysis

```bash
# Combine all kernel JSON files (or analyze individually)
python ../../iron/runtime/tools/kernel_comparator.py \
    kernels/attn.json \
    kernels/layer.json \
    output/compatibility_report.md
```

### Step 5: Review Results

```bash
# View the report
cat output/compatibility_report.md

# Check GO/NO-GO recommendation
grep -A 5 "GO/NO-GO" output/compatibility_report.md
```

---

## Discovery Deliverables

After completing the discovery phase, we should have:

| File | Description |
|------|-------------|
| `discovery/fastflowlm/kernel_inventory.json` | Complete kernel inventory |
| `discovery/fastflowlm/kernels/*.json` | Per-kernel interface details |
| `discovery/fastflowlm/compatibility_report.md` | IRON compatibility analysis |
| `discovery/xdna/runtime_audit.md` | xDNA vs XRT API comparison |
| `discovery/xclbin_format/analysis.md` | .xclbin format analysis |
| `discovery/lemonade/wrapped_server_api.md` | Lemonade backend API docs |

---

## GO/NO-GO Criteria

After Week 2 discovery phase, we make a GO/NO-GO decision:

### GO (Proceed with Implementation)

- **80%+ critical operator compatibility** (GEMM, RMSNorm, RoPE, SwiGLU, Softmax)
- **No legal blockers** for kernel redistribution
- **.xclbin files loadable** programmatically
- **xDNA runtime provides equivalent functionality** to XRT

### NO-GO (Alternative Approach Needed)

- **Critical operators incompatible** (GEMM, RMSNorm have no matching kernels)
- **.xclbin format is platform-specific** (can't cross-load Linux/Windows)
- **Licensing restrictions** prevent redistribution
- **xDNA runtime missing critical APIs**

### Contingency Options

If NO-GO:
1. **Option A:** Linux-only backend (XRT), Windows deferred
2. **Option B:** Continue with IRON's MLIR runtime compilation for both platforms
3. **Option C:** Partner with AMD for kernel interface documentation

---

## Prerequisites

### Python Packages

```bash
pip install numpy ml-dtypes
```

### System Tools (Optional but Recommended)

```bash
# XRT utilities for .xclbin inspection
sudo apt install xilinx-xclbinutil

# Or download from AMD:
# https://www.xilinx.com/support/download/xilinx-unified.html
```

---

## Troubleshooting

### "Invalid .xclbin magic number"

The file may not be a valid .xclbin, or may be a different version. Check:
- File was copied correctly
- File is from FastFlowLM installation
- Try using `xclbinutil --info` for alternative parsing

### "No kernels found"

The .xclbin may have non-standard metadata encoding. Try:
- Running `xclbinutil --info --input file.xclbin` first
- Check if file has XML metadata section
- Verify file is not corrupted

### "XML parse error"

Some .xclbin files may have non-standard XML. The inspector will continue with partial information.

---

## References

- [TECHNICAL_DESIGN_DISCOVERY_PHASE.md](../../docs/TECHNICAL_DESIGN_DISCOVERY_PHASE.md) - Complete technical design
- [IRON_LEMONADE_INTEGRATION.md](../../docs/IRON_LEMONADE_INTEGRATION.md) - Overall integration plan
- [XRT Documentation](https://xilinx.github.io/xrt/) - XRT runtime reference
- [FastFlowLM GitHub](https://github.com/FastFlowLM/FastFlowLM) - FastFlowLM project

---

*Copyright &copy; 2026 Advanced Micro Devices, Inc. All rights reserved.*
