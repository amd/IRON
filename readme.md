# IRON - CI Summary

## Examples

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
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 186.60 | ✅ | 276.44 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 196.16 | ✅ | 392.88 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 175.70 | ✅ | 271.86 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 160.86 | ✅ | 267.58 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 199.00 | ✅ | 659.04 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 152.90 | ✅ | 362.32 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 173.22 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 189.14 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 4229.06 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 920.98 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 152.62 | ✅ | 301.18 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 172.48 | ✅ | 326.04 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 188.30 | ✅ | 791.80 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 187.24 | ✅ | 436.32 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 179.36 | ✅ | 522.52 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 203.94 | ✅ | 532.32 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 188.82 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 223.22 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 2103.58 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 483.44 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 157.88 | ✅ | 331.98 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 173.90 | ✅ | 463.12 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 219.20 | ✅ | 503.78 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 208.38 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4837.84 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 875.72 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 172.56 | ✅ | 439.70 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 186.98 | ✅ | 446.02 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 180.98 | ✅ | 479.50 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 216.62 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3474.18 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 899.24 | - | - |

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
| test_large_k_shapes[K_4096-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | - | - | - |
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
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 369.16 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 376.02 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 309.42 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 321.46 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 331.30 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 335.14 | ✅ | 812.76 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 371.00 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 920.24 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 821.66 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 1105.88 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 740.54 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 1105.44 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 1261.90 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 791.64 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 447.14 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1201.56 |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/prefill_attn</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | 369.98 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 374.18 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 771.30 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_2] | ✅ | 768.70 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 1820.18 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 1816.94 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1002.76 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_2] | ✅ | 1005.60 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 4510.08 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_2] | ✅ | 4564.26 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 2042.36 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1918.80 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 213.84 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 214.92 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 802.92 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 800.62 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 2354.42 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_2] | ✅ | 2374.70 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1256.10 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1252.48 | - | - |
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
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 174.14 | ✅ | 438.80 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 159.10 | ✅ | 427.22 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 198.26 | ✅ | 458.90 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 172.44 | ✅ | 462.74 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 160.46 | ✅ | 518.30 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 197.10 | ✅ | 461.24 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 214.58 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 238.32 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 4031.74 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 747.88 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2304.94 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 291.80 | ✅ | 421.86 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 245.06 | ✅ | 495.62 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47080.76 | ✅ | 80774.92 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27680.78 | ✅ | 19058.98 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7796.00 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2190.18 | ✅ | 4701.00 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3184.92 | ✅ | 6780.02 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1520.56 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 190.60 | ✅ | 271.54 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2677.50 | ✅ | 9556.60 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1397.10 | ✅ | 5680.92 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 985.32 | ✅ | 3994.58 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 816.48 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2522.34 | ✅ | 9205.94 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1539.14 | ✅ | 5319.06 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 950.98 | ✅ | 4211.74 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 765.18 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 501.48 | ✅ | 3411.50 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 331.80 | ✅ | 1141.48 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 252.76 | ✅ | 1096.68 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 469.22 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 978.20 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 224.00 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 317.04 | ✅ | 1908.86 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 174.84 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2579.90 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2622.46 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 172.96 | ✅ | 323.66 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 152.74 | ✅ | 427.68 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 156.96 | ✅ | 461.50 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 175.26 | ✅ | 516.24 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 175.70 | ✅ | 437.14 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 192.90 | ✅ | 511.60 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 216.88 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 236.16 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3071.36 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 726.70 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 187.68 | ✅ | 370.64 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 158.52 | ✅ | 341.38 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 148.54 | ✅ | 348.64 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 206.36 | ✅ | 378.68 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 178.66 | ✅ | 372.00 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 190.20 | ✅ | 478.88 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 180.00 | ✅ | 410.72 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 179.06 | ✅ | 497.40 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 166.98 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 220.36 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 2860.84 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 664.46 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 152.14 | ✅ | 496.56 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 217.28 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 182.62 | ✅ | 410.74 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 174.40 | ✅ | 394.34 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 180.74 | ✅ | 838.52 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 159.02 | ✅ | 595.38 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 168.02 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 145.64 | ✅ | 496.42 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 688.54 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 3992.24 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 17292.38 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 192.38 | ✅ | 344.04 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 177.28 | ✅ | 403.16 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 162.76 | ✅ | 362.08 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 190.14 | ✅ | 770.56 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 176.86 | ✅ | 378.72 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 230.18 | ✅ | 462.30 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 165.78 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 240.78 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3429.20 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 667.42 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 182.76 | ✅ | 201.80 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 178.26 | ✅ | 251.48 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 171.66 | ✅ | 215.22 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 168.32 | ✅ | 633.74 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 157.94 | ✅ | 345.80 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 162.48 | ✅ | 406.70 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 221.76 | ✅ | 484.64 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 188.78 | ✅ | 478.72 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 164.82 | ✅ | 944.78 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 173.68 | ✅ | 376.78 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 180.60 | ✅ | 544.64 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 181.46 | ✅ | 374.84 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 171.54 | ✅ | 535.14 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 195.60 | ✅ | 493.70 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 228.42 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 178.50 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 199.96 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 199.14 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3525.52 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 2954.24 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 670.88 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 645.26 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 171.84 | ✅ | 414.10 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 169.56 | ✅ | 575.42 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 172.84 | ✅ | 456.72 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 208.56 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 178.54 | ✅ | 366.58 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 174.30 | ✅ | 758.66 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 182.12 | ✅ | 398.06 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 229.88 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1173.72 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 325.78 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 170.98 | ✅ | 270.70 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 203.10 | ✅ | 432.94 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 205.02 | ✅ | 344.52 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 173.46 | ✅ | 396.48 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 182.40 | ✅ | 425.72 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 159.72 | ✅ | 438.42 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 210.88 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 217.32 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3950.44 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 674.16 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 147.24 | ✅ | 477.18 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 159.76 | ✅ | 446.50 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 177.76 | ✅ | 422.04 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 178.56 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4997.76 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 787.20 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 524.86 | ✅ | 2746.68 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 189.48 | ✅ | 470.44 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 181.86 | ✅ | 493.52 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 194.58 | ✅ | 522.60 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 510.78 | ✅ | 2022.24 |
| test_strided_copy[chunked_transfer] | ✅ | 161.18 | ✅ | 395.32 |
| test_strided_copy[contiguous] | ✅ | 180.62 | ✅ | 330.82 |
| test_strided_copy[four_channels] | ✅ | 160.56 | ✅ | 702.24 |
| test_strided_copy[kv_slot0] | ✅ | 157.28 | ✅ | 274.04 |
| test_strided_copy[kv_slot5] | ✅ | 165.04 | ✅ | 442.06 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 161.62 | ✅ | 419.96 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 159.92 | ✅ | 425.22 |
| test_strided_copy[kv_slot_last] | ✅ | 163.88 | ✅ | 350.48 |
| test_strided_copy[two_channels] | ✅ | 174.12 | ✅ | 381.10 |
| test_strided_copy[two_channels_chunked] | ✅ | 147.68 | ✅ | 405.92 |
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
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 984.93 | ✅ | 15554.62 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1034.25 | ✅ | 11921.38 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2130.66 | ✅ | 26229.21 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2368.07 | ✅ | 22393.58 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 166.20 | ✅ | 348.88 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 180.24 | ✅ | 430.12 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 198.64 | ✅ | 281.14 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 187.94 | ✅ | 384.98 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 181.64 | ✅ | 513.82 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 179.08 | ✅ | 468.86 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 188.90 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 186.80 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3930.74 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 696.08 | - | - |

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
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 201.18 | ✅ | 522.28 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 197.16 | ✅ | 768.98 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 228.96 | ✅ | 395.06 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3336.44 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 945.40 | - | - |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_1.003] | ✅ | 190.24 | ✅ | 373.12 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 163.24 | ✅ | 428.60 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 167.12 | ✅ | 336.08 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_1.003] | ✅ | 161.68 | ✅ | 329.02 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 176.68 | ✅ | 371.96 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 170.42 | ✅ | 654.96 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_1.003] | ✅ | 219.34 | ✅ | 690.58 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 161.62 | ✅ | 731.76 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 175.10 | ✅ | 422.92 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_1.003] | ✅ | 215.54 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 173.14 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 186.92 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 183.84 | ✅ | 307.32 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 163.88 | ✅ | 327.48 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 181.50 | ✅ | 471.10 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 181.20 | ✅ | 435.72 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 184.46 | ✅ | 378.02 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 189.92 | ✅ | 367.48 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 176.34 | ✅ | 403.72 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 183.32 | ✅ | 477.30 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 193.74 | ✅ | 412.80 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 184.42 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 193.74 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 222.58 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_1.003] | ✅ | 171.80 | ✅ | 367.58 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 199.04 | ✅ | 336.72 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 166.48 | ✅ | 600.98 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_1.003] | ✅ | 171.38 | ✅ | 365.70 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 196.62 | ✅ | 392.96 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 158.12 | ✅ | 384.58 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_1.003] | ✅ | 179.94 | ✅ | 392.78 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 187.14 | ✅ | 711.14 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 200.94 | ✅ | 410.50 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_1.003] | ✅ | 219.08 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 211.58 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 248.80 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_1.003] | ✅ | 169.04 | ✅ | 418.80 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 163.60 | ✅ | 365.10 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 171.20 | ✅ | 387.96 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_1.003] | ✅ | 163.94 | ✅ | 365.44 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 201.92 | ✅ | 387.10 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 201.76 | ✅ | 762.16 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_1.003] | ✅ | 187.34 | ✅ | 491.84 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 161.24 | ✅ | 436.32 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 184.12 | ✅ | 680.00 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_1.003] | ✅ | 194.86 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 191.94 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 210.62 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 4317.92 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 879.32 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 145.46 | ✅ | 387.28 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 148.16 | ✅ | 367.60 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 159.04 | ✅ | 411.00 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 157.28 | ✅ | 450.62 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 171.28 | ✅ | 422.22 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 219.02 | ✅ | 440.50 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 202.66 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 252.86 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 159.38 | ✅ | 416.68 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 163.22 | ✅ | 353.74 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 170.36 | ✅ | 420.72 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 161.32 | ✅ | 449.70 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 194.10 | ✅ | 425.50 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 211.70 | ✅ | 491.50 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 179.00 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 196.10 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 180.68 | ✅ | 319.18 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 185.78 | ✅ | 394.36 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 187.54 | ✅ | 397.04 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 188.60 | ✅ | 499.30 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 185.34 | ✅ | 806.24 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 206.24 | ✅ | 608.24 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 185.08 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 210.22 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 201.02 | ✅ | 421.26 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 166.38 | ✅ | 370.90 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 175.92 | ✅ | 419.74 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 172.00 | ✅ | 746.18 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 170.76 | ✅ | 480.56 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 172.68 | ✅ | 576.96 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 163.70 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 211.94 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 2286.48 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 462.72 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 189.60 | ✅ | 353.76 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 159.28 | ✅ | 456.72 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 163.50 | ✅ | 529.76 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 181.08 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 157.76 | ✅ | 551.94 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 175.98 | ✅ | 430.16 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 171.52 | ✅ | 419.48 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 187.48 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 195.36 | ✅ | 359.16 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 177.90 | ✅ | 495.12 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 189.20 | ✅ | 453.10 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 208.10 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 200.16 | ✅ | 372.04 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 197.90 | ✅ | 401.16 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 182.42 | ✅ | 907.94 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 207.56 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4922.76 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 943.00 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 185.42 | ✅ | 352.72 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 203.40 | ✅ | 418.54 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 166.04 | ✅ | 436.48 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 193.12 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 159.44 | ✅ | 429.50 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 164.96 | ✅ | 546.68 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 182.04 | ✅ | 478.20 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 178.18 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 175.82 | ✅ | 425.34 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 156.68 | ✅ | 349.60 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 170.66 | ✅ | 557.40 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 186.62 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 158.38 | ✅ | 474.80 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 175.20 | ✅ | 681.58 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 170.90 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 5003.24 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 845.78 | - | - |

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
| test_large_k_shapes[K_12288-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | - | - | - |
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
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4144.20 | - | - |
| test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 4969.84 |
| test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 882.06 | - | - |
| test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4110.06 | - | - |
| test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1475.76 | ✅ | 9616.58 |
| test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7600.66 | - | - |
| test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 7307.44 |
| test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1521.06 | - | - |
| test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7585.58 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 293.56 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 315.08 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 331.86 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 317.78 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even] | ✅ | 403.82 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 353.68 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor] | ✅ | 382.80 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 294.12 | ✅ | 940.84 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 391.62 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 706.54 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 782.78 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 1943.34 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 1335.76 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 1245.42 |
| test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even] | - | - | ✅ | 860.14 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 891.92 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor] | - | - | ✅ | 1434.94 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 713.62 |
| test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | - | - | ✅ | 1626.94 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 436.58 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | ✅ | 464.64 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1595.78 |
| test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 472.04 | ✅ | 3680.20 |
| test_gemm_gelu_bf16_steps_matches_overlay[M_256-K_512-N_1024] | - | - | ❌ | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_256] | - | - | ❌ | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_6144] | - | - | ❌ | - |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64] | - | - | ✅ | - |
| test_gemm_tile_options[tn16-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma32] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma32] | ✅ | - | ❌ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma64] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

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
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | 372.60 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 372.94 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 769.54 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_2] | ✅ | 769.38 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 1834.20 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 1828.38 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1000.26 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_2] | ✅ | 1002.50 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 4507.18 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_2] | ✅ | 4502.88 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1911.16 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1910.38 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 216.50 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 215.46 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 802.82 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 803.34 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 2368.82 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_2] | ✅ | 2370.66 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1256.12 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1247.36 | - | - |
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
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 165.74 | ✅ | 324.00 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 172.68 | ✅ | 430.58 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 179.30 | ✅ | 505.26 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 152.14 | ✅ | 418.50 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 180.82 | ✅ | 821.00 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 199.76 | ✅ | 382.90 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 204.82 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 214.86 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 158.18 | ✅ | 420.70 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 167.40 | ✅ | 444.74 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 193.18 | ✅ | 515.88 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 142.76 | ✅ | 859.28 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 156.38 | ✅ | 536.20 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 174.60 | ✅ | 538.04 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 174.48 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 210.74 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 197.20 | ✅ | 413.72 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 223.34 | ✅ | 407.06 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 155.70 | ✅ | 891.40 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 164.52 | ✅ | 457.02 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 180.54 | ✅ | 464.84 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 180.60 | ✅ | 521.92 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 169.40 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 226.36 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 158.58 | ✅ | 402.94 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 153.32 | ✅ | 764.16 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 160.56 | ✅ | 403.66 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 148.30 | ✅ | 509.50 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 155.78 | ✅ | 738.08 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 174.32 | ✅ | 599.70 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 203.34 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 206.58 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3612.12 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 653.24 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 18864.42 | - | - |
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2294.46 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 217.06 | ✅ | 630.94 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 245.74 | ✅ | 577.38 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47018.40 | ✅ | 81202.12 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-partition_N_1] | ✅ | 119555.96 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27571.08 | ✅ | 18911.28 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-partition_N_1] | ✅ | 6798.52 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-partition_N_1] | ✅ | 8417.80 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7754.80 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93355.38 | ✅ | 92210.58 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100912.82 | ✅ | 92772.96 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 107494.44 | ✅ | 73550.40 |
| test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 36981.94 | - | - |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1223.86 | ✅ | 2638.88 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 1119.66 | ✅ | 2827.84 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1121.26 | ✅ | 2146.10 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3563.16 | ✅ | 6224.88 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 3938.02 | ✅ | 7705.56 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3911.26 | ✅ | 6015.34 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93113.98 | ✅ | 98423.04 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100734.18 | ✅ | 99243.18 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 106554.90 | ✅ | 75164.78 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2262.64 | ✅ | 4829.24 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3679.44 | ✅ | 7141.20 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1713.12 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 184.10 | ✅ | 385.52 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2669.72 | ✅ | 9280.30 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1379.64 | ✅ | 5320.70 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 808.70 | ✅ | 3540.58 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 849.78 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2770.36 | ✅ | 9594.66 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1374.86 | ✅ | 5676.58 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 852.14 | ✅ | 3838.70 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 770.88 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 489.28 | ✅ | 3560.40 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 348.74 | ✅ | 768.06 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 241.86 | ✅ | 642.72 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 517.66 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 1016.54 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 249.06 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 291.36 | ✅ | 1322.14 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 170.02 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2721.64 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2752.84 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 179.46 | ✅ | 667.96 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 191.88 | ✅ | 473.74 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 188.22 | ✅ | 480.62 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 173.86 | ✅ | 468.18 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 196.16 | ✅ | 445.30 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 193.80 | ✅ | 446.54 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 211.86 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 260.14 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 172.52 | ✅ | 408.40 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 193.14 | ✅ | 410.24 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 172.20 | ✅ | 519.06 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 178.00 | ✅ | 365.26 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 183.60 | ✅ | 426.82 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 180.90 | ✅ | 454.32 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 218.76 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 270.16 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 173.60 | ✅ | 413.62 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 212.60 | ✅ | 608.26 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 198.42 | ✅ | 694.92 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 179.84 | ✅ | 373.94 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 168.80 | ✅ | 395.46 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 177.14 | ✅ | 510.44 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 194.74 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 224.28 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 160.88 | ✅ | 370.24 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 168.02 | ✅ | 371.84 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 169.76 | ✅ | 424.56 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 192.56 | ✅ | 536.10 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 196.56 | ✅ | 451.78 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 192.12 | ✅ | 538.22 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 203.28 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 259.56 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3489.02 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 705.06 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 183.68 | ✅ | 352.38 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 170.28 | ✅ | 413.30 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 158.82 | ✅ | 394.24 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 180.90 | ✅ | 426.66 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 196.70 | ✅ | 448.54 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 191.86 | ✅ | 511.90 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 186.70 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 221.52 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 168.16 | ✅ | 398.62 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 187.48 | ✅ | 310.00 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 220.18 | ✅ | 362.48 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 175.90 | ✅ | 407.10 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 171.70 | ✅ | 401.42 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 160.38 | ✅ | 414.18 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 187.42 | ✅ | 424.30 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 169.96 | ✅ | 542.48 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 189.12 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 201.60 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 177.12 | ✅ | 360.02 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 167.62 | ✅ | 395.36 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 178.10 | ✅ | 446.56 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 188.94 | ✅ | 440.14 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 161.48 | ✅ | 944.38 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 196.76 | ✅ | 485.56 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 177.68 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 208.74 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 158.62 | ✅ | 527.02 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 159.96 | ✅ | 442.76 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 157.04 | ✅ | 439.64 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 160.06 | ✅ | 452.46 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 180.86 | ✅ | 451.18 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 181.42 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 218.98 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 2892.00 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 667.66 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 158.94 | ✅ | 393.92 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 186.56 | ✅ | 322.38 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 216.58 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 206.38 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 143.78 | ✅ | 694.50 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 155.38 | ✅ | 291.38 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 167.04 | ✅ | 601.80 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 182.58 | ✅ | 476.36 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 178.64 | ✅ | 491.74 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 181.92 | ✅ | 378.44 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 176.28 | ✅ | 496.08 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 182.12 | ✅ | 466.88 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 199.96 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 191.36 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 177.68 | ✅ | 548.10 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 180.70 | ✅ | 498.44 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 170.64 | ✅ | 682.02 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 148.16 | ✅ | 360.86 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 244.94 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 227.12 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 158.56 | ✅ | 356.50 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 156.24 | ✅ | 428.86 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 157.24 | ✅ | 397.68 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 147.64 | ✅ | 403.34 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 172.06 | ✅ | 454.90 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 203.54 | ✅ | 440.42 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 176.80 | ✅ | 765.06 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 186.16 | ✅ | 417.92 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 182.00 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 190.50 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 176.38 | ✅ | 525.50 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 209.40 | ✅ | 482.96 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 188.60 | ✅ | 325.34 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 191.06 | ✅ | 322.16 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 195.54 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 190.06 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 145.94 | ✅ | 425.08 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 163.94 | ✅ | 421.26 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 178.10 | ✅ | 343.66 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 158.18 | ✅ | 742.64 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 212.40 | ✅ | 374.08 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 174.42 | ✅ | 337.12 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 180.90 | ✅ | 482.92 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 180.46 | ✅ | 435.70 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 178.06 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 193.20 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 228.18 | ✅ | 473.90 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 164.40 | ✅ | 548.84 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 148.98 | ✅ | 375.58 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 165.76 | ✅ | 432.46 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 210.90 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 189.16 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 184.50 | ✅ | 393.24 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 169.50 | ✅ | 391.72 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 168.34 | ✅ | 490.92 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 160.34 | ✅ | 385.92 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 173.04 | ✅ | 456.88 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 165.32 | ✅ | 505.20 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 155.48 | ✅ | 488.84 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 219.64 | ✅ | 486.50 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 180.12 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 194.48 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 190.86 | ✅ | 482.46 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 174.96 | ✅ | 469.30 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 780.64 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 2918.70 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 18503.10 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 17716.20 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 154589.42 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 150.84 | ✅ | 291.48 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 187.70 | ✅ | 333.20 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 224.10 | ✅ | 524.54 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 171.82 | ✅ | 380.72 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 208.84 | ✅ | 484.88 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 187.68 | ✅ | 640.34 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 209.26 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 218.48 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 161.40 | ✅ | 532.58 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 165.94 | ✅ | 459.44 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 192.48 | ✅ | 375.82 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 166.60 | ✅ | 335.24 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 175.14 | ✅ | 407.14 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 193.20 | ✅ | 583.78 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 187.10 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 231.94 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 157.74 | ✅ | 719.94 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 152.40 | ✅ | 472.80 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 151.08 | ✅ | 840.72 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 154.28 | ✅ | 421.96 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 167.92 | ✅ | 546.64 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 181.82 | ✅ | 544.96 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 180.44 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 206.86 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 202.28 | ✅ | 440.40 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 163.02 | ✅ | 646.28 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 171.08 | ✅ | 506.22 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 152.24 | ✅ | 507.46 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 171.72 | ✅ | 475.56 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 182.86 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 213.24 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3169.14 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 665.76 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 161.90 | ✅ | 362.30 |
| test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None] | ✅ | 175.84 | ✅ | 353.38 |
| test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64] | ✅ | 823.08 | ✅ | 3478.60 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 160.52 | ✅ | 382.36 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 153.24 | ✅ | 257.46 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 148.00 | ✅ | 396.72 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 150.10 | ✅ | 353.14 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 153.48 | ✅ | 446.70 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 146.36 | ✅ | 462.54 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 148.76 | ✅ | 320.40 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 147.54 | ✅ | 357.58 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 158.28 | ✅ | 437.22 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 146.18 | ✅ | 589.10 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 146.54 | ✅ | 757.88 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 181.10 | ✅ | 430.70 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 190.44 | ✅ | 500.38 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 215.00 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 179.62 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 208.32 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 225.20 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 172.40 | ✅ | 402.80 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 151.20 | ✅ | 313.26 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 176.60 | ✅ | 371.76 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 150.38 | ✅ | 348.50 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 192.16 | ✅ | 366.74 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 152.94 | ✅ | 425.14 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 208.60 | ✅ | 396.60 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 172.74 | ✅ | 422.84 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 162.52 | ✅ | 446.42 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 165.62 | ✅ | 726.98 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 163.74 | ✅ | 497.64 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 220.94 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 176.04 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 196.94 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 198.66 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 151.42 | ✅ | 348.32 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 166.84 | ✅ | 496.72 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 156.34 | ✅ | 609.72 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 184.30 | ✅ | 701.18 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 161.62 | ✅ | 282.24 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 180.60 | ✅ | 703.66 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 184.22 | ✅ | 418.60 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 170.32 | ✅ | 534.62 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 178.26 | ✅ | 393.96 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 169.58 | ✅ | 508.94 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 184.50 | ✅ | 484.44 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 230.14 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 182.32 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 217.28 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 208.46 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 175.00 | ✅ | 323.24 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 179.76 | ✅ | 371.52 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 153.94 | ✅ | 418.32 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 157.50 | ✅ | 413.20 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 159.70 | ✅ | 361.28 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 164.10 | ✅ | 471.72 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 160.80 | ✅ | 467.28 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 170.92 | ✅ | 411.70 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 157.34 | ✅ | 501.76 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 188.32 | ✅ | 585.34 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 200.48 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 173.04 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 193.74 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 199.28 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3092.32 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 3446.28 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 738.00 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 619.28 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 174.54 | ✅ | 386.48 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 174.78 | ✅ | 330.96 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 198.06 | ✅ | 683.48 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 172.94 | ✅ | 375.36 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 181.24 | ✅ | 740.06 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 168.96 | ✅ | 381.08 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 203.32 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 220.02 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 188.80 | ✅ | 412.80 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 168.28 | ✅ | 450.28 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 161.94 | ✅ | 405.72 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 161.60 | ✅ | 457.44 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 187.32 | ✅ | 407.82 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 167.32 | ✅ | 372.12 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 180.54 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 179.56 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 185.92 | ✅ | 687.68 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 159.46 | ✅ | 330.26 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 178.54 | ✅ | 371.76 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 166.80 | ✅ | 625.68 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 161.50 | ✅ | 391.12 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 160.26 | ✅ | 473.50 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 195.76 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 210.74 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 161.30 | ✅ | 503.96 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 185.62 | ✅ | 355.98 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 163.92 | ✅ | 415.32 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 216.00 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 160.26 | ✅ | 316.62 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 171.88 | ✅ | 873.68 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 181.06 | ✅ | 566.10 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 222.86 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 954.02 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 306.38 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 201.06 | ✅ | 486.16 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 178.00 | ✅ | 483.10 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 191.84 | ✅ | 360.88 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 187.04 | ✅ | 390.70 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 170.62 | ✅ | 412.52 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 154.18 | ✅ | 496.42 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 186.14 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 207.50 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 162.16 | ✅ | 595.82 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 169.96 | ✅ | 421.74 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 190.80 | ✅ | 310.26 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 202.56 | ✅ | 398.88 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 183.28 | ✅ | 431.50 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 168.94 | ✅ | 763.20 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 183.30 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 205.34 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 158.30 | ✅ | 333.94 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 174.24 | ✅ | 651.98 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 181.06 | ✅ | 418.02 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 196.36 | ✅ | 732.84 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 160.96 | ✅ | 442.60 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 154.40 | ✅ | 603.22 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 187.28 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 199.94 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 179.54 | ✅ | 358.60 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 156.70 | ✅ | 335.54 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 191.48 | ✅ | 381.54 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 163.22 | ✅ | 415.98 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 215.24 | ✅ | 467.04 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 214.04 | ✅ | 813.72 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 181.18 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 236.50 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 169.30 | ✅ | 348.42 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 154.94 | ✅ | 600.86 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 154.54 | ✅ | 748.94 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 157.48 | ✅ | 331.08 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 162.12 | ✅ | 359.10 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 201.78 | ✅ | 403.14 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 209.62 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 221.28 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 165.08 | ✅ | 477.08 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 150.82 | ✅ | 380.06 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 199.86 | ✅ | 532.00 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 219.82 | ✅ | 739.66 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 206.10 | ✅ | 522.40 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 158.02 | ✅ | 597.34 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 180.46 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 229.36 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 168.08 | ✅ | 355.54 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 163.10 | ✅ | 409.30 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 180.24 | ✅ | 377.02 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 167.92 | ✅ | 345.06 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 231.48 | ✅ | 525.44 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 201.24 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 236.12 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2969.30 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 681.54 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 143.24 | ✅ | 405.04 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 149.96 | ✅ | 445.08 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 185.80 | ✅ | 464.12 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 201.36 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 164.68 | ✅ | 432.56 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 160.98 | ✅ | 383.98 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 166.60 | ✅ | 352.30 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 177.28 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 154.60 | ✅ | 441.12 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 166.44 | ✅ | 286.14 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 171.16 | ✅ | 480.96 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 178.82 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 173.12 | ✅ | 419.82 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 188.06 | ✅ | 423.66 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 186.44 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 5048.80 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 680.38 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 530.86 | ✅ | 2369.48 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 192.88 | ✅ | 384.96 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 184.50 | ✅ | 441.40 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 166.74 | ✅ | 347.40 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 494.02 | ✅ | 2394.52 |
| test_strided_copy[chunked_transfer] | ✅ | 166.64 | ✅ | 347.06 |
| test_strided_copy[contiguous] | ✅ | 143.86 | ✅ | 342.52 |
| test_strided_copy[four_channels] | ✅ | 165.14 | ✅ | 434.72 |
| test_strided_copy[kv_llama_full] | ✅ | 157.32 | ✅ | 320.70 |
| test_strided_copy[kv_slot0] | ✅ | 141.06 | ✅ | 361.28 |
| test_strided_copy[kv_slot5] | ✅ | 131.40 | ✅ | 745.06 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 198.12 | ✅ | 401.52 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 153.92 | ✅ | 470.08 |
| test_strided_copy[kv_slot_last] | ✅ | 137.66 | ✅ | 397.58 |
| test_strided_copy[two_channels] | ✅ | 162.70 | ✅ | 276.76 |
| test_strided_copy[two_channels_chunked] | ✅ | 155.96 | ✅ | 331.60 |
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
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 997.90 | ✅ | 14387.63 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1049.04 | ✅ | 13937.54 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2174.10 | ✅ | 24664.43 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2332.53 | ✅ | 24759.30 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 185.56 | ✅ | 313.70 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 183.42 | ✅ | 508.10 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 162.64 | ✅ | 413.34 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 175.46 | ✅ | 504.96 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 184.56 | ✅ | 741.92 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 195.60 | ✅ | 714.36 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 198.40 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 233.94 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 143.88 | ✅ | 280.84 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 160.54 | ✅ | 467.40 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 163.06 | ✅ | 349.38 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 161.94 | ✅ | 383.80 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 167.48 | ✅ | 366.20 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 177.18 | ✅ | 689.14 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 179.18 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 215.20 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 147.12 | ✅ | 334.72 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 191.54 | ✅ | 445.40 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 176.42 | ✅ | 484.10 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 172.10 | ✅ | 318.96 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 156.00 | ✅ | 497.78 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 171.12 | ✅ | 488.68 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 164.96 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 218.48 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 156.38 | ✅ | 347.02 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 185.88 | ✅ | 446.24 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 188.50 | ✅ | 547.74 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 176.22 | ✅ | 562.92 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 206.44 | ✅ | 781.02 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 181.24 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 243.00 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3445.82 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 694.68 | - | - |

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
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 218.26 | ✅ | 1133.96 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 227.96 | ✅ | 1749.02 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 247.80 | ✅ | 713.88 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 251.22 | ✅ | 723.94 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 275.34 | ✅ | 1027.32 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 275.98 | ✅ | 1085.90 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 282.98 | ✅ | 2200.14 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 252.68 | ✅ | 1318.88 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 249.24 | ✅ | 695.32 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 244.50 | ✅ | 1269.22 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 371.38 | ✅ | 1414.94 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 356.30 | ✅ | 1356.46 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 352.56 | ✅ | 1317.20 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 327.96 | ✅ | 1880.36 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 336.58 | ✅ | 1284.86 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 318.90 | ✅ | 1224.38 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 323.26 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 328.04 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 197.44 | ✅ | 1233.48 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 198.50 | ✅ | 597.50 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 265.18 | ✅ | 1213.78 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 200.30 | ✅ | 559.32 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 170.64 | ✅ | 345.58 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 177.44 | ✅ | 449.56 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 170.84 | ✅ | 359.26 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 168.24 | ✅ | 673.56 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 183.00 | ✅ | 427.16 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 165.06 | ✅ | 447.46 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 192.72 | ✅ | 398.24 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 177.02 | ✅ | 455.04 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 165.04 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 169.36 | ✅ | 439.04 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3665.08 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 931.94 | - | - |

</details>

