#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Assemble the pull request comment from the per-suite trend reports.

Takes the artifact tree the CI workflows produce, one ``{arch}/{suite}``
directory per job, and emits the markdown body to post. A run that moves no
benchmark posts a one-line comment.
"""

import argparse
import os

# The posting step matches this to update its own comment.
MARKER = "<!-- iron-ci-aggregate -->"

SUITES = [
    ("krackan/small", "Krackan - Operators"),
    ("krackan/examples", "Krackan - Applications"),
    ("phoenix/small", "Phoenix - Operators"),
    ("phoenix/examples", "Phoenix - Applications"),
]


def read_trends(path):
    """Return a suite's trend report without its title, or '' if it says nothing."""
    try:
        with open(path) as f:
            text = f.read()
    except OSError:
        return ""
    body = "\n".join(
        line for line in text.splitlines() if not line.startswith("# ")
    ).strip()
    # pretty_trends.py opens its report with this when it found nothing.
    if body.startswith("No benchmark moved"):
        return ""
    return body


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-root", default=".")
    parser.add_argument("--commit", default="")
    parser.add_argument("--date", default="")
    parser.add_argument("--commit-url", default="")
    parser.add_argument("--pages-url", default="")
    parser.add_argument("-o", "--output", default="comment.md")
    args = parser.parse_args()

    commit = (
        f"[`{args.commit}`]({args.commit_url})"
        if args.commit_url
        else f"`{args.commit}`"
    )
    lines = [MARKER, "## CI performance trends", "", f"{commit} ({args.date})", ""]

    sections = []
    for directory, label in SUITES:
        body = read_trends(os.path.join(args.results_root, directory, "trends.md"))
        if body:
            sections += [
                f"<details open>",
                f"<summary><b>{label}</b></summary>",
                "",
                body,
                "",
                "</details>",
                "",
            ]

    if sections:
        lines += sections
    else:
        lines += ["No benchmark moved past the reporting threshold.", ""]

    if args.pages_url:
        lines += [f"[Full benchmark history]({args.pages_url})", ""]

    with open(args.output, "w") as f:
        f.write("\n".join(lines))
    print(f"Written: {args.output}")


if __name__ == "__main__":
    main()
