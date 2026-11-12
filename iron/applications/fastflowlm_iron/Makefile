# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

FLM_REPO   := https://github.com/andrej/FastFlowLM.git
# Temporary pin to feat/embedding-model-extensions until embedding plugins merge.
FLM_COMMIT := 1b27e4e2be4d4dfe81f7153ef7486c498ade65bf
BUILD      := $(CURDIR)/build
FLM_ROOT   := $(BUILD)/FastFlowLM

.PHONY: flm
flm: $(FLM_ROOT)/.git/iron-$(FLM_COMMIT)
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
	git -C $(FLM_ROOT) checkout $(FLM_COMMIT)
	git -C $(FLM_ROOT) submodule update --init --recursive
	touch $@
