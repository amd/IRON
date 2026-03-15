# IRON-Lemonade Integration: Technical Design for Discovery Phase

**Document Type:** Technical Design Specification
**Status:** SUPERSEDED - Option B+ Selected (2026-03-15)
**Date:** 2026-03-15
**Author:** Jordan Blake, Principal Software Engineer & Technical Lead
**Based on:** Strategic Review by Dr. Sarah Kim

---

## Executive Summary

**UPDATE 2026-03-15:** This document has been SUPERSEDED by the Option B+ strategic decision.

**CRITICAL INTELLIGENCE:** FastFlowLM production infrastructure discovered at `C:\Program Files\flm`:
- 30+ model families with pre-compiled .xclbin files
- Production Windows NPU runtime (DLLs for gemm, mha, dequant, lm_head)
- Model-family DLLs (llama_npu.dll, qwen3_npu.dll, gpt_oss_npu.dll, etc.)
- GPT-OSS-20B-NPU2 proves 20B parameter deployment works (14GB footprint)
- HuggingFace distribution: `FastFlowLM/<model-name>` with versioned releases

**NEW STRATEGY (Option B+):**
- Leverage FastFlowLM .xclbin files directly (cross-platform)
- Build C++ wrapper around FastFlowLM DLLs on Windows
- Use XRT on Linux with FastFlowLM .xclbin files
- Maintain IRON MLIR compilation as fallback for custom operators

**ORIGINAL DOCUMENT FOLLOWS (for reference):**

---

# PART 1: Discovery Task Technical Specifications

## 1.1 FastFlowLM Kernel Audit (Priority #1)

### Technical Objectives

1. **Inventory all available kernels** in FastFlowLM .xclbin files
2. **Extract kernel interface signatures** (arguments, data types, memory layout)
3. **Map FastFlowLM kernels to IRON operators** (GEMM, RoPE, RMSNorm, etc.)
4. **Identify kernel ABI compatibility** between FastFlowLM and IRON
5. **Document redistribution/licensing constraints**

### Files/Locations to Examine

**FastFlowLM Installation Paths:**

```bash
# Linux paths
~/.config/flm/models/<model-name>/src/xclbins/
/opt/amd/fastflowlm/kernels/
/usr/lib/x86_64-linux-gnu/fastflowlm/

# Windows paths
C:\ProgramData\AMD\FastFlowLM\kernels\
C:\Program Files\AMD\FastFlowLM\share\
```

**Expected .xclbin Files:**
```
attn.xclbin          # Attention mechanism (QKV projection, softmax)
layer.xclbin         # Complete transformer layer
lm_head.xclbin       # Language model output projection
dequant.xclbin       # Weight dequantization
embed.xclbin         # Token embedding lookup
```

### Commands/Code for Investigation

#### Step 1: Locate and List .xclbin Files

```bash
# Linux: Find all .xclbin files
find ~/.config/flm -name "*.xclbin" 2>/dev/null
find /opt/amd -name "*.xclbin" 2>/dev/null

# Windows: Find all .xclbin files (PowerShell)
Get-ChildItem -Path "C:\ProgramData\AMD\FastFlowLM" -Recurse -Filter "*.xclbin"

# Get file sizes and timestamps
ls -lh ~/.config/flm/models/*/src/xclbins/*.xclbin
```

#### Step 2: Extract .xclbin Metadata

```bash
# Use xclbinutil to inspect .xclbin structure
# Install: sudo apt install xilinx-xclbinutil or download from AMD

# Display .xclbin table of contents
xclbinutil --info --input attn.xclbin

# Extract kernel metadata as JSON
xclbinutil --info --input attn.xclbin --output attn_metadata.json

# Dump all sections
xclbinutil --dump-section .xclbin --output dump_dir/ --input attn.xclbin
```

#### Step 3: Parse .xclbin Programmatically (Python)

```python
# File: iron/runtime/tools/xclbin_inspector.py
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""
FastFlowLM .xclbin Inspector

Tool for extracting kernel interfaces from FastFlowLM .xclbin files.
"""

import struct
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

# .xclbin binary format constants
XCLBIN_MAGIC = b'xclbin2\x00'  # 8 bytes
XCLBIN_HEADER_SIZE = 64

@dataclass
class KernelArgument:
    """Represents a single kernel argument"""
    name: str
    address_qualifier: int  # 0=value, 1=pointer to global, 2=pointer to constant
    size: int
    type_name: str
    offset: int

@dataclass
class KernelInterface:
    """Represents a kernel's interface"""
    name: str
    language: str  # "C", "RTL", etc.
    arguments: List[KernelArgument]
    work_group_size: List[int]
    compile_options: str

@dataclass
class XclbinInfo:
    """Complete .xclbin file information"""
    path: str
    file_size: int
    kernels: List[KernelInterface]
    sections: Dict[str, int]  # section_name -> size

class XclbinInspector:
    """Parses .xclbin files and extracts kernel information"""

    def __init__(self, xclbin_path: str):
        self.path = Path(xclbin_path)
        self.data = self.path.read_bytes()
        self.info = XclbinInfo(
            path=str(self.path),
            file_size=len(self.data),
            kernels=[],
            sections={}
        )

    def parse(self) -> XclbinInfo:
        """Parse .xclbin and extract all information"""
        # Verify magic number
        if self.data[:8] != XCLBIN_MAGIC:
            raise ValueError(f"Invalid .xclbin file: {self.path}")

        # Parse header
        header = self._parse_header()

        # Find and parse IP_LAYOUT section (kernel info)
        self._parse_ip_layout(header)

        # Find and parse CONNECTIVITY section (memory connections)
        self._parse_connectivity(header)

        return self.info

    def _parse_header(self) -> dict:
        """Parse xclbin header"""
        # Header layout (64 bytes total):
        # [0:8]   Magic number "xclbin2\x00"
        # [8:24]  UUID (16 bytes)
        # [24:32] Version
        # [32:40] Number of sections
        # [40:48] Header length
        # [48:56] Reserved
        # [56:64] Checksum

        uuid = self.data[8:24].hex()
        version = struct.unpack('<Q', self.data[24:32])[0]
        num_sections = struct.unpack('<Q', self.data[32:40])[0]
        header_len = struct.unpack('<Q', self.data[40:48])[0]

        return {
            'uuid': uuid,
            'version': version,
            'num_sections': num_sections,
            'header_len': header_len
        }

    def _parse_ip_layout(self, header: dict):
        """Parse IP_LAYOUT section to find kernels"""
        # IP_LAYOUT section contains kernel metadata in XML format
        # Search for XML metadata section
        xml_start = self.data.find(b'<?xml')
        if xml_start == -1:
            return

        xml_end = self.data.find(b'</xcl:root>') + 11
        xml_data = self.data[xml_start:xml_end].decode('utf-8', errors='ignore')

        # Parse XML (simplified - use xml.etree in production)
        import xml.etree.ElementTree as ET
        try:
            root = ET.fromstring(xml_data)
            for kernel in root.findall('.//xcl:kernel',
                                       namespaces={'xcl': 'http://www.xilinx.com'}):
                kernel_info = self._parse_kernel_xml(kernel)
                self.info.kernels.append(kernel_info)
        except ET.ParseError:
            pass

    def _parse_kernel_xml(self, kernel_elem) -> KernelInterface:
        """Parse kernel XML element"""
        name = kernel_elem.get('name', 'unknown')
        language = kernel_elem.get('language', 'C')
        compile_options = kernel_elem.get('compileOptions', '')

        arguments = []
        for arg in kernel_elem.findall('.//xcl:arg',
                                        namespaces={'xcl': 'http://www.xilinx.com'}):
            arg_info = KernelArgument(
                name=arg.get('name', 'unknown'),
                address_qualifier=int(arg.get('addressQualifier', '0')),
                size=int(arg.get('size', '0')),
                type_name=arg.get('type', 'unknown'),
                offset=int(arg.get('offset', '0'))
            )
            arguments.append(arg_info)

        work_group_size = [1, 1, 1]
        wg_elem = kernel_elem.find('.//xcl:workGroupSize',
                                    namespaces={'xcl': 'http://www.xilinx.com'})
        if wg_elem is not None:
            work_group_size = [
                int(wg_elem.get('dim1', '1')),
                int(wg_elem.get('dim2', '1')),
                int(wg_elem.get('dim3', '1'))
            ]

        return KernelInterface(
            name=name,
            language=language,
            arguments=arguments,
            work_group_size=work_group_size,
            compile_options=compile_options
        )

    def _parse_connectivity(self, header: dict):
        """Parse memory connectivity information"""
        # For now, just record section sizes
        pass

    def export_json(self, output_path: str):
        """Export parsed information as JSON"""
        with open(output_path, 'w') as f:
            json.dump(asdict(self.info), f, indent=2)


def main():
    """Command-line entry point"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python xclbin_inspector.py <xclbin_file> [output.json]")
        sys.exit(1)

    xclbin_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    inspector = XclbinInspector(xclbin_path)
    info = inspector.parse()

    print(f"\n=== {xclbin_path} ===")
    print(f"File size: {info.file_size:,} bytes")
    print(f"Kernel count: {len(info.kernels)}")

    for kernel in info.kernels:
        print(f"\n  Kernel: {kernel.name}")
        print(f"    Language: {kernel.language}")
        print(f"    Work group size: {kernel.work_group_size}")
        print(f"    Arguments:")
        for arg in kernel.arguments:
            print(f"      - {arg.name}: {arg.type_name} (size={arg.size}, offset={arg.offset})")

    if output_path:
        inspector.export_json(output_path)
        print(f"\nExported to: {output_path}")


if __name__ == '__main__':
    main()
```

