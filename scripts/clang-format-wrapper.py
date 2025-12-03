#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List


def find_cpp_files(root_dir: str = ".") -> List[str]:
    """Find all C/C++ files in the given directory."""
    extensions = ["*.c", "*.cpp", "*.h", "*.hpp", "*.cc", "*.cxx", "*.C", "*.H"]
    files = []

    # Directories to ignore
    ignore_dirs = {
        "build",
        "Build",
        "BUILD",
        ".git",
        ".svn",
        "node_modules",
        "__pycache__",
        ".pytest_cache",
        "third_party",
        "3rdparty",
        "external",
        "vendor",
        "deps",
        "ironenv",
        "venv",
        ".venv",
    }

    root_path = Path(root_dir)
    for ext in extensions:
        for file_path in root_path.rglob(ext):
            # Check if any parent directory is in the ignore list
            if not any(part in ignore_dirs for part in file_path.parts):
                files.append(file_path)

    return [str(f) for f in files]


def run_clang_format_diff(files: List[str]) -> str:
    """Run clang-format and return the diff output."""
    if not files:
        return ""

    diff_output = ""
    for file in files:
        try:
            # Get formatted output
            result = subprocess.run(
                ["clang-format", file], capture_output=True, text=True, check=True
            )
            formatted_content = result.stdout

            # Read original file
            with open(file, "r", encoding="utf-8") as f:
                original_content = f.read()

            # Generate diff if there are differences
            if formatted_content != original_content:
                diff_result = subprocess.run(
                    ["diff", "-u", file, "-"],
                    input=formatted_content,
                    capture_output=True,
                    text=True,
                )
                if diff_result.stdout:
                    diff_output += diff_result.stdout + "\n"

        except subprocess.CalledProcessError as e:
            print(f"Error running clang-format on {file}: {e}", file=sys.stderr)
            sys.exit(1)
        except FileNotFoundError:
            print(
                "Error: clang-format not found. Please install clang-format.",
                file=sys.stderr,
            )
            sys.exit(1)

    return diff_output


def check_formatting(files: List[str]) -> bool:
    """Check if all files are properly formatted. Returns True if all files are formatted."""
    if not files:
        return True

    all_formatted = True
    unformatted_files = []

    for file in files:
        try:
            # Get formatted output
            result = subprocess.run(
                ["clang-format", file], capture_output=True, text=True, check=True
            )
            formatted_content = result.stdout

            # Read original file
            with open(file, "r", encoding="utf-8") as f:
                original_content = f.read()

            # Check if formatting would change the file
            if formatted_content != original_content:
                all_formatted = False
                unformatted_files.append(file)

        except subprocess.CalledProcessError as e:
            print(f"Error running clang-format on {file}: {e}", file=sys.stderr)
            sys.exit(1)
        except FileNotFoundError:
            print(
                "Error: clang-format not found. Please install clang-format.",
                file=sys.stderr,
            )
            sys.exit(1)

    if not all_formatted:
        print("❌ The following files are not properly formatted:", file=sys.stderr)
        for file in unformatted_files:
            print(f"  - {file}", file=sys.stderr)
        print("\nRun the following command to fix formatting:", file=sys.stderr)
        print("python scripts/format_cpp.py --fix", file=sys.stderr)
        return False

    print("✅ All C/C++ files are properly formatted")
    return True


def format_files(files: List[str]) -> None:
    """Format files in-place using clang-format."""
    if not files:
        print("No C/C++ files found to format")
        return

    for file in files:
        try:
            subprocess.run(["clang-format", "-i", file], check=True)
            print(f"Formatted: {file}")
        except subprocess.CalledProcessError as e:
            print(f"Error formatting {file}: {e}", file=sys.stderr)
            sys.exit(1)
        except FileNotFoundError:
            print(
                "Error: clang-format not found. Please install clang-format.",
                file=sys.stderr,
            )
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Format C/C++ files using clang-format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/format_cpp.py --diff          # Show formatting differences
  python scripts/format_cpp.py --check         # Check if files are formatted (exit 1 if not)
  python scripts/format_cpp.py --fix           # Format files in-place
  python scripts/format_cpp.py --path src/     # Only format files in src/ directory
        """,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--diff",
        action="store_true",
        help="Show formatting differences without modifying files",
    )
    group.add_argument(
        "--check",
        action="store_true",
        help="Check if files are formatted correctly (exit 1 if not)",
    )
    group.add_argument("--fix", action="store_true", help="Format files in-place")

    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Path to search for C/C++ files (default: current directory)",
    )

    args = parser.parse_args()

    # Find all C/C++ files
    cpp_files = find_cpp_files(args.path)

    if not cpp_files:
        print(f"No C/C++ files found in {args.path}")
        return

    print(f"Found {len(cpp_files)} C/C++ file(s)")

    if args.diff:
        diff_output = run_clang_format_diff(cpp_files)
        if diff_output:
            print("Formatting differences found:")
            print(diff_output)
        else:
            print("No formatting differences found")

    elif args.check:
        if not check_formatting(cpp_files):
            sys.exit(1)

    elif args.fix:
        format_files(cpp_files)
        print(f"Formatted {len(cpp_files)} file(s)")


if __name__ == "__main__":
    main()
