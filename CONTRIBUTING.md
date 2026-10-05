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