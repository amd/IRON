# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

FLM_REPO   := https://github.com/andrej/FastFlowLM.git
FLM_COMMIT := ea31ca5a6f8738e691e5f323a0c99f01e676f0d8
BUILD      := $(CURDIR)/build
FLM_ROOT   := $(BUILD)/FastFlowLM
FLM_SRC    := $(FLM_ROOT)/src
FLM_BIN    := $(FLM_SRC)/build/flm
CACHE      ?= $(BUILD)/cache
MODELS     ?= $(CURDIR)/models
PORT       ?= 52625
JOBS       ?= 2
FLM_VERSION ?= 1.0.7
NPU_VERSION ?= 32.0.203.304
IRON_PYTHON ?= $(shell python3 -c 'import sys; print(sys.executable)')

.PHONY: flm pull serve-llama serve-embedding

$(FLM_ROOT):
	git clone $(FLM_REPO) $@
	git -C $@ checkout $(FLM_COMMIT)
	git -C $@ submodule update --init --recursive

flm: | $(FLM_ROOT)
	cmake -S $(FLM_SRC) -B $(FLM_SRC)/build -G Ninja \
	    -DCMAKE_BUILD_TYPE=Release \
	    -DFLM_VERSION=$(FLM_VERSION) \
	    -DNPU_VERSION=$(NPU_VERSION) \
	    -DFLM_ENABLE_IRON=ON
	cmake --build $(FLM_SRC)/build -j$(JOBS)

pull: flm
	FLM_CONFIG_PATH=$(FLM_SRC)/model_list.json \
	FLM_MODELINFO_PATH=$(FLM_SRC)/model_info.json \
	FLM_MODEL_PATH=$(MODELS)/.. \
	FLM_XCLBIN_PATH=$(FLM_SRC)/xclbins \
	$(FLM_BIN) pull llama3.2-iron:1b
	FLM_CONFIG_PATH=$(FLM_SRC)/model_list.json \
	FLM_MODELINFO_PATH=$(FLM_SRC)/model_info.json \
	FLM_MODEL_PATH=$(MODELS)/.. \
	FLM_XCLBIN_PATH=$(FLM_SRC)/xclbins \
	$(FLM_BIN) pull embeddinggemma-2

serve-llama: flm
	FLM_CONFIG_PATH=$(FLM_SRC)/model_list.json \
	FLM_MODELINFO_PATH=$(FLM_SRC)/model_info.json \
	FLM_MODEL_PATH=$(MODELS)/.. \
	FLM_XCLBIN_PATH=$(FLM_SRC)/xclbins \
	FLM_IRON_PYTHON=$(IRON_PYTHON) \
	PYTHONPATH=$(CURDIR)/../../..:$${PYTHONPATH} \
	NPU_CACHE_HOME=$(CACHE) \
	$(FLM_BIN) serve llama3.2-iron:1b --ctx-len 2048 --port $(PORT)

serve-embedding: flm
	FLM_CONFIG_PATH=$(FLM_SRC)/model_list.json \
	FLM_MODELINFO_PATH=$(FLM_SRC)/model_info.json \
	FLM_MODEL_PATH=$(MODELS)/.. \
	FLM_XCLBIN_PATH=$(FLM_SRC)/xclbins \
	FLM_IRON_PYTHON=$(IRON_PYTHON) \
	PYTHONPATH=$(CURDIR)/../../..:$${PYTHONPATH} \
	NPU_CACHE_HOME=$(CACHE) \
	$(FLM_BIN) serve embeddinggemma-2 --backend iron --port $(PORT)
