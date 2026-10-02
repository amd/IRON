# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# FastFlowLM's Gemma 4 E2B engine with its text-path operators on IRON.
# Run the targets in this order: make clone operators engine, then make serve.

FLM_REPO   := https://github.com/andrej/FastFlowLM
FLM_COMMIT := 609bc6714987beb8c35079ac8a51b53e0bf067d0
BUILD      := $(CURDIR)/build
FLM        := $(BUILD)/FastFlowLM/src
CMAKE      := cmake -S $(FLM) -G Ninja -DFLM_VERSION=1.0.5 -DNPU_VERSION=32.0.203.304
PORT       ?= 11434

.PHONY: clone operators engine weights serve

clone:
	git clone $(FLM_REPO) $(BUILD)/FastFlowLM
	git -C $(BUILD)/FastFlowLM checkout $(FLM_COMMIT)
	git -C $(BUILD)/FastFlowLM submodule update --init --recursive

operators:
	python3 build.py $(FLM)/xclbins $(BUILD)

# Two engines from one checkout: build/engine compiles overrides.hpp in,
# build/stock is FastFlowLM's own. Both builds write flm to $(FLM)/build/flm.
engine:
	$(CMAKE) -B $(BUILD)/engine -DFLM_OVERRIDE_FLAGS='-I$(CURDIR) -I$(BUILD)/gen \
	    -I$(shell python3 -c "import aie.utils.config as c; print(c.runtime_header_path())") \
	    -DFLM_OVERRIDES="\"overrides.hpp\""'
	cmake --build $(BUILD)/engine
	$(CMAKE) -B $(BUILD)/stock
	cmake --build $(BUILD)/stock --target gemma4e_npu

weights:
	cd $(FLM) && ./build/flm pull gemma4-it:e2b

serve:
	cd $(FLM) && LD_LIBRARY_PATH=$(BUILD)/engine/engines FLM_XCLBIN_PATH=$(BUILD) \
	    ./build/flm serve gemma4-it:e2b --pcl 512 --port $(PORT)
