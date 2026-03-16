# Phase 3 Week 2 Implementation: Senior Developer Handoff Package

**Document Type:** Implementation Handoff Package
**Date:** 2026-03-15
**Prepared By:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**For:** Senior Developer - Week 2 Model Loader Implementation

---

## 1. Executive Summary

### 1.1 Mission

Implement **2 critical components** for Phase 3 Week 2: Model Loader. These components enable loading Llama3.2 model configurations and weights from HuggingFace Hub.

### 1.2 Week 2 Tasks Overview

| # | Task ID | Component | Priority | Effort | Status |
|---|---------|-----------|----------|--------|--------|
| 1 | #68 | Llama3.2 Config Loader | CRITICAL | 2 days | READY |
| 2 | #69 | Weight Loader (safetensors) | CRITICAL | 3 days | READY |

**Total Effort:** 5 developer-days

### 1.3 Key Documents

| Document | Purpose | Location |
|----------|---------|----------|
| Implementation Scope | Full specifications & acceptance criteria | `docs/PHASE3_WEEK2_IMPLEMENTATION_SCOPE.md` |
| Week 1 Scope | Foundation components reference | `docs/PHASE3_WEEK1_IMPLEMENTATION_SCOPE.md` |
| Week 1 Progress | Foundation completion report | `docs/PHASE3_WEEK1_PROGRESS_REPORT.md` |
| Status Tracker | Project-wide status | `docs/PROJECT_STATUS_TRACKER.md` |

### 1.4 Week 1 Foundation Status

Week 1 components are **COMPLETE** and available for Week 2 integration:

| Component | Status | Week 2 Usage |
|-----------|--------|--------------|
| MemoryBudget | COMPLETE | Validate model load before downloading |
| ThreadSafeModelLoader | COMPLETE | Queue concurrent load requests |
| GenerationConfig | COMPLETE | Model configuration integration |
| RoPECache | COMPLETE | Config provides RoPE parameters |
| PagedKVCache | COMPLETE | Config provides KV cache sizing |

---

## 2. Implementation Checklist

### 2.1 Pre-Implementation

Before starting coding:

- [ ] Read `PHASE3_WEEK2_IMPLEMENTATION_SCOPE.md` thoroughly
- [ ] Review Week 1 components in `iron/runtime/cpp/include/iron/`
- [ ] Review `PHASE3_WEEK1_IMPLEMENTATION_SCOPE.md` for context
- [ ] Understand HuggingFace Hub API (`huggingface_hub` package)
- [ ] Understand safetensors format (`safetensors` package)
- [ ] Set up development environment (Python 3.10+, pip dependencies)

### 2.2 File Creation Checklist

Create the following files:

#### Python Source Files (6 files)

- [ ] `iron/models/__init__.py` - Model package init
- [ ] `iron/models/base.py` - Base model interface
- [ ] `iron/models/llama32/__init__.py` - Llama32 package init
- [ ] `iron/models/llama32/config.py` - Model configuration (200 lines)
- [ ] `iron/models/llama32/loader.py` - Weight loading (300 lines)
- [ ] `iron/models/llama32/weights.py` - Weight structures (100 lines)
- [ ] `iron/models/registry.py` - Model registry (80 lines)

#### Test Files (2 files)

- [ ] `iron/models/test_config.py` - Config tests (150 lines, 20+ tests)
- [ ] `iron/models/llama32/test_loader.py` - Loader tests (200 lines, 20+ tests)

### 2.3 Implementation Order

Recommended implementation sequence:

```
Day 1-2: Task #68 - Config Loader
         └── Create Llama32Config dataclass
         └── Implement from_pretrained() for HF Hub
         └── Implement from_json() / to_json()
         └── Add validation (_validate())
         └── Create ModelRegistry

Day 2-4: Task #69 - Weight Loader
         └── Create WeightLoader class
         └── Implement download_model() with retry
         └── Implement validate_weights() with checksum
         └── Implement load_weights_mmap() for efficient loading
         └── Integrate with MemoryBudget
         └── Create LlamaWeights dataclass

Day 5:   Integration & Testing
         └── Write 40+ unit tests
         └── Run integration tests
         └── Quality review
```