#### Step 4: Compare with IRON Operator Signatures

```python
# File: iron/runtime/tools/kernel_comparator.py
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""
Compare FastFlowLM kernel interfaces with IRON operator signatures.
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass

@dataclass
class SignatureMatch:
    """Result of signature comparison"""
    iron_operator: str
    fastflowlm_kernel: str
    match_type: str  # "exact", "compatible", "incompatible"
    differences: List[str]
    notes: str

def load_iron_operator_signatures() -> Dict[str, Dict]:
    """Extract operator signatures from IRON codebase"""
    # These would be extracted from iron/operators/*/op.py files
    return {
        "AIEGEMM": {
            "inputs": [
                {"name": "A", "type": "bfloat16*", "layout": "row-major"},
                {"name": "B", "type": "bfloat16*", "layout": "col-major"},
            ],
            "outputs": [
                {"name": "C", "type": "bfloat16*", "layout": "row-major"},
            ],
            "parameters": [
                {"name": "M", "type": "uint32"},
                {"name": "K", "type": "uint32"},
                {"name": "N", "type": "uint32"},
            ]
        },
        "AIERMSNorm": {
            "inputs": [
                {"name": "input", "type": "bfloat16*"},
                {"name": "weight", "type": "bfloat16*"},
            ],
            "outputs": [
                {"name": "output", "type": "bfloat16*"},
            ],
            "parameters": [
                {"name": "hidden_size", "type": "uint32"},
                {"name": "epsilon", "type": "float32"},
            ]
        },
        "AIERoPE": {
            "inputs": [
                {"name": "q", "type": "bfloat16*"},
                {"name": "k", "type": "bfloat16*"},
                {"name": "cos", "type": "bfloat16*"},
                {"name": "sin", "type": "bfloat16*"},
            ],
            "outputs": [
                {"name": "q_rot", "type": "bfloat16*"},
                {"name": "k_rot", "type": "bfloat16*"},
            ],
            "parameters": [
                {"name": "seq_len", "type": "uint32"},
                {"name": "head_dim", "type": "uint32"},
            ]
        }
    }

def compare_signatures(
    iron_sigs: Dict[str, Dict],
    ff_kernel_json: str
) -> List[SignatureMatch]:
    """Compare IRON operator signatures with FastFlowLM kernels"""

    with open(ff_kernel_json) as f:
        ff_info = json.load(f)

    matches = []

    for iron_op, iron_sig in iron_sigs.items():
        best_match = None
        best_score = 0

        for ff_kernel in ff_info.get('kernels', []):
            score, match_type, differences = _score_kernel_match(iron_sig, ff_kernel)

            if score > best_score:
                best_score = score
                best_match = SignatureMatch(
                    iron_operator=iron_op,
                    fastflowlm_kernel=ff_kernel['name'],
                    match_type=match_type,
                    differences=differences,
                    notes=f"Compatibility score: {score}/10"
                )

        if best_match:
            matches.append(best_match)

    return matches

def _score_kernel_match(iron_sig: Dict, ff_kernel: Dict) -> Tuple[int, str, List[str]]:
    """Score how well a FastFlowLM kernel matches an IRON operator"""
    score = 0
    differences = []

    # Compare input count
    ff_inputs = [a for a in ff_kernel.get('arguments', [])
                 if a.get('address_qualifier') == 1]  # pointers
    iron_input_count = len(iron_sig.get('inputs', []))

    if len(ff_inputs) == iron_input_count:
        score += 3
    else:
        differences.append(f"Input count mismatch: IRON={iron_input_count}, FF={len(ff_inputs)}")

    # Compare argument types
    for i, iron_arg in enumerate(iron_sig.get('inputs', [])):
        if i < len(ff_inputs):
            ff_type = ff_inputs[i].get('type_name', '')
            if _types_compatible(iron_arg['type'], ff_type):
                score += 2
            else:
                differences.append(f"Type mismatch on arg {i}: {iron_arg['type']} vs {ff_type}")

    # Determine match type
    if score >= 8:
        match_type = "exact"
    elif score >= 5:
        match_type = "compatible"
    else:
        match_type = "incompatible"

    return score, match_type, differences

def _types_compatible(iron_type: str, ff_type: str) -> bool:
    """Check if two type strings are compatible"""
    type_map = {
        'bfloat16': ['bfloat16', 'bf16', 'uint16'],
        'float32': ['float', 'float32', 'fp32'],
        'int32': ['int', 'int32'],
        'uint32': ['uint', 'uint32'],
    }

    iron_base = iron_type.replace('*', '').strip()
    ff_base = ff_type.replace('*', '').strip()

    return ff_base in type_map.get(iron_base, [iron_base])

def main():
    iron_sigs = load_iron_operator_signatures()

    # Would load FastFlowLM kernel JSON from inspector output
    import sys
    if len(sys.argv) < 2:
        print("Usage: python kernel_comparator.py <ff_kernel.json>")
        sys.exit(1)

    matches = compare_signatures(iron_sigs, sys.argv[1])

    print("\n=== Kernel Compatibility Report ===\n")
    for match in matches:
        print(f"{match.iron_operator} <-> {match.fastflowlm_kernel}")
        print(f"  Match Type: {match.match_type}")
        print(f"  {match.notes}")
        if match.differences:
            print(f"  Differences:")
            for diff in match.differences:
                print(f"    - {diff}")
        print()

if __name__ == '__main__':
    main()
```

### Data to Collect

| Data Item | Format | Storage Location |
|-----------|--------|------------------|
| Kernel inventory | JSON | `discovery/fastflowlm/kernel_inventory.json` |
| Kernel interfaces | JSON per kernel | `discovery/fastflowlm/kernels/<kernel_name>.json` |
| Compatibility analysis | Markdown | `discovery/fastflowlm/compatibility_report.md` |
| Signature mappings | JSON | `discovery/fastflowlm/signature_map.json` |
| Licensing terms | Text/Markdown | `discovery/fastflowlm/licensing_notes.md` |

### Success Criteria

The FastFlowLM Kernel Audit is **successful** when we can answer:

1. [ ] **Complete kernel inventory**: List of all kernels in FastFlowLM .xclbin files
2. [ ] **Interface signatures**: For each kernel, document all arguments (name, type, size, offset)
3. [ ] **IRON mapping**: For each IRON operator (GEMM, RoPE, RMSNorm, etc.), identify corresponding FastFlowLM kernel
4. [ ] **Compatibility assessment**: For each mapping, classify as:
    - `EXACT`: Drop-in replacement possible
    - `COMPATIBLE`: Wrapper/adaptation needed
    - `INCOMPATIBLE`: Must use IRON's MLIR-compiled kernels
5. [ ] **Licensing clarity**: Document any redistribution restrictions for FastFlowLM kernels

