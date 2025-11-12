# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

add_aie_ci_test(llama_3.2_1b
                RUN 
                    "python3 ${CMAKE_CURRENT_SOURCE_DIR}/inference.py /srv/llama3.2-1b/model.safetensors /srv/llama3.2-1b/tokenizer.model --prompt_len 2048 --num_tokens 40"
                CHECK
                    "PASS!"
                METRICS 
                    "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                    "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
                    "Total" [=[  Total time: (?P<metric>[\d\.e\+-]+) seconds]=]
                    "TTFT" [=[  Prefill time: (?P<metric>[\d\.e\+-]+) seconds]=]
                    "TPS" [=[  Tokens per second: (?P<metric>[\d\.e\+-]+)]=]
                    "Num Tokens" [=[  Tokens generated: (?P<metric>[\d\.e\+-]+)]=]
)
