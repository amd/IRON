# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Auto-Converter for IRON API

Automatically downloads HuggingFace models and converts them to IRON format,
with caching for fast subsequent loads.
"""

from pathlib import Path
from typing import Optional, Tuple
import logging
import shutil

from .model_registry import ModelRegistry, ModelEntry
from ..model_convert import HuggingFaceConverter, ModelAssembler

logger = logging.getLogger(__name__)


class AutoConverter:
    """
    Automatically downloads and converts HuggingFace models to IRON format.

    The auto-converter handles:
    1. Checking cache for pre-converted models
    2. Downloading models from HuggingFace Hub
    3. Converting weights to IRON format
    4. Caching converted models for subsequent loads
    5. Loading converted models into memory

    Usage:
        registry = ModelRegistry()
        converter = AutoConverter(registry)

        # Convert and load a model
        entry, assembler = converter.get_or_load("meta-llama/Llama-3.2-1B")

        # Or just convert (returns path to cached model)
        entry, model_path = converter.get_or_convert("meta-llama/Llama-3.2-1B")
    """

    def __init__(
        self,
        registry: Optional[ModelRegistry] = None,
        num_aie_columns: int = 8,
        compile_artifacts: bool = False,
    ):
        """
        Initialize the auto-converter.

        Args:
            registry: Optional model registry (creates default if None)
            num_aie_columns: Number of AIE columns to use
            compile_artifacts: Whether to compile AIE artifacts during conversion
        """
        self.registry = registry or ModelRegistry()
        self.num_aie_columns = num_aie_columns
        self.compile_artifacts = compile_artifacts

        logger.info(f"AutoConverter initialized with {num_aie_columns} AIE columns")

    def get_or_convert(
        self,
        model_id: str,
        trust_remote_code: bool = False,
    ) -> Tuple[ModelEntry, Path]:
        """
        Get converted model path, converting if needed.

        This method:
        1. Checks if model is already converted in cache
        2. If not, downloads from HF Hub and converts
        3. Returns the path to converted model

        Args:
            model_id: HuggingFace model ID (e.g., "meta-llama/Llama-3.2-1B")
            trust_remote_code: Whether to trust remote code for HF loading

        Returns:
            Tuple of (ModelEntry, Path to converted model)

        Raises:
            RuntimeError: If conversion fails
        """
        model_path = self.registry.get_model_path(model_id)
        config_path = model_path / "iron_config.json"

        # Check if already converted
        if config_path.exists():
            logger.info(f"Using cached model: {model_path}")
            entry = self._get_or_create_entry(model_id)
            entry.status = "ready"
            self.registry.update(entry)
            return entry, model_path

        # Start conversion
        logger.info(f"Converting {model_id}...")
        entry = self._get_or_create_entry(model_id)
        entry.status = "converting"
        self.registry.update(entry)

        try:
            # Create converter (downloads config from HF if needed)
            converter = HuggingFaceConverter(
                model_id,
                num_aie_columns=self.num_aie_columns,
                trust_remote_code=trust_remote_code,
            )

            # Convert weights to cache
            logger.info(f"Converting weights to {model_path}...")
            converter.convert_weights(output_dir=str(model_path))

            # Export config
            converter.export_config(str(config_path))

            # Update entry with model info
            entry.architecture = converter.norm_config.architecture.value
            entry.hidden_size = converter.norm_config.hidden_size
            entry.num_layers = converter.norm_config.num_hidden_layers
            entry.vocab_size = converter.norm_config.vocab_size
            entry.status = "ready"
            self.registry.update(entry)

            logger.info(f"Successfully converted {model_id} to {model_path}")

        except Exception as e:
            entry.status = "error"
            entry.error_message = str(e)
            self.registry.update(entry)
            logger.error(f"Conversion failed for {model_id}: {e}")
            raise RuntimeError(f"Failed to convert {model_id}: {e}")

        return entry, model_path

    def get_or_load(
        self,
        model_id: str,
        trust_remote_code: bool = False,
    ) -> Tuple[ModelEntry, ModelAssembler]:
        """
        Get converted model and load it into memory.

        This method:
        1. Converts model if not in cache
        2. Loads converted model into memory
        3. Compiles AIE artifacts if not already compiled

        Args:
            model_id: HuggingFace model ID
            trust_remote_code: Whether to trust remote code for HF loading

        Returns:
            Tuple of (ModelEntry, ModelAssembler ready for inference)

        Raises:
            RuntimeError: If conversion or loading fails
        """
        # Get or convert
        entry, model_path = self.get_or_convert(
            model_id,
            trust_remote_code=trust_remote_code,
        )

        # Load model
        logger.info(f"Loading model from {model_path}...")

        from ..model_convert import create_model

        assembler = create_model(
            config_path=model_path / "iron_config.json",
            weights_path=model_path,
            num_aie_columns=self.num_aie_columns,
        )

        # Compile artifacts if not already compiled
        if self.compile_artifacts:
            logger.info("Compiling AIE artifacts...")
            assembler.compile_artifacts()

        # Update usage
        self.registry.update_usage(model_id)

        logger.info(f"Model {model_id} loaded successfully")

        return entry, assembler

    def _get_or_create_entry(self, model_id: str) -> ModelEntry:
        """Get existing entry or create new one"""
        try:
            return self.registry.get(model_id)
        except KeyError:
            return self.registry.register_model(model_id)

    def clear_cache(self, model_id: Optional[str] = None):
        """
        Clear model cache.

        Args:
            model_id: Optional specific model to clear (clears all if None)
        """
        if model_id:
            model_path = self.registry.get_model_path(model_id)
            if model_path.exists():
                shutil.rmtree(model_path)
                self.registry.remove(model_id)
                logger.info(f"Cleared cache for {model_id}")
        else:
            # Clear all
            for item in self.cache_dir.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
            self.registry.models.clear()
            self.registry._save_registry()
            logger.info("Cleared all model cache")

    def list_cached_models(self) -> list:
        """
        List all cached models.

        Returns:
            List of ModelEntry objects for cached models
        """
        return self.registry.list_models(status_filter="ready")
