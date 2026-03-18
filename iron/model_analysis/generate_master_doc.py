#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Master Document Generator for IRON Operator Creation

Generates a COMPLETE, self-contained markdown document with ALL data needed
to implement a custom NPU operator for a specific layer.

Usage:
    python -m iron.model_analysis.generate_master_doc <model_name> <layer_name> [-o output.md]

Example:
    python -m iron.model_analysis.generate_master_doc mistralai/Mistral-7B-v0.1 MistralAttention -o mistral_attention_master.md
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from .transformers_integration import scan_model_from_transformers
from .operator_spec import generate_operator_spec, OperatorSpec


def extract_layer_source(model_name: str, layer_name: str) -> str:
    """Extract the actual forward() source code for a layer."""
    from .operator_spec import OperatorSpecGenerator

    generator = OperatorSpecGenerator()
    info = scan_model_from_transformers(model_name)

    layer_class = generator._get_layer_class(info.modeling_module, layer_name)
    if layer_class is None:
        return "# Could not find layer class"

    try:
        import inspect

        source = inspect.getsource(layer_class.forward)
        # Clean up indentation
        lines = source.split("\n")
        while lines and not lines[0].strip():
            lines.pop(0)
        min_indent = min(
            (len(line) - len(line.lstrip())) for line in lines if line.strip()
        )
        lines = [
            line[min_indent:] if len(line) >= min_indent else line for line in lines
        ]
        return "\n".join(lines)
    except Exception as e:
        return f"# Could not extract source: {e}"


def get_operator_base_class(layer_name: str) -> str:
    """Suggest IRON base class based on layer name."""
    layer_lower = layer_name.lower()

    base_class_map = {
        "attention": "AIEGEMM + custom attention mechanism",
        "selfattention": "AIEGEMM + custom attention mechanism",
        "multihead": "AIEMHA",
        "sliding": "AIEOperatorBase (custom sliding window)",
        "norm": "AIERMSNorm",
        "layernorm": "AIELayerNorm",
        "rmsnorm": "AIERMSNorm",
        "mlp": "AIEGEMM",
        "ffn": "AIEGEMM",
        "dense": "AIEGEMM",
        "linear": "AIEGEMM",
        "moe": "AIEOperatorBase (custom MoE routing)",
        "expert": "AIEOperatorBase (custom routing)",
        "rope": "AIERoPE",
        "rotary": "AIERoPE",
        "embedding": "AIEEmbedding",
    }

    for pattern, base_class in base_class_map.items():
        if pattern in layer_lower:
            return base_class

    return "AIEOperatorBase (custom)"


