# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
HuggingFace Model Converter

Main entry point for converting HuggingFace models to IRON NPU format.
This module provides a simple, unified API for the entire conversion process.

Example usage:
    from iron.model_convert import HuggingFaceConverter

    # Convert a Llama model
    converter = HuggingFaceConverter("meta-llama/Llama-2-7b-hf")
    converter.convert_to_iron(output_dir="./iron_model")

    # Load and run
    model = converter.load_iron_model()
    output = model.generate(input_ids, max_new_tokens=100)
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, asdict
import logging

import torch

from .config_adapter import (
    ConfigAdapter,
    NormalizedConfig,
    ModelArchitecture,
    load_hf_config,
    get_iron_ready_config,
)
from .weight_mapper import WeightMapper, create_weight_mapper, QuantizedWeightMapper
from .shape_manager import ShapeManager, TilingConfig, create_shape_manager
from .operator_factory import (
    OperatorFactory,
    OperatorType,
    create_operator_factory,
    OperatorBuilder,
)
from .layer_builder import (
    LayerConfig,
    AttentionLayerBuilder,
    FeedForwardBuilder,
    TransformerBlockBuilder,
    create_attention_layer,
    create_ffn_layer,
    create_transformer_block,
)
from .model_assembler import ModelAssembler, ModelAssemblyConfig, create_model
from .gap_analyzer import (
    GapAnalyzer,
    generate_gap_report,
    quick_check as quick_compatibility_check,
)
from .architecture_scanner import ArchitectureScanner

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class ConversionConfig:
    """Configuration for model conversion"""

    # Source model
    model_name_or_path: str

    # NPU configuration
    num_aie_columns: int = 8
    tile_m: int = 64
    tile_k: int = 64
    tile_n: int = 64

    # Operator enable flags
    enable_aie_gemm: bool = True
    enable_aie_gemv: bool = False  # For decode
    enable_aie_norm: bool = True
    enable_aie_mha: bool = False
    enable_aie_rope: bool = False
    enable_aie_ffn: bool = True

    # Execution settings
    use_kv_cache: bool = True
    max_seq_len: int = 512
    batch_size: int = 1

    # Quantization (future)
    quantize: bool = False
    quant_type: Optional[str] = None

    # Output settings
    output_dir: Optional[str] = None
    verbose: bool = False


