#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Application test discovery script.

Discovers test.py files in application subdirectories and generates test index.
"""

import sys
import importlib.util
from pathlib import Path


def load_test_module(test_path):
    """Load a test.py module and return it."""
    spec = importlib.util.spec_from_file_location("test_module", test_path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Warning: Failed to load {test_path}: {e}", file=sys.stderr)
        return None


def discover_application_tests(applications_dir, output_dir):
    """Discover test.py files in application subdirectories."""
    applications_dir = Path(applications_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    tests = []
    test_names = []
    test_paths = []

    # Find all subdirectories with test.py files
    for subdir in sorted(applications_dir.iterdir()):
        if not subdir.is_dir():
            continue

        test_file = subdir / "test.py"
        if not test_file.exists():
            continue

        # Use directory name as test name
        test_name = subdir.name

        # Load the test module to extract its values
        module = load_test_module(test_file)
        if module is None:
            continue

        # Extract run command, checks, and metrics from the module
        run_command = getattr(module, "run", None)
        checks = getattr(module, "checks", [])
        metrics = getattr(module, "metrics", [])

        if run_command is None:
            print(f"Warning: No 'run' command found in {test_file}", file=sys.stderr)
            continue

        # Create output directory for this test
        test_output_dir = output_dir / test_name
        test_output_dir.mkdir(parents=True, exist_ok=True)

        # Generate test file content with evaluated values
        output_test_file = test_output_dir / f"{test_name}.py"
        content = f"""run = {run_command!r}
checks = {checks!r}
metrics = {metrics!r}
"""
        output_test_file.write_text(content)

        tests.append(test_name)
        test_names.append(test_name)
        test_paths.append(str(test_output_dir))

        print(f"Discovered application test: {test_name}")

    # Generate ci_tests.py index file
    if tests:
        ci_tests_file = output_dir / "ci_tests.py"
        ci_tests_content = f"""tests = {test_names!r}
paths = {test_paths!r}
"""
        ci_tests_file.write_text(ci_tests_content)
        print(f"Created index file: {ci_tests_file}")

    return tests


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Discover application tests")
    parser.add_argument(
        "--applications-dir",
        default=str(Path(__file__).parent),
        help="Path to applications directory (default: parent of this script)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default=".",
        help="Output directory for test files (default: current working directory)",
    )

    args = parser.parse_args()

    tests = discover_application_tests(args.applications_dir, args.output_dir)

    print(f"\nGenerated {len(tests)} application test(s)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
