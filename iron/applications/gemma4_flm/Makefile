# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# FastFlowLM's Gemma 4 E2B engine with its text-path operators on IRON.
#
#   make weights   builds flm and downloads the model
#   make engine    builds the IRON operators and the IRON engine
#   make serve     serves the model on the IRON engine

FLM_REPO   := https://github.com/andrej/FastFlowLM
FLM_COMMIT := 609bc6714987beb8c35079ac8a51b53e0bf067d0
BUILD      := $(CURDIR)/build
FLM        := $(BUILD)/FastFlowLM/src
CMAKE      := cmake -S $(FLM) -G Ninja -DFLM_VERSION=1.0.5 -DNPU_VERSION=32.0.203.304
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

$(MODEL)/model.q4nx: | flm
	cd $(FLM) && ./build/flm pull gemma4-it:e2b

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
	    ./build/flm serve gemma4-it:e2b --prefill-chunk-len 512 --port $(PORT)