def generate_skeleton_code(
    layer_name: str, config: Dict[str, Any], base_class: str
) -> str:
    """Generate Python skeleton code for the operator."""

    # Extract key hyperparameters
    hidden_size = config.get("hidden_size", 4096)
    num_heads = config.get("num_attention_heads", 32)
    num_kv_heads = config.get("num_key_value_heads", num_heads)
    intermediate_size = config.get("intermediate_size", 11008)

    return f'''# SPDX-FileCopyrightText: Copyright (C) 2025 AMD
# SPDX-License-Identifier: Apache-2.0

"""
{layer_name} NPU Operator

AUTO-GENERATED SKELETON - Fill in the TODOs

Base class: {base_class}
"""

from iron.common import AIEOperatorBase, AIEContext
from iron.common.compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    PythonGeneratedMLIRArtifact,
)
from pathlib import Path


class AIE{layer_name.replace("ForCausalLM", "").replace("Model", "")}(AIEOperatorBase):
    """
    NPU implementation of {layer_name}.

    TODO: Review the master document to understand:
    1. What computations this layer performs
    2. What hyperparameters are needed
    3. What the forward() signature looks like
    """

    def __init__(
        self,
        hidden_size: int = {hidden_size},
        num_heads: int = {num_heads},
        num_kv_heads: int = {num_kv_heads},
        intermediate_size: int = {intermediate_size},
        context=None,
    ):
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.num_kv_heads = num_kv_heads
        self.intermediate_size = intermediate_size
        super().__init__(context=context)

    def set_up_artifacts(self):
        """
        Set up compilation artifacts.

        TODO:
        1. Create MLIR generation callback in design.py
        2. Define xclbin, insts_bin, kernel_obj, kra artifacts
        3. Link to design.py generate_mlir() function
        """
        operator_dir = Path(__file__).parent

        # TODO: Create the MLIR artifact pointing to design.py
        self.mlir_artifact = PythonGeneratedMLIRArtifact.new(
            "{layer_name.lower()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="generate_mlir",
            callback_kwargs={{
                "hidden_size": self.hidden_size,
                "num_heads": self.num_heads,
                "num_kv_heads": self.num_kv_heads,
            }},
        )

        # TODO: Create compilation artifacts
        self.xclbin_artifact = XclbinArtifact.new(
            "{layer_name.lower()}.xclbin",
            mlir_artifact=self.mlir_artifact,
        )

        self.insts_bin_artifact = InstsBinArtifact.new(
            "{layer_name.lower()}.insts.bin",
            xclbin_artifact=self.xclbin_artifact,
        )

        self.kernel_obj_artifact = KernelObjectArtifact.new(
            "{layer_name.lower()}.o",
            xclbin_artifact=self.xclbin_artifact,
        )

        self.kra_artifact = KernelArchiveArtifact.new(
            "{layer_name.lower()}.kra",
            kernel_obj_artifacts=[self.kernel_obj_artifact],
        )

    def set_up_runtime(self):
        """
        Set up runtime buffers and kernels.

        TODO:
        1. Define input/output buffers with correct sizes
        2. Define kernels for each operation
        3. Build runlist
        """
        # TODO: Input buffer - adjust size based on actual tensor shapes
        self.add_buffer("input", self.hidden_size * 2)  # bytes (bf16)

        # TODO: Weight buffers
        # self.add_buffer("weight_name", size_in_bytes)

        # TODO: Output buffer
        self.add_buffer("output", self.hidden_size * 2)  # bytes (bf16)

        # TODO: Define kernels
        # self.add_kernel("kernel_name", input_buffers=[...], output_buffers=[...])

        # TODO: Build runlist
        # self.add_to_runlist("kernel_name", "buffer1", "buffer2", ...)

    def forward(self, hidden_states, *args, **kwargs):
        """
        Forward pass.

        Args:
            hidden_states: Input tensor [batch, seq_len, hidden_size]
            *args: Additional arguments (see master doc for signature)
            **kwargs: Additional keyword arguments

        Returns:
            Output tensor [batch, seq_len, hidden_size]
        """
        batch_size, seq_len, _ = hidden_states.shape

        # TODO: Write input to NPU buffer
        # self.write_buffer("input", hidden_states)

        # TODO: Execute runlist
        # self.run_runlist()

        # TODO: Read output from NPU buffer
        # output_shape = (batch_size, seq_len, self.hidden_size)
        # result = self.read_buffer_as_torch("output", shape=output_shape)

        # Placeholder - replace with actual implementation
        return hidden_states


def generate_mlir(hidden_size, num_heads, num_kv_heads):
    """
    MLIR generation callback for {layer_name}.

    This function is called by the PythonGeneratedMLIRArtifact
    to generate the MLIR program.

    TODO:
    1. Import aie.iron dialect
    2. Define device type (XC35 for Ryzen AI)
    3. Create Runtime with sequence of operations
    4. Define ObjectFifos for data movement
    5. Define compute kernels
    6. Return MLIR module
    """
    import aie
    from aie.iron import Kernel, ObjectFifo, Program, Buffer, Runtime
    from aie.iron.placers import SequentialPlacer

    device_type = aie.device.XC35
    rt = Runtime()

    # TODO: Define your MLIR program
    # Example structure:
    # with rt.sequence(dtype, "input", "output") as (win, wout):
    #     # Load data from DRAM
    #     # Compute on NPU
    #     # Store results

    program = Program(device_type, rt)
    module = program.resolve_program(SequentialPlacer())
    return module
'''


