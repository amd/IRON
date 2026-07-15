# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# IRON dev container with GitHub Actions runner
# To run with NPU device passthrough, use:
# docker run -v /dev/accel/accel0:/dev/accel/accel0 --device-cgroup-rule 'c 261:* rmw' --ulimit memlock=-1:-1 <image>

# To build this docker, run from the repo root:
# docker build -f ci/docker-based/Dockerfile -t iron-dev-github-runner

FROM ubuntu:24.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    # MLIR-AIE build requirements  
    build-essential ninja-build python3 python3-dev python3.12-venv unzip \
    libssl-dev libboost-dev libboost-filesystem-dev libboost-program-options-dev uuid-dev \
    # Required by MHA kernel
    llvm-18 \
    # graphviz provides the `dot` binary that stream-dse's codegen shells out to
    # (via pydot) to render its workload graph; without it the stream-backed
    # operators fail at MLIR-generation time with: "dot" not found in path.
    graphviz \
    # GitHub Actions runner requirements
    git jq curl tar \
 && rm -rf /var/lib/apt/lists/*

ARG USER=iron
RUN useradd -m -s /bin/bash ${USER}

USER ${USER}
WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt

# Environment setup 
# ---

ENV HOME=/workspace 

# Ensure XRT is mounted by the host
# This errors if it does not exist.
# copy entrypoint into image and make it executable (ensure file is in the build context)
COPY --chown=${USER}:${USER} ./ci/docker-based/inside_docker /opt/inside_docker/
RUN chmod +x /opt/inside_docker/entrypoint.sh /opt/inside_docker/actions_runner.sh
ENTRYPOINT ["/opt/inside_docker/entrypoint.sh"]

CMD ["/opt/inside_docker/actions_runner.sh"]
