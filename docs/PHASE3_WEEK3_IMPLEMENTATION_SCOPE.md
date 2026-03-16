# Phase 3 Week 3 Implementation Scope: Generation Loop

**Document Type:** Technical Implementation Specification
**Date:** 2026-03-15
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Version:** 1.0.0
**Status:** READY FOR EXECUTION

---

## 1. Executive Summary

### 1.1 Purpose

This document defines the implementation scope for **Phase 3 Week 3: Generation Loop**. These components enable autoregressive token generation with KV cache persistence for context retention.

### 1.2 Week 3 Goals

Implement three critical components that enable:
- Token-by-token autoregressive generation
- KV cache persistence across tokens for context retention
- Proper EOS detection and stop condition handling
- Streaming generation pipeline for low-latency output

### 1.3 Success Criteria

| Criterion | Measurement | Target |
|-----------|-------------|--------|
| **Autoregressive Generation** | Can generate tokens one-by-one | 10+ tokens generated |
| **KV Cache Persistence** | Context retained across tokens | Attention uses past KV |
| **EOS Handling** | Stops on end-of-sequence token | Clean termination |
| **Stop Conditions** | Max tokens, stop strings supported | Configurable limits |
| **Test Coverage** | Unit tests with >90% coverage | 50+ tests |
| **Quality Review** | GO decision from reviewer | No blocking issues |

### 1.4 Week 1-2 Dependency Status

Week 3 builds on Week 1-2 foundation components:

| Week 1-2 Component | Week 3 Usage | Status |
|--------------------|--------------|--------|
| `PagedKVCache` | Store KV states per token | COMPLETE |
| `SequenceState` | Track generation state per sequence | COMPLETE |
| `GenerationConfig` | EOS tokens, stop conditions | COMPLETE |
| `Llama32Config` | Model hyperparameters | COMPLETE |
| `WeightLoader` | Load model weights | COMPLETE |
| `MemoryBudget` | Memory validation during generation | COMPLETE |
| `RoPECache` | Pre-computed RoPE angles | COMPLETE |

---

## 2. Task Overview

### 2.1 Week 3 Task List

| Task ID | Subject | Priority | Effort | Dependencies |
|---------|---------|----------|--------|--------------|
| **#70** | Autoregressive Generation Loop | CRITICAL | 2 days | Tasks #68-#69 complete |
| **#71** | KV Cache Persistence | CRITICAL | 2 days | Task #70, Week 1 KVCache |
| **#72** | Streaming Generation Optimization | HIGH | 1 day | Task #70 |

**Total Effort:** 5 developer-days

### 2.2 Implementation Order

```
Day 1-2: Task #70 - Generation Loop Core
         ├── Create generation package structure
         ├── Implement main generation loop
         ├── Token-by-token forward pass
         └── Logits to token sampling

Day 2-4: Task #71 - KV Cache Integration
         ├── Integrate PagedKVCache with generation
         ├── SequenceState tracking per sequence
         ├── KV cache write after each token
         └── KV cache read for attention context

Day 4-5: Task #72 - Streaming & Stop Conditions
         ├── EOS token detection
         ├── Stop string detection
         ├── Max token limit enforcement
         └── Streaming output pipeline

Day 5:   Integration & Testing
         ├── End-to-end generation test
         ├── Unit tests (50+ tests)
         └── Quality review
```

---

## 3. Technical Specifications

### 3.1 Task #70: Autoregressive Generation Loop

#### 3.1.1 Problem Statement

Generate text tokens autoregressively (one token at a time) by:
- Running forward pass on input prompt (prefill phase)
- Sampling next token from logits
- Running forward pass on single token (decode phase)
- Repeating until stop condition met

#### 3.1.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **Prefill Phase** | Process full prompt in parallel | CRITICAL |
| **Decode Phase** | Process single token efficiently | CRITICAL |
| **Token Sampling** | Support temperature, top_p, top_k | CRITICAL |
| **Logits Processing** | Apply temperature, repetition penalty | HIGH |
| **State Management** | Track position, sequence ID | HIGH |

#### 3.1.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/generation/__init__.py` | Package | Generation package init |
| `iron/generation/loop.py` | Source | Main generation loop |
| `iron/generation/sampling.py` | Source | Token sampling strategies |
| `iron/generation/test_loop.py` | Test | Generation loop tests |
| `iron/generation/test_sampling.py` | Test | Sampling tests |

#### 3.1.4 Class Specifications

**GenerationLoop Class:**