def generate_master_document(model_name: str, layer_name: str) -> str:
    """Generate a complete master document with all data for implementing an operator."""

    # Gather all data
    print(f"Scanning model: {model_name}...")
    info = scan_model_from_transformers(model_name)
    config = info.config_dict

    print(f"Generating operator spec for: {layer_name}...")
    try:
        spec = generate_operator_spec(model_name, layer_name)
        forward_source = spec.forward_source
        operations = spec.operations
        inputs = spec.inputs
        outputs = spec.outputs
        hyperparams = spec.hyperparameters
        special_handling = spec.special_handling
        base_class = spec.suggested_base_class
    except Exception as e:
        print(f"Warning: Could not generate full spec: {e}")
        forward_source = "# Could not extract source"
        operations = []
        inputs = []
        outputs = []
        hyperparams = []
        special_handling = []
        base_class = get_operator_base_class(layer_name)

    # Get layer source
    layer_source = extract_layer_source(model_name, layer_name)

    # Generate skeleton code
    skeleton_code = generate_skeleton_code(layer_name, config, base_class)

    # Build the master document
    doc_lines = [
        "# Operator Master Document",
        "",
        f"**Layer:** `{layer_name}`",
        f"**Model:** {model_name}",
        f"**Model Type:** {info.model_type}",
        f"**Generated:** This document contains ALL data needed to implement this operator",
        "",
        "---",
        "",
        "## Quick Reference",
        "",
        f"| Property | Value |",
        f"|----------|-------|",
        f"| **Base Class** | `{base_class}` |",
        f"| **Hidden Size** | {config.get('hidden_size', 'N/A')} |",
        f"| **Num Heads** | {config.get('num_attention_heads', 'N/A')} |",
        f"| **KV Heads** | {config.get('num_key_value_heads', config.get('num_attention_heads', 'N/A'))} |",
        f"| **Intermediate Size** | {config.get('intermediate_size', 'N/A')} |",
        "",
    ]

    # Special features
    special_features = []
    if info.has_sliding_window:
        special_features.append(
            f"Sliding Window: {config.get('sliding_window', 'enabled')}"
        )
    if info.has_moe:
        special_features.append(
            f"MoE: {config.get('num_experts', 'N/A')} experts, {config.get('num_experts_per_tok', 'N/A')} per token"
        )
    if info.has_rope:
        special_features.append(f"RoPE: theta={config.get('rope_theta', 'N/A')}")
    if info.has_qk_norm:
        special_features.append(f"QK Norm: enabled")

    if special_features:
        doc_lines.extend(
            [
                "**Special Features:**",
                "",
            ]
        )
        for feature in special_features:
            doc_lines.append(f"- {feature}")
        doc_lines.append("")

    # Attention type
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 1. Hyperparameters",
            "",
            "These values must be passed to the operator constructor:",
            "",
            "| Name | Value | Dtype | Description |",
            "|------|-------|-------|-------------|",
        ]
    )

    for hp in hyperparams[:15]:  # Limit to top 15
        doc_lines.append(f"| `{hp.name}` | `{hp.value}` | {hp.dtype} | |")

    doc_lines.extend(
        [
            "",
            "### Constructor Template",
            "",
            "```python",
            f"class AIE{layer_name.replace('ForCausalLM', '').replace('Model', '')}(AIEOperatorBase):",
            "    def __init__(",
            "        self,",
        ]
    )

    for hp in hyperparams[:10]:
        default = hp.value if hp.value is not None else "None"
        doc_lines.append(f"        {hp.name}: {hp.dtype} = {default},")

    doc_lines.extend(
        [
            "    ):",
            "        # Store hyperparameters",
            "        pass",
            "```",
            "",
        ]
    )

    # Input/Output signatures
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 2. Forward Signature",
            "",
            "### Inputs",
            "",
            "| Name | Shape | Dtype | Description |",
            "|------|-------|-------|-------------|",
        ]
    )

    for inp in inputs:
        doc_lines.append(
            f"| `{inp.name}` | {inp.shape} | {inp.dtype} | {inp.description} |"
        )

    if not inputs:
        doc_lines.append(
            f"| `hidden_states` | `[batch, seq_len, {config.get('hidden_size', '?')}]` | torch.float16 | Input tensor |"
        )

    doc_lines.extend(
        [
            "",
            "### Outputs",
            "",
            "| Name | Shape | Dtype | Description |",
            "|------|-------|-------|-------------|",
        ]
    )

    for out in outputs:
        doc_lines.append(
            f"| `{out.name}` | {out.shape} | {out.dtype} | {out.description} |"
        )

    if not outputs:
        doc_lines.append(
            f"| `output` | `[batch, seq_len, {config.get('hidden_size', '?')}]` | torch.float16 | Output tensor |"
        )

    doc_lines.extend(
        [
            "",
            "### forward() Method Template",
            "",
            "```python",
            "def forward(self, hidden_states, attention_mask=None, position_embeddings=None, **kwargs):",
            '    """',
            "    Forward pass for " + layer_name + ".",
            "    ",
            "    Args:",
        ]
    )

    for inp in inputs[:5]:
        doc_lines.append(f"        {inp.name}: {inp.description} (shape: {inp.shape})")

    doc_lines.extend(
        [
            "    ",
            "    Returns:",
            "        Output tensor [batch, seq_len, hidden_size]",
            '    """',
            "    # Implementation below",
            "```",
            "",
        ]
    )

    # Reference implementation
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 3. Reference Implementation (Transformers)",
            "",
            "**Source:** This is the EXACT code from Transformers that your NPU operator must replicate.",
            "",
            "```python",
            layer_source,
            "```",
            "",
        ]
    )

    # Operations analysis
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 4. Operations Analysis",
            "",
            "These PyTorch operations are used in the forward() method.",
            "Each must be translated to AIE/MLIR equivalents:",
            "",
        ]
    )

    if operations:
        for op in set(operations):
            doc_lines.append(f"- `{op}`")
    else:
        doc_lines.append("- (Could not analyze - review source code above)")

    doc_lines.extend(
        [
            "",
            "### Computation Flow",
            "",
            "Based on the reference implementation above, the computation flow is:",
            "",
            "1. **Input processing** - Receive hidden_states tensor",
            "2. **Projection** - Apply QKV linear projections",
            "3. **Reshape** - Restructure tensors for multi-head attention",
            "4. **Position embeddings** - Apply RoPE if present",
            "5. **Attention computation** - Compute attention weights and apply",
            "6. **Output projection** - Final linear projection",
            "",
        ]
    )

    # Special handling
    if special_handling:
        doc_lines.extend(
            [
                "",
                "---",
                "",
                "## 5. Special Handling Required",
                "",
                "**CRITICAL:** This layer has special requirements:",
                "",
            ]
        )
        for handling in special_handling:
            doc_lines.append(f"- {handling}")
        doc_lines.append("")

    # Implementation checklist
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 6. Implementation Checklist",
            "",
            "### Files to Create",
            "",
            "```\n",
            f"{layer_name.lower()}/",
            f"├── {layer_name.lower()}.py      # Operator class (skeleton below)",
            f"├── design.py               # MLIR generation",
            f"├── test.py                 # Unit tests",
            f"└── MASTER_DOC.md           # This document",
            "```",
            "",
            "### Steps",
            "",
            "- [ ] Review reference implementation (Section 3)",
            "- [ ] Understand operations needed (Section 4)",
            "- [ ] Fill in operator skeleton (Section 7)",
            "- [ ] Implement design.py MLIR generation",
            "- [ ] Define input/output buffers matching signatures (Section 2)",
            "- [ ] Implement tiling strategy for tensor sizes",
            "- [ ] Write unit tests against Transformers reference",
            "- [ ] Compare outputs for correctness",
            "",
        ]
    )

    # Skeleton code
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 7. Operator Skeleton (Copy This Code)",
            "",
            f"**File:** `{layer_name.lower()}/{layer_name.lower()}.py`",
            "",
            "```python",
            skeleton_code,
            "```",
            "",
        ]
    )

    # MLIR design template
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 8. MLIR Design Template",
            "",
            f"**File:** `{layer_name.lower()}/design.py`",
            "",
            "```python",
            """# SPDX-FileCopyrightText: Copyright (C) 2025 AMD
# SPDX-License-Identifier: Apache-2.0

\"\"\"
MLIR Generation for """
            + layer_name
            + """
\"\"\"

import aie
from aie.iron import Kernel, ObjectFifo, Program, Buffer, Runtime
from aie.iron.placers import SequentialPlacer


def generate_mlir(hidden_size, num_heads, num_kv_heads):
    \"\"\"
    Generate MLIR for """
            + layer_name
            + """.

    TODO: Study the reference implementation in MASTER_DOC.md Section 3
    and translate each operation to AIE/MLIR.
    \"\"\"
    device_type = aie.device.XC35
    rt = Runtime()

    # TODO: Define your MLIR program
    # 1. Create buffers for inputs, weights, outputs
    # 2. Create ObjectFifos for data movement
    # 3. Create kernels for compute
    # 4. Build runlist

    # Example structure:
    # with rt.sequence(aie_dtype, "in", "out") as (win, wout):
    #     # Define data flow
    #     pass

    program = Program(device_type, rt)
    module = program.resolve_program(SequentialPlacer())
    return module
""",
            "```",
            "",
        ]
    )

    # Resources
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "## 9. Resources",
            "",
            "### Documentation",
            "",
            f"- [IRON CREATING_OPERATORS.md](../CREATING_OPERATORS.md) - Complete workflow guide",
            f"- [IRON DATA_SOURCES_GUIDE.md](../DATA_SOURCES_GUIDE.md) - Data extraction reference",
            "- [mlir-aie docs](https://github.com/Xilinx/mlir-aie/tree/main/docs) - AIE/MLIR reference",
            "",
            "### Example Operators",
            "",
            "- `iron/operators/gemm/` - Matrix multiplication",
            "- `iron/operators/rms_norm/` - Normalization",
            "- `iron/operators/rope/` - RoPE embeddings",
            "- `iron/operators/mha/` - Multi-head attention",
            "",
            "### HuggingFace References",
            "",
            f"- Model: https://huggingface.co/{model_name}",
            f"- Config: https://huggingface.co/{model_name}/raw/main/config.json",
            "",
        ]
    )

    # Footer
    doc_lines.extend(
        [
            "",
            "---",
            "",
            "*Generated by `python -m iron.model_analysis.generate_master_doc`*",
            "",
        ]
    )

    return "\n".join(doc_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate master document for implementing a custom IRON operator"
    )
    parser.add_argument(
        "model_name", help="HuggingFace model name (e.g., mistralai/Mistral-7B-v0.1)"
    )
    parser.add_argument("layer_name", help="Layer class name (e.g., MistralAttention)")
    parser.add_argument(
        "-o",
        "--output",
        default="MASTER_DOC.md",
        help="Output file path (default: MASTER_DOC.md)",
    )
    parser.add_argument(
        "--trust-remote-code",
        action="store_true",
        help="Trust remote code from HuggingFace Hub",
    )

    args = parser.parse_args()

    print(f"{'='*60}")
    print(f"IRON Master Document Generator")
    print(f"{'='*60}")
    print(f"Model: {args.model_name}")
    print(f"Layer: {args.layer_name}")
    print(f"Output: {args.output}")
    print(f"{'='*60}")
    print()

    # Generate document
    doc = generate_master_document(args.model_name, args.layer_name)

    # Write to file
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(doc)

    print()
    print(f"{'='*60}")
    print(f"Master document generated: {output_path.absolute()}")
    print(f"{'='*60}")
    print()
    print("Next steps:")
    print(f"  1. Review {args.output}")
    print(f"  2. Create operator directory: mkdir {args.layer_name.lower()}")
    print(f"  3. Copy skeleton code from Section 7")
    print(f"  4. Implement design.py based on Section 8")
    print(f"  5. Write tests against Transformers reference")


if __name__ == "__main__":
    main()
