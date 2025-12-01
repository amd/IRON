#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Test discovery script for operator tests.

This script discovers all operator tests by importing test modules and
extracting their test case definitions, generating a list of tests.
"""

import os
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


def discover_tests(operators_dir, extensive=False):
    operators_dir = Path(operators_dir)
    tests = []

    # Iterate over all subdirectories in operators/
    for subdir in sorted(operators_dir.iterdir()):
        test_file = subdir / "test.py"
        if not subdir.is_dir() or subdir.name == "common" or not test_file.exists():
            continue

        module = load_test_module(test_file)
        if module is None:
            continue

        operator_name = subdir.name

        regular_cases = getattr(module, "regular_test_cases", [])
        extensive_cases = getattr(module, "extensive_test_cases", [])
        test_cases = regular_cases if not extensive else extensive_cases

        for test_name, test_args in test_cases:
            test_command = f"{test_file} {test_args}"
            tests.append((operator_name, test_command, test_name))

    return tests


def generate_test_list(operators_dir, output_dir=None, extensive=False):
    """
    Creates a directory structure where each operator has its own subdirectory, and each test for that operator has its own
    test definition file within that directory. A top-level ci_tests.py index file lists all these tests.

    Args:
        operators_dir: Path to the operators directory
        output_dir: Path to output directory (default: current working directory)
        extensive: If True, include extensive test cases
    """
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    tests = discover_tests(operators_dir, extensive=extensive)

    # Create individual test files
    test_names = []
    test_paths = []

    for operator_name, test_command, test_name in tests:
        # Create subdirectory for this operator
        operator_dir = output_dir / operator_name
        operator_dir.mkdir(parents=True, exist_ok=True)

        # Create test file
        test_file = operator_dir / f"{test_name}.py"

        # Convert test_command to avoid import conflicts:
        test_parts = test_command.split()
        test_script = test_parts[0]
        test_args = " ".join(test_parts[1:]) if len(test_parts) > 1 else ""

        # Wrap command to run from /tmp to avoid sys.path issues
        if test_args:
            wrapped_command = f"cd /tmp && python3 {test_script} {test_args}"
        else:
            wrapped_command = f"cd /tmp && python3 {test_script}"

        # Generate test file content
        content = f"""run = '{wrapped_command}'
checks = [
    'PASS!',
]
metrics = [
    ('Latency', r"Latency \\(us\\): (?P<metric>[\\d\\.]+)"),
    ('Bandwidth', r"Effective Bandwidth: (?P<metric>[\\d\\.e\\+-]+) GB/s"),
]
"""

        with open(test_file, "w") as f:
            f.write(content)

        test_names.append(test_name)
        test_paths.append(str(operator_dir))

    # Generate ci_tests.py index file
    ci_tests_file = output_dir / "ci_tests.py"
    ci_tests_content = f"""tests = {repr(test_names)}
paths = {repr(test_paths)}
"""

    with open(ci_tests_file, "w") as f:
        f.write(ci_tests_content)

    print(f"Generated {len(tests)} test files in {output_dir}")
    print(f"Created index file: {ci_tests_file}")

    return tests


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Discover and list operator tests")
    parser.add_argument(
        "--operators-dir",
        default=str(Path(__file__).parent.parent),
        help="Path to operators directory (default: parent of this script)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        help="Output directory for test files (default: current working directory)",
    )
    parser.add_argument(
        "--extensive", action="store_true", help="Include extensive test cases"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Just list test names (do not generate files)",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Just print the count of tests (do not generate files)",
    )

    args = parser.parse_args()

    tests = discover_tests(args.operators_dir, extensive=args.extensive)

    if args.count:
        print(len(tests))
    elif args.list:
        for operator_name, test_command, test_name in tests:
            print(test_name)
    else:
        generate_test_list(args.operators_dir, args.output_dir, args.extensive)

    return 0


if __name__ == "__main__":
    sys.exit(main())
