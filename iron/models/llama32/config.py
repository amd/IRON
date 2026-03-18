# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Llama3.2 model configuration.

This module provides the Llama32Config dataclass for managing
Llama3.2 model hyperparameters and configuration.

Example:
    >>> from iron.models.llama32 import Llama32Config
    >>> config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")
    >>> print(f"Hidden size: {config.hidden_size}")
    >>> print(f"Max context: {config.max_position_embeddings}")
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class Llama32Config:
    """Configuration for Llama3.2 models.

    This dataclass holds all hyperparameters needed to initialize
    a Llama3.2 model. It supports loading from HuggingFace Hub,
    JSON serialization, and provides computed properties for
    memory estimation.

    Attributes:
        # Architecture
        vocab_size: Vocabulary size (default: 128256 for Llama3.2)
        hidden_size: Hidden layer dimension (default: 2048 for 1B model)
        intermediate_size: MLP intermediate dimension (default: 8192)
        num_hidden_layers: Number of transformer layers (default: 16)
        num_attention_heads: Number of attention heads (default: 32)
        num_key_value_heads: Number of KV heads for GQA (default: 8)
        head_dim: Dimension per attention head (default: 64)

        # Sequence
        max_position_embeddings: Maximum context length (default: 131072)
        rope_theta: RoPE theta parameter (default: 500000.0)

        # Normalization
        rms_norm_eps: RMSNorm epsilon (default: 1e-5)

        # Model identification
        model_type: Model type identifier (default: "llama")
        architectures: Architecture list (default: ["LlamaForCausalLM"])
        hidden_act: Activation function (default: "silu")

        # Optional features
        tie_word_embeddings: Tie input/output embeddings (default: False)
        rope_scaling: RoPE scaling configuration (default: None)
        attention_bias: Use bias in attention projections (default: False)
        mlp_bias: Use bias in MLP projections (default: False)

        # Metadata
        model_path: Path to model files (set after download)

    Raises:
        ValueError: If configuration parameters are invalid

    Example:
        >>> config = Llama32Config(
        ...     hidden_size=2048,
        ...     num_hidden_layers=16,
        ...     num_attention_heads=32
        ... )
        >>> print(config.model_size)
        1.0B
    """

    # =========================================================================
    # Architecture Parameters
    # =========================================================================

    vocab_size: int = 128256
    hidden_size: int = 2048
    intermediate_size: int = 8192
    num_hidden_layers: int = 16
    num_attention_heads: int = 32
    num_key_value_heads: int = 8  # GQA groups
    head_dim: int = 64

    # =========================================================================
    # Sequence Parameters
    # =========================================================================

    max_position_embeddings: int = 131072  # 128K context
    rope_theta: float = 500000.0

    # =========================================================================
    # Normalization Parameters
    # =========================================================================

    rms_norm_eps: float = 1e-5

    # =========================================================================
    # Model Identification
    # =========================================================================

    model_type: str = "llama"
    architectures: List[str] = field(default_factory=lambda: ["LlamaForCausalLM"])
    hidden_act: str = "silu"

    # =========================================================================
    # Optional Features
    # =========================================================================

    tie_word_embeddings: bool = False
    rope_scaling: Optional[Dict[str, Any]] = None
    attention_bias: bool = False
    mlp_bias: bool = False

    # =========================================================================
    # KV Cache Configuration (for generation)
    # =========================================================================

    block_size: int = 32  # Tokens per KV block

    # =========================================================================
    # Metadata (set after loading)
    # =========================================================================

    model_path: Optional[Path] = None

    # =========================================================================
    # Initialization
    # =========================================================================

    def __post_init__(self) -> None:
        """Validate configuration after initialization.

        This method is automatically called by dataclasses after
        object construction.

        Raises:
            ValueError: If any configuration parameter is invalid
        """
        self._validate()

    def _validate(self) -> None:
        """Validate configuration parameters.

        Checks all required parameters are within valid ranges and
        that GQA compatibility is maintained.

        Raises:
            ValueError: If validation fails

        Example:
            >>> config = Llama32Config()
            >>> config._validate()  # No exception = valid
        """
        # Basic parameter validation
        if self.vocab_size < 1:
            raise ValueError(f"vocab_size must be >= 1, got {self.vocab_size}")
        if self.hidden_size < 1:
            raise ValueError(f"hidden_size must be >= 1, got {self.hidden_size}")
        if self.num_hidden_layers < 1:
            raise ValueError(f"num_hidden_layers must be >= 1, got {self.num_hidden_layers}")
        if self.num_attention_heads < 1:
            raise ValueError(f"num_attention_heads must be >= 1, got {self.num_attention_heads}")
        if self.head_dim < 1:
            raise ValueError(f"head_dim must be >= 1, got {self.head_dim}")
        if self.rms_norm_eps <= 0:
            raise ValueError(f"rms_norm_eps must be > 0, got {self.rms_norm_eps}")
        if self.intermediate_size < 1:
            raise ValueError(f"intermediate_size must be >= 1, got {self.intermediate_size}")
        if self.max_position_embeddings < 1:
            raise ValueError(
                f"max_position_embeddings must be >= 1, got {self.max_position_embeddings}"
            )
        if self.rope_theta <= 0:
            raise ValueError(f"rope_theta must be > 0, got {self.rope_theta}")

        # GQA compatibility: num_attention_heads must be divisible by num_key_value_heads
        if self.num_attention_heads % self.num_key_value_heads != 0:
            raise ValueError(
                f"num_attention_heads ({self.num_attention_heads}) must be "
                f"divisible by num_key_value_heads ({self.num_key_value_heads}) "
                f"for Grouped Query Attention"
            )

        # Validate attention head dimension
        expected_head_dim = self.hidden_size // self.num_attention_heads
        if self.head_dim != expected_head_dim:
            logger.warning(
                f"head_dim ({self.head_dim}) differs from expected "
                f"({expected_head_dim} = hidden_size // num_attention_heads)"
            )

    # =========================================================================
    # Class Methods - Loading
    # =========================================================================

    @classmethod
    def from_pretrained(
        cls,
        model_id: str = "meta-llama/Llama-3.2-1B",
        cache_dir: Optional[str] = None,
        force_download: bool = False,
        local_files_only: bool = False
    ) -> "Llama32Config":
        """Load configuration from HuggingFace Hub.

        Downloads the config.json file from the specified model repository
        and loads it into a Llama32Config instance.

        Args:
            model_id: HuggingFace model ID (e.g., "meta-llama/Llama-3.2-1B")
            cache_dir: Cache directory for downloaded files. If None, uses
                the default HuggingFace cache directory
            force_download: Force re-download even if already cached
            local_files_only: Only use locally cached files, don't download

        Returns:
            Llama32Config instance loaded from the model's config.json

        Raises:
            ValueError: If the configuration is invalid
            FileNotFoundError: If config.json is not found (local_files_only)
            ConnectionError: If download fails due to network issues

        Example:
            >>> config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")
            >>> print(config.hidden_size)
            2048
            >>> print(config.num_hidden_layers)
            16
        """
        try:
            from huggingface_hub import hf_hub_download
        except ImportError as e:
            raise ImportError(
                "huggingface_hub is required for from_pretrained(). "
                "Install it with: pip install huggingface_hub"
            ) from e

        logger.info(f"Downloading config.json from {model_id}...")

        try:
            config_path = hf_hub_download(
                repo_id=model_id,
                filename="config.json",
                cache_dir=cache_dir,
                force_download=force_download,
                local_files_only=local_files_only
            )
        except Exception as e:
            logger.error(f"Failed to download config from {model_id}: {e}")
            raise

        config = cls.from_json(config_path)
        config.model_path = Path(config_path).parent
        logger.info(f"Loaded config from {config_path}")

        return config

    @classmethod
    def from_json(cls, json_path: str) -> "Llama32Config":
        """Load configuration from JSON file.

        Reads a config.json file (typically from a HuggingFace model
        repository) and creates a Llama32Config instance.

        Args:
            json_path: Path to config.json file

        Returns:
            Llama32Config instance

        Raises:
            FileNotFoundError: If the JSON file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
            ValueError: If the configuration is invalid

        Example:
            >>> config = Llama32Config.from_json("path/to/config.json")
        """
        json_path = Path(json_path)
        if not json_path.exists():
            raise FileNotFoundError(f"Config file not found: {json_path}")

        logger.debug(f"Loading config from {json_path}")

        with open(json_path, "r", encoding="utf-8") as f:
            config_dict = json.load(f)

        return cls(**config_dict)

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "Llama32Config":
        """Load configuration from dictionary.

        Creates a Llama32Config instance from a dictionary of
        configuration parameters.

        Args:
            config_dict: Dictionary of configuration parameters

        Returns:
            Llama32Config instance

        Example:
            >>> config = Llama32Config.from_dict({
            ...     "hidden_size": 2048,
            ...     "num_attention_heads": 32
            ... })
        """
        # Filter out unknown keys that might be in the dict
        known_keys = {
            "vocab_size", "hidden_size", "intermediate_size",
            "num_hidden_layers", "num_attention_heads", "num_key_value_heads",
            "head_dim", "max_position_embeddings", "rope_theta",
            "rms_norm_eps", "model_type", "architectures", "hidden_act",
            "tie_word_embeddings", "rope_scaling", "attention_bias", "mlp_bias"
        }

        filtered_dict = {
            k: v for k, v in config_dict.items()
            if k in known_keys or k == "model_path"
        }

        # Handle model_path specially
        if "model_path" in config_dict:
            filtered_dict["model_path"] = Path(config_dict["model_path"])

        return cls(**filtered_dict)

    # =========================================================================
    # Serialization
    # =========================================================================

    def to_json(self, json_path: str) -> None:
        """Save configuration to JSON file.

        Writes the configuration to a JSON file in a format compatible
        with HuggingFace's config.json format.

        Args:
            json_path: Path to output JSON file

        Example:
            >>> config = Llama32Config()
            >>> config.to_json("output/config.json")
        """
        config_dict = self.to_dict()

        json_path = Path(json_path)
        json_path.parent.mkdir(parents=True, exist_ok=True)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(config_dict, f, indent=2)

        logger.debug(f"Saved config to {json_path}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary.

        Returns:
            Dictionary of configuration parameters

        Example:
            >>> config = Llama32Config()
            >>> config_dict = config.to_dict()
            >>> print(config_dict["hidden_size"])
            2048
        """
        return {
            "vocab_size": self.vocab_size,
            "hidden_size": self.hidden_size,
            "intermediate_size": self.intermediate_size,
            "num_hidden_layers": self.num_hidden_layers,
            "num_attention_heads": self.num_attention_heads,
            "num_key_value_heads": self.num_key_value_heads,
            "head_dim": self.head_dim,
            "max_position_embeddings": self.max_position_embeddings,
            "rope_theta": self.rope_theta,
            "rms_norm_eps": self.rms_norm_eps,
            "model_type": self.model_type,
            "architectures": self.architectures,
            "hidden_act": self.hidden_act,
            "tie_word_embeddings": self.tie_word_embeddings,
            "rope_scaling": self.rope_scaling,
            "attention_bias": self.attention_bias,
            "mlp_bias": self.mlp_bias,
        }

    def to_json_string(self) -> str:
        """Convert configuration to JSON string.

        Returns:
            JSON string representation of the configuration

        Example:
            >>> config = Llama32Config()
            >>> json_str = config.to_json_string()
        """
        return json.dumps(self.to_dict(), indent=2)

    # =========================================================================
    # Computed Properties
    # =========================================================================

    @property
    def model_size(self) -> str:
        """Get approximate model size identifier.

        Calculates the approximate parameter count and returns
        a human-readable size string.

        Returns:
            Model size string (e.g., "1B", "3B", "500M")

        Example:
            >>> config = Llama32Config(
            ...     hidden_size=2048,
            ...     num_hidden_layers=16,
            ...     intermediate_size=8192
            ... )
            >>> print(config.model_size)
            1B
        """
        # Approximate parameter count (embedding + transformer layers + output)
        # Embedding: vocab_size * hidden_size
        # Per layer: 3 * hidden_size * hidden_size (QKV) + hidden_size * hidden_size (O)
        #          + 2 * hidden_size * intermediate_size (MLP)
        # Note: This is approximate; actual count may vary

        params_per_layer = (
            4 * self.hidden_size * self.hidden_size +  # Attention (QKV + O)
            2 * self.hidden_size * self.intermediate_size  # MLP (gate/up + down)
        )

        total_params = (
            self.vocab_size * self.hidden_size +  # Embeddings
            self.num_hidden_layers * params_per_layer +  # Transformer layers
            self.hidden_size * self.vocab_size  # Output projection (if not tied)
        )

        if total_params >= 1e9:
            return f"{total_params / 1e9:.1f}B"
        elif total_params >= 1e6:
            return f"{total_params / 1e6:.0f}M"
        else:
            return f"{total_params:.0f}K"

    @property
    def num_attention_layers(self) -> int:
        """Get number of attention/transformer layers.

        Returns:
            Number of hidden layers

        Example:
            >>> config = Llama32Config(num_hidden_layers=16)
            >>> print(config.num_attention_layers)
            16
        """
        return self.num_hidden_layers

    @property
    def kv_cache_size_per_token(self) -> int:
        """Calculate KV cache size per token in bytes.

        Computes the memory required for storing KV cache for a single
        token across all layers.

        Returns:
            Bytes per token for KV cache (assuming float32)

        Example:
            >>> config = Llama32Config()
            >>> print(config.kv_cache_size_per_token)
            131072  # bytes per token
        """
        # 2 (key + value) * num_layers * num_kv_heads * head_dim * sizeof(float32)
        return (
            2 * self.num_hidden_layers *
            self.num_key_value_heads *
            self.head_dim *
            4  # float32 = 4 bytes
        )

    @property
    def kv_cache_size_per_token_bf16(self) -> int:
        """Calculate KV cache size per token in bytes (bfloat16).

        Computes the memory required for storing KV cache for a single
        token across all layers using bfloat16 precision.

        Returns:
            Bytes per token for KV cache (assuming bfloat16)

        Example:
            >>> config = Llama32Config()
            >>> print(config.kv_cache_size_per_token_bf16)
            65536  # bytes per token
        """
        # 2 (key + value) * num_layers * num_kv_heads * head_dim * sizeof(bfloat16)
        return (
            2 * self.num_hidden_layers *
            self.num_key_value_heads *
            self.head_dim *
            2  # bfloat16 = 2 bytes
        )

    @property
    def gqa_groups(self) -> int:
        """Get number of GQA (Grouped Query Attention) groups.

        Returns:
            Number of attention head groups per KV head

        Example:
            >>> config = Llama32Config(
            ...     num_attention_heads=32,
            ...     num_key_value_heads=8
            ... )
            >>> print(config.gqa_groups)
            4
        """
        return self.num_attention_heads // self.num_key_value_heads

    @property
    def hidden_per_layer_bytes(self) -> int:
        """Calculate bytes needed for one hidden state.

        Returns:
            Bytes for one hidden state (float32)

        Example:
            >>> config = Llama32Config(hidden_size=2048)
            >>> print(config.hidden_per_layer_bytes)
            8192  # bytes
        """
        return self.hidden_size * 4  # float32

    # =========================================================================
    # Memory Estimation
    # =========================================================================

    def estimate_weight_memory(self, dtype: str = "float32") -> int:
        """Estimate memory required for model weights.

        Args:
            dtype: Data type string ("float32", "float16", "bfloat16")

        Returns:
            Estimated weight memory in bytes

        Example:
            >>> config = Llama32Config()
            >>> print(config.estimate_weight_memory("bfloat16"))
            ~2GB for 1B model
        """
        bytes_per_param = {"float32": 4, "float16": 2, "bfloat16": 2}.get(dtype, 4)

        # Approximate parameter count
        params_per_layer = (
            4 * self.hidden_size * self.hidden_size +  # Attention
            2 * self.hidden_size * self.intermediate_size  # MLP
        )

        total_params = (
            self.vocab_size * self.hidden_size +  # Embeddings
            self.num_hidden_layers * params_per_layer +  # Layers
            self.hidden_size * self.vocab_size  # Output
        )

        return total_params * bytes_per_param

    def estimate_kv_cache_memory(
        self,
        batch_size: int,
        seq_len: int,
        dtype: str = "float32"
    ) -> int:
        """Estimate memory required for KV cache.

        Args:
            batch_size: Number of sequences
            seq_len: Sequence length
            dtype: Data type string

        Returns:
            Estimated KV cache memory in bytes

        Example:
            >>> config = Llama32Config()
            >>> print(config.estimate_kv_cache_memory(1, 4096, "bfloat16"))
        """
        bytes_per_param = {"float32": 4, "float16": 2, "bfloat16": 2}.get(dtype, 4)

        return (
            2 *  # key + value
            self.num_hidden_layers *
            self.num_key_value_heads *
            self.head_dim *
            batch_size *
            seq_len *
            bytes_per_param
        )

    # =========================================================================
    # Utility Methods
    # =========================================================================

    def __str__(self) -> str:
        """Get human-readable string representation.

        Returns:
            Formatted string with key configuration parameters

        Example:
            >>> config = Llama32Config()
            >>> print(config)
            Llama32Config(vocab_size=128256, hidden_size=2048, layers=16, ...)
        """
        return (
            f"Llama32Config("
            f"vocab_size={self.vocab_size}, "
            f"hidden_size={self.hidden_size}, "
            f"num_layers={self.num_hidden_layers}, "
            f"num_heads={self.num_attention_heads}, "
            f"kv_heads={self.num_key_value_heads}, "
            f"max_seq_len={self.max_position_embeddings})"
        )

    def __repr__(self) -> str:
        """Get detailed string representation."""
        return self.__str__()