---

## 1.2 xDNA Runtime Feature Audit

### Technical Objectives

1. **Understand xDNA runtime API** on Windows (load, execute, buffer management)
2. **Compare xDNA vs XRT APIs** to identify common abstraction points
3. **Document buffer object semantics** (host-to-device, device-to-host)
4. **Identify kernel execution mechanisms** (sync vs async, runlists)
5. **Determine environment requirements** (drivers, runtime libraries)

### Files/Locations to Examine

**Windows xDNA Runtime:**
```
C:\Program Files\AMD\XDNA\
C:\Windows\System32\xdna_*.dll
C:\ProgramData\AMD\XDNA\driver\
```

**Linux XRT Runtime:**
```
/opt/xilinx/xrt/
/usr/lib/x86_64-linux-gnu/libxrt_core*.so
/opt/xilinx/xrt/include/xrt/
```

**Python Bindings:**
```bash
# Check installed packages
pip show xrt
pip show pyxrt
```

### Commands/Code for Investigation

#### Step 1: Environment Discovery

```bash
# Linux: Check XRT installation
which xrt-config
xrt-config --includedir
xrt-config --libdir

# List XRT libraries
ls -la /opt/xilinx/xrt/lib/
ldconfig -p | grep xrt

# Python XRT inspection
python3 -c "import pyxrt; print(dir(pyxrt))"
python3 -c "import pyxrt; print(pyxrt.__version__)"
```

#### Step 2: API Comparison Script

```python
# File: iron/runtime/tools/runtime_api_audit.py
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""
Audit xDNA and XRT runtime APIs to find common abstraction points.
"""

import inspect
import platform
from typing import Dict, List, Any, Callable
from dataclasses import dataclass

@dataclass
class ApiFunction:
    """Represents a runtime API function"""
    name: str
    signature: str
    parameters: List[Dict[str, str]]
    return_type: str
    description: str
    category: str  # "device", "buffer", "kernel", "execution"

@dataclass
class RuntimeAudit:
    """Complete runtime API audit"""
    runtime_name: str
    version: str
    platform: str
    functions: List[ApiFunction]
    categories: Dict[str, List[str]]

class RuntimeAuditor:
    """Audits a runtime library's API"""

    def __init__(self, runtime_name: str):
        self.runtime_name = runtime_name
        self.runtime_module = self._import_runtime(runtime_name)

    def _import_runtime(self, name: str):
        """Import runtime module"""
        if name == "xrt":
            import pyxrt
            return pyxrt
        elif name == "xdna":
            # Windows-only
            try:
                import xdna_runtime as xdna
                return xdna
            except ImportError:
                print("XDNA runtime not available (Windows-only)")
                return None
        else:
            raise ValueError(f"Unknown runtime: {name}")

    def audit(self) -> RuntimeAudit:
        """Perform complete API audit"""
        if self.runtime_module is None:
            return RuntimeAudit(
                runtime_name=self.runtime_name,
                version="N/A",
                platform=platform.system(),
                functions=[],
                categories={}
            )

        version = getattr(self.runtime_module, '__version__', 'unknown')

        functions = []
        categories = {}

        # Audit all public classes and functions
        for name, obj in inspect.getmembers(self.runtime_module):
            if name.startswith('_'):
                continue

            if inspect.isclass(obj):
                func_info = self._audit_class(name, obj)
                functions.extend(func_info)

                # Categorize
                category = self._categorize_class(name)
                categories.setdefault(category, []).append(name)

        return RuntimeAudit(
            runtime_name=self.runtime_name,
            version=version,
            platform=platform.system(),
            functions=functions,
            categories=categories
        )

    def _audit_class(self, name: str, cls: type) -> List[ApiFunction]:
        """Audit methods of a class"""
        functions = []

        for method_name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
            if method_name.startswith('_'):
                continue

            try:
                sig = inspect.signature(method)
                params = []
                for param_name, param in sig.parameters.items():
                    params.append({
                        'name': param_name,
                        'annotation': str(param.annotation) if param.annotation != inspect.Parameter.empty else 'Any',
                        'default': str(param.default) if param.default != inspect.Parameter.default else None
                    })

                return_annotation = str(sig.return_annotation) if sig.return_annotation != inspect.Signature.empty else 'None'

                func_info = ApiFunction(
                    name=f"{name}.{method_name}",
                    signature=str(sig),
                    parameters=params,
                    return_type=return_annotation,
                    description=method.__doc__ or '',
                    category=self._categorize_method(name, method_name)
                )
                functions.append(func_info)
            except (ValueError, TypeError):
                pass

        return functions

    def _categorize_class(self, name: str) -> str:
        """Categorize a class by name"""
        name_lower = name.lower()
        if 'device' in name_lower:
            return 'device'
        elif 'bo' in name_lower or 'buffer' in name_lower:
            return 'buffer'
        elif 'kernel' in name_lower:
            return 'kernel'
        elif 'run' in name_lower or 'exec' in name_lower:
            return 'execution'
        elif 'context' in name_lower:
            return 'context'
        else:
            return 'other'

    def _categorize_method(self, class_name: str, method_name: str) -> str:
        """Categorize a method"""
        method_lower = method_name.lower()
        if 'read' in method_lower or 'write' in method_lower or 'sync' in method_lower:
            return 'buffer_ops'
        elif 'load' in method_lower or 'get' in method_lower:
            return 'device_ops'
        elif 'run' in method_lower or 'execute' in method_lower:
            return 'execution_ops'
        elif 'create' in method_lower or 'new' in method_lower:
            return 'construction'
        else:
            return 'other'


def compare_runtimes(xrt_audit: RuntimeAudit, xdna_audit: RuntimeAudit) -> Dict:
    """Compare two runtime audits to find common patterns"""

    comparison = {
        'common_categories': [],
        'xrt_only': [],
        'xdna_only': [],
        'common_functions': [],
        'api_differences': []
    }

    # Compare categories
    xrt_cats = set(xrt_audit.categories.keys())
    xdna_cats = set(xdna_audit.categories.keys())

    comparison['common_categories'] = list(xrt_cats & xdna_cats)
    comparison['xrt_only'] = list(xrt_cats - xdna_cats)
    comparison['xdna_only'] = list(xdna_cats - xrt_cats)

    # Compare function patterns
    xrt_funcs = {f.name for f in xrt_audit.functions}
    xdna_funcs = {f.name for f in xdna_audit.functions}

    comparison['common_functions'] = list(xrt_funcs & xdna_funcs)

    return comparison


def generate_abstraction_recommendations(comparison: Dict) -> List[Dict]:
    """Generate recommendations for abstraction layer design"""
    recommendations = []

    # For each common category, suggest interface methods
    for category in comparison.get('common_categories', []):
        recommendations.append({
            'category': category,
            'action': 'Create common interface method',
            'priority': 'HIGH'
        })

    # For XRT-only features, note Linux-only limitation
    for feature in comparison.get('xrt_only', []):
        recommendations.append({
            'category': feature,
            'action': 'Linux-only feature - provide fallback or stub',
            'priority': 'MEDIUM'
        })

    return recommendations


def main():
    # Audit XRT (Linux)
    print("Auditing XRT runtime...")
    xrt_auditor = RuntimeAuditor('xrt')
    xrt_audit = xrt_auditor.audit()

    print(f"  Found {len(xrt_audit.functions)} API functions")
    print(f"  Categories: {list(xrt_audit.categories.keys())}")

    # Audit xDNA (Windows)
    print("\nAuditing xDNA runtime...")
    xdna_auditor = RuntimeAuditor('xdna')
    xdna_audit = xdna_auditor.audit()

    print(f"  Found {len(xdna_audit.functions)} API functions")
    print(f"  Categories: {list(xdna_audit.categories.keys())}")

    # Compare
    print("\n=== Runtime Comparison ===")
    comparison = compare_runtimes(xrt_audit, xdna_audit)

    print(f"Common categories: {comparison['common_categories']}")
    print(f"XRT-only: {comparison['xrt_only']}")
    print(f"xDNA-only: {comparison['xdna_only']}")

    # Recommendations
    print("\n=== Abstraction Recommendations ===")
    recommendations = generate_abstraction_recommendations(comparison)
    for rec in recommendations:
        print(f"  [{rec['priority']}] {rec['category']}: {rec['action']}")


if __name__ == '__main__':
    main()
```