---

## 3. Technical Specifications Summary

### 3.1 Task #68: Llama3.2 Config Loader

**Purpose:** Load and validate Llama3.2 model configuration from HuggingFace Hub

**Key Design Decisions:**
- Dataclass for type safety and JSON serialization
- HuggingFace Hub integration for remote loading
- Validation for GQA compatibility
- Helper methods for KV cache sizing

**Files:**
- `iron/models/llama32/config.py` - Main configuration class
- `iron/models/registry.py` - Model architecture registry

**Acceptance Criteria:**
- [ ] Can load config from HuggingFace Hub
- [ ] Can load config from local JSON file
- [ ] Can save config to JSON file
- [ ] Validates GQA compatibility
- [ ] Provides model size estimation
- [ ] Calculates KV cache size per token
- [ ] Model registry works

**Key Methods:**
```python
# Load from HuggingFace Hub
config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")

# Load from local file
config = Llama32Config.from_json("config.json")

# Save to file
config.to_json("output_config.json")

# Helper properties
print(config.model_size)  # "1B"
print(config.kv_cache_size_per_token)  # bytes per token
```

---

### 3.2 Task #69: Weight Loader (safetensors)

**Purpose:** Download and load Llama3.2 weights in safetensors format

**Key Design Decisions:**
- safetensors format for safe, fast loading
- Retry logic for network resilience
- Checksum validation for integrity
- Memory-mapped loading for efficiency
- Integration with MemoryBudget

**Files:**
- `iron/models/llama32/loader.py` - Weight loader
- `iron/models/llama32/weights.py` - Weight structures

**Acceptance Criteria:**
- [ ] Downloads from HuggingFace Hub
- [ ] Retry logic works on failure
- [ ] Checksum validation works
- [ ] Memory budget validation works
- [ ] Memory-mapped loading works
- [ ] Graceful error handling
- [ ] Weight structure correct

**Key Methods:**
```python
# Initialize with memory budget
from iron.runtime import MemoryBudget
loader = WeightLoader(memory_budget=MemoryBudget())

# Download model
model_path = loader.download_model("meta-llama/Llama-3.2-1B")

# Validate weights
weight_info = loader.validate_weights(model_path)

# Validate memory
loader.validate_memory(weight_info)

# Load weights (memory-mapped)
weights = loader.load_weights_mmap(model_path)
```

---

## 4. Code Templates

### 4.1 Config Template

```python
# Starter template for iron/models/llama32/config.py

from dataclasses import dataclass, field
from typing import Optional, List
from pathlib import Path


@dataclass
class Llama32Config:
    """Llama3.2 model configuration."""

    # Architecture defaults for Llama3.2-1B
    vocab_size: int = 128256
    hidden_size: int = 2048
    intermediate_size: int = 8192
    num_hidden_layers: int = 16
    num_attention_heads: int = 32
    num_key_value_heads: int = 8
    head_dim: int = 64
    max_position_embeddings: int = 131072
    rope_theta: float = 500000.0
    rms_norm_eps: float = 1e-5

    def __post_init__(self):
        self._validate()

    def _validate(self):
        """Validate configuration."""
        # Add validation logic here
        pass

    @classmethod
    def from_pretrained(cls, model_id: str, **kwargs):
        """Load from HuggingFace Hub."""
        # Implement HF Hub download
        pass

    @classmethod
    def from_json(cls, json_path: str):
        """Load from JSON file."""
        # Implement JSON loading
        pass
```

### 4.2 Loader Template

