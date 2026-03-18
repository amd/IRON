# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Week 2 Quality Review - Manual Test Execution"""

import sys

sys.path.insert(0, ".")

from iron.models.llama32.config import Llama32Config
from iron.models.llama32.weights import LlamaWeights, TransformerWeights
from iron.models.llama32.loader import WeightLoader, WeightInfo
from iron.models.registry import ModelRegistry, ModelSpec
import tempfile
from pathlib import Path
import json
import numpy as np

print("=" * 70)
print("WEEK 2 QUALITY REVIEW - MANUAL TEST EXECUTION")
print("=" * 70)
print()

# Track test results
results = {"passed": 0, "failed": 0, "skipped": 0}
test_details = []

# ===== TEST CONFIG =====
print("[TESTING] Llama32Config...")

# Test 1: Default config
try:
    config = Llama32Config()
    assert config.vocab_size == 128256
    assert config.hidden_size == 2048
    assert config.num_hidden_layers == 16
    results["passed"] += 1
    test_details.append(("Config defaults", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Config defaults", f"FAIL: {e}"))

# Test 2: Validation - invalid vocab
try:
    try:
        Llama32Config(vocab_size=-1)
        results["failed"] += 1
        test_details.append(("Config validation vocab_size", "FAIL: Should raise"))
    except ValueError:
        results["passed"] += 1
        test_details.append(("Config validation vocab_size", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Config validation vocab_size", f"FAIL: {e}"))

# Test 3: GQA compatibility
try:
    try:
        Llama32Config(num_attention_heads=32, num_key_value_heads=7)
        results["failed"] += 1
        test_details.append(("Config GQA validation", "FAIL: Should raise"))
    except ValueError:
        results["passed"] += 1
        test_details.append(("Config GQA validation", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Config GQA validation", f"FAIL: {e}"))

# Test 4: JSON serialization
try:
    with tempfile.TemporaryDirectory() as tmpdir:
        config = Llama32Config()
        json_path = Path(tmpdir) / "config.json"
        config.to_json(json_path)
        reloaded = Llama32Config.from_json(json_path)
        assert reloaded.vocab_size == config.vocab_size
    results["passed"] += 1
    test_details.append(("Config JSON roundtrip", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Config JSON roundtrip", f"FAIL: {e}"))

# Test 5: Memory estimation
try:
    config = Llama32Config()
    mem = config.estimate_weight_memory("float32")
    assert mem > 0
    results["passed"] += 1
    test_details.append(("Config memory estimation", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Config memory estimation", f"FAIL: {e}"))

# Test 6: KV cache calculation
try:
    config = Llama32Config()
    kv_bytes = config.kv_cache_size_per_token
    expected = 2 * 16 * 8 * 64 * 4  # 65536
    assert kv_bytes == expected
    results["passed"] += 1
    test_details.append(("Config KV cache calc", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Config KV cache calc", f"FAIL: {e}"))

print(f'  Config tests: {results["passed"]} passed')
print()

# ===== TEST WEIGHTS =====
print("[TESTING] LlamaWeights and TransformerWeights...")
weights_passed = results["passed"]

# Test 7: TransformerWeights creation
try:
    layer = TransformerWeights(
        wq=np.random.randn(2048, 2048).astype(np.float32),
        wk=np.random.randn(2048, 512).astype(np.float32),
        wv=np.random.randn(2048, 512).astype(np.float32),
        wo=np.random.randn(2048, 2048).astype(np.float32),
        w1=np.random.randn(2048, 8192).astype(np.float32),
        w2=np.random.randn(8192, 2048).astype(np.float32),
        w3=np.random.randn(2048, 8192).astype(np.float32),
        attn_norm=np.random.randn(2048).astype(np.float32),
        ffn_norm=np.random.randn(2048).astype(np.float32),
    )
    assert layer.total_params > 0
    assert layer.memory_bytes > 0
    results["passed"] += 1
    test_details.append(("TransformerWeights creation", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("TransformerWeights creation", f"FAIL: {e}"))

# Test 8: LlamaWeights structure
try:
    layers = [
        TransformerWeights(
            wq=np.random.randn(100, 128).astype(np.float32),
            wk=np.random.randn(100, 64).astype(np.float32),
            wv=np.random.randn(100, 64).astype(np.float32),
            wo=np.random.randn(128, 100).astype(np.float32),
            w1=np.random.randn(100, 256).astype(np.float32),
            w2=np.random.randn(256, 100).astype(np.float32),
            w3=np.random.randn(100, 256).astype(np.float32),
            attn_norm=np.random.randn(100).astype(np.float32),
            ffn_norm=np.random.randn(100).astype(np.float32),
        )
        for _ in range(2)
    ]

    weights = LlamaWeights(
        token_embd=np.random.randn(1000, 128).astype(np.float32),
        layers=layers,
        output_norm=np.random.randn(128).astype(np.float32),
        output=None,
        vocab_size=1000,
        hidden_size=128,
        num_layers=2,
    )
    assert weights.total_params > 0
    assert weights.is_output_tied == True
    results["passed"] += 1
    test_details.append(("LlamaWeights structure", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("LlamaWeights structure", f"FAIL: {e}"))

print(f'  Weights tests: {results["passed"] - weights_passed} passed')
print()

# ===== TEST REGISTRY =====
print("[TESTING] ModelRegistry...")
registry_passed = results["passed"]

# Test 9: Registry has llama
try:
    assert ModelRegistry.is_supported("llama") == True
    results["passed"] += 1
    test_details.append(("Registry llama supported", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Registry llama supported", f"FAIL: {e}"))

# Test 10: Get config class
try:
    config_class = ModelRegistry.get_config_class("llama")
    assert config_class == Llama32Config
    results["passed"] += 1
    test_details.append(("Registry config class", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Registry config class", f"FAIL: {e}"))

print(f'  Registry tests: {results["passed"] - registry_passed} passed')
print()

# ===== TEST LOADER =====
print("[TESTING] WeightLoader...")
loader_passed = results["passed"]

# Test 11: Loader initialization
try:
    with tempfile.TemporaryDirectory() as tmpdir:
        loader = WeightLoader(cache_dir=tmpdir)
        assert loader.cache_dir == Path(tmpdir)
    results["passed"] += 1
    test_details.append(("Loader init with cache", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Loader init with cache", f"FAIL: {e}"))

# Test 12: Loader no cache
try:
    loader = WeightLoader()
    assert loader.cache_dir is None
    results["passed"] += 1
    test_details.append(("Loader init no cache", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Loader init no cache", f"FAIL: {e}"))

# Test 13: WeightInfo
try:
    info = WeightInfo(
        file_path=Path("/test"),
        file_size=1048576,
        num_tensors=100,
        total_tensor_size=900000,
        checksum="abc123",
    )
    assert info.file_size_mb == 1.0
    assert info.safetensors_files == []
    results["passed"] += 1
    test_details.append(("WeightInfo creation", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("WeightInfo creation", f"FAIL: {e}"))

# Test 14: Validate file not found
try:
    loader = WeightLoader()
    try:
        loader.validate_weights(Path("/nonexistent"))
        results["failed"] += 1
        test_details.append(("Loader validate not found", "FAIL: Should raise"))
    except FileNotFoundError:
        results["passed"] += 1
        test_details.append(("Loader validate not found", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Loader validate not found", f"FAIL: {e}"))

# Test 15: Create and validate safetensors
try:
    from safetensors.numpy import save_file

    with tempfile.TemporaryDirectory() as tmpdir:
        model_dir = Path(tmpdir)
        weights = {"test": np.array([1.0, 2.0, 3.0]).astype(np.float32)}
        save_file(weights, model_dir / "model.safetensors")

        loader = WeightLoader()
        info = loader.validate_weights(model_dir)
        assert info.num_tensors == 1
        assert len(info.checksum) == 64  # SHA256 hex length
    results["passed"] += 1
    test_details.append(("Loader validate safetensors", "PASS"))
except ImportError:
    results["skipped"] += 1
    test_details.append(
        ("Loader validate safetensors", "SKIP: safetensors not installed")
    )
except Exception as e:
    results["failed"] += 1
    test_details.append(("Loader validate safetensors", f"FAIL: {e}"))

# Test 16: Load weights
try:
    from safetensors.numpy import save_file

    with tempfile.TemporaryDirectory() as tmpdir:
        model_dir = Path(tmpdir)
        weights = {"embed": np.random.randn(100, 64).astype(np.float32)}
        save_file(weights, model_dir / "model.safetensors")

        loader = WeightLoader()
        loaded = loader.load_weights_mmap(model_dir)
        assert "embed" in loaded
        assert loaded["embed"].shape == (100, 64)
    results["passed"] += 1
    test_details.append(("Loader load_weights_mmap", "PASS"))
except ImportError:
    results["skipped"] += 1
    test_details.append(("Loader load_weights_mmap", "SKIP: safetensors not installed"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Loader load_weights_mmap", f"FAIL: {e}"))

# Test 17: Clear cache
try:
    with tempfile.TemporaryDirectory() as tmpdir:
        loader = WeightLoader(cache_dir=tmpdir)
        cache_file = loader.cache_dir / "test.txt"
        cache_file.write_text("test")
        loader.clear_cache()
        assert not cache_file.exists()
    results["passed"] += 1
    test_details.append(("Loader clear cache", "PASS"))
except Exception as e:
    results["failed"] += 1
    test_details.append(("Loader clear cache", f"FAIL: {e}"))

print(f'  Loader tests: {results["passed"] - loader_passed} passed')
print()

# ===== SUMMARY =====
print("=" * 70)
print("TEST SUMMARY")
print("=" * 70)
print(f'  Passed:  {results["passed"]}')
print(f'  Failed:  {results["failed"]}')
print(f'  Skipped: {results["skipped"]}')
print(f"  Total:   {sum(results.values())}")
print()
print("Test Details:")
for name, status in test_details:
    print(f"  [{status}] {name}")
print()

if results["failed"] == 0:
    print("ALL TESTS PASSED!")
else:
    print(f'WARNING: {results["failed"]} tests failed')
