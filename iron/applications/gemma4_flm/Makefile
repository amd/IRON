# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# FastFlowLM's Gemma 4 E2B engine with its text-path operators on IRON.
#
#   make weights   builds flm and downloads the model
#   make engine    builds the IRON operators and the IRON engine
#   make serve     serves the model on the IRON engine

FLM_REPO   := https://github.com/ROCm/FastFlowLM
FLM_COMMIT := 95f455e7ca39a2088b8a457dc44af10ecb3c2b40
BUILD      := $(CURDIR)/build
FLM        := $(BUILD)/FastFlowLM/src
# The stock build writes flm to its own binary directory.
FLM_BIN    := $(BUILD)/stock/flm
# FLM_BUILD_GEMMA4E defaults to off, which links FastFlowLM's prebuilt Gemma 4
# engine and leaves the gemma4e_npu target undefined.
CMAKE      := cmake -S $(FLM) -G Ninja -DFLM_VERSION=1.0.5 -DNPU_VERSION=32.0.203.304 \
              -DFLM_BUILD_GEMMA4E=ON
TXN_INC    := $(shell python3 -c "import aie.utils.config as c; print(c.runtime_header_path())")
MODEL      := $(or $(FLM_MODEL_PATH),$(error set FLM_MODEL_PATH))/models/Gemma4-E2B-IT-NPU2
PORT       ?= 11434

.PHONY: flm weights operators engine serve

$(BUILD)/FastFlowLM:
	git clone $(FLM_REPO) $@
	git -C $@ checkout $(FLM_COMMIT)
	git -C $@ submodule update --init --recursive

# flm with FastFlowLM's own Gemma 4 engine, the stock engine.
flm: | $(BUILD)/FastFlowLM
	$(CMAKE) -B $(BUILD)/stock
	cmake --build $(BUILD)/stock

weights: $(MODEL)/model.q4nx

# flm looks for model_info.json next to its executable or in its install
# prefix. A build that is not installed finds it through FLM_MODELINFO_PATH.
# flm pull exits 0 when it downloads nothing, so the recipe checks the file.
$(MODEL)/model.q4nx: | flm
	cd $(FLM) && FLM_MODELINFO_PATH=$(FLM)/model_info.json $(FLM_BIN) pull gemma4-it:e2b
	test -f $@

# build.py reads the model's config and repacks its PLI weights.
operators: $(MODEL)/model.q4nx | $(BUILD)/FastFlowLM
	python3 build.py $(FLM)/xclbins $(BUILD)

# The IRON engine. The flm of the stock build loads it through LD_LIBRARY_PATH.
engine: flm operators
	$(CMAKE) -B $(BUILD)/engine \
	    -DFLM_OVERRIDE_FLAGS='-I$(CURDIR) -I$(BUILD)/gen -I$(TXN_INC) -DFLM_OVERRIDES="\"overrides.hpp\""'
	cmake --build $(BUILD)/engine --target gemma4e_npu

serve:
	cd $(FLM) && LD_LIBRARY_PATH=$(BUILD)/engine/engines:$$LD_LIBRARY_PATH FLM_XCLBIN_PATH=$(BUILD) \
	    $(FLM_BIN) serve gemma4-it:e2b --prefill-chunk-len 512 --port $(PORT)
