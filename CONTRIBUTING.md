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
- **Issue References**: Always reference related Issues in your PR description using `#issue-number`

### Issue Management
- Use the provided Issue template when creating new issues
- Provide clear reproduction steps for bugs
- Include relevant system information and error messages
- Tag issues appropriately (bug, enhancement, documentation, etc.)

## Add a model

A model is a package under `iron/applications/<name>/` over `iron.lm`. Most
Hugging Face decoders need a config, a model class and a runner; see
`iron/applications/qwen3/model.py`, which is the whole of Qwen3.

1. **Config.** Subclass `DecoderConfig`. Its fields are read from the
   checkpoint's `config.json` by `metadata={"json": ...}`. Override
   `attention(i)` or `layer(i)` to pick the parts that differ from Llama's
   (`Norm`, `Attention`, `MLP`, `DecoderLayer` in `iron/lm/blocks.py`):

   ```python
   def attention(self, i):
       return dataclasses.replace(super().attention(i), qk_norm=True)
   ```

2. **Model.** Subclass `CausalLM` (or `Encoder`, `Tower`, `EncoderDecoder`)
   and point `profile` at a `profiles/` directory. A layer reads the
   checkpoint's own module names (`input_layernorm`, `self_attn.q_proj`,
   ...). When the checkpoint names them differently, override
   `sanitize(w)` to map one layer's modules to those names at load time
   (`iron/applications/lfm2/model.py`); a fused projection is cut into
   views, not copied (`iron/applications/phi3/model.py`). Write the model
   body with `iron.functional as F` and handle arithmetic (`x + y`), the
   way you would with `torch.nn.functional`.

3. **Runner.** Subclass `iron.lm.Runner`, naming `config`, `model` and
   `bos`, and end the file with `lm.main(Runner, "...")`.

4. **Tests.** A device-free test builds a toy config, draws random weights
   (`Checkpoint.tree("random", seed)`) and compares the model run on the
   host (`class Host(OnHost, MyModel)`) with transformers' logits on the
   same weights. Those logits are recorded once into `goldens/` beside the
   test by the `golden` fixture:

   ```python
   reference = golden("toy", lambda: HuggingFace.build("qwen3", config, weights))
   ```

   Record with `pytest <test> --record-goldens -p no:xdist` (transformers
   and torch are needed only then) and commit the `.npz`. See
   `tests/applications/phi3/reference/test.py`. The device test goes in
   `tests/applications/<name>/test.py` and uses `iron.lm.testing`'s
   checks; `check_accuracy` judges the real checkpoint against the
   `golden.npz` recorded beside it.

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
   it, add the C++ under `aie_kernels/<family>/` in mlir-aie and a factory
   beside the others in `python/iron/kernels/<family>.py`. The factory's
   `KernelContract` carries the numpy reference and the tolerance, so the
   operator needs neither (see `relu_sized` in `eltwise.py`).
2. **Operator.** Subclass the closest family (`UnaryElementwise`,
   `BinaryElementwise`, ... in `iron/common/elementwise.py`) and return the
   factory from `Array.kernel()`. A new data layout needs its own
   `Operator` with `In`/`Out` operands and `Array.build()`; `gemm.py` and
   `mha.py` are the worked examples.
3. **Test.** Declare `test = Testing(...)` on the class;
   `iron/tests/operators/catalog.py` runs every operator's cases.
4. **Register.** Add the name to `_OPERATOR_MODULES` in
   `iron/operators/__init__.py` and to `__init__.pyi`.
5. **Use it.** Inside a graph's `body()`, `ReLU.step(x)` records a step.
   If models will call it, add a function to `iron/functional.py`.

The full reference (operand declarations, tunables, shipped binaries,
the hooks an operator may override) is "Adding a New Operator" in
[AGENTS.md](AGENTS.md).

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

### C++ Code Style
We use **clang-format** with a custom configuration based on LLVM style:

**Style Rules:**
- **Line length**: 120 characters maximum
- **Indentation**: 4 spaces (no tabs)
- **Braces**: Linux style (opening brace on new line for functions/classes)
- **Spacing**: Space before parentheses in control statements
- **Include sorting**: Automatic sorting and grouping of includes

**Formatting Commands:**
```bash
# Check C++ formatting
python scripts/clang-format-wrapper.py --check

# Show formatting differences
python scripts/clang-format-wrapper.py --diff

# Auto-format all C++ files
python scripts/clang-format-wrapper.py --fix

# Format specific directory only
python scripts/clang-format-wrapper.py --fix --path src/
```

## Licensing

### License Headers
All source files must include the Apache 2.0 license header. We use the **REUSE** tool to ensure compliance:

**Required Headers:**
```cpp
// For C++ files
// Licensed under the Apache License, Version 2.0 (the License); you may
// not use this file except in compliance with the License.
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an AS IS BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// SPDX-FileCopyrightText: Copyright (c) 2025, Advanced Micro Devices, Inc. All rights reserved.
//
// SPDX-License-Identifier: Apache-2.0
```

```python
# For Python files
# Licensed under the Apache License, Version 2.0 (the License); you may
# not use this file except in compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-FileCopyrightText: Copyright (c) 2025, Advanced Micro Devices, Inc. All rights reserved.
#
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