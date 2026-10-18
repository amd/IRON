<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Contributing to IRON

We actively welcome community involvement in this project! If you have a question or a request, please open an issue. Before contributing to IRON, please read the guidelines below.

## Overview

### Pull Request Workflow
- **Target Branch**: Submit PRs to the `devel` branch
- **CI Requirements**: All CI tests must pass, including linting and formatting checks
- **Draft PRs**: Open draft PRs as soon as possible with "DRAFT:" prefix to get early feedback
- **Refactors**: Use "REFACTOR:" prefix for refactoring PRs to clearly indicate the nature of changes
- **PR Template**: Use the provided PR template with:
  - Short summary of changes
  - **Added**: New features or functionality
  - **Changed**: Modifications to existing behavior
  - **Removed**: Deprecated or deleted functionality
- **Changelog**: A PR that changes the public API adds an entry under Unreleased in [CHANGELOG.md](CHANGELOG.md)
- **Issue References**: Always reference related Issues in your PR description using `#issue-number`

### Issue Management
- Use the provided Issue template when creating new issues
- Provide clear reproduction steps for bugs
- Include relevant system information and error messages
- Tag issues appropriately (bug, enhancement, documentation, etc.)

## Add a model

A model is a package under `iron/applications/<name>/` over `iron.lm`. Most
Hugging Face decoders need a config and a model class; see
`iron/applications/qwen3/model.py`, which is the whole of Qwen3.

1. **Config.** Subclass `DecoderConfig`. Its fields are read from the
   checkpoint's `config.json` by name, or at `metadata={"json": ...}`;
   `not_json(default)` marks an IRON choice. Override
   `attention(i)` or `layer(i)` to pick the parts that differ from Llama's
   (`Norm`, `Attention`, `MLP`, `DecoderLayer` in `iron/lm/blocks.py`):

   ```python
   def attention(self, i):
       return dataclasses.replace(super().attention(i), qk_norm=True)
   ```

2. **Model.** Subclass `CausalLM` (or `Encoder`, `Tower`, `EncoderDecoder`),
   naming `config` and pointing `profile` at a `profiles/` directory (and
   naming `bos` where `config.json` has no `bos_token_id`). A layer reads the
   checkpoint's own module names (`input_layernorm`, `self_attn.q_proj`,
   ...). When the checkpoint names them differently, override
   `sanitize(w)` to map one layer's modules to those names at load time
   (`iron/applications/lfm2/model.py`); a fused projection is cut into
   views, not copied (`iron/applications/phi3/model.py`). Write the model
   body with `iron.functional as F` and handle arithmetic (`x + y`), the
   way you would with `torch.nn.functional`. End the file with
   `lm.main(Qwen3)` on your class, its command line, and export it from the
   package's `__init__.py` with `__getattr__ = exports(__name__, __all__)`
   (`iron.lm.cli`).

3. **Tests.** A decoder's device-free test subclasses `Decoder`
   (`iron/tests/common/llama_reference.py`) with the model, a toy config
   and transformers' model type: it draws random weights
   (`Checkpoint.tree("random", seed)`) and compares the model run on the
   host (`OnHost`) with transformers' logits on the same weights, recorded
   once into `goldens/` beside the test by the `golden` fixture. See
   `tests/applications/qwen3/reference/test.py`. Record with
   `pytest <test> --record-goldens -p no:xdist` (transformers and torch
   are needed only then) and commit the `.npz`. The device test goes in
   `tests/applications/<name>/test.py` and uses `iron.lm.testing`'s
   checks; `check_accuracy` judges the real checkpoint against the
   `golden.npz` recorded beside it. The host run uses each operator's
   reference, which does not model aie2p's bfp16 rounding in flm.ProjectionGEMM, so
   only the device test measures that error.