```python
# File: iron/generation/loop.py
"""Autoregressive generation loop."""

import logging
from typing import Iterator, List, Optional
from dataclasses import dataclass

from ..models.llama32.config import Llama32Config
from ..models.llama32.loader import LlamaWeights
from ..api.generation_config import GenerationConfig


logger = logging.getLogger(__name__)


@dataclass
class GenerationResult:
    """Result from generation step."""
    token_id: int
    token_text: str
    logit_prob: float
    is_eos: bool
    stop_reason: Optional[str] = None


class GenerationLoop:
    """Autoregressive generation loop for Llama3.2.

    Supports:
    - Prefill phase (parallel prompt processing)
    - Decode phase (token-by-token generation)
    - Configurable sampling (temperature, top_p, top_k)
    - Stop conditions (EOS, max_tokens, stop_strings)
    """

    def __init__(
        self,
        config: Llama32Config,
        weights: LlamaWeights,
        generation_config: Optional[GenerationConfig] = None
    ):
        """Initialize generation loop.

        Args:
            config: Llama3.2 model configuration
            weights: Llama3.2 model weights
            generation_config: Generation configuration
        """
        self.config = config
        self.weights = weights
        self.generation_config = generation_config or GenerationConfig()

    def prefill(self, prompt_tokens: List[int]) -> List[float]:
        """Process full prompt in parallel.

        Args:
            prompt_tokens: Tokenized prompt

        Returns:
            Logits for next token prediction
        """
        logger.info(f"Prefill phase: {len(prompt_tokens)} tokens")
        # TODO: Implement prompt processing
        # 1. Forward pass through all layers
        # 2. Write KV cache for all positions
        # 3. Return logits for last position
        pass

    def decode(self, token_id: int, position: int) -> List[float]:
        """Process single token.

        Args:
            token_id: Current token ID
            position: Position in sequence

        Returns:
            Logits for next token prediction
        """
        # TODO: Implement single-token forward pass
        # 1. Forward pass through all layers
        # 2. Read KV cache for attention context
        # 3. Write new KV cache entry
        # 4. Return logits
        pass

    def sample(self, logits: List[float]) -> int:
        """Sample next token from logits.

        Args:
            logits: Raw logits from model

        Returns:
            Sampled token ID
        """
        # TODO: Implement sampling
        # 1. Apply temperature
        # 2. Apply top_k filtering
        # 3. Apply top_p (nucleus) filtering
        # 4. Sample from distribution
        pass

    def generate(
        self,
        prompt_tokens: List[int],
        max_tokens: Optional[int] = None
    ) -> Iterator[GenerationResult]:
        """Generate tokens autoregressively.

        Args:
            prompt_tokens: Tokenized prompt
            max_tokens: Maximum tokens to generate

        Yields:
            GenerationResult for each generated token

        Example:
            >>> loop = GenerationLoop(config, weights)
            >>> prompt = tokenizer.encode("Hello, how are you?")
            >>> for result in loop.generate(prompt):
            ...     print(tokenizer.decode([result.token_id]), end="")
        """
        # TODO: Implement main generation loop
        # 1. Prefill phase
        # 2. Sample first token
        # 3. Decode loop until stop condition
        # 4. Yield results
        pass
```

**TokenSampler Class:**

```python
# File: iron/generation/sampling.py
"""Token sampling strategies."""

import numpy as np
from typing import List


class TokenSampler:
    """Token sampling with temperature, top_k, top_p."""

    def __init__(
        self,
        temperature: float = 0.7,
        top_k: int = 50,
        top_p: float = 0.9,
        repetition_penalty: float = 1.0
    ):
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p
        self.repetition_penalty = repetition_penalty

    def apply_temperature(self, logits: np.ndarray) -> np.ndarray:
        """Apply temperature scaling."""
        if self.temperature == 0:
            # Greedy decoding
            return logits
        return logits / self.temperature

    def apply_top_k(self, logits: np.ndarray) -> np.ndarray:
        """Filter to top_k tokens."""
        if self.top_k <= 0:
            return logits
        indices_to_remove = np.argsort(logits)[:-self.top_k]
        logits[indices_to_remove] = float('-inf')
        return logits

    def apply_top_p(self, logits: np.ndarray) -> np.ndarray:
        """Nucleus sampling - filter to top_p probability mass."""
        if self.top_p <= 0 or self.top_p >= 1:
            return logits
        sorted_indices = np.argsort(logits)[::-1]
        sorted_logits = logits[sorted_indices]
        cumulative_probs = np.cumsum(np.exp(sorted_logits))
        cumulative_probs = cumulative_probs / np.sum(np.exp(sorted_logits))
        # Remove tokens with cumulative probability above top_p
        sorted_indices_to_remove = sorted_indices[cumulative_probs > self.top_p]
        logits[sorted_indices_to_remove] = float('-inf')
        return logits

    def sample(self, logits: np.ndarray) -> int:
        """Sample token from logits."""
        # Apply all transformations
        logits = self.apply_temperature(logits)
        logits = self.apply_top_k(logits)
        logits = self.apply_top_p(logits)
        # Convert to probabilities
        probs = np.exp(logits) / np.sum(np.exp(logits))
        # Sample
        return np.random.choice(len(logits), p=probs)
```

