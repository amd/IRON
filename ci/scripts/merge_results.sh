#!/usr/bin/env bash
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# merge_results.sh RUN SUITE_DIR: merge a run's results (RUN/latest.csv and
# RUN/readme.md, as format_results writes them) into SUITE_DIR, a suite's
# directory on the ci branch: all.csv keeps the runs merge_all.py --prune
# keeps, trends.md compares this run with the one before.
set -euo pipefail
scripts=$(dirname "$0")
run=$1 dir=$2
mkdir -p "$dir"
cp "$run/latest.csv" "$run/readme.md" "$dir/"
touch "$dir/all.csv"
cp "$dir/all.csv" "$dir/last_two.csv"
"$scripts/merge_all.py" --all "$dir/all.csv" --latest "$dir/latest.csv" --prune
"$scripts/merge_all.py" --all "$dir/last_two.csv" --latest "$dir/latest.csv" --limit 2
"$scripts/pretty_trends.py" "$dir/last_two.csv" -o "$dir/trends.md"
rm "$dir/last_two.csv"