### Data to Collect

| Data Item | Format | Storage Location |
|-----------|--------|------------------|
| XRT API inventory | JSON | `discovery/xdna/xrt_api.json` |
| xDNA API inventory | JSON | `discovery/xdna/xdna_api.json` |
| API comparison matrix | Markdown | `discovery/xdna/api_comparison.md` |
| Abstraction recommendations | Markdown | `discovery/xdna/abstraction_design.md` |
| Environment requirements | Markdown | `discovery/xdna/environment_requirements.md` |

### Success Criteria

The xDNA Runtime Feature Audit is **successful** when:

1. [ ] **XRT API documented**: Complete inventory of pyxrt classes and methods
2. [ ] **xDNA API documented** (if accessible): Complete inventory of xDNA runtime APIs
3. [ ] **Common patterns identified**: List of shared concepts (device, buffer, kernel, execution)
4. [ ] **Differences documented**: Clear list of platform-specific features
5. [ ] **Abstraction design draft**: Proposed interface that works for both runtimes

---

## 1.3 .xclbin Format Analysis

### Technical Objectives

1. **Understand .xclbin binary format** (header, sections, metadata)
2. **Identify platform-specific sections** (Linux vs Windows differences)
3. **Document kernel loading process** (how runtime parses .xclbin)
4. **Assess format stability** (versioning, backward compatibility)
5. **Determine if cross-platform .xclbin is feasible**

### Files/Locations to Examine

**Format Documentation:**
```
/opt/xilinx/xrt/include/experimental/xclbin.h
/usr/include/xrt/detail/xclbin.h
https://xilinx.github.io/XRT/master/html/xclbin_format.html
```

**Sample .xclbin Files:**
```
# From IRON compilation (after first compile)
build/*.xclbin

# From FastFlowLM
~/.config/flm/models/*/src/xclbins/*.xclbin
```

### Commands/Code for Investigation

#### Step 1: Binary Format Inspection

```bash
# Use hexdump to examine header
hexdump -C ~/.config/flm/models/llama-3.2-1b/src/xclbins/attn.xclbin | head -50

# Use xclbinutil for structured inspection
xclbinutil --info --input attn.xclbin

# Extract specific sections
xclbinutil --dump-section .xclbin --output extracted/ --input attn.xclbin
```

#### Step 2: Format Analysis Script

```python
# File: iron/runtime/tools/xclbin_format_analyzer.py
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""
Analyze .xclbin binary format structure.
"""

import struct
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

@dataclass
class XclbinHeader:
    """xclbin file header structure"""
    magic: str
    uuid: str
    version: int
    num_sections: int
    header_length: int
    checksum: int

@dataclass
class SectionInfo:
    """Information about a single section"""
    name: str
    offset: int
    size: int
    section_kind: int

@dataclass
class XclbinAnalysis:
    """Complete .xclbin format analysis"""
    path: str
    file_size: int
    header: XclbinHeader
    sections: List[SectionInfo]
    xml_metadata: Optional[str]
    platform_indicators: List[str]

class XclbinFormatAnalyzer:
    """Analyzes .xclbin binary format"""

    # Section kind constants (from xclbin.h)
    SECTION_KINDS = {
        0x00000000: "UNKNOWN",
        0x00000001: "BITSTREAM",
        0x00000002: "IP_LAYOUT",
        0x00000003: "KERNEL_LAYOUT",
        0x00000004: "CONNECTIVITY",
        0x00000005: "EMBEDDED_METADATA",
        0x00000006: "SOFT_KERNEL",
        0x00000007: "CLOCK_TOPOLOGY",
        0x00000008: "DEBUG_IP_LAYOUT",
        0x00000009: "SYSTEM_METADATA",
        0x0000000A: "EMBEDDED_METADATA_XML",
    }

    SECTION_NAMES = {
        b"PRIMARY_IP_LAYOUT": "IP Layout",
        b"IP_LAYOUT": "IP Layout",
        b"KERNEL_LAYOUT": "Kernel Layout",
        b"CONNECTIVITY": "Connectivity",
        b"EMBEDDED_METADATA": "Embedded Metadata",
        b"BITSTREAM": "Bitstream",
        b"CLOCK_TOPOLOGY": "Clock Topology",
        b"DEBUG_IP_LAYOUT": "Debug IP Layout",
        b"SYSTEM_METADATA": "System Metadata",
    }

    def __init__(self, xclbin_path: str):
        self.path = Path(xclbin_path)
        self.data = self.path.read_bytes()

    def analyze(self) -> XclbinAnalysis:
        """Perform complete format analysis"""
        header = self._parse_header()
        sections = self._find_sections()
        xml_metadata = self._extract_xml_metadata()
        platform_indicators = self._detect_platform_indicators()

        return XclbinAnalysis(
            path=str(self.path),
            file_size=len(self.data),
            header=header,
            sections=sections,
            xml_metadata=xml_metadata,
            platform_indicators=platform_indicators
        )

    def _parse_header(self) -> XclbinHeader:
        """Parse xclbin header (64 bytes)"""
        # struct xclbin2_header {
        #     char m_magic[8];        // "xclbin2\x00"
        #     char m_uuid[16];        // UUID
        #     uint64_t m_version;     // Version
        #     uint64_t m_numSections; // Number of sections
        #     uint64_t m_headerLength; // Header length
        #     uint64_t m_checksum;    // Checksum
        # };

        magic = self.data[0:8].rstrip(b'\x00').decode('ascii')
        uuid = self.data[8:24].hex()
        version = struct.unpack('<Q', self.data[24:32])[0]
        num_sections = struct.unpack('<Q', self.data[32:40])[0]
        header_length = struct.unpack('<Q', self.data[40:48])[0]
        checksum = struct.unpack('<Q', self.data[48:56])[0]

        return XclbinHeader(
            magic=magic,
            uuid=uuid,
            version=version,
            num_sections=num_sections,
            header_length=header_length,
            checksum=checksum
        )

    def _find_sections(self) -> List[SectionInfo]:
        """Find all sections in the file"""
        # Section header follows main header
        # struct xclbin2_section_header {
        #     uint32_t m_sectionType;
        #     uint64_t m_sectionOffset;
        #     uint64_t m_sectionSize;
        #     uint32_t m_sectionKind;
        #     char m_sectionName[64];
        #     ...
        # };

        sections = []
        offset = 64  # After main header

        while offset < len(self.data):
            try:
                section_type = struct.unpack('<I', self.data[offset:offset+4])[0]
                section_offset = struct.unpack('<Q', self.data[offset+8:offset+16])[0]
                section_size = struct.unpack('<Q', self.data[offset+16:offset+24])[0]
                section_kind = struct.unpack('<I', self.data[offset+24:offset+28])[0]
                section_name = self.data[offset+28:offset+92].rstrip(b'\x00').decode('ascii', errors='ignore')

                if section_size == 0 or section_offset == 0:
                    break

                kind_name = self.SECTION_KINDS.get(section_kind, f"UNKNOWN_0x{section_kind:X}")

                sections.append(SectionInfo(
                    name=section_name or kind_name,
                    offset=section_offset,
                    size=section_size,
                    section_kind=section_kind
                ))

                offset += 92  # Section header size
            except (struct.error, UnicodeDecodeError):
                break

        return sections

    def _extract_xml_metadata(self) -> Optional[str]:
        """Extract embedded XML metadata"""
        # Search for XML start
        xml_start = self.data.find(b'<?xml')
        if xml_start == -1:
            return None

        # Find XML end
        xml_end = self.data.find(b'</xcl:root>')
        if xml_end == -1:
            return None
        xml_end += 11

        return self.data[xml_start:xml_end].decode('utf-8', errors='ignore')

    def _detect_platform_indicators(self) -> List[str]:
        """Detect platform-specific indicators in the .xclbin"""
        indicators = []

        # Check for Windows-specific strings
        if b'\\' in self.data[:1000]:
            indicators.append("Possible Windows path separators")

        # Check for Linux-specific strings
        if b'/opt/' in self.data or b'/usr/' in self.data:
            indicators.append("Linux path references found")

        # Check for xrt references
        if b'xrt' in self.data.lower():
            indicators.append("XRT references detected")

        # Check for xdna references
        if b'xdna' in self.data.lower():
            indicators.append("xDNA references detected")

        return indicators


def main():
    import sys
    import json

    if len(sys.argv) < 2:
        print("Usage: python xclbin_format_analyzer.py <xclbin_file> [output.json]")
        sys.exit(1)

    analyzer = XclbinFormatAnalyzer(sys.argv[1])
    analysis = analyzer.analyze()

    print(f"\n=== .xclbin Format Analysis ===")
    print(f"File: {analysis.path}")
    print(f"Size: {analysis.file_size:,} bytes")
    print(f"\nHeader:")
    print(f"  Magic: {analysis.header.magic}")
    print(f"  UUID: {analysis.header.uuid}")
    print(f"  Version: {analysis.header.version}")
    print(f"  Sections: {analysis.header.num_sections}")

    print(f"\nSections ({len(analysis.sections)} found):")
    for i, section in enumerate(analysis.sections[:10]):  # Show first 10
        print(f"  [{i}] {section.name}")
        print(f"      Offset: 0x{section.offset:X}, Size: {section.size:,} bytes")
        print(f"      Kind: 0x{section.section_kind:X}")

    if len(analysis.sections) > 10:
        print(f"  ... and {len(analysis.sections) - 10} more")

    print(f"\nPlatform Indicators:")
    for indicator in analysis.platform_indicators:
        print(f"  - {indicator}")

    if analysis.xml_metadata:
        print(f"\nXML Metadata: {len(analysis.xml_metadata)} bytes")

    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w') as f:
            json.dump(asdict(analysis), f, indent=2)
        print(f"\nExported to: {sys.argv[2]}")


if __name__ == '__main__':
    main()
```

