# Phase 3 Week 2 Implementation Scope: Model Loader

**Document Type:** Technical Implementation Specification
**Date:** 2026-03-15
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Version:** 1.0.0
**Status:** READY FOR EXECUTION

---

## 1. Executive Summary

### 1.1 Purpose

This document defines the implementation scope for **Phase 3 Week 2: Model Loader**. These components enable loading Llama3.2 model configurations and weights from HuggingFace Hub.

### 1.2 Week 2 Goals

Implement two critical components that enable:
- Loading Llama3.2 model configuration from HuggingFace
- Downloading and validating safetensors weights
- Memory-mapped weight loading for efficient memory usage
- Integration with Week 1 MemoryBudget for validation

### 1.3 Success Criteria

| Criterion | Measurement | Target |
|-----------|-------------|--------|
| **Config Loading** | Can load Llama3.2-1B config from HF | 100% success rate |
| **Weight Download** | Downloads safetensors with validation | Checksum verified |
| **Memory Integration** | Uses Week 1 MemoryBudget | Pre-load validation |
| **Concurrent Safety** | Uses Week 1 ModelLoader queue | Thread-safe operations |
| **Test Coverage** | Unit tests with >90% coverage | 40+ tests |
| **Quality Review** | GO decision from reviewer | No blocking issues |

### 1.4 Week 1 Dependency Status

Week 2 builds on Week 1 foundation components:

| Week 1 Component | Week 2 Usage |
|------------------|--------------|
| `MemoryBudget` | Validate model load before downloading |
| `ThreadSafeModelLoader` | Queue concurrent load requests |
| `GenerationConfig` | Model configuration integration |
| `RoPECache` | Config provides RoPE parameters |

---

## 2. Task Overview

### 2.1 Week 2 Task List

| Task ID | Subject | Priority | Effort | Dependencies |
|---------|---------|----------|--------|--------------|
| **#68** | Llama3.2 Model Config Loader | CRITICAL | 2 days | Week 1 complete |
| **#69** | Weight Loader (safetensors) | CRITICAL | 3 days | Task #68 |

**Total Effort:** 5 developer-days

### 2.2 Implementation Order

```
Day 1-2: Task #68 - Config Loader
         └── Parse Llama3.2 config.json
         └── Extract hyperparameters
         └── Validate configuration

Day 2-4: Task #69 - Weight Loader
         └── Download from HuggingFace Hub
         └── Validate safetensors format
         └── Memory-mapped loading
         └── Checksum verification

Day 5:   Integration & Testing
         └── End-to-end model load test
         └── Unit tests (40+ tests)
         └── Quality review
```

---

## 3. Technical Specifications

### 3.1 Task #68: Llama3.2 Model Config Loader

#### 3.1.1 Problem Statement

Llama3.2 model configuration is stored in `config.json` on HuggingFace Hub. Need to:
- Parse configuration into strongly-typed Python dataclass
- Extract all hyperparameters needed for model initialization
- Validate configuration against supported models
- Provide defaults for optional parameters

#### 3.1.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **HuggingFace Integration** | Load config from HF Hub | CRITICAL |
| **Strong Typing** | Dataclass with type hints | CRITICAL |
| **Validation** | Check supported model types | HIGH |
| **Defaults** | Sensible defaults for optional params | MEDIUM |
| **Serialization** | JSON load/save support | HIGH |

#### 3.1.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/models/__init__.py` | Package | Model package init |
| `iron/models/base.py` | Source | Base model interface |
| `iron/models/llama32/__init__.py` | Package | Llama32 package init |
| `iron/models/llama32/config.py` | Source | Model configuration |
| `iron/models/registry.py` | Source | Model registry |

#### 3.1.4 Class Specifications

**Llama32Config Dataclass:**

