# IRON - CI Summary

## Examples

<details>
<summary>iron/applications/gemma4_flm</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_iron_matches_engine[prompt_long_prompt] | ✅ | - | - | - |
| test_iron_matches_engine[prompt_word_problem] | ✅ | - | - | - |

</details>

<details>
<summary>iron/applications/llama_3.2_1b</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter0] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter1] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter2] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter3] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter4] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter0] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter1] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter2] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter3] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter4] | ✅ | - | - | - |

</details>

## Small

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 155.12 | ✅ | 361.88 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 155.90 | ✅ | 424.42 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 172.82 | ✅ | 517.80 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 166.34 | ✅ | 436.62 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 195.06 | ✅ | 678.38 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 217.60 | ✅ | 412.32 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 192.96 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 220.08 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 4723.66 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 850.28 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 177.36 | ✅ | 422.34 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 149.18 | ✅ | 355.08 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 142.52 | ✅ | 658.70 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 137.96 | ✅ | 821.48 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 139.80 | ✅ | 431.78 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 196.50 | ✅ | 694.78 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 181.74 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 201.06 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 1919.32 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 484.22 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 145.14 | ✅ | 426.50 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 172.90 | ✅ | 331.44 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 172.78 | ✅ | 394.82 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 168.00 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3861.54 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 981.48 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 167.48 | ✅ | 296.94 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 183.54 | ✅ | 425.64 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 175.94 | ✅ | 436.00 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 206.32 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 5699.84 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 877.66 | - | - |

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gate_up_interleaved_blob[iter0] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter1] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter2] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter3] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter4] | ✅ | - | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | 663.68 | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | 963.78 | - | - |
| test_matches_reference[K_1024-N_128] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_512] | ✅ | - | - | - |
| test_matches_reference[K_1536-N_640] | ✅ | - | - | - |
| test_matches_reference[K_2048-N_256] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter0] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter1] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter2] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter3] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter4] | ✅ | - | - | - |
| test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | - | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 353.60 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 307.12 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 296.76 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 289.10 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 336.50 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 313.00 | - | - |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 294.62 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 372.28 | - | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/layer</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[gemma4_e2b-global-5] | ✅ | 823.16 | - | - |
| test_matches_reference[gemma4_e2b-global-700] | ✅ | 876.62 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-37] | ✅ | 1234.32 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-700] | ✅ | 1283.14 | - | - |
| test_matches_reference[gemma4_e2b-swa-1023] | ✅ | 784.50 | - | - |
| test_matches_reference[gemma4_e2b-swa-37] | ✅ | 729.88 | - | - |
| test_matches_reference[gemma4_e2b-swa-511] | ✅ | 737.44 | - | - |
| test_matches_reference[gemma4_e2b-swa-512] | ✅ | 744.26 | - | - |
| test_matches_reference[gemma4_e2b-swa-700] | ✅ | 745.54 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-1023] | ✅ | 1041.52 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-37] | ✅ | 1188.86 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-511] | ✅ | 1011.56 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-512] | ✅ | 1132.44 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-700] | ✅ | 1088.12 | - | - |
| test_rejects_unknown_configurations[geometry] | ✅ | - | ✅ | - |
| test_rejects_unknown_configurations[layer_type] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa_skip] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/lm_head</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemma4_softcap[dim_1536] | ✅ | - | - | - |
| test_gemma4_softcap[dim_2560] | ✅ | - | - | - |
| test_projection_matches_reference[dim_1536] | ✅ | - | - | - |
| test_projection_matches_reference[dim_2560] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_inf-match_finite and positive] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter0] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter1] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter2] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter3] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter4] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/prefill_attn</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | 369.68 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 374.98 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 766.94 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_2] | ✅ | 770.08 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 1873.94 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 2066.84 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1013.28 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_2] | ✅ | 1003.34 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 4510.56 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_2] | ✅ | 4501.54 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1912.70 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1901.24 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 216.74 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 216.32 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 801.34 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 807.38 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 2671.96 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_2] | ✅ | 2361.52 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1255.12 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1252.86 | - | - |
| test_one_callable_serves_every_range[kind_attn] | ✅ | - | - | - |
| test_one_callable_serves_every_range[kind_swa] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 4}-match_query heads] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 174.46 | ✅ | 287.90 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 181.98 | ✅ | 419.04 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 208.48 | ✅ | 381.90 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 209.38 | ✅ | 446.92 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 161.64 | ✅ | 474.22 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 173.86 | ✅ | 550.86 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 199.66 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 227.50 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3937.26 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 687.78 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2268.62 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 238.90 | ✅ | 806.18 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 259.04 | ✅ | 628.80 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 46982.78 | ✅ | 83295.70 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27692.88 | ✅ | 18886.68 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7674.80 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2210.16 | ✅ | 3675.70 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3278.60 | ✅ | 7594.62 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1438.56 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 178.12 | ✅ | 335.02 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2634.42 | ✅ | 9336.36 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1394.28 | ✅ | 5077.66 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 830.98 | ✅ | 3104.24 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 792.80 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2810.00 | ✅ | 9217.36 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1473.78 | ✅ | 5301.26 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 836.68 | ✅ | 2945.32 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 843.12 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 462.38 | ✅ | 2391.30 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 309.58 | ✅ | 795.50 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 237.16 | ✅ | 2255.52 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 446.58 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 1100.98 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 205.14 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 290.38 | ✅ | 2362.50 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 191.92 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2641.52 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2599.58 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 154.16 | ✅ | 416.86 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 161.06 | ✅ | 487.38 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 168.66 | ✅ | 444.52 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 173.02 | ✅ | 889.62 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 166.74 | ✅ | 444.46 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 172.50 | ✅ | 594.66 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 218.32 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 213.54 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3521.56 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 706.96 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 161.10 | ✅ | 347.48 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 174.74 | ✅ | 327.86 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 178.34 | ✅ | 331.24 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 175.96 | ✅ | 411.78 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 177.80 | ✅ | 539.08 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 163.80 | ✅ | 426.60 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 144.14 | ✅ | 719.40 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 176.56 | ✅ | 562.26 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 181.76 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 206.62 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 3444.54 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 676.88 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 186.82 | ✅ | 365.92 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 233.44 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 166.18 | ✅ | 485.82 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 148.30 | ✅ | 552.88 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 153.44 | ✅ | 598.66 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 157.12 | ✅ | 431.16 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 187.66 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 175.06 | ✅ | 457.98 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 670.02 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 3970.52 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 17077.68 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 158.72 | ✅ | 303.56 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 156.84 | ✅ | 581.88 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 191.06 | ✅ | 432.36 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 173.98 | ✅ | 432.98 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 153.32 | ✅ | 672.94 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 173.20 | ✅ | 621.82 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 187.84 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 196.18 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 4020.82 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 677.94 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 162.98 | ✅ | 412.96 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 196.54 | ✅ | 396.50 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 199.80 | ✅ | 267.80 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 170.02 | ✅ | 464.46 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 164.54 | ✅ | 414.96 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 171.50 | ✅ | 612.86 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 162.16 | ✅ | 640.10 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 198.92 | ✅ | 381.96 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 165.52 | ✅ | 322.78 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 156.28 | ✅ | 431.40 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 199.62 | ✅ | 465.34 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 171.58 | ✅ | 486.16 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 190.00 | ✅ | 331.58 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 179.84 | ✅ | 904.02 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 203.46 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 180.88 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 221.96 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 208.08 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3221.84 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 3924.32 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 736.40 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 683.30 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 189.26 | ✅ | 579.14 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 177.94 | ✅ | 425.74 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 184.30 | ✅ | 414.86 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 202.42 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 175.48 | ✅ | 276.26 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 160.58 | ✅ | 492.82 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 164.26 | ✅ | 655.82 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 186.58 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1687.04 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 323.96 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 189.86 | ✅ | 401.16 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 171.38 | ✅ | 692.72 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 167.08 | ✅ | 422.24 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 161.76 | ✅ | 381.82 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 168.18 | ✅ | 379.24 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 180.18 | ✅ | 822.84 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 192.26 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 191.38 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3026.22 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 674.80 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 162.78 | ✅ | 317.86 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 201.74 | ✅ | 405.52 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 177.78 | ✅ | 471.52 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 206.22 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4821.56 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 682.54 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 518.82 | ✅ | 2085.52 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 175.14 | ✅ | 344.56 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 168.84 | ✅ | 333.24 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 171.02 | ✅ | 428.80 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 476.30 | ✅ | 2607.04 |
| test_strided_copy[chunked_transfer] | ✅ | 169.56 | ✅ | 413.96 |
| test_strided_copy[contiguous] | ✅ | 176.70 | ✅ | 310.86 |
| test_strided_copy[four_channels] | ✅ | 173.12 | ✅ | 376.98 |
| test_strided_copy[kv_slot0] | ✅ | 163.40 | ✅ | 430.50 |
| test_strided_copy[kv_slot5] | ✅ | 172.74 | ✅ | 668.64 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 161.64 | ✅ | 375.98 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 165.92 | ✅ | 375.66 |
| test_strided_copy[kv_slot_last] | ✅ | 156.98 | ✅ | 287.94 |
| test_strided_copy[two_channels] | ✅ | 199.64 | ✅ | 300.98 |
| test_strided_copy[two_channels_chunked] | ✅ | 155.58 | ✅ | 311.20 |
| test_strided_copy_cache_offset_parameter[iter0] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter1] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter2] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter3] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter4] | ✅ | - | - | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 1012.42 | ✅ | 15150.81 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1043.82 | ✅ | 10393.00 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2147.32 | ✅ | 22345.06 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2330.91 | ✅ | 18566.00 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 158.80 | ✅ | 441.26 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 165.66 | ✅ | 387.40 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 166.20 | ✅ | 458.02 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 208.20 | ✅ | 507.30 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 209.70 | ✅ | 466.72 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 193.56 | ✅ | 441.88 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 221.72 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 234.28 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 4413.30 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 777.98 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns] | ✅ | - | ✅ | - |
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_1] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_2] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_4] | ✅ | - | ✅ | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 180.44 | ✅ | 449.36 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 213.22 | ✅ | 1725.60 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 205.48 | ✅ | 481.76 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3841.50 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 994.68 | - | - |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_1.003] | ✅ | 150.56 | ✅ | 470.16 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 169.04 | ✅ | 515.08 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 188.40 | ✅ | 331.70 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_1.003] | ✅ | 169.44 | ✅ | 514.24 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 172.66 | ✅ | 507.58 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 160.50 | ✅ | 470.50 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_1.003] | ✅ | 184.82 | ✅ | 411.56 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 199.02 | ✅ | 358.20 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 181.36 | ✅ | 431.90 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_1.003] | ✅ | 208.40 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 169.48 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 181.16 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 200.00 | ✅ | 324.78 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 179.58 | ✅ | 432.00 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 165.18 | ✅ | 594.96 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 166.80 | ✅ | 398.78 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 163.32 | ✅ | 367.90 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 179.66 | ✅ | 443.28 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 183.04 | ✅ | 530.92 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 178.56 | ✅ | 428.14 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 176.38 | ✅ | 505.14 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 252.04 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 189.12 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 207.22 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_1.003] | ✅ | 174.92 | ✅ | 507.46 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 172.14 | ✅ | 683.30 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 180.90 | ✅ | 498.02 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_1.003] | ✅ | 165.46 | ✅ | 472.84 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 180.40 | ✅ | 419.82 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 173.72 | ✅ | 511.86 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_1.003] | ✅ | 174.42 | ✅ | 554.02 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 188.64 | ✅ | 544.38 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 186.74 | ✅ | 443.80 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_1.003] | ✅ | 215.90 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 194.62 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 200.76 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_1.003] | ✅ | 180.82 | ✅ | 337.36 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 176.42 | ✅ | 386.48 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 183.18 | ✅ | 366.26 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_1.003] | ✅ | 192.86 | ✅ | 447.50 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 166.14 | ✅ | 402.78 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 166.14 | ✅ | 432.48 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_1.003] | ✅ | 194.16 | ✅ | 556.30 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 182.74 | ✅ | 557.24 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 166.00 | ✅ | 400.18 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_1.003] | ✅ | 195.76 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 214.22 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 194.50 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 4718.22 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 995.32 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 140.54 | ✅ | 338.76 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 134.44 | ✅ | 352.30 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 167.70 | ✅ | 823.94 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 150.72 | ✅ | 882.90 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 166.92 | ✅ | 384.88 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 174.80 | ✅ | 779.40 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 217.52 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 257.24 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 196.16 | ✅ | 303.24 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 179.78 | ✅ | 346.42 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 160.64 | ✅ | 456.08 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 157.76 | ✅ | 833.86 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 170.14 | ✅ | 429.24 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 196.46 | ✅ | 419.84 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 161.50 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 200.72 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 197.18 | ✅ | 408.16 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 158.10 | ✅ | 447.48 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 150.96 | ✅ | 366.54 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 171.58 | ✅ | 444.88 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 146.48 | ✅ | 403.10 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 198.18 | ✅ | 554.10 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 162.64 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 202.58 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 175.18 | ✅ | 435.90 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 172.50 | ✅ | 455.96 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 158.72 | ✅ | 447.28 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 187.96 | ✅ | 627.06 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 172.98 | ✅ | 379.80 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 181.68 | ✅ | 544.78 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 200.98 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 236.32 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 1551.28 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 472.74 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 173.32 | ✅ | 325.10 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 153.24 | ✅ | 375.24 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 169.44 | ✅ | 455.60 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 214.32 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 166.82 | ✅ | 282.98 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 153.82 | ✅ | 343.48 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 179.06 | ✅ | 481.18 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 241.98 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 173.28 | ✅ | 826.80 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 172.80 | ✅ | 292.24 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 150.74 | ✅ | 423.14 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 231.72 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 148.44 | ✅ | 321.48 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 180.48 | ✅ | 500.02 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 169.44 | ✅ | 776.56 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 203.72 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4618.30 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 884.14 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 163.00 | ✅ | 315.44 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 141.90 | ✅ | 416.00 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 164.44 | ✅ | 371.56 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 185.20 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 159.42 | ✅ | 273.70 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 147.88 | ✅ | 613.00 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 182.20 | ✅ | 811.22 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 176.62 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 146.38 | ✅ | 366.36 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 166.06 | ✅ | 404.68 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 175.38 | ✅ | 452.80 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 202.18 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 159.82 | ✅ | 530.22 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 174.44 | ✅ | 482.18 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 217.62 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 5456.26 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 887.76 | - | - |

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_e4b_gate_up_interleaved[iter0] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter1] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter2] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter3] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter4] | ✅ | - | - | - |
| test_e4b_shapes[K_10240-N_2560] | ✅ | - | - | - |
| test_e4b_shapes[K_2560-N_10240] | ✅ | - | - | - |
| test_e4b_shapes[K_2560-N_2560] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter0] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter1] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter2] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter3] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter4] | ✅ | - | - | - |
| test_large_k_shapes[K_12288-N_1536] | ✅ | 1734.56 | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | 632.90 | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | 806.60 | - | - |
| test_matches_reference[K_1024-N_128] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_512] | ✅ | - | - | - |
| test_matches_reference[K_1536-N_640] | ✅ | - | - | - |
| test_matches_reference[K_2048-N_256] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter0] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter1] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter2] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter3] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter4] | ✅ | - | - | - |
| test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | - | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | - | - |
| test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4027.84 | - | - |
| test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 879.26 | - | - |
| test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 3516.04 | - | - |
| test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1038.58 | - | - |
| test_gemm[M_16384-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1990.28 | - | - |
| test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7519.28 | - | - |
| test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1262.36 | - | - |
| test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 5997.94 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 365.84 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 342.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 304.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 331.62 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even] | ✅ | 353.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 360.38 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor] | ✅ | 349.62 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 298.20 | - | - |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 350.68 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 425.00 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | ✅ | 451.64 | - | - |
| test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 462.98 | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_256-K_512-N_1024] | ✅ | - | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_256] | ✅ | - | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_6144] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma64] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/layer</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[gemma4_e2b-global-5] | ✅ | 802.60 | - | - |
| test_matches_reference[gemma4_e2b-global-700] | ✅ | 940.14 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-37] | ✅ | 1117.90 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-700] | ✅ | 1561.34 | - | - |
| test_matches_reference[gemma4_e2b-swa-1023] | ✅ | 748.78 | - | - |
| test_matches_reference[gemma4_e2b-swa-37] | ✅ | 740.74 | - | - |
| test_matches_reference[gemma4_e2b-swa-511] | ✅ | 741.36 | - | - |
| test_matches_reference[gemma4_e2b-swa-512] | ✅ | 734.46 | - | - |
| test_matches_reference[gemma4_e2b-swa-700] | ✅ | 756.44 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-1023] | ✅ | 1063.62 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-37] | ✅ | 1061.22 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-511] | ✅ | 981.44 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-512] | ✅ | 1056.76 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-700] | ✅ | 1161.36 | - | - |
| test_matches_reference[gemma4_e4b-global-5] | ✅ | 1813.28 | - | - |
| test_matches_reference[gemma4_e4b-global-700] | ✅ | 1948.80 | - | - |
| test_matches_reference[gemma4_e4b-global_skip-37] | ✅ | 1942.74 | - | - |
| test_matches_reference[gemma4_e4b-global_skip-700] | ✅ | 2003.16 | - | - |
| test_matches_reference[gemma4_e4b-swa-1023] | ✅ | 1817.14 | - | - |
| test_matches_reference[gemma4_e4b-swa-37] | ✅ | 1429.64 | - | - |
| test_matches_reference[gemma4_e4b-swa-511] | ✅ | 1523.88 | - | - |
| test_matches_reference[gemma4_e4b-swa-512] | ✅ | 1772.88 | - | - |
| test_matches_reference[gemma4_e4b-swa-700] | ✅ | 1739.44 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-1023] | ✅ | 1686.64 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-37] | ✅ | 1513.08 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-511] | ✅ | 1725.44 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-512] | ✅ | 1494.74 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-700] | ✅ | 1535.92 | - | - |
| test_rejects_unknown_configurations[geometry] | ✅ | - | ✅ | - |
| test_rejects_unknown_configurations[layer_type] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa_skip] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/lm_head</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemma4_softcap[dim_1536] | ✅ | - | - | - |
| test_gemma4_softcap[dim_2560] | ✅ | - | - | - |
| test_gemma4_vocabulary[dim_1536] | ✅ | 4441.02 | - | - |
| test_gemma4_vocabulary[dim_2560] | ✅ | 6599.20 | - | - |
| test_projection_matches_reference[dim_1536] | ✅ | - | - | - |
| test_projection_matches_reference[dim_2560] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_inf-match_finite and positive] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter0] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter1] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter2] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter3] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter4] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/mm_prebuilt</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_silu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1280-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_640-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_512-K_1024-N_2048-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_none-clamp_(-2.0, 2.0)] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_sigmoid-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_silu-clamp_None] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/prefill_attn</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemma4_cache_bound[kind_attn-num_kv_heads_1] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_attn-num_kv_heads_2] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_swa-num_kv_heads_1] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_swa-num_kv_heads_2] | ✅ | - | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | 371.84 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 375.28 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 775.12 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_2] | ✅ | 767.16 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 1830.22 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 1822.52 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1004.42 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_2] | ✅ | 1001.48 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 4862.66 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_2] | ✅ | 4497.38 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1914.22 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 2097.80 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 216.04 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 217.22 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 803.40 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 804.08 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 2354.06 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_2] | ✅ | 2364.72 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1569.30 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1591.32 | - | - |
| test_one_callable_serves_every_range[kind_attn] | ✅ | - | - | - |
| test_one_callable_serves_every_range[kind_swa] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 4}-match_query heads] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 185.72 | ✅ | 362.48 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 189.10 | ✅ | 441.84 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 158.16 | ✅ | 820.54 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 175.96 | ✅ | 665.26 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 189.00 | ✅ | 401.92 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 183.98 | ✅ | 468.68 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 192.46 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 248.88 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 171.10 | ✅ | 413.78 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 180.36 | ✅ | 348.52 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 181.82 | ✅ | 349.12 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 187.34 | ✅ | 376.78 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 176.42 | ✅ | 425.64 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 188.10 | ✅ | 657.54 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 217.00 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 249.00 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 173.48 | ✅ | 393.90 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 186.86 | ✅ | 434.22 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 156.88 | ✅ | 436.44 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 164.52 | ✅ | 435.34 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 166.38 | ✅ | 393.32 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 201.24 | ✅ | 493.84 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 195.34 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 254.68 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 173.64 | ✅ | 454.34 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 176.24 | ✅ | 799.36 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 171.38 | ✅ | 720.18 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 201.22 | ✅ | 438.42 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 173.66 | ✅ | 771.36 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 206.36 | ✅ | 554.44 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 196.52 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 263.10 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 4133.42 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 716.10 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 18863.30 | - | - |
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2128.86 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 232.00 | ✅ | 520.38 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 220.42 | ✅ | 661.84 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47061.32 | ✅ | 81460.24 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-partition_N_1] | ✅ | 119595.48 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27623.76 | ✅ | 18543.22 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-partition_N_1] | ✅ | 6957.12 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-partition_N_1] | ✅ | 8540.82 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7701.26 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93227.28 | ✅ | 92153.94 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100816.24 | ✅ | 91694.60 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 107222.50 | ✅ | 72882.96 |
| test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 36914.46 | - | - |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1074.52 | ✅ | 2590.06 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 1173.16 | ✅ | 3417.64 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1339.88 | ✅ | 2695.16 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3664.08 | ✅ | 6805.52 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 3793.26 | ✅ | 6681.02 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3972.18 | ✅ | 5569.00 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93217.82 | ✅ | 98850.60 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100754.30 | ✅ | 96713.60 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 106331.04 | ✅ | 75088.58 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2136.06 | ✅ | 3949.98 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3236.36 | ✅ | 6653.70 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1513.06 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 185.78 | ✅ | 401.24 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2753.96 | ✅ | 9777.16 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1442.90 | ✅ | 5535.86 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 881.78 | ✅ | 3952.84 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 830.26 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2706.86 | ✅ | 9307.32 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1408.22 | ✅ | 5770.06 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 854.12 | ✅ | 3977.94 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 831.94 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 502.18 | ✅ | 2911.10 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 317.58 | ✅ | 2461.40 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 252.14 | ✅ | 963.80 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 442.54 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 999.10 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 242.92 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 275.64 | ✅ | 2551.78 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 143.86 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2610.24 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2528.84 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 170.24 | ✅ | 314.38 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 147.98 | ✅ | 455.90 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 153.18 | ✅ | 283.50 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 183.46 | ✅ | 408.62 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 165.98 | ✅ | 844.86 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 185.46 | ✅ | 525.12 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 158.54 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 249.10 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 187.54 | ✅ | 393.76 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 152.80 | ✅ | 325.88 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 180.68 | ✅ | 429.30 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 178.70 | ✅ | 418.38 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 180.28 | ✅ | 441.02 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 207.52 | ✅ | 478.50 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 168.60 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 241.98 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 156.28 | ✅ | 269.56 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 161.72 | ✅ | 781.92 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 170.52 | ✅ | 340.14 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 179.48 | ✅ | 544.36 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 176.02 | ✅ | 493.44 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 208.90 | ✅ | 496.50 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 197.26 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 216.50 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 199.76 | ✅ | 335.68 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 176.84 | ✅ | 435.70 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 164.26 | ✅ | 345.02 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 190.78 | ✅ | 441.06 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 191.40 | ✅ | 335.40 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 176.56 | ✅ | 565.56 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 175.24 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 210.66 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 4068.68 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 765.42 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 166.90 | ✅ | 360.98 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 166.14 | ✅ | 317.70 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 179.66 | ✅ | 447.28 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 179.50 | ✅ | 499.58 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 178.78 | ✅ | 874.22 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 170.56 | ✅ | 438.96 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 174.30 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 217.56 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 169.62 | ✅ | 299.38 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 166.44 | ✅ | 396.74 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 164.38 | ✅ | 288.70 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 163.20 | ✅ | 463.48 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 166.28 | ✅ | 271.88 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 162.18 | ✅ | 378.82 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 180.10 | ✅ | 411.40 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 174.12 | ✅ | 826.24 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 191.28 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 206.66 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 141.22 | ✅ | 463.44 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 153.58 | ✅ | 350.22 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 209.54 | ✅ | 343.48 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 151.36 | ✅ | 426.32 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 157.24 | ✅ | 529.54 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 187.26 | ✅ | 566.54 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 187.30 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 214.06 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 185.38 | ✅ | 420.16 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 164.00 | ✅ | 445.88 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 172.88 | ✅ | 416.74 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 183.72 | ✅ | 423.50 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 189.78 | ✅ | 437.86 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 173.02 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 205.86 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 3034.10 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 643.52 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 151.56 | ✅ | 368.24 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 158.84 | ✅ | 411.66 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 238.06 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 195.26 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 163.92 | ✅ | 430.94 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 162.58 | ✅ | 434.62 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 150.54 | ✅ | 350.56 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 172.62 | ✅ | 422.74 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 173.40 | ✅ | 411.20 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 167.24 | ✅ | 895.18 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 180.68 | ✅ | 488.58 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 170.34 | ✅ | 472.78 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 196.36 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 177.84 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 220.18 | ✅ | 466.98 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 176.82 | ✅ | 511.44 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 181.30 | ✅ | 287.36 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 148.32 | ✅ | 328.96 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 206.86 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 196.34 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 139.28 | ✅ | 356.66 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 153.52 | ✅ | 437.62 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 138.16 | ✅ | 430.00 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 141.26 | ✅ | 606.00 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 185.32 | ✅ | 464.92 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 150.68 | ✅ | 413.50 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 157.72 | ✅ | 384.36 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 153.32 | ✅ | 343.44 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 193.64 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 180.12 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 173.38 | ✅ | 485.88 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 157.78 | ✅ | 493.50 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 158.30 | ✅ | 346.76 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 163.48 | ✅ | 446.96 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 182.42 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 183.26 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 149.86 | ✅ | 529.18 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 149.46 | ✅ | 307.50 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 139.50 | ✅ | 674.68 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 167.38 | ✅ | 431.12 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 171.98 | ✅ | 357.32 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 170.96 | ✅ | 303.74 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 179.12 | ✅ | 423.84 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 179.42 | ✅ | 514.68 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 152.24 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 166.00 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 169.90 | ✅ | 522.72 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 156.82 | ✅ | 503.12 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 160.50 | ✅ | 320.78 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 150.28 | ✅ | 253.50 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 213.28 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 217.30 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 179.42 | ✅ | 263.44 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 133.98 | ✅ | 286.22 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 153.50 | ✅ | 443.46 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 253.94 | ✅ | 374.62 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 173.02 | ✅ | 427.44 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 155.26 | ✅ | 282.64 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 176.00 | ✅ | 756.68 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 147.64 | ✅ | 344.10 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 177.52 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 162.20 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 190.16 | ✅ | 473.90 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 179.24 | ✅ | 374.32 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 712.28 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 3765.04 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 17672.60 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 16307.64 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 148277.42 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 161.48 | ✅ | 700.16 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 162.42 | ✅ | 510.64 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 178.16 | ✅ | 651.40 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 188.02 | ✅ | 529.42 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 190.76 | ✅ | 774.32 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 196.84 | ✅ | 508.48 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 202.58 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 213.48 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 165.74 | ✅ | 373.98 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 161.92 | ✅ | 329.42 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 164.16 | ✅ | 406.70 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 183.86 | ✅ | 623.30 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 184.78 | ✅ | 456.78 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 178.10 | ✅ | 543.14 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 182.48 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 241.72 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 157.12 | ✅ | 290.68 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 174.62 | ✅ | 316.98 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 170.14 | ✅ | 469.20 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 166.14 | ✅ | 388.46 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 174.06 | ✅ | 715.56 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 186.18 | ✅ | 450.80 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 183.44 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 204.64 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 158.98 | ✅ | 282.86 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 175.52 | ✅ | 410.70 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 181.54 | ✅ | 386.04 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 185.52 | ✅ | 465.56 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 181.34 | ✅ | 458.96 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 187.58 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 238.76 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2784.74 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 774.58 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 180.04 | ✅ | 333.96 |
| test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None] | ✅ | 184.62 | ✅ | 304.18 |
| test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64] | ✅ | 821.86 | ✅ | 2964.88 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 179.92 | ✅ | 317.50 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 186.02 | ✅ | 304.40 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 188.88 | ✅ | 341.78 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 170.18 | ✅ | 964.70 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 160.22 | ✅ | 319.68 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 147.30 | ✅ | 441.40 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 181.82 | ✅ | 327.84 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 210.72 | ✅ | 430.20 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 171.76 | ✅ | 391.72 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 175.52 | ✅ | 507.30 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 182.82 | ✅ | 423.48 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 179.64 | ✅ | 506.82 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 197.40 | ✅ | 490.40 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 199.74 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 213.54 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 216.82 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 215.26 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 160.92 | ✅ | 345.98 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 168.36 | ✅ | 503.42 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 228.98 | ✅ | 508.08 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 185.64 | ✅ | 809.98 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 186.88 | ✅ | 345.58 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 159.26 | ✅ | 559.04 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 161.40 | ✅ | 707.70 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 173.26 | ✅ | 446.04 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 173.40 | ✅ | 519.22 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 147.58 | ✅ | 299.10 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 171.78 | ✅ | 462.82 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 225.00 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 168.02 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 177.98 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 181.14 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 172.62 | ✅ | 436.46 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 189.48 | ✅ | 323.14 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 169.88 | ✅ | 441.92 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 201.50 | ✅ | 744.46 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 179.44 | ✅ | 371.24 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 189.68 | ✅ | 820.00 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 183.68 | ✅ | 469.52 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 188.46 | ✅ | 396.16 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 162.02 | ✅ | 710.18 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 192.42 | ✅ | 573.98 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 164.40 | ✅ | 487.30 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 213.90 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 174.16 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 213.54 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 191.88 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 160.30 | ✅ | 432.42 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 156.10 | ✅ | 401.88 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 221.56 | ✅ | 564.72 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 160.90 | ✅ | 458.16 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 197.98 | ✅ | 514.28 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 172.08 | ✅ | 522.84 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 174.14 | ✅ | 552.40 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 162.98 | ✅ | 839.96 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 190.30 | ✅ | 765.26 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 170.12 | ✅ | 925.80 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 209.58 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 178.00 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 239.74 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 213.14 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3664.72 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 4053.48 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 735.98 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 693.26 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 179.46 | ✅ | 440.28 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 163.50 | ✅ | 411.18 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 192.26 | ✅ | 655.90 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 182.20 | ✅ | 443.34 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 184.82 | ✅ | 789.52 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 179.12 | ✅ | 485.76 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 203.70 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 174.34 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 181.62 | ✅ | 350.22 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 184.88 | ✅ | 603.86 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 165.72 | ✅ | 291.58 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 145.30 | ✅ | 503.90 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 184.06 | ✅ | 475.52 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 173.90 | ✅ | 354.22 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 183.04 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 195.82 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 164.00 | ✅ | 396.52 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 195.90 | ✅ | 418.26 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 170.74 | ✅ | 386.48 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 188.74 | ✅ | 379.06 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 178.64 | ✅ | 459.58 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 202.50 | ✅ | 663.04 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 163.78 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 175.90 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 155.52 | ✅ | 276.18 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 175.42 | ✅ | 467.50 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 169.18 | ✅ | 521.76 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 204.38 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 179.96 | ✅ | 385.94 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 166.02 | ✅ | 747.96 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 186.54 | ✅ | 401.06 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 192.70 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1079.00 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 297.36 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 159.00 | ✅ | 364.80 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 186.00 | ✅ | 337.64 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 193.26 | ✅ | 393.58 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 176.26 | ✅ | 258.22 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 181.52 | ✅ | 359.72 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 145.32 | ✅ | 456.28 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 195.52 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 229.16 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 185.62 | ✅ | 771.62 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 176.90 | ✅ | 393.26 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 155.90 | ✅ | 327.10 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 191.84 | ✅ | 369.28 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 169.64 | ✅ | 726.48 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 151.62 | ✅ | 394.42 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 182.22 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 204.02 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 160.64 | ✅ | 384.04 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 156.86 | ✅ | 334.92 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 154.56 | ✅ | 465.50 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 175.66 | ✅ | 417.58 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 168.86 | ✅ | 690.24 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 181.32 | ✅ | 332.36 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 193.72 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 207.22 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 168.02 | ✅ | 368.12 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 154.86 | ✅ | 475.24 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 157.74 | ✅ | 715.40 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 160.84 | ✅ | 488.72 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 173.40 | ✅ | 513.24 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 218.38 | ✅ | 533.76 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 189.66 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 229.46 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 196.60 | ✅ | 693.16 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 192.44 | ✅ | 413.92 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 154.02 | ✅ | 368.28 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 178.78 | ✅ | 894.92 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 152.04 | ✅ | 591.60 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 195.16 | ✅ | 449.84 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 211.20 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 266.44 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 163.06 | ✅ | 453.22 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 172.00 | ✅ | 401.88 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 181.04 | ✅ | 574.12 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 177.04 | ✅ | 413.78 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 177.96 | ✅ | 522.24 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 183.54 | ✅ | 790.36 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 162.20 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 215.30 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 170.86 | ✅ | 451.36 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 162.74 | ✅ | 483.90 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 171.88 | ✅ | 404.14 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 185.86 | ✅ | 477.00 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 181.94 | ✅ | 568.54 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 174.66 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 230.00 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3130.30 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 728.64 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 170.42 | ✅ | 307.72 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 190.76 | ✅ | 379.24 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 180.18 | ✅ | 471.66 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 198.10 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 172.66 | ✅ | 379.02 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 176.70 | ✅ | 559.74 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 162.52 | ✅ | 570.24 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 183.94 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 163.10 | ✅ | 950.52 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 177.76 | ✅ | 372.48 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 179.30 | ✅ | 589.32 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 184.62 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 184.70 | ✅ | 381.30 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 183.12 | ✅ | 493.02 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 227.72 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4297.62 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 660.92 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 547.46 | ✅ | 3392.88 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 190.90 | ✅ | 492.88 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 188.22 | ✅ | 403.92 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 207.28 | ✅ | 749.26 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 499.38 | ✅ | 2596.12 |
| test_strided_copy[chunked_transfer] | ✅ | 188.94 | ✅ | 667.06 |
| test_strided_copy[contiguous] | ✅ | 173.24 | ✅ | 396.38 |
| test_strided_copy[four_channels] | ✅ | 176.26 | ✅ | 464.18 |
| test_strided_copy[kv_llama_full] | ✅ | 152.76 | ✅ | 344.54 |
| test_strided_copy[kv_slot0] | ✅ | 184.38 | ✅ | 367.60 |
| test_strided_copy[kv_slot5] | ✅ | 181.18 | ✅ | 386.24 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 167.64 | ✅ | 444.72 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 161.58 | ✅ | 414.70 |
| test_strided_copy[kv_slot_last] | ✅ | 164.70 | ✅ | 442.44 |
| test_strided_copy[two_channels] | ✅ | 178.42 | ✅ | 379.26 |
| test_strided_copy[two_channels_chunked] | ✅ | 172.70 | ✅ | 314.14 |
| test_strided_copy_cache_offset_parameter[iter0] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter1] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter2] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter3] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter4] | ✅ | - | - | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 1005.62 | ✅ | 14363.52 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1051.79 | ✅ | 18098.56 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2171.65 | ✅ | 24630.81 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2318.63 | ✅ | 25000.01 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 150.00 | ✅ | 311.82 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 149.42 | ✅ | 322.48 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 164.34 | ✅ | 731.26 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 184.32 | ✅ | 464.50 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 174.84 | ✅ | 472.90 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 199.22 | ✅ | 473.18 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 189.82 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 205.56 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 158.70 | ✅ | 401.28 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 161.86 | ✅ | 369.66 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 167.62 | ✅ | 453.48 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 174.62 | ✅ | 629.94 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 195.52 | ✅ | 441.84 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 180.22 | ✅ | 637.92 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 241.50 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 229.72 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 167.00 | ✅ | 345.50 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 184.06 | ✅ | 473.20 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 214.72 | ✅ | 342.24 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 189.48 | ✅ | 387.80 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 192.30 | ✅ | 733.72 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 199.22 | ✅ | 558.48 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 212.16 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 235.30 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 184.78 | ✅ | 429.42 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 174.48 | ✅ | 466.08 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 227.84 | ✅ | 528.02 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 163.00 | ✅ | 365.18 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 182.80 | ✅ | 360.82 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 189.02 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 223.86 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3606.24 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 705.42 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns] | ✅ | - | ✅ | - |
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_1] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_2] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_4] | ✅ | - | ✅ | - |
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 219.16 | ✅ | 1937.74 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 201.82 | ✅ | 1051.64 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 217.30 | ✅ | 2285.78 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 224.42 | ✅ | 1061.38 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 285.84 | ✅ | 1936.00 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 260.88 | ✅ | 656.94 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 249.68 | ✅ | 1206.56 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 228.86 | ✅ | 657.50 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 234.54 | ✅ | 1261.76 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 232.50 | ✅ | 890.20 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 360.96 | ✅ | 1497.06 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 342.76 | ✅ | 1534.92 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 367.50 | ✅ | 799.52 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 338.86 | ✅ | 619.72 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 344.76 | ✅ | 1768.10 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 315.52 | ✅ | 834.58 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 322.98 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 330.92 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 173.10 | ✅ | 587.44 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 224.50 | ✅ | 729.50 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 271.62 | ✅ | 1309.94 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 201.48 | ✅ | 768.88 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 180.12 | ✅ | 451.68 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 201.62 | ✅ | 729.28 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 187.82 | ✅ | 507.38 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 160.22 | ✅ | 461.34 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 177.80 | ✅ | 520.68 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 165.06 | ✅ | 504.38 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 171.30 | ✅ | 424.40 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 161.36 | ✅ | 457.86 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 160.46 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 198.32 | ✅ | 295.68 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3693.78 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 973.40 | - | - |

</details>