### Data to Collect

| Data Item | Format | Storage Location |
|-----------|--------|------------------|
| Format analysis report | JSON | `discovery/xclbin_format/analysis.json` |
| Section inventory | Markdown | `discovery/xclbin_format/sections.md` |
| Platform compatibility assessment | Markdown | `discovery/xclbin_format/platform_compatibility.md` |
| Cross-platform loading strategy | Markdown | `discovery/xclbin_format/cross_platform_strategy.md` |

### Success Criteria

The .xclbin Format Analysis is **successful** when:

1. [ ] **Header structure documented**: Complete understanding of 64-byte header
2. [ ] **Section inventory**: List of all section types found in FastFlowLM .xclbin files
3. [ ] **XML metadata extracted**: Kernel interface information from embedded XML
4. [ ] **Platform differences identified**: Any Linux vs Windows format differences
5. [ ] **Cross-platform strategy**: Clear answer on whether same .xclbin works on both platforms

---

## 1.4 Lemonade Backend API Review

### Technical Objectives

1. **Understand `WrappedServer` interface** requirements
2. **Document backend lifecycle** (load, unload, inference)
3. **Identify integration points** with IRON runtime
4. **Review existing backend implementations** for patterns
5. **Document model format expectations**

### Files/Locations to Examine

**Lemonade Source (external repo):**
```bash
# Clone Lemonade repository
git clone https://github.com/lemonade-sdk/lemonade.git ~/dev/lemonade

# Key files to examine
~/dev/lemonade/src/cpp/include/lemon/wrapped_server.h
~/dev/lemonade/src/cpp/server/backends/
~/dev/lemonade/src/cpp/include/lemon/backends/
```

### Commands/Code for Investigation

#### Step 1: Examine WrappedServer Interface

```cpp
// Pseudo-code based on typical WrappedServer interface
// This needs to be verified against actual Lemonade source

class WrappedServer {
public:
    virtual ~WrappedServer() = default;

    // Backend lifecycle
    virtual void load(
        const std::string& model_name,
        const ModelInfo& model_info,
        const RecipeOptions& options,
        bool do_not_upgrade = false
    ) = 0;

    virtual void unload() = 0;

    // Inference endpoints
    virtual json chat_completion(const json& request) = 0;
    virtual json completion(const json& request) = 0;
    virtual json responses(const json& request) = 0;

    // Health check
    virtual json health_check() = 0;

    // Backend availability
    static virtual bool is_available();

protected:
    // Helper methods
    std::string choose_port();
    bool wait_for_ready(const std::string& endpoint);
    json forward_request(const std::string& path, const json& request);

    // State
    std::string port_;
    bool is_loaded_;
    bool debug_;
};
```

#### Step 2: Review Existing Backend Implementations

```bash
# Examine existing backend implementations
cd ~/dev/lemonade

# llamacpp backend
cat src/cpp/server/backends/llamacpp_server.cpp

# ryzenai backend (if exists)
cat src/cpp/server/backends/ryzenai_server.cpp

# Any other wrapped server implementations
find src/cpp/server/backends/ -name "*_server.cpp" -exec cat {} \;
```

### Data to Collect

| Data Item | Format | Storage Location |
|-----------|--------|------------------|
| WrappedServer API documentation | Markdown | `discovery/lemonade/wrapped_server_api.md` |
| Backend lifecycle diagram | Markdown/Mermaid | `discovery/lemonade/backend_lifecycle.md` |
| Integration points analysis | Markdown | `discovery/lemonade/integration_points.md` |
| Model format requirements | Markdown | `discovery/lemonade/model_formats.md` |

### Success Criteria

The Lemonade Backend API Review is **successful** when:

1. [ ] **WrappedServer interface documented**: All required methods identified
2. [ ] **Lifecycle understood**: Clear flow from load() to inference to unload()
3. [ ] **Integration points identified**: Where IRON runtime connects to backend
4. [ ] **Model format clarified**: What format Lemonade expects for model weights
5. [ ] **Port/communication strategy**: How C++ backend talks to Python/IRON runtime

---

# PART 2: FastFlowLM .xclbin Kernel Audit (Priority #1)

## Detailed Technical Plan

### Phase 2.1: Locating and Extracting FastFlowLM .xclbin Files

#### Step 1: Check FastFlowLM Installation

```bash
# Linux: Check if FastFlowLM is installed
which flm
flm --version

# Check FastFlowLM config directory
ls -la ~/.config/flm/

# List installed models
flm model list 2>/dev/null || echo "No 'flm' command found"

# Search for .xclbin files
find ~ -name "*.xclbin" 2>/dev/null | head -20
```

#### Step 2: Download Sample Model (if needed)

```bash
# If FastFlowLM is not installed, download a sample model
# This would use FastFlowLM's model download functionality

# Example (actual command depends on FastFlowLM CLI):
# flm model download meta-llama/Llama-3.2-1B-Instruct

# Or check FastFlowLM documentation for model acquisition
```

#### Step 3: Copy .xclbin Files for Analysis

```bash
# Create analysis directory
mkdir -p ~/dev/IRON/discovery/fastflowlm/xclbins/

# Copy all .xclbin files
cp ~/.config/flm/models/*/src/xclbins/*.xclbin ~/dev/IRON/discovery/fastflowlm/xclbins/

# List copied files
ls -lh ~/dev/IRON/discovery/fastflowlm/xclbins/
```

### Phase 2.2: Analyzing Kernel Interfaces

#### Step 1: Run xclbinutil on Each File

```bash
cd ~/dev/IRON/discovery/fastflowlm/xclbins/

# Create output directory
mkdir -p analysis_output/

# Process each .xclbin file
for xclbin in *.xclbin; do
    echo "=== Processing $xclbin ==="

    # Get basic info
    xclbinutil --info --input "$xclbin" > "analysis_output/${xclbin%.xclbin}_info.txt"

    # Export JSON metadata
    xclbinutil --info --input "$xclbin" --output "analysis_output/${xclbin%.xclbin}_metadata.json"

    # Dump sections
    mkdir -p "analysis_output/${xclbin%.xclbin}_sections/"
    xclbinutil --dump-section .xclbin \
        --output "analysis_output/${xclbin%.xclbin}_sections/" \
        --input "$xclbin"
done
```

#### Step 2: Run Custom Inspector