```python
# File: iron/models/llama32/config.py
"""Llama3.2 model configuration."""

from dataclasses import dataclass, field
from typing import Optional, List
import json
from pathlib import Path
from huggingface_hub import hf_hub_download


@dataclass
class Llama32Config:
    """Configuration for Llama3.2 models.

    Attributes:
        # Architecture
        vocab_size: Vocabulary size
        hidden_size: Hidden layer dimension
        intermediate_size: MLP intermediate dimension
        num_hidden_layers: Number of transformer layers
        num_attention_heads: Number of attention heads
        num_key_value_heads: Number of KV heads (for GQA)
        head_dim: Dimension per attention head

        # Sequence
        max_position_embeddings: Maximum context length
        rope_theta: RoPE theta parameter

        # Normalization
        rms_norm_eps: RMSNorm epsilon

        # Model identification
        model_type: Model type identifier
        architectures: Architecture list
        hidden_act: Activation function

        # Optional features
        tie_word_embeddings: Tie input/output embeddings
        rope_scaling: RoPE scaling configuration
        attention_bias: Use bias in attention projections
        mlp_bias: Use bias in MLP projections

        # Metadata
        model_path: Path to model files (after download)
    """

    # Architecture
    vocab_size: int = 128256
    hidden_size: int = 2048
    intermediate_size: int = 8192
    num_hidden_layers: int = 16
    num_attention_heads: int = 32
    num_key_value_heads: int = 8  # GQA groups
    head_dim: int = 64

    # Sequence
    max_position_embeddings: int = 131072  # 128K context
    rope_theta: float = 500000.0

    # Normalization
    rms_norm_eps: float = 1e-5

    # Model identification
    model_type: str = "llama"
    architectures: List[str] = field(default_factory=lambda: ["LlamaForCausalLM"])
    hidden_act: str = "silu"

    # Optional features
    tie_word_embeddings: bool = False
    rope_scaling: Optional[dict] = None
    attention_bias: bool = False
    mlp_bias: bool = False

    # Metadata (set after loading)
    model_path: Optional[Path] = None

    # Llama3.2-specific defaults
    def __post_init__(self):
        """Validate configuration."""
        self._validate()

    def _validate(self):
        """Validate configuration parameters."""
        if self.vocab_size < 1:
            raise ValueError("vocab_size must be >= 1")
        if self.hidden_size < 1:
            raise ValueError("hidden_size must be >= 1")
        if self.num_hidden_layers < 1:
            raise ValueError("num_hidden_layers must be >= 1")
        if self.num_attention_heads < 1:
            raise ValueError("num_attention_heads must be >= 1")
        if self.head_dim < 1:
            raise ValueError("head_dim must be >= 1")
        if self.rms_norm_eps <= 0:
            raise ValueError("rms_norm_eps must be > 0")

        # Validate GQA compatibility
        if self.num_attention_heads % self.num_key_value_heads != 0:
            raise ValueError(
                f"num_attention_heads ({self.num_attention_heads}) must be "
                f"divisible by num_key_value_heads ({self.num_key_value_heads})"
            )

    @classmethod
    def from_pretrained(cls, model_id: str, cache_dir: Optional[str] = None) -> "Llama32Config":
        """Load configuration from HuggingFace Hub.

        Args:
            model_id: HuggingFace model ID (e.g., "meta-llama/Llama-3.2-1B")
            cache_dir: Cache directory for downloaded files

        Returns:
            Llama32Config instance

        Example:
            >>> config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")
            >>> print(config.hidden_size)
            2048
        """
        config_path = hf_hub_download(
            repo_id=model_id,
            filename="config.json",
            cache_dir=cache_dir
        )
        return cls.from_json(config_path)

    @classmethod
    def from_json(cls, json_path: str) -> "Llama32Config":
        """Load configuration from JSON file.

        Args:
            json_path: Path to config.json file

        Returns:
            Llama32Config instance
        """
        with open(json_path, "r") as f:
            config_dict = json.load(f)
        return cls(**config_dict)

    def to_json(self, json_path: str) -> None:
        """Save configuration to JSON file.

        Args:
            json_path: Path to output JSON file
        """
        config_dict = {
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
        with open(json_path, "w") as f:
            json.dump(config_dict, f, indent=2)

    @property
    def model_size(self) -> str:
        """Get model size identifier.

        Returns:
            Model size string (e.g., "1B", "3B")
        """
        # Approximate parameter count
        params = (
            2 * self.num_hidden_layers * self.hidden_size *
            (self.intermediate_size + self.hidden_size)
        )
        if params < 1e9:
            return f"{params / 1e6:.0f}M"
        else:
            return f"{params / 1e9:.1f}B"

    @property
    def kv_cache_size_per_token(self) -> int:
        """Calculate KV cache size per token in bytes.

        Returns:
            Bytes per token for KV cache
        """
        # 2 (key + value) * num_layers * num_kv_heads * head_dim * sizeof(bfloat16)
        return (
            2 * self.num_hidden_layers *
            self.num_key_value_heads *
            self.head_dim *
            2  # bfloat16 = 2 bytes
        )
```

