# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Operator Specification Generator

Generates comprehensive specifications for implementing custom NPU operators.
Extracts information from Transformers source code and model configs to create
actionable documentation for IRON operator development.

Usage:
    from iron.model_analysis.operator_spec import generate_operator_spec
    spec = generate_operator_spec("mistralai/Mistral-7B-v0.1", "MistralAttention")
    print(spec.to_markdown())
"""

import inspect
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Callable
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


@dataclass
class TensorSpec:
    """Specification for a tensor input/output"""

    name: str
    shape: str
    dtype: str
    description: str = ""


@dataclass
class HyperparameterSpec:
    """Specification for a hyperparameter"""

    name: str
    value: Any
    dtype: str
    description: str = ""


@dataclass
class OperatorSpec:
    """Complete specification for a custom operator"""

    # Identification
    layer_name: str
    model_name: str
    model_type: str
    module_path: str

    # Purpose
    purpose: str = ""
    description: str = ""

    # Signatures
    inputs: List[TensorSpec] = field(default_factory=list)
    outputs: List[TensorSpec] = field(default_factory=list)

    # Hyperparameters
    hyperparameters: List[HyperparameterSpec] = field(default_factory=list)

    # Source code
    forward_signature: str = ""
    forward_source: str = ""

    # IRON integration
    suggested_base_class: str = ""
    iron_integration_notes: str = ""

    # Operations used
    operations: List[str] = field(default_factory=list)

    # Additional notes
    special_handling: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        """Generate markdown documentation"""
        lines = [
            f"# Operator Specification: {self.layer_name}",
            f"",
            f"**Model:** {self.model_name}",
            f"**Type:** {self.model_type}",
            f"**Module:** {self.module_path}",
            f"",
        ]

        # Purpose
        if self.purpose or self.description:
            lines.extend(
                [
                    "## Purpose",
                    f"",
                    self.purpose,
                    self.description,
                    f"",
                ]
            )

        # Mathematical formulation
        lines.extend(
            [
                "## Mathematical Formulation",
                f"",
                "*TODO: Add mathematical description based on forward() analysis*",
                f"",
            ]
        )

        # Inputs
        if self.inputs:
            lines.extend(
                [
                    "## Inputs",
                    f"",
                    "| Name | Shape | Dtype | Description |",
                    "|------|-------|-------|-------------|",
                ]
            )
            for inp in self.inputs:
                lines.append(
                    f"| {inp.name} | {inp.shape} | {inp.dtype} | {inp.description} |"
                )
            lines.append("")

        # Outputs
        if self.outputs:
            lines.extend(
                [
                    "## Outputs",
                    f"",
                    "| Name | Shape | Dtype | Description |",
                    "|------|-------|-------|-------------|",
                ]
            )
            for out in self.outputs:
                lines.append(
                    f"| {out.name} | {out.shape} | {out.dtype} | {out.description} |"
                )
            lines.append("")

        # Hyperparameters
        if self.hyperparameters:
            lines.extend(
                [
                    "## Hyperparameters (from config)",
                    f"",
                    "| Name | Value | Dtype | Description |",
                    "|------|-------|-------|-------------|",
                ]
            )
            for hp in self.hyperparameters:
                lines.append(
                    f"| {hp.name} | {hp.value} | {hp.dtype} | {hp.description} |"
                )
            lines.append("")

        # Operations
        if self.operations:
            lines.extend(
                [
                    "## Operations Used",
                    f"",
                ]
            )
            for op in self.operations:
                lines.append(f"- `{op}`")
            lines.append("")

        # IRON Integration
        lines.extend(
            [
                "## IRON Integration",
                f"",
                f"**Suggested Base Class:** `{self.suggested_base_class}`",
                f"",
            ]
        )

        if self.iron_integration_notes:
            lines.extend(
                [
                    "**Integration Notes:**",
                    self.iron_integration_notes,
                    f"",
                ]
            )

        if self.special_handling:
            lines.extend(
                [
                    "**Special Handling Required:**",
                ]
            )
            for note in self.special_handling:
                lines.append(f"- {note}")
            lines.append("")

        # Source code
        if self.forward_source:
            lines.extend(
                [
                    "## Reference Implementation (Transformers)",
                    f"",
                    "```python",
                    self.forward_source,
                    "```",
                    f"",
                ]
            )

        # Action items
        lines.extend(
            [
                "## Implementation Checklist",
                f"",
                f"- [ ] Create `{self.layer_name}NPU` class extending `{self.suggested_base_class}`",
                f"- [ ] Implement forward pass matching signature",
                f"- [ ] Add AIE memory mapping for inputs/outputs",
                f"- [ ] Implement tiling strategy for NPU",
                f"- [ ] Write unit tests against Transformers reference",
                f"- [ ] Add to operator registry",
                f"",
            ]
        )

        # References
        if self.references:
            lines.extend(
                [
                    "## References",
                    f"",
                ]
            )
            for ref in self.references:
                lines.append(f"- {ref}")
            lines.append("")

        return "\n".join(lines)


class OperatorSpecGenerator:
    """
    Generates operator specifications from Transformers models.

    Usage:
        generator = OperatorSpecGenerator()
        spec = generator.generate("mistralai/Mistral-7B-v0.1", "MistralAttention")
    """

    # Mapping of layer patterns to IRON base classes
    IRON_BASE_CLASS_MAP = {
        # Attention patterns
        "attention": "AIEGEMM + custom attention mask",
        "selfattention": "AIEGEMM + custom attention mask",
        "multihead": "AIEMHA",
        "sliding": "AIEGEMM (needs sliding window extension)",
        # Normalization patterns
        "norm": "AIERMSNorm",
        "layernorm": "AIELayerNorm",
        "rmsnorm": "AIERMSNorm",
        # FFN patterns
        "mlp": "AIEGEMM",
        "ffn": "AIEGEMM",
        "dense": "AIEGEMM",
        "linear": "AIEGEMM",
        # MoE patterns
        "moe": "AIEGEMM + custom routing",
        "expert": "AIEGEMM + custom routing",
        "switch": "AIEGEMM + custom routing",
        # Positional patterns
        "rope": "AIERoPE",
        "rotary": "AIERoPE",
        "positional": "AIEEmbedding",
        # Embedding patterns
        "embedding": "AIEEmbedding",
    }

    # Config keys relevant to different layer types
    CONFIG_KEY_MAP = {
        "attention": [
            "hidden_size",
            "num_attention_heads",
            "num_key_value_heads",
            "head_dim",
            "attention_dropout",
            "sliding_window",
        ],
        "norm": [
            "rms_norm_eps",
            "layer_norm_eps",
            "norm_eps",
        ],
        "mlp": [
            "intermediate_size",
            "hidden_size",
        ],
        "rope": [
            "rope_theta",
            "rope_scaling",
            "max_position_embeddings",
        ],
        "moe": [
            "num_experts",
            "num_experts_per_tok",
            "expert_intermediate_size",
            "moe_aux_loss_coeff",
        ],
    }

    def __init__(self):
        self._config_cache: Dict[str, Any] = {}
        self._module_cache: Dict[str, Any] = {}

    def generate(
        self,
        model_name: str,
        layer_name: str,
        trust_remote_code: bool = False,
    ) -> OperatorSpec:
        """
        Generate operator specification for a layer.

        Args:
            model_name: HuggingFace model name
            layer_name: Name of the layer class (e.g., "MistralAttention")
            trust_remote_code: Whether to trust remote code

        Returns:
            OperatorSpec with complete specification
        """
        from .transformers_integration import scan_model_from_transformers

        # Scan the model to get info
        info = scan_model_from_transformers(model_name, trust_remote_code)

        # Find the layer class
        layer_class = self._get_layer_class(info.modeling_module, layer_name)
        if layer_class is None:
            raise ValueError(f"Could not find layer class: {layer_name}")

        # Create spec object
        spec = OperatorSpec(
            layer_name=layer_name,
            model_name=model_name,
            model_type=info.model_type,
            module_path=info.modeling_module or "",
        )

        # Extract purpose from docstring
        spec.purpose, spec.description = self._extract_docstring(layer_class)

        # Extract inputs/outputs from signature
        spec.inputs, spec.outputs = self._extract_signature(
            layer_class, info.config_dict
        )

        # Extract hyperparameters from config
        spec.hyperparameters = self._extract_hyperparameters(
            layer_name, info.config_dict
        )

        # Extract source code
        spec.forward_signature, spec.forward_source = self._extract_source(layer_class)

        # Analyze operations
        spec.operations = self._analyze_operations(spec.forward_source)

        # Suggest IRON base class
        spec.suggested_base_class = self._suggest_iron_base(layer_name)

        # Generate integration notes
        spec.iron_integration_notes = self._generate_iron_notes(spec)

        # Check for special handling
        spec.special_handling = self._check_special_handling(info, layer_name)

        # Add references
        spec.references = [
            f"Transformers source: {info.modeling_module}",
            f"HuggingFace model: https://huggingface.co/{model_name}",
        ]

        return spec

    def _get_layer_class(
        self,
        module_path: str,
        layer_name: str,
    ) -> Optional[type]:
        """Get the layer class from transformers module"""
        import importlib

        # Try multiple import paths
        import_paths = [
            f"{module_path}.modeling_{module_path.split('.')[-1]}",  # transformers.models.mistral.modeling_mistral
            module_path,  # transformers.models.mistral
            f"transformers.models.{layer_name.lower().replace('forcausallm', '').replace('model', '')}",  # fallback
        ]

        for path in import_paths:
            try:
                module = importlib.import_module(path)
                cls = getattr(module, layer_name, None)
                if cls is not None:
                    return cls
            except Exception:
                continue

        # Last resort: search all transformers.models submodules
        try:
            import transformers.models

            for attr_name in dir(transformers.models):
                try:
                    submodule = getattr(transformers.models, attr_name)
                    if hasattr(submodule, layer_name):
                        return getattr(submodule, layer_name)
                except Exception:
                    continue
        except Exception:
            pass

        logger.warning(f"Could not find layer class: {layer_name} in {module_path}")
        return None

    def _extract_docstring(self, cls) -> Tuple[str, str]:
        """Extract purpose and description from docstring"""
        docstring = inspect.getdoc(cls) or ""

        # Split into first sentence (purpose) and rest (description)
        if "." in docstring:
            parts = docstring.split(".", 1)
            purpose = parts[0].strip() + "."
            description = parts[1].strip() if len(parts) > 1 else ""
        else:
            purpose = docstring.strip()
            description = ""

        return purpose, description

    def _extract_signature(
        self,
        cls,
        config_dict: Dict[str, Any],
    ) -> Tuple[List[TensorSpec], List[TensorSpec]]:
        """Extract input/output tensor specifications"""
        inputs = []
        outputs = []

        try:
            sig = inspect.signature(cls.forward)

            # Get hidden size from config
            hidden_size = config_dict.get("hidden_size", "unknown")
            num_heads = config_dict.get("num_attention_heads", "unknown")

            # Analyze parameters
            for name, param in sig.parameters.items():
                if name == "self":
                    continue

                # Infer tensor info from annotation
                annotation = param.annotation
                shape = "unknown"
                dtype = "unknown"
                description = ""

                # Try to infer from name and annotation
                if "hidden_states" in name.lower():
                    shape = f"[batch, seq_len, {hidden_size}]"
                    dtype = "torch.float16"
                    description = "Input hidden states"
                elif "attention_mask" in name.lower():
                    shape = "[batch, seq_len] or [batch, heads, seq_len, seq_len]"
                    dtype = "torch.float32"
                    description = "Attention mask (optional)"
                elif "position" in name.lower():
                    shape = "[batch, seq_len] or tuple of [seq_len, head_dim]"
                    dtype = "torch.float32"
                    description = "Position IDs or embeddings"
                elif "past_key" in name.lower() or "cache" in name.lower():
                    shape = "Cache object"
                    dtype = "torch.float16"
                    description = "KV cache (optional)"

                if shape != "unknown":
                    inputs.append(
                        TensorSpec(
                            name=name,
                            shape=shape,
                            dtype=dtype,
                            description=description,
                        )
                    )

            # Infer outputs from return annotation
            return_annotation = sig.return_annotation
            if return_annotation != inspect.Signature.empty:
                return_str = str(return_annotation)
                if "tuple" in return_str.lower():
                    outputs.append(
                        TensorSpec(
                            name="hidden_states",
                            shape=f"[batch, seq_len, {hidden_size}]",
                            dtype="torch.float16",
                            description="Output hidden states",
                        )
                    )
                    if "attention" in return_str.lower():
                        outputs.append(
                            TensorSpec(
                                name="attention_weights",
                                shape="[batch, heads, seq_len, seq_len]",
                                dtype="torch.float32",
                                description="Attention weights (optional)",
                            )
                        )
                else:
                    outputs.append(
                        TensorSpec(
                            name="output",
                            shape=f"[batch, seq_len, {hidden_size}]",
                            dtype="torch.float16",
                            description="Layer output",
                        )
                    )
            else:
                # Default output
                outputs.append(
                    TensorSpec(
                        name="output",
                        shape=f"[batch, seq_len, {hidden_size}]",
                        dtype="torch.float16",
                        description="Layer output",
                    )
                )

        except Exception as e:
            logger.warning(f"Could not extract signature: {e}")

            # Fallback: create generic specs
            hidden_size = config_dict.get("hidden_size", "unknown")
            inputs.append(
                TensorSpec(
                    name="hidden_states",
                    shape=f"[batch, seq_len, {hidden_size}]",
                    dtype="torch.float16",
                    description="Input tensor",
                )
            )
            outputs.append(
                TensorSpec(
                    name="output",
                    shape=f"[batch, seq_len, {hidden_size}]",
                    dtype="torch.float16",
                    description="Output tensor",
                )
            )

        return inputs, outputs

    def _extract_hyperparameters(
        self,
        layer_name: str,
        config_dict: Dict[str, Any],
    ) -> List[HyperparameterSpec]:
        """Extract relevant hyperparameters from config"""
        hyperparams = []

        # Determine which config keys are relevant
        layer_lower = layer_name.lower()
        relevant_keys = set()

        for pattern, keys in self.CONFIG_KEY_MAP.items():
            if pattern in layer_lower:
                relevant_keys.update(keys)

        # Also add common keys
        common_keys = ["hidden_size", "vocab_size", "max_position_embeddings"]
        relevant_keys.update(common_keys)

        # Extract values
        for key in sorted(relevant_keys):
            if key in config_dict:
                value = config_dict[key]
                dtype = type(value).__name__
                hyperparams.append(
                    HyperparameterSpec(
                        name=key,
                        value=value,
                        dtype=dtype,
                    )
                )

        return hyperparams

    def _extract_source(self, cls) -> Tuple[str, str]:
        """Extract forward method source code"""
        try:
            forward_method = cls.forward

            # Get signature
            sig = inspect.signature(forward_method)
            sig_str = f"{cls.__name__}.forward{sig}"

            # Get source
            source = inspect.getsource(forward_method)

            # Clean up indentation
            source_lines = source.split("\n")
            # Remove leading empty lines
            while source_lines and not source_lines[0].strip():
                source_lines.pop(0)

            # Get minimum indentation
            min_indent = float("inf")
            for line in source_lines:
                if line.strip():
                    indent = len(line) - len(line.lstrip())
                    min_indent = min(min_indent, indent)

            # Remove common indentation
            if min_indent < float("inf"):
                source_lines = [
                    line[min_indent:] if len(line) >= min_indent else line
                    for line in source_lines
                ]

            source = "\n".join(source_lines)

            return sig_str, source

        except Exception as e:
            logger.warning(f"Could not extract source: {e}")
            return "", f"# Could not extract source: {e}"

    def _analyze_operations(self, source: str) -> List[str]:
        """Analyze source code to identify PyTorch operations used"""
        operations = []

        # Common PyTorch operations to look for
        torch_ops = [
            # Linear operations
            "linear",
            "conv2d",
            "conv1d",
            "embedding",
            # Activation functions
            "relu",
            "gelu",
            "silu",
            "swiglu",
            "sigmoid",
            "tanh",
            # Normalization
            "layer_norm",
            "rms_norm",
            "batch_norm",
            # Attention
            "softmax",
            "scaled_dot_product_attention",
            "einsum",
            # Tensor operations
            "transpose",
            "reshape",
            "view",
            "permute",
            "contiguous",
            "cat",
            "stack",
            "split",
            "chunk",
            # Math
            "matmul",
            "bmm",
            "mm",
            "add",
            "mul",
            "div",
            # RoPE
            "apply_rotary_pos_emb",
            "rotate_half",
        ]

        source_lower = source.lower()
        for op in torch_ops:
            if op in source_lower:
                operations.append(f"torch.{op}")

        # Look for custom/external function calls
        # Match patterns like "func_name(" or "module.func_name("
        func_pattern = r"(\w+)\("
        matches = re.findall(func_pattern, source)
        for match in matches:
            if match not in ["if", "for", "while", "with", "def", "return", "self"]:
                if match not in torch_ops and match.startswith("apply_"):
                    operations.append(match)

        return sorted(set(operations))

    def _suggest_iron_base(self, layer_name: str) -> str:
        """Suggest which IRON base class to extend"""
        layer_lower = layer_name.lower()

        for pattern, base_class in self.IRON_BASE_CLASS_MAP.items():
            if pattern in layer_lower:
                return base_class

        return "AIEOperator (custom base)"

    def _generate_iron_notes(self, spec: OperatorSpec) -> str:
        """Generate IRON integration notes"""
        notes = []

        layer_lower = spec.layer_name.lower()

        # Check for sliding window
        for hp in spec.hyperparameters:
            if "sliding" in hp.name.lower() and hp.value is not None:
                notes.append(
                    f"Sliding window size ({hp.value}) requires custom attention mask. "
                    "Extend attention mechanism to limit receptive field."
                )

        # Check for MoE
        if "moe" in layer_lower or "expert" in layer_lower:
            notes.append(
                "MoE layer requires custom routing logic. "
                "Consider implementing sparse top-k selection on NPU or CPU fallback."
            )

        # Check for GQA/MQA
        for hp in spec.hyperparameters:
            if hp.name == "num_key_value_heads":
                if hp.value == 1:
                    notes.append(
                        "Multi-Query Attention (MQA) - single KV head, optimize memory access."
                    )
                else:
                    notes.append(
                        f"Grouped Query Attention (GQA) with {hp.value} KV heads."
                    )

        # Check for RoPE
        has_rope = any("rope" in op.lower() for op in spec.operations)
        if has_rope:
            notes.append("Uses RoPE - integrate with AIE RoPE operator.")

        return (
            "\n".join(notes)
            if notes
            else "Standard implementation should work with existing IRON operators."
        )

    def _check_special_handling(
        self,
        info,
        layer_name: str,
    ) -> List[str]:
        """Check for special handling requirements"""
        special = []

        layer_lower = layer_name.lower()

        # Check for sliding window
        if info.has_sliding_window and "attention" in layer_lower:
            special.append(
                "CRITICAL: Sliding window attention requires custom implementation"
            )

        # Check for MoE
        if info.has_moe and ("moe" in layer_lower or "expert" in layer_lower):
            special.append("CRITICAL: MoE routing not supported, needs custom operator")

        # Check for QK norm
        if info.has_qk_norm and "attention" in layer_lower:
            special.append(
                "QK normalization required - ensure RMSNorm is applied to Q/K before attention"
            )

        return special


def generate_operator_spec(
    model_name: str,
    layer_name: str,
    trust_remote_code: bool = False,
) -> OperatorSpec:
    """
    Convenience function to generate operator specification.

    Args:
        model_name: HuggingFace model name
        layer_name: Name of the layer class
        trust_remote_code: Whether to trust remote code

    Returns:
        OperatorSpec
    """
    generator = OperatorSpecGenerator()
    return generator.generate(model_name, layer_name, trust_remote_code)


def save_operator_spec(spec: OperatorSpec, output_path: str) -> None:
    """
    Save operator specification to file.

    Args:
        spec: OperatorSpec to save
        output_path: Path to output file (markdown)
    """
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w") as f:
        f.write(spec.to_markdown())

    logger.info(f"Operator spec saved to {output}")