```bash
cd ~/dev/IRON/discovery/fastflowlm/

# Run Python inspector on each .xclbin
for xclbin in xclbins/*.xclbin; do
    python3 ../../runtime/tools/xclbin_inspector.py \
        "$xclbin" \
        "kernels/$(basename ${xclbin%.xclbin}).json"
done

# Generate combined report
python3 ../../runtime/tools/kernel_comparator.py \
    kernels/*.json > kernel_compatibility_report.md
```

### Phase 2.3: Comparing with IRON Operator Signatures

#### IRON Operator Signature Reference

Based on the IRON codebase analysis:

| Operator | Primary Inputs | Primary Outputs | Key Parameters |
|----------|---------------|-----------------|----------------|
| AIEGEMM | A (MxK), B (KxN) | C (MxN) | M, K, N, tile sizes |
| AIERMSNorm | input, weight | output | hidden_size, epsilon |
| AIERoPE | q, k, cos, sin | q_rot, k_rot | seq_len, head_dim |
| AIESoftmax | input | output | dim, scale |
| AIESwiGLU | input, weight_gate, weight_up | output | hidden_size, intermediate_size |

#### Comparison Matrix Template

```markdown
| IRON Operator | FastFlowLM Kernel | Match | Notes |
|--------------|-------------------|-------|-------|
| AIEGEMM | gemm_kernel | YES/NO | Interface compatible? |
| AIERMSNorm | norm_kernel | YES/NO | |
| AIERoPE | rope_kernel | YES/NO | |
| AIESoftmax | softmax_kernel | YES/NO | |
| AIESwiGLU | swiglu_kernel | YES/NO | |
```

### Phase 2.4: Documentation Template

```markdown
# FastFlowLM Kernel Audit Report

## Date: YYYY-MM-DD

## Executive Summary

[Brief summary of findings - can we use FastFlowLM kernels?]

## Kernel Inventory

### attn.xclbin
- **File size:** X MB
- **Kernels found:** N
- **Primary kernel:** kernel_name
- **Interface:**
  - Argument 0: name, type, purpose
  - Argument 1: name, type, purpose
  - ...

### layer.xclbin
[...]

## IRON Compatibility Analysis

### AIEGEMM Compatibility
- **Matching FastFlowLM kernel:** gemm_kernel
- **Match type:** EXACT/COMPATIBLE/INCOMPATIBLE
- **Interface differences:** [...]
- **Adaptation needed:** Yes/No - what changes

### AIERMSNorm Compatibility
[...]

## Redistribution/Licensing

[Findings about whether we can redistribute FastFlowLM kernels]

## Recommendations

1. [Specific recommendation]
2. [Specific recommendation]

## GO/NO-GO Recommendation

Based on kernel compatibility analysis, we recommend:
- [ ] **GO**: Proceed with C++ runtime abstraction
- [ ] **NO-GO**: Significant technical blockers identified

Rationale: [explanation]
```

---

# PART 3: IXclbinRuntime Interface Design

## Design Rationale

The `IXclbinRuntime` interface must account for the fundamental difference between:
- **Linux**: Runtime compilation via MLIR, XRT handles .xclbin loading
- **Windows**: Pre-compiled kernels from FastFlowLM, xDNA runtime loads .xclbin

The interface provides:
1. **Unified .xclbin loading** regardless of platform
2. **Buffer management abstraction** (BOs in XRT terminology)
3. **Kernel execution interface** with proper argument binding
4. **Operator-level kernel loading** for future extensibility

## C++ Header File: `ixclbin_runtime.h`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
// SPDX-License-Identifier: Apache-2.0

/**
 * @file ixclbin_runtime.h
 * @brief Cross-platform runtime interface for .xclbin kernel execution
 *
 * This header defines the abstract interface for loading and executing
 * .xclbin kernels on AMD Ryzen AI NPUs. The implementation differs
 * between Linux (XRT) and Windows (xDNA), but the interface remains
 * consistent.
 */

#pragma once

#include <string>
#include <vector>
#include <memory>
#include <cstdint>
#include <optional>
#include <variant>

namespace iron {
namespace runtime {

/**
 * @brief Buffer handle for device memory
 *
 * Represents a buffer object (BO) in the NPU's memory space.
 * Platform-specific implementations wrap XRT BOs (Linux) or
 * xDNA buffer handles (Windows).
 */
class IBuffer {
public:
    virtual ~IBuffer() = default;

    /**
     * @brief Get buffer size in bytes
     */
    virtual size_t size() const = 0;

    /**
     * @brief Write data to buffer (host-to-device)
     * @param data Pointer to source data
     * @param size Number of bytes to write
     * @param offset Offset in destination buffer
     */
    virtual void write(const void* data, size_t size, size_t offset = 0) = 0;

    /**
     * @brief Read data from buffer (device-to-host)
     * @param data Pointer to destination buffer
     * @param size Number of bytes to read
     * @param offset Offset in source buffer
     */
    virtual void read(void* data, size_t size, size_t offset = 0) const = 0;

    /**
     * @brief Sync buffer with device
     * @param to_device If true, sync host-to-device; otherwise device-to-host
     */
    virtual void sync(bool to_device) = 0;

    /**
     * @brief Get native buffer handle (platform-specific)
     * @return Opaque handle for platform-specific code
     */
    virtual void* native_handle() = 0;
};

/**
 * @brief Result of kernel execution
 */
struct ExecutionResult {
    /// Execution status code (0 = success)
    int status;

    /// Execution time in microseconds (optional)
    std::optional<uint64_t> execution_time_us;

    /// Error message if execution failed
    std::optional<std::string> error_message;

    /// Output buffers (if kernel produces outputs)
    std::vector<std::shared_ptr<IBuffer>> outputs;

    bool success() const { return status == 0; }
};

/**
 * @brief Kernel argument variant types
 */
using KernelArgument = std::variant<
    std::shared_ptr<IBuffer>,  // Buffer argument
    int32_t,                    // Scalar integer
    float,                      // Scalar float
    uint32_t                    // Scalar unsigned integer
>;

/**
 * @brief Kernel execution options
 */
struct ExecutionOptions {
    /// Timeout in milliseconds (0 = no timeout)
    uint32_t timeout_ms = 0;

    /// Enable profiling
    bool profile = false;

    /// Synchronous execution (wait for completion)
    bool synchronous = true;
};

/**
 * @brief Abstract interface for .xclbin runtime
 *
 * This interface provides platform-agnostic kernel loading and execution.
 * Implementations exist for:
 * - Linux: XrtRuntime (uses XRT/pyxrt)
 * - Windows: XdnaRuntime (uses xDNA runtime)
 *
 * Example usage:
 * @code
 * auto runtime = IXclbinRuntime::create();
 * runtime->load_xclbin("/path/to/kernel.xclbin");
 *
 * auto kernel = runtime->get_kernel("gemm_kernel");
 * kernel->set_arg(0, buffer_a);
 * kernel->set_arg(1, buffer_b);
 * kernel->set_arg(2, buffer_c);
 * kernel->set_arg(3, static_cast<int32_t>(M));
 * kernel->set_arg(4, static_cast<int32_t>(K));
 * kernel->set_arg(5, static_cast<int32_t>(N));
 *
 * auto result = kernel->execute();
 * @endcode
 */
class IXclbinRuntime {
public:
    virtual ~IXclbinRuntime() = default;

    /**
     * @brief Load .xclbin kernel package
     *
     * Loads all kernels contained in the .xclbin file.
     * The file must exist and be a valid .xclbin format.
     *
     * @param path Path to .xclbin file
     * @return true if loaded successfully, false otherwise
     */
    virtual bool load_xclbin(const std::string& path) = 0;

    /**
     * @brief Load .xclbin from memory buffer
     *
     * Allows loading .xclbin from a memory buffer instead of file.
     * Useful for embedded scenarios or custom loading logic.
     *
     * @param data Pointer to .xclbin data
     * @param size Size of data in bytes
     * @return true if loaded successfully, false otherwise
     */
    virtual bool load_xclbin_from_memory(const void* data, size_t size) = 0;

    /**
     * @brief Get list of available kernel names
     * @return Vector of kernel names
     */
    virtual std::vector<std::string> get_kernel_names() const = 0;

    /**
     * @brief Check if a specific kernel is available
     * @param kernel_name Name of kernel to check
     * @return true if kernel is loaded and available
     */
    virtual bool has_kernel(const std::string& kernel_name) const = 0;