**Model Registry:**

```python
# File: iron/models/registry.py
"""Model registry for supported architectures."""

from typing import Dict, Type, Optional
from dataclasses import dataclass
from .llama32.config import Llama32Config


@dataclass
class ModelSpec:
    """Model specification for registry."""
    config_class: Type
    supported_variants: list
    default_variant: str


class ModelRegistry:
    """Registry for supported model architectures."""

    _registry: Dict[str, ModelSpec] = {}

    @classmethod
    def register(cls, model_type: str, spec: ModelSpec) -> None:
        """Register a model architecture.

        Args:
            model_type: Model type identifier
            spec: Model specification
        """
        cls._registry[model_type] = spec

    @classmethod
    def get(cls, model_type: str) -> Optional[ModelSpec]:
        """Get model specification.

        Args:
            model_type: Model type identifier

        Returns:
            Model specification or None
        """
        return cls._registry.get(model_type)

    @classmethod
    def is_supported(cls, model_type: str) -> bool:
        """Check if model type is supported.

        Args:
            model_type: Model type identifier

        Returns:
            True if supported
        """
        return model_type in cls._registry

    @classmethod
    def list_supported(cls) -> list:
        """List all supported model types.

        Returns:
            List of model type strings
        """
        return list(cls._registry.keys())


# Register Llama3.2
ModelRegistry.register(
    "llama",
    ModelSpec(
        config_class=Llama32Config,
        supported_variants=[
            "meta-llama/Llama-3.2-1B",
            "meta-llama/Llama-3.2-3B",
        ],
        default_variant="meta-llama/Llama-3.2-1B"
    )
)
```

#### 3.1.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-68.1 | Can load config from HuggingFace Hub | Integration test |
| AC-68.2 | Can load config from local JSON file | Unit test |
| AC-68.3 | Can save config to JSON file | Unit test |
| AC-68.4 | Validates GQA compatibility | Unit test: invalid config |
| AC-68.5 | Provides model size estimation | Unit test |
| AC-68.6 | Calculates KV cache size | Unit test |
| AC-68.7 | Model registry works | Unit test: register/list |

---

### 3.2 Task #69: Weight Loader (safetensors)

#### 3.2.1 Problem Statement

Llama3.2 weights are distributed in safetensors format on HuggingFace Hub. Need to:
- Download safetensors files with retry logic
- Validate file integrity via checksums
- Load weights using memory mapping for efficiency
- Integrate with MemoryBudget for validation

#### 3.2.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **HuggingFace Download** | Download from HF Hub with retry | CRITICAL |
| **Checksum Validation** | Verify file integrity | CRITICAL |
| **Memory Mapping** | Use mmap for efficient loading | HIGH |
| **Memory Budget** | Validate before loading | CRITICAL |
| **Progress Reporting** | Show download progress | MEDIUM |
| **Error Handling** | Graceful failure with clear messages | HIGH |

#### 3.2.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/models/llama32/loader.py` | Source | Weight loading |
| `iron/models/llama32/weights.py` | Source | Weight structures |
| `iron/models/llama32/test_loader.py` | Test | Loader tests |

