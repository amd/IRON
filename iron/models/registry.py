# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Model registry for supported architectures.

This module provides a centralized registry for all supported model
architectures, enabling dynamic model selection and validation.

Example:
    >>> from iron.models import ModelRegistry, ModelSpec
    >>> from iron.models.llama32.config import Llama32Config
    >>> spec = ModelRegistry.get("llama")
    >>> if spec:
    ...     config = spec.config_class.from_pretrained(spec.default_variant)
"""

from typing import Dict, Type, Optional, List
from dataclasses import dataclass


@dataclass
class ModelSpec:
    """Model specification for registry.

    Attributes:
        config_class: Configuration class for the model
        supported_variants: List of supported model variant IDs
        default_variant: Default variant to use if not specified

    Example:
        >>> spec = ModelSpec(
        ...     config_class=Llama32Config,
        ...     supported_variants=["meta-llama/Llama-3.2-1B"],
        ...     default_variant="meta-llama/Llama-3.2-1B"
        ... )
    """

    config_class: Type
    supported_variants: List[str]
    default_variant: str

    def is_variant_supported(self, variant: str) -> bool:
        """Check if a model variant is supported.

        Args:
            variant: Model variant ID to check

        Returns:
            True if variant is supported
        """
        return variant in self.supported_variants


class ModelRegistry:
    """Registry for supported model architectures.

    The registry provides centralized management of all supported models,
    enabling:
    - Dynamic model discovery
    - Variant validation
    - Configuration class lookup

    Thread Safety:
        The registry uses class-level storage and is safe for concurrent
        read access. Write operations (register) should be done during
        initialization only.

    Example:
        >>> ModelRegistry.is_supported("llama")
        True
        >>> ModelRegistry.list_supported()
        ['llama']
        >>> spec = ModelRegistry.get("llama")
    """

    _registry: Dict[str, ModelSpec] = {}

    @classmethod
    def register(cls, model_type: str, spec: ModelSpec) -> None:
        """Register a model architecture.

        Args:
            model_type: Model type identifier (e.g., "llama", "gpt2")
            spec: Model specification with config class and variants

        Raises:
            ValueError: If model_type is already registered

        Example:
            >>> spec = ModelSpec(Llama32Config, ["meta-llama/Llama-3.2-1B"], "meta-llama/Llama-3.2-1B")
            >>> ModelRegistry.register("llama", spec)
        """
        if model_type in cls._registry:
            raise ValueError(f"Model type '{model_type}' is already registered")
        cls._registry[model_type] = spec

    @classmethod
    def get(cls, model_type: str) -> Optional[ModelSpec]:
        """Get model specification.

        Args:
            model_type: Model type identifier

        Returns:
            Model specification or None if not found

        Example:
            >>> spec = ModelRegistry.get("llama")
            >>> if spec:
            ...     print(f"Default variant: {spec.default_variant}")
        """
        return cls._registry.get(model_type)

    @classmethod
    def get_or_raise(cls, model_type: str) -> ModelSpec:
        """Get model specification or raise an error.

        Args:
            model_type: Model type identifier

        Returns:
            Model specification

        Raises:
            KeyError: If model type is not supported

        Example:
            >>> spec = ModelRegistry.get_or_raise("llama")
        """
        spec = cls.get(model_type)
        if spec is None:
            raise KeyError(
                f"Model type '{model_type}' is not supported. "
                f"Supported types: {cls.list_supported()}"
            )
        return spec

    @classmethod
    def is_supported(cls, model_type: str) -> bool:
        """Check if model type is supported.

        Args:
            model_type: Model type identifier

        Returns:
            True if supported

        Example:
            >>> ModelRegistry.is_supported("llama")
            True
            >>> ModelRegistry.is_supported("unknown_model")
            False
        """
        return model_type in cls._registry

    @classmethod
    def list_supported(cls) -> List[str]:
        """List all supported model types.

        Returns:
            List of model type strings

        Example:
            >>> ModelRegistry.list_supported()
            ['llama']
        """
        return list(cls._registry.keys())

    @classmethod
    def get_config_class(cls, model_type: str) -> Optional[Type]:
        """Get configuration class for a model type.

        Args:
            model_type: Model type identifier

        Returns:
            Configuration class or None if not found

        Example:
            >>> config_cls = ModelRegistry.get_config_class("llama")
            >>> if config_cls:
            ...     config = config_cls.from_pretrained("meta-llama/Llama-3.2-1B")
        """
        spec = cls.get(model_type)
        return spec.config_class if spec else None

    @classmethod
    def validate_variant(cls, model_type: str, variant: str) -> bool:
        """Validate that a model variant is supported.

        Args:
            model_type: Model type identifier
            variant: Model variant ID to validate

        Returns:
            True if variant is supported for this model type

        Example:
            >>> ModelRegistry.validate_variant("llama", "meta-llama/Llama-3.2-1B")
            True
        """
        spec = cls.get(model_type)
        if spec is None:
            return False
        return spec.is_variant_supported(variant)

    @classmethod
    def clear(cls) -> None:
        """Clear all registered models.

        Note:
            This is primarily for testing purposes.

        Example:
            >>> ModelRegistry.clear()
            >>> assert len(ModelRegistry.list_supported()) == 0
        """
        cls._registry.clear()


# Register built-in model architectures
def _register_builtin_models() -> None:
    """Register built-in model architectures."""
    # Import here to avoid circular dependency
    from iron.models.llama32.config import Llama32Config

    # Register Llama3.2 architecture
    ModelRegistry.register(
        "llama",
        ModelSpec(
            config_class=Llama32Config,
            supported_variants=[
                "meta-llama/Llama-3.2-1B",
                "meta-llama/Llama-3.2-1B-Instruct",
                "meta-llama/Llama-3.2-3B",
                "meta-llama/Llama-3.2-3B-Instruct",
            ],
            default_variant="meta-llama/Llama-3.2-1B"
        )
    )


# Auto-register built-in models on module import
_register_builtin_models()