#### 3.1.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-70.1 | Prefill processes full prompt | Unit test: forward pass |
| AC-70.2 | Decode processes single token | Unit test: single token forward |
| AC-70.3 | Sampling produces valid tokens | Unit test: token ID in vocab |
| AC-70.4 | Temperature affects distribution | Unit test: different temps |
| AC-70.5 | Top_k filtering works | Unit test: only top_k tokens possible |
| AC-70.6 | Top_p filtering works | Unit test: probability mass check |
| AC-70.7 | Generate yields tokens | Integration test: 10+ tokens |

---

### 3.2 Task #71: KV Cache Persistence

#### 3.2.1 Problem Statement

Maintain KV cache across tokens for context retention:
- Write KV entries after each token generation
- Read KV entries for attention computation
- Track KV block allocation per sequence
- Support multiple concurrent sequences

#### 3.2.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **KV Write** | Store K, V after each token | CRITICAL |
| **KV Read** | Retrieve K, V for attention | CRITICAL |
| **Block Allocation** | Allocate KV blocks per sequence | CRITICAL |
| **Sequence Tracking** | Track position, blocks per sequence | HIGH |
| **Memory Management** | Release blocks on sequence end | HIGH |

#### 3.2.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/generation/kv_manager.py` | Source | KV cache management |
| `iron/generation/test_kv_manager.py` | Test | KV manager tests |

#### 3.2.4 Class Specifications

**KVCacheManager Class:**

```python
# File: iron/generation/kv_manager.py
"""KV cache management for generation."""

import logging
from typing import Dict, List, Optional, Tuple
import numpy as np

from ..runtime import PagedKVCache, SequenceState


logger = logging.getLogger(__name__)


class KVCacheManager:
    """Manages KV cache during generation.

    Responsibilities:
    - Allocate KV blocks for new sequences
    - Write KV entries for each token
    - Read KV context for attention
    - Track sequence state
    - Release blocks on sequence completion
    """

    def __init__(
        self,
        kv_cache: PagedKVCache,
        config: Llama32Config
    ):
        """Initialize KV cache manager.

        Args:
            kv_cache: PagedKVCache instance
            config: Llama3.2 configuration
        """
        self.kv_cache = kv_cache
        self.config = config
        self.sequences: Dict[int, SequenceState] = {}

    def start_sequence(self, prompt_length: int) -> int:
        """Start new generation sequence.

        Args:
            prompt_length: Length of prompt tokens

        Returns:
            Sequence ID
        """
        sequence_id = self._generate_sequence_id()
        # Allocate KV blocks for prompt + max generation
        total_tokens = prompt_length + self.config.max_position_embeddings
        num_blocks = (total_tokens + self.config.block_size - 1) // self.config.block_size
        block_ids = self.kv_cache.allocate_blocks(num_blocks)

        self.sequences[sequence_id] = SequenceState(
            sequence_id=sequence_id,
            kv_blocks=block_ids,
            current_length=prompt_length
        )
        logger.info(f"Started sequence {sequence_id} with {len(block_ids)} blocks")
        return sequence_id

    def write_kv(
        self,
        sequence_id: int,
        position: int,
        key: np.ndarray,
        value: np.ndarray,
        layer: int
    ) -> None:
        """Write KV entry for token.

        Args:
            sequence_id: Sequence ID
            position: Token position
            key: Key vector [num_heads, head_dim]
            value: Value vector [num_heads, head_dim]
            layer: Layer index
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")

        state = self.sequences[sequence_id]
        # Calculate block index and offset
        block_index = position // self.config.block_size
        block_offset = position % self.config.block_size

        # Write to KV cache
        self.kv_cache.write_key(
            layer=layer,
            block_id=state.kv_blocks[block_index],
            offset=block_offset,
            key=key
        )
        self.kv_cache.write_value(
            layer=layer,
            block_id=state.kv_blocks[block_index],
            offset=block_offset,
            value=value
        )

    def read_kv_context(
        self,
        sequence_id: int,
        context_length: int,
        layer: int
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Read KV context for attention.

        Args:
            sequence_id: Sequence ID
            context_length: Number of tokens to read
            layer: Layer index

        Returns:
            Tuple of (keys, values) with shape [context_length, num_heads, head_dim]
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")

        state = self.sequences[sequence_id]
        current_pos = state.current_length

        # Read KV entries for context
        keys = np.zeros((context_length, self.config.num_attention_heads, self.config.head_dim))
        values = np.zeros((context_length, self.config.num_attention_heads, self.config.head_dim))

        for i in range(context_length):
            position = current_pos - context_length + i
            block_index = position // self.config.block_size
            block_offset = position % self.config.block_size

            keys[i], values[i] = self.kv_cache.read_key_value(
                layer=layer,
                block_id=state.kv_blocks[block_index],
                offset=block_offset
            )

        return keys, values

    def update_position(self, sequence_id: int, new_length: int) -> None:
        """Update sequence position.

        Args:
            sequence_id: Sequence ID
            new_length: New sequence length
        """
        if sequence_id not in self.sequences:
            raise ValueError(f"Unknown sequence {sequence_id}")
        self.sequences[sequence_id].current_length = new_length

    def end_sequence(self, sequence_id: int) -> None:
        """End sequence and release resources.

        Args:
            sequence_id: Sequence ID
        """
        if sequence_id not in self.sequences:
            return

        state = self.sequences[sequence_id]
        # Release KV blocks
        for block_id in state.kv_blocks:
            self.kv_cache.release_block(block_id)

        del self.sequences[sequence_id]
        logger.info(f"Ended sequence {sequence_id}")

    def _generate_sequence_id(self) -> int:
        """Generate unique sequence ID."""
        import time
        return int(time.time() * 1000) % (2**31)
```