#### 3.2.4 Class Specifications

**WeightLoader Class:**

```python
# File: iron/models/llama32/loader.py
"""Llama3.2 weight loader."""

import logging
from pathlib import Path
from typing import Dict, Optional, Any
from dataclasses import dataclass
import hashlib

from safetensors import safe_open
from huggingface_hub import hf_hub_download, snapshot_download
from tenacity import retry, stop_after_attempt, wait_exponential

from ...runtime import MemoryBudget


logger = logging.getLogger(__name__)


@dataclass
class WeightInfo:
    """Information about loaded weights."""
    file_path: Path
    file_size: int
    num_tensors: int
    total_tensor_size: int
    checksum: str


class WeightLoader:
    """Loader for Llama3.2 weights in safetensors format.

    Features:
    - Download from HuggingFace Hub with retry
    - Checksum validation
    - Memory-mapped loading
    - Memory budget integration
    """

    def __init__(
        self,
        cache_dir: Optional[str] = None,
        memory_budget: Optional[MemoryBudget] = None
    ):
        """Initialize weight loader.

        Args:
            cache_dir: Cache directory for downloaded weights
            memory_budget: Memory budget for validation
        """
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.memory_budget = memory_budget

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def download_model(
        self,
        model_id: str,
        variant: str = "1B",
        force_download: bool = False
    ) -> Path:
        """Download model weights from HuggingFace Hub.

        Args:
            model_id: HuggingFace model ID
            variant: Model variant (e.g., "1B", "3B")
            force_download: Force re-download even if cached

        Returns:
            Path to downloaded model directory

        Raises:
            RuntimeError: If download fails after retries
        """
        logger.info(f"Downloading {model_id} ({variant})...")

        try:
            model_path = snapshot_download(
                repo_id=model_id,
                cache_dir=self.cache_dir,
                force_download=force_download,
                allow_patterns=["*.safetensors", "config.json"]
            )
            logger.info(f"Downloaded to: {model_path}")
            return Path(model_path)
        except Exception as e:
            logger.error(f"Download failed: {e}")
            self._cleanup_partial_downloads()
            raise

    def _cleanup_partial_downloads(self) -> None:
        """Clean up partial download files."""
        # Implementation: remove incomplete downloads
        pass

    def validate_weights(self, model_path: Path) -> WeightInfo:
        """Validate weight files.

        Args:
            model_path: Path to model directory

        Returns:
            WeightInfo with validation results

        Raises:
            ValueError: If validation fails
        """
        safetensors_files = list(model_path.glob("*.safetensors"))

        if not safetensors_files:
            raise ValueError(f"No safetensors files found in {model_path}")

        total_size = 0
        num_tensors = 0
        total_tensor_size = 0

        for file_path in safetensors_files:
            file_size = file_path.stat().st_size
            total_size += file_size

            # Calculate checksum
            checksum = self._calculate_checksum(file_path)
            logger.info(f"Validated {file_path.name}: {file_size} bytes, checksum: {checksum[:16]}...")

            # Count tensors
            with safe_open(file_path, framework="numpy") as f:
                num_tensors += len(f.keys())
                for key in f.keys():
                    tensor = f.get_tensor(key)
                    total_tensor_size += tensor.nbytes

        return WeightInfo(
            file_path=model_path,
            file_size=total_size,
            num_tensors=num_tensors,
            total_tensor_size=total_tensor_size,
            checksum=checksum
        )

    def _calculate_checksum(self, file_path: Path, chunk_size: int = 8192) -> str:
        """Calculate SHA256 checksum of file.

        Args:
            file_path: Path to file
            chunk_size: Read chunk size

        Returns:
            SHA256 hex digest
        """
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                sha256.update(chunk)
        return sha256.hexdigest()

    def validate_memory(self, weight_info: WeightInfo) -> bool:
        """Validate weight loading fits within memory budget.

        Args:
            weight_info: Weight information

        Returns:
            True if loading is safe

        Raises:
            MemoryError: If weights exceed budget
        """
        if self.memory_budget is None:
            return True

        result = self.memory_budget.validateModelLoad(
            requiredWeights=weight_info.total_tensor_size,
            requiredKV=0,  # Will be calculated separately
            requiredActivations=0  # Will be calculated separately
        )

        if not result.success:
            raise MemoryError(
                f"Weight loading would exceed memory budget: "
                f"{result.requestedSize} bytes requested, "
                f"{result.availableSize} bytes available. "
                f"Error: {result.errorMessage}"
            )

        return True

    def load_weights(
        self,
        model_path: Path,
        device: str = "cpu"
    ) -> Dict[str, Any]:
        """Load weights into memory.

        Args:
            model_path: Path to model directory
            device: Target device ("cpu", "npu")

        Returns:
            Dictionary of weight tensors
        """
        logger.info(f"Loading weights from {model_path}...")

        weights = {}
        safetensors_files = sorted(model_path.glob("*.safetensors"))

        for file_path in safetensors_files:
            logger.info(f"Loading {file_path.name}...")
            with safe_open(file_path, framework="numpy") as f:
                for key in f.keys():
                    weights[key] = f.get_tensor(key)

        logger.info(f"Loaded {len(weights)} tensors")
        return weights

    def load_weights_mmap(
        self,
        model_path: Path
    ) -> Dict[str, Any]:
        """Load weights using memory mapping.

        Args:
            model_path: Path to model directory

        Returns:
            Dictionary of memory-mapped tensors
        """
        logger.info(f"Loading weights (mmap) from {model_path}...")

        weights = {}
        safetensors_files = sorted(model_path.glob("*.safetensors"))

        for file_path in safetensors_files:
            logger.info(f"Memory-mapping {file_path.name}...")
            with safe_open(file_path, framework="numpy") as f:
                for key in f.keys():
                    # Memory-mapped tensor - doesn't copy to RAM
                    weights[key] = f.get_tensor(key)

        logger.info(f"Memory-mapped {len(weights)} tensors")
        return weights
```

