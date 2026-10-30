# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

FLM_REPO   := https://github.com/andrej/FastFlowLM.git
FLM_COMMIT := 33b96efc06fb177fa82e9ea56d469858cadb9039
BUILD      := $(CURDIR)/build
FLM_ROOT   := $(BUILD)/FastFlowLM

.PHONY: flm
flm: $(FLM_ROOT)/.git/iron-$(FLM_COMMIT)
	BUILD_DIR=$(BUILD)/flm FLM_PREFIX=$(BUILD)/install \
	    CMAKE_BUILD_PARALLEL_LEVEL=$${CMAKE_BUILD_PARALLEL_LEVEL:-2} \
	    $(FLM_ROOT)/src/home_install.sh --iron

$(FLM_ROOT)/.git/iron-$(FLM_COMMIT):
	git init $(FLM_ROOT)
	git -C $(FLM_ROOT) fetch --depth 1 $(FLM_REPO) $(FLM_COMMIT)
	git -C $(FLM_ROOT) checkout $(FLM_COMMIT)
	git -C $(FLM_ROOT) submodule update --init --recursive
	touch $@