#### 3.2.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-71.1 | KV write stores data correctly | Unit test: write then read |
| AC-71.2 | KV read retrieves correct data | Unit test: read after write |
| AC-71.3 | Block allocation works | Unit test: allocate/release |
| AC-71.4 | Sequence tracking accurate | Unit test: position updates |
| AC-71.5 | Multiple sequences supported | Integration test: 2+ sequences |
| AC-71.6 | Memory released on end | Unit test: block count after release |

---

### 3.3 Task #72: Streaming Generation Optimization

#### 3.3.1 Problem Statement

Implement efficient streaming generation with:
- EOS token detection and clean termination
- Stop string detection in decoded output
- Max token limit enforcement
- Token-by-token streaming output

#### 3.3.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **EOS Detection** | Stop on end-of-sequence token | CRITICAL |
| **Stop Strings** | Detect configured stop strings | HIGH |
| **Max Tokens** | Enforce maximum generation limit | HIGH |
| **Streaming Output** | Yield tokens as generated | CRITICAL |
| **Clean Termination** | Proper cleanup on stop | HIGH |

#### 3.3.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/generation/stop_conditions.py` | Source | Stop condition handling |
| `iron/generation/test_stop_conditions.py` | Test | Stop condition tests |

#### 3.3.4 Class Specifications

**StopConditionChecker Class:**