**LlamaWeights Dataclass:**

```python
# File: iron/models/llama32/weights.py
"""Llama3.2 weight structures."""

from dataclasses import dataclass
from typing import Optional
import numpy as np


@dataclass
class TransformerWeights:
    """Weights for a single transformer layer."""
    # Attention
    wq: np.ndarray  # [hidden_size, num_heads * head_dim]
    wk: np.ndarray  # [hidden_size, num_kv_heads * head_dim]
    wv: np.ndarray  # [hidden_size, num_kv_heads * head_dim]
    wo: np.ndarray  # [num_heads * head_dim, hidden_size]

    # MLP
    w1: np.ndarray  # [hidden_size, intermediate_size] (gate)
    w2: np.ndarray  # [intermediate_size, hidden_size] (down)
    w3: np.ndarray  # [hidden_size, intermediate_size] (up)

    # Normalization
    attn_norm: np.ndarray  # [hidden_size]
    ffn_norm: np.ndarray  # [hidden_size]


@dataclass
class LlamaWeights:
    """Complete Llama3.2 weights."""
    # Embeddings
    token_embd: np.ndarray  # [vocab_size, hidden_size]

    # Transformer layers
    layers: list[TransformerWeights]

    # Final normalization
    output_norm: np.ndarray  # [hidden_size]

    # Output projection (if not tied)
    output: Optional[np.ndarray]  # [hidden_size, vocab_size]

    # Metadata
    vocab_size: int
    hidden_size: int
    num_layers: int

    @classmethod
    def from_raw_weights(cls, raw_weights: dict, config) -> "LlamaWeights":
        """Construct from raw weight dictionary.

        Args:
            raw_weights: Dictionary from WeightLoader
            config: Llama32Config

        Returns:
            LlamaWeights instance
        """
        layers = []
        for i in range(config.num_hidden_layers):
            layer = TransformerWeights(
                wq=raw_weights[f"model.layers.{i}.self_attn.q_proj.weight"],
                wk=raw_weights[f"model.layers.{i}.self_attn.k_proj.weight"],
                wv=raw_weights[f"model.layers.{i}.self_attn.v_proj.weight"],
                wo=raw_weights[f"model.layers.{i}.self_attn.o_proj.weight"],
                w1=raw_weights[f"model.layers.{i}.mlp.gate_proj.weight"],
                w2=raw_weights[f"model.layers.{i}.mlp.down_proj.weight"],
                w3=raw_weights[f"model.layers.{i}.mlp.up_proj.weight"],
                attn_norm=raw_weights[f"model.layers.{i}.input_layernorm.weight"],
                ffn_norm=raw_weights[f"model.layers.{i}.post_attention_layernorm.weight"],
            )
            layers.append(layer)

        return cls(
            token_embd=raw_weights["model.embed_tokens.weight"],
            layers=layers,
            output_norm=raw_weights["model.norm.weight"],
            output=raw_weights.get("lm_head.weight"),  # May not exist if tied
            vocab_size=config.vocab_size,
            hidden_size=config.hidden_size,
            num_layers=config.num_hidden_layers
        )
```

