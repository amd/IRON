#!/bin/bash

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

SCOPE="repo"

RUNNER_VERSION="2.329.0"               # check for latest: https://github.com/actions/runner/releases
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

get_registration_token() {
  if [ "${SCOPE}" = "repo" ]; then
    URL="https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/actions/runners/registration-token"
  elif [ "${SCOPE}" = "org" ]; then
    URL="https://api.github.com/orgs/${GITHUB_OWNER}/actions/runners/registration-token"
  else
    echo "Unknown scope: ${SCOPE}"
    exit 1
  fi

  TOKEN=$(curl -sX POST -H "Authorization: token ${GITHUB_PAT}" \
    -H "Accept: application/vnd.github+json" "${URL}" \
    | jq -r .token)

  if [ "${TOKEN}" = "null" ]; then
    echo "Failed to get runner registration token"
    exit 1
  fi
  echo "${TOKEN}"
}

configure_runner() {
    local token="$1"
    cd "${RUNNER_DIR}"
    ./config.sh \
      --url "https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}" \
      --token "${token}" \
      --name "${RUNNER_NAME}" \
      --work _work \
      --unattended \
      --ephemeral \
      --labels chroot
}

install_runner
if ! token="$(get_registration_token)"; then
  echo "Failed to get runner registration token" >&2
  exit 1
fi
export token
echo "Got runner token: ${token}"
configure_runner "${token}"

echo "Configured. Running actions runner..."
cd "${RUNNER_DIR}"
./run.sh