class HuggingFaceConverter:
    """
    Main converter class for HuggingFace to IRON conversion.

    Provides a simple API for:
    1. Loading HF model configuration
    2. Converting weights to NPU format
    3. Creating NPU operators
    4. Running inference on NPU

    Example:
        converter = HuggingFaceConverter("mistralai/Mistral-7B-v0.1")

        # Convert weights
        converter.convert_weights(output_dir="./weights")

        # Create NPU model
        model = converter.create_npu_model()

        # Run inference
        output = model.generate(input_ids, max_new_tokens=100)
    """

    def __init__(
        self,
        model_name_or_path: str,
        config: Optional[ConversionConfig] = None,
        **kwargs,
    ):
        """
        Initialize the converter.

        Args:
            model_name_or_path: HF model name or local path
            config: Optional conversion configuration
            **kwargs: Additional configuration options
        """
        self.model_name_or_path = model_name_or_path
        self.model_path = Path(model_name_or_path)

        # Build configuration
        if config:
            self.config = config
        else:
            self.config = ConversionConfig(
                model_name_or_path=model_name_or_path,
                **kwargs,
            )

        # Load model configuration
        self._load_config()

        # Initialize components
        self._init_components()

    def _load_config(self):
        """Load and normalize model configuration"""
        config_path = self.model_path / "config.json"

        if config_path.exists():
            self.config_adapter = ConfigAdapter(str(config_path))
            self.norm_config = self.config_adapter.normalize()
            self.iron_config = self.config_adapter.get_iron_config()
        else:
            # Try to load from HF hub
            try:
                from huggingface_hub import hf_hub_download

                config_path = hf_hub_download(self.model_name_or_path, "config.json")
                self.config_adapter = ConfigAdapter(config_path)
                self.norm_config = self.config_adapter.normalize()
                self.iron_config = self.config_adapter.get_iron_config()
            except ImportError:
                raise ImportError(
                    "Please install huggingface_hub: pip install huggingface_hub"
                )
            except Exception as e:
                raise RuntimeError(
                    f"Could not load config for {self.model_name_or_path}: {e}"
                )

        logger.info(f"Loaded config for {self.norm_config.architecture.value} model")
        logger.info(f"  Hidden size: {self.norm_config.hidden_size}")
        logger.info(f"  Layers: {self.norm_config.num_hidden_layers}")
        logger.info(f"  Attention heads: {self.norm_config.num_attention_heads}")
        logger.info(f"  KV heads: {self.norm_config.num_kv_heads}")

    def _init_components(self):
        """Initialize converter components"""
        # Weight mapper
        self.weight_mapper = create_weight_mapper(
            architecture=self.norm_config.architecture.value,
            quantized=self.config.quantize,
            quant_type=self.config.quant_type or "awq",
        )

        # Shape manager
        self.shape_manager = create_shape_manager(
            hidden_size=self.norm_config.hidden_size,
            num_heads=self.norm_config.num_attention_heads,
            num_kv_heads=self.norm_config.num_kv_heads,
            num_aie_columns=self.config.num_aie_columns,
        )

        # Operator factory (created when needed with AIE context)
        self._operator_factory = None

    @property
    def operator_factory(self) -> OperatorFactory:
        """Get or create operator factory"""
        if self._operator_factory is None:
            from iron.common import AIEContext

            self._operator_factory = create_operator_factory(
                context=AIEContext(),
                num_aie_columns=self.config.num_aie_columns,
            )
        return self._operator_factory

    def convert_weights(
        self,
        output_dir: Optional[str] = None,
        output_format: str = "numpy",
    ) -> Dict[str, Any]:
        """
        Convert model weights to NPU format.

        Args:
            output_dir: Optional directory to save converted weights
            output_format: Output format (numpy, torch)

        Returns:
            Dictionary of converted weights
        """
        logger.info("Loading weights from source...")

        # Load source weights
        if (self.model_path / "model.safetensors").exists():
            state_dict = self.weight_mapper.load_safetensors(self.model_path)
        elif (self.model_path / "model.safetensors.index.json").exists():
            state_dict = self.weight_mapper.load_safetensors(self.model_path)
        else:
            state_dict = self.weight_mapper.load_pytorch(self.model_path)

        logger.info(f"Loaded {len(state_dict)} weight tensors")

        # Map weights to IRON format
        logger.info("Mapping weights to IRON format...")
        converted_weights = self.weight_mapper.map_weights(state_dict)

        # Save if output directory specified
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            if output_format == "numpy":
                import numpy as np

                for name, weight in converted_weights.items():
                    safe_name = name.replace(".", "_").replace("/", "_")
                    np.save(output_path / f"{safe_name}.npy", weight)
            elif output_format == "torch":
                torch.save(converted_weights, output_path / "iron_weights.pt")

            logger.info(f"Saved converted weights to {output_dir}")

        return converted_weights

    def create_npu_model(
        self,
        compile_artifacts: bool = False,
        **kwargs,
    ) -> ModelAssembler:
        """
        Create NPU model for inference.

        Args:
            compile_artifacts: Whether to compile AIE artifacts
            **kwargs: Additional model configuration

        Returns:
            ModelAssembler instance
        """
        logger.info("Creating NPU model...")

        # Create assembly config
        assembly_config = ModelAssemblyConfig(
            normalized_config=self.norm_config,
            num_aie_columns=self.config.num_aie_columns,
            use_aie_gemm=self.config.enable_aie_gemm,
            use_aie_gemv=self.config.enable_aie_gemv,
            use_aie_norm=self.config.enable_aie_norm,
            use_aie_attention=self.config.enable_aie_mha,
            use_aie_rope=self.config.enable_aie_rope,
            use_aie_ffn=self.config.enable_aie_ffn,
            use_kv_cache=self.config.use_kv_cache,
            max_seq_len=self.config.max_seq_len,
            batch_size=self.config.batch_size,
            compile_artifacts=compile_artifacts,
        )

        # Create and assemble model
        assembler = ModelAssembler(assembly_config)
        assembler.assemble()

        logger.info("NPU model created successfully")

        # Print memory requirements
        mem_info = assembler.get_memory_info()
        logger.info(f"Estimated memory requirements:")
        logger.info(f"  KV Cache: {mem_info['kv_cache_bytes'] / 1024 / 1024:.1f} MB")
        logger.info(
            f"  Prefill activations: {mem_info['prefill_activation_bytes'] / 1024 / 1024:.1f} MB"
        )

        return assembler

    def convert_and_load(
        self,
        weights_path: Optional[str] = None,
        compile_artifacts: bool = False,
    ) -> ModelAssembler:
        """
        Convert weights and create NPU model in one step.

        Args:
            weights_path: Optional path to save/load converted weights
            compile_artifacts: Whether to compile AIE artifacts

        Returns:
            ModelAssembler instance ready for inference
        """
        # Convert weights
        if weights_path:
            weights_dir = Path(weights_path)
            if weights_dir.exists():
                # Load existing converted weights
                logger.info(f"Loading pre-converted weights from {weights_path}")
                # For now, just convert again - future: load cached weights
                self.convert_weights(output_dir=weights_path)
            else:
                self.convert_weights(output_dir=weights_path)
        else:
            self.convert_weights()

        # Create model
        assembler = self.create_npu_model(compile_artifacts=compile_artifacts)

        return assembler

    def get_model_info(self) -> Dict[str, Any]:
        """Get model information"""
        return {
            "architecture": self.norm_config.architecture.value,
            "hidden_size": self.norm_config.hidden_size,
            "num_layers": self.norm_config.num_hidden_layers,
            "num_heads": self.norm_config.num_attention_heads,
            "num_kv_heads": self.norm_config.num_kv_heads,
            "vocab_size": self.norm_config.vocab_size,
            "intermediate_size": self.norm_config.intermediate_size,
            "norm_type": self.norm_config.norm_type.value,
            "ffn_type": self.norm_config.ffn_type.value,
            "rope_theta": self.norm_config.rope_theta,
            "max_position_embeddings": self.norm_config.max_position_embeddings,
            "npu_config": {
                "num_aie_columns": self.config.num_aie_columns,
                "tile_sizes": {
                    "m": self.config.tile_m,
                    "k": self.config.tile_k,
                    "n": self.config.tile_n,
                },
            },
        }

    def export_config(self, output_path: str) -> None:
        """
        Export IRON-ready configuration to JSON.

        Args:
            output_path: Path to save configuration
        """
        config = self.get_iron_config()

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w") as f:
            json.dump(config, f, indent=2, default=str)

        logger.info(f"Exported IRON config to {output_path}")

    def get_iron_config(self) -> Dict[str, Any]:
        """Get IRON-ready configuration dictionary"""
        return {
            **self.iron_config,
            "num_aie_columns": self.config.num_aie_columns,
            "tile_m": self.config.tile_m,
            "tile_k": self.config.tile_k,
            "tile_n": self.config.tile_n,
            "use_aie_gemm": self.config.enable_aie_gemm,
            "use_aie_gemv": self.config.enable_aie_gemv,
            "use_aie_norm": self.config.enable_aie_norm,
            "use_aie_mha": self.config.enable_aie_mha,
            "use_aie_rope": self.config.enable_aie_rope,
            "use_aie_ffn": self.config.enable_aie_ffn,
            "use_kv_cache": self.config.use_kv_cache,
            "max_seq_len": self.config.max_seq_len,
        }

    def check_compatibility(self) -> Dict[str, Any]:
        """
        Check model compatibility with IRON capabilities.

        Returns:
            Dictionary with compatibility information:
            - is_supported: bool
            - support_percentage: float
            - feasibility: str
            - gaps: list of unsupported components
        """
        try:
            # Scan model architecture
            scanner = ArchitectureScanner(self.model_name_or_path)
            requirements = scanner.scan()

            # Analyze gaps
            analyzer = GapAnalyzer()
            report = analyzer.analyze(requirements)

            return {
                "is_supported": report.conversion_feasibility != "not_feasible",
                "support_percentage": report.support_percentage,
                "feasibility": report.conversion_feasibility,
                "total_components": report.total_components,
                "supported_components": report.supported_components,
                "unsupported_components": report.unsupported_components,
                "critical_gaps": [
                    {
                        "name": gap.component_name,
                        "module_path": gap.module_path,
                        "reason": gap.reason,
                        "impact": gap.impact,
                    }
                    for gap in report.critical_gaps
                ],
                "recommendation": report.recommended_approach,
            }

        except Exception as e:
            logger.warning(f"Could not check compatibility: {e}")
            return {
                "is_supported": None,
                "support_percentage": 0,
                "feasibility": "unknown",
                "error": str(e),
            }

    def quick_check(self) -> bool:
        """
        Quick check if model is likely supported.

        Returns:
            True if model is likely supported, False otherwise
        """
        return quick_compatibility_check(self.model_name_or_path)