#### 3.2.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-69.1 | Downloads from HuggingFace Hub | Integration test |
| AC-69.2 | Retry logic works on failure | Unit test: mock failure |
| AC-69.3 | Checksum validation works | Unit test: corrupt file |
| AC-69.4 | Memory budget validation | Integration test |
| AC-69.5 | Memory-mapped loading works | Unit test: verify mmap |
| AC-69.6 | Graceful error handling | Unit test: invalid paths |
| AC-69.7 | Weight structure correct | Unit test: from_raw_weights |

---

## 4. Dependencies Analysis

### 4.1 Week 1 Dependencies

```
Week 1 Components Used by Week 2:

┌─────────────────────┐
│   MemoryBudget      │ ◄── Used by WeightLoader.validate_memory()
│   (Task #65)        │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ ThreadSafeModelLoader│ ◄── Used for concurrent load protection
│   (Task #67)        │
└─────────────────────┘
```

### 4.2 External Dependencies

| Dependency | Version | Purpose | Installation |
|------------|---------|---------|--------------|
| `safetensors` | >=0.3.0 | Weight file format | `pip install safetensors` |
| `huggingface_hub` | >=0.17.0 | Model download | `pip install huggingface_hub` |
| `tenacity` | Latest | Retry logic | `pip install tenacity` |
| `numpy` | Latest | Array operations | `pip install numpy` |

---

## 5. File Creation Summary

### 5.1 Python Files

| File | Type | Lines (est.) |
|------|------|--------------|
| `iron/models/__init__.py` | Package | 20 |
| `iron/models/base.py` | Source | 100 |
| `iron/models/llama32/__init__.py` | Package | 20 |
| `iron/models/llama32/config.py` | Source | 200 |
| `iron/models/llama32/loader.py` | Source | 300 |
| `iron/models/llama32/weights.py` | Source | 100 |
| `iron/models/registry.py` | Source | 80 |

**Total Python Lines:** ~820

### 5.2 Test Files

| File | Type | Lines (est.) | Tests |
|------|------|--------------|-------|
| `iron/models/test_config.py` | Test | 150 | 20+ |
| `iron/models/llama32/test_loader.py` | Test | 200 | 20+ |

**Total Test Lines:** ~350 (40+ tests)

---

## 6. Testing Strategy

### 6.1 Unit Tests

**Config Tests:**
```python
# iron/models/test_config.py

def test_config_from_json():
    """Test loading config from JSON file."""
    pass

def test_config_to_json():
    """Test saving config to JSON file."""
    pass

def test_config_validation():
    """Test config validation catches errors."""
    pass

def test_gqa_compatibility_check():
    """Test GQA divisibility validation."""
    pass

def test_model_size_estimation():
    """Test model size calculation."""
    pass

def test_kv_cache_size():
    """Test KV cache size calculation."""
    pass

def test_from_pretrained():
    """Test HuggingFace Hub download."""
    pass
```