A Llama-shaped decoder (Mistral v0.3, Qwen, SmolLM) needs only these
steps. A sliding window over the caches, Gemma's `(1 + w)` norms and
sandwich norms, per-layer RoPE tables, or post-norm layers (OLMo 2) need
new code in `iron/lm/` first; `iron/applications/embedding_gemma2/blocks.py`
shows a sandwich-normed layer.

## Add an operator and kernel

An operator is a class under `iron/operators/`; its compute kernel lives in
mlir-aie. An elementwise operator is a few lines (`iron/operators/relu.py`):

```python
class ReLU(UnaryElementwise):
    test = Testing(Sweep(), draw=lambda op: dict(centered=(op.x,)))

    class Array(UnaryElementwise.Array):
        def kernel(self):
            return eltwise.relu_sized(self.tile_size)
```

1. **Kernel.** If no factory in mlir-aie's `aie.iron.kernels` computes
   it, add the C++ under `aie_kernels/<family>/` in mlir-aie (architecture
   specifics in `*_aie2.h` / `*_aie2p.h`) and a factory beside the others
   in `python/iron/kernels/<family>.py`. The factory's `KernelContract`
   carries the numpy reference and the tolerance, so the operator needs
   neither (see `relu_sized` in `eltwise.py`), and it checks the vector
   alignment its tile needs. IRON sees the factory once `requirements.txt`
   pins an mlir-aie wheel that has it.
2. **Operator.** Subclass the closest family (`UnaryElementwise`,
   `BinaryElementwise`, ... in `iron/common/elementwise.py`) and return the
   factory from `Array.kernel()`. A new data layout needs its own
   `Operator` with `In`/`Out` operands and `Array.build()`; `gemm.py` and
   `mha.py` are the worked examples.
3. **Test.** Declare `test = Testing(...)` on the class;
   `iron/tests/operators/catalog.py` runs every operator's cases. Every
   operator needs a `bench=True` case and a `lower=True` case per layout
   (`Sweep` adds the first, and the second with `lower=True`); a shape it
   must refuse goes in `iron/tests/operators/rejected_shapes.py`.
4. **Register.** Add the name to `_OPERATOR_MODULES` in
   `iron/operators/__init__.py` and to `__init__.pyi`.
5. **Use it.** Inside a graph's `body()`, `ReLU.step(x)` records a step.
   If models will call it, add a function to `iron/functional.py`.

The rules (operand declarations, tunables, shipped binaries, the hooks an
operator may override) are "Adding an operator" in [AGENTS.md](AGENTS.md).

## Style Guide

### Python Code Style
We use **Black** for Python code formatting with default settings:
- Line length: 88 characters (Black default)
- String quotes: Double quotes preferred
- Trailing commas: Added automatically by Black

**Formatting Commands:**
```bash
# Check formatting
black --check .

# Auto-format all Python files
black .
```

**Best Practices:**
- Use type annotations for function parameters and return values
- Follow PEP 8 naming conventions
- Write descriptive docstrings for public functions and classes
- Use meaningful variable and function names

### Git hook
`scripts/hooks/pre-push` runs CI's lint checks (reuse, black, clang-format) before a push:
```bash
cp scripts/hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```
`git push --no-verify` skips it.

### C++ Code Style
The few C++ files here follow `.clang-format`; `python scripts/clang-format-wrapper.py --fix` applies it.

## Licensing

### License Headers
All source files must include the Apache 2.0 license header. We use the **REUSE** tool to ensure compliance:

**Required Headers:** two SPDX lines, as `reuse annotate` below writes them
(`//` in place of `#` for C++):
```python
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
```

**License Compliance Check:**
```bash
# Check license compliance
reuse lint

# Automatically annotate new files without licenses
reuse annotate --template ApacheAMD --copyright-prefix spdx-string-c --copyright "Advanced Micro Devices, Inc. All rights reserved." --license="Apache-2.0" --recursive --skip-unrecognised ./
```

## Additional Resources

- [Apache License 2.0](LICENSE)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Project Credits](CREDITS.md)
- [REUSE Specification](https://reuse.software/)