#!/bin/bash

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

IMAGE_NAME="iron-public-dev-github-runner"
GITHUB_OWNER="amd"
GITHUB_REPO="IRON"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# This script drops into an interactive shell (CMD override below), which does not
# register a runner, so the PAT is optional here -- don't fail if it is absent.
GITHUB_PAT=$(cat "${SCRIPT_DIR}/secret_github_token" 2>/dev/null || true)

DATE=$(printf '%(%Y_%m_%d_%H_%M_%S)T')
NAME="ci-run-${DATE}"
docker run \
    --rm \
    --name "${NAME}" \
    --device-cgroup-rule 'c 261:* rmw' \
    --ulimit memlock=-1:-1 \
    -v /opt/xilinx/xrt:/opt/xilinx/xrt:ro \
    -v /dev/accel/accel0:/dev/accel/accel0 \
    -v /srv:/srv:ro \
    -e GITHUB_PAT="${GITHUB_PAT}" \
    -e GITHUB_OWNER="${GITHUB_OWNER}" \
    -e GITHUB_REPO="${GITHUB_REPO}" \
    -it \
    ${IMAGE_NAME} \
    bash