```python
# File: iron/generation/stop_conditions.py
"""Stop condition detection for generation."""

import logging
from typing import List, Optional, Set
from dataclasses import dataclass

from ..api.generation_config import GenerationConfig


logger = logging.getLogger(__name__)


@dataclass
class StopResult:
    """Result of stop condition check."""
    should_stop: bool
    reason: Optional[str] = None
    stop_string: Optional[str] = None


class StopConditionChecker:
    """Checks stop conditions during generation.

    Supported conditions:
    - EOS token detection
    - Stop string detection
    - Maximum token limit
    """

    def __init__(self, config: GenerationConfig):
        """Initialize stop condition checker.

        Args:
            config: Generation configuration
        """
        self.config = config
        self.eos_tokens: Set[int] = set(config.eos_tokens or [])
        self.stop_strings: List[str] = config.stop_strings or []
        self.max_tokens: int = config.max_new_tokens or 2048

    def check_eos(self, token_id: int) -> StopResult:
        """Check if token is EOS.

        Args:
            token_id: Generated token ID

        Returns:
            StopResult with EOS status
        """
        if token_id in self.eos_tokens:
            logger.info(f"EOS token {token_id} detected")
            return StopResult(should_stop=True, reason="eos_token")
        return StopResult(should_stop=False)

    def check_stop_string(
        self,
        generated_text: str,
        tokenizer
    ) -> StopResult:
        """Check if generated text contains stop string.

        Args:
            generated_text: Full generated text so far
            tokenizer: Tokenizer for decoding

        Returns:
            StopResult with stop string status
        """
        for stop_string in self.stop_strings:
            if stop_string in generated_text:
                logger.info(f"Stop string '{stop_string}' detected")
                return StopResult(
                    should_stop=True,
                    reason="stop_string",
                    stop_string=stop_string
                )
        return StopResult(should_stop=False)

    def check_max_tokens(self, num_generated: int) -> StopResult:
        """Check if max tokens reached.

        Args:
            num_generated: Number of tokens generated

        Returns:
            StopResult with max tokens status
        """
        if num_generated >= self.max_tokens:
            logger.info(f"Max tokens ({self.max_tokens}) reached")
            return StopResult(should_stop=True, reason="max_tokens")
        return StopResult(should_stop=False)

    def check_all(
        self,
        token_id: int,
        generated_text: str,
        num_generated: int,
        tokenizer=None
    ) -> StopResult:
        """Check all stop conditions.

        Args:
            token_id: Current token ID
            generated_text: Generated text so far
            num_generated: Number of tokens generated
            tokenizer: Tokenizer for stop string check

        Returns:
            StopResult with first triggered condition
        """
        # Check EOS
        result = self.check_eos(token_id)
        if result.should_stop:
            return result

        # Check max tokens
        result = self.check_max_tokens(num_generated)
        if result.should_stop:
            return result

        # Check stop strings
        if tokenizer and self.stop_strings:
            result = self.check_stop_string(generated_text, tokenizer)
            if result.should_stop:
                return result

        return StopResult(should_stop=False)
```

#### 3.3.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-72.1 | EOS token triggers stop | Unit test: EOS token |
| AC-72.2 | Stop string triggers stop | Unit test: stop string in text |
| AC-72.3 | Max tokens enforced | Unit test: count reaches max |
| AC-72.4 | Clean termination | Integration test: no errors on stop |
| AC-72.5 | Stop reason reported | Unit test: reason field populated |

---

## 4. Dependencies Analysis

### 4.1 Week 1-2 Dependencies

```
Week 1-2 Components Used by Week 3:

┌─────────────────────┐
│   PagedKVCache      │ ◄── Used by KVCacheManager
│   (Task #63)        │
└─────────┬───────────┘
          │
┌─────────────────────┐
│   SequenceState     │ ◄── Used for sequence tracking
│   (Task #63)        │
└─────────┬───────────┘
          │
┌─────────────────────┐
│   GenerationConfig  │ ◄── Used for stop conditions
│   (Task #66)        │
└─────────┬───────────┘
          │
┌─────────────────────┐
│   Llama32Config     │ ◄── Used for model params
│   (Task #68)        │
└─────────┬───────────┘
          │
┌─────────────────────┐
│   LlamaWeights      │ ◄── Used for forward pass
│   (Task #69)        │
└─────────────────────┘
```

### 4.2 External Dependencies

| Dependency | Version | Purpose | Installation |
|------------|---------|---------|--------------|
| `numpy` | Latest | Array operations | `pip install numpy` |
| `tokenizers` | Latest | Token encoding/decoding | `pip install tokenizers` |

---

## 5. File Creation Summary

### 5.1 Python Source Files

| File | Type | Lines (est.) |
|------|------|--------------|
| `iron/generation/__init__.py` | Package | 30 |
| `iron/generation/loop.py` | Source | 350 |
| `iron/generation/sampling.py` | Source | 150 |
| `iron/generation/kv_manager.py` | Source | 250 |
| `iron/generation/stop_conditions.py` | Source | 150 |

**Total Python Source Lines:** ~930

### 5.2 Test Files

| File | Type | Lines (est.) | Tests |
|------|------|--------------|-------|
| `iron/generation/test_loop.py` | Test | 200 | 20+ |
| `iron/generation/test_sampling.py` | Test | 150 | 15+ |
| `iron/generation/test_kv_manager.py` | Test | 200 | 15+ |
| `iron/generation/test_stop_conditions.py` | Test | 150 | 10+ |

**Total Test Lines:** ~700 (60+ tests)

---

## 6. Testing Strategy

### 6.1 Unit Tests

