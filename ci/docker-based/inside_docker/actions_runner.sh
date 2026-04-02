#!/bin/bash

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

SCOPE="repo"

RUNNER_VERSION="2.333.1"               # check for latest: https://github.com/actions/runner/releases
RUNNER_NAME="docker-runner-$(cat /etc/hostname)"
RUNNER_DIR="/workspace/runner"

install_runner() {
  mkdir -p "${RUNNER_DIR}"
  cd "${RUNNER_DIR}"
  curl -L \
    "https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz" \
    -o runner.tar.gz
  tar -xzf runner.tar.gz
  rm runner.tar.gz
}

configure_runner() {
    local token="$1"
    local labels="${RUNNER_LABELS:-docker}"
    cd "${RUNNER_DIR}"
    ./config.sh \
      --url "https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}" \
      --token "${token}" \
      --name "${RUNNER_NAME}" \
      --work _work \
      --unattended \
      --ephemeral \
      --labels "${labels}"
}

install_runner

configure_runner "${GITHUB_RUNNER_TOKEN}"

echo "Configured. Running actions runner..."
cd "${RUNNER_DIR}"
./run.sh
