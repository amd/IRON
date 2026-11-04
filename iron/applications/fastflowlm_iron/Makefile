# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

FLM_REPO   := https://github.com/andrej/FastFlowLM.git
FLM_COMMIT := b38fdbc4b64625758ef20318556b97b081516b36
BUILD      := $(CURDIR)/build
FLM_ROOT   := $(BUILD)/FastFlowLM

.PHONY: flm
flm: $(FLM_ROOT)/.git/iron-$(FLM_COMMIT)
	BUILD_DIR=$(BUILD)/flm FLM_PREFIX=$(BUILD)/install \
	    CMAKE_BUILD_PARALLEL_LEVEL=$${CMAKE_BUILD_PARALLEL_LEVEL:-2} \
	    $(FLM_ROOT)/src/home_install.sh
	cmake -S $(FLM_ROOT)/extensions/iron -B $(BUILD)/plugin \
	    -DCMAKE_PREFIX_PATH=$(BUILD)/install -DCMAKE_BUILD_TYPE=Release
	cmake --build $(BUILD)/plugin --parallel $${CMAKE_BUILD_PARALLEL_LEVEL:-2}
	ctest --test-dir $(BUILD)/plugin --output-on-failure

$(FLM_ROOT)/.git/iron-$(FLM_COMMIT):
	git init $(FLM_ROOT)
	git -C $(FLM_ROOT) fetch --depth 1 $(FLM_REPO) $(FLM_COMMIT)
	git -C $(FLM_ROOT) checkout $(FLM_COMMIT)
	git -C $(FLM_ROOT) submodule update --init --recursive
	touch $@