```python
# Starter template for iron/models/llama32/loader.py

from pathlib import Path
from typing import Dict, Optional
from safetensors import safe_open
from huggingface_hub import hf_hub_download
from tenacity import retry, stop_after_attempt, wait_exponential


class WeightLoader:
    """Llama3.2 weight loader."""

    def __init__(self, cache_dir=None, memory_budget=None):
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.memory_budget = memory_budget

    @retry(stop=stop_after_attempt(3),
           wait=wait_exponential(multiplier=1, min=4, max=10))
    def download_model(self, model_id: str) -> Path:
        """Download model from HuggingFace Hub."""
        # Implement download with retry
        pass

    def validate_weights(self, model_path: Path):
        """Validate weight files."""
        # Implement checksum validation
        pass

    def load_weights_mmap(self, model_path: Path) -> Dict:
        """Load weights using memory mapping."""
        # Implement mmap loading
        pass
```

---

## 5. Testing Requirements

### 5.1 Unit Tests

Create unit tests:

| Component | Test File | Key Tests |
|-----------|-----------|-----------|
| Llama32Config | `test_config.py` | JSON load/save, validation, HF download |
| WeightLoader | `test_loader.py` | Download retry, checksum, mmap, errors |

### 5.2 Test Execution

```bash
# Run Python tests
cd iron
python -m pytest models/test_config.py -v
python -m pytest models/llama32/test_loader.py -v

# Run with coverage
python -m pytest models/ --cov=iron/models --cov-report=html
```

---

## 6. Quality Gates

### 6.1 Code Quality

| Gate | Requirement | Verification |
|------|-------------|--------------|
| Type hints | All public APIs typed | `mypy --strict iron/models/` |
| Documentation | Docstrings for all classes | `pydocstyle iron/models/` |
| Error handling | Graceful failures | Code review |
| Logging | Appropriate log levels | Code review |

### 6.2 Test Coverage

| Metric | Target | Verification |
|--------|--------|--------------|
| Line coverage | >90% | `pytest --cov` |
| Branch coverage | >85% | `pytest --cov` |
| All acceptance criteria | 100% verified | Manual checklist |

### 6.3 Performance

| Component | Metric | Target | Verification |
|-----------|--------|--------|--------------|
| Config load | Time | <100ms | Profile |
| Weight download | Network | HF Hub speed | Profile |
| Memory-mapped load | Time | <5s for 1B | Profile |

---

## 7. Integration Points

### 7.1 With Week 1 Components

```python
# Integration with MemoryBudget
from iron.runtime import MemoryBudget

memory_budget = MemoryBudget()
loader = WeightLoader(memory_budget=memory_budget)

# Validate before loading
weight_info = loader.validate_weights(model_path)
loader.validate_memory(weight_info)  # Raises MemoryError if exceeded

# Integration with ThreadSafeModelLoader
from iron.runtime import ThreadSafeModelLoader

model_loader = ThreadSafeModelLoader(memory_budget=memory_budget)
result = model_loader.load(model_path)  # Thread-safe loading
```

### 7.2 With Python API

```python
# Usage pattern for Week 3-4
from iron.models import Llama32Config, WeightLoader

# Load configuration
config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")

# Load weights
loader = WeightLoader()
model_path = loader.download_model("meta-llama/Llama-3.2-1B")
weights = loader.load_weights_mmap(model_path)

# Ready for model class (Week 3)
# model = Llama32Model(config, weights)
```

---

## 8. Risk Mitigation

### 8.1 Known Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| R1: HF Hub unavailable | Medium | High | Retry logic, local cache |
| R2: Memory budget exceeded | Medium | High | Pre-load validation |
| R3: Corrupt weights | Low | High | Checksum validation |
| R4: Thread safety issues | Low | High | Use Week 1 ModelLoader |
| R5: Model format changes | Low | Medium | Flexible config parsing |

### 8.2 Escalation Path

If you encounter blockers:

1. **Technical questions:** Review `PHASE3_WEEK2_IMPLEMENTATION_SCOPE.md`
2. **Design clarifications:** Consult with Dr. Sarah Kim
3. **Code review:** Schedule review with Quality Reviewer
4. **Integration issues:** Check Week 1 component code

---

## 9. Deliverables

### 9.1 Required Deliverables