    /**
     * @brief Execute kernel with provided arguments
     *
     * @param kernel_name Name of kernel to execute
     * @param arguments Kernel arguments (buffers and scalars)
     * @param options Execution options
     * @return ExecutionResult with status and outputs
     */
    virtual ExecutionResult execute(
        const std::string& kernel_name,
        const std::vector<KernelArgument>& arguments,
        const ExecutionOptions& options = ExecutionOptions()
    ) = 0;

    /**
     * @brief Create a kernel execution handle
     *
     * Returns a handle for repeated kernel execution with
     * different arguments. More efficient than execute() for
     * repeated calls.
     *
     * @param kernel_name Name of kernel
     * @return Kernel handle, or nullptr if kernel not found
     */
    virtual std::shared_ptr<class IKernelHandle> get_kernel(
        const std::string& kernel_name
    ) = 0;

    /**
     * @brief Allocate buffer for kernel I/O
     *
     * @param size Size in bytes
     * @param host_accessible If true, buffer is accessible from host
     * @return Shared pointer to buffer
     */
    virtual std::shared_ptr<IBuffer> allocate_buffer(
        size_t size,
        bool host_accessible = true
    ) = 0;

    /**
     * @brief Allocate buffer from existing host data
     *
     * Creates a device buffer and copies initial data from host.
     *
     * @param data Pointer to host data
     * @param size Size in bytes
     * @return Shared pointer to buffer
     */
    virtual std::shared_ptr<IBuffer> allocate_buffer_from_data(
        const void* data,
        size_t size
    ) = 0;

    /**
     * @brief Unload all kernels and free resources
     */
    virtual void unload() = 0;

    /**
     * @brief Check if runtime has loaded kernels
     * @return true if any kernels are loaded
     */
    virtual bool is_loaded() const = 0;

    /**
     * @brief Get platform name
     * @return "XRT" for Linux, "xDNA" for Windows
     */
    virtual std::string get_platform_name() const = 0;

    /**
     * @brief Get runtime version string
     * @return Version information
     */
    virtual std::string get_version() const = 0;

    /**
     * @brief Check if NPU device is available
     * @return true if NPU is present and accessible
     */
    static bool is_device_available();

    /**
     * @brief Create platform-appropriate runtime implementation
     *
     * Factory method that returns XrtRuntime on Linux
     * or XdnaRuntime on Windows.
     *
     * @return Unique pointer to runtime instance
     */
    static std::unique_ptr<IXclbinRuntime> create();
};

/**
 * @brief Handle for repeated kernel execution
 *
 * Provides a more efficient interface for kernels that
 * need to be executed multiple times with different arguments.
 */
class IKernelHandle {
public:
    virtual ~IKernelHandle() = default;

    /**
     * @brief Get kernel name
     */
    virtual std::string name() const = 0;

    /**
     * @brief Set kernel argument
     *
     * @param index Argument index (0-based)
     * @param arg Argument value
     */
    virtual void set_arg(size_t index, const KernelArgument& arg) = 0;

    /**
     * @brief Execute kernel with set arguments
     * @param options Execution options
     * @return Execution result
     */
    virtual ExecutionResult execute(const ExecutionOptions& options = ExecutionOptions()) = 0;

    /**
     * @brief Reset all arguments to default state
     */
    virtual void reset() = 0;

    /**
     * @brief Get number of kernel arguments
     * @return Argument count
     */
    virtual size_t num_arguments() const = 0;
};

/**
 * @brief Buffer manager for efficient memory allocation
 *
 * Manages a pool of buffers to avoid repeated allocation/deallocation.
 */
class IBufferManager {
public:
    virtual ~IBufferManager() = default;

    /**
     * @brief Allocate buffer from pool
     * @param size Minimum buffer size needed
     * @return Buffer handle
     */
    virtual std::shared_ptr<IBuffer> allocate(size_t size) = 0;

    /**
     * @brief Return buffer to pool for reuse
     * @param buffer Buffer to return
     */
    virtual void deallocate(std::shared_ptr<IBuffer> buffer) = 0;

    /**
     * @brief Get pool statistics
     * @return Map of buffer size to count of available buffers
     */
    virtual std::map<size_t, size_t> get_pool_stats() const = 0;

    /**
     * @brief Clear all buffers from pool
     */
    virtual void clear() = 0;
};

} // namespace runtime
} // namespace iron
```

## Implementation Notes

### Linux (XRT) Implementation

```cpp
// xrt_runtime.cpp - skeleton
class XrtRuntime : public IXclbinRuntime {
private:
    pyxrt::device device_;
    pyxrt::hw_context context_;
    std::map<std::string, pyxrt::kernel> kernels_;

public:
    XrtRuntime() : device_(0), context_(device_) {}

    bool load_xclbin(const std::string& path) override {
        pyxrt::xclbin xclbin(path);
        device_.load_xclbin(xclbin);

        // Extract kernels
        auto uuid = xclbin.get_uuid();
        // ... register kernels
        return true;
    }

    std::shared_ptr<IBuffer> allocate_buffer(size_t size, bool host_accessible) override {
        // Use XRT BO allocation
        auto bo = pyxrt::bo(device_, size,
                           host_accessible ? pyxrt::bo::host_only : 0,
                           0);
        return std::make_shared<XrtBuffer>(bo);
    }

    // ... other implementations
};
```

### Windows (xDNA) Implementation

```cpp
// xdna_runtime.cpp - skeleton
class XdnaRuntime : public IXclbinRuntime {
private:
    void* device_handle_;  // xDNA device handle
    std::map<std::string, void*> kernels_;  // xDNA kernel handles
    std::vector<std::string> xclbin_paths_;

public:
    XdnaRuntime() {
        // Initialize xDNA runtime
        // device_handle_ = xdna_open(0);
    }

    bool load_xclbin(const std::string& path) override {
        // Load pre-compiled .xclbin on Windows
        // xclbin_loader_load(device_handle_, path.c_str());
        xclbin_paths_.push_back(path);
        return true;
    }

    std::shared_ptr<IBuffer> allocate_buffer(size_t size, bool host_accessible) override {
        // Use xDNA buffer allocation
        // auto handle = xdna_buffer_alloc(device_handle_, size);
        return std::make_shared<XdnaBuffer>(handle);
    }

