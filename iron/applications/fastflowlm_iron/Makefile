# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

FLM_REPO   := https://github.com/ROCm/FastFlowLM.git
FLM_COMMIT := 69f691b58c30effdd29fa263839054b545d8ecc7
BUILD      := $(CURDIR)/build
FLM_ROOT   := $(BUILD)/FastFlowLM

.PHONY: flm
flm: $(FLM_ROOT)/.git/iron-$(FLM_COMMIT)
	git -C $(FLM_ROOT) checkout $(FLM_COMMIT)
	git -C $(FLM_ROOT) submodule update --init --recursive
	USER=$${USER:-$$(id -un)} BUILD_DIR=$(BUILD)/flm FLM_PREFIX=$(BUILD)/install \
	    CMAKE_BUILD_PARALLEL_LEVEL=$${CMAKE_BUILD_PARALLEL_LEVEL:-2} \
	    $(FLM_ROOT)/src/home_install.sh
	cmake -S $(CURDIR) -B $(BUILD)/plugin \
	    -DCMAKE_PREFIX_PATH=$(BUILD)/install -DCMAKE_BUILD_TYPE=Release \
	    -DJSON_INCLUDE_DIR=$(FLM_ROOT)/src/include
	cmake --build $(BUILD)/plugin --parallel $${CMAKE_BUILD_PARALLEL_LEVEL:-2}
	ctest --test-dir $(BUILD)/plugin --output-on-failure

$(FLM_ROOT)/.git/iron-$(FLM_COMMIT):
	git init $(FLM_ROOT)
	git -C $(FLM_ROOT) fetch --depth 1 $(FLM_REPO) $(FLM_COMMIT)
	touch $@