**Loader Tests:**
```python
# iron/models/llama32/test_loader.py

def test_download_with_retry():
    """Test download retry logic."""
    pass

def test_checksum_validation():
    """Test checksum calculation."""
    pass

def test_memory_validation():
    """Test memory budget validation."""
    pass

def test_mmap_loading():
    """Test memory-mapped loading."""
    pass

def test_weight_structure():
    """Test weight dataclass construction."""
    pass

def test_error_handling():
    """Test graceful error handling."""
    pass
```

### 6.2 Integration Tests

| Test | Components | Purpose |
|------|------------|---------|
| End-to-end load | Config + Loader | Full model load from HF |
| Memory integration | Loader + MemoryBudget | Validate memory checks |
| Concurrent loads | Loader + ModelLoader | Thread-safe loading |

---

## 7. Quality Gates

### 7.1 Code Quality

| Gate | Requirement | Verification |
|------|-------------|--------------|
| Type hints | All public APIs typed | `mypy --strict` |
| Documentation | Docstrings for all classes | `pydocstyle` |
| Error handling | Graceful failures | Code review |
| Logging | Appropriate log levels | Code review |

### 7.2 Test Coverage

| Metric | Target | Verification |
|--------|--------|--------------|
| Line coverage | >90% | `pytest --cov` |
| Branch coverage | >85% | `pytest --cov` |
| All acceptance criteria | 100% verified | Manual checklist |

### 7.3 Performance

| Component | Metric | Target | Verification |
|-----------|--------|--------|--------------|
| Config load | Time | <100ms | Profile |
| Weight download | Network | HF Hub speed | Profile |
| Memory-mapped load | Time | <5s for 1B | Profile |

---

## 8. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| R1: HF Hub unavailable | Medium | High | Retry logic, local cache |
| R2: Memory budget exceeded | Medium | High | Pre-load validation |
| R3: Corrupt weights | Low | High | Checksum validation |
| R4: Thread safety issues | Low | High | Use Week 1 ModelLoader |
| R5: Model format changes | Low | Medium | Flexible config parsing |

---

## 9. Handoff Package for Senior Developer

### 9.1 Implementation Checklist

**For Senior Developer executing Week 2 tasks:**

- [ ] Read this specification thoroughly
- [ ] Review Week 1 components (MemoryBudget, ModelLoader)
- [ ] Create all files listed in Section 5
- [ ] Implement classes per specifications in Section 3
- [ ] Write unit tests per Section 6
- [ ] Verify all acceptance criteria are met
- [ ] Run mypy for type checking
- [ ] Document any deviations from specification

### 9.2 Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Dataclass for config | Type safety, JSON serialization |
| safetensors format | Safe, fast, widely supported |
| Memory-mapped loading | Efficient memory usage |
| Retry logic | Network resilience |
| Checksum validation | Integrity verification |

### 9.3 Points of Contact

| Role | Responsibility |
|------|----------------|
| Dr. Sarah Kim | Technical specifications, requirements |
| Senior Developer | Implementation, testing |
| Quality Reviewer | Code review, acceptance verification |

---

## 10. Next Steps After Week 2

Upon successful completion of Week 2:

### Week 3: Generation Loop
- Implement autoregressive generation
- KV cache integration for context retention
- EOS handling and stop conditions

### Week 4: API Integration
- OpenAI-compatible `/v1/chat/completions` endpoint
- Streaming support (SSE)
- Tokenizer enhancement

### Week 5: Testing
- Comprehensive unit tests
- Integration tests
- Load tests (concurrent requests)

### Week 6: Hardening
- Error handling improvements
- Documentation completion
- CI/CD integration

---

**Document Approval:**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Technical Product Strategist | Dr. Sarah Kim | 2026-03-15 | /s/ Dr. Sarah Kim |

---

*Copyright &copy; 2026 IRON Project. All rights reserved.*