    // ... other implementations
};
```

---

# PART 4: Revised Phase 1 Implementation Plan

## Week 1-2: Discovery Tasks

### Deliverables

| Task | Deliverable | Location | Owner |
|------|-------------|----------|-------|
| FastFlowLM Kernel Audit | `discovery/fastflowlm/kernel_audit.md` | IRON/docs/ | TBD |
| FastFlowLM Kernel Audit | `discovery/fastflowlm/kernels/*.json` | IRON/discovery/ | TBD |
| xDNA Runtime Audit | `discovery/xdna/runtime_audit.md` | IRON/docs/ | TBD |
| xDNA Runtime Audit | `discovery/xdna/xrt_api.json`, `xdna_api.json` | IRON/discovery/ | TBD |
| .xclbin Format Analysis | `discovery/xclbin_format/analysis.md` | IRON/docs/ | TBD |
| .xclbin Format Analysis | `discovery/xclbin_format/analysis.json` | IRON/discovery/ | TBD |
| Lemonade API Review | `discovery/lemonade/wrapped_server_api.md` | IRON/docs/ | TBD |

### Week 1 Milestones

- [ ] **Day 1-2**: Set up discovery environment, clone Lemonade repo
- [ ] **Day 3-5**: FastFlowLM .xclbin extraction and initial inspection
- [ ] **Day 5**: xDNA runtime API audit (if Windows environment available)

### Week 2 Milestones

- [ ] **Day 1-2**: Complete kernel interface extraction
- [ ] **Day 3**: Run compatibility analysis against IRON operators
- [ ] **Day 4**: Complete .xclbin format analysis
- [ ] **Day 5**: **GO/NO-GO Review Meeting**

## Week 2 GO/NO-GO Decision Criteria

### GO Criteria (All must be met)

1. **Kernel Compatibility**: At least 80% of critical IRON operators have EXACT or COMPATIBLE FastFlowLM kernel matches
    - Critical operators: GEMM, RMSNorm, RoPE, SwiGLU, Softmax
2. **Loading Feasibility**: .xclbin files can be loaded programmatically (via xclbinutil or custom parser)
3. **No Legal Blockers**: Licensing review shows no redistribution restrictions blocking integration
4. **Runtime API Parity**: xDNA runtime provides equivalent functionality to XRT for:
    - Device enumeration
    - Buffer allocation
    - Kernel loading
    - Kernel execution

### NO-GO Triggers (Any triggers NO-GO)

1. **Kernel Incompatibility**: Critical operators (GEMM, RMSNorm) have INCOMPATIBLE kernel interfaces
2. **Format Mismatch**: .xclbin files are platform-specific and cannot be cross-loaded
3. **Legal Restrictions**: FastFlowLM kernels cannot be redistributed
4. **Runtime API Gaps**: xDNA runtime missing critical functionality (buffer management, kernel execution)

### NO-GO Contingency Plan

If NO-GO decision is reached:

1. **Option A**: Linux-only backend (XRT), Windows deferred
2. **Option B**: Continue with IRON's MLIR runtime compilation for both platforms
3. **Option C**: Partner with AMD/FastFlowLM team for kernel interface documentation

## Week 3-5: C++ Runtime Abstraction

**Assumption**: GO decision made at Week 2 review

### Deliverables

| Component | File | Status |
|-----------|------|--------|
| Core interface | `iron/runtime/ixclbin_runtime.h` | Draft above |
| Buffer interface | `iron/runtime/ibuffer.h` | To implement |
| Platform utilities | `iron/runtime/platform_utils.h/.cpp` | To implement |
| XRT implementation | `iron/runtime/xrt_runtime.h/.cpp` | To implement |
| xDNA implementation | `iron/runtime/xdna_runtime.h/.cpp` | To implement |
| CMake configuration | `iron/runtime/CMakeLists.txt` | To implement |

### Week 3 Milestones

- [ ] Finalize `IXclbinRuntime` interface design
- [ ] Implement `IBuffer` interface
- [ ] Implement platform detection utilities
- [ ] Set up CMake build configuration

### Week 4 Milestones

- [ ] Complete XRT runtime implementation (Linux)
- [ ] Basic kernel loading working on Linux
- [ ] Unit tests for XRT runtime

### Week 5 Milestones

- [ ] Complete xDNA runtime implementation (Windows)
- [ ] Basic kernel loading working on Windows
- [ ] Unit tests for xDNA runtime
- [ ] Cross-platform build verification

## Week 6-10: Linux XRT Backend

### Week 6-7: MLIR Integration

- [ ] Integrate with IRON's MLIR compilation system
- [ ] Runtime compilation via `aiecc.py`
- [ ] .xclbin caching strategy

### Week 8-9: Buffer Management

- [ ] Implement buffer pooling
- [ ] Zero-copy buffer optimization
- [ ] Host-to-device transfer optimization

### Week 10: Integration Testing

- [ ] End-to-end tests with IRON operators
- [ ] Performance benchmarking
- [ ] Documentation

---

# PART 5: Technical Questions for FastFlowLM Team

## Kernel Interface Specifications

1. **What is the exact kernel ABI** for FastFlowLM kernels?
    - Argument ordering and types
    - Scalar vs buffer argument conventions
    - Memory layout expectations (row-major vs column-major)

2. **Are kernel interfaces stable** across FastFlowLM versions?
    - Versioning scheme for kernel interfaces
    - Backward compatibility guarantees

3. **What are the work group dimensions** for each kernel?
    - Local work size (X, Y, Z)
    - Global work size calculation

4. **Do kernels support dynamic dispatch** (runtime problem sizes) or are they compiled for fixed dimensions?

## .xclbin Format Details

5. **Are FastFlowLM .xclbin files cross-platform** (same file works on Linux and Windows)?
    - If not, what are the differences?
    - Is there a common subset that works on both?

6. **What XRT/xdna runtime version** is required to load FastFlowLM .xclbin files?

7. **Can .xclbin files be loaded from memory** (not just file path)?
    - Needed for embedded scenarios

8. **What sections are required** in the .xclbin for kernel execution?
    - Can we strip unnecessary sections to reduce size?

## Licensing and Redistribution

9. **Can FastFlowLM .xclbin kernels be redistributed** as part of IRON?
    - License terms for kernel binaries
    - Attribution requirements

10. **Are there model-specific restrictions** on kernel usage?
    - Do kernels from `llama-3.2-1b` work for other models?
    - Per-model kernel licensing?

11. **Can we ship FastFlowLM kernels** as part of Lemonade backend installation?
    - Installation mechanism
    - EULA requirements

## Compatibility with IRON Operators

12. **What is the mapping between FastFlowLM kernels and standard LLM operators?**
    - Does `attn.xclbin` contain QKV projection, attention, and output projection?
    - Or are these separate kernels?

13. **What precision do kernels support?**
    - FP16, BF16, INT8, FP8?
    - Mixed precision support?

14. **Do kernels support variable sequence lengths** or are they fixed at compilation time?

15. **What is the recommended batch size** for optimal performance?
    - Static vs dynamic batching

## Runtime Integration

16. **What is the proper initialization sequence** for the xDNA/XRT runtime?
    - Device enumeration
    - Context creation
    - Kernel loading

17. **Are there any special environment variables** or configuration needed?

18. **What error handling mechanisms** are available?
    - Kernel execution failures
    - Timeout handling

19. **Is there a recommended profiling approach** for kernel execution?
    - Execution time measurement
    - Memory bandwidth monitoring

## Future Roadmap

20. **What is the FastFlowLM roadmap** for new operator support?
    - Upcoming kernel releases
    - Planned features

21. **Is AMD planning to open-source** any part of FastFlowLM kernel library?

22. **Can we collaborate on kernel interface standardization** to improve interoperability?

---

# Appendix A: Discovery Environment Setup

## Required Tools

### Linux

```bash
# XRT installation (if not already present)
sudo apt install xilinx-xrt

# xclbinutil for .xclbin inspection
sudo apt install xilinx-xclbinutil

# Python dependencies
pip install pyxrt ml-dtypes numpy

# Verify installation
python3 -c "import pyxrt; print(pyxrt.__version__)"
xclbinutil --version
```

### Windows

```powershell
# AMD XDNA driver (should be installed with NPU hardware)
# Verify installation
Get-Module -ListAvailable | Select-String "xdna"

# Python dependencies
pip install numpy

# FastFlowLM (if available)
# Follow AMD FastFlowLM installation guide
```

## Directory Structure

```
IRON/
├── discovery/
│   ├── fastflowlm/
│   │   ├── xclbins/           # Copied .xclbin files
│   │   ├── kernels/           # JSON kernel descriptions
│   │   └── kernel_audit.md    # Final report
│   ├── xdna/
│   │   ├── xrt_api.json
│   │   ├── xdna_api.json
│   │   └── runtime_audit.md
│   ├── xclbin_format/
│   │   ├── analysis.json
│   │   └── analysis.md
│   └── lemonade/
│       └── wrapped_server_api.md
├── runtime/
│   ├── tools/                 # Discovery scripts
│   │   ├── xclbin_inspector.py
│   │   ├── kernel_comparator.py
│   │   ├── runtime_api_audit.py
│   │   └── xclbin_format_analyzer.py
│   ├── ixclbin_runtime.h      # Interface design
│   └── ...                    # Implementation (Week 3-5)
└── docs/
    └── TECHNICAL_DESIGN_DISCOVERY_PHASE.md  # This document
```

---

# Appendix B: Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| R1: FastFlowLM kernels incompatible with IRON | Medium | High | Early audit (Week 1), fallback to MLIR compilation |
| R2: xDNA runtime API insufficient | Medium | High | Runtime audit (Week 1), CPU fallback path |
| R3: .xclbin format is platform-specific | Low | High | Format analysis (Week 1), separate compilation paths |
| R4: Licensing blocks redistribution | Low | Critical | Legal review early, document findings |
| R5: No Windows test environment available | Medium | Medium | Use Linux for development, remote Windows testing |

---

**Document End**

*Copyright &copy; 2026 Advanced Micro Devices, Inc. All rights reserved.*
