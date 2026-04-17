#!/bin/bash

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -x

ARCH="${1}"

# Auto-detect architecture if not specified
if [ -z "${ARCH}" ]; then
    source /opt/xilinx/xrt/setup.sh
    XRT_OUTPUT=$(xrt-smi examine 2>/dev/null)
    if echo "${XRT_OUTPUT}" | grep -qi "phoenix"; then
        ARCH="phoenix"
    elif echo "${XRT_OUTPUT}" | grep -qi "strix"; then
        ARCH="strix"
    elif echo "${XRT_OUTPUT}" | grep -qi "krackan"; then
        ARCH="krackan"
    else
        echo "ERROR: Could not auto-detect architecture from xrt-smi examine output:"
        echo "${XRT_OUTPUT}"
        exit 1
    fi
    echo "Auto-detected architecture: ${ARCH}"
fi

# Ensure lowercase
ARCH=$(echo "${ARCH}" | tr '[:upper:]' '[:lower:]')

IMAGE_NAME="iron-public-dev-github-runner"
GITHUB_OWNER="amd"
GITHUB_REPO="IRON"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GITHUB_PAT=$(cat "${SCRIPT_DIR}/secret_github_token")
SCOPE="repo"

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

while true; do
    DATE=$(printf '%(%Y_%m_%d_%H_%M_%S)T')
    NAME="ci-run-${ARCH}-${DATE}"
    if ! TOKEN="$(get_registration_token)"; then
        echo "Failed to get runner registration token" >&2
        exit 1
    fi
    echo "Got token for runner registration: ${TOKEN}"
    echo "Running new container: ${NAME}"
    docker run \
        --rm \
        --name "${NAME}" \
        --device-cgroup-rule 'c 261:* rmw' \
        --ulimit memlock=-1:-1 \
        -v /opt/xilinx/xrt:/opt/xilinx/xrt:ro \
        -v /dev/accel/accel0:/dev/accel/accel0 \
        -v /srv:/srv:ro \
        -e GITHUB_RUNNER_TOKEN="${TOKEN}" \
        -e GITHUB_OWNER="${GITHUB_OWNER}" \
        -e GITHUB_REPO="${GITHUB_REPO}" \
        -e RUNNER_LABELS="${ARCH},docker" \
        ${IMAGE_NAME}
    echo "Container ${NAME} exited. Restarting in 2 seconds..."
    sleep 2
done