def convert_model(
    model_name_or_path: str,
    output_dir: Optional[str] = None,
    num_aie_columns: int = 8,
    compile_artifacts: bool = False,
    **kwargs,
) -> ModelAssembler:
    """
    Convenience function to convert a model and return the NPU assembler.

    Args:
        model_name_or_path: HF model name or path
        output_dir: Optional directory for converted weights
        num_aie_columns: Number of AIE columns
        compile_artifacts: Whether to compile artifacts
        **kwargs: Additional configuration

    Returns:
        ModelAssembler instance
    """
    converter = HuggingFaceConverter(
        model_name_or_path,
        num_aie_columns=num_aie_columns,
        **kwargs,
    )

    if output_dir:
        converter.convert_weights(output_dir=output_dir)

    return converter.create_npu_model(compile_artifacts=compile_artifacts)


def load_iron_model(
    config_path: Union[str, Path, Dict],
    weights_path: Optional[Union[str, Path]] = None,
    **kwargs,
) -> ModelAssembler:
    """
    Load an IRON model from configuration and optional weights.

    Args:
        config_path: Path to IRON config or HF config.json
        weights_path: Optional path to model weights
        **kwargs: Additional model configuration

    Returns:
        ModelAssembler instance
    """
    return create_model(
        config_path=config_path,
        weights_path=weights_path,
        **kwargs,
    )


__all__ = [
    # Main classes
    "HuggingFaceConverter",
    "ConversionConfig",
    "ModelAssembler",
    "ModelAssemblyConfig",
    # Config adapter
    "ConfigAdapter",
    "NormalizedConfig",
    "ModelArchitecture",
    "load_hf_config",
    "get_iron_ready_config",
    # Weight mapper
    "WeightMapper",
    "QuantizedWeightMapper",
    "create_weight_mapper",
    # Shape manager
    "ShapeManager",
    "TilingConfig",
    "create_shape_manager",
    # Operator factory
    "OperatorFactory",
    "OperatorType",
    "create_operator_factory",
    "OperatorBuilder",
    # Layer builder
    "LayerConfig",
    "AttentionLayerBuilder",
    "FeedForwardBuilder",
    "TransformerBlockBuilder",
    "create_attention_layer",
    "create_ffn_layer",
    "create_transformer_block",
    # Convenience functions
    "convert_model",
    "load_iron_model",
    "create_model",
]