| # | Deliverable | Format | Location |
|---|-------------|--------|----------|
| 1 | Config Loader implementation | Python source | `iron/models/llama32/config.py` |
| 2 | Weight Loader implementation | Python source | `iron/models/llama32/loader.py` |
| 3 | Weight structures | Python source | `iron/models/llama32/weights.py` |
| 4 | Model registry | Python source | `iron/models/registry.py` |
| 5 | Unit tests | Python tests | `iron/models/test_config.py`, `test_loader.py` |
| 6 | Package inits | Python init | `iron/models/__init__.py`, etc. |

### 9.2 Optional Deliverables

| # | Deliverable | Format | Notes |
|---|-------------|--------|-------|
| 7 | Integration tests | Python tests | If time permits |
| 8 | API documentation | Sphinx | Auto-generated |

---

## 10. Acceptance Process

### 10.1 Self-Verification

Before submitting for review:

- [ ] All files pass `mypy --strict`
- [ ] All unit tests pass
- [ ] Code coverage meets targets (>90% line, >85% branch)
- [ ] No linting errors (`pylint`, `pydocstyle`)
- [ ] All acceptance criteria verified
- [ ] Documentation complete (docstrings)

### 10.2 Code Review

Submit for review:

1. Create pull request to `devel` branch
2. Request review from:
   - Dr. Sarah Kim (Technical specifications)
   - Quality Reviewer (Code quality)
3. Address review comments
4. Re-run tests after changes

### 10.3 Merge Criteria

- [ ] All review comments addressed
- [ ] CI/CD pipeline passes
- [ ] Test coverage verified
- [ ] Documentation complete

---

## 11. Post-Week 2: Next Steps

Upon successful completion of Week 2:

### Week 3: Generation Loop
- Implement autoregressive generation with KV cache
- EOS handling and stop conditions
- Context retention across tokens

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

## 12. Quick Reference

### 12.1 Command Summary

```bash
# Run config tests
cd iron
python -m pytest models/test_config.py -v

# Run loader tests
python -m pytest models/llama32/test_loader.py -v

# Run all model tests with coverage
python -m pytest models/ --cov=iron/models --cov-report=html

# Type checking
mypy --strict iron/models/

# Linting
pylint iron/models/
pydocstyle iron/models/
```

### 12.2 Key Classes

```python
# Config
iron.models.llama32.config.Llama32Config
  - from_pretrained(model_id) -> Config
  - from_json(path) -> Config
  - to_json(path) -> None
  - model_size -> str
  - kv_cache_size_per_token -> int

# Loader
iron.models.llama32.loader.WeightLoader
  - download_model(model_id) -> Path
  - validate_weights(path) -> WeightInfo
  - validate_memory(info) -> bool
  - load_weights_mmap(path) -> Dict

# Weights
iron.models.llama32.weights.LlamaWeights
  - from_raw_weights(dict, config) -> LlamaWeights
```

### 12.3 Key Functions

```python
# Config loading
config = Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")
config = Llama32Config.from_json("config.json")

# Weight loading
loader = WeightLoader(memory_budget=MemoryBudget())
model_path = loader.download_model("meta-llama/Llama-3.2-1B")
weights = loader.load_weights_mmap(model_path)

# Memory validation
weight_info = loader.validate_weights(model_path)
loader.validate_memory(weight_info)  # Raises MemoryError if exceeded
```

---

## 13. Contact Information

| Role | Name | Responsibility |
|------|------|----------------|
| Technical Product Strategist | Dr. Sarah Kim | Specifications, requirements, design |
| Senior Developer | You | Implementation, testing |
| Quality Reviewer | TBD | Code review, acceptance verification |

---

## 14. Document History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-03-15 | Initial creation - Week 2 handoff package | Dr. Sarah Kim |

---

**Handoff Package Prepared By:**

Dr. Sarah Kim
Technical Product Strategist & Engineering Lead
Date: 2026-03-15

---

*Copyright &copy; 2026 IRON Project. All rights reserved.*