**Generation Loop Tests:**
```python
# iron/generation/test_loop.py

def test_prefill_forward():
    """Test prompt processing."""
    pass

def test_decode_single_token():
    """Test single token forward pass."""
    pass

def test_sampling_temperature():
    """Test temperature affects sampling."""
    pass

def test_sampling_top_k():
    """Test top_k filtering."""
    pass

def test_sampling_top_p():
    """Test top_p filtering."""
    pass

def test_generate_yields_tokens():
    """Test generation yields tokens."""
    pass
```

**KV Manager Tests:**
```python
# iron/generation/test_kv_manager.py

def test_kv_write_read():
    """Test KV write and read."""
    pass

def test_block_allocation():
    """Test block allocation."""
    pass

def test_sequence_tracking():
    """Test sequence position tracking."""
    pass

def test_multiple_sequences():
    """Test concurrent sequences."""
    pass

def test_block_release():
    """Test block release on sequence end."""
    pass
```

**Stop Condition Tests:**
```python
# iron/generation/test_stop_conditions.py

def test_eos_detection():
    """Test EOS token detection."""
    pass

def test_stop_string_detection():
    """Test stop string detection."""
    pass

def test_max_tokens_enforcement():
    """Test max token limit."""
    pass

def test_clean_termination():
    """Test clean termination."""
    pass
```

### 6.2 Integration Tests

| Test | Components | Purpose |
|------|------------|---------|
| End-to-end generation | All components | Generate 10+ tokens |
| KV cache persistence | Loop + KV Manager | Context retention |
| Multi-sequence generation | KV Manager | Concurrent sequences |
| Stop condition workflow | Loop + Stop Conditions | Proper termination |

---

## 7. Quality Gates

### 7.1 Code Quality

| Gate | Requirement | Verification |
|------|-------------|--------------|
| Type hints | All public APIs typed | `mypy --strict iron/generation/` |
| Documentation | Docstrings for all classes | `pydocstyle iron/generation/` |
| Error handling | Graceful failures | Code review |
| Logging | Appropriate log levels | Code review |

### 7.2 Test Coverage

| Metric | Target | Verification |
|--------|--------|--------------|
| Line coverage | >90% | `pytest --cov` |
| Branch coverage | >85% | `pytest --cov` |
| All acceptance criteria | 100% verified | Manual checklist |
| Test count | 50+ | pytest --collect-only |

### 7.3 Performance

| Component | Metric | Target | Verification |
|-----------|--------|--------|--------------|
| Prefill | Time per token | <10ms avg | Profile |
| Decode | Time per token | <50ms | Profile |
| KV cache | Write/read latency | <1ms | Profile |
| Sampling | Time per sample | <1ms | Profile |

---

## 8. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| R1: KV cache memory layout wrong | Medium | High | Unit tests for write/read |
| R2: Sequence tracking errors | Medium | High | Position validation |
| R3: EOS not detected | Low | High | Multiple EOS token support |
| R4: Stop string false positives | Low | Medium | Full token boundary check |
| R5: Memory leak in sequences | Medium | High | Block release tracking |

---

## 9. Handoff Package for Senior Developer

### 9.1 Implementation Checklist

**For Senior Developer executing Week 3 tasks:**

- [ ] Read this specification thoroughly
- [ ] Review Week 1-2 components (KVCache, GenerationConfig, Llama32Config)
- [ ] Create all files listed in Section 5
- [ ] Implement classes per specifications in Section 3
- [ ] Write unit tests per Section 6
- [ ] Verify all acceptance criteria are met
- [ ] Run mypy for type checking
- [ ] Document any deviations from specification

### 9.2 Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Iterator-based generation | Streaming output, low latency |
| Separate sampling module | Reusability, testability |
| KV cache manager abstraction | Clean separation of concerns |
| Stop condition composition | Flexible, extensible design |

### 9.3 Points of Contact

| Role | Responsibility |
|------|----------------|
| Dr. Sarah Kim | Technical specifications, requirements |
| Senior Developer | Implementation, testing |
| Quality Reviewer | Code review, acceptance verification |

---

## 10. Next Steps After Week 3

Upon successful completion of Week 3:

### Week 4: API Integration
- Implement OpenAI-compatible `/v1/chat/completions` endpoint
- Add streaming support (SSE)
- Enhance tokenizer with robust fallback

### Week 5: Testing
- Comprehensive unit tests for all components
- Integration tests for end-to-end generation
- Load tests for concurrent requests

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
*SPDX-License-Identifier: Apache-2.0*
