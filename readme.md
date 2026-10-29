# IRON - CI Summary

## Small

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_one_xclbin_serves_every_shape[test_one_xclbin_serves_every_shape] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[test_output_feeds_gemm_unchanged] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[npu1-M_256-K_512-N_128-epilogue_none-rounding_conv_even] | - | - | ✅ | 82.35 |
| test_gemm[npu1-M_256-K_512-N_256-epilogue_none-rounding_conv_even] | - | - | ✅ | 84.98 |
| test_gemm[npu1-M_256-K_512-N_320-epilogue_none-rounding_conv_even] | - | - | ✅ | 129.70 |
| test_gemm[npu1-M_256-K_512-N_512-epilogue_gelu-rounding_conv_even] | - | - | ✅ | 140.71 |
| test_gemm[npu1-M_256-K_512-N_512-epilogue_none-rounding_floor] | - | - | ✅ | 140.38 |
| test_gemm[npu1-M_256-K_512-N_512-epilogue_silu-rounding_conv_even] | - | - | ✅ | 147.31 |
| test_gemm[npu1-M_256-K_512-N_64-epilogue_none-rounding_conv_even] | - | - | ✅ | 81.65 |
| test_gemm[npu2-M_2048-K_1024-N_16-epilogue_none-rounding_conv_even] | ✅ | 120.62 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_gelu-rounding_conv_even] | ✅ | 78.21 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_none-rounding_conv_even] | ✅ | 70.06 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_none-rounding_floor] | ✅ | 76.88 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_silu-rounding_conv_even] | ✅ | 75.79 | - | - |
| test_gemm[npu2-M_256-K_512-N_128-epilogue_none-rounding_conv_even] | ✅ | 46.69 | - | - |
| test_gemm[npu2-M_256-K_512-N_1536-epilogue_none-rounding_conv_even] | ✅ | 83.30 | - | - |
| test_gemm_b_col_maj[npu1-resident-high] | - | - | ✅ | 85.58 |
| test_gemm_b_col_maj[npu1-streamed-high] | - | - | ✅ | 660.21 |
| test_gemm_b_col_maj[npu1-tables-linked-high] | - | - | ✅ | 92.76 |
| test_gemm_b_col_maj[npu1-tn128-high] | - | - | ✅ | 154.82 |
| test_gemm_b_col_maj[npu1-tn16-high] | - | - | ✅ | 82.84 |
| test_gemm_b_col_maj[npu1-tn32-high] | - | - | ✅ | 64.50 |
| test_gemm_b_col_maj[npu1-trailing-col-high] | - | - | ✅ | 106.79 |
| test_gemm_b_col_maj[npu2-resident-high] | ✅ | 105.68 | - | - |
| test_gemm_b_col_maj[npu2-resident-medium] | ✅ | 61.30 | - | - |
| test_gemm_b_col_maj[npu2-streamed-high] | ✅ | 1245.59 | - | - |
| test_gemm_b_col_maj[npu2-streamed-medium] | ✅ | 298.94 | - | - |
| test_gemm_b_col_maj[npu2-tables-linked-high] | ✅ | 107.85 | - | - |
| test_gemm_b_col_maj[npu2-tables-linked-medium] | ✅ | 58.93 | - | - |
| test_gemm_b_col_maj[npu2-tn128-high] | ✅ | 175.39 | - | - |
| test_gemm_b_col_maj[npu2-tn128-medium] | ✅ | 80.22 | - | - |
| test_gemm_b_col_maj[npu2-tn16-high] | ✅ | 58.79 | - | - |
| test_gemm_b_col_maj[npu2-tn16-medium] | ✅ | 43.25 | - | - |
| test_gemm_b_col_maj[npu2-tn32-high] | ✅ | 82.07 | - | - |
| test_gemm_b_col_maj[npu2-tn32-medium] | ✅ | 49.66 | - | - |
| test_gemm_b_col_maj[npu2-trailing-col-high] | ✅ | 142.98 | - | - |
| test_gemm_b_col_maj[npu2-trailing-col-medium] | ✅ | 68.87 | - | - |
| test_gemm_k_slices[npu1-default] | - | - | ✅ | - |
| test_gemm_k_slices[npu2-default] | ✅ | - | - | - |
| test_gemm_k_tile[K_256] | ✅ | - | ✅ | - |
| test_gemm_k_tile[K_768] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_16-tile_n_16-k_tile_16-ct_k_16-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_16-tile_n_16-k_tile_16-ct_k_16-medium] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_512-tile_n_64-k_tile_128-ct_k_128-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_512-tile_n_64-k_tile_128-ct_k_128-medium] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_64-tile_n_32-k_tile_64-ct_k_32-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_64-tile_n_32-k_tile_64-ct_k_32-medium] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_96-tile_n_32-k_tile_96-ct_k_32-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_96-tile_n_32-k_tile_96-ct_k_32-medium] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[test_gemm_split_leg_bounds_runs] | ✅ | - | ✅ | - |
| test_gemm_tile_options[npu1-tn128-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn16-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn32-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn64-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu2-tn128-default] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn16-default] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn32-default] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn64-default] | ✅ | - | - | - |
| test_gemm_without_activations[M_256-K_512-N_256] | ✅ | 52.28 | ✅ | 93.33 |
| test_gemm_without_activations[M_512-K_1024-N_512] | ✅ | 79.97 | ✅ | 288.16 |
| test_one_xclbin_serves_every_shape[test_one_xclbin_serves_every_shape] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/layer</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_types_take_turns[test_layer_types_take_turns] | ✅ | - | - | - |
| test_matches_reference[gemma4_e2b-global-5] | ✅ | 620.91 | - | - |
| test_matches_reference[gemma4_e2b-global-700] | ✅ | 723.90 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-37] | ✅ | 872.08 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-700] | ✅ | 937.57 | - | - |
| test_matches_reference[gemma4_e2b-swa-1023] | ✅ | 549.72 | - | - |
| test_matches_reference[gemma4_e2b-swa-37] | ✅ | 537.37 | - | - |
| test_matches_reference[gemma4_e2b-swa-511] | ✅ | 560.76 | - | - |
| test_matches_reference[gemma4_e2b-swa-512] | ✅ | 543.30 | - | - |
| test_matches_reference[gemma4_e2b-swa-700] | ✅ | 562.02 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-1023] | ✅ | 803.04 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-37] | ✅ | 794.31 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-511] | ✅ | 806.45 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-512] | ✅ | 814.52 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-700] | ✅ | 810.00 | - | - |
| test_refuses_unservable_contexts[layer_type_global-context_len_-1-max_l_1024-match_context_len must be >= 0] | ✅ | - | - | - |
| test_refuses_unservable_contexts[layer_type_global-context_len_1024-max_l_1024-match_context_len must be below max_l] | ✅ | - | - | - |
| test_refuses_unservable_contexts[layer_type_swa-context_len_37-max_l_65536-match_max_l exceeds 32768] | ✅ | - | - | - |
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
| test_projection_matches_reference[dim_1536] | ✅ | - | - | - |
| test_projection_matches_reference[dim_2560] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/prefill_attn</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | 271.60 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 271.93 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 657.54 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 953.03 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1720.47 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 5446.66 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1468.30 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 112.97 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 113.86 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 678.11 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 1451.72 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1102.88 | - | - |
| test_one_image_serves_every_range[kind_attn] | ✅ | - | - | - |
| test_one_image_serves_every_range[kind_swa] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_-128-L_end_256-max_l_1024-match_L_begin must be >= 0] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_0-L_end_200-max_l_1024-match_L_end must be a multiple of 128] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_0-L_end_256-max_l_2048-match_max_l exceeds max_context] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_0-L_end_512-max_l_256-match_slice stop exceeds the dimension] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_64-L_end_256-max_l_1024-match_L_begin must be a multiple of 128] | ✅ | - | - | - |

</details>

<details>
<summary>iron/tests/common</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| TestLlama::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks] | ✅ | - | ✅ | - |
| TestLlama::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token] | ✅ | - | ✅ | - |
| TestLlama::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves] | ✅ | - | ✅ | - |
| TestLlama::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference] | ✅ | - | ✅ | - |
| TestLlama::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic] | ✅ | - | ✅ | - |
| TestLlama::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches] | ✅ | - | ✅ | - |
| test_a_block_float_tile_is_sized_by_its_blocks[test_a_block_float_tile_is_sized_by_its_blocks] | ✅ | - | ✅ | - |
| test_a_body_of_args_with_no_signature_is_refused_as_its_class_is_made[test_a_body_of_args_with_no_signature_is_refused_as_its_class_is_made] | ✅ | - | ✅ | - |
| test_a_bound_is_refused_where_no_extent_takes_it[test_a_bound_is_refused_where_no_extent_takes_it] | ✅ | - | ✅ | - |
| test_a_bound_on_one_side_of_a_copy_holds_the_other[test_a_bound_on_one_side_of_a_copy_holds_the_other] | ✅ | - | ✅ | - |
| test_a_bound_travels_through_reshape_and_transpose[test_a_bound_travels_through_reshape_and_transpose] | ✅ | - | ✅ | - |
| test_a_bound_value_is_its_member_on_the_instance[test_a_bound_value_is_its_member_on_the_instance] | ✅ | - | ✅ | - |
| test_a_bound_value_survives_tuning[test_a_bound_value_survives_tuning] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_refuses_a_call_with_no_rows[test_a_bounded_flm_gemm_refuses_a_call_with_no_rows] | ✅ | - | ✅ | - |
| test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin[test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin] | ✅ | - | ✅ | - |
| test_a_bounded_operand_binds_the_extent_and_what_derives_from_it[test_a_bounded_operand_binds_the_extent_and_what_derives_from_it] | ✅ | - | ✅ | - |
| test_a_bounded_operand_goes_round_robin_over_the_lanes[test_a_bounded_operand_goes_round_robin_over_the_lanes] | ✅ | - | ✅ | - |
| test_a_bounded_operand_makes_the_trip_count_per_call[test_a_bounded_operand_makes_the_trip_count_per_call] | ✅ | - | ✅ | - |
| test_a_bounded_rope_lane_takes_whole_positions_and_their_angles[test_a_bounded_rope_lane_takes_whole_positions_and_their_angles] | ✅ | - | ✅ | - |
| test_a_bounded_step_ends_no_command[test_a_bounded_step_ends_no_command] | ✅ | - | ✅ | - |
| test_a_bounded_view_of_a_state_is_its_rows_this_call[test_a_bounded_view_of_a_state_is_its_rows_this_call] | ✅ | - | ✅ | - |
| test_a_call_skips_the_commands_its_values_leave_without_work[test_a_call_skips_the_commands_its_values_leave_without_work] | ✅ | - | ✅ | - |
| test_a_called_graph_records_into_its_caller[test_a_called_graph_records_into_its_caller] | ✅ | - | ✅ | - |
| test_a_called_graph_takes_every_value_and_carries_none[test_a_called_graph_takes_every_value_and_carries_none] | ✅ | - | ✅ | - |
| test_a_called_graph_writes_a_given_output_bounded_by_its_callers_value[test_a_called_graph_writes_a_given_output_bounded_by_its_callers_value] | ✅ | - | ✅ | - |
| test_a_caller_bounds_its_rows[test_a_caller_bounds_its_rows] | ✅ | - | ✅ | - |
| test_a_caller_records_and_bounds_it[test_a_caller_records_and_bounds_it] | ✅ | - | ✅ | - |
| test_a_carried_handle_may_also_be_returned[test_a_carried_handle_may_also_be_returned] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Copy-contiguous] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Emit-one_carried] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[PatchPositions-rows_2304-out_height_768-out_width_768] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ResampleTaps-in_size_17-out_size_1008] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Sample-small] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[flm.DequantBFP-K_512-N_128] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[flm.LMHead-dim_1536-vocab_4096-softcap_30.0] | ✅ | - | ✅ | - |
| test_a_causal_model_s_versions_and_signature[test_a_causal_model_s_versions_and_signature] | ✅ | - | ✅ | - |
| test_a_channel_count_no_column_fits_adds_no_grid[test_a_channel_count_no_column_fits_adds_no_grid] | ✅ | - | ✅ | - |
| test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_<|bos|>] | ✅ | - | ✅ | - |
| test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_] | ✅ | - | ✅ | - |
| test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_{{ bos_token }}] | ✅ | - | ✅ | - |
| test_a_chat_template_jinja_file_is_read_and_may_call_strftime_now[test_a_chat_template_jinja_file_is_read_and_may_call_strftime_now] | ✅ | - | ✅ | - |
| test_a_chat_template_jinja_file_is_read_over_tokenizer_config_s[test_a_chat_template_jinja_file_is_read_over_tokenizer_config_s] | ✅ | - | ✅ | - |
| test_a_chat_template_s_raise_exception_raises_its_message[test_a_chat_template_s_raise_exception_raises_its_message] | ✅ | - | ✅ | - |
| test_a_chat_template_writes_tokenizer_config_s_bos_token[given_<s>-written_<s>] | ✅ | - | ✅ | - |
| test_a_chat_template_writes_tokenizer_config_s_bos_token[given_None-written_] | ✅ | - | ✅ | - |
| test_a_chat_template_writes_tokenizer_config_s_bos_token[given_{'content': '<s>'}-written_<s>] | ✅ | - | ✅ | - |
| test_a_checkpoint_s_golden_is_refused_once_it_changes[change_config] | ✅ | - | ✅ | - |
| test_a_checkpoint_s_golden_is_refused_once_it_changes[change_first weight] | ✅ | - | ✅ | - |
| test_a_checkpoint_s_golden_is_refused_once_it_changes[change_last weight] | ✅ | - | ✅ | - |
| test_a_column_major_product_is_read_as_stored_by_the_next_reference[test_a_column_major_product_is_read_as_stored_by_the_next_reference] | ✅ | - | ✅ | - |
| test_a_command_reads_at_most_a_scratchpads_words[test_a_command_reads_at_most_a_scratchpads_words] | ✅ | - | ✅ | - |
| test_a_config_whose_application_states_no_precision_is_refused[test_a_config_whose_application_states_no_precision_is_refused] | ✅ | - | ✅ | - |
| test_a_context_no_chunk_divides_is_allocated_exactly[test_a_context_no_chunk_divides_is_allocated_exactly] | ✅ | - | ✅ | - |
| test_a_context_no_chunk_divides_runs_to_its_last_position[test_a_context_no_chunk_divides_runs_to_its_last_position] | ✅ | - | ✅ | - |
| test_a_decoder_without_rope_places_its_positions_through_the_hook[test_a_decoder_without_rope_places_its_positions_through_the_hook] | ✅ | - | ✅ | - |
| test_a_derive_that_fails_for_another_reason_than_resolution_raises[test_a_derive_that_fails_for_another_reason_than_resolution_raises] | ✅ | - | ✅ | - |
| test_a_derived_value_is_written_once_per_build[test_a_derived_value_is_written_once_per_build] | ✅ | - | ✅ | - |
| test_a_design_is_keyed_by_what_it_builds[test_a_design_is_keyed_by_what_it_builds] | ✅ | - | ✅ | - |
| test_a_difference_is_one_axpy_and_a_number_less_a_handle_two_steps[test_a_difference_is_one_axpy_and_a_number_less_a_handle_two_steps] | ✅ | - | ✅ | - |
| test_a_fetch_refuses_plain_http_and_a_download_of_another_digest[test_a_fetch_refuses_plain_http_and_a_download_of_another_digest] | ✅ | - | ✅ | - |
| test_a_fetch_reuses_a_file_of_the_pinned_digest[test_a_fetch_reuses_a_file_of_the_pinned_digest] | ✅ | - | ✅ | - |
| test_a_field_added_at_its_default_keeps_the_fingerprint[test_a_field_added_at_its_default_keeps_the_fingerprint] | ✅ | - | ✅ | - |
| test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known[test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known] | ✅ | - | ✅ | - |
| test_a_file_of_other_inputs_is_refused_and_rerecorded[test_a_file_of_other_inputs_is_refused_and_rerecorded] | ✅ | - | ✅ | - |
| test_a_float32_product_is_not_rounded_to_its_inputs_dtype[test_a_float32_product_is_not_rounded_to_its_inputs_dtype] | ✅ | - | ✅ | - |
| test_a_forced_xclbin_is_derived_and_says_why[test_a_forced_xclbin_is_derived_and_says_why] | ✅ | - | ✅ | - |
| test_a_full_elf_ends_a_command_at_a_host_step[test_a_full_elf_ends_a_command_at_a_host_step] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_(array([0, 1]), slice(0, 4, None))-match_whole of every axis] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[ 0 64]-match_gathering] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[-65]-match_gathering] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[0. 1.]-match_1-D integer array] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[[0 1]]-match_1-D integer array] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[]-match_gathering] | ✅ | - | ✅ | - |
| test_a_generation_block_renders_its_body[test_a_generation_block_renders_its_body] | ✅ | - | ✅ | - |
| test_a_generation_s_timings_are_the_model_s_stats[test_a_generation_s_timings_are_the_model_s_stats] | ✅ | - | ✅ | - |
| test_a_given_output_of_another_rank_is_refused_unless_declared_flat[test_a_given_output_of_another_rank_is_refused_unless_declared_flat] | ✅ | - | ✅ | - |
| test_a_graph_carries_its_next_values[test_a_graph_carries_its_next_values] | ✅ | - | ✅ | - |
| test_a_graph_carries_its_profile[test_a_graph_carries_its_profile] | ✅ | - | ✅ | - |
| test_a_graph_names_its_inputs_and_values_in_signature[count_2] | ✅ | - | ✅ | - |
| test_a_graph_names_its_inputs_and_values_in_signature[count_3] | ✅ | - | ✅ | - |
| test_a_graph_reads_as_its_name_and_recorded_shapes[test_a_graph_reads_as_its_name_and_recorded_shapes] | ✅ | - | ✅ | - |
| test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps[test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps] | ✅ | - | ✅ | - |
| test_a_held_array_is_viewed_in_the_body_under_its_own_path[test_a_held_array_is_viewed_in_the_body_under_its_own_path] | ✅ | - | ✅ | - |
| test_a_held_array_that_is_no_param_is_refused[test_a_held_array_that_is_no_param_is_refused] | ✅ | - | ✅ | - |
| test_a_host_step_is_recorded_before_the_next_step[test_a_host_step_is_recorded_before_the_next_step] | ✅ | - | ✅ | - |
| test_a_host_step_runs_between_the_device_s_steps[each_step] | ✅ | - | ✅ | - |
| test_a_host_step_runs_between_the_device_s_steps[full_elf] | ✅ | - | - | - |
| test_a_host_write_to_a_state_a_step_writes_is_refused[test_a_host_write_to_a_state_a_step_writes_is_refused] | ✅ | - | ✅ | - |
| test_a_host_write_to_other_than_a_state_is_refused[test_a_host_write_to_other_than_a_state_is_refused] | ✅ | - | ✅ | - |
| test_a_lane_pins_to_a_channel_moving_its_way[test_a_lane_pins_to_a_channel_moving_its_way] | ✅ | - | ✅ | - |
| test_a_layer_norm_s_eps_is_its_kernel_s[test_a_layer_norm_s_eps_is_its_kernel_s] | ✅ | - | ✅ | - |
| test_a_matvec_whose_columns_are_given_resolves_with_no_device[test_a_matvec_whose_columns_are_given_resolves_with_no_device] | ✅ | - | ✅ | - |
| test_a_mixed_call_places_the_soft_tokens_and_attends_over_them[soft_1] | ✅ | - | ✅ | - |
| test_a_mixed_call_places_the_soft_tokens_and_attends_over_them[soft_5] | ✅ | - | ✅ | - |
| test_a_model_fits_its_context_with_no_device_bound[test_a_model_fits_its_context_with_no_device_bound] | ✅ | - | ✅ | - |
| test_a_model_runs_only_the_versions_it_loaded[test_a_model_runs_only_the_versions_it_loaded] | ✅ | - | ✅ | - |
| test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given[test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given] | ✅ | - | ✅ | - |
| test_a_norm_is_its_kernel_weighted_if_given_then_any_bias[layer_weighted_biased] | ✅ | - | ✅ | - |
| test_a_norm_is_its_kernel_weighted_if_given_then_any_bias[rms_unweighted] | ✅ | - | ✅ | - |
| test_a_norm_over_another_axis_than_the_last_is_refused[layer] | ✅ | - | ✅ | - |
| test_a_norm_over_another_axis_than_the_last_is_refused[rms] | ✅ | - | ✅ | - |
| test_a_number_on_either_side_is_a_row_of_it[test_a_number_on_either_side_is_a_row_of_it] | ✅ | - | ✅ | - |
| test_a_numpy_function_on_a_handle_says_what_to_call[test_a_numpy_function_on_a_handle_says_what_to_call] | ✅ | - | ✅ | - |
| test_a_padded_pattern_does_not_fit_a_shim_descriptor[test_a_padded_pattern_does_not_fit_a_shim_descriptor] | ✅ | - | ✅ | - |
| test_a_per_call_length_counts_a_dimension_by_a_word[no_dimension_of_the_unit] | ✅ | - | ✅ | - |
| test_a_per_call_length_counts_a_dimension_by_a_word[not_a_word] | ✅ | - | ✅ | - |
| test_a_per_call_value_cannot_steer_the_record[test_a_per_call_value_cannot_steer_the_record] | ✅ | - | ✅ | - |
| test_a_per_call_value_s_default_is_given_when_left_out[test_a_per_call_value_s_default_is_given_when_left_out] | ✅ | - | ✅ | - |
| test_a_per_layer_slice_is_drawn_in_its_layer[test_a_per_layer_slice_is_drawn_in_its_layer] | ✅ | - | ✅ | - |
| test_a_positional_operand_past_the_inputs_is_an_output_not_an_optional_one[test_a_positional_operand_past_the_inputs_is_an_output_not_an_optional_one] | ✅ | - | ✅ | - |
| test_a_profile_fills_the_tunables_a_call_leaves_open[test_a_profile_fills_the_tunables_a_call_leaves_open] | ✅ | - | ✅ | - |
| test_a_profile_is_checked_as_it_is_written_and_as_it_is_read[test_a_profile_is_checked_as_it_is_written_and_as_it_is_read] | ✅ | - | ✅ | - |
| test_a_prompt_begins_as_the_tokenizer_begins_a_text[gemma-4-e2b-it] | ✅ | - | ✅ | - |
| test_a_prompt_begins_as_the_tokenizer_begins_a_text[llama3.2-1b] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_0-rows_256-inside_True] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_1-rows_44-inside_True] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_1-rows_45-inside_False] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_2-rows_1-inside_False] | ✅ | - | ✅ | - |
| test_a_recorded_graph_names_every_step_and_every_edge[test_a_recorded_graph_names_every_step_and_every_edge] | ✅ | - | ✅ | - |
| test_a_reference_only_operator_runs_its_reference_and_does_not_compile[test_a_reference_only_operator_runs_its_reference_and_does_not_compile] | ✅ | - | ✅ | - |
| test_a_reference_only_operator_takes_no_image[test_a_reference_only_operator_takes_no_image] | ✅ | - | ✅ | - |
| test_a_reference_takes_valid_rows_short_of_a_whole_line[n_128] | ✅ | - | ✅ | - |
| test_a_reference_takes_valid_rows_short_of_a_whole_line[n_1] | ✅ | - | ✅ | - |
| test_a_reference_takes_valid_rows_short_of_a_whole_line[n_9] | ✅ | - | ✅ | - |
| test_a_refused_compile_restores_the_device_it_was_given_over[test_a_refused_compile_restores_the_device_it_was_given_over] | ✅ | - | ✅ | - |
| test_a_refused_step_names_the_graph_the_operator_and_the_held_path[test_a_refused_step_names_the_graph_the_operator_and_the_held_path] | ✅ | - | ✅ | - |
| test_a_refused_step_shows_an_unheld_param_as_an_array_of_its_shape[test_a_refused_step_shows_an_unheld_param_as_an_array_of_its_shape] | ✅ | - | ✅ | - |
| test_a_row_bound_needs_one_row_block_per_unit[test_a_row_bound_needs_one_row_block_per_unit] | ✅ | - | ✅ | - |
| test_a_row_sweep_splits_each_length_into_rows_of_the_tile[test_a_row_sweep_splits_each_length_into_rows_of_the_tile] | ✅ | - | ✅ | - |
| test_a_run_as_wide_as_its_axis_keeps_its_start_under_a_bound[test_a_run_as_wide_as_its_axis_keeps_its_start_under_a_bound] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[another_value] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[no_stop] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[two_per_call] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[wider_than_the_axis] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_is_its_whole_chunk_s_view[test_a_run_from_a_per_call_start_is_its_whole_chunk_s_view] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_is_written_and_read_as_numpy_does[test_a_run_from_a_per_call_start_is_written_and_read_as_numpy_does] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_takes_any_start_on_any_axis[test_a_run_from_a_per_call_start_takes_any_start_on_any_axis] | ✅ | - | ✅ | - |
| test_a_run_is_bounded_from_its_start_on_its_own_axis[test_a_run_is_bounded_from_its_start_on_its_own_axis] | ✅ | - | ✅ | - |
| test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides[test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides] | ✅ | - | ✅ | - |
| test_a_run_past_the_buffer_s_end_is_kept_inside_by_each_call[test_a_run_past_the_buffer_s_end_is_kept_inside_by_each_call] | ✅ | - | ✅ | - |
| test_a_run_that_draws_no_eos_draws_max_tokens[test_a_run_that_draws_no_eos_draws_max_tokens] | ✅ | - | ✅ | - |
| test_a_scratchpad_parameter_holds_one_word[test_a_scratchpad_parameter_holds_one_word] | ✅ | - | ✅ | - |
| test_a_shipped_image_declares_its_pins_and_parameter_block[test_a_shipped_image_declares_its_pins_and_parameter_block] | ✅ | - | ✅ | - |
| test_a_shipped_image_in_a_graph_is_refused[test_a_shipped_image_in_a_graph_is_refused] | ✅ | - | ✅ | - |
| test_a_shipped_image_runs_only_with_instructions[test_a_shipped_image_runs_only_with_instructions] | ✅ | - | ✅ | - |
| test_a_size_the_default_line_does_not_split_takes_a_narrower_one[test_a_size_the_default_line_does_not_split_takes_a_narrower_one] | ✅ | - | ✅ | - |
| test_a_sliding_window_some_layers_take_is_refused[test_a_sliding_window_some_layers_take_is_refused] | ✅ | - | ✅ | - |
| test_a_state_is_subtracted_as_it_is_added[test_a_state_is_subtracted_as_it_is_added] | ✅ | - | ✅ | - |
| test_a_state_written_by_one_step_is_pinned_and_readable[test_a_state_written_by_one_step_is_pinned_and_readable] | ✅ | - | ✅ | - |
| test_a_stream_binds_a_handle_per_lane[test_a_stream_binds_a_handle_per_lane] | ✅ | - | ✅ | - |
| test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget[test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget] | ✅ | - | ✅ | - |
| test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere[test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere] | ✅ | - | ✅ | - |
| test_a_text_only_call_runs_the_text_model_s_version[test_a_text_only_call_runs_the_text_model_s_version] | ✅ | - | ✅ | - |
| test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch[outside_-1] | ✅ | - | ✅ | - |
| test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch[outside_1024] | ✅ | - | ✅ | - |
| test_a_tower_runs_its_front_end_s_rows[test_a_tower_runs_its_front_end_s_rows] | ✅ | - | ✅ | - |
| test_a_towers_layers_are_found_under_its_prefix[test_a_towers_layers_are_found_under_its_prefix] | ✅ | - | ✅ | - |
| test_a_tunable_free_operator_takes_the_widest_split_that_leaves_whole_lines[test_a_tunable_free_operator_takes_the_widest_split_that_leaves_whole_lines] | ✅ | - | ✅ | - |
| test_a_turn_runs_from_its_first_new_token[test_a_turn_runs_from_its_first_new_token] | ✅ | - | ✅ | - |
| test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident[test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident] | ✅ | - | ✅ | - |
| test_a_value_only_a_core_reads_is_declared_on_a_full_elf[test_a_value_only_a_core_reads_is_declared_on_a_full_elf] | ✅ | - | ✅ | - |
| test_a_version_reads_none_of_the_words_its_image_writes[test_a_version_reads_none_of_the_words_its_image_writes] | ✅ | - | ✅ | - |
| test_a_version_reads_only_the_values_its_steps_read[test_a_version_reads_only_the_values_its_steps_read] | ✅ | - | ✅ | - |
| test_a_version_with_no_tensor_splits_at_a_host_step_too[test_a_version_with_no_tensor_splits_at_a_host_step_too] | ✅ | - | ✅ | - |
| test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[2, 2, 8, 2048]-strides_[0, 65536, 4096, 1]-bounded_True-match_one shim] | ✅ | - | ✅ | - |
| test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[4, 4, 4, 1024]-strides_[0, 4096, 1024, 1]-bounded_False-match_give bounds] | ✅ | - | ✅ | - |
| test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[64, 4096]-strides_[4096, 1]-bounded_True-match_one shim] | ✅ | - | ✅ | - |
| test_a_weight_given_where_an_optional_input_was_meant_is_refused[view_False] | ✅ | - | ✅ | - |
| test_a_weight_given_where_an_optional_input_was_meant_is_refused[view_True] | ✅ | - | ✅ | - |
| test_a_weight_times_a_row_is_linear_and_a_plain_matrix_is_refused[test_a_weight_times_a_row_is_linear_and_a_plain_matrix_is_refused] | ✅ | - | ✅ | - |
| test_a_whole_reshape_of_a_held_array_is_gathered_under_its_own_path[test_a_whole_reshape_of_a_held_array_is_gathered_under_its_own_path] | ✅ | - | ✅ | - |
| test_alike_instances_bound_to_different_values_are_different_designs[test_alike_instances_bound_to_different_values_are_different_designs] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[GELU-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[GELU-device_npu2] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[SiLU-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[SiLU-device_npu2] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Sigmoid-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Sigmoid-device_npu2] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Tanh-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Tanh-device_npu2] | ✅ | - | ✅ | - |
| test_an_assignment_into_a_view_is_the_copy_into_it[test_an_assignment_into_a_view_is_the_copy_into_it] | ✅ | - | ✅ | - |
| test_an_axis_is_found_through_the_branch_a_select_takes[test_an_axis_is_found_through_the_branch_a_select_takes] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_1-window_64] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_1-window_None] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_128-window_64] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_128-window_None] | ✅ | - | ✅ | - |
| test_an_encoder_places_its_positions_through_the_hook[n_128] | ✅ | - | ✅ | - |
| test_an_encoder_places_its_positions_through_the_hook[n_9] | ✅ | - | ✅ | - |
| test_an_explicit_instance_is_applied_like_the_class[test_an_explicit_instance_is_applied_like_the_class] | ✅ | - | ✅ | - |
| test_an_exported_design_replaces_the_derived_one[test_an_exported_design_replaces_the_derived_one] | ✅ | - | ✅ | - |
| test_an_extent_reads_as_its_field_until_a_graph_bounds_it[test_an_extent_reads_as_its_field_until_a_graph_bounds_it] | ✅ | - | ✅ | - |
| test_an_image_a_call_does_not_hold_is_refused[test_an_image_a_call_does_not_hold_is_refused] | ✅ | - | ✅ | - |
| test_an_index_before_a_bound_keeps_the_bound_on_its_axis[test_an_index_before_a_bound_keeps_the_bound_on_its_axis] | ✅ | - | ✅ | - |
| test_an_index_may_floor_and_a_bound_may_only_clamp[test_an_index_may_floor_and_a_bound_may_only_clamp] | ✅ | - | ✅ | - |
| test_an_input_given_as_an_output_is_refused[test_an_input_given_as_an_output_is_refused] | ✅ | - | ✅ | - |
| test_an_input_named_as_a_compile_keyword_is_refused[test_an_input_named_as_a_compile_keyword_is_refused] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[bound] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[exact] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[relative] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[relative_atol] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[relative_range] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[ulps] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[ulps_atol] | ✅ | - | ✅ | - |
| test_an_operand_declared_when_a_flag_exists_only_where_it_is_true[test_an_operand_declared_when_a_flag_exists_only_where_it_is_true] | ✅ | - | ✅ | - |
| test_an_operand_fills_only_inside_its_operators_sequence[test_an_operand_fills_only_inside_its_operators_sequence] | ✅ | - | ✅ | - |
| test_an_operand_with_a_tile_is_its_own_stream[test_an_operand_with_a_tile_is_its_own_stream] | ✅ | - | ✅ | - |
| test_an_operator_written_by_inheritance_inherits_the_sweep[test_an_operator_written_by_inheritance_inherits_the_sweep] | ✅ | - | ✅ | - |
| test_an_optional_input_gives_a_version_without_it[test_an_optional_input_gives_a_version_without_it] | ✅ | - | ✅ | - |
| test_an_unaligned_gather_computes_whole_blocks[test_an_unaligned_gather_computes_whole_blocks] | ✅ | - | ✅ | - |
| test_an_unaligned_gather_writes_no_callers_output[test_an_unaligned_gather_writes_no_callers_output] | ✅ | - | ✅ | - |
| test_an_xclbin_is_asked_for_where_a_full_elf_would_do[test_an_xclbin_is_asked_for_where_a_full_elf_would_do] | ✅ | - | ✅ | - |
| test_angles_are_the_unscaled_table_at_rope_width[test_angles_are_the_unscaled_table_at_rope_width] | ✅ | - | ✅ | - |
| test_array_sees_the_array_tier_alone[test_array_sees_the_array_tier_alone] | ✅ | - | ✅ | - |
| test_arrays_are_shared_by_array_key_and_extents_are_not[test_arrays_are_shared_by_array_key_and_extents_are_not] | ✅ | - | ✅ | - |
| test_attention_scaling_multiplies_the_whole_table_once[test_attention_scaling_multiplies_the_whole_table_once] | ✅ | - | ✅ | - |
| test_binding_two_handles_to_one_instance_is_an_error[test_binding_two_handles_to_one_instance_is_an_error] | ✅ | - | ✅ | - |
| test_buffers_resolve_shape_dtype_and_direction[test_buffers_resolve_shape_dtype_and_direction] | ✅ | - | ✅ | - |
| test_by_default_the_table_is_rope_angles_at_head_dim[test_by_default_the_table_is_rope_angles_at_head_dim] | ✅ | - | ✅ | - |
| test_call_reference_gives_an_output_only_to_a_reference_that_names_it[test_call_reference_gives_an_output_only_to_a_reference_that_names_it] | ✅ | - | ✅ | - |
| test_call_reference_pairs_buffers_by_name_not_by_order[test_call_reference_pairs_buffers_by_name_not_by_order] | ✅ | - | ✅ | - |
| test_call_reference_refuses_a_reference_that_returns_nothing[test_call_reference_refuses_a_reference_that_returns_nothing] | ✅ | - | ✅ | - |
| test_chat_messages_are_rendered_by_the_checkpoint_s_template[test_chat_messages_are_rendered_by_the_checkpoint_s_template] | ✅ | - | ✅ | - |
| test_check_takes_an_xclbin_per_step[test_check_takes_an_xclbin_per_step] | ✅ | - | ✅ | - |
| test_compatible_runs_at_construction_once_every_tunable_is_known[test_compatible_runs_at_construction_once_every_tunable_is_known] | ✅ | - | ✅ | - |
| test_concurrent_fetches_of_a_shipped_image_each_get_the_whole_file[test_concurrent_fetches_of_a_shipped_image_each_get_the_whole_file] | ✅ | - | ✅ | - |
| test_decode_step_reads_the_rope_table_at_its_own_width[test_decode_step_reads_the_rope_table_at_its_own_width] | ✅ | - | ✅ | - |
| test_default_is_a_full_elf_on_npu2[test_default_is_a_full_elf_on_npu2] | ✅ | - | ✅ | - |
| test_devices_are_named_for_their_design_not_their_step[test_devices_are_named_for_their_design_not_their_step] | ✅ | - | ✅ | - |
| test_each_gelu_is_its_operator_s_form[act_gelu-approximate_none] | ✅ | - | ✅ | - |
| test_each_gelu_is_its_operator_s_form[act_gelu_pytorch_tanh-approximate_tanh] | ✅ | - | ✅ | - |
| test_each_layer_s_steps_are_drawn_in_its_cluster[test_each_layer_s_steps_are_drawn_in_its_cluster] | ✅ | - | ✅ | - |
| test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.embedding_gemma2.model.Config'>-instance_Config(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, vocab_size=262144, hidden_size=512, num_hidden_layers=24, num_attention_heads=4, intermediate_size=2048, num_key_value_heads=2, head_dim=256, rope_theta=10000.0, layer_types=('sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention'), global_kv_groups=1, global_head_dim=512, global_rope_theta=1000000.0, sliding_window=512, ple_dim=512, embedding_dim=768, hidden_act='gelu_pytorch_tanh', mrl_dims=(768, 512, 256, 128), image_token=258880, audio_token=258881, boi=255999, eoi=258882, boa=256000, eoa=258883, max_tokens=2048, block=64)] | ✅ | - | ✅ | - |
| test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.gemma4.audio.AudioConfig'>-instance_AudioConfig(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, hidden_size=1024, num_hidden_layers=12, num_attention_heads=8, intermediate_size=4096, mels=128, subsampling_conv_channels=(128, 32), window=12, band=32, attention_logit_cap=50.0, use_clipped_linears=True, conv_kernel_size=5, residual_weight=0.5, text_dim=512, output_proj_dims=1536, sample_rate=16000, frame=320, hop=160, max_samples=480000, max_tokens=768)] | ✅ | - | ✅ | - |
| test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.gemma4.vision.VisionConfig'>-instance_VisionConfig(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, hidden_size=768, num_hidden_layers=16, num_attention_heads=12, head_dim=64, intermediate_size=3072, patch_size=16, pooling_kernel_size=3, position_embedding_size=10240, rope_theta=100.0, hidden_act='gelu_pytorch_tanh', use_clipped_linears=False, text_dim=512, image_tokens=280, patches=2560, largest=(3072, 4096), rows=256, chunk=4096, patch_columns=8)] | ✅ | - | ✅ | - |
| test_embeddinggemma_2_loads_a_layer_s_per_layer_input_flat_or_nested[test_embeddinggemma_2_loads_a_layer_s_per_layer_input_flat_or_nested] | ✅ | - | ✅ | - |
| test_equal_kernel_recipes_share_one_object_across_designs[test_equal_kernel_recipes_share_one_object_across_designs] | ✅ | - | ✅ | - |
| test_every_carried_value_is_carried_and_nothing_else[test_every_carried_value_is_carried_and_nothing_else] | ✅ | - | ✅ | - |
| test_every_declared_case_resolves_on_npu2[test_every_declared_case_resolves_on_npu2] | ✅ | - | ✅ | - |
| test_every_tolerance_says_where_its_numbers_come_from[npu1] | ✅ | - | ✅ | - |
| test_every_tolerance_says_where_its_numbers_come_from[npu2] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_AXPY] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Clamp] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Copy] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_DepthwiseConv1d] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ElementwiseAdd] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ElementwiseMul] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Emit] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GELU] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GEMM] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GEMV] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GatherWords] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Gather] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_LayerNorm] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Limbs] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Log] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_MHA] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Magnitude] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Merge] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_PatchPositions] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RMSNorm] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ReLU] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ResampleTaps] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Resample] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RoPE] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RowwiseAdd] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RowwiseMul] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Sample] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_SiLU] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Sigmoid] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Softmax] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Tanh] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.DecodeLayer] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.DequantBFP] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.LMHead] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.PrefillAttention] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.PrefillSlidingAttention] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.ProjectionGEMM] | ✅ | - | ✅ | - |
| test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks[test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks] | ✅ | - | ✅ | - |
| test_flm_gemm_declares_every_b_pool_whichever_columns_a_shape_fills[test_flm_gemm_declares_every_b_pool_whichever_columns_a_shape_fills] | ✅ | - | ✅ | - |
| test_flm_gemm_image_keeps_the_tiles_a_narrow_shape_resolves_to[test_flm_gemm_image_keeps_the_tiles_a_narrow_shape_resolves_to] | ✅ | - | ✅ | - |
| test_flm_gemm_keyword_construction_tunes_from_the_device[test_flm_gemm_keyword_construction_tunes_from_the_device] | ✅ | - | ✅ | - |
| test_flm_gemm_selects_its_activation_by_a_word[test_flm_gemm_selects_its_activation_by_a_word] | ✅ | - | ✅ | - |
| test_float_scratchpad_annotation_is_rejected[test_float_scratchpad_annotation_is_rejected] | ✅ | - | ✅ | - |
| test_from_checkpoint_draws_its_weights_at_a_seed[test_from_checkpoint_draws_its_weights_at_a_seed] | ✅ | - | ✅ | - |
| test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it[test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it] | ✅ | - | ✅ | - |
| test_from_checkpoint_names_the_keys_a_config_json_lacks[test_from_checkpoint_names_the_keys_a_config_json_lacks] | ✅ | - | ✅ | - |
| test_from_checkpoint_opens_the_tokenizer_beside_it[test_from_checkpoint_opens_the_tokenizer_beside_it] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.embedding_gemma2.model.Config] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.gemma4.audio.AudioConfig] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.gemma4.vision.VisionConfig] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.llama.model.LlamaConfig] | ✅ | - | ✅ | - |
| test_from_checkpoint_refuses_a_rope_scaling_it_builds_no_table_for[test_from_checkpoint_refuses_a_rope_scaling_it_builds_no_table_for] | ✅ | - | ✅ | - |
| test_from_checkpoint_takes_either_the_file_or_its_directory[test_from_checkpoint_takes_either_the_file_or_its_directory] | ✅ | - | ✅ | - |
| test_gathered_patches_hold_no_padding[test_gathered_patches_hold_no_padding] | ✅ | - | ✅ | - |
| test_gelu_refuses_a_form_it_has_no_kernel_for[test_gelu_refuses_a_form_it_has_no_kernel_for] | ✅ | - | ✅ | - |
| test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic[test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic] | ✅ | - | ✅ | - |
| test_gemma_s_text_layer_projects_at_highest_precision[test_gemma_s_text_layer_projects_at_highest_precision] | ✅ | - | ✅ | - |
| test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s[test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s] | ✅ | - | ✅ | - |
| test_generate_gives_text_for_text_and_ids_for_ids[test_generate_gives_text_for_text_and_ids_for_ids] | ✅ | - | ✅ | - |
| test_generation_stops_at_an_eos_and_includes_it[test_generation_stops_at_an_eos_and_includes_it] | ✅ | - | ✅ | - |
| test_head_dim_falls_back_and_max_seq_len_is_the_native_context[test_head_dim_falls_back_and_max_seq_len_is_the_native_context] | ✅ | - | ✅ | - |
| test_highest_runs_the_gemm_that_rounds_once[test_highest_runs_the_gemm_that_rounds_once] | ✅ | - | ✅ | - |
| test_identity_holds_across_processes[test_identity_holds_across_processes] | ✅ | - | ✅ | - |
| test_identity_is_what_the_text_is_a_function_of[test_identity_is_what_the_text_is_a_function_of] | ✅ | - | ✅ | - |
| test_inline_records_only_into_a_body[test_inline_records_only_into_a_body] | ✅ | - | ✅ | - |
| test_inputs_pad_with_zero_and_give_rows[test_inputs_pad_with_zero_and_give_rows] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[-1]-error_<class 'IndexError'>] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]-error_<class 'ValueError'>] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[32]-error_<class 'IndexError'>] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[]-error_<class 'ValueError'>] | ✅ | - | ✅ | - |
| test_integer_arithmetic_on_an_expression_is_an_expression[test_integer_arithmetic_on_an_expression_is_an_expression] | ✅ | - | ✅ | - |
| test_it_records_only_while_asked_and_reads_back_without_the_reference[test_it_records_only_while_asked_and_reads_back_without_the_reference] | ✅ | - | ✅ | - |
| test_its_signature_is_its_text_model_s_and_towers[test_its_signature_is_its_text_model_s_and_towers] | ✅ | - | ✅ | - |
| test_judge_names_each_output_and_refuses_a_missing_one[test_judge_names_each_output_and_refuses_a_missing_one] | ✅ | - | ✅ | - |
| test_keyword_only_parameters_must_be_annotated_as_values[test_keyword_only_parameters_must_be_annotated_as_values] | ✅ | - | ✅ | - |
| test_linear_takes_a_precision_for_any_rows_and_gemv_tunables_for_one[gemm] | ✅ | - | ✅ | - |
| test_linear_takes_a_precision_for_any_rows_and_gemv_tunables_for_one[gemv] | ✅ | - | ✅ | - |
| test_linear_takes_one_row_or_several[test_linear_takes_one_row_or_several] | ✅ | - | ✅ | - |
| test_llama_1b_from_checkpoint_is_its_published_shape[test_llama_1b_from_checkpoint_is_its_published_shape] | ✅ | - | ✅ | - |
| test_llama_decode_records_and_tunes[test_llama_decode_records_and_tunes] | ✅ | - | ✅ | - |
| test_llama_projects_at_high_from_3b_s_width_unless_given[test_llama_projects_at_high_from_3b_s_width_unless_given] | ✅ | - | ✅ | - |
| test_llama_prompt_projects_with_flm_gemm[device_npu1] | ✅ | - | ✅ | - |
| test_llama_prompt_projects_with_flm_gemm[device_npu2] | ✅ | - | ✅ | - |
| test_llama_prompt_records_over_the_same_caches[test_llama_prompt_records_over_the_same_caches] | ✅ | - | ✅ | - |
| test_log_mel_holds_to_the_extractor[test_log_mel_holds_to_the_extractor] | ✅ | - | ✅ | - |
| test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[param] | ✅ | - | ✅ | - |
| test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[state] | ✅ | - | ✅ | - |
| test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[weight] | ✅ | - | ✅ | - |
| test_mha_binds_p_times_v_at_its_own_shape[test_mha_binds_p_times_v_at_its_own_shape] | ✅ | - | ✅ | - |
| test_mha_refuses_a_sequence_pad_of_no_whole_blocks[test_mha_refuses_a_sequence_pad_of_no_whole_blocks] | ✅ | - | ✅ | - |
| test_no_column_count_resolves_when_one_column_overruns_the_shim[test_no_column_count_resolves_when_one_column_overruns_the_shim] | ✅ | - | ✅ | - |
| test_no_npu_says_how_to_compile_without_one[test_no_npu_says_how_to_compile_without_one] | ✅ | - | ✅ | - |
| test_no_sampler_is_greedy[test_no_sampler_is_greedy] | ✅ | - | ✅ | - |
| test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering[test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_bounded_flm_gemm_repeats_a_by_the_dispatch_scalar[test_on_an_xclbin_a_bounded_flm_gemm_repeats_a_by_the_dispatch_scalar] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_copy_bounded_on_its_innermost_axis_sizes_it[test_on_an_xclbin_a_copy_bounded_on_its_innermost_axis_sizes_it] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_per_call_length_sizes_the_coalesced_descriptor[five_dimensions] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_per_call_length_sizes_the_coalesced_descriptor[repeat_led] | ✅ | - | ✅ | - |
| test_on_an_xclbin_the_size_is_the_dispatch_scalar[test_on_an_xclbin_the_size_is_the_dispatch_scalar] | ✅ | - | ✅ | - |
| test_on_host_outside_a_body_is_refused[test_on_host_outside_a_body_is_refused] | ✅ | - | ✅ | - |
| test_one_configuration_records_at_one_size[test_one_configuration_records_at_one_size] | ✅ | - | ✅ | - |
| test_one_row_a_core_holds_is_still_rowwise[test_one_row_a_core_holds_is_still_rowwise] | ✅ | - | ✅ | - |
| test_one_row_times_a_number_is_elementwise[test_one_row_times_a_number_is_elementwise] | ✅ | - | ✅ | - |
| test_only_a_copy_takes_the_rows_an_input_names[test_only_a_copy_takes_the_rows_an_input_names] | ✅ | - | ✅ | - |
| test_only_none_may_default_an_input[test_only_none_may_default_an_input] | ✅ | - | ✅ | - |
| test_patches_short_of_a_tile_compute_a_whole_one[test_patches_short_of_a_tile_compute_a_whole_one] | ✅ | - | ✅ | - |
| test_per_call_values_bind_on_the_operator[test_per_call_values_bind_on_the_operator] | ✅ | - | ✅ | - |
| test_per_call_values_bind_to_the_operator_and_enable_it[test_per_call_values_bind_to_the_operator_and_enable_it] | ✅ | - | ✅ | - |
| test_placeholders_that_are_not_the_soft_tokens_are_refused[test_placeholders_that_are_not_the_soft_tokens_are_refused] | ✅ | - | ✅ | - |
| test_prompt_chunk_reads_the_rope_table_at_its_own_width[test_prompt_chunk_reads_the_rope_table_at_its_own_width] | ✅ | - | ✅ | - |
| test_reference_without_a_device_names_how_to_bind_one[test_reference_without_a_device_names_how_to_bind_one] | ✅ | - | ✅ | - |
| test_report_reads_as_one_block[test_report_reads_as_one_block] | ✅ | - | ✅ | - |
| test_resolve_columns_is_the_count_given_or_the_most_that_fit[test_resolve_columns_is_the_count_given_or_the_most_that_fit] | ✅ | - | ✅ | - |
| test_returning_an_input_or_a_slice_is_refused[test_returning_an_input_or_a_slice_is_refused] | ✅ | - | ✅ | - |
| test_rope_width_is_the_rotary_dim_when_given[test_rope_width_is_the_rotary_dim_when_given] | ✅ | - | ✅ | - |
| test_runtime_parameters_lay_out_the_buffer_words_and_skip_scratchpad_ones[test_runtime_parameters_lay_out_the_buffer_words_and_skip_scratchpad_ones] | ✅ | - | ✅ | - |
| test_saving_an_operator_outside_the_catalog_names_it[test_saving_an_operator_outside_the_catalog_names_it] | ✅ | - | ✅ | - |
| test_shape_mismatch_and_rank_rules[test_shape_mismatch_and_rank_rules] | ✅ | - | ✅ | - |
| test_slices_are_views_into_the_parent_in_bytes[test_slices_are_views_into_the_parent_in_bytes] | ✅ | - | ✅ | - |
| test_split_takes_every_batch_and_broadcasts[test_split_takes_every_batch_and_broadcasts] | ✅ | - | ✅ | - |
| test_stream_s_pieces_joined_are_what_generate_gives[test_stream_s_pieces_joined_are_what_generate_gives] | ✅ | - | ✅ | - |
| test_testing_resolves_cases_and_callables_of_the_class[test_testing_resolves_cases_and_callables_of_the_class] | ✅ | - | ✅ | - |
| test_the_architecture_decides_not_the_name[test_the_architecture_decides_not_the_name] | ✅ | - | ✅ | - |
| test_the_binary_sweep_and_an_all_extensive_sweep[test_the_binary_sweep_and_an_all_extensive_sweep] | ✅ | - | ✅ | - |
| test_the_callers_reference_runs_the_called_graph[test_the_callers_reference_runs_the_called_graph] | ✅ | - | ✅ | - |
| test_the_carried_draws_are_the_host_loop_s_tokens[temperature_0.0] | ✅ | - | ✅ | - |
| test_the_carried_draws_are_the_host_loop_s_tokens[temperature_0.7] | ✅ | - | ✅ | - |
| test_the_cases_judge_by_every_kind_of_tolerance[test_the_cases_judge_by_every_kind_of_tolerance] | ✅ | - | ✅ | - |
| test_the_default_layer_is_an_encoder_layer_attending_both_ways[test_the_default_layer_is_an_encoder_layer_attending_both_ways] | ✅ | - | ✅ | - |
| test_the_gather_reads_only_the_rows_a_call_bounds[test_the_gather_reads_only_the_rows_a_call_bounds] | ✅ | - | ✅ | - |
| test_the_oracles_steps_pass_and_a_wrong_weight_is_caught_at_its_step[test_the_oracles_steps_pass_and_a_wrong_weight_is_caught_at_its_step] | ✅ | - | ✅ | - |
| test_the_quick_start_script_runs_on_a_toy_repository[test_the_quick_start_script_runs_on_a_toy_repository] | ✅ | - | ✅ | - |
| test_the_reference_computes_the_expressions[test_the_reference_computes_the_expressions] | ✅ | - | ✅ | - |
| test_the_reference_copies_a_bounded_call_into_the_rows_it_covers[test_the_reference_copies_a_bounded_call_into_the_rows_it_covers] | ✅ | - | ✅ | - |
| test_the_reference_holds_one_layer_s_intermediates_at_a_time[test_the_reference_holds_one_layer_s_intermediates_at_a_time] | ✅ | - | ✅ | - |
| test_the_reference_is_its_parts_on_their_own[test_the_reference_is_its_parts_on_their_own] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_band] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_depthwise] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_depthwise_13_rows] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_patches] | ✅ | - | ✅ | - |
| test_the_reference_refuses_what_a_call_refuses[test_the_reference_refuses_what_a_call_refuses] | ✅ | - | ✅ | - |
| test_the_reference_runs_the_host_step_on_the_rows_the_call_bounds[rows_16] | ✅ | - | ✅ | - |
| test_the_reference_runs_the_host_step_on_the_rows_the_call_bounds[rows_5] | ✅ | - | ✅ | - |
| test_the_reference_runs_the_trace_so_held_state_takes_arithmetic[test_the_reference_runs_the_trace_so_held_state_takes_arithmetic] | ✅ | - | ✅ | - |
| test_the_reference_writes_a_copy_into_a_strided_view_through_it[test_the_reference_writes_a_copy_into_a_strided_view_through_it] | ✅ | - | ✅ | - |
| test_the_reference_writes_a_given_output_of_an_operator_that_returns_one[test_the_reference_writes_a_given_output_of_an_operator_that_returns_one] | ✅ | - | ✅ | - |
| test_the_refusals_name_what_to_change[test_the_refusals_name_what_to_change] | ✅ | - | ✅ | - |
| test_the_slots_after_a_multi_word_value_follow_its_words[test_the_slots_after_a_multi_word_value_follow_its_words] | ✅ | - | ✅ | - |
| test_the_trace_records_the_range_each_per_call_index_and_bound_holds[test_the_trace_records_the_range_each_per_call_index_and_bound_holds] | ✅ | - | ✅ | - |
| test_the_trip_count_is_a_resident_the_build_writes[test_the_trip_count_is_a_resident_the_build_writes] | ✅ | - | ✅ | - |
| test_the_unary_sweep_reads_the_class_it_is_resolved_for[test_the_unary_sweep_reads_the_class_it_is_resolved_for] | ✅ | - | ✅ | - |
| test_to_json_is_from_checkpoint_s_inverse[embedding_gemma2] | ✅ | - | ✅ | - |
| test_to_json_is_from_checkpoint_s_inverse[llama] | ✅ | - | ✅ | - |
| test_tracing_records_the_runlist_with_names_from_roles[test_tracing_records_the_runlist_with_names_from_roles] | ✅ | - | ✅ | - |
| test_two_designs_whose_device_names_collide_are_refused[test_two_designs_whose_device_names_collide_are_refused] | ✅ | - | ✅ | - |
| test_two_sessions_share_one_model[test_two_sessions_share_one_model] | ✅ | - | ✅ | - |
| test_two_towers_on_one_input_name_are_refused[test_two_towers_on_one_input_name_are_refused] | ✅ | - | ✅ | - |
| test_v_shows_iron_s_info_lines[test_v_shows_iron_s_info_lines] | ✅ | - | ✅ | - |
| test_vectors_draws_each_input_and_runs_the_reference_on_the_draw[test_vectors_draws_each_input_and_runs_the_reference_on_the_draw] | ✅ | - | ✅ | - |
| test_vectors_takes_a_given_shape_or_refuses_an_unknown_input[test_vectors_takes_a_given_shape_or_refuses_an_unknown_input] | ✅ | - | ✅ | - |
| test_walks_take_a_repeat_each[taps_1-repeats_2] | ✅ | - | ✅ | - |
| test_walks_take_a_repeat_each[taps_2-repeats_1] | ✅ | - | ✅ | - |
| test_what_a_bound_makes_per_call_is_worked_out_once_per_binding[test_what_a_bound_makes_per_call_is_worked_out_once_per_binding] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/tests/docs</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_section1_axpy_matches_numpy[test_section1_axpy_matches_numpy] | ✅ | - | ✅ | - |
| test_section1_axpy_on_device[test_section1_axpy_on_device] | ✅ | - | - | - |
| test_section2_first_graph_matches_numpy[test_section2_first_graph_matches_numpy] | ✅ | - | ✅ | - |
| test_section2_first_graph_on_device[test_section2_first_graph_on_device] | ✅ | - | - | - |
| test_section3_bounded_graph_matches_numpy[test_section3_bounded_graph_matches_numpy] | ✅ | - | ✅ | - |
| test_section3_bounded_graph_on_device[test_section3_bounded_graph_on_device] | ✅ | - | - | - |
| test_section3_bounded_graph_rejects_an_out_of_range_call[test_section3_bounded_graph_rejects_an_out_of_range_call] | ✅ | - | ✅ | - |
| test_section4_subtraction_exercise_selects_arithmetic[test_section4_subtraction_exercise_selects_arithmetic] | ✅ | - | ✅ | - |
| test_section4_weights_and_state_matches_numpy[test_section4_weights_and_state_matches_numpy] | ✅ | - | ✅ | - |
| test_section4_weights_and_state_on_device[test_section4_weights_and_state_on_device] | ✅ | - | - | - |
| test_section5_carried_loop_on_device[test_section5_carried_loop_on_device] | ✅ | - | - | - |
| test_section5_walk_matches_numpy_host_driven[test_section5_walk_matches_numpy_host_driven] | ✅ | - | ✅ | - |
| test_section6_check_mode_on_device[test_section6_check_mode_on_device] | ✅ | - | - | - |
| test_section6_reference_matches_its_operators_chained_by_hand[test_section6_reference_matches_its_operators_chained_by_hand] | ✅ | - | ✅ | - |
| test_section7_a_calls_own_value_wins_over_the_profile[test_section7_a_calls_own_value_wins_over_the_profile] | ✅ | - | ✅ | - |
| test_section7_profile_on_device[test_section7_profile_on_device] | ✅ | - | - | - |
| test_section7_profile_sets_tunables_by_shape[test_section7_profile_sets_tunables_by_shape] | ✅ | - | ✅ | - |
| test_section8_toy_decoder_matches_numpy[test_section8_toy_decoder_matches_numpy] | ✅ | - | ✅ | - |
| test_section8_toy_decoder_on_device[test_section8_toy_decoder_on_device] | ✅ | - | - | - |

</details>

<details>
<summary>iron/tests/infrastructure</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_batchnorm_s_int64_counter_loads_beside_its_float_weights[test_a_batchnorm_s_int64_counter_loads_beside_its_float_weights] | ✅ | - | ✅ | - |
| test_a_buffer_named_in_part_is_never_pooled[test_a_buffer_named_in_part_is_never_pooled] | ✅ | - | ✅ | - |
| test_a_call_takes_exactly_the_declared_scalars[scalars_{'m': 1}-error_<class 'TypeError'>-match_unexpected keyword argument\(s\): \['m'\]] | ✅ | - | ✅ | - |
| test_a_call_takes_exactly_the_declared_scalars[scalars_{'n': 1, 'm': 1}-error_<class 'TypeError'>-match_unexpected keyword argument\(s\): \['m'\]] | ✅ | - | ✅ | - |
| test_a_call_takes_exactly_the_declared_scalars[scalars_{}-error_<class 'aie.utils.hostruntime.hostruntime.HostRuntimeError'>-match_dispatch scalar mismatch] | ✅ | - | ✅ | - |
| test_a_carried_loop_walks_a_linked_list_on_the_device[depth_1] | ✅ | - | - | - |
| test_a_carried_loop_walks_a_linked_list_on_the_device[depth_2] | ✅ | - | - | - |
| test_a_carried_loop_walks_a_linked_list_on_the_device[depth_3] | ✅ | - | - | - |
| test_a_chain_of_more_designs_than_a_context_configures_runs[test_a_chain_of_more_designs_than_a_context_configures_runs] | ✅ | - | - | - |
| test_a_design_links_the_same_objects_alone_or_composed[test_a_design_links_the_same_objects_alone_or_composed] | ✅ | - | ✅ | - |
| test_a_field_the_repr_leaves_out_still_keys_the_build[test_a_field_the_repr_leaves_out_still_keys_the_build] | ✅ | - | ✅ | - |
| test_a_filled_tree_has_the_checkpoints_names_shapes_and_dtypes[fill_random] | ✅ | - | ✅ | - |
| test_a_filled_tree_has_the_checkpoints_names_shapes_and_dtypes[fill_unread] | ✅ | - | ✅ | - |
| test_a_full_elf_refuses_a_dispatch_value[test_a_full_elf_refuses_a_dispatch_value] | ✅ | - | ✅ | - |
| test_a_full_elf_takes_the_repeat_count_from_the_scratchpad[test_a_full_elf_takes_the_repeat_count_from_the_scratchpad] | ✅ | - | ✅ | - |
| test_a_gap_between_fixed_allocations_is_used_when_it_fits[test_a_gap_between_fixed_allocations_is_used_when_it_fits] | ✅ | - | ✅ | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[aot-dispatch_composed] | ✅ | - | - | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[aot-dispatch_separate] | ✅ | - | - | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[jit-dispatch_composed] | ✅ | - | - | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[jit-dispatch_separate] | ✅ | - | - | - |
| test_a_graph_records_the_same_steps_as_a_hand_written_runlist[test_a_graph_records_the_same_steps_as_a_hand_written_runlist] | ✅ | - | ✅ | - |
| test_a_graph_walks_a_linked_list_through_its_carried_values[test_a_graph_walks_a_linked_list_through_its_carried_values] | ✅ | - | - | - |
| test_a_layer_index_far_past_its_layers_is_refused[test_a_layer_index_far_past_its_layers_is_refused] | ✅ | - | ✅ | - |
| test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice[test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice] | ✅ | - | ✅ | - |
| test_a_pytorch_checkpoint_naming_another_global_is_refused[module_os-name_system] | ✅ | - | ✅ | - |
| test_a_pytorch_checkpoint_naming_another_global_is_refused[module_torch-name_DoubleStorage] | ✅ | - | ✅ | - |
| test_a_pytorch_checkpoint_naming_another_global_is_refused[module_torch._utils-name__rebuild_parameter] | ✅ | - | ✅ | - |
| test_a_pytorch_tensor_outside_its_storage_is_refused[foreign_id] | ✅ | - | ✅ | - |
| test_a_pytorch_tensor_outside_its_storage_is_refused[past_the_end] | ✅ | - | ✅ | - |
| test_a_pytorch_tensor_outside_its_storage_is_refused[short_storage] | ✅ | - | ✅ | - |
| test_a_read_leaves_nothing_for_the_next_call_to_push[test_a_read_leaves_nothing_for_the_next_call_to_push] | ✅ | - | - | - |
| test_a_released_run_is_made_again_on_the_next_call[test_a_released_run_is_made_again_on_the_next_call] | ✅ | - | - | - |
| test_a_resident_has_one_offset_in_every_image[test_a_resident_has_one_offset_in_every_image] | ✅ | - | ✅ | - |
| test_a_resident_needs_a_size[test_a_resident_needs_a_size] | ✅ | - | ✅ | - |
| test_a_session_not_asked_for_a_csv_writes_none[test_a_session_not_asked_for_a_csv_writes_none] | ✅ | - | ✅ | - |
| test_a_test_failing_in_setup_is_a_failed_check[test_a_test_failing_in_setup_is_a_failed_check] | ✅ | - | ✅ | - |
| test_a_traced_build_carries_the_lowered_module[test_a_traced_build_carries_the_lowered_module] | ✅ | - | ✅ | - |
| test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state[test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state] | ✅ | - | ✅ | - |
| test_a_version_reads_as_its_inputs_plan_and_build_directory[test_a_version_reads_as_its_inputs_plan_and_build_directory] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[faster] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[fewer_tokens_a_second] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[kl] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[slower_first_token] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[within] | ✅ | - | ✅ | - |
| test_a_written_pytorch_tensor_reads_as_its_storage[test_a_written_pytorch_tensor_reads_as_its_storage] | ✅ | - | ✅ | - |
| test_aligned_row_count_records_with_the_given_extents[test_aligned_row_count_records_with_the_given_extents] | ✅ | - | ✅ | - |
| test_an_argument_ends_past_the_arena_buffer_placed_last[test_an_argument_ends_past_the_arena_buffer_placed_last] | ✅ | - | ✅ | - |
| test_an_each_step_version_and_a_full_elf_share_one_arena[test_an_each_step_version_and_a_full_elf_share_one_arena] | ✅ | - | - | - |
| test_an_opaque_design_parameter_is_rejected[test_an_opaque_design_parameter_is_rejected] | ✅ | - | ✅ | - |
| test_an_operator_builds_its_own_image_once[test_an_operator_builds_its_own_image_once] | ✅ | - | ✅ | - |
| test_auto_dispatch_selects_platform_default[size_4096] | ✅ | - | ✅ | - |
| test_captured_graph_compiles_to_an_elf[test_captured_graph_compiles_to_an_elf] | ✅ | - | ✅ | - |
| test_cgroup_limit_reads_the_lowest_ceiling[unbounded] | ✅ | - | ✅ | - |
| test_cgroup_limit_reads_the_lowest_ceiling[v1] | ✅ | - | ✅ | - |
| test_cgroup_limit_reads_the_lowest_ceiling[v2-nested] | ✅ | - | ✅ | - |
| test_check_mode_catches_a_step_outside_its_tolerance_at_that_step[test_check_mode_catches_a_step_outside_its_tolerance_at_that_step] | ✅ | - | - | - |
| test_check_mode_holds_each_step_to_its_reference[test_check_mode_holds_each_step_to_its_reference] | ✅ | - | - | - |
| test_check_mode_judges_each_step_by_its_tolerance[test_check_mode_judges_each_step_by_its_tolerance] | ✅ | - | ✅ | - |
| test_check_mode_judges_every_output_at_the_calls_values[test_check_mode_judges_every_output_at_the_calls_values] | ✅ | - | ✅ | - |
| test_checkpoint_matches_safetensors_for_every_dtype[test_checkpoint_matches_safetensors_for_every_dtype] | ✅ | - | ✅ | - |
| test_checkpoint_reads_a_sharded_index[test_checkpoint_reads_a_sharded_index] | ✅ | - | ✅ | - |
| test_checkpoint_refuses_a_shard_outside_the_index_s_directory[shard_../a.safetensors] | ✅ | - | ✅ | - |
| test_checkpoint_refuses_a_shard_outside_the_index_s_directory[shard_/tmp/a.safetensors] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_malformed_file[range-before-the-data] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_malformed_file[range-not-the-shape] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_malformed_file[range-past-the-end] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_shard_that_disagrees_with_the_index[test_checkpoint_rejects_a_shard_that_disagrees_with_the_index] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_tensor_with_no_byte_range[test_checkpoint_rejects_a_tensor_with_no_byte_range] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_an_empty_archive[test_checkpoint_rejects_an_empty_archive] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_an_unsupported_dtype[test_checkpoint_rejects_an_unsupported_dtype] | ✅ | - | ✅ | - |
| test_checkpoint_release_drops_the_right_shard[test_checkpoint_release_drops_the_right_shard] | ✅ | - | ✅ | - |
| test_checkpoint_views_the_mapping_without_copying[test_checkpoint_views_the_mapping_without_copying] | ✅ | - | ✅ | - |
| test_commands_are_runtime_sequences_over_the_same_designs[test_commands_are_runtime_sequences_over_the_same_designs] | ✅ | - | ✅ | - |
| test_composed_mlir_contains_reconfiguration[sequence_add_relu] | ✅ | - | ✅ | - |
| test_designs_of_one_array_run_on_one_configure[test_designs_of_one_array_run_on_one_configure] | ✅ | - | - | - |
| test_device_rows_are_the_host_draws[test_device_rows_are_the_host_draws] | ✅ | - | ✅ | - |
| test_device_rows_refuse_an_unbounded_top_k[test_device_rows_refuse_an_unbounded_top_k] | ✅ | - | ✅ | - |
| test_dispatch_modes_bit_identical[dispatch_compare] | ✅ | - | ✅ | - |
| test_dispatch_modes_bit_identical[dispatch_composed] | ✅ | - | - | - |
| test_dispatch_modes_bit_identical[dispatch_separate] | ✅ | - | ✅ | - |
| test_download_fetches_into_the_cache_not_the_read_only_weights_dir[test_download_fetches_into_the_cache_not_the_read_only_weights_dir] | ✅ | - | ✅ | - |
| test_download_shares_no_partial_file_with_a_concurrent_fetch[test_download_shares_no_partial_file_with_a_concurrent_fetch] | ✅ | - | ✅ | - |
| test_draws_follow_the_distribution[test_draws_follow_the_distribution] | ✅ | - | ✅ | - |
| test_dump_writes_raw_words_and_perfetto_json[test_dump_writes_raw_words_and_perfetto_json] | ✅ | - | - | - |
| test_each_checkpoint_tensor_lands_on_its_name_bitwise[test_each_checkpoint_tensor_lands_on_its_name_bitwise] | ✅ | - | ✅ | - |
| test_each_design_of_one_array_runs_on_its_own_values[test_each_design_of_one_array_runs_on_its_own_values] | ✅ | - | - | - |
| test_each_merge_of_one_array_runs_on_its_own_count[test_each_merge_of_one_array_runs_on_its_own_count] | ✅ | - | - | - |
| test_each_position_table_of_one_array_runs_on_its_own_rows[test_each_position_table_of_one_array_runs_on_its_own_rows] | ✅ | - | - | - |
| test_each_resize_of_one_array_runs_on_its_own_sizes[test_each_resize_of_one_array_runs_on_its_own_sizes] | ✅ | - | - | - |
| test_each_runner_s_nightly_results_get_charts_of_their_own[test_each_runner_s_nightly_results_get_charts_of_their_own] | ✅ | - | ✅ | - |
| test_each_step_versions_share_weights_and_state_through_one_arena[test_each_step_versions_share_weights_and_state_through_one_arena] | ✅ | - | ✅ | - |
| test_each_table_of_one_array_runs_on_its_own_sizes[test_each_table_of_one_array_runs_on_its_own_sizes] | ✅ | - | - | - |
| test_empty_graph[test_empty_graph] | ✅ | - | ✅ | - |
| test_every_dispatch_returns_its_own_output[calls_2] | ✅ | - | ✅ | - |
| test_every_dispatch_returns_its_own_output[calls_3] | ✅ | - | ✅ | - |
| test_feedback_argument_only_when_declared[test_feedback_argument_only_when_declared] | ✅ | - | ✅ | - |
| test_feedback_chain_queued[test_feedback_chain_queued] | ✅ | - | - | - |
| test_feedback_into_plain_buffers[test_feedback_into_plain_buffers] | ✅ | - | - | - |
| test_feedback_ping_pong[test_feedback_ping_pong] | ✅ | - | - | - |
| test_feedback_with_trace[test_feedback_with_trace] | ✅ | - | - | - |
| test_fixed_allocations_are_obstacles_at_every_step[test_fixed_allocations_are_obstacles_at_every_step] | ✅ | - | ✅ | - |
| test_graph_inputs_and_outputs_are_left_alone[test_graph_inputs_and_outputs_are_left_alone] | ✅ | - | ✅ | - |
| test_greedy_is_argmax[test_greedy_is_argmax] | ✅ | - | ✅ | - |
| test_identical_operators_reuse_the_compiled_xclbin[test_identical_operators_reuse_the_compiled_xclbin] | ✅ | - | ✅ | - |
| test_identical_sequences_reuse_the_compiled_elf[test_identical_sequences_reuse_the_compiled_elf] | ✅ | - | ✅ | - |
| test_importing_iron_and_its_applications_imports_no_torch_or_transformers[test_importing_iron_and_its_applications_imports_no_torch_or_transformers] | ✅ | - | ✅ | - |
| test_int32_slice_at_word_offset[test_int32_slice_at_word_offset] | ✅ | - | - | - |
| test_int32_step_at_nonzero_offsets[test_int32_step_at_nonzero_offsets] | ✅ | - | - | - |
| test_kernel_objects_land_in_the_entry_under_bare_names[test_kernel_objects_land_in_the_entry_under_bare_names] | ✅ | - | ✅ | - |
| test_live_range_overlap[test_live_range_overlap] | ✅ | - | ✅ | - |
| test_llama3_scaling_matches_the_formula_in_every_band[test_llama3_scaling_matches_the_formula_in_every_band] | ✅ | - | ✅ | - |
| test_load_hands_each_piece_of_each_weight_to_release_once_it_is_uploaded[test_load_hands_each_piece_of_each_weight_to_release_once_it_is_uploaded] | ✅ | - | ✅ | - |
| test_load_loads_a_version_whose_weights_are_already_uploaded[test_load_loads_a_version_whose_weights_are_already_uploaded] | ✅ | - | ✅ | - |
| test_misaligned_buffer_is_rejected[test_misaligned_buffer_is_rejected] | ✅ | - | ✅ | - |
| test_mixed_sizes_reach_the_lower_bound[test_mixed_sizes_reach_the_lower_bound] | ✅ | - | ✅ | - |
| test_non_aligned_row_count_raises_instead_of_being_padded[test_non_aligned_row_count_raises_instead_of_being_padded] | ✅ | - | ✅ | - |
| test_non_input_buffers_sync_without_explicit_flush[dispatch_composed] | ✅ | - | - | - |
| test_non_input_buffers_sync_without_explicit_flush[dispatch_separate] | ✅ | - | ✅ | - |
| test_npu1_xclbin_pushes_the_call_s_repeat_count[test_npu1_xclbin_pushes_the_call_s_repeat_count] | ✅ | - | ✅ | - |
| test_odd_sizes_never_leave_an_offset_unaligned[test_odd_sizes_never_leave_an_offset_unaligned] | ✅ | - | ✅ | - |
| test_offsets_are_aligned[test_offsets_are_aligned] | ✅ | - | ✅ | - |
| test_one_design_expands_only_to_reconfigure[reconfigure_False] | ✅ | - | ✅ | - |
| test_one_design_expands_only_to_reconfigure[reconfigure_True] | ✅ | - | ✅ | - |
| test_one_design_is_configured_once[test_one_design_is_configured_once] | ✅ | - | - | - |
| test_one_design_reconfigures_after_another_image[test_one_design_reconfigures_after_another_image] | ✅ | - | - | - |
| test_one_image_repeats_a_tile_k_times[image_elf] | ✅ | - | - | - |
| test_one_image_repeats_a_tile_k_times[image_xclbin] | ✅ | - | - | - |
| test_one_image_serves_every_parameter[test_one_image_serves_every_parameter] | ✅ | - | ✅ | - |
| test_one_storage_is_one_size[test_one_storage_is_one_size] | ✅ | - | ✅ | - |
| test_pinned_buffers_are_not_pooled[test_pinned_buffers_are_not_pooled] | ✅ | - | ✅ | - |
| test_random_fill_draws_a_bias_about_zero[test_random_fill_draws_a_bias_about_zero] | ✅ | - | ✅ | - |
| test_random_fill_draws_at_its_seed[test_random_fill_draws_at_its_seed] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_0] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_10] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_11] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_12] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_13] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_14] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_15] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_16] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_17] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_18] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_19] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_1] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_2] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_3] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_4] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_5] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_6] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_7] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_8] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_9] | ✅ | - | ✅ | - |
| test_real_checkpoint_every_tensor_bitwise[test_real_checkpoint_every_tensor_bitwise] | ✅ | - | ✅ | - |
| test_real_checkpoint_is_llama_3_2_1b[test_real_checkpoint_is_llama_3_2_1b] | ✅ | - | ✅ | - |
| test_real_sharded_checkpoint_every_tensor_bitwise[test_real_sharded_checkpoint_every_tensor_bitwise] | ✅ | - | ✅ | - |
| test_real_tokenizer_s_added_tokens_are_their_ids[test_real_tokenizer_s_added_tokens_are_their_ids] | ✅ | - | ✅ | - |
| test_refuses_an_n_past_the_buffers[test_refuses_an_n_past_the_buffers] | ✅ | - | ✅ | - |
| test_release_drops_the_pages_and_keeps_the_bytes[test_release_drops_the_pages_and_keeps_the_bytes] | ✅ | - | ✅ | - |
| test_release_frees_the_buffers_and_the_next_call_loads_them_again[test_release_frees_the_buffers_and_the_next_call_loads_them_again] | ✅ | - | ✅ | - |
| test_release_leaves_anything_else_alone[test_release_leaves_anything_else_alone] | ✅ | - | ✅ | - |
| test_renamed_is_a_copy_a_caller_may_change[test_renamed_is_a_copy_a_caller_may_change] | ✅ | - | ✅ | - |
| test_repeated_block_packs_to_one_block_worth[test_repeated_block_packs_to_one_block_worth] | ✅ | - | ✅ | - |
| test_restricted_test_without_npu_runtime_skips_with_the_reason[test_restricted_test_without_npu_runtime_skips_with_the_reason] | ✅ | - | ✅ | - |
| test_restricted_tests_skip_where_the_device_is_not_listed[test_restricted_tests_skip_where_the_device_is_not_listed] | ✅ | - | ✅ | - |
| test_rope_is_correctly_rounded_at_position_zero_and_one[test_rope_is_correctly_rounded_at_position_zero_and_one] | ✅ | - | ✅ | - |
| test_rope_is_the_formula_rounded_once[test_rope_is_the_formula_rounded_once] | ✅ | - | ✅ | - |
| test_scaled_rope_table_rotates_by_the_scaled_frequencies[test_scaled_rope_table_rotates_by_the_scaled_frequencies] | ✅ | - | ✅ | - |
| test_seeded_sampling_is_reproducible[test_seeded_sampling_is_reproducible] | ✅ | - | ✅ | - |
| test_sequential_chain_double_buffers[test_sequential_chain_double_buffers] | ✅ | - | ✅ | - |
| test_simultaneously_live_buffers_do_not_share[test_simultaneously_live_buffers_do_not_share] | ✅ | - | ✅ | - |
| test_the_compile_key_covers_the_library_a_design_calls[test_the_compile_key_covers_the_library_a_design_calls] | ✅ | - | ✅ | - |
| test_the_compile_key_does_not_depend_on_a_device_being_bound_yet[test_the_compile_key_does_not_depend_on_a_device_being_bound_yet] | ✅ | - | - | - |
| test_the_compile_key_is_stable_across_identical_operators[test_the_compile_key_is_stable_across_identical_operators] | ✅ | - | ✅ | - |
| test_the_device_keys_the_build_by_identity_not_address[test_the_device_keys_the_build_by_identity_not_address] | ✅ | - | ✅ | - |
| test_the_lm_testing_helpers_import_without_pytest[test_the_lm_testing_helpers_import_without_pytest] | ✅ | - | ✅ | - |
| test_the_prompt_text_repeats_past_its_end[test_the_prompt_text_repeats_past_its_end] | ✅ | - | ✅ | - |
| test_the_stream_is_generated_per_call[test_the_stream_is_generated_per_call] | ✅ | - | ✅ | - |
| test_top_k_keeps_ties_with_the_kth[test_top_k_keeps_ties_with_the_kth] | ✅ | - | ✅ | - |
| test_top_k_never_leaves_the_top_k[test_top_k_never_leaves_the_top_k] | ✅ | - | ✅ | - |
| test_touching_ranges_ignore_names_not_asked_for[test_touching_ranges_ignore_names_not_asked_for] | ✅ | - | ✅ | - |
| test_touching_ranges_span_first_to_last_use_whatever_the_direction[test_touching_ranges_span_first_to_last_use_whatever_the_direction] | ✅ | - | ✅ | - |
| test_tree_names_a_layer_past_the_last[test_tree_names_a_layer_past_the_last] | ✅ | - | ✅ | - |
| test_tree_names_a_missing_tensor_by_its_path_and_file[test_tree_names_a_missing_tensor_by_its_path_and_file] | ✅ | - | ✅ | - |
| test_tree_names_a_tensor_of_a_skipped_layer[test_tree_names_a_tensor_of_a_skipped_layer] | ✅ | - | ✅ | - |
| test_two_graphs_get_distinct_cache_keys[test_two_graphs_get_distinct_cache_keys] | ✅ | - | ✅ | - |
| test_two_shapes_share_weights_and_state_through_one_arena[test_two_shapes_share_weights_and_state_through_one_arena] | ✅ | - | - | - |
| test_unread_fill_zeroes_a_scalar[test_unread_fill_zeroes_a_scalar] | ✅ | - | ✅ | - |
| test_unrestricted_tests_need_no_npu_runtime[test_unrestricted_tests_need_no_npu_runtime] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/tests/lm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_cache_attends_within_its_window[test_a_cache_attends_within_its_window] | ✅ | - | ✅ | - |
| test_a_causal_model_draws_after_its_soft_tokens[test_a_causal_model_draws_after_its_soft_tokens] | ✅ | - | - | - |
| test_a_causal_model_places_soft_tokens_across_its_chunks[test_a_causal_model_places_soft_tokens_across_its_chunks] | ✅ | - | - | - |
| test_a_graph_held_at_two_paths_skips_the_second_paths_tensors[test_a_graph_held_at_two_paths_skips_the_second_paths_tensors] | ✅ | - | ✅ | - |
| test_a_layer_reading_another_s_cache_projects_and_writes_no_keys[test_a_layer_reading_another_s_cache_projects_and_writes_no_keys] | ✅ | - | ✅ | - |
| test_a_param_never_bound_is_named_at_record[test_a_param_never_bound_is_named_at_record] | ✅ | - | ✅ | - |
| test_a_q_table_scaled_by_two_doubles_the_logits_scale[test_a_q_table_scaled_by_two_doubles_the_logits_scale] | ✅ | - | ✅ | - |
| test_a_random_tree_draws_a_scalar_as_an_array[test_a_random_tree_draws_a_scalar_as_an_array] | ✅ | - | ✅ | - |
| test_a_ring_restarts_at_the_chunk_while_it_holds_the_window_before[test_a_ring_restarts_at_the_chunk_while_it_holds_the_window_before] | ✅ | - | ✅ | - |
| test_a_ring_s_chunk_attends_from_its_valid_rows_alone[test_a_ring_s_chunk_attends_from_its_valid_rows_alone] | ✅ | - | ✅ | - |
| test_a_second_bind_is_refused[test_a_second_bind_is_refused] | ✅ | - | ✅ | - |
| test_a_tied_param_ignores_a_tensor_at_its_other_path[test_a_tied_param_ignores_a_tensor_at_its_other_path] | ✅ | - | ✅ | - |
| test_a_turn_over_a_ring_is_the_run_from_scratch_bit_for_bit[test_a_turn_over_a_ring_is_the_run_from_scratch_bit_for_bit] | ✅ | - | ✅ | - |
| test_a_window_keeps_every_position_where_a_ring_takes_as_many_rows[test_a_window_keeps_every_position_where_a_ring_takes_as_many_rows] | ✅ | - | ✅ | - |
| test_an_index_a_checkpoint_skips_is_empty_and_no_leaf[test_an_index_a_checkpoint_skips_is_empty_and_no_leaf] | ✅ | - | ✅ | - |
| test_an_odd_vocabulary_pads_the_head_with_a_row_no_draw_takes[test_an_odd_vocabulary_pads_the_head_with_a_row_no_draw_takes] | ✅ | - | ✅ | - |
| test_attention_refuses_a_norm_of_other_than_q_k_and_v[test_attention_refuses_a_norm_of_other_than_q_k_and_v] | ✅ | - | ✅ | - |
| test_attention_turns_only_the_rotary_columns[test_attention_turns_only_the_rotary_columns] | ✅ | - | ✅ | - |
| test_conv2d[case_depthwise_13_rows-share_0.25] | ✅ | - | ✅ | - |
| test_conv2d[case_depthwise_13_rows-share_1.0] | ✅ | - | ✅ | - |
| test_each_generation_check_prefills_its_whole_prompt[test_each_generation_check_prefills_its_whole_prompt] | ✅ | - | ✅ | - |
| test_each_layer_reads_the_rows_of_its_own_rope[test_each_layer_reads_the_rows_of_its_own_rope] | ✅ | - | ✅ | - |
| test_embedding_gemma2_is_on_npu[test_embedding_gemma2_is_on_npu] | ✅ | - | ✅ | - |
| test_gemma4_towers_are_on_npu[test_gemma4_towers_are_on_npu] | ✅ | - | ✅ | - |
| test_leaf_modules_match_numpy[test_leaf_modules_match_numpy] | ✅ | - | ✅ | - |
| test_load_state_dict_casts_to_the_params_dtype[test_load_state_dict_casts_to_the_params_dtype] | ✅ | - | ✅ | - |
| test_load_state_dict_names_each_kind_in_one_error[test_load_state_dict_names_each_kind_in_one_error] | ✅ | - | ✅ | - |
| test_load_state_dict_refuses_a_change_of_kind[test_load_state_dict_refuses_a_change_of_kind] | ✅ | - | ✅ | - |
| test_load_state_dict_refuses_a_param_in_a_frozen_dataclass[test_load_state_dict_refuses_a_param_in_a_frozen_dataclass] | ✅ | - | ✅ | - |
| test_load_state_dict_refuses_a_param_in_a_tuple[test_load_state_dict_refuses_a_param_in_a_tuple] | ✅ | - | ✅ | - |
| test_log_mel[frames_200] | ✅ | 5899.41 | ✅ | 20135.84 |
| test_log_mel[frames_3072] | ✅ | 12010.26 | ✅ | 26094.14 |
| test_tensors_at_indices_are_a_list_of_tensors[test_tensors_at_indices_are_a_list_of_tensors] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/tests/operators</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_bound_past_a_wrap_of_tiles_per_lane[test_a_bound_past_a_wrap_of_tiles_per_lane] | ✅ | - | - | - |
| test_a_bounded_gather_moves_its_rows_and_a_unit_for_each_other[test_a_bounded_gather_moves_its_rows_and_a_unit_for_each_other] | ✅ | - | ✅ | - |
| test_a_bounded_gather_of_rows_not_whole_16_byte_units_is_refused[test_a_bounded_gather_of_rows_not_whole_16_byte_units_is_refused] | ✅ | - | ✅ | - |
| test_a_bounded_prompt_chunk_moves_13_rows_not_2048[test_a_bounded_prompt_chunk_moves_13_rows_not_2048] | ✅ | - | ✅ | - |
| test_a_call_starts_its_queries_anywhere[causal] | ✅ | - | - | - |
| test_a_call_starts_its_queries_anywhere[sliding] | ✅ | - | - | - |
| test_a_chunk_attends_over_the_cache_before_it[full_elf] | ✅ | - | - | - |
| test_a_chunk_attends_over_the_cache_before_it[xclbin] | ✅ | - | - | - |
| test_a_chunk_lands_in_its_rows_of_the_cache[test_a_chunk_lands_in_its_rows_of_the_cache] | ✅ | - | - | - |
| test_a_copy_moves_the_valid_rows_of_each_head[test_a_copy_moves_the_valid_rows_of_each_head] | ✅ | - | - | - |
| test_a_float32_softmax_under_a_per_call_bound_is_refused[test_a_float32_softmax_under_a_per_call_bound_is_refused] | ✅ | - | ✅ | - |
| test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu1-feeds_3] | ✅ | - | ✅ | - |
| test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu2-feeds_0] | ✅ | - | ✅ | - |
| test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu2-feeds_5] | ✅ | - | ✅ | - |
| test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused[test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused] | ✅ | - | ✅ | - |
| test_a_given_raster_keeps_the_rows_past_the_image[test_a_given_raster_keeps_the_rows_past_the_image] | ✅ | - | ✅ | - |
| test_a_graph_gathers_twice_from_a_weight_and_a_state[full_elf] | ✅ | - | - | - |
| test_a_graph_gathers_twice_from_a_weight_and_a_state[xclbin] | ✅ | - | - | - |
| test_a_line_of_part_of_a_vector_is_refused[limbs] | ✅ | - | ✅ | - |
| test_a_line_of_part_of_a_vector_is_refused[magnitude] | ✅ | - | ✅ | - |
| test_a_row_lands_at_its_index_on_the_leading_axis[full_elf] | ✅ | - | - | - |
| test_a_row_lands_at_its_index_on_the_leading_axis[xclbin] | ✅ | - | - | - |
| test_a_run_lands_from_any_start_and_is_read_back[full_elf] | ✅ | - | - | - |
| test_a_run_lands_from_any_start_and_is_read_back[xclbin] | ✅ | - | - | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu1-precision_high-M_16-rows_1-tile_m_16] | ✅ | - | ✅ | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu1-precision_high-M_32-rows_2-tile_m_16] | ✅ | - | ✅ | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu2-precision_high-M_16-rows_2-tile_m_8] | ✅ | - | ✅ | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu2-precision_medium-M_32-rows_2-tile_m_16] | ✅ | - | ✅ | - |
| test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused[test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused] | ✅ | - | ✅ | - |
| test_a_tile_past_what_one_core_holds_is_refused_not_split[test_a_tile_past_what_one_core_holds_is_refused_not_split] | ✅ | - | ✅ | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[flat-channels_1] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[flat-channels_2] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[flat-channels_4] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[head_rows-channels_1] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[head_rows-channels_2] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[head_rows-channels_4] | ✅ | - | - | - |
| test_a_transposing_copy_on_any_channel_count[channels_1] | ✅ | - | - | - |
| test_a_transposing_copy_on_any_channel_count[channels_2] | ✅ | - | - | - |
| test_a_transposing_copy_on_any_channel_count[channels_4] | ✅ | - | - | - |
| test_a_validate_or_compatible_branch_refuses[clamp_bounds] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[conv_channels] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[conv_runs] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[emit_rows] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_angle_rows] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_angle_rows_split] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_cols] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_rows_split] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[softmax_f32_option] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[softmax_window_alone] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[softmax_window_no_addend] | ✅ | - | ✅ | - |
| test_a_walk_by_a_per_call_repeat_and_length_is_its_reference[band_stride_0] | ✅ | - | ✅ | - |
| test_a_walk_by_a_per_call_repeat_and_length_is_its_reference[band_stride_1] | ✅ | - | ✅ | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_0-full_elf] | ✅ | - | - | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_0-xclbin] | ✅ | - | - | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_1-full_elf] | ✅ | - | - | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_1-xclbin] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[llama] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[resident] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[resident_tail] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[slice_is_k_max] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[streamed] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[streamed_unaligned] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[uneven] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[uneven_streamed] | ✅ | - | - | - |
| test_aie2_activations_bring_their_lut_tables_into_the_frame[test_aie2_activations_bring_their_lut_tables_into_the_frame] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_an_input_gathers_from_a_table_once[test_an_input_gathers_from_a_table_once] | ✅ | - | ✅ | - |
| test_an_m_no_tile_splits_is_rejected[device_npu1-precision_high] | ✅ | - | ✅ | - |
| test_an_m_no_tile_splits_is_rejected[device_npu2-precision_medium] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu1-precision_high-M_64-tile_m_16] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_high-M_32-tile_m_8] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_128-tile_m_32] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_2048-tile_m_64] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_64-tile_m_16] | ✅ | - | ✅ | - |
| test_attention_reduces_over_the_valid_keys[test_attention_reduces_over_the_valid_keys] | ✅ | - | - | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_32-chunks_1] | ✅ | - | ✅ | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_32-chunks_3] | ✅ | - | ✅ | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_64-chunks_1] | ✅ | - | ✅ | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_64-chunks_3] | ✅ | - | ✅ | - |
| test_bounded_rows_past_a_wrap_fill_either_half[test_bounded_rows_past_a_wrap_fill_either_half] | ✅ | - | - | - |
| test_bounded_rows_past_a_wrap_halve_the_run[test_bounded_rows_past_a_wrap_halve_the_run] | ✅ | - | ✅ | - |
| test_buffers_do_not_follow_the_pipeline_count[test_buffers_do_not_follow_the_pipeline_count] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_1024-N_128] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_1536-N_640] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_2048-N_2048] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_2048-N_256] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_512-N_64] | ✅ | - | ✅ | - |
| test_channels_not_dividing_the_shared_run_are_rejected[test_channels_not_dividing_the_shared_run_are_rejected] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_128] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_16] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_32] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_64] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_128] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_16] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_32] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_64] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu1-b_bytes_2-tile_n_128-expected_(32, 32, 2)] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu1-b_bytes_2-tile_n_64-expected_(64, 64, 2)] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu2-b_bytes_1.125-tile_n_128-expected_(64, 32, 2)] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu2-b_bytes_1.125-tile_n_64-expected_(128, 32, 2)] | ✅ | - | ✅ | - |
| test_descriptors_are_dma_expressible[test_descriptors_are_dma_expressible] | ✅ | - | ✅ | - |
| test_each_step_gathers_by_ids_the_device_made[n_ids_15] | ✅ | - | ✅ | - |
| test_each_step_gathers_by_ids_the_device_made[n_ids_512] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds[n_ids_15] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds[n_ids_256] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds_by_ids_the_device_made[n_ids_15] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds_by_ids_the_device_made[n_ids_256] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_an_input_names[test_each_step_gathers_the_rows_an_input_names] | ✅ | - | ✅ | - |
| test_every_operator_is_in_the_catalog[test_every_operator_is_in_the_catalog] | ✅ | - | ✅ | - |
| test_every_row_of_a_bound_is_computed[test_every_row_of_a_bound_is_computed] | ✅ | - | - | - |
| test_explicit_aie2_tile_falls_back_to_single_buffered_b[test_explicit_aie2_tile_falls_back_to_single_buffered_b] | ✅ | - | ✅ | - |
| test_flm_decode_layer_rejects_unknown_configurations[geometry] | ✅ | - | ✅ | - |
| test_flm_decode_layer_rejects_unknown_configurations[layer_type] | ✅ | - | ✅ | - |
| test_flm_dequant_rejects_unservable_shapes[K_1000-N_128-match_K \(1000\)] | ✅ | - | ✅ | - |
| test_flm_dequant_rejects_unservable_shapes[K_1024-N_100-match_N \(100\)] | ✅ | - | ✅ | - |
| test_flm_gemm_reads_b_as_stored_in_bf16[test_flm_gemm_reads_b_as_stored_in_bf16] | ✅ | - | ✅ | - |
| test_flm_lm_head_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_dim \(1000\) must be a multiple] | ✅ | - | ✅ | - |
| test_flm_lm_head_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_vocab \(1000\) must be a multiple] | ✅ | - | ✅ | - |
| test_flm_lm_head_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128] | ✅ | - | ✅ | - |
| test_gemm_on_columns_that_do_not_divide_its_rows_is_refused[device_npu1] | ✅ | - | ✅ | - |
| test_gemm_on_columns_that_do_not_divide_its_rows_is_refused[device_npu2] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[k4_emulated] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[m8] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[m8_emulated] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[n8] | ✅ | - | ✅ | - |
| test_ids_past_the_table_are_refused[outside_-262145] | ✅ | - | - | - |
| test_ids_past_the_table_are_refused[outside_262144] | ✅ | - | - | - |
| test_merge_of_no_or_repeated_placeholders_is_refused[placeholders_((7, 0), (7, 64))] | ✅ | - | ✅ | - |
| test_merge_of_no_or_repeated_placeholders_is_refused[placeholders_()] | ✅ | - | ✅ | - |
| test_merge_of_part_of_a_block_is_refused[test_merge_of_part_of_a_block_is_refused] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[block_past_the_padding] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[empty_window] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[head_not_whole_64] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[negative_scale] | ✅ | - | ✅ | - |
| test_mha_of_one_query_that_does_not_pack_is_refused[group_past_a_block] | ✅ | - | ✅ | - |
| test_mha_of_one_query_that_does_not_pack_is_refused[more_than_four_pipelines] | ✅ | - | ✅ | - |
| test_mha_of_one_query_that_does_not_pack_is_refused[uneven_groups] | ✅ | - | ✅ | - |
| test_mha_one_query_packed_takes_the_narrowest_block_and_64_keys[test_mha_one_query_packed_takes_the_narrowest_block_and_64_keys] | ✅ | - | ✅ | - |
| test_mha_whose_blocks_do_not_line_up_is_refused[kv_len_not_whole_blocks] | ✅ | - | ✅ | - |
| test_mha_whose_blocks_do_not_line_up_is_refused[kv_len_short_of_queries] | ✅ | - | ✅ | - |
| test_mha_whose_head_fits_no_block_is_refused[test_mha_whose_head_fits_no_block_is_refused] | ✅ | - | ✅ | - |
| test_mha_whose_pipelines_do_not_fill_the_rows_is_refused[test_mha_whose_pipelines_do_not_fill_the_rows_is_refused] | ✅ | - | ✅ | - |
| test_mha_whose_pv_split_does_not_route_is_refused[one_query_packed] | ✅ | - | ✅ | - |
| test_mha_whose_pv_split_does_not_route_is_refused[six_pipelines_to_a_join] | ✅ | - | ✅ | - |
| test_mha_whose_pv_split_does_not_route_is_refused[three_ways] | ✅ | - | ✅ | - |
| test_one_input_s_ids_gather_from_each_of_three_tables[full_elf_False] | ✅ | - | - | - |
| test_one_input_s_ids_gather_from_each_of_three_tables[full_elf_True] | ✅ | - | - | - |
| test_one_pipeline_fills_k_and_v_past_the_task_queue[test_one_pipeline_fills_k_and_v_past_the_task_queue] | ✅ | - | - | - |
| test_one_query_is_as_accurate_deep_in_the_cache_as_near_its_start[test_one_query_is_as_accurate_deep_in_the_cache_as_near_its_start] | ✅ | - | - | - |
| test_operator[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | - | - | ✅ | 24.99 |
| test_operator[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | - | - | ✅ | 20.92 |
| test_operator[npu1-AXPY-size_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | - | - | ✅ | 31.14 |
| test_operator[npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 3179.29 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | - | - | ✅ | 20.81 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_1-tile_size_2048-low_0.5-high_1.5] | - | - | ✅ | 22.50 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_2-tile_size_1024-low_-30000.0-high_30000.0] | - | - | ✅ | 19.34 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_4-num_channels_2-tile_size_256-low_-0.75-high_1.25] | - | - | ✅ | 49.01 |
| test_operator[npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25] | - | - | ✅ | 1143.83 |
| test_operator[npu1-Copy-bench_flat_4mi] | - | - | ✅ | 1060.75 |
| test_operator[npu1-Copy-by_head_two_channels] | - | - | ✅ | 18.13 |
| test_operator[npu1-Copy-chunked_transfer] | - | - | ✅ | 22.77 |
| test_operator[npu1-Copy-contiguous] | - | - | ✅ | 18.78 |
| test_operator[npu1-Copy-float32] | - | - | ✅ | 22.30 |
| test_operator[npu1-Copy-past_one_memtile] | - | - | ✅ | 546.86 |
| test_operator[npu1-Copy-slot5] | - | - | ✅ | 18.42 |
| test_operator[npu1-Copy-slot5_two_channels] | - | - | ✅ | 18.39 |
| test_operator[npu1-Copy-slot_last] | - | - | ✅ | 17.92 |
| test_operator[npu1-Copy-two_channels] | - | - | ✅ | 17.55 |
| test_operator[npu1-DepthwiseConv1d-rows_64-channels_256-num_aie_columns_2] | - | - | ✅ | 26.95 |
| test_operator[npu1-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | - | - | ✅ | 24.90 |
| test_operator[npu1-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 20.50 |
| test_operator[npu1-ElementwiseAdd-size_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 33.30 |
| test_operator[npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 1588.24 |
| test_operator[npu1-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 29.66 |
| test_operator[npu1-ElementwiseMul-size_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 30.07 |
| test_operator[npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 1565.28 |
| test_operator[npu1-Emit-eight_carried] | - | - | ✅ | 16.38 |
| test_operator[npu1-Emit-one_carried] | - | - | ✅ | 19.54 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-approximate_none] | - | - | ✅ | 50.03 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 28.64 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256-approximate_none] | - | - | ✅ | 45.70 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 48.70 |
| test_operator[npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2848.29 |
| test_operator[npu1-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | - | - | ✅ | 51.92 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | - | - | ✅ | 7752.65 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | - | - | ✅ | 79247.58 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 18318.42 |
| test_operator[npu1-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | - | - | ✅ | -46.67 |
| test_operator[npu1-GEMM-M_384-K_1536-N_1792-num_aie_columns_4-tile_m_32-tile_k_48-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 4283.09 |
| test_operator[npu1-GEMM-f32_out] | - | - | ✅ | 172.80 |
| test_operator[npu1-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | - | - | ✅ | 1064.79 |
| test_operator[npu1-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_2] | - | - | ✅ | 2088.20 |
| test_operator[npu1-GEMV-M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | - | - | ✅ | 322.28 |
| test_operator[npu1-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | - | - | ✅ | 34.84 |
| test_operator[npu1-GEMV-M_2048-K_64-num_aie_columns_4-tile_size_input_4-tile_size_output_256-num_channels_2-num_batches_32-repeat_4] | - | - | ✅ | 1022.64 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | - | - | ✅ | 144.06 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_32-num_channels_2-num_batches_8] | - | - | ✅ | 102.27 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_4] | - | - | ✅ | 91.31 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_8-repeat_4] | - | - | ✅ | 148.65 |
| test_operator[npu1-GEMV-M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | - | - | ✅ | 417.54 |
| test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 19.31 |
| test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 20.09 |
| test_operator[npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 1220.54 |
| test_operator[npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 1148.99 |
| test_operator[npu1-LayerNorm-rows_4-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | - | - | ✅ | 29.56 |
| test_operator[npu1-LayerNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 45.86 |
| test_operator[npu1-Limbs-rows_512-line_320-num_aie_columns_4] | - | - | ✅ | 158.74 |
| test_operator[npu1-Limbs-rows_64-line_160-num_aie_columns_1] | - | - | ✅ | 50.80 |
| test_operator[npu1-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 62.11 |
| test_operator[npu1-Log-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 46.18 |
| test_operator[npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 22532.64 |
| test_operator[npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4] | - | - | ✅ | 81319.99 |
| test_operator[npu1-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | - | - | ✅ | 654.41 |
| test_operator[npu1-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | - | - | ✅ | 359.15 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | - | - | ✅ | 310.43 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_4-heads_interleaved_True] | - | - | ✅ | 11451.59 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_4] | - | - | ✅ | 65520.95 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_2-seq_len_2000-d_256-causal_False-window_512-num_pipelines_4] | - | - | ✅ | 49050.73 |
| test_operator[npu1-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | - | - | ✅ | 364.23 |
| test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_4] | - | - | ✅ | 57895.14 |
| test_operator[npu1-Magnitude-rows_512-width_640-num_aie_columns_4] | - | - | ✅ | 434.98 |
| test_operator[npu1-Magnitude-rows_64-width_640-num_aie_columns_1] | - | - | ✅ | 233.39 |
| test_operator[npu1-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))-offset_True] | - | - | ✅ | 25.87 |
| test_operator[npu1-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))] | - | - | ✅ | 26.19 |
| test_operator[npu1-Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))] | - | - | ✅ | 22.86 |
| test_operator[npu1-Merge-rows_192-placeholders_((49190, 64),)] | - | - | ✅ | 23.00 |
| test_operator[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))-offset_True] | - | - | ✅ | 84.93 |
| test_operator[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | - | - | ✅ | 80.71 |
| test_operator[npu1-PatchPositions-rows_2048-out_height_480-out_width_1056-cores_8] | - | - | ✅ | 112.16 |
| test_operator[npu1-PatchPositions-rows_2304-out_height_768-out_width_768] | - | - | ✅ | 116.09 |
| test_operator[npu1-PatchPositions-rows_256-out_height_48-out_width_48] | - | - | ✅ | 29.84 |
| test_operator[npu1-PatchPositions-rows_2560-out_height_672-out_width_912] | - | - | ✅ | 123.27 |
| test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 28.93 |
| test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 19.53 |
| test_operator[npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 1202.52 |
| test_operator[npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 1147.35 |
| test_operator[npu1-RMSNorm-rows_4-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | - | - | ✅ | 30.49 |
| test_operator[npu1-RMSNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 44.30 |
| test_operator[npu1-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 20.32 |
| test_operator[npu1-ReLU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 24.00 |
| test_operator[npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 1155.03 |
| test_operator[npu1-Resample-height_3024-width_4032-out_height_672-out_width_912] | - | - | ✅ | 50763.68 |
| test_operator[npu1-Resample-height_37-width_53-out_height_96-out_width_144] | - | - | ✅ | 315.53 |
| test_operator[npu1-Resample-height_37-width_53-out_height_96-out_width_256] | - | - | ✅ | 352.30 |
| test_operator[npu1-Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4] | - | - | ✅ | 8548.70 |
| test_operator[npu1-Resample-height_6000-width_500-out_height_672-out_width_432] | - | - | ✅ | 32672.18 |
| test_operator[npu1-ResampleTaps-in_size_1-out_size_48-num_aie_columns_2] | - | - | ✅ | 883.50 |
| test_operator[npu1-ResampleTaps-in_size_17-out_size_1008] | - | - | ✅ | 4409.89 |
| test_operator[npu1-ResampleTaps-in_size_3024-out_size_672-words_356-slots_16] | - | - | ✅ | 12419.50 |
| test_operator[npu1-ResampleTaps-in_size_4032-out_size_912] | - | - | ✅ | 15848.12 |
| test_operator[npu1-ResampleTaps-in_size_8000-out_size_672-num_aie_columns_1-num_channels_1] | - | - | ✅ | 214190.51 |
| test_operator[npu1-ResampleTaps-in_size_961-out_size_960] | - | - | ✅ | 4024.43 |
| test_operator[npu1-RoPE-rows_32-cols_128-num_aie_columns_1-angle_rows_8-two_halves_False] | - | - | ✅ | 24.74 |
| test_operator[npu1-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | - | - | ✅ | 24.56 |
| test_operator[npu1-RoPE-rows_32-cols_512-num_aie_columns_4-angle_rows_32] | - | - | ✅ | 31.29 |
| test_operator[npu1-RoPE-rows_4096-cols_512-angle_rows_8] | - | - | ✅ | 319.16 |
| test_operator[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 23.72 |
| test_operator[npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096] | - | - | ✅ | 1596.57 |
| test_operator[npu1-RowwiseAdd-rows_4-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 34.91 |
| test_operator[npu1-RowwiseAdd-wide_row] | - | - | ✅ | 85.59 |
| test_operator[npu1-RowwiseAdd-wider_row] | - | - | ✅ | 46.25 |
| test_operator[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 22.73 |
| test_operator[npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096] | - | - | ✅ | 1185.01 |
| test_operator[npu1-RowwiseMul-rows_4-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 32.39 |
| test_operator[npu1-RowwiseMul-wide_row] | - | - | ✅ | 80.05 |
| test_operator[npu1-RowwiseMul-wider_row] | - | - | ✅ | 47.01 |
| test_operator[npu1-Sample-llama] | - | - | ✅ | 338.43 |
| test_operator[npu1-Sample-padded] | - | - | ✅ | 359.27 |
| test_operator[npu1-Sample-small] | - | - | ✅ | 155.62 |
| test_operator[npu1-Sample-two_cores] | - | - | ✅ | 119.67 |
| test_operator[npu1-Sample-uneven] | - | - | ✅ | 168.88 |
| test_operator[npu1-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 23.04 |
| test_operator[npu1-SiLU-size_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 27.83 |
| test_operator[npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 2686.34 |
| test_operator[npu1-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 23.32 |
| test_operator[npu1-Sigmoid-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 50.01 |
| test_operator[npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 1142.50 |
| test_operator[npu1-Softmax-f32_soft_cap_banded_addend] | - | - | ✅ | 51.70 |
| test_operator[npu1-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | - | - | ✅ | 127.99 |
| test_operator[npu1-Softmax-rows_16-cols_4608-num_aie_columns_2-num_channels_2] | - | - | ✅ | 150.95 |
| test_operator[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | - | - | ✅ | 115.60 |
| test_operator[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | - | - | ✅ | 37.82 |
| test_operator[npu1-Softmax-rows_32-cols_32768-num_aie_columns_2-num_channels_2] | - | - | ✅ | 1647.81 |
| test_operator[npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2] | - | - | ✅ | 1289.30 |
| test_operator[npu1-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 18.48 |
| test_operator[npu1-Tanh-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 46.56 |
| test_operator[npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 1782.50 |
| test_operator[npu2-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 26.80 | - | - |
| test_operator[npu2-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 19.57 | - | - |
| test_operator[npu2-AXPY-size_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 31.11 | - | - |
| test_operator[npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 702.75 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | 16.19 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_1-tile_size_2048-low_0.5-high_1.5] | ✅ | 19.51 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_2-tile_size_1024-low_-30000.0-high_30000.0] | ✅ | 15.46 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_8-num_channels_2-tile_size_128-low_-0.75-high_1.25] | ✅ | 47.92 | - | - |
| test_operator[npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25] | ✅ | 502.42 | - | - |
| test_operator[npu2-Copy-bench_flat_4mi] | ✅ | 364.68 | - | - |
| test_operator[npu2-Copy-by_head_two_channels] | ✅ | 24.20 | - | - |
| test_operator[npu2-Copy-chunked_transfer] | ✅ | 26.68 | - | - |
| test_operator[npu2-Copy-contiguous] | ✅ | 18.08 | - | - |
| test_operator[npu2-Copy-float32] | ✅ | 17.51 | - | - |
| test_operator[npu2-Copy-past_one_memtile] | ✅ | 172.10 | - | - |
| test_operator[npu2-Copy-slot5] | ✅ | 25.79 | - | - |
| test_operator[npu2-Copy-slot5_two_channels] | ✅ | 25.69 | - | - |
| test_operator[npu2-Copy-slot_last] | ✅ | 27.57 | - | - |
| test_operator[npu2-Copy-two_channels] | ✅ | 26.30 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_32-channels_96-num_aie_columns_8] | ✅ | 23.70 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_64-channels_256-num_aie_columns_2] | ✅ | 17.95 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | 18.75 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8] | ✅ | 71.52 | - | - |
| test_operator[npu2-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | 18.66 | - | - |
| test_operator[npu2-ElementwiseAdd-size_2048-num_aie_columns_8-tile_size_256] | ✅ | 26.61 | - | - |
| test_operator[npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 694.37 | - | - |
| test_operator[npu2-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | 22.15 | - | - |
| test_operator[npu2-ElementwiseMul-size_2048-num_aie_columns_8-tile_size_256] | ✅ | 28.39 | - | - |
| test_operator[npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 704.64 | - | - |
| test_operator[npu2-Emit-eight_carried] | ✅ | 17.48 | - | - |
| test_operator[npu2-Emit-one_carried] | ✅ | 18.23 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-approximate_none] | ✅ | 24.68 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 30.66 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_8-num_channels_2-tile_size_128-approximate_none] | ✅ | 47.33 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 48.54 | - | - |
| test_operator[npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 534.38 | - | - |
| test_operator[npu2-GEMM-M_1792-K_896-N_1152-num_aie_columns_8-tile_m_64-tile_k_32-tile_n_48-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | 1674.68 | - | - |
| test_operator[npu2-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | 33.23 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | ✅ | 3007.59 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | 46062.07 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 27416.64 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_8-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | 6929.58 | - | - |
| test_operator[npu2-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | 623.29 | - | - |
| test_operator[npu2-GEMM-M_384-K_1536-N_1792-num_aie_columns_4-tile_m_32-tile_k_48-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 1701.84 | - | - |
| test_operator[npu2-GEMM-M_896-K_1792-N_640-num_aie_columns_8-tile_m_32-tile_k_64-tile_n_80-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | 873.22 | - | - |
| test_operator[npu2-GEMM-f32_out] | ✅ | 87.18 | - | - |
| test_operator[npu2-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 317.81 | - | - |
| test_operator[npu2-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_2] | ✅ | 614.59 | - | - |
| test_operator[npu2-GEMV-M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 167.95 | - | - |
| test_operator[npu2-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 21.17 | - | - |
| test_operator[npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64] | ✅ | 681.99 | - | - |
| test_operator[npu2-GEMV-M_2048-K_64-num_aie_columns_4-tile_size_input_4-tile_size_output_256-num_channels_2-num_batches_32-repeat_4] | ✅ | 240.90 | - | - |
| test_operator[npu2-GEMV-M_2048-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_256-num_batches_32-repeat_4] | ✅ | 240.98 | - | - |
| test_operator[npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 615.72 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 92.87 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_32-num_channels_2-num_batches_8] | ✅ | 57.56 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_4] | ✅ | 57.31 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_8-repeat_4] | ✅ | 96.99 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 687.37 | - | - |
| test_operator[npu2-GEMV-M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 1304.64 | - | - |
| test_operator[npu2-GEMV-M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 237.62 | - | - |
| test_operator[npu2-GEMV-M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 135.04 | - | - |
| test_operator[npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 618.24 | - | - |
| test_operator[npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2] | ✅ | 451.65 | - | - |
| test_operator[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 16.06 | - | - |
| test_operator[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 20.04 | - | - |
| test_operator[npu2-LayerNorm-rows_16-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 46.15 | - | - |
| test_operator[npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 505.10 | - | - |
| test_operator[npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 494.00 | - | - |
| test_operator[npu2-LayerNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 30.57 | - | - |
| test_operator[npu2-Limbs-rows_4096-line_320-num_aie_columns_8] | ✅ | 378.96 | - | - |
| test_operator[npu2-Limbs-rows_512-line_320-num_aie_columns_4] | ✅ | 72.19 | - | - |
| test_operator[npu2-Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | 25.19 | - | - |
| test_operator[npu2-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 28.23 | - | - |
| test_operator[npu2-Log-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 50.13 | - | - |
| test_operator[npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 3567.34 | - | - |
| test_operator[npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8] | ✅ | 31994.35 | - | - |
| test_operator[npu2-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | 179.28 | - | - |
| test_operator[npu2-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | 109.47 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | ✅ | 133.10 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_8-heads_interleaved_True] | ✅ | 2514.97 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_8] | ✅ | 35838.86 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_2-seq_len_2000-d_256-causal_False-window_512-num_pipelines_8] | ✅ | 17689.37 | - | - |
| test_operator[npu2-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | 109.09 | - | - |
| test_operator[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8] | ✅ | 25966.81 | - | - |
| test_operator[npu2-Magnitude-rows_4096-width_640-num_aie_columns_8] | ✅ | 819.32 | - | - |
| test_operator[npu2-Magnitude-rows_512-width_640-num_aie_columns_4] | ✅ | 218.53 | - | - |
| test_operator[npu2-Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | 118.46 | - | - |
| test_operator[npu2-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))-offset_True] | ✅ | 21.30 | - | - |
| test_operator[npu2-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))] | ✅ | 20.27 | - | - |
| test_operator[npu2-Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))] | ✅ | 27.42 | - | - |
| test_operator[npu2-Merge-rows_192-placeholders_((49190, 64),)] | ✅ | 19.10 | - | - |
| test_operator[npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))-offset_True] | ✅ | 92.32 | - | - |
| test_operator[npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | ✅ | 97.16 | - | - |
| test_operator[npu2-PatchPositions-rows_2048-out_height_480-out_width_1056-cores_8] | ✅ | 71.60 | - | - |
| test_operator[npu2-PatchPositions-rows_2304-out_height_768-out_width_768] | ✅ | 74.07 | - | - |
| test_operator[npu2-PatchPositions-rows_256-out_height_48-out_width_48] | ✅ | 28.90 | - | - |
| test_operator[npu2-PatchPositions-rows_2560-out_height_672-out_width_912] | ✅ | 70.82 | - | - |
| test_operator[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 16.46 | - | - |
| test_operator[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 17.64 | - | - |
| test_operator[npu2-RMSNorm-rows_16-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 44.98 | - | - |
| test_operator[npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 509.04 | - | - |
| test_operator[npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 503.58 | - | - |
| test_operator[npu2-RMSNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 25.82 | - | - |
| test_operator[npu2-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 16.13 | - | - |
| test_operator[npu2-ReLU-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 53.39 | - | - |
| test_operator[npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 501.21 | - | - |
| test_operator[npu2-Resample-height_3024-width_4032-out_height_672-out_width_912] | ✅ | 14465.50 | - | - |
| test_operator[npu2-Resample-height_37-width_53-out_height_96-out_width_144] | ✅ | 131.99 | - | - |
| test_operator[npu2-Resample-height_37-width_53-out_height_96-out_width_256] | ✅ | 160.12 | - | - |
| test_operator[npu2-Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4] | ✅ | 3904.97 | - | - |
| test_operator[npu2-Resample-height_6000-width_500-out_height_672-out_width_432] | ✅ | 10125.22 | - | - |
| test_operator[npu2-ResampleTaps-in_size_1-out_size_48-num_aie_columns_2] | ✅ | 311.67 | - | - |
| test_operator[npu2-ResampleTaps-in_size_17-out_size_1008] | ✅ | 1560.43 | - | - |
| test_operator[npu2-ResampleTaps-in_size_3024-out_size_672-words_356-slots_16] | ✅ | 3218.88 | - | - |
| test_operator[npu2-ResampleTaps-in_size_4032-out_size_912] | ✅ | 4157.72 | - | - |
| test_operator[npu2-ResampleTaps-in_size_8000-out_size_672-num_aie_columns_1-num_channels_1] | ✅ | 116392.29 | - | - |
| test_operator[npu2-ResampleTaps-in_size_961-out_size_960] | ✅ | 1439.36 | - | - |
| test_operator[npu2-RoPE-rows_32-cols_128-num_aie_columns_1-angle_rows_8-two_halves_False] | ✅ | 16.67 | - | - |
| test_operator[npu2-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | 21.85 | - | - |
| test_operator[npu2-RoPE-rows_32-cols_512-num_aie_columns_8-angle_rows_32] | ✅ | 30.93 | - | - |
| test_operator[npu2-RoPE-rows_4096-cols_512-angle_rows_8] | ✅ | 149.98 | - | - |
| test_operator[npu2-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 14.87 | - | - |
| test_operator[npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | ✅ | 513.23 | - | - |
| test_operator[npu2-RowwiseAdd-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 22.43 | - | - |
| test_operator[npu2-RowwiseAdd-wide_row] | ✅ | 45.61 | - | - |
| test_operator[npu2-RowwiseAdd-wider_row] | ✅ | 30.12 | - | - |
| test_operator[npu2-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 21.96 | - | - |
| test_operator[npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | ✅ | 508.82 | - | - |
| test_operator[npu2-RowwiseMul-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 23.96 | - | - |
| test_operator[npu2-RowwiseMul-wide_row] | ✅ | 54.89 | - | - |
| test_operator[npu2-RowwiseMul-wider_row] | ✅ | 27.16 | - | - |
| test_operator[npu2-Sample-llama] | ✅ | 199.24 | - | - |
| test_operator[npu2-Sample-padded] | ✅ | 210.08 | - | - |
| test_operator[npu2-Sample-small] | ✅ | 105.82 | - | - |
| test_operator[npu2-Sample-two_cores] | ✅ | 77.92 | - | - |
| test_operator[npu2-Sample-uneven] | ✅ | 114.96 | - | - |
| test_operator[npu2-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | 20.20 | - | - |
| test_operator[npu2-SiLU-size_2048-num_aie_columns_8-tile_size_256] | ✅ | 22.16 | - | - |
| test_operator[npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 521.29 | - | - |
| test_operator[npu2-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 17.36 | - | - |
| test_operator[npu2-Sigmoid-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 48.82 | - | - |
| test_operator[npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 499.64 | - | - |
| test_operator[npu2-Softmax-f32_soft_cap_banded_addend] | ✅ | 26.51 | - | - |
| test_operator[npu2-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | ✅ | 30.68 | - | - |
| test_operator[npu2-Softmax-rows_16-cols_4608-num_aie_columns_2-num_channels_2] | ✅ | 33.39 | - | - |
| test_operator[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | ✅ | 61.93 | - | - |
| test_operator[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | 20.34 | - | - |
| test_operator[npu2-Softmax-rows_32-cols_32768-num_aie_columns_2-num_channels_2] | ✅ | 254.96 | - | - |
| test_operator[npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2] | ✅ | 264.90 | - | - |
| test_operator[npu2-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 18.63 | - | - |
| test_operator[npu2-Tanh-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 49.76 | - | - |
| test_operator[npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 501.17 | - | - |
| test_operator[npu2-flm.DequantBFP-K_1024-N_1024-run_out_features_512-run_period_out_features_1024] | ✅ | 85.23 | - | - |
| test_operator[npu2-flm.DequantBFP-K_1024-N_512] | ✅ | 52.97 | - | - |
| test_operator[npu2-flm.DequantBFP-K_4096-N_1536] | ✅ | 424.91 | - | - |
| test_operator[npu2-flm.DequantBFP-K_512-N_128] | ✅ | 21.08 | - | - |
| test_operator[npu2-flm.DequantBFP-K_6144-N_1536] | ✅ | 630.57 | - | - |
| test_operator[npu2-flm.LMHead-dim_1536-vocab_1024-softcap_5.0] | ✅ | 48.03 | - | - |
| test_operator[npu2-flm.LMHead-dim_1536-vocab_4096-softcap_30.0] | ✅ | 465.39 | - | - |
| test_operator[npu2-flm.LMHead-dim_2560-vocab_4096-softcap_30.0] | ✅ | -25.38 | - | - |
| test_patch_positions_that_do_not_tile_are_refused[more_patches_than_rows] | ✅ | - | ✅ | - |
| test_patch_positions_that_do_not_tile_are_refused[not_whole_windows] | ✅ | - | ✅ | - |
| test_patch_positions_that_do_not_tile_are_refused[rows_not_whole_blocks] | ✅ | - | ✅ | - |
| test_reference_matches_device_convention_across_shapes[test_reference_matches_device_convention_across_shapes] | ✅ | - | ✅ | - |
| test_rows_a_state_names_are_gathered[n_ids_1] | ✅ | - | - | - |
| test_rows_a_state_names_are_gathered[n_ids_256] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[full_elf-llama] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[full_elf-unaligned] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[full_elf-vision] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[xclbin-llama] | ✅ | - | ✅ | - |
| test_rows_are_masked_to_the_per_call_length[xclbin-unaligned] | ✅ | - | ✅ | - |
| test_rows_are_masked_to_the_per_call_length[xclbin-vision] | ✅ | - | ✅ | - |
| test_rows_each_call_names_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_rows_each_call_names_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_rows_each_call_names_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_None-n_ids_1] | ✅ | - | - | - |
| test_rows_of_a_weight_are_gathered[test_rows_of_a_weight_are_gathered] | ✅ | - | - | - |
| test_rows_of_an_intermediate_are_gathered[test_rows_of_an_intermediate_are_gathered] | ✅ | - | - | - |
| test_rows_past_the_valid_length_are_zero[causal] | ✅ | - | - | - |
| test_rows_past_the_valid_length_are_zero[global] | ✅ | - | - | - |
| test_rows_past_the_valid_length_are_zero[sliding] | ✅ | - | - | - |
| test_sample_over_an_odd_vocab_is_refused[test_sample_over_an_odd_vocab_is_refused] | ✅ | - | ✅ | - |
| test_sample_with_more_cores_than_a_memtile_joins_is_refused[test_sample_with_more_cores_than_a_memtile_joins_is_refused] | ✅ | - | ✅ | - |
| test_softmax_with_no_column_count_that_tiles_is_refused[test_softmax_with_no_column_count_that_tiles_is_refused] | ✅ | - | ✅ | - |
| test_the_bound_rows_are_what_moves[n_1] | ✅ | - | ✅ | - |
| test_the_bound_rows_are_what_moves[n_256] | ✅ | - | ✅ | - |
| test_the_bound_rows_are_what_moves[n_40] | ✅ | - | ✅ | - |
| test_the_bound_rows_turn_on_the_device[test_the_bound_rows_turn_on_the_device] | ✅ | - | - | - |
| test_the_cache_offset_is_applied_per_call[test_the_cache_offset_is_applied_per_call] | ✅ | - | - | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_144-device_npu1] | ✅ | - | ✅ | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_144-device_npu2] | ✅ | - | ✅ | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_256-device_npu1] | ✅ | - | ✅ | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_256-device_npu2] | ✅ | - | ✅ | - |
| test_the_offset_moves_every_piece_of_a_split_pattern[test_the_offset_moves_every_piece_of_a_split_pattern] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_accurate-full_elf] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_accurate-xclbin] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_b_col_maj-full_elf] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_b_col_maj-xclbin] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_medium-full_elf] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_medium-xclbin] | ✅ | - | - | - |
| test_the_reference_scores_a_long_cache_a_few_rows_at_a_time[test_the_reference_scores_a_long_cache_a_few_rows_at_a_time] | ✅ | - | ✅ | - |
| test_the_rows_a_call_bounds_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_by_ids_the_device_made_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_by_ids_the_device_made_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_by_ids_the_device_made_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_the_rows_of_a_bound_are_computed[full_elf] | ✅ | - | - | - |
| test_the_rows_of_a_bound_are_computed[xclbin] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-qwen2_down] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-qwen2_up] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-resident_b] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-streamed_b] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-qwen2_down] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-qwen2_up] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-resident_b] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-streamed_b] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_a_bounded_row_is_rejected[test_transfer_size_not_dividing_a_bounded_row_is_rejected] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_the_per_channel_share_is_rejected[test_transfer_size_not_dividing_the_per_channel_share_is_rejected] | ✅ | - | ✅ | - |
| test_walks_in_turn_are_their_reference[band_stride_0] | ✅ | - | ✅ | - |
| test_walks_in_turn_are_their_reference[band_stride_1] | ✅ | - | ✅ | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_0-full_elf] | ✅ | - | - | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_0-xclbin] | ✅ | - | - | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_1-full_elf] | ✅ | - | - | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_1-xclbin] | ✅ | - | - | - |
| test_what_lies_past_the_bound_does_not_reach_the_output[test_what_lies_past_the_bound_does_not_reach_the_output] | ✅ | - | - | - |

</details>

<details>
<summary>iron/tests/toolchain</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_bounded_operator_lowers[device_npu1-gemm-GEMM--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-mha-MHA--kv_valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-mha-MHA--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-relu-ReLU--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-rms_norm-RMSNorm--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-rope-RoPE--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-softmax-Softmax--length] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-gemm-GEMM--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-mha-MHA--kv_valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-mha-MHA--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-relu-ReLU--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-rms_norm-RMSNorm--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-rope-RoPE--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-softmax-Softmax--length] | ✅ | - | ✅ | - |
| test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with[test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with] | ✅ | - | ✅ | - |
| test_a_declared_operator_compiles_to_an_xclbin_on_npu1[test_a_declared_operator_compiles_to_an_xclbin_on_npu1] | ✅ | - | ✅ | - |
| test_a_graph_called_in_a_graph_lowers[device_npu1] | ✅ | - | ✅ | - |
| test_a_graph_called_in_a_graph_lowers[device_npu2] | ✅ | - | ✅ | - |
| test_a_graph_compiles_to_one_xclbin_per_operator_chained[device_npu1] | ✅ | - | ✅ | - |
| test_a_graph_compiles_to_one_xclbin_per_operator_chained[device_npu2] | ✅ | - | ✅ | - |
| test_a_per_call_size_over_one_block_builds_at_each_step[test_a_per_call_size_over_one_block_builds_at_each_step] | ✅ | - | ✅ | - |
| test_a_scratch_arena_past_a_bank_links_as_its_banks[test_a_scratch_arena_past_a_bank_links_as_its_banks] | ✅ | - | ✅ | - |
| test_an_inline_kernel_lowers[device_npu1] | ✅ | - | ✅ | - |
| test_an_inline_kernel_lowers[device_npu2] | ✅ | - | ✅ | - |
| test_attention_over_a_128k_cache_lowers[rows_decode] | ✅ | - | ✅ | - |
| test_attention_over_a_128k_cache_lowers[rows_prompt] | ✅ | - | ✅ | - |
| test_convolutions_called_in_a_graph_lower[device_npu1] | ✅ | - | ✅ | - |
| test_convolutions_called_in_a_graph_lower[device_npu2] | ✅ | - | ✅ | - |
| test_decode_graph_builds_a_full_elf_with_its_values_in_the_table[test_decode_graph_builds_a_full_elf_with_its_values_in_the_table] | ✅ | - | ✅ | - |
| test_decode_graph_operators_lower_with_their_values[test_decode_graph_operators_lower_with_their_values] | ✅ | - | ✅ | - |
| test_each_call_softmaxes_its_columns_and_copies_them_into_its_slot[test_each_call_softmaxes_its_columns_and_copies_them_into_its_slot] | ✅ | - | - | - |
| test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions[test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions] | ✅ | - | ✅ | - |
| test_flm_gemm_lowers_and_so_does_its_configuration_module[base] | ✅ | - | ✅ | - |
| test_flm_gemm_lowers_and_so_does_its_configuration_module[n10240] | ✅ | - | ✅ | - |
| test_flm_gemm_lowers_and_so_does_its_configuration_module[tn128] | ✅ | - | ✅ | - |
| test_image_patches_called_in_a_graph_lower[device_npu1] | ✅ | - | ✅ | - |
| test_image_patches_called_in_a_graph_lower[device_npu2] | ✅ | - | ✅ | - |
| test_instructions_compile_alone_against_an_external_image[test_instructions_compile_alone_against_an_external_image] | ✅ | - | ✅ | - |
| test_its_reference_is_the_contracts[device_npu1] | ✅ | - | ✅ | - |
| test_its_reference_is_the_contracts[device_npu2] | ✅ | - | ✅ | - |
| test_no_scratch_buffer_crosses_a_bank[test_no_scratch_buffer_crosses_a_bank] | ✅ | - | ✅ | - |
| test_npu1_compiles_each_step_unasked[test_npu1_compiles_each_step_unasked] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-by_head_two_channels] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-contiguous] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-float32] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-slot5] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Emit-one_carried] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-f32_out] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-PatchPositions-rows_2560-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Resample-height_3024-width_4032-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ResampleTaps-in_size_4032-out_size_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseAdd-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseMul-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sample-padded] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sample-small] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sample-uneven] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-by_head_two_channels] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-contiguous] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-float32] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-slot5] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Emit-one_carried] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_1792-K_896-N_1152-num_aie_columns_8-tile_m_64-tile_k_32-tile_n_48-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_8-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_896-K_1792-N_640-num_aie_columns_8-tile_m_32-tile_k_64-tile_n_80-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-f32_out] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_8-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-PatchPositions-rows_2560-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Resample-height_3024-width_4032-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ResampleTaps-in_size_4032-out_size_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseAdd-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseMul-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sample-padded] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sample-small] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sample-uneven] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-flm.DequantBFP-K_512-N_128] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-flm.LMHead-dim_1536-vocab_4096-softcap_30.0] | ✅ | - | ✅ | - |
| test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table[test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table] | ✅ | - | ✅ | - |
| test_prefill_graph_operators_lower_with_their_value[test_prefill_graph_operators_lower_with_their_value] | ✅ | - | ✅ | - |
| test_prefill_steps_lower_at_llama_size[down_projection_checkpoint_layout] | ✅ | - | ✅ | - |
| test_prefill_steps_lower_at_llama_size[kv_into_cache] | ✅ | - | ✅ | - |
| test_prefill_steps_lower_at_llama_size[mha_in_the_projections_layout] | ✅ | - | ✅ | - |
| test_shipped_builds_its_instructions_for_the_external_image[test_shipped_builds_its_instructions_for_the_external_image] | ✅ | - | ✅ | - |
| test_shipped_external_sequence_lowers[test_shipped_external_sequence_lowers] | ✅ | - | ✅ | - |
| test_shipped_fetches_its_image[test_shipped_fetches_its_image] | ✅ | - | ✅ | - |
| test_swiglu_graph_compiles_to_a_full_elf[test_swiglu_graph_compiles_to_a_full_elf] | ✅ | - | ✅ | - |
| test_swiglu_graphs_operators_lower[test_swiglu_graphs_operators_lower] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-elementwise_add-ElementwiseAdd--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-gemm-GEMM--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-gemv-GEMV--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-rope-RoPE--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-softmax-Softmax--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-elementwise_add-ElementwiseAdd--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-gemm-GEMM--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-gemv-GEMV--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-rope-RoPE--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-softmax-Softmax--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[elementwise_add-ElementwiseAdd--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[gemm-GEMM--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[gemv-GEMV--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[rope-RoPE--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[softmax-Softmax--] | ✅ | - | ✅ | - |
| test_values_become_dispatch_time_kernels_at_each_step[device_npu1] | ✅ | - | ✅ | - |
| test_values_become_dispatch_time_kernels_at_each_step[device_npu2] | ✅ | - | ✅ | - |

</details>

## Extensive

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_one_xclbin_serves_every_shape[test_one_xclbin_serves_every_shape] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[test_output_feeds_gemm_unchanged] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even] | - | - | ✅ | 6653.59 |
| test_gemm[npu1-M_16384-K_512-N_256-epilogue_none-rounding_conv_even] | - | - | ✅ | 3323.36 |
| test_gemm[npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even] | - | - | ✅ | 5593.56 |
| test_gemm[npu1-M_256-K_512-N_128-epilogue_none-rounding_conv_even] | - | - | ✅ | 86.44 |
| test_gemm[npu1-M_256-K_512-N_256-epilogue_none-rounding_conv_even] | - | - | ✅ | 95.44 |
| test_gemm[npu1-M_256-K_512-N_320-epilogue_none-rounding_conv_even] | - | - | ✅ | 128.52 |
| test_gemm[npu1-M_256-K_512-N_512-epilogue_gelu-rounding_conv_even] | - | - | ✅ | 139.17 |
| test_gemm[npu1-M_256-K_512-N_512-epilogue_none-rounding_floor] | - | - | ✅ | 134.17 |
| test_gemm[npu1-M_256-K_512-N_512-epilogue_sigmoid-rounding_conv_even] | - | - | ✅ | 146.66 |
| test_gemm[npu1-M_256-K_512-N_512-epilogue_silu-rounding_conv_even] | - | - | ✅ | 146.76 |
| test_gemm[npu1-M_256-K_512-N_64-epilogue_none-rounding_conv_even] | - | - | ✅ | 79.41 |
| test_gemm[npu2-M_1024-K_10240-N_2560-epilogue_none-rounding_conv_even] | ✅ | 3526.82 | - | - |
| test_gemm[npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even] | ✅ | 2873.85 | - | - |
| test_gemm[npu2-M_16384-K_512-N_1024-epilogue_none-rounding_conv_even] | ✅ | 1248.58 | - | - |
| test_gemm[npu2-M_2048-K_1024-N_16-epilogue_none-rounding_conv_even] | ✅ | 120.25 | - | - |
| test_gemm[npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even] | ✅ | 5422.85 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_gelu-rounding_conv_even] | ✅ | 74.18 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_none-rounding_conv_even] | ✅ | 76.12 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_none-rounding_floor] | ✅ | 74.79 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_sigmoid-rounding_conv_even] | ✅ | 75.07 | - | - |
| test_gemm[npu2-M_256-K_512-N_1024-epilogue_silu-rounding_conv_even] | ✅ | 73.61 | - | - |
| test_gemm[npu2-M_256-K_512-N_128-epilogue_none-rounding_conv_even] | ✅ | 56.46 | - | - |
| test_gemm[npu2-M_256-K_512-N_1536-epilogue_none-rounding_conv_even] | ✅ | 85.32 | - | - |
| test_gemm_b_col_maj[npu1-resident-high] | - | - | ✅ | 88.56 |
| test_gemm_b_col_maj[npu1-slabs-high] | - | - | ✅ | 3144.84 |
| test_gemm_b_col_maj[npu1-streamed-high] | - | - | ✅ | 660.41 |
| test_gemm_b_col_maj[npu1-tables-linked-high] | - | - | ✅ | 101.49 |
| test_gemm_b_col_maj[npu1-tn128-high] | - | - | ✅ | 161.44 |
| test_gemm_b_col_maj[npu1-tn16-high] | - | - | ✅ | 80.04 |
| test_gemm_b_col_maj[npu1-tn32-high] | - | - | ✅ | 63.68 |
| test_gemm_b_col_maj[npu1-trailing-col-high] | - | - | ✅ | 103.35 |
| test_gemm_b_col_maj[npu2-resident-high] | ✅ | 107.30 | - | - |
| test_gemm_b_col_maj[npu2-resident-medium] | ✅ | 65.17 | - | - |
| test_gemm_b_col_maj[npu2-slabs-high] | ✅ | 3254.74 | - | - |
| test_gemm_b_col_maj[npu2-slabs-medium] | ✅ | 667.71 | - | - |
| test_gemm_b_col_maj[npu2-streamed-high] | ✅ | 1242.16 | - | - |
| test_gemm_b_col_maj[npu2-streamed-medium] | ✅ | 299.86 | - | - |
| test_gemm_b_col_maj[npu2-tables-linked-high] | ✅ | 107.22 | - | - |
| test_gemm_b_col_maj[npu2-tables-linked-medium] | ✅ | 59.15 | - | - |
| test_gemm_b_col_maj[npu2-tn128-high] | ✅ | 174.78 | - | - |
| test_gemm_b_col_maj[npu2-tn128-medium] | ✅ | 85.78 | - | - |
| test_gemm_b_col_maj[npu2-tn16-high] | ✅ | 62.81 | - | - |
| test_gemm_b_col_maj[npu2-tn16-medium] | ✅ | 54.43 | - | - |
| test_gemm_b_col_maj[npu2-tn32-high] | ✅ | 81.37 | - | - |
| test_gemm_b_col_maj[npu2-tn32-medium] | ✅ | 57.10 | - | - |
| test_gemm_b_col_maj[npu2-trailing-col-high] | ✅ | 144.20 | - | - |
| test_gemm_b_col_maj[npu2-trailing-col-medium] | ✅ | 68.26 | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_256-K_512-N_1024] | ✅ | - | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_256] | ✅ | - | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_6144] | ✅ | - | - | - |
| test_gemm_k_slices[npu1-ck128] | - | - | ✅ | - |
| test_gemm_k_slices[npu1-ck16] | - | - | ✅ | - |
| test_gemm_k_slices[npu1-ck32] | - | - | ✅ | - |
| test_gemm_k_slices[npu1-ck8] | - | - | ✅ | - |
| test_gemm_k_slices[npu1-default] | - | - | ✅ | - |
| test_gemm_k_slices[npu2-ck16] | ✅ | - | - | - |
| test_gemm_k_slices[npu2-ck256] | ✅ | - | - | - |
| test_gemm_k_slices[npu2-ck32] | ✅ | - | - | - |
| test_gemm_k_slices[npu2-ck64] | ✅ | - | - | - |
| test_gemm_k_slices[npu2-ck8] | ✅ | - | - | - |
| test_gemm_k_slices[npu2-default] | ✅ | - | - | - |
| test_gemm_k_tile[K_256] | ✅ | - | ✅ | - |
| test_gemm_k_tile[K_768] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_16-tile_n_16-k_tile_16-ct_k_16-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_16-tile_n_16-k_tile_16-ct_k_16-medium] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_512-tile_n_64-k_tile_128-ct_k_128-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_512-tile_n_64-k_tile_128-ct_k_128-medium] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_64-tile_n_32-k_tile_64-ct_k_32-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_64-tile_n_32-k_tile_64-ct_k_32-medium] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_96-tile_n_32-k_tile_96-ct_k_32-high] | ✅ | - | ✅ | - |
| test_gemm_k_tile_of_few_chunks[K_96-tile_n_32-k_tile_96-ct_k_32-medium] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[test_gemm_split_leg_bounds_runs] | ✅ | - | ✅ | - |
| test_gemm_tile_options[npu1-tn128-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn128-ma16] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn128-ma64] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn16-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn16-ma16] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn16-ma64] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn32-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn32-ma16] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn32-ma64] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn64-default] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn64-ma16] | - | - | ✅ | - |
| test_gemm_tile_options[npu1-tn64-ma32] | - | - | ✅ | - |
| test_gemm_tile_options[npu2-tn128-default] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn128-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn128-ma64] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn16-default] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn16-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn16-ma64] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn32-default] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn32-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn32-ma64] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn64-default] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn64-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[npu2-tn64-ma64] | ✅ | - | - | - |
| test_gemm_without_activations[M_256-K_512-N_256] | ✅ | 52.75 | ✅ | 85.67 |
| test_gemm_without_activations[M_512-K_1024-N_512] | ✅ | 83.34 | ✅ | 298.07 |
| test_one_xclbin_serves_every_shape[test_one_xclbin_serves_every_shape] | ✅ | - | ✅ | - |
| test_shipped_epilogue_matches_accumulator[epilogue_sigmoid] | ✅ | - | - | - |
| test_shipped_epilogue_matches_accumulator[epilogue_silu] | ✅ | - | - | - |
| test_shipped_overlay[M_256-K_512-N_1024-epilogue_gelu] | ✅ | 129.29 | - | - |
| test_shipped_overlay[M_256-K_512-N_1024-epilogue_none] | ✅ | 121.99 | - | - |
| test_shipped_overlay[M_256-K_512-N_1024-epilogue_silu] | ✅ | 120.23 | - | - |
| test_shipped_overlay[M_256-K_512-N_1280-epilogue_none] | ✅ | 153.51 | - | - |
| test_shipped_overlay[M_256-K_512-N_640-epilogue_none] | ✅ | 119.34 | - | - |
| test_shipped_overlay[M_512-K_1024-N_2048-epilogue_none] | ✅ | 346.12 | - | - |

</details>

<details>
<summary>iron/operators/flm/layer</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_types_take_turns[test_layer_types_take_turns] | ✅ | - | - | - |
| test_matches_reference[gemma4_e2b-global-5] | ✅ | 605.81 | - | - |
| test_matches_reference[gemma4_e2b-global-700] | ✅ | 678.81 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-37] | ✅ | 833.06 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-700] | ✅ | 912.26 | - | - |
| test_matches_reference[gemma4_e2b-swa-1023] | ✅ | 557.74 | - | - |
| test_matches_reference[gemma4_e2b-swa-37] | ✅ | 537.88 | - | - |
| test_matches_reference[gemma4_e2b-swa-511] | ✅ | 583.12 | - | - |
| test_matches_reference[gemma4_e2b-swa-512] | ✅ | 550.81 | - | - |
| test_matches_reference[gemma4_e2b-swa-700] | ✅ | 571.22 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-1023] | ✅ | 818.44 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-37] | ✅ | 744.25 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-511] | ✅ | 793.49 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-512] | ✅ | 804.89 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-700] | ✅ | 823.08 | - | - |
| test_matches_reference[gemma4_e4b-global-5] | ✅ | 1317.29 | - | - |
| test_matches_reference[gemma4_e4b-global-700] | ✅ | 1394.37 | - | - |
| test_matches_reference[gemma4_e4b-global_skip-37] | ✅ | 1300.97 | - | - |
| test_matches_reference[gemma4_e4b-global_skip-700] | ✅ | 1383.60 | - | - |
| test_matches_reference[gemma4_e4b-swa-1023] | ✅ | 1193.83 | - | - |
| test_matches_reference[gemma4_e4b-swa-37] | ✅ | 1188.58 | - | - |
| test_matches_reference[gemma4_e4b-swa-511] | ✅ | 1182.86 | - | - |
| test_matches_reference[gemma4_e4b-swa-512] | ✅ | 1177.46 | - | - |
| test_matches_reference[gemma4_e4b-swa-700] | ✅ | 1225.00 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-1023] | ✅ | 1168.18 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-37] | ✅ | 1163.68 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-511] | ✅ | 1168.63 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-512] | ✅ | 1181.04 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-700] | ✅ | 1193.05 | - | - |
| test_refuses_unservable_contexts[layer_type_global-context_len_-1-max_l_1024-match_context_len must be >= 0] | ✅ | - | - | - |
| test_refuses_unservable_contexts[layer_type_global-context_len_1024-max_l_1024-match_context_len must be below max_l] | ✅ | - | - | - |
| test_refuses_unservable_contexts[layer_type_swa-context_len_37-max_l_65536-match_max_l exceeds 32768] | ✅ | - | - | - |
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
| test_projection_matches_reference[dim_1536] | ✅ | - | - | - |
| test_projection_matches_reference[dim_2560] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/prefill_attn</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemma4_cache_bound[kind_attn-num_kv_heads_1] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_attn-num_kv_heads_2] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_swa-num_kv_heads_1] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_swa-num_kv_heads_2] | ✅ | - | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | -3072.32 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 271.01 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 662.20 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | -88.32 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1734.52 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 4393.28 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 917.37 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 115.23 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 113.71 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 674.75 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 1871.54 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 925.93 | - | - |
| test_one_image_serves_every_range[kind_attn] | ✅ | - | - | - |
| test_one_image_serves_every_range[kind_swa] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_-128-L_end_256-max_l_1024-match_L_begin must be >= 0] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_0-L_end_200-max_l_1024-match_L_end must be a multiple of 128] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_0-L_end_256-max_l_2048-match_max_l exceeds max_context] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_0-L_end_512-max_l_256-match_slice stop exceeds the dimension] | ✅ | - | - | - |
| test_refuses_unservable_ranges[L_begin_64-L_end_256-max_l_1024-match_L_begin must be a multiple of 128] | ✅ | - | - | - |

</details>

<details>
<summary>iron/tests/common</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| TestLlama::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks] | ✅ | - | ✅ | - |
| TestLlama::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token] | ✅ | - | ✅ | - |
| TestLlama::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves] | ✅ | - | ✅ | - |
| TestLlama::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference] | ✅ | - | ✅ | - |
| TestLlama::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic] | ✅ | - | ✅ | - |
| TestLlama::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches] | ✅ | - | ✅ | - |
| test_a_block_float_tile_is_sized_by_its_blocks[test_a_block_float_tile_is_sized_by_its_blocks] | ✅ | - | ✅ | - |
| test_a_body_of_args_with_no_signature_is_refused_as_its_class_is_made[test_a_body_of_args_with_no_signature_is_refused_as_its_class_is_made] | ✅ | - | ✅ | - |
| test_a_bound_is_refused_where_no_extent_takes_it[test_a_bound_is_refused_where_no_extent_takes_it] | ✅ | - | ✅ | - |
| test_a_bound_on_one_side_of_a_copy_holds_the_other[test_a_bound_on_one_side_of_a_copy_holds_the_other] | ✅ | - | ✅ | - |
| test_a_bound_travels_through_reshape_and_transpose[test_a_bound_travels_through_reshape_and_transpose] | ✅ | - | ✅ | - |
| test_a_bound_value_is_its_member_on_the_instance[test_a_bound_value_is_its_member_on_the_instance] | ✅ | - | ✅ | - |
| test_a_bound_value_survives_tuning[test_a_bound_value_survives_tuning] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-llama_q] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-qwen2_down] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-qwen2_up] | ✅ | - | ✅ | - |
| test_a_bounded_flm_gemm_refuses_a_call_with_no_rows[test_a_bounded_flm_gemm_refuses_a_call_with_no_rows] | ✅ | - | ✅ | - |
| test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin[test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin] | ✅ | - | ✅ | - |
| test_a_bounded_operand_binds_the_extent_and_what_derives_from_it[test_a_bounded_operand_binds_the_extent_and_what_derives_from_it] | ✅ | - | ✅ | - |
| test_a_bounded_operand_goes_round_robin_over_the_lanes[test_a_bounded_operand_goes_round_robin_over_the_lanes] | ✅ | - | ✅ | - |
| test_a_bounded_operand_makes_the_trip_count_per_call[test_a_bounded_operand_makes_the_trip_count_per_call] | ✅ | - | ✅ | - |
| test_a_bounded_rope_lane_takes_whole_positions_and_their_angles[test_a_bounded_rope_lane_takes_whole_positions_and_their_angles] | ✅ | - | ✅ | - |
| test_a_bounded_step_ends_no_command[test_a_bounded_step_ends_no_command] | ✅ | - | ✅ | - |
| test_a_bounded_view_of_a_state_is_its_rows_this_call[test_a_bounded_view_of_a_state_is_its_rows_this_call] | ✅ | - | ✅ | - |
| test_a_call_skips_the_commands_its_values_leave_without_work[test_a_call_skips_the_commands_its_values_leave_without_work] | ✅ | - | ✅ | - |
| test_a_called_graph_records_into_its_caller[test_a_called_graph_records_into_its_caller] | ✅ | - | ✅ | - |
| test_a_called_graph_takes_every_value_and_carries_none[test_a_called_graph_takes_every_value_and_carries_none] | ✅ | - | ✅ | - |
| test_a_called_graph_writes_a_given_output_bounded_by_its_callers_value[test_a_called_graph_writes_a_given_output_bounded_by_its_callers_value] | ✅ | - | ✅ | - |
| test_a_caller_bounds_its_rows[test_a_caller_bounds_its_rows] | ✅ | - | ✅ | - |
| test_a_caller_records_and_bounds_it[test_a_caller_records_and_bounds_it] | ✅ | - | ✅ | - |
| test_a_carried_handle_may_also_be_returned[test_a_carried_handle_may_also_be_returned] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Copy-contiguous] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Emit-one_carried] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[PatchPositions-rows_2304-out_height_768-out_width_768] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ResampleTaps-in_size_17-out_size_1008] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Sample-small] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[flm.DequantBFP-K_512-N_128] | ✅ | - | ✅ | - |
| test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[flm.LMHead-dim_1536-vocab_4096-softcap_30.0] | ✅ | - | ✅ | - |
| test_a_causal_model_s_versions_and_signature[test_a_causal_model_s_versions_and_signature] | ✅ | - | ✅ | - |
| test_a_channel_count_no_column_fits_adds_no_grid[test_a_channel_count_no_column_fits_adds_no_grid] | ✅ | - | ✅ | - |
| test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_<|bos|>] | ✅ | - | ✅ | - |
| test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_] | ✅ | - | ✅ | - |
| test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_{{ bos_token }}] | ✅ | - | ✅ | - |
| test_a_chat_template_jinja_file_is_read_and_may_call_strftime_now[test_a_chat_template_jinja_file_is_read_and_may_call_strftime_now] | ✅ | - | ✅ | - |
| test_a_chat_template_jinja_file_is_read_over_tokenizer_config_s[test_a_chat_template_jinja_file_is_read_over_tokenizer_config_s] | ✅ | - | ✅ | - |
| test_a_chat_template_s_raise_exception_raises_its_message[test_a_chat_template_s_raise_exception_raises_its_message] | ✅ | - | ✅ | - |
| test_a_chat_template_writes_tokenizer_config_s_bos_token[given_<s>-written_<s>] | ✅ | - | ✅ | - |
| test_a_chat_template_writes_tokenizer_config_s_bos_token[given_None-written_] | ✅ | - | ✅ | - |
| test_a_chat_template_writes_tokenizer_config_s_bos_token[given_{'content': '<s>'}-written_<s>] | ✅ | - | ✅ | - |
| test_a_checkpoint_s_golden_is_refused_once_it_changes[change_config] | ✅ | - | ✅ | - |
| test_a_checkpoint_s_golden_is_refused_once_it_changes[change_first weight] | ✅ | - | ✅ | - |
| test_a_checkpoint_s_golden_is_refused_once_it_changes[change_last weight] | ✅ | - | ✅ | - |
| test_a_column_major_product_is_read_as_stored_by_the_next_reference[test_a_column_major_product_is_read_as_stored_by_the_next_reference] | ✅ | - | ✅ | - |
| test_a_command_reads_at_most_a_scratchpads_words[test_a_command_reads_at_most_a_scratchpads_words] | ✅ | - | ✅ | - |
| test_a_config_whose_application_states_no_precision_is_refused[test_a_config_whose_application_states_no_precision_is_refused] | ✅ | - | ✅ | - |
| test_a_context_no_chunk_divides_is_allocated_exactly[test_a_context_no_chunk_divides_is_allocated_exactly] | ✅ | - | ✅ | - |
| test_a_context_no_chunk_divides_runs_to_its_last_position[test_a_context_no_chunk_divides_runs_to_its_last_position] | ✅ | - | ✅ | - |
| test_a_decoder_without_rope_places_its_positions_through_the_hook[test_a_decoder_without_rope_places_its_positions_through_the_hook] | ✅ | - | ✅ | - |
| test_a_derive_that_fails_for_another_reason_than_resolution_raises[test_a_derive_that_fails_for_another_reason_than_resolution_raises] | ✅ | - | ✅ | - |
| test_a_derived_value_is_written_once_per_build[test_a_derived_value_is_written_once_per_build] | ✅ | - | ✅ | - |
| test_a_design_is_keyed_by_what_it_builds[test_a_design_is_keyed_by_what_it_builds] | ✅ | - | ✅ | - |
| test_a_difference_is_one_axpy_and_a_number_less_a_handle_two_steps[test_a_difference_is_one_axpy_and_a_number_less_a_handle_two_steps] | ✅ | - | ✅ | - |
| test_a_fetch_refuses_plain_http_and_a_download_of_another_digest[test_a_fetch_refuses_plain_http_and_a_download_of_another_digest] | ✅ | - | ✅ | - |
| test_a_fetch_reuses_a_file_of_the_pinned_digest[test_a_fetch_reuses_a_file_of_the_pinned_digest] | ✅ | - | ✅ | - |
| test_a_field_added_at_its_default_keeps_the_fingerprint[test_a_field_added_at_its_default_keeps_the_fingerprint] | ✅ | - | ✅ | - |
| test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known[test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known] | ✅ | - | ✅ | - |
| test_a_file_of_other_inputs_is_refused_and_rerecorded[test_a_file_of_other_inputs_is_refused_and_rerecorded] | ✅ | - | ✅ | - |
| test_a_float32_product_is_not_rounded_to_its_inputs_dtype[test_a_float32_product_is_not_rounded_to_its_inputs_dtype] | ✅ | - | ✅ | - |
| test_a_forced_xclbin_is_derived_and_says_why[test_a_forced_xclbin_is_derived_and_says_why] | ✅ | - | ✅ | - |
| test_a_full_elf_ends_a_command_at_a_host_step[test_a_full_elf_ends_a_command_at_a_host_step] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_(array([0, 1]), slice(0, 4, None))-match_whole of every axis] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[ 0 64]-match_gathering] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[-65]-match_gathering] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[0. 1.]-match_1-D integer array] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[[0 1]]-match_1-D integer array] | ✅ | - | ✅ | - |
| test_a_gather_refuses_what_it_cannot_lower[index_[]-match_gathering] | ✅ | - | ✅ | - |
| test_a_generation_block_renders_its_body[test_a_generation_block_renders_its_body] | ✅ | - | ✅ | - |
| test_a_generation_s_timings_are_the_model_s_stats[test_a_generation_s_timings_are_the_model_s_stats] | ✅ | - | ✅ | - |
| test_a_given_output_of_another_rank_is_refused_unless_declared_flat[test_a_given_output_of_another_rank_is_refused_unless_declared_flat] | ✅ | - | ✅ | - |
| test_a_graph_carries_its_next_values[test_a_graph_carries_its_next_values] | ✅ | - | ✅ | - |
| test_a_graph_carries_its_profile[test_a_graph_carries_its_profile] | ✅ | - | ✅ | - |
| test_a_graph_names_its_inputs_and_values_in_signature[count_2] | ✅ | - | ✅ | - |
| test_a_graph_names_its_inputs_and_values_in_signature[count_3] | ✅ | - | ✅ | - |
| test_a_graph_reads_as_its_name_and_recorded_shapes[test_a_graph_reads_as_its_name_and_recorded_shapes] | ✅ | - | ✅ | - |
| test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps[test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps] | ✅ | - | ✅ | - |
| test_a_held_array_is_viewed_in_the_body_under_its_own_path[test_a_held_array_is_viewed_in_the_body_under_its_own_path] | ✅ | - | ✅ | - |
| test_a_held_array_that_is_no_param_is_refused[test_a_held_array_that_is_no_param_is_refused] | ✅ | - | ✅ | - |
| test_a_host_step_is_recorded_before_the_next_step[test_a_host_step_is_recorded_before_the_next_step] | ✅ | - | ✅ | - |
| test_a_host_step_runs_between_the_device_s_steps[each_step] | ✅ | - | ✅ | - |
| test_a_host_step_runs_between_the_device_s_steps[full_elf] | ✅ | - | - | - |
| test_a_host_write_to_a_state_a_step_writes_is_refused[test_a_host_write_to_a_state_a_step_writes_is_refused] | ✅ | - | ✅ | - |
| test_a_host_write_to_other_than_a_state_is_refused[test_a_host_write_to_other_than_a_state_is_refused] | ✅ | - | ✅ | - |
| test_a_lane_pins_to_a_channel_moving_its_way[test_a_lane_pins_to_a_channel_moving_its_way] | ✅ | - | ✅ | - |
| test_a_layer_norm_s_eps_is_its_kernel_s[test_a_layer_norm_s_eps_is_its_kernel_s] | ✅ | - | ✅ | - |
| test_a_matvec_whose_columns_are_given_resolves_with_no_device[test_a_matvec_whose_columns_are_given_resolves_with_no_device] | ✅ | - | ✅ | - |
| test_a_mixed_call_places_the_soft_tokens_and_attends_over_them[soft_1] | ✅ | - | ✅ | - |
| test_a_mixed_call_places_the_soft_tokens_and_attends_over_them[soft_5] | ✅ | - | ✅ | - |
| test_a_model_fits_its_context_with_no_device_bound[test_a_model_fits_its_context_with_no_device_bound] | ✅ | - | ✅ | - |
| test_a_model_runs_only_the_versions_it_loaded[test_a_model_runs_only_the_versions_it_loaded] | ✅ | - | ✅ | - |
| test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given[test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given] | ✅ | - | ✅ | - |
| test_a_norm_is_its_kernel_weighted_if_given_then_any_bias[layer_weighted_biased] | ✅ | - | ✅ | - |
| test_a_norm_is_its_kernel_weighted_if_given_then_any_bias[rms_unweighted] | ✅ | - | ✅ | - |
| test_a_norm_over_another_axis_than_the_last_is_refused[layer] | ✅ | - | ✅ | - |
| test_a_norm_over_another_axis_than_the_last_is_refused[rms] | ✅ | - | ✅ | - |
| test_a_number_on_either_side_is_a_row_of_it[test_a_number_on_either_side_is_a_row_of_it] | ✅ | - | ✅ | - |
| test_a_numpy_function_on_a_handle_says_what_to_call[test_a_numpy_function_on_a_handle_says_what_to_call] | ✅ | - | ✅ | - |
| test_a_padded_pattern_does_not_fit_a_shim_descriptor[test_a_padded_pattern_does_not_fit_a_shim_descriptor] | ✅ | - | ✅ | - |
| test_a_per_call_length_counts_a_dimension_by_a_word[no_dimension_of_the_unit] | ✅ | - | ✅ | - |
| test_a_per_call_length_counts_a_dimension_by_a_word[not_a_word] | ✅ | - | ✅ | - |
| test_a_per_call_value_cannot_steer_the_record[test_a_per_call_value_cannot_steer_the_record] | ✅ | - | ✅ | - |
| test_a_per_call_value_s_default_is_given_when_left_out[test_a_per_call_value_s_default_is_given_when_left_out] | ✅ | - | ✅ | - |
| test_a_per_layer_slice_is_drawn_in_its_layer[test_a_per_layer_slice_is_drawn_in_its_layer] | ✅ | - | ✅ | - |
| test_a_positional_operand_past_the_inputs_is_an_output_not_an_optional_one[test_a_positional_operand_past_the_inputs_is_an_output_not_an_optional_one] | ✅ | - | ✅ | - |
| test_a_profile_fills_the_tunables_a_call_leaves_open[test_a_profile_fills_the_tunables_a_call_leaves_open] | ✅ | - | ✅ | - |
| test_a_profile_is_checked_as_it_is_written_and_as_it_is_read[test_a_profile_is_checked_as_it_is_written_and_as_it_is_read] | ✅ | - | ✅ | - |
| test_a_prompt_begins_as_the_tokenizer_begins_a_text[gemma-4-e2b-it] | ✅ | - | ✅ | - |
| test_a_prompt_begins_as_the_tokenizer_begins_a_text[llama3.2-1b] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_0-rows_256-inside_True] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_1-rows_44-inside_True] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_1-rows_45-inside_False] | ✅ | - | ✅ | - |
| test_a_prompt_chunk_past_the_last_position_is_refused[chunk_2-rows_1-inside_False] | ✅ | - | ✅ | - |
| test_a_recorded_graph_names_every_step_and_every_edge[test_a_recorded_graph_names_every_step_and_every_edge] | ✅ | - | ✅ | - |
| test_a_reference_only_operator_runs_its_reference_and_does_not_compile[test_a_reference_only_operator_runs_its_reference_and_does_not_compile] | ✅ | - | ✅ | - |
| test_a_reference_only_operator_takes_no_image[test_a_reference_only_operator_takes_no_image] | ✅ | - | ✅ | - |
| test_a_reference_takes_valid_rows_short_of_a_whole_line[n_128] | ✅ | - | ✅ | - |
| test_a_reference_takes_valid_rows_short_of_a_whole_line[n_1] | ✅ | - | ✅ | - |
| test_a_reference_takes_valid_rows_short_of_a_whole_line[n_9] | ✅ | - | ✅ | - |
| test_a_refused_compile_restores_the_device_it_was_given_over[test_a_refused_compile_restores_the_device_it_was_given_over] | ✅ | - | ✅ | - |
| test_a_refused_step_names_the_graph_the_operator_and_the_held_path[test_a_refused_step_names_the_graph_the_operator_and_the_held_path] | ✅ | - | ✅ | - |
| test_a_refused_step_shows_an_unheld_param_as_an_array_of_its_shape[test_a_refused_step_shows_an_unheld_param_as_an_array_of_its_shape] | ✅ | - | ✅ | - |
| test_a_row_bound_needs_one_row_block_per_unit[test_a_row_bound_needs_one_row_block_per_unit] | ✅ | - | ✅ | - |
| test_a_row_sweep_splits_each_length_into_rows_of_the_tile[test_a_row_sweep_splits_each_length_into_rows_of_the_tile] | ✅ | - | ✅ | - |
| test_a_run_as_wide_as_its_axis_keeps_its_start_under_a_bound[test_a_run_as_wide_as_its_axis_keeps_its_start_under_a_bound] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[another_value] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[no_stop] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[two_per_call] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[wider_than_the_axis] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_is_its_whole_chunk_s_view[test_a_run_from_a_per_call_start_is_its_whole_chunk_s_view] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_is_written_and_read_as_numpy_does[test_a_run_from_a_per_call_start_is_written_and_read_as_numpy_does] | ✅ | - | ✅ | - |
| test_a_run_from_a_per_call_start_takes_any_start_on_any_axis[test_a_run_from_a_per_call_start_takes_any_start_on_any_axis] | ✅ | - | ✅ | - |
| test_a_run_is_bounded_from_its_start_on_its_own_axis[test_a_run_is_bounded_from_its_start_on_its_own_axis] | ✅ | - | ✅ | - |
| test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides[test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides] | ✅ | - | ✅ | - |
| test_a_run_past_the_buffer_s_end_is_kept_inside_by_each_call[test_a_run_past_the_buffer_s_end_is_kept_inside_by_each_call] | ✅ | - | ✅ | - |
| test_a_run_that_draws_no_eos_draws_max_tokens[test_a_run_that_draws_no_eos_draws_max_tokens] | ✅ | - | ✅ | - |
| test_a_scratchpad_parameter_holds_one_word[test_a_scratchpad_parameter_holds_one_word] | ✅ | - | ✅ | - |
| test_a_shipped_image_declares_its_pins_and_parameter_block[test_a_shipped_image_declares_its_pins_and_parameter_block] | ✅ | - | ✅ | - |
| test_a_shipped_image_in_a_graph_is_refused[test_a_shipped_image_in_a_graph_is_refused] | ✅ | - | ✅ | - |
| test_a_shipped_image_runs_only_with_instructions[test_a_shipped_image_runs_only_with_instructions] | ✅ | - | ✅ | - |
| test_a_size_the_default_line_does_not_split_takes_a_narrower_one[test_a_size_the_default_line_does_not_split_takes_a_narrower_one] | ✅ | - | ✅ | - |
| test_a_sliding_window_some_layers_take_is_refused[test_a_sliding_window_some_layers_take_is_refused] | ✅ | - | ✅ | - |
| test_a_state_is_subtracted_as_it_is_added[test_a_state_is_subtracted_as_it_is_added] | ✅ | - | ✅ | - |
| test_a_state_written_by_one_step_is_pinned_and_readable[test_a_state_written_by_one_step_is_pinned_and_readable] | ✅ | - | ✅ | - |
| test_a_stream_binds_a_handle_per_lane[test_a_stream_binds_a_handle_per_lane] | ✅ | - | ✅ | - |
| test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget[test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget] | ✅ | - | ✅ | - |
| test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere[test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere] | ✅ | - | ✅ | - |
| test_a_text_only_call_runs_the_text_model_s_version[test_a_text_only_call_runs_the_text_model_s_version] | ✅ | - | ✅ | - |
| test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch[outside_-1] | ✅ | - | ✅ | - |
| test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch[outside_1024] | ✅ | - | ✅ | - |
| test_a_tower_runs_its_front_end_s_rows[test_a_tower_runs_its_front_end_s_rows] | ✅ | - | ✅ | - |
| test_a_towers_layers_are_found_under_its_prefix[test_a_towers_layers_are_found_under_its_prefix] | ✅ | - | ✅ | - |
| test_a_tunable_free_operator_takes_the_widest_split_that_leaves_whole_lines[test_a_tunable_free_operator_takes_the_widest_split_that_leaves_whole_lines] | ✅ | - | ✅ | - |
| test_a_turn_runs_from_its_first_new_token[test_a_turn_runs_from_its_first_new_token] | ✅ | - | ✅ | - |
| test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident[test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident] | ✅ | - | ✅ | - |
| test_a_value_only_a_core_reads_is_declared_on_a_full_elf[test_a_value_only_a_core_reads_is_declared_on_a_full_elf] | ✅ | - | ✅ | - |
| test_a_version_reads_none_of_the_words_its_image_writes[test_a_version_reads_none_of_the_words_its_image_writes] | ✅ | - | ✅ | - |
| test_a_version_reads_only_the_values_its_steps_read[test_a_version_reads_only_the_values_its_steps_read] | ✅ | - | ✅ | - |
| test_a_version_with_no_tensor_splits_at_a_host_step_too[test_a_version_with_no_tensor_splits_at_a_host_step_too] | ✅ | - | ✅ | - |
| test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[2, 2, 8, 2048]-strides_[0, 65536, 4096, 1]-bounded_True-match_one shim] | ✅ | - | ✅ | - |
| test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[4, 4, 4, 1024]-strides_[0, 4096, 1024, 1]-bounded_False-match_give bounds] | ✅ | - | ✅ | - |
| test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[64, 4096]-strides_[4096, 1]-bounded_True-match_one shim] | ✅ | - | ✅ | - |
| test_a_weight_given_where_an_optional_input_was_meant_is_refused[view_False] | ✅ | - | ✅ | - |
| test_a_weight_given_where_an_optional_input_was_meant_is_refused[view_True] | ✅ | - | ✅ | - |
| test_a_weight_times_a_row_is_linear_and_a_plain_matrix_is_refused[test_a_weight_times_a_row_is_linear_and_a_plain_matrix_is_refused] | ✅ | - | ✅ | - |
| test_a_whole_reshape_of_a_held_array_is_gathered_under_its_own_path[test_a_whole_reshape_of_a_held_array_is_gathered_under_its_own_path] | ✅ | - | ✅ | - |
| test_alike_instances_bound_to_different_values_are_different_designs[test_alike_instances_bound_to_different_values_are_different_designs] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[GELU-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[GELU-device_npu2] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[SiLU-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[SiLU-device_npu2] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Sigmoid-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Sigmoid-device_npu2] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Tanh-device_npu1] | ✅ | - | ✅ | - |
| test_an_activation_is_judged_by_its_devices_row[Tanh-device_npu2] | ✅ | - | ✅ | - |
| test_an_assignment_into_a_view_is_the_copy_into_it[test_an_assignment_into_a_view_is_the_copy_into_it] | ✅ | - | ✅ | - |
| test_an_axis_is_found_through_the_branch_a_select_takes[test_an_axis_is_found_through_the_branch_a_select_takes] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_1-window_64] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_1-window_None] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_128-window_64] | ✅ | - | ✅ | - |
| test_an_encoder_attends_its_valid_rows_both_ways[n_128-window_None] | ✅ | - | ✅ | - |
| test_an_encoder_places_its_positions_through_the_hook[n_128] | ✅ | - | ✅ | - |
| test_an_encoder_places_its_positions_through_the_hook[n_9] | ✅ | - | ✅ | - |
| test_an_explicit_instance_is_applied_like_the_class[test_an_explicit_instance_is_applied_like_the_class] | ✅ | - | ✅ | - |
| test_an_exported_design_replaces_the_derived_one[test_an_exported_design_replaces_the_derived_one] | ✅ | - | ✅ | - |
| test_an_extent_reads_as_its_field_until_a_graph_bounds_it[test_an_extent_reads_as_its_field_until_a_graph_bounds_it] | ✅ | - | ✅ | - |
| test_an_image_a_call_does_not_hold_is_refused[test_an_image_a_call_does_not_hold_is_refused] | ✅ | - | ✅ | - |
| test_an_index_before_a_bound_keeps_the_bound_on_its_axis[test_an_index_before_a_bound_keeps_the_bound_on_its_axis] | ✅ | - | ✅ | - |
| test_an_index_may_floor_and_a_bound_may_only_clamp[test_an_index_may_floor_and_a_bound_may_only_clamp] | ✅ | - | ✅ | - |
| test_an_input_given_as_an_output_is_refused[test_an_input_given_as_an_output_is_refused] | ✅ | - | ✅ | - |
| test_an_input_named_as_a_compile_keyword_is_refused[test_an_input_named_as_a_compile_keyword_is_refused] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[bound] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[exact] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[relative] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[relative_atol] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[relative_range] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[ulps] | ✅ | - | ✅ | - |
| test_an_interval_is_what_compare_admits[ulps_atol] | ✅ | - | ✅ | - |
| test_an_operand_declared_when_a_flag_exists_only_where_it_is_true[test_an_operand_declared_when_a_flag_exists_only_where_it_is_true] | ✅ | - | ✅ | - |
| test_an_operand_fills_only_inside_its_operators_sequence[test_an_operand_fills_only_inside_its_operators_sequence] | ✅ | - | ✅ | - |
| test_an_operand_with_a_tile_is_its_own_stream[test_an_operand_with_a_tile_is_its_own_stream] | ✅ | - | ✅ | - |
| test_an_operator_written_by_inheritance_inherits_the_sweep[test_an_operator_written_by_inheritance_inherits_the_sweep] | ✅ | - | ✅ | - |
| test_an_optional_input_gives_a_version_without_it[test_an_optional_input_gives_a_version_without_it] | ✅ | - | ✅ | - |
| test_an_unaligned_gather_computes_whole_blocks[test_an_unaligned_gather_computes_whole_blocks] | ✅ | - | ✅ | - |
| test_an_unaligned_gather_writes_no_callers_output[test_an_unaligned_gather_writes_no_callers_output] | ✅ | - | ✅ | - |
| test_an_xclbin_is_asked_for_where_a_full_elf_would_do[test_an_xclbin_is_asked_for_where_a_full_elf_would_do] | ✅ | - | ✅ | - |
| test_angles_are_the_unscaled_table_at_rope_width[test_angles_are_the_unscaled_table_at_rope_width] | ✅ | - | ✅ | - |
| test_array_sees_the_array_tier_alone[test_array_sees_the_array_tier_alone] | ✅ | - | ✅ | - |
| test_arrays_are_shared_by_array_key_and_extents_are_not[test_arrays_are_shared_by_array_key_and_extents_are_not] | ✅ | - | ✅ | - |
| test_attention_scaling_multiplies_the_whole_table_once[test_attention_scaling_multiplies_the_whole_table_once] | ✅ | - | ✅ | - |
| test_binding_two_handles_to_one_instance_is_an_error[test_binding_two_handles_to_one_instance_is_an_error] | ✅ | - | ✅ | - |
| test_buffers_resolve_shape_dtype_and_direction[test_buffers_resolve_shape_dtype_and_direction] | ✅ | - | ✅ | - |
| test_by_default_the_table_is_rope_angles_at_head_dim[test_by_default_the_table_is_rope_angles_at_head_dim] | ✅ | - | ✅ | - |
| test_call_reference_gives_an_output_only_to_a_reference_that_names_it[test_call_reference_gives_an_output_only_to_a_reference_that_names_it] | ✅ | - | ✅ | - |
| test_call_reference_pairs_buffers_by_name_not_by_order[test_call_reference_pairs_buffers_by_name_not_by_order] | ✅ | - | ✅ | - |
| test_call_reference_refuses_a_reference_that_returns_nothing[test_call_reference_refuses_a_reference_that_returns_nothing] | ✅ | - | ✅ | - |
| test_chat_messages_are_rendered_by_the_checkpoint_s_template[test_chat_messages_are_rendered_by_the_checkpoint_s_template] | ✅ | - | ✅ | - |
| test_check_takes_an_xclbin_per_step[test_check_takes_an_xclbin_per_step] | ✅ | - | ✅ | - |
| test_compatible_runs_at_construction_once_every_tunable_is_known[test_compatible_runs_at_construction_once_every_tunable_is_known] | ✅ | - | ✅ | - |
| test_concurrent_fetches_of_a_shipped_image_each_get_the_whole_file[test_concurrent_fetches_of_a_shipped_image_each_get_the_whole_file] | ✅ | - | ✅ | - |
| test_decode_step_reads_the_rope_table_at_its_own_width[test_decode_step_reads_the_rope_table_at_its_own_width] | ✅ | - | ✅ | - |
| test_default_is_a_full_elf_on_npu2[test_default_is_a_full_elf_on_npu2] | ✅ | - | ✅ | - |
| test_devices_are_named_for_their_design_not_their_step[test_devices_are_named_for_their_design_not_their_step] | ✅ | - | ✅ | - |
| test_each_gelu_is_its_operator_s_form[act_gelu-approximate_none] | ✅ | - | ✅ | - |
| test_each_gelu_is_its_operator_s_form[act_gelu_pytorch_tanh-approximate_tanh] | ✅ | - | ✅ | - |
| test_each_layer_s_steps_are_drawn_in_its_cluster[test_each_layer_s_steps_are_drawn_in_its_cluster] | ✅ | - | ✅ | - |
| test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.embedding_gemma2.model.Config'>-instance_Config(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, vocab_size=262144, hidden_size=512, num_hidden_layers=24, num_attention_heads=4, intermediate_size=2048, num_key_value_heads=2, head_dim=256, rope_theta=10000.0, layer_types=('sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention'), global_kv_groups=1, global_head_dim=512, global_rope_theta=1000000.0, sliding_window=512, ple_dim=512, embedding_dim=768, hidden_act='gelu_pytorch_tanh', mrl_dims=(768, 512, 256, 128), image_token=258880, audio_token=258881, boi=255999, eoi=258882, boa=256000, eoa=258883, max_tokens=2048, block=64)] | ✅ | - | ✅ | - |
| test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.gemma4.audio.AudioConfig'>-instance_AudioConfig(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, hidden_size=1024, num_hidden_layers=12, num_attention_heads=8, intermediate_size=4096, mels=128, subsampling_conv_channels=(128, 32), window=12, band=32, attention_logit_cap=50.0, use_clipped_linears=True, conv_kernel_size=5, residual_weight=0.5, text_dim=512, output_proj_dims=1536, sample_rate=16000, frame=320, hop=160, max_samples=480000, max_tokens=768)] | ✅ | - | ✅ | - |
| test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.gemma4.vision.VisionConfig'>-instance_VisionConfig(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, hidden_size=768, num_hidden_layers=16, num_attention_heads=12, head_dim=64, intermediate_size=3072, patch_size=16, pooling_kernel_size=3, position_embedding_size=10240, rope_theta=100.0, hidden_act='gelu_pytorch_tanh', use_clipped_linears=False, text_dim=512, image_tokens=280, patches=2560, largest=(3072, 4096), rows=256, chunk=4096, patch_columns=8)] | ✅ | - | ✅ | - |
| test_embeddinggemma_2_loads_a_layer_s_per_layer_input_flat_or_nested[test_embeddinggemma_2_loads_a_layer_s_per_layer_input_flat_or_nested] | ✅ | - | ✅ | - |
| test_equal_kernel_recipes_share_one_object_across_designs[test_equal_kernel_recipes_share_one_object_across_designs] | ✅ | - | ✅ | - |
| test_every_carried_value_is_carried_and_nothing_else[test_every_carried_value_is_carried_and_nothing_else] | ✅ | - | ✅ | - |
| test_every_declared_case_resolves_on_npu2[test_every_declared_case_resolves_on_npu2] | ✅ | - | ✅ | - |
| test_every_tolerance_says_where_its_numbers_come_from[npu1] | ✅ | - | ✅ | - |
| test_every_tolerance_says_where_its_numbers_come_from[npu2] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_AXPY] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Clamp] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Copy] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_DepthwiseConv1d] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ElementwiseAdd] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ElementwiseMul] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Emit] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GELU] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GEMM] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GEMV] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_GatherWords] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Gather] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_LayerNorm] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Limbs] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Log] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_MHA] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Magnitude] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Merge] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_PatchPositions] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RMSNorm] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ReLU] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_ResampleTaps] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Resample] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RoPE] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RowwiseAdd] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_RowwiseMul] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Sample] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_SiLU] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Sigmoid] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Softmax] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_Tanh] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.DecodeLayer] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.DequantBFP] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.LMHead] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.PrefillAttention] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.PrefillSlidingAttention] | ✅ | - | ✅ | - |
| test_exported_operator_is_declared[name_flm.ProjectionGEMM] | ✅ | - | ✅ | - |
| test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks[test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks] | ✅ | - | ✅ | - |
| test_flm_gemm_declares_every_b_pool_whichever_columns_a_shape_fills[test_flm_gemm_declares_every_b_pool_whichever_columns_a_shape_fills] | ✅ | - | ✅ | - |
| test_flm_gemm_image_keeps_the_tiles_a_narrow_shape_resolves_to[test_flm_gemm_image_keeps_the_tiles_a_narrow_shape_resolves_to] | ✅ | - | ✅ | - |
| test_flm_gemm_keyword_construction_tunes_from_the_device[test_flm_gemm_keyword_construction_tunes_from_the_device] | ✅ | - | ✅ | - |
| test_flm_gemm_selects_its_activation_by_a_word[test_flm_gemm_selects_its_activation_by_a_word] | ✅ | - | ✅ | - |
| test_float_scratchpad_annotation_is_rejected[test_float_scratchpad_annotation_is_rejected] | ✅ | - | ✅ | - |
| test_from_checkpoint_draws_its_weights_at_a_seed[test_from_checkpoint_draws_its_weights_at_a_seed] | ✅ | - | ✅ | - |
| test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it[test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it] | ✅ | - | ✅ | - |
| test_from_checkpoint_names_the_keys_a_config_json_lacks[test_from_checkpoint_names_the_keys_a_config_json_lacks] | ✅ | - | ✅ | - |
| test_from_checkpoint_opens_the_tokenizer_beside_it[test_from_checkpoint_opens_the_tokenizer_beside_it] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.embedding_gemma2.model.Config] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.gemma4.audio.AudioConfig] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.gemma4.vision.VisionConfig] | ✅ | - | ✅ | - |
| test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.llama.model.LlamaConfig] | ✅ | - | ✅ | - |
| test_from_checkpoint_refuses_a_rope_scaling_it_builds_no_table_for[test_from_checkpoint_refuses_a_rope_scaling_it_builds_no_table_for] | ✅ | - | ✅ | - |
| test_from_checkpoint_takes_either_the_file_or_its_directory[test_from_checkpoint_takes_either_the_file_or_its_directory] | ✅ | - | ✅ | - |
| test_gathered_patches_hold_no_padding[test_gathered_patches_hold_no_padding] | ✅ | - | ✅ | - |
| test_gelu_refuses_a_form_it_has_no_kernel_for[test_gelu_refuses_a_form_it_has_no_kernel_for] | ✅ | - | ✅ | - |
| test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic[test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic] | ✅ | - | ✅ | - |
| test_gemma_s_text_layer_projects_at_highest_precision[test_gemma_s_text_layer_projects_at_highest_precision] | ✅ | - | ✅ | - |
| test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s[test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s] | ✅ | - | ✅ | - |
| test_generate_gives_text_for_text_and_ids_for_ids[test_generate_gives_text_for_text_and_ids_for_ids] | ✅ | - | ✅ | - |
| test_generation_stops_at_an_eos_and_includes_it[test_generation_stops_at_an_eos_and_includes_it] | ✅ | - | ✅ | - |
| test_head_dim_falls_back_and_max_seq_len_is_the_native_context[test_head_dim_falls_back_and_max_seq_len_is_the_native_context] | ✅ | - | ✅ | - |
| test_highest_runs_the_gemm_that_rounds_once[test_highest_runs_the_gemm_that_rounds_once] | ✅ | - | ✅ | - |
| test_identity_holds_across_processes[test_identity_holds_across_processes] | ✅ | - | ✅ | - |
| test_identity_is_what_the_text_is_a_function_of[test_identity_is_what_the_text_is_a_function_of] | ✅ | - | ✅ | - |
| test_inline_records_only_into_a_body[test_inline_records_only_into_a_body] | ✅ | - | ✅ | - |
| test_inputs_pad_with_zero_and_give_rows[test_inputs_pad_with_zero_and_give_rows] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[-1]-error_<class 'IndexError'>] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]-error_<class 'ValueError'>] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[32]-error_<class 'IndexError'>] | ✅ | - | ✅ | - |
| test_inputs_refuse_what_no_call_takes[tokens_[]-error_<class 'ValueError'>] | ✅ | - | ✅ | - |
| test_integer_arithmetic_on_an_expression_is_an_expression[test_integer_arithmetic_on_an_expression_is_an_expression] | ✅ | - | ✅ | - |
| test_it_records_only_while_asked_and_reads_back_without_the_reference[test_it_records_only_while_asked_and_reads_back_without_the_reference] | ✅ | - | ✅ | - |
| test_its_signature_is_its_text_model_s_and_towers[test_its_signature_is_its_text_model_s_and_towers] | ✅ | - | ✅ | - |
| test_judge_names_each_output_and_refuses_a_missing_one[test_judge_names_each_output_and_refuses_a_missing_one] | ✅ | - | ✅ | - |
| test_keyword_only_parameters_must_be_annotated_as_values[test_keyword_only_parameters_must_be_annotated_as_values] | ✅ | - | ✅ | - |
| test_linear_takes_a_precision_for_any_rows_and_gemv_tunables_for_one[gemm] | ✅ | - | ✅ | - |
| test_linear_takes_a_precision_for_any_rows_and_gemv_tunables_for_one[gemv] | ✅ | - | ✅ | - |
| test_linear_takes_one_row_or_several[test_linear_takes_one_row_or_several] | ✅ | - | ✅ | - |
| test_llama_1b_from_checkpoint_is_its_published_shape[test_llama_1b_from_checkpoint_is_its_published_shape] | ✅ | - | ✅ | - |
| test_llama_decode_records_and_tunes[test_llama_decode_records_and_tunes] | ✅ | - | ✅ | - |
| test_llama_projects_at_high_from_3b_s_width_unless_given[test_llama_projects_at_high_from_3b_s_width_unless_given] | ✅ | - | ✅ | - |
| test_llama_prompt_projects_with_flm_gemm[device_npu1] | ✅ | - | ✅ | - |
| test_llama_prompt_projects_with_flm_gemm[device_npu2] | ✅ | - | ✅ | - |
| test_llama_prompt_records_over_the_same_caches[test_llama_prompt_records_over_the_same_caches] | ✅ | - | ✅ | - |
| test_log_mel_holds_to_the_extractor[test_log_mel_holds_to_the_extractor] | ✅ | - | ✅ | - |
| test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[param] | ✅ | - | ✅ | - |
| test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[state] | ✅ | - | ✅ | - |
| test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[weight] | ✅ | - | ✅ | - |
| test_mha_binds_p_times_v_at_its_own_shape[test_mha_binds_p_times_v_at_its_own_shape] | ✅ | - | ✅ | - |
| test_mha_refuses_a_sequence_pad_of_no_whole_blocks[test_mha_refuses_a_sequence_pad_of_no_whole_blocks] | ✅ | - | ✅ | - |
| test_no_column_count_resolves_when_one_column_overruns_the_shim[test_no_column_count_resolves_when_one_column_overruns_the_shim] | ✅ | - | ✅ | - |
| test_no_npu_says_how_to_compile_without_one[test_no_npu_says_how_to_compile_without_one] | ✅ | - | ✅ | - |
| test_no_sampler_is_greedy[test_no_sampler_is_greedy] | ✅ | - | ✅ | - |
| test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering[test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_bounded_flm_gemm_repeats_a_by_the_dispatch_scalar[test_on_an_xclbin_a_bounded_flm_gemm_repeats_a_by_the_dispatch_scalar] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_copy_bounded_on_its_innermost_axis_sizes_it[test_on_an_xclbin_a_copy_bounded_on_its_innermost_axis_sizes_it] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_per_call_length_sizes_the_coalesced_descriptor[five_dimensions] | ✅ | - | ✅ | - |
| test_on_an_xclbin_a_per_call_length_sizes_the_coalesced_descriptor[repeat_led] | ✅ | - | ✅ | - |
| test_on_an_xclbin_the_size_is_the_dispatch_scalar[test_on_an_xclbin_the_size_is_the_dispatch_scalar] | ✅ | - | ✅ | - |
| test_on_host_outside_a_body_is_refused[test_on_host_outside_a_body_is_refused] | ✅ | - | ✅ | - |
| test_one_configuration_records_at_one_size[test_one_configuration_records_at_one_size] | ✅ | - | ✅ | - |
| test_one_row_a_core_holds_is_still_rowwise[test_one_row_a_core_holds_is_still_rowwise] | ✅ | - | ✅ | - |
| test_one_row_times_a_number_is_elementwise[test_one_row_times_a_number_is_elementwise] | ✅ | - | ✅ | - |
| test_only_a_copy_takes_the_rows_an_input_names[test_only_a_copy_takes_the_rows_an_input_names] | ✅ | - | ✅ | - |
| test_only_none_may_default_an_input[test_only_none_may_default_an_input] | ✅ | - | ✅ | - |
| test_patches_short_of_a_tile_compute_a_whole_one[test_patches_short_of_a_tile_compute_a_whole_one] | ✅ | - | ✅ | - |
| test_per_call_values_bind_on_the_operator[test_per_call_values_bind_on_the_operator] | ✅ | - | ✅ | - |
| test_per_call_values_bind_to_the_operator_and_enable_it[test_per_call_values_bind_to_the_operator_and_enable_it] | ✅ | - | ✅ | - |
| test_placeholders_that_are_not_the_soft_tokens_are_refused[test_placeholders_that_are_not_the_soft_tokens_are_refused] | ✅ | - | ✅ | - |
| test_prompt_chunk_reads_the_rope_table_at_its_own_width[test_prompt_chunk_reads_the_rope_table_at_its_own_width] | ✅ | - | ✅ | - |
| test_reference_without_a_device_names_how_to_bind_one[test_reference_without_a_device_names_how_to_bind_one] | ✅ | - | ✅ | - |
| test_report_reads_as_one_block[test_report_reads_as_one_block] | ✅ | - | ✅ | - |
| test_resolve_columns_is_the_count_given_or_the_most_that_fit[test_resolve_columns_is_the_count_given_or_the_most_that_fit] | ✅ | - | ✅ | - |
| test_returning_an_input_or_a_slice_is_refused[test_returning_an_input_or_a_slice_is_refused] | ✅ | - | ✅ | - |
| test_rope_width_is_the_rotary_dim_when_given[test_rope_width_is_the_rotary_dim_when_given] | ✅ | - | ✅ | - |
| test_runtime_parameters_lay_out_the_buffer_words_and_skip_scratchpad_ones[test_runtime_parameters_lay_out_the_buffer_words_and_skip_scratchpad_ones] | ✅ | - | ✅ | - |
| test_saving_an_operator_outside_the_catalog_names_it[test_saving_an_operator_outside_the_catalog_names_it] | ✅ | - | ✅ | - |
| test_shape_mismatch_and_rank_rules[test_shape_mismatch_and_rank_rules] | ✅ | - | ✅ | - |
| test_slices_are_views_into_the_parent_in_bytes[test_slices_are_views_into_the_parent_in_bytes] | ✅ | - | ✅ | - |
| test_split_takes_every_batch_and_broadcasts[test_split_takes_every_batch_and_broadcasts] | ✅ | - | ✅ | - |
| test_stream_s_pieces_joined_are_what_generate_gives[test_stream_s_pieces_joined_are_what_generate_gives] | ✅ | - | ✅ | - |
| test_testing_resolves_cases_and_callables_of_the_class[test_testing_resolves_cases_and_callables_of_the_class] | ✅ | - | ✅ | - |
| test_the_architecture_decides_not_the_name[test_the_architecture_decides_not_the_name] | ✅ | - | ✅ | - |
| test_the_binary_sweep_and_an_all_extensive_sweep[test_the_binary_sweep_and_an_all_extensive_sweep] | ✅ | - | ✅ | - |
| test_the_callers_reference_runs_the_called_graph[test_the_callers_reference_runs_the_called_graph] | ✅ | - | ✅ | - |
| test_the_carried_draws_are_the_host_loop_s_tokens[temperature_0.0] | ✅ | - | ✅ | - |
| test_the_carried_draws_are_the_host_loop_s_tokens[temperature_0.7] | ✅ | - | ✅ | - |
| test_the_cases_judge_by_every_kind_of_tolerance[test_the_cases_judge_by_every_kind_of_tolerance] | ✅ | - | ✅ | - |
| test_the_default_layer_is_an_encoder_layer_attending_both_ways[test_the_default_layer_is_an_encoder_layer_attending_both_ways] | ✅ | - | ✅ | - |
| test_the_gather_reads_only_the_rows_a_call_bounds[test_the_gather_reads_only_the_rows_a_call_bounds] | ✅ | - | ✅ | - |
| test_the_oracles_steps_pass_and_a_wrong_weight_is_caught_at_its_step[test_the_oracles_steps_pass_and_a_wrong_weight_is_caught_at_its_step] | ✅ | - | ✅ | - |
| test_the_quick_start_script_runs_on_a_toy_repository[test_the_quick_start_script_runs_on_a_toy_repository] | ✅ | - | ✅ | - |
| test_the_reference_computes_the_expressions[test_the_reference_computes_the_expressions] | ✅ | - | ✅ | - |
| test_the_reference_copies_a_bounded_call_into_the_rows_it_covers[test_the_reference_copies_a_bounded_call_into_the_rows_it_covers] | ✅ | - | ✅ | - |
| test_the_reference_holds_one_layer_s_intermediates_at_a_time[test_the_reference_holds_one_layer_s_intermediates_at_a_time] | ✅ | - | ✅ | - |
| test_the_reference_is_its_parts_on_their_own[test_the_reference_is_its_parts_on_their_own] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_band] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_depthwise] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_depthwise_13_rows] | ✅ | - | ✅ | - |
| test_the_reference_is_the_convolution[case_patches] | ✅ | - | ✅ | - |
| test_the_reference_refuses_what_a_call_refuses[test_the_reference_refuses_what_a_call_refuses] | ✅ | - | ✅ | - |
| test_the_reference_runs_the_host_step_on_the_rows_the_call_bounds[rows_16] | ✅ | - | ✅ | - |
| test_the_reference_runs_the_host_step_on_the_rows_the_call_bounds[rows_5] | ✅ | - | ✅ | - |
| test_the_reference_runs_the_trace_so_held_state_takes_arithmetic[test_the_reference_runs_the_trace_so_held_state_takes_arithmetic] | ✅ | - | ✅ | - |
| test_the_reference_writes_a_copy_into_a_strided_view_through_it[test_the_reference_writes_a_copy_into_a_strided_view_through_it] | ✅ | - | ✅ | - |
| test_the_reference_writes_a_given_output_of_an_operator_that_returns_one[test_the_reference_writes_a_given_output_of_an_operator_that_returns_one] | ✅ | - | ✅ | - |
| test_the_refusals_name_what_to_change[test_the_refusals_name_what_to_change] | ✅ | - | ✅ | - |
| test_the_slots_after_a_multi_word_value_follow_its_words[test_the_slots_after_a_multi_word_value_follow_its_words] | ✅ | - | ✅ | - |
| test_the_trace_records_the_range_each_per_call_index_and_bound_holds[test_the_trace_records_the_range_each_per_call_index_and_bound_holds] | ✅ | - | ✅ | - |
| test_the_trip_count_is_a_resident_the_build_writes[test_the_trip_count_is_a_resident_the_build_writes] | ✅ | - | ✅ | - |
| test_the_unary_sweep_reads_the_class_it_is_resolved_for[test_the_unary_sweep_reads_the_class_it_is_resolved_for] | ✅ | - | ✅ | - |
| test_to_json_is_from_checkpoint_s_inverse[embedding_gemma2] | ✅ | - | ✅ | - |
| test_to_json_is_from_checkpoint_s_inverse[llama] | ✅ | - | ✅ | - |
| test_tracing_records_the_runlist_with_names_from_roles[test_tracing_records_the_runlist_with_names_from_roles] | ✅ | - | ✅ | - |
| test_two_designs_whose_device_names_collide_are_refused[test_two_designs_whose_device_names_collide_are_refused] | ✅ | - | ✅ | - |
| test_two_sessions_share_one_model[test_two_sessions_share_one_model] | ✅ | - | ✅ | - |
| test_two_towers_on_one_input_name_are_refused[test_two_towers_on_one_input_name_are_refused] | ✅ | - | ✅ | - |
| test_v_shows_iron_s_info_lines[test_v_shows_iron_s_info_lines] | ✅ | - | ✅ | - |
| test_vectors_draws_each_input_and_runs_the_reference_on_the_draw[test_vectors_draws_each_input_and_runs_the_reference_on_the_draw] | ✅ | - | ✅ | - |
| test_vectors_takes_a_given_shape_or_refuses_an_unknown_input[test_vectors_takes_a_given_shape_or_refuses_an_unknown_input] | ✅ | - | ✅ | - |
| test_walks_take_a_repeat_each[taps_1-repeats_2] | ✅ | - | ✅ | - |
| test_walks_take_a_repeat_each[taps_2-repeats_1] | ✅ | - | ✅ | - |
| test_what_a_bound_makes_per_call_is_worked_out_once_per_binding[test_what_a_bound_makes_per_call_is_worked_out_once_per_binding] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/tests/docs</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_section1_axpy_matches_numpy[test_section1_axpy_matches_numpy] | ✅ | - | ✅ | - |
| test_section1_axpy_on_device[test_section1_axpy_on_device] | ✅ | - | - | - |
| test_section2_first_graph_matches_numpy[test_section2_first_graph_matches_numpy] | ✅ | - | ✅ | - |
| test_section2_first_graph_on_device[test_section2_first_graph_on_device] | ✅ | - | - | - |
| test_section3_bounded_graph_matches_numpy[test_section3_bounded_graph_matches_numpy] | ✅ | - | ✅ | - |
| test_section3_bounded_graph_on_device[test_section3_bounded_graph_on_device] | ✅ | - | - | - |
| test_section3_bounded_graph_rejects_an_out_of_range_call[test_section3_bounded_graph_rejects_an_out_of_range_call] | ✅ | - | ✅ | - |
| test_section4_subtraction_exercise_selects_arithmetic[test_section4_subtraction_exercise_selects_arithmetic] | ✅ | - | ✅ | - |
| test_section4_weights_and_state_matches_numpy[test_section4_weights_and_state_matches_numpy] | ✅ | - | ✅ | - |
| test_section4_weights_and_state_on_device[test_section4_weights_and_state_on_device] | ✅ | - | - | - |
| test_section5_carried_loop_on_device[test_section5_carried_loop_on_device] | ✅ | - | - | - |
| test_section5_walk_matches_numpy_host_driven[test_section5_walk_matches_numpy_host_driven] | ✅ | - | ✅ | - |
| test_section6_check_mode_on_device[test_section6_check_mode_on_device] | ✅ | - | - | - |
| test_section6_reference_matches_its_operators_chained_by_hand[test_section6_reference_matches_its_operators_chained_by_hand] | ✅ | - | ✅ | - |
| test_section7_a_calls_own_value_wins_over_the_profile[test_section7_a_calls_own_value_wins_over_the_profile] | ✅ | - | ✅ | - |
| test_section7_profile_on_device[test_section7_profile_on_device] | ✅ | - | - | - |
| test_section7_profile_sets_tunables_by_shape[test_section7_profile_sets_tunables_by_shape] | ✅ | - | ✅ | - |
| test_section8_toy_decoder_matches_numpy[test_section8_toy_decoder_matches_numpy] | ✅ | - | ✅ | - |
| test_section8_toy_decoder_on_device[test_section8_toy_decoder_on_device] | ✅ | - | - | - |

</details>

<details>
<summary>iron/tests/infrastructure</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_batchnorm_s_int64_counter_loads_beside_its_float_weights[test_a_batchnorm_s_int64_counter_loads_beside_its_float_weights] | ✅ | - | ✅ | - |
| test_a_buffer_named_in_part_is_never_pooled[test_a_buffer_named_in_part_is_never_pooled] | ✅ | - | ✅ | - |
| test_a_call_takes_exactly_the_declared_scalars[scalars_{'m': 1}-error_<class 'TypeError'>-match_unexpected keyword argument\(s\): \['m'\]] | ✅ | - | ✅ | - |
| test_a_call_takes_exactly_the_declared_scalars[scalars_{'n': 1, 'm': 1}-error_<class 'TypeError'>-match_unexpected keyword argument\(s\): \['m'\]] | ✅ | - | ✅ | - |
| test_a_call_takes_exactly_the_declared_scalars[scalars_{}-error_<class 'aie.utils.hostruntime.hostruntime.HostRuntimeError'>-match_dispatch scalar mismatch] | ✅ | - | ✅ | - |
| test_a_carried_loop_walks_a_linked_list_on_the_device[depth_1] | ✅ | - | - | - |
| test_a_carried_loop_walks_a_linked_list_on_the_device[depth_2] | ✅ | - | - | - |
| test_a_carried_loop_walks_a_linked_list_on_the_device[depth_3] | ✅ | - | - | - |
| test_a_chain_of_more_designs_than_a_context_configures_runs[test_a_chain_of_more_designs_than_a_context_configures_runs] | ✅ | - | - | - |
| test_a_design_links_the_same_objects_alone_or_composed[test_a_design_links_the_same_objects_alone_or_composed] | ✅ | - | ✅ | - |
| test_a_field_the_repr_leaves_out_still_keys_the_build[test_a_field_the_repr_leaves_out_still_keys_the_build] | ✅ | - | ✅ | - |
| test_a_filled_tree_has_the_checkpoints_names_shapes_and_dtypes[fill_random] | ✅ | - | ✅ | - |
| test_a_filled_tree_has_the_checkpoints_names_shapes_and_dtypes[fill_unread] | ✅ | - | ✅ | - |
| test_a_full_elf_refuses_a_dispatch_value[test_a_full_elf_refuses_a_dispatch_value] | ✅ | - | ✅ | - |
| test_a_full_elf_takes_the_repeat_count_from_the_scratchpad[test_a_full_elf_takes_the_repeat_count_from_the_scratchpad] | ✅ | - | ✅ | - |
| test_a_gap_between_fixed_allocations_is_used_when_it_fits[test_a_gap_between_fixed_allocations_is_used_when_it_fits] | ✅ | - | ✅ | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[aot-dispatch_composed] | ✅ | - | - | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[aot-dispatch_separate] | ✅ | - | - | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[jit-dispatch_composed] | ✅ | - | - | - |
| test_a_graph_matches_the_hand_written_runlist_numerically[jit-dispatch_separate] | ✅ | - | - | - |
| test_a_graph_records_the_same_steps_as_a_hand_written_runlist[test_a_graph_records_the_same_steps_as_a_hand_written_runlist] | ✅ | - | ✅ | - |
| test_a_graph_walks_a_linked_list_through_its_carried_values[test_a_graph_walks_a_linked_list_through_its_carried_values] | ✅ | - | - | - |
| test_a_layer_index_far_past_its_layers_is_refused[test_a_layer_index_far_past_its_layers_is_refused] | ✅ | - | ✅ | - |
| test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice[test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice] | ✅ | - | ✅ | - |
| test_a_pytorch_checkpoint_naming_another_global_is_refused[module_os-name_system] | ✅ | - | ✅ | - |
| test_a_pytorch_checkpoint_naming_another_global_is_refused[module_torch-name_DoubleStorage] | ✅ | - | ✅ | - |
| test_a_pytorch_checkpoint_naming_another_global_is_refused[module_torch._utils-name__rebuild_parameter] | ✅ | - | ✅ | - |
| test_a_pytorch_tensor_outside_its_storage_is_refused[foreign_id] | ✅ | - | ✅ | - |
| test_a_pytorch_tensor_outside_its_storage_is_refused[past_the_end] | ✅ | - | ✅ | - |
| test_a_pytorch_tensor_outside_its_storage_is_refused[short_storage] | ✅ | - | ✅ | - |
| test_a_read_leaves_nothing_for_the_next_call_to_push[test_a_read_leaves_nothing_for_the_next_call_to_push] | ✅ | - | - | - |
| test_a_released_run_is_made_again_on_the_next_call[test_a_released_run_is_made_again_on_the_next_call] | ✅ | - | - | - |
| test_a_resident_has_one_offset_in_every_image[test_a_resident_has_one_offset_in_every_image] | ✅ | - | ✅ | - |
| test_a_resident_needs_a_size[test_a_resident_needs_a_size] | ✅ | - | ✅ | - |
| test_a_session_not_asked_for_a_csv_writes_none[test_a_session_not_asked_for_a_csv_writes_none] | ✅ | - | ✅ | - |
| test_a_test_failing_in_setup_is_a_failed_check[test_a_test_failing_in_setup_is_a_failed_check] | ✅ | - | ✅ | - |
| test_a_traced_build_carries_the_lowered_module[test_a_traced_build_carries_the_lowered_module] | ✅ | - | ✅ | - |
| test_a_tuned_profile_runs_bit_identically[test_a_tuned_profile_runs_bit_identically] | ❌ | - | - | - |
| test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state[test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state] | ✅ | - | ✅ | - |
| test_a_version_reads_as_its_inputs_plan_and_build_directory[test_a_version_reads_as_its_inputs_plan_and_build_directory] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[faster] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[fewer_tokens_a_second] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[kl] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[slower_first_token] | ✅ | - | ✅ | - |
| test_a_worse_time_fails_the_run[within] | ✅ | - | ✅ | - |
| test_a_written_pytorch_tensor_reads_as_its_storage[test_a_written_pytorch_tensor_reads_as_its_storage] | ✅ | - | ✅ | - |
| test_aligned_row_count_records_with_the_given_extents[test_aligned_row_count_records_with_the_given_extents] | ✅ | - | ✅ | - |
| test_an_argument_ends_past_the_arena_buffer_placed_last[test_an_argument_ends_past_the_arena_buffer_placed_last] | ✅ | - | ✅ | - |
| test_an_each_step_version_and_a_full_elf_share_one_arena[test_an_each_step_version_and_a_full_elf_share_one_arena] | ✅ | - | - | - |
| test_an_opaque_design_parameter_is_rejected[test_an_opaque_design_parameter_is_rejected] | ✅ | - | ✅ | - |
| test_an_operator_builds_its_own_image_once[test_an_operator_builds_its_own_image_once] | ✅ | - | ✅ | - |
| test_auto_dispatch_selects_platform_default[size_4096] | ✅ | - | ✅ | - |
| test_captured_graph_compiles_to_an_elf[test_captured_graph_compiles_to_an_elf] | ✅ | - | ✅ | - |
| test_cgroup_limit_reads_the_lowest_ceiling[unbounded] | ✅ | - | ✅ | - |
| test_cgroup_limit_reads_the_lowest_ceiling[v1] | ✅ | - | ✅ | - |
| test_cgroup_limit_reads_the_lowest_ceiling[v2-nested] | ✅ | - | ✅ | - |
| test_check_mode_catches_a_step_outside_its_tolerance_at_that_step[test_check_mode_catches_a_step_outside_its_tolerance_at_that_step] | ✅ | - | - | - |
| test_check_mode_holds_each_step_to_its_reference[test_check_mode_holds_each_step_to_its_reference] | ✅ | - | - | - |
| test_check_mode_judges_each_step_by_its_tolerance[test_check_mode_judges_each_step_by_its_tolerance] | ✅ | - | ✅ | - |
| test_check_mode_judges_every_output_at_the_calls_values[test_check_mode_judges_every_output_at_the_calls_values] | ✅ | - | ✅ | - |
| test_checkpoint_matches_safetensors_for_every_dtype[test_checkpoint_matches_safetensors_for_every_dtype] | ✅ | - | ✅ | - |
| test_checkpoint_reads_a_sharded_index[test_checkpoint_reads_a_sharded_index] | ✅ | - | ✅ | - |
| test_checkpoint_refuses_a_shard_outside_the_index_s_directory[shard_../a.safetensors] | ✅ | - | ✅ | - |
| test_checkpoint_refuses_a_shard_outside_the_index_s_directory[shard_/tmp/a.safetensors] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_malformed_file[range-before-the-data] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_malformed_file[range-not-the-shape] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_malformed_file[range-past-the-end] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_shard_that_disagrees_with_the_index[test_checkpoint_rejects_a_shard_that_disagrees_with_the_index] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_a_tensor_with_no_byte_range[test_checkpoint_rejects_a_tensor_with_no_byte_range] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_an_empty_archive[test_checkpoint_rejects_an_empty_archive] | ✅ | - | ✅ | - |
| test_checkpoint_rejects_an_unsupported_dtype[test_checkpoint_rejects_an_unsupported_dtype] | ✅ | - | ✅ | - |
| test_checkpoint_release_drops_the_right_shard[test_checkpoint_release_drops_the_right_shard] | ✅ | - | ✅ | - |
| test_checkpoint_views_the_mapping_without_copying[test_checkpoint_views_the_mapping_without_copying] | ✅ | - | ✅ | - |
| test_commands_are_runtime_sequences_over_the_same_designs[test_commands_are_runtime_sequences_over_the_same_designs] | ✅ | - | ✅ | - |
| test_composed_mlir_contains_reconfiguration[sequence_add_relu] | ✅ | - | ✅ | - |
| test_designs_of_one_array_run_on_one_configure[test_designs_of_one_array_run_on_one_configure] | ✅ | - | - | - |
| test_device_rows_are_the_host_draws[test_device_rows_are_the_host_draws] | ✅ | - | ✅ | - |
| test_device_rows_refuse_an_unbounded_top_k[test_device_rows_refuse_an_unbounded_top_k] | ✅ | - | ✅ | - |
| test_dispatch_modes_bit_identical[dispatch_compare] | ✅ | - | ✅ | - |
| test_dispatch_modes_bit_identical[dispatch_composed] | ✅ | - | - | - |
| test_dispatch_modes_bit_identical[dispatch_separate] | ✅ | - | ✅ | - |
| test_download_fetches_into_the_cache_not_the_read_only_weights_dir[test_download_fetches_into_the_cache_not_the_read_only_weights_dir] | ✅ | - | ✅ | - |
| test_download_shares_no_partial_file_with_a_concurrent_fetch[test_download_shares_no_partial_file_with_a_concurrent_fetch] | ✅ | - | ✅ | - |
| test_draws_follow_the_distribution[test_draws_follow_the_distribution] | ✅ | - | ✅ | - |
| test_dump_writes_raw_words_and_perfetto_json[test_dump_writes_raw_words_and_perfetto_json] | ✅ | - | - | - |
| test_each_checkpoint_tensor_lands_on_its_name_bitwise[test_each_checkpoint_tensor_lands_on_its_name_bitwise] | ✅ | - | ✅ | - |
| test_each_design_of_one_array_runs_on_its_own_values[test_each_design_of_one_array_runs_on_its_own_values] | ✅ | - | - | - |
| test_each_merge_of_one_array_runs_on_its_own_count[test_each_merge_of_one_array_runs_on_its_own_count] | ✅ | - | - | - |
| test_each_position_table_of_one_array_runs_on_its_own_rows[test_each_position_table_of_one_array_runs_on_its_own_rows] | ✅ | - | - | - |
| test_each_resize_of_one_array_runs_on_its_own_sizes[test_each_resize_of_one_array_runs_on_its_own_sizes] | ✅ | - | - | - |
| test_each_runner_s_nightly_results_get_charts_of_their_own[test_each_runner_s_nightly_results_get_charts_of_their_own] | ✅ | - | ✅ | - |
| test_each_step_versions_share_weights_and_state_through_one_arena[test_each_step_versions_share_weights_and_state_through_one_arena] | ✅ | - | ✅ | - |
| test_each_table_of_one_array_runs_on_its_own_sizes[test_each_table_of_one_array_runs_on_its_own_sizes] | ✅ | - | - | - |
| test_empty_graph[test_empty_graph] | ✅ | - | ✅ | - |
| test_every_dispatch_returns_its_own_output[calls_2] | ✅ | - | ✅ | - |
| test_every_dispatch_returns_its_own_output[calls_3] | ✅ | - | ✅ | - |
| test_feedback_argument_only_when_declared[test_feedback_argument_only_when_declared] | ✅ | - | ✅ | - |
| test_feedback_chain_queued[test_feedback_chain_queued] | ✅ | - | - | - |
| test_feedback_into_plain_buffers[test_feedback_into_plain_buffers] | ✅ | - | - | - |
| test_feedback_ping_pong[test_feedback_ping_pong] | ✅ | - | - | - |
| test_feedback_with_trace[test_feedback_with_trace] | ✅ | - | - | - |
| test_fixed_allocations_are_obstacles_at_every_step[test_fixed_allocations_are_obstacles_at_every_step] | ✅ | - | ✅ | - |
| test_graph_inputs_and_outputs_are_left_alone[test_graph_inputs_and_outputs_are_left_alone] | ✅ | - | ✅ | - |
| test_greedy_is_argmax[test_greedy_is_argmax] | ✅ | - | ✅ | - |
| test_identical_operators_reuse_the_compiled_xclbin[test_identical_operators_reuse_the_compiled_xclbin] | ✅ | - | ✅ | - |
| test_identical_sequences_reuse_the_compiled_elf[test_identical_sequences_reuse_the_compiled_elf] | ✅ | - | ✅ | - |
| test_importing_iron_and_its_applications_imports_no_torch_or_transformers[test_importing_iron_and_its_applications_imports_no_torch_or_transformers] | ✅ | - | ✅ | - |
| test_int32_slice_at_word_offset[test_int32_slice_at_word_offset] | ✅ | - | - | - |
| test_int32_step_at_nonzero_offsets[test_int32_step_at_nonzero_offsets] | ✅ | - | - | - |
| test_kernel_objects_land_in_the_entry_under_bare_names[test_kernel_objects_land_in_the_entry_under_bare_names] | ✅ | - | ✅ | - |
| test_live_range_overlap[test_live_range_overlap] | ✅ | - | ✅ | - |
| test_llama3_scaling_matches_the_formula_in_every_band[test_llama3_scaling_matches_the_formula_in_every_band] | ✅ | - | ✅ | - |
| test_load_hands_each_piece_of_each_weight_to_release_once_it_is_uploaded[test_load_hands_each_piece_of_each_weight_to_release_once_it_is_uploaded] | ✅ | - | ✅ | - |
| test_load_loads_a_version_whose_weights_are_already_uploaded[test_load_loads_a_version_whose_weights_are_already_uploaded] | ✅ | - | ✅ | - |
| test_misaligned_buffer_is_rejected[test_misaligned_buffer_is_rejected] | ✅ | - | ✅ | - |
| test_mixed_sizes_reach_the_lower_bound[test_mixed_sizes_reach_the_lower_bound] | ✅ | - | ✅ | - |
| test_non_aligned_row_count_raises_instead_of_being_padded[test_non_aligned_row_count_raises_instead_of_being_padded] | ✅ | - | ✅ | - |
| test_non_input_buffers_sync_without_explicit_flush[dispatch_composed] | ✅ | - | - | - |
| test_non_input_buffers_sync_without_explicit_flush[dispatch_separate] | ✅ | - | ✅ | - |
| test_npu1_xclbin_pushes_the_call_s_repeat_count[test_npu1_xclbin_pushes_the_call_s_repeat_count] | ✅ | - | ✅ | - |
| test_odd_sizes_never_leave_an_offset_unaligned[test_odd_sizes_never_leave_an_offset_unaligned] | ✅ | - | ✅ | - |
| test_offsets_are_aligned[test_offsets_are_aligned] | ✅ | - | ✅ | - |
| test_one_design_expands_only_to_reconfigure[reconfigure_False] | ✅ | - | ✅ | - |
| test_one_design_expands_only_to_reconfigure[reconfigure_True] | ✅ | - | ✅ | - |
| test_one_design_is_configured_once[test_one_design_is_configured_once] | ✅ | - | - | - |
| test_one_design_reconfigures_after_another_image[test_one_design_reconfigures_after_another_image] | ✅ | - | - | - |
| test_one_image_repeats_a_tile_k_times[image_elf] | ✅ | - | - | - |
| test_one_image_repeats_a_tile_k_times[image_xclbin] | ✅ | - | - | - |
| test_one_image_serves_every_parameter[test_one_image_serves_every_parameter] | ✅ | - | ✅ | - |
| test_one_operator_is_timed_from_the_command_line[test_one_operator_is_timed_from_the_command_line] | ✅ | - | - | - |
| test_one_storage_is_one_size[test_one_storage_is_one_size] | ✅ | - | ✅ | - |
| test_pinned_buffers_are_not_pooled[test_pinned_buffers_are_not_pooled] | ✅ | - | ✅ | - |
| test_random_fill_draws_a_bias_about_zero[test_random_fill_draws_a_bias_about_zero] | ✅ | - | ✅ | - |
| test_random_fill_draws_at_its_seed[test_random_fill_draws_at_its_seed] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_0] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_10] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_11] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_12] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_13] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_14] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_15] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_16] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_17] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_18] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_19] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_1] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_2] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_3] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_4] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_5] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_6] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_7] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_8] | ✅ | - | ✅ | - |
| test_random_images_keep_every_invariant[seed_9] | ✅ | - | ✅ | - |
| test_real_checkpoint_every_tensor_bitwise[test_real_checkpoint_every_tensor_bitwise] | ✅ | - | ✅ | - |
| test_real_checkpoint_is_llama_3_2_1b[test_real_checkpoint_is_llama_3_2_1b] | ✅ | - | ✅ | - |
| test_real_sharded_checkpoint_every_tensor_bitwise[test_real_sharded_checkpoint_every_tensor_bitwise] | ✅ | - | ✅ | - |
| test_real_tokenizer_s_added_tokens_are_their_ids[test_real_tokenizer_s_added_tokens_are_their_ids] | ✅ | - | ✅ | - |
| test_refuses_an_n_past_the_buffers[test_refuses_an_n_past_the_buffers] | ✅ | - | ✅ | - |
| test_release_drops_the_pages_and_keeps_the_bytes[test_release_drops_the_pages_and_keeps_the_bytes] | ✅ | - | ✅ | - |
| test_release_frees_the_buffers_and_the_next_call_loads_them_again[test_release_frees_the_buffers_and_the_next_call_loads_them_again] | ✅ | - | ✅ | - |
| test_release_leaves_anything_else_alone[test_release_leaves_anything_else_alone] | ✅ | - | ✅ | - |
| test_renamed_is_a_copy_a_caller_may_change[test_renamed_is_a_copy_a_caller_may_change] | ✅ | - | ✅ | - |
| test_repeated_block_packs_to_one_block_worth[test_repeated_block_packs_to_one_block_worth] | ✅ | - | ✅ | - |
| test_restricted_test_without_npu_runtime_skips_with_the_reason[test_restricted_test_without_npu_runtime_skips_with_the_reason] | ✅ | - | ✅ | - |
| test_restricted_tests_skip_where_the_device_is_not_listed[test_restricted_tests_skip_where_the_device_is_not_listed] | ✅ | - | ✅ | - |
| test_rope_is_correctly_rounded_at_position_zero_and_one[test_rope_is_correctly_rounded_at_position_zero_and_one] | ✅ | - | ✅ | - |
| test_rope_is_the_formula_rounded_once[test_rope_is_the_formula_rounded_once] | ✅ | - | ✅ | - |
| test_scaled_rope_table_rotates_by_the_scaled_frequencies[test_scaled_rope_table_rotates_by_the_scaled_frequencies] | ✅ | - | ✅ | - |
| test_seeded_sampling_is_reproducible[test_seeded_sampling_is_reproducible] | ✅ | - | ✅ | - |
| test_sequential_chain_double_buffers[test_sequential_chain_double_buffers] | ✅ | - | ✅ | - |
| test_simultaneously_live_buffers_do_not_share[test_simultaneously_live_buffers_do_not_share] | ✅ | - | ✅ | - |
| test_the_compile_key_covers_the_library_a_design_calls[test_the_compile_key_covers_the_library_a_design_calls] | ✅ | - | ✅ | - |
| test_the_compile_key_does_not_depend_on_a_device_being_bound_yet[test_the_compile_key_does_not_depend_on_a_device_being_bound_yet] | ✅ | - | - | - |
| test_the_compile_key_is_stable_across_identical_operators[test_the_compile_key_is_stable_across_identical_operators] | ✅ | - | ✅ | - |
| test_the_device_keys_the_build_by_identity_not_address[test_the_device_keys_the_build_by_identity_not_address] | ✅ | - | ✅ | - |
| test_the_lm_testing_helpers_import_without_pytest[test_the_lm_testing_helpers_import_without_pytest] | ✅ | - | ✅ | - |
| test_the_prompt_text_repeats_past_its_end[test_the_prompt_text_repeats_past_its_end] | ✅ | - | ✅ | - |
| test_the_stream_is_generated_per_call[test_the_stream_is_generated_per_call] | ✅ | - | ✅ | - |
| test_top_k_keeps_ties_with_the_kth[test_top_k_keeps_ties_with_the_kth] | ✅ | - | ✅ | - |
| test_top_k_never_leaves_the_top_k[test_top_k_never_leaves_the_top_k] | ✅ | - | ✅ | - |
| test_touching_ranges_ignore_names_not_asked_for[test_touching_ranges_ignore_names_not_asked_for] | ✅ | - | ✅ | - |
| test_touching_ranges_span_first_to_last_use_whatever_the_direction[test_touching_ranges_span_first_to_last_use_whatever_the_direction] | ✅ | - | ✅ | - |
| test_tree_names_a_layer_past_the_last[test_tree_names_a_layer_past_the_last] | ✅ | - | ✅ | - |
| test_tree_names_a_missing_tensor_by_its_path_and_file[test_tree_names_a_missing_tensor_by_its_path_and_file] | ✅ | - | ✅ | - |
| test_tree_names_a_tensor_of_a_skipped_layer[test_tree_names_a_tensor_of_a_skipped_layer] | ✅ | - | ✅ | - |
| test_two_graphs_get_distinct_cache_keys[test_two_graphs_get_distinct_cache_keys] | ✅ | - | ✅ | - |
| test_two_shapes_share_weights_and_state_through_one_arena[test_two_shapes_share_weights_and_state_through_one_arena] | ✅ | - | - | - |
| test_unread_fill_zeroes_a_scalar[test_unread_fill_zeroes_a_scalar] | ✅ | - | ✅ | - |
| test_unrestricted_tests_need_no_npu_runtime[test_unrestricted_tests_need_no_npu_runtime] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/tests/lm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_cache_attends_within_its_window[test_a_cache_attends_within_its_window] | ✅ | - | ✅ | - |
| test_a_causal_model_draws_after_its_soft_tokens[test_a_causal_model_draws_after_its_soft_tokens] | ✅ | - | - | - |
| test_a_causal_model_places_soft_tokens_across_its_chunks[test_a_causal_model_places_soft_tokens_across_its_chunks] | ✅ | - | - | - |
| test_a_graph_held_at_two_paths_skips_the_second_paths_tensors[test_a_graph_held_at_two_paths_skips_the_second_paths_tensors] | ✅ | - | ✅ | - |
| test_a_layer_reading_another_s_cache_projects_and_writes_no_keys[test_a_layer_reading_another_s_cache_projects_and_writes_no_keys] | ✅ | - | ✅ | - |
| test_a_param_never_bound_is_named_at_record[test_a_param_never_bound_is_named_at_record] | ✅ | - | ✅ | - |
| test_a_q_table_scaled_by_two_doubles_the_logits_scale[test_a_q_table_scaled_by_two_doubles_the_logits_scale] | ✅ | - | ✅ | - |
| test_a_random_tree_draws_a_scalar_as_an_array[test_a_random_tree_draws_a_scalar_as_an_array] | ✅ | - | ✅ | - |
| test_a_ring_restarts_at_the_chunk_while_it_holds_the_window_before[test_a_ring_restarts_at_the_chunk_while_it_holds_the_window_before] | ✅ | - | ✅ | - |
| test_a_ring_s_chunk_attends_from_its_valid_rows_alone[test_a_ring_s_chunk_attends_from_its_valid_rows_alone] | ✅ | - | ✅ | - |
| test_a_second_bind_is_refused[test_a_second_bind_is_refused] | ✅ | - | ✅ | - |
| test_a_tied_param_ignores_a_tensor_at_its_other_path[test_a_tied_param_ignores_a_tensor_at_its_other_path] | ✅ | - | ✅ | - |
| test_a_turn_over_a_ring_is_the_run_from_scratch_bit_for_bit[test_a_turn_over_a_ring_is_the_run_from_scratch_bit_for_bit] | ✅ | - | ✅ | - |
| test_a_window_keeps_every_position_where_a_ring_takes_as_many_rows[test_a_window_keeps_every_position_where_a_ring_takes_as_many_rows] | ✅ | - | ✅ | - |
| test_an_index_a_checkpoint_skips_is_empty_and_no_leaf[test_an_index_a_checkpoint_skips_is_empty_and_no_leaf] | ✅ | - | ✅ | - |
| test_an_odd_vocabulary_pads_the_head_with_a_row_no_draw_takes[test_an_odd_vocabulary_pads_the_head_with_a_row_no_draw_takes] | ✅ | - | ✅ | - |
| test_attention_refuses_a_norm_of_other_than_q_k_and_v[test_attention_refuses_a_norm_of_other_than_q_k_and_v] | ✅ | - | ✅ | - |
| test_attention_turns_only_the_rotary_columns[test_attention_turns_only_the_rotary_columns] | ✅ | - | ✅ | - |
| test_conv2d[case_depthwise_13_rows-share_0.25] | ✅ | - | ✅ | - |
| test_conv2d[case_depthwise_13_rows-share_1.0] | ✅ | - | ✅ | - |
| test_each_generation_check_prefills_its_whole_prompt[test_each_generation_check_prefills_its_whole_prompt] | ✅ | - | ✅ | - |
| test_each_layer_reads_the_rows_of_its_own_rope[test_each_layer_reads_the_rows_of_its_own_rope] | ✅ | - | ✅ | - |
| test_embedding_gemma2_is_on_npu[test_embedding_gemma2_is_on_npu] | ✅ | - | ✅ | - |
| test_gemma4_towers_are_on_npu[test_gemma4_towers_are_on_npu] | ✅ | - | ✅ | - |
| test_leaf_modules_match_numpy[test_leaf_modules_match_numpy] | ✅ | - | ✅ | - |
| test_load_state_dict_casts_to_the_params_dtype[test_load_state_dict_casts_to_the_params_dtype] | ✅ | - | ✅ | - |
| test_load_state_dict_names_each_kind_in_one_error[test_load_state_dict_names_each_kind_in_one_error] | ✅ | - | ✅ | - |
| test_load_state_dict_refuses_a_change_of_kind[test_load_state_dict_refuses_a_change_of_kind] | ✅ | - | ✅ | - |
| test_load_state_dict_refuses_a_param_in_a_frozen_dataclass[test_load_state_dict_refuses_a_param_in_a_frozen_dataclass] | ✅ | - | ✅ | - |
| test_load_state_dict_refuses_a_param_in_a_tuple[test_load_state_dict_refuses_a_param_in_a_tuple] | ✅ | - | ✅ | - |
| test_log_mel[frames_200] | ✅ | 5222.34 | ✅ | 28648.62 |
| test_log_mel[frames_3072] | ✅ | 12643.42 | ✅ | 24585.09 |
| test_tensors_at_indices_are_a_list_of_tensors[test_tensors_at_indices_are_a_list_of_tensors] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/tests/operators</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_bound_past_a_wrap_of_tiles_per_lane[test_a_bound_past_a_wrap_of_tiles_per_lane] | ✅ | - | - | - |
| test_a_bounded_gather_moves_its_rows_and_a_unit_for_each_other[test_a_bounded_gather_moves_its_rows_and_a_unit_for_each_other] | ✅ | - | ✅ | - |
| test_a_bounded_gather_of_rows_not_whole_16_byte_units_is_refused[test_a_bounded_gather_of_rows_not_whole_16_byte_units_is_refused] | ✅ | - | ✅ | - |
| test_a_bounded_prompt_chunk_moves_13_rows_not_2048[test_a_bounded_prompt_chunk_moves_13_rows_not_2048] | ✅ | - | ✅ | - |
| test_a_call_starts_its_queries_anywhere[causal] | ✅ | - | - | - |
| test_a_call_starts_its_queries_anywhere[sliding] | ✅ | - | - | - |
| test_a_chunk_attends_over_the_cache_before_it[full_elf] | ✅ | - | - | - |
| test_a_chunk_attends_over_the_cache_before_it[xclbin] | ✅ | - | - | - |
| test_a_chunk_lands_in_its_rows_of_the_cache[test_a_chunk_lands_in_its_rows_of_the_cache] | ✅ | - | - | - |
| test_a_copy_moves_the_valid_rows_of_each_head[test_a_copy_moves_the_valid_rows_of_each_head] | ✅ | - | - | - |
| test_a_float32_softmax_under_a_per_call_bound_is_refused[test_a_float32_softmax_under_a_per_call_bound_is_refused] | ✅ | - | ✅ | - |
| test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu1-feeds_3] | ✅ | - | ✅ | - |
| test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu2-feeds_0] | ✅ | - | ✅ | - |
| test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu2-feeds_5] | ✅ | - | ✅ | - |
| test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused[test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused] | ✅ | - | ✅ | - |
| test_a_given_raster_keeps_the_rows_past_the_image[test_a_given_raster_keeps_the_rows_past_the_image] | ✅ | - | ✅ | - |
| test_a_graph_gathers_twice_from_a_weight_and_a_state[full_elf] | ✅ | - | - | - |
| test_a_graph_gathers_twice_from_a_weight_and_a_state[xclbin] | ✅ | - | - | - |
| test_a_line_of_part_of_a_vector_is_refused[limbs] | ✅ | - | ✅ | - |
| test_a_line_of_part_of_a_vector_is_refused[magnitude] | ✅ | - | ✅ | - |
| test_a_row_lands_at_its_index_on_the_leading_axis[full_elf] | ✅ | - | - | - |
| test_a_row_lands_at_its_index_on_the_leading_axis[xclbin] | ✅ | - | - | - |
| test_a_run_lands_from_any_start_and_is_read_back[full_elf] | ✅ | - | - | - |
| test_a_run_lands_from_any_start_and_is_read_back[xclbin] | ✅ | - | - | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu1-precision_high-M_16-rows_1-tile_m_16] | ✅ | - | ✅ | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu1-precision_high-M_32-rows_2-tile_m_16] | ✅ | - | ✅ | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu2-precision_high-M_16-rows_2-tile_m_8] | ✅ | - | ✅ | - |
| test_a_short_m_takes_fewer_rows_of_cores[device_npu2-precision_medium-M_32-rows_2-tile_m_16] | ✅ | - | ✅ | - |
| test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused[test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused] | ✅ | - | ✅ | - |
| test_a_tile_past_what_one_core_holds_is_refused_not_split[test_a_tile_past_what_one_core_holds_is_refused_not_split] | ✅ | - | ✅ | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[flat-channels_1] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[flat-channels_2] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[flat-channels_4] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[head_rows-channels_1] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[head_rows-channels_2] | ✅ | - | - | - |
| test_a_transpose_into_wider_rows_on_any_channel_count[head_rows-channels_4] | ✅ | - | - | - |
| test_a_transposing_copy_on_any_channel_count[channels_1] | ✅ | - | - | - |
| test_a_transposing_copy_on_any_channel_count[channels_2] | ✅ | - | - | - |
| test_a_transposing_copy_on_any_channel_count[channels_4] | ✅ | - | - | - |
| test_a_validate_or_compatible_branch_refuses[clamp_bounds] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[conv_channels] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[conv_runs] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[emit_rows] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_angle_rows] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_angle_rows_split] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_cols] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[rope_rows_split] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[softmax_f32_option] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[softmax_window_alone] | ✅ | - | ✅ | - |
| test_a_validate_or_compatible_branch_refuses[softmax_window_no_addend] | ✅ | - | ✅ | - |
| test_a_walk_by_a_per_call_repeat_and_length_is_its_reference[band_stride_0] | ✅ | - | ✅ | - |
| test_a_walk_by_a_per_call_repeat_and_length_is_its_reference[band_stride_1] | ✅ | - | ✅ | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_0-full_elf] | ✅ | - | - | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_0-xclbin] | ✅ | - | - | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_1-full_elf] | ✅ | - | - | - |
| test_a_walk_repeats_and_bounds_per_call[band_stride_1-xclbin] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[llama] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[resident] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[resident_tail] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[slice_is_k_max] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[streamed] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[streamed_unaligned] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[uneven] | ✅ | - | - | - |
| test_adversarial_logits_draw_the_reference_token[uneven_streamed] | ✅ | - | - | - |
| test_aie2_activations_bring_their_lut_tables_into_the_frame[test_aie2_activations_bring_their_lut_tables_into_the_frame] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_64] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_128] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_16] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_32] | ✅ | - | ✅ | - |
| test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_64] | ✅ | - | ✅ | - |
| test_an_input_gathers_from_a_table_once[test_an_input_gathers_from_a_table_once] | ✅ | - | ✅ | - |
| test_an_m_no_tile_splits_is_rejected[device_npu1-precision_high] | ✅ | - | ✅ | - |
| test_an_m_no_tile_splits_is_rejected[device_npu2-precision_medium] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu1-precision_high-M_64-tile_m_16] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_high-M_32-tile_m_8] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_128-tile_m_32] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_2048-tile_m_64] | ✅ | - | ✅ | - |
| test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_64-tile_m_16] | ✅ | - | ✅ | - |
| test_attention_reduces_over_the_valid_keys[test_attention_reduces_over_the_valid_keys] | ✅ | - | - | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_32-chunks_1] | ✅ | - | ✅ | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_32-chunks_3] | ✅ | - | ✅ | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_64-chunks_1] | ✅ | - | ✅ | - |
| test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_64-chunks_3] | ✅ | - | ✅ | - |
| test_bounded_rows_past_a_wrap_fill_either_half[test_bounded_rows_past_a_wrap_fill_either_half] | ✅ | - | - | - |
| test_bounded_rows_past_a_wrap_halve_the_run[test_bounded_rows_past_a_wrap_halve_the_run] | ✅ | - | ✅ | - |
| test_buffers_do_not_follow_the_pipeline_count[test_buffers_do_not_follow_the_pipeline_count] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_1024-N_128] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_1536-N_640] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_2048-N_2048] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_2048-N_256] | ✅ | - | ✅ | - |
| test_bytes_match_pack_b[K_512-N_64] | ✅ | - | ✅ | - |
| test_channels_not_dividing_the_shared_run_are_rejected[test_channels_not_dividing_the_shared_run_are_rejected] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_128] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_16] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_32] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_64] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_128] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_16] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_32] | ✅ | - | ✅ | - |
| test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_64] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu1-b_bytes_2-tile_n_128-expected_(32, 32, 2)] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu1-b_bytes_2-tile_n_64-expected_(64, 64, 2)] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu2-b_bytes_1.125-tile_n_128-expected_(64, 32, 2)] | ✅ | - | ✅ | - |
| test_default_tiles_account_for_the_frame[device_npu2-b_bytes_1.125-tile_n_64-expected_(128, 32, 2)] | ✅ | - | ✅ | - |
| test_descriptors_are_dma_expressible[test_descriptors_are_dma_expressible] | ✅ | - | ✅ | - |
| test_each_step_gathers_by_ids_the_device_made[n_ids_15] | ✅ | - | ✅ | - |
| test_each_step_gathers_by_ids_the_device_made[n_ids_512] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds[n_ids_15] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds[n_ids_256] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds_by_ids_the_device_made[n_ids_15] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_a_call_bounds_by_ids_the_device_made[n_ids_256] | ✅ | - | ✅ | - |
| test_each_step_gathers_the_rows_an_input_names[test_each_step_gathers_the_rows_an_input_names] | ✅ | - | ✅ | - |
| test_every_operator_is_in_the_catalog[test_every_operator_is_in_the_catalog] | ✅ | - | ✅ | - |
| test_every_row_of_a_bound_is_computed[test_every_row_of_a_bound_is_computed] | ✅ | - | - | - |
| test_explicit_aie2_tile_falls_back_to_single_buffered_b[test_explicit_aie2_tile_falls_back_to_single_buffered_b] | ✅ | - | ✅ | - |
| test_flm_decode_layer_rejects_unknown_configurations[geometry] | ✅ | - | ✅ | - |
| test_flm_decode_layer_rejects_unknown_configurations[layer_type] | ✅ | - | ✅ | - |
| test_flm_dequant_rejects_unservable_shapes[K_1000-N_128-match_K \(1000\)] | ✅ | - | ✅ | - |
| test_flm_dequant_rejects_unservable_shapes[K_1024-N_100-match_N \(100\)] | ✅ | - | ✅ | - |
| test_flm_gemm_reads_b_as_stored_in_bf16[test_flm_gemm_reads_b_as_stored_in_bf16] | ✅ | - | ✅ | - |
| test_flm_lm_head_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_dim \(1000\) must be a multiple] | ✅ | - | ✅ | - |
| test_flm_lm_head_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_vocab \(1000\) must be a multiple] | ✅ | - | ✅ | - |
| test_flm_lm_head_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads] | ✅ | - | ✅ | - |
| test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128] | ✅ | - | ✅ | - |
| test_gemm_on_columns_that_do_not_divide_its_rows_is_refused[device_npu1] | ✅ | - | ✅ | - |
| test_gemm_on_columns_that_do_not_divide_its_rows_is_refused[device_npu2] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[k4_emulated] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[m8] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[m8_emulated] | ✅ | - | ✅ | - |
| test_gemm_tile_the_kernel_cannot_build_is_rejected[n8] | ✅ | - | ✅ | - |
| test_ids_past_the_table_are_refused[outside_-262145] | ✅ | - | - | - |
| test_ids_past_the_table_are_refused[outside_262144] | ✅ | - | - | - |
| test_merge_of_no_or_repeated_placeholders_is_refused[placeholders_((7, 0), (7, 64))] | ✅ | - | ✅ | - |
| test_merge_of_no_or_repeated_placeholders_is_refused[placeholders_()] | ✅ | - | ✅ | - |
| test_merge_of_part_of_a_block_is_refused[test_merge_of_part_of_a_block_is_refused] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[block_past_the_padding] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[empty_window] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[head_not_whole_64] | ✅ | - | ✅ | - |
| test_mha_band_and_head_that_do_not_tile_are_refused[negative_scale] | ✅ | - | ✅ | - |
| test_mha_of_one_query_that_does_not_pack_is_refused[group_past_a_block] | ✅ | - | ✅ | - |
| test_mha_of_one_query_that_does_not_pack_is_refused[more_than_four_pipelines] | ✅ | - | ✅ | - |
| test_mha_of_one_query_that_does_not_pack_is_refused[uneven_groups] | ✅ | - | ✅ | - |
| test_mha_one_query_packed_takes_the_narrowest_block_and_64_keys[test_mha_one_query_packed_takes_the_narrowest_block_and_64_keys] | ✅ | - | ✅ | - |
| test_mha_whose_blocks_do_not_line_up_is_refused[kv_len_not_whole_blocks] | ✅ | - | ✅ | - |
| test_mha_whose_blocks_do_not_line_up_is_refused[kv_len_short_of_queries] | ✅ | - | ✅ | - |
| test_mha_whose_head_fits_no_block_is_refused[test_mha_whose_head_fits_no_block_is_refused] | ✅ | - | ✅ | - |
| test_mha_whose_pipelines_do_not_fill_the_rows_is_refused[test_mha_whose_pipelines_do_not_fill_the_rows_is_refused] | ✅ | - | ✅ | - |
| test_mha_whose_pv_split_does_not_route_is_refused[one_query_packed] | ✅ | - | ✅ | - |
| test_mha_whose_pv_split_does_not_route_is_refused[six_pipelines_to_a_join] | ✅ | - | ✅ | - |
| test_mha_whose_pv_split_does_not_route_is_refused[three_ways] | ✅ | - | ✅ | - |
| test_one_input_s_ids_gather_from_each_of_three_tables[full_elf_False] | ✅ | - | - | - |
| test_one_input_s_ids_gather_from_each_of_three_tables[full_elf_True] | ✅ | - | - | - |
| test_one_pipeline_fills_k_and_v_past_the_task_queue[test_one_pipeline_fills_k_and_v_past_the_task_queue] | ✅ | - | - | - |
| test_one_query_is_as_accurate_deep_in_the_cache_as_near_its_start[test_one_query_is_as_accurate_deep_in_the_cache_as_near_its_start] | ✅ | - | - | - |
| test_operator[npu1-AXPY-size_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | - | - | ✅ | 33.08 |
| test_operator[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | - | - | ✅ | 23.34 |
| test_operator[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | - | - | ✅ | 20.39 |
| test_operator[npu1-AXPY-size_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | - | - | ✅ | 33.99 |
| test_operator[npu1-AXPY-size_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 30.02 |
| test_operator[npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 1562.27 |
| test_operator[npu1-Clamp-size_1024-num_aie_columns_4-num_channels_2-tile_size_128-low_-0.75-high_1.25] | - | - | ✅ | 57.22 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | - | - | ✅ | 26.20 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_1-tile_size_2048-low_0.5-high_1.5] | - | - | ✅ | 22.44 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_2-tile_size_1024-low_-30000.0-high_30000.0] | - | - | ✅ | 20.01 |
| test_operator[npu1-Clamp-size_2048-num_aie_columns_4-num_channels_2-tile_size_256-low_-0.75-high_1.25] | - | - | ✅ | 50.80 |
| test_operator[npu1-Clamp-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096-low_-0.75-high_1.25] | - | - | ✅ | 26.76 |
| test_operator[npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25] | - | - | ✅ | 1132.01 |
| test_operator[npu1-Copy-bench_flat_4mi] | - | - | ✅ | 1062.44 |
| test_operator[npu1-Copy-by_head_two_channels] | - | - | ✅ | 17.67 |
| test_operator[npu1-Copy-chunked_transfer] | - | - | ✅ | 21.90 |
| test_operator[npu1-Copy-contiguous] | - | - | ✅ | 18.13 |
| test_operator[npu1-Copy-float32] | - | - | ✅ | 22.59 |
| test_operator[npu1-Copy-past_one_memtile] | - | - | ✅ | 560.00 |
| test_operator[npu1-Copy-slot5] | - | - | ✅ | 13.90 |
| test_operator[npu1-Copy-slot5_two_channels] | - | - | ✅ | 17.58 |
| test_operator[npu1-Copy-slot_last] | - | - | ✅ | 13.76 |
| test_operator[npu1-Copy-two_channels] | - | - | ✅ | 17.29 |
| test_operator[npu1-DepthwiseConv1d-rows_64-channels_256-num_aie_columns_2] | - | - | ✅ | 24.38 |
| test_operator[npu1-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | - | - | ✅ | 27.82 |
| test_operator[npu1-ElementwiseAdd-size_1024-num_aie_columns_4-tile_size_256] | - | - | ✅ | 34.56 |
| test_operator[npu1-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 19.81 |
| test_operator[npu1-ElementwiseAdd-size_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 31.94 |
| test_operator[npu1-ElementwiseAdd-size_4096-num_aie_columns_1-tile_size_4096] | - | - | ✅ | 24.94 |
| test_operator[npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 1556.08 |
| test_operator[npu1-ElementwiseMul-size_1024-num_aie_columns_4-tile_size_256] | - | - | ✅ | 31.17 |
| test_operator[npu1-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 21.83 |
| test_operator[npu1-ElementwiseMul-size_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 43.31 |
| test_operator[npu1-ElementwiseMul-size_4096-num_aie_columns_1-tile_size_4096] | - | - | ✅ | 23.36 |
| test_operator[npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3405.15 |
| test_operator[npu1-Emit-eight_carried] | - | - | ✅ | 17.16 |
| test_operator[npu1-Emit-one_carried] | - | - | ✅ | 29.10 |
| test_operator[npu1-GELU-size_1024-num_aie_columns_4-num_channels_2-tile_size_128-approximate_none] | - | - | ✅ | 49.58 |
| test_operator[npu1-GELU-size_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 47.80 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-approximate_none] | - | - | ✅ | 58.32 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 23.79 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256-approximate_none] | - | - | ✅ | 45.02 |
| test_operator[npu1-GELU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 50.08 |
| test_operator[npu1-GELU-size_8192-num_aie_columns_1-num_channels_1-tile_size_8192-approximate_none] | - | - | ✅ | 138.95 |
| test_operator[npu1-GELU-size_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | - | - | ✅ | 45.84 |
| test_operator[npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3216.79 |
| test_operator[npu1-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | - | - | ✅ | 63.28 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | - | - | ✅ | 7709.33 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | - | - | ✅ | 79132.02 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-precision_medium-placement_tiles] | - | - | ✅ | 17947.54 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 18102.01 |
| test_operator[npu1-GEMM-M_2048-K_2048-N_8192-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 71615.66 |
| test_operator[npu1-GEMM-M_2048-K_64-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 2346.27 |
| test_operator[npu1-GEMM-M_2048-K_64-N_8192-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 4246.17 |
| test_operator[npu1-GEMM-M_2048-K_8192-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 76398.26 |
| test_operator[npu1-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | - | - | ✅ | -44.98 |
| test_operator[npu1-GEMM-M_384-K_1536-N_1792-num_aie_columns_4-tile_m_32-tile_k_48-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | - | - | ✅ | 4359.47 |
| test_operator[npu1-GEMM-f32_out] | - | - | ✅ | 173.67 |
| test_operator[npu1-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | - | - | ✅ | 1528.33 |
| test_operator[npu1-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_2] | - | - | ✅ | 2144.13 |
| test_operator[npu1-GEMV-M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | - | - | ✅ | 323.96 |
| test_operator[npu1-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | - | - | ✅ | 34.02 |
| test_operator[npu1-GEMV-M_2048-K_64-num_aie_columns_4-tile_size_input_4-tile_size_output_256-num_channels_2-num_batches_32-repeat_4] | - | - | ✅ | 567.45 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | - | - | ✅ | 147.64 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_32-num_channels_2-num_batches_8] | - | - | ✅ | 105.53 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_4] | - | - | ✅ | 95.17 |
| test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_8-repeat_4] | - | - | ✅ | 156.78 |
| test_operator[npu1-GEMV-M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | - | - | ✅ | 437.70 |
| test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 20.10 |
| test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 21.69 |
| test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | - | - | ✅ | 21.79 |
| test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_8192] | - | - | ✅ | 28.73 |
| test_operator[npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 1191.29 |
| test_operator[npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3176.20 |
| test_operator[npu1-LayerNorm-rows_4-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | - | - | ✅ | 30.79 |
| test_operator[npu1-LayerNorm-rows_4-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | - | - | ✅ | 28.79 |
| test_operator[npu1-LayerNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 46.77 |
| test_operator[npu1-LayerNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 44.94 |
| test_operator[npu1-Limbs-rows_512-line_320-num_aie_columns_4] | - | - | ✅ | 157.84 |
| test_operator[npu1-Limbs-rows_64-line_160-num_aie_columns_1] | - | - | ✅ | 63.07 |
| test_operator[npu1-Log-size_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 53.83 |
| test_operator[npu1-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 64.96 |
| test_operator[npu1-Log-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 46.86 |
| test_operator[npu1-Log-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 102.68 |
| test_operator[npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 22459.95 |
| test_operator[npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4] | - | - | ✅ | 81287.13 |
| test_operator[npu1-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | - | - | ✅ | 1272.95 |
| test_operator[npu1-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | - | - | ✅ | 372.33 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | - | - | ✅ | 299.75 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_4-heads_interleaved_True] | - | - | ✅ | 11649.01 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_4] | - | - | ✅ | 65310.44 |
| test_operator[npu1-MHA-num_heads_4-num_KV_heads_2-seq_len_2000-d_256-causal_False-window_512-num_pipelines_4] | - | - | ✅ | 49182.60 |
| test_operator[npu1-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | - | - | ✅ | 366.00 |
| test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_1-kv_len_512-num_pipelines_1] | - | - | ✅ | 81.05 |
| test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4] | - | - | ✅ | 640271.41 |
| test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-d_128-num_pipelines_4] | - | - | ✅ | 40633.63 |
| test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_4] | - | - | ✅ | 57825.80 |
| test_operator[npu1-Magnitude-rows_512-width_640-num_aie_columns_4] | - | - | ✅ | 440.75 |
| test_operator[npu1-Magnitude-rows_64-width_640-num_aie_columns_1] | - | - | ✅ | 238.21 |
| test_operator[npu1-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))-offset_True] | - | - | ✅ | 21.15 |
| test_operator[npu1-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))] | - | - | ✅ | 20.11 |
| test_operator[npu1-Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))] | - | - | ✅ | 32.82 |
| test_operator[npu1-Merge-rows_192-placeholders_((49190, 64),)] | - | - | ✅ | 23.38 |
| test_operator[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))-offset_True] | - | - | ✅ | 85.27 |
| test_operator[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | - | - | ✅ | 80.70 |
| test_operator[npu1-PatchPositions-rows_2048-out_height_480-out_width_1056-cores_8] | - | - | ✅ | 102.57 |
| test_operator[npu1-PatchPositions-rows_2304-out_height_768-out_width_768] | - | - | ✅ | 120.15 |
| test_operator[npu1-PatchPositions-rows_256-out_height_48-out_width_48] | - | - | ✅ | 26.66 |
| test_operator[npu1-PatchPositions-rows_2560-out_height_672-out_width_912] | - | - | ✅ | 128.22 |
| test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 19.77 |
| test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 25.32 |
| test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | - | - | ✅ | 27.53 |
| test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_8192] | - | - | ✅ | 32.21 |
| test_operator[npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 1263.80 |
| test_operator[npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3235.82 |
| test_operator[npu1-RMSNorm-rows_4-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | - | - | ✅ | 29.93 |
| test_operator[npu1-RMSNorm-rows_4-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | - | - | ✅ | 29.39 |
| test_operator[npu1-RMSNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 46.83 |
| test_operator[npu1-RMSNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 44.98 |
| test_operator[npu1-ReLU-size_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 45.65 |
| test_operator[npu1-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 23.33 |
| test_operator[npu1-ReLU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 45.33 |
| test_operator[npu1-ReLU-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 19.02 |
| test_operator[npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3198.31 |
| test_operator[npu1-Resample-height_3024-width_4032-out_height_672-out_width_912] | - | - | ✅ | 50708.19 |
| test_operator[npu1-Resample-height_37-width_53-out_height_96-out_width_144] | - | - | ✅ | 314.24 |
| test_operator[npu1-Resample-height_37-width_53-out_height_96-out_width_256] | - | - | ✅ | 352.11 |
| test_operator[npu1-Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4] | - | - | ✅ | 8076.34 |
| test_operator[npu1-Resample-height_6000-width_500-out_height_672-out_width_432] | - | - | ✅ | 32650.16 |
| test_operator[npu1-ResampleTaps-in_size_1-out_size_48-num_aie_columns_2] | - | - | ✅ | 1828.57 |
| test_operator[npu1-ResampleTaps-in_size_17-out_size_1008] | - | - | ✅ | 5254.51 |
| test_operator[npu1-ResampleTaps-in_size_3024-out_size_672-words_356-slots_16] | - | - | ✅ | 12317.63 |
| test_operator[npu1-ResampleTaps-in_size_4032-out_size_912] | - | - | ✅ | 15753.50 |
| test_operator[npu1-ResampleTaps-in_size_8000-out_size_672-num_aie_columns_1-num_channels_1] | - | - | ✅ | 214174.32 |
| test_operator[npu1-ResampleTaps-in_size_961-out_size_960] | - | - | ✅ | 4048.94 |
| test_operator[npu1-RoPE-rows_32-cols_128-num_aie_columns_1-angle_rows_8-two_halves_False] | - | - | ✅ | 20.39 |
| test_operator[npu1-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | - | - | ✅ | 30.97 |
| test_operator[npu1-RoPE-rows_32-cols_512-num_aie_columns_4-angle_rows_32] | - | - | ✅ | 32.62 |
| test_operator[npu1-RoPE-rows_4096-cols_512-angle_rows_8] | - | - | ✅ | 325.12 |
| test_operator[npu1-RoPE-rows_64-cols_128-num_aie_columns_4-angle_rows_16] | - | - | ✅ | 29.07 |
| test_operator[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 23.04 |
| test_operator[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 21.63 |
| test_operator[npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096] | - | - | ✅ | 1520.16 |
| test_operator[npu1-RowwiseAdd-rows_4-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 28.64 |
| test_operator[npu1-RowwiseAdd-rows_4-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 31.94 |
| test_operator[npu1-RowwiseAdd-wide_row] | - | - | ✅ | 68.41 |
| test_operator[npu1-RowwiseAdd-wider_row] | - | - | ✅ | 46.99 |
| test_operator[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 29.98 |
| test_operator[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 20.80 |
| test_operator[npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096] | - | - | ✅ | 3222.04 |
| test_operator[npu1-RowwiseMul-rows_4-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 32.07 |
| test_operator[npu1-RowwiseMul-rows_4-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 28.65 |
| test_operator[npu1-RowwiseMul-wide_row] | - | - | ✅ | 71.77 |
| test_operator[npu1-RowwiseMul-wider_row] | - | - | ✅ | 45.51 |
| test_operator[npu1-Sample-llama] | - | - | ✅ | 331.09 |
| test_operator[npu1-Sample-padded] | - | - | ✅ | 358.36 |
| test_operator[npu1-Sample-small] | - | - | ✅ | 172.22 |
| test_operator[npu1-Sample-two_cores] | - | - | ✅ | 122.39 |
| test_operator[npu1-Sample-uneven] | - | - | ✅ | 181.43 |
| test_operator[npu1-SiLU-size_1024-num_aie_columns_4-tile_size_256] | - | - | ✅ | 28.41 |
| test_operator[npu1-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 25.80 |
| test_operator[npu1-SiLU-size_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 38.97 |
| test_operator[npu1-SiLU-size_4096-num_aie_columns_1-tile_size_4096] | - | - | ✅ | 31.82 |
| test_operator[npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3120.30 |
| test_operator[npu1-Sigmoid-size_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 46.42 |
| test_operator[npu1-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 19.85 |
| test_operator[npu1-Sigmoid-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 45.16 |
| test_operator[npu1-Sigmoid-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 25.87 |
| test_operator[npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2180.17 |
| test_operator[npu1-Softmax-f32_soft_cap_banded_addend] | - | - | ✅ | 53.19 |
| test_operator[npu1-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | - | - | ✅ | 125.96 |
| test_operator[npu1-Softmax-rows_16-cols_4608-num_aie_columns_2-num_channels_2] | - | - | ✅ | 138.16 |
| test_operator[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | - | - | ✅ | 119.73 |
| test_operator[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | - | - | ✅ | 36.71 |
| test_operator[npu1-Softmax-rows_32-cols_32768-num_aie_columns_2-num_channels_2] | - | - | ✅ | 1642.82 |
| test_operator[npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2] | - | - | ✅ | 1284.28 |
| test_operator[npu1-Tanh-size_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 45.31 |
| test_operator[npu1-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 18.62 |
| test_operator[npu1-Tanh-size_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 44.78 |
| test_operator[npu1-Tanh-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 30.60 |
| test_operator[npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3190.64 |
| test_operator[npu2-AXPY-size_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 26.34 | - | - |
| test_operator[npu2-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 14.98 | - | - |
| test_operator[npu2-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 20.14 | - | - |
| test_operator[npu2-AXPY-size_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 34.43 | - | - |
| test_operator[npu2-AXPY-size_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 16.47 | - | - |
| test_operator[npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 708.73 | - | - |
| test_operator[npu2-Clamp-size_1024-num_aie_columns_8-num_channels_2-tile_size_64-low_-0.75-high_1.25] | ✅ | 47.90 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | 18.11 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_1-tile_size_2048-low_0.5-high_1.5] | ✅ | 19.83 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_2-tile_size_1024-low_-30000.0-high_30000.0] | ✅ | 19.31 | - | - |
| test_operator[npu2-Clamp-size_2048-num_aie_columns_8-num_channels_2-tile_size_128-low_-0.75-high_1.25] | ✅ | 43.28 | - | - |
| test_operator[npu2-Clamp-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096-low_-0.75-high_1.25] | ✅ | 18.19 | - | - |
| test_operator[npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25] | ✅ | 503.96 | - | - |
| test_operator[npu2-Copy-bench_flat_4mi] | ✅ | 360.25 | - | - |
| test_operator[npu2-Copy-by_head_two_channels] | ✅ | 19.85 | - | - |
| test_operator[npu2-Copy-chunked_transfer] | ✅ | 25.75 | - | - |
| test_operator[npu2-Copy-contiguous] | ✅ | 28.11 | - | - |
| test_operator[npu2-Copy-float32] | ✅ | 22.41 | - | - |
| test_operator[npu2-Copy-past_one_memtile] | ✅ | 173.79 | - | - |
| test_operator[npu2-Copy-slot5] | ✅ | 27.31 | - | - |
| test_operator[npu2-Copy-slot5_two_channels] | ✅ | 25.88 | - | - |
| test_operator[npu2-Copy-slot_last] | ✅ | 26.77 | - | - |
| test_operator[npu2-Copy-two_channels] | ✅ | 25.78 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_32-channels_96-num_aie_columns_8] | ✅ | 25.17 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_64-channels_256-num_aie_columns_2] | ✅ | 21.42 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | 19.34 | - | - |
| test_operator[npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8] | ✅ | 70.96 | - | - |
| test_operator[npu2-ElementwiseAdd-size_1024-num_aie_columns_8-tile_size_128] | ✅ | 26.32 | - | - |
| test_operator[npu2-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | 16.27 | - | - |
| test_operator[npu2-ElementwiseAdd-size_2048-num_aie_columns_8-tile_size_256] | ✅ | 28.78 | - | - |
| test_operator[npu2-ElementwiseAdd-size_4096-num_aie_columns_1-tile_size_4096] | ✅ | 26.23 | - | - |
| test_operator[npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 706.51 | - | - |
| test_operator[npu2-ElementwiseMul-size_1024-num_aie_columns_8-tile_size_128] | ✅ | 27.34 | - | - |
| test_operator[npu2-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | 18.02 | - | - |
| test_operator[npu2-ElementwiseMul-size_2048-num_aie_columns_8-tile_size_256] | ✅ | 29.46 | - | - |
| test_operator[npu2-ElementwiseMul-size_4096-num_aie_columns_1-tile_size_4096] | ✅ | 18.09 | - | - |
| test_operator[npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 705.98 | - | - |
| test_operator[npu2-Emit-eight_carried] | ✅ | 17.08 | - | - |
| test_operator[npu2-Emit-one_carried] | ✅ | 17.88 | - | - |
| test_operator[npu2-GELU-size_1024-num_aie_columns_8-num_channels_2-tile_size_64-approximate_none] | ✅ | 45.71 | - | - |
| test_operator[npu2-GELU-size_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 46.53 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-approximate_none] | ✅ | 22.79 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 17.94 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_8-num_channels_2-tile_size_128-approximate_none] | ✅ | 48.48 | - | - |
| test_operator[npu2-GELU-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 47.04 | - | - |
| test_operator[npu2-GELU-size_8192-num_aie_columns_1-num_channels_1-tile_size_8192-approximate_none] | ✅ | 68.22 | - | - |
| test_operator[npu2-GELU-size_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 28.13 | - | - |
| test_operator[npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 534.92 | - | - |
| test_operator[npu2-GEMM-M_1024-K_2560-N_10240-num_aie_columns_8-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | 18291.70 | - | - |
| test_operator[npu2-GEMM-M_1792-K_896-N_1152-num_aie_columns_8-tile_m_64-tile_k_32-tile_n_48-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | 968.97 | - | - |
| test_operator[npu2-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | 34.74 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | ✅ | 1967.77 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | 46041.44 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-precision_medium-placement_tiles] | ✅ | 8475.70 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 27278.20 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-tile_m_8-tile_k_16-tile_n_32-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | 120494.99 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_8-tile_m_128-tile_k_32-tile_n_32-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 7249.84 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_8-tile_m_32-tile_k_32-tile_n_128-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | 6407.08 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_8-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | 6984.75 | - | - |
| test_operator[npu2-GEMM-M_2048-K_2048-N_8192-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 106944.46 | - | - |
| test_operator[npu2-GEMM-M_2048-K_64-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 1744.16 | - | - |
| test_operator[npu2-GEMM-M_2048-K_64-N_8192-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 3462.97 | - | - |
| test_operator[npu2-GEMM-M_2048-K_8192-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 106144.60 | - | - |
| test_operator[npu2-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | 231.60 | - | - |
| test_operator[npu2-GEMM-M_384-K_1536-N_1792-num_aie_columns_4-tile_m_32-tile_k_48-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest] | ✅ | 970.84 | - | - |
| test_operator[npu2-GEMM-M_896-K_1792-N_640-num_aie_columns_8-tile_m_32-tile_k_64-tile_n_80-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | 872.06 | - | - |
| test_operator[npu2-GEMM-f32_out] | ✅ | 87.91 | - | - |
| test_operator[npu2-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 317.59 | - | - |
| test_operator[npu2-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_2] | ✅ | 620.11 | - | - |
| test_operator[npu2-GEMV-M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 170.92 | - | - |
| test_operator[npu2-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 20.44 | - | - |
| test_operator[npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64] | ✅ | 684.21 | - | - |
| test_operator[npu2-GEMV-M_2048-K_64-num_aie_columns_4-tile_size_input_4-tile_size_output_256-num_channels_2-num_batches_32-repeat_4] | ✅ | 241.40 | - | - |
| test_operator[npu2-GEMV-M_2048-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_256-num_batches_32-repeat_4] | ✅ | 240.21 | - | - |
| test_operator[npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 610.05 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 95.27 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_32-num_channels_2-num_batches_8] | ✅ | 59.64 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_4] | ✅ | 56.39 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_8-repeat_4] | ✅ | 87.83 | - | - |
| test_operator[npu2-GEMV-M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 689.09 | - | - |
| test_operator[npu2-GEMV-M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 1310.26 | - | - |
| test_operator[npu2-GEMV-M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 238.29 | - | - |
| test_operator[npu2-GEMV-M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 135.10 | - | - |
| test_operator[npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 615.39 | - | - |
| test_operator[npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2] | ✅ | 458.03 | - | - |
| test_operator[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 17.77 | - | - |
| test_operator[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 19.61 | - | - |
| test_operator[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 16.26 | - | - |
| test_operator[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 20.04 | - | - |
| test_operator[npu2-LayerNorm-rows_16-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 47.16 | - | - |
| test_operator[npu2-LayerNorm-rows_16-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 44.94 | - | - |
| test_operator[npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 509.00 | - | - |
| test_operator[npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 495.36 | - | - |
| test_operator[npu2-LayerNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 26.73 | - | - |
| test_operator[npu2-LayerNorm-rows_8-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 24.93 | - | - |
| test_operator[npu2-Limbs-rows_4096-line_320-num_aie_columns_8] | ✅ | 376.48 | - | - |
| test_operator[npu2-Limbs-rows_512-line_320-num_aie_columns_4] | ✅ | 69.36 | - | - |
| test_operator[npu2-Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | 24.83 | - | - |
| test_operator[npu2-Log-size_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 46.89 | - | - |
| test_operator[npu2-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 29.74 | - | - |
| test_operator[npu2-Log-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 44.69 | - | - |
| test_operator[npu2-Log-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 45.24 | - | - |
| test_operator[npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 3419.14 | - | - |
| test_operator[npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8] | ✅ | 31950.13 | - | - |
| test_operator[npu2-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | 181.10 | - | - |
| test_operator[npu2-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | 109.14 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | ✅ | 133.81 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_8-heads_interleaved_True] | ✅ | 2948.32 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_8] | ✅ | 35839.31 | - | - |
| test_operator[npu2-MHA-num_heads_4-num_KV_heads_2-seq_len_2000-d_256-causal_False-window_512-num_pipelines_8] | ✅ | 17775.62 | - | - |
| test_operator[npu2-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | 104.44 | - | - |
| test_operator[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_1-kv_len_512-num_pipelines_2] | ✅ | 30.18 | - | - |
| test_operator[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8] | ✅ | 251131.77 | - | - |
| test_operator[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-d_128-num_pipelines_8] | ✅ | 14017.59 | - | - |
| test_operator[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8] | ✅ | 26004.14 | - | - |
| test_operator[npu2-Magnitude-rows_4096-width_640-num_aie_columns_8] | ✅ | 820.38 | - | - |
| test_operator[npu2-Magnitude-rows_512-width_640-num_aie_columns_4] | ✅ | 225.97 | - | - |
| test_operator[npu2-Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | 121.50 | - | - |
| test_operator[npu2-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))-offset_True] | ✅ | 20.24 | - | - |
| test_operator[npu2-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))] | ✅ | 21.67 | - | - |
| test_operator[npu2-Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))] | ✅ | 32.58 | - | - |
| test_operator[npu2-Merge-rows_192-placeholders_((49190, 64),)] | ✅ | 28.47 | - | - |
| test_operator[npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))-offset_True] | ✅ | 92.13 | - | - |
| test_operator[npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | ✅ | 96.29 | - | - |
| test_operator[npu2-PatchPositions-rows_2048-out_height_480-out_width_1056-cores_8] | ✅ | 65.02 | - | - |
| test_operator[npu2-PatchPositions-rows_2304-out_height_768-out_width_768] | ✅ | 75.07 | - | - |
| test_operator[npu2-PatchPositions-rows_256-out_height_48-out_width_48] | ✅ | 25.59 | - | - |
| test_operator[npu2-PatchPositions-rows_2560-out_height_672-out_width_912] | ✅ | 73.92 | - | - |
| test_operator[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 16.51 | - | - |
| test_operator[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 17.78 | - | - |
| test_operator[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 15.83 | - | - |
| test_operator[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 18.25 | - | - |
| test_operator[npu2-RMSNorm-rows_16-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 47.71 | - | - |
| test_operator[npu2-RMSNorm-rows_16-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 46.74 | - | - |
| test_operator[npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 512.81 | - | - |
| test_operator[npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 503.17 | - | - |
| test_operator[npu2-RMSNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 24.67 | - | - |
| test_operator[npu2-RMSNorm-rows_8-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 26.43 | - | - |
| test_operator[npu2-ReLU-size_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 46.48 | - | - |
| test_operator[npu2-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 20.35 | - | - |
| test_operator[npu2-ReLU-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 47.97 | - | - |
| test_operator[npu2-ReLU-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 18.63 | - | - |
| test_operator[npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 502.90 | - | - |
| test_operator[npu2-Resample-height_3024-width_4032-out_height_672-out_width_912] | ✅ | 14442.83 | - | - |
| test_operator[npu2-Resample-height_37-width_53-out_height_96-out_width_144] | ✅ | 129.43 | - | - |
| test_operator[npu2-Resample-height_37-width_53-out_height_96-out_width_256] | ✅ | 159.58 | - | - |
| test_operator[npu2-Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4] | ✅ | 4162.54 | - | - |
| test_operator[npu2-Resample-height_6000-width_500-out_height_672-out_width_432] | ✅ | 10066.38 | - | - |
| test_operator[npu2-ResampleTaps-in_size_1-out_size_48-num_aie_columns_2] | ✅ | 312.63 | - | - |
| test_operator[npu2-ResampleTaps-in_size_17-out_size_1008] | ✅ | 1558.18 | - | - |
| test_operator[npu2-ResampleTaps-in_size_3024-out_size_672-words_356-slots_16] | ✅ | 3223.69 | - | - |
| test_operator[npu2-ResampleTaps-in_size_4032-out_size_912] | ✅ | 4156.95 | - | - |
| test_operator[npu2-ResampleTaps-in_size_8000-out_size_672-num_aie_columns_1-num_channels_1] | ✅ | 116388.34 | - | - |
| test_operator[npu2-ResampleTaps-in_size_961-out_size_960] | ✅ | 1432.88 | - | - |
| test_operator[npu2-RoPE-rows_32-cols_128-num_aie_columns_1-angle_rows_8-two_halves_False] | ✅ | 17.17 | - | - |
| test_operator[npu2-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | 16.38 | - | - |
| test_operator[npu2-RoPE-rows_32-cols_512-num_aie_columns_8-angle_rows_32] | ✅ | 27.57 | - | - |
| test_operator[npu2-RoPE-rows_4096-cols_512-angle_rows_8] | ✅ | 151.18 | - | - |
| test_operator[npu2-RoPE-rows_64-cols_128-num_aie_columns_8-angle_rows_16] | ✅ | 25.06 | - | - |
| test_operator[npu2-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 19.41 | - | - |
| test_operator[npu2-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 24.14 | - | - |
| test_operator[npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | ✅ | 511.39 | - | - |
| test_operator[npu2-RowwiseAdd-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 26.65 | - | - |
| test_operator[npu2-RowwiseAdd-rows_8-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 33.64 | - | - |
| test_operator[npu2-RowwiseAdd-wide_row] | ✅ | 43.90 | - | - |
| test_operator[npu2-RowwiseAdd-wider_row] | ✅ | 28.42 | - | - |
| test_operator[npu2-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 18.13 | - | - |
| test_operator[npu2-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 25.87 | - | - |
| test_operator[npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096] | ✅ | 512.22 | - | - |
| test_operator[npu2-RowwiseMul-rows_8-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 24.51 | - | - |
| test_operator[npu2-RowwiseMul-rows_8-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 34.13 | - | - |
| test_operator[npu2-RowwiseMul-wide_row] | ✅ | 49.81 | - | - |
| test_operator[npu2-RowwiseMul-wider_row] | ✅ | 26.63 | - | - |
| test_operator[npu2-Sample-llama] | ✅ | 199.36 | - | - |
| test_operator[npu2-Sample-padded] | ✅ | 212.61 | - | - |
| test_operator[npu2-Sample-small] | ✅ | 105.96 | - | - |
| test_operator[npu2-Sample-two_cores] | ✅ | 79.35 | - | - |
| test_operator[npu2-Sample-uneven] | ✅ | 112.18 | - | - |
| test_operator[npu2-SiLU-size_1024-num_aie_columns_8-tile_size_128] | ✅ | 25.92 | - | - |
| test_operator[npu2-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | 21.50 | - | - |
| test_operator[npu2-SiLU-size_2048-num_aie_columns_8-tile_size_256] | ✅ | 26.08 | - | - |
| test_operator[npu2-SiLU-size_4096-num_aie_columns_1-tile_size_4096] | ✅ | 21.09 | - | - |
| test_operator[npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 520.34 | - | - |
| test_operator[npu2-Sigmoid-size_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 51.55 | - | - |
| test_operator[npu2-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 17.05 | - | - |
| test_operator[npu2-Sigmoid-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 52.98 | - | - |
| test_operator[npu2-Sigmoid-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 17.82 | - | - |
| test_operator[npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 502.32 | - | - |
| test_operator[npu2-Softmax-f32_soft_cap_banded_addend] | ✅ | 27.29 | - | - |
| test_operator[npu2-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | ✅ | 31.69 | - | - |
| test_operator[npu2-Softmax-rows_16-cols_4608-num_aie_columns_2-num_channels_2] | ✅ | 37.30 | - | - |
| test_operator[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | ✅ | 63.71 | - | - |
| test_operator[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | 21.89 | - | - |
| test_operator[npu2-Softmax-rows_32-cols_32768-num_aie_columns_2-num_channels_2] | ✅ | 256.47 | - | - |
| test_operator[npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2] | ✅ | 263.48 | - | - |
| test_operator[npu2-Tanh-size_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 48.33 | - | - |
| test_operator[npu2-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 17.26 | - | - |
| test_operator[npu2-Tanh-size_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 48.33 | - | - |
| test_operator[npu2-Tanh-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 19.47 | - | - |
| test_operator[npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 506.95 | - | - |
| test_operator[npu2-flm.DequantBFP-K_1024-N_1024-run_out_features_512-run_period_out_features_1024] | ✅ | 86.75 | - | - |
| test_operator[npu2-flm.DequantBFP-K_1024-N_512] | ✅ | 54.66 | - | - |
| test_operator[npu2-flm.DequantBFP-K_10240-N_2560] | ✅ | 1683.91 | - | - |
| test_operator[npu2-flm.DequantBFP-K_12288-N_1536] | ✅ | 1223.28 | - | - |
| test_operator[npu2-flm.DequantBFP-K_2560-N_10240-run_out_features_5120-run_period_out_features_10240] | ✅ | 1739.00 | - | - |
| test_operator[npu2-flm.DequantBFP-K_2560-N_10240] | ✅ | 1747.55 | - | - |
| test_operator[npu2-flm.DequantBFP-K_2560-N_2560] | ✅ | 449.19 | - | - |
| test_operator[npu2-flm.DequantBFP-K_4096-N_1536] | ✅ | 424.73 | - | - |
| test_operator[npu2-flm.DequantBFP-K_512-N_128] | ✅ | 19.76 | - | - |
| test_operator[npu2-flm.DequantBFP-K_6144-N_1536] | ✅ | 623.96 | - | - |
| test_operator[npu2-flm.LMHead-dim_1536-vocab_1024-softcap_5.0] | ✅ | -28.77 | - | - |
| test_operator[npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0] | ✅ | 3793.86 | - | - |
| test_operator[npu2-flm.LMHead-dim_1536-vocab_4096-softcap_30.0] | ✅ | -68.95 | - | - |
| test_operator[npu2-flm.LMHead-dim_2560-vocab_262144-softcap_30.0] | ✅ | 6206.24 | - | - |
| test_operator[npu2-flm.LMHead-dim_2560-vocab_4096-softcap_30.0] | ✅ | -25.93 | - | - |
| test_patch_positions_that_do_not_tile_are_refused[more_patches_than_rows] | ✅ | - | ✅ | - |
| test_patch_positions_that_do_not_tile_are_refused[not_whole_windows] | ✅ | - | ✅ | - |
| test_patch_positions_that_do_not_tile_are_refused[rows_not_whole_blocks] | ✅ | - | ✅ | - |
| test_reference_matches_device_convention_across_shapes[test_reference_matches_device_convention_across_shapes] | ✅ | - | ✅ | - |
| test_rows_a_state_names_are_gathered[n_ids_1] | ✅ | - | - | - |
| test_rows_a_state_names_are_gathered[n_ids_256] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[full_elf-llama] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[full_elf-unaligned] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[full_elf-vision] | ✅ | - | - | - |
| test_rows_are_masked_to_the_per_call_length[xclbin-llama] | ✅ | - | ✅ | - |
| test_rows_are_masked_to_the_per_call_length[xclbin-unaligned] | ✅ | - | ✅ | - |
| test_rows_are_masked_to_the_per_call_length[xclbin-vision] | ✅ | - | ✅ | - |
| test_rows_each_call_names_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_rows_each_call_names_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_rows_each_call_names_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_rows_ids_the_device_made_name_are_gathered[feeds_None-n_ids_1] | ✅ | - | - | - |
| test_rows_of_a_weight_are_gathered[test_rows_of_a_weight_are_gathered] | ✅ | - | - | - |
| test_rows_of_an_intermediate_are_gathered[test_rows_of_an_intermediate_are_gathered] | ✅ | - | - | - |
| test_rows_past_the_valid_length_are_zero[causal] | ✅ | - | - | - |
| test_rows_past_the_valid_length_are_zero[global] | ✅ | - | - | - |
| test_rows_past_the_valid_length_are_zero[sliding] | ✅ | - | - | - |
| test_sample_over_an_odd_vocab_is_refused[test_sample_over_an_odd_vocab_is_refused] | ✅ | - | ✅ | - |
| test_sample_with_more_cores_than_a_memtile_joins_is_refused[test_sample_with_more_cores_than_a_memtile_joins_is_refused] | ✅ | - | ✅ | - |
| test_softmax_with_no_column_count_that_tiles_is_refused[test_softmax_with_no_column_count_that_tiles_is_refused] | ✅ | - | ✅ | - |
| test_the_bound_rows_are_what_moves[n_1] | ✅ | - | ✅ | - |
| test_the_bound_rows_are_what_moves[n_256] | ✅ | - | ✅ | - |
| test_the_bound_rows_are_what_moves[n_40] | ✅ | - | ✅ | - |
| test_the_bound_rows_turn_on_the_device[test_the_bound_rows_turn_on_the_device] | ✅ | - | - | - |
| test_the_cache_offset_is_applied_per_call[test_the_cache_offset_is_applied_per_call] | ✅ | - | - | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_144-device_npu1] | ✅ | - | ✅ | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_144-device_npu2] | ✅ | - | ✅ | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_256-device_npu1] | ✅ | - | ✅ | - |
| test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_256-device_npu2] | ✅ | - | ✅ | - |
| test_the_offset_moves_every_piece_of_a_split_pattern[test_the_offset_moves_every_piece_of_a_split_pattern] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_accurate-full_elf] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_accurate-xclbin] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_b_col_maj-full_elf] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_b_col_maj-xclbin] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_medium-full_elf] | ✅ | - | - | - |
| test_the_reduction_stops_at_the_per_call_length[mode_medium-xclbin] | ✅ | - | - | - |
| test_the_reference_scores_a_long_cache_a_few_rows_at_a_time[test_the_reference_scores_a_long_cache_a_few_rows_at_a_time] | ✅ | - | ✅ | - |
| test_the_rows_a_call_bounds_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_by_ids_the_device_made_are_gathered[feeds_1-n_ids_512] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_by_ids_the_device_made_are_gathered[feeds_4-n_ids_71] | ✅ | - | - | - |
| test_the_rows_a_call_bounds_by_ids_the_device_made_are_gathered[feeds_None-n_ids_15] | ✅ | - | - | - |
| test_the_rows_of_a_bound_are_computed[full_elf] | ✅ | - | - | - |
| test_the_rows_of_a_bound_are_computed[xclbin] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-qwen2_down] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-qwen2_up] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-resident_b] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[full_elf-streamed_b] | ✅ | - | - | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-qwen2_down] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-qwen2_up] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-resident_b] | ✅ | - | ✅ | - |
| test_the_units_a_bound_reaches_are_computed[xclbin-streamed_b] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_a_bounded_row_is_rejected[test_transfer_size_not_dividing_a_bounded_row_is_rejected] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_the_per_channel_share_is_rejected[test_transfer_size_not_dividing_the_per_channel_share_is_rejected] | ✅ | - | ✅ | - |
| test_walks_in_turn_are_their_reference[band_stride_0] | ✅ | - | ✅ | - |
| test_walks_in_turn_are_their_reference[band_stride_1] | ✅ | - | ✅ | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_0-full_elf] | ✅ | - | - | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_0-xclbin] | ✅ | - | - | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_1-full_elf] | ✅ | - | - | - |
| test_walks_in_turn_repeat_each_per_call[band_stride_1-xclbin] | ✅ | - | - | - |
| test_what_lies_past_the_bound_does_not_reach_the_output[test_what_lies_past_the_bound_does_not_reach_the_output] | ✅ | - | - | - |

</details>

<details>
<summary>iron/tests/toolchain</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_bounded_operator_lowers[device_npu1-gemm-GEMM--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-mha-MHA--kv_valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-mha-MHA--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-relu-ReLU--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-rms_norm-RMSNorm--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-rope-RoPE--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu1-softmax-Softmax--length] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-gemm-GEMM--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-mha-MHA--kv_valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-mha-MHA--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-relu-ReLU--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-rms_norm-RMSNorm--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-rope-RoPE--valid] | ✅ | - | ✅ | - |
| test_a_bounded_operator_lowers[device_npu2-softmax-Softmax--length] | ✅ | - | ✅ | - |
| test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with[test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with] | ✅ | - | ✅ | - |
| test_a_declared_operator_compiles_to_an_xclbin_on_npu1[test_a_declared_operator_compiles_to_an_xclbin_on_npu1] | ✅ | - | ✅ | - |
| test_a_graph_called_in_a_graph_lowers[device_npu1] | ✅ | - | ✅ | - |
| test_a_graph_called_in_a_graph_lowers[device_npu2] | ✅ | - | ✅ | - |
| test_a_graph_compiles_to_one_xclbin_per_operator_chained[device_npu1] | ✅ | - | ✅ | - |
| test_a_graph_compiles_to_one_xclbin_per_operator_chained[device_npu2] | ✅ | - | ✅ | - |
| test_a_per_call_size_over_one_block_builds_at_each_step[test_a_per_call_size_over_one_block_builds_at_each_step] | ✅ | - | ✅ | - |
| test_a_scratch_arena_past_a_bank_links_as_its_banks[test_a_scratch_arena_past_a_bank_links_as_its_banks] | ✅ | - | ✅ | - |
| test_an_inline_kernel_lowers[device_npu1] | ✅ | - | ✅ | - |
| test_an_inline_kernel_lowers[device_npu2] | ✅ | - | ✅ | - |
| test_attention_over_a_128k_cache_lowers[rows_decode] | ✅ | - | ✅ | - |
| test_attention_over_a_128k_cache_lowers[rows_prompt] | ✅ | - | ✅ | - |
| test_convolutions_called_in_a_graph_lower[device_npu1] | ✅ | - | ✅ | - |
| test_convolutions_called_in_a_graph_lower[device_npu2] | ✅ | - | ✅ | - |
| test_decode_graph_builds_a_full_elf_with_its_values_in_the_table[test_decode_graph_builds_a_full_elf_with_its_values_in_the_table] | ✅ | - | ✅ | - |
| test_decode_graph_operators_lower_with_their_values[test_decode_graph_operators_lower_with_their_values] | ✅ | - | ✅ | - |
| test_each_call_softmaxes_its_columns_and_copies_them_into_its_slot[test_each_call_softmaxes_its_columns_and_copies_them_into_its_slot] | ✅ | - | - | - |
| test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions[test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions] | ✅ | - | ✅ | - |
| test_flm_gemm_lowers_and_so_does_its_configuration_module[base] | ✅ | - | ✅ | - |
| test_flm_gemm_lowers_and_so_does_its_configuration_module[n10240] | ✅ | - | ✅ | - |
| test_flm_gemm_lowers_and_so_does_its_configuration_module[tn128] | ✅ | - | ✅ | - |
| test_image_patches_called_in_a_graph_lower[device_npu1] | ✅ | - | ✅ | - |
| test_image_patches_called_in_a_graph_lower[device_npu2] | ✅ | - | ✅ | - |
| test_instructions_compile_alone_against_an_external_image[test_instructions_compile_alone_against_an_external_image] | ✅ | - | ✅ | - |
| test_its_reference_is_the_contracts[device_npu1] | ✅ | - | ✅ | - |
| test_its_reference_is_the_contracts[device_npu2] | ✅ | - | ✅ | - |
| test_llama_builds_xclbins_at_its_size_on_npu1[chunk_False-pipelines_2] | ✅ | - | ✅ | - |
| test_llama_builds_xclbins_at_its_size_on_npu1[chunk_True-pipelines_4] | ✅ | - | ✅ | - |
| test_no_scratch_buffer_crosses_a_bank[test_no_scratch_buffer_crosses_a_bank] | ✅ | - | ✅ | - |
| test_npu1_compiles_each_step_unasked[test_npu1_compiles_each_step_unasked] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-by_head_two_channels] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-contiguous] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-float32] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Copy-slot5] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Emit-one_carried] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMM-f32_out] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-PatchPositions-rows_2560-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Resample-height_3024-width_4032-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-ResampleTaps-in_size_4032-out_size_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseAdd-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-RowwiseMul-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sample-padded] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sample-small] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sample-uneven] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu1-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-by_head_two_channels] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-contiguous] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-float32] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Copy-slot5] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Emit-one_carried] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_1792-K_896-N_1152-num_aie_columns_8-tile_m_64-tile_k_32-tile_n_48-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_8-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-M_896-K_1792-N_640-num_aie_columns_8-tile_m_32-tile_k_64-tile_n_80-b_col_maj_False-c_col_maj_True-precision_highest] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMM-f32_out] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Limbs-rows_64-line_160-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_8-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Magnitude-rows_64-width_640-num_aie_columns_1] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-PatchPositions-rows_2560-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Resample-height_3024-width_4032-out_height_672-out_width_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-ResampleTaps-in_size_4032-out_size_912] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseAdd-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-RowwiseMul-wide_row] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sample-padded] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sample-small] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sample-uneven] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-SiLU-size_2048-num_aie_columns_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-flm.DequantBFP-K_512-N_128] | ✅ | - | ✅ | - |
| test_operator_lowers_to_instructions[npu2-flm.LMHead-dim_1536-vocab_4096-softcap_30.0] | ✅ | - | ✅ | - |
| test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer[test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer] | ✅ | - | ✅ | - |
| test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table[test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table] | ✅ | - | ✅ | - |
| test_prefill_graph_operators_lower_with_their_value[test_prefill_graph_operators_lower_with_their_value] | ✅ | - | ✅ | - |
| test_prefill_steps_lower_at_llama_size[down_projection_checkpoint_layout] | ✅ | - | ✅ | - |
| test_prefill_steps_lower_at_llama_size[kv_into_cache] | ✅ | - | ✅ | - |
| test_prefill_steps_lower_at_llama_size[mha_in_the_projections_layout] | ✅ | - | ✅ | - |
| test_shipped_builds_its_instructions_for_the_external_image[test_shipped_builds_its_instructions_for_the_external_image] | ✅ | - | ✅ | - |
| test_shipped_external_sequence_lowers[test_shipped_external_sequence_lowers] | ✅ | - | ✅ | - |
| test_shipped_fetches_its_image[test_shipped_fetches_its_image] | ✅ | - | ✅ | - |
| test_swiglu_graph_compiles_to_a_full_elf[test_swiglu_graph_compiles_to_a_full_elf] | ✅ | - | ✅ | - |
| test_swiglu_graphs_operators_lower[test_swiglu_graphs_operators_lower] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-elementwise_add-ElementwiseAdd--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-gemm-GEMM--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-gemv-GEMV--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-rope-RoPE--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu1-softmax-Softmax--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-elementwise_add-ElementwiseAdd--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-gemm-GEMM--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-gemv-GEMV--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-rope-RoPE--] | ✅ | - | ✅ | - |
| test_the_array_is_the_same_at_two_extents[device_npu2-softmax-Softmax--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[elementwise_add-ElementwiseAdd--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[gemm-GEMM--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[gemv-GEMV--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[rope-RoPE--] | ✅ | - | ✅ | - |
| test_the_extents_share_one_device[softmax-Softmax--] | ✅ | - | ✅ | - |
| test_values_become_dispatch_time_kernels_at_each_step[device_npu1] | ✅ | - | ✅ | - |
| test_values_become_dispatch_time_kernels_at_each_step[device_npu2] | ✅ | - | ✅ | - |

</details>

## Examples

<details>
<summary>tests/applications/decoders</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_generation[gemma4-short-1] | ✅ | - | - | - |

</details>

<details>
<summary>tests/applications/embedding_gemma2</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_embeddinggemma_2_accuracy[document] | ✅ | - | ✅ | - |
| test_embeddinggemma_2_accuracy[long_document] | ✅ | - | ✅ | - |
| test_embeddinggemma_2_accuracy[near_the_limit] | ✅ | - | ✅ | - |
| test_embeddinggemma_2_accuracy[past_the_window] | ✅ | - | ✅ | - |
| test_embeddinggemma_2_accuracy[query] | ✅ | - | ✅ | - |
| test_image_processor_refuses[shape_(1, 5000)-tokens_280-refusal_patch columns] | ✅ | - | ✅ | - |
| test_image_processor_refuses[shape_(5000, 4000)-tokens_280-refusal_does not fit] | ✅ | - | ✅ | - |
| test_image_processor_refuses[shape_(97, 2003)-tokens_280-refusal_patch columns] | ✅ | - | ✅ | - |
| test_image_processor_refuses_on_npu1[test_image_processor_refuses_on_npu1] | ✅ | - | ✅ | - |
| test_vision_window_positions_are_each_patch_rows[hk_1-wk_1] | ✅ | - | ✅ | - |
| test_vision_window_positions_are_each_patch_rows[hk_14-wk_19] | ✅ | - | ✅ | - |
| test_vision_window_positions_are_each_patch_rows[hk_16-wk_16] | ✅ | - | ✅ | - |
| test_vision_window_positions_are_each_patch_rows[hk_200-wk_1] | ✅ | - | ✅ | - |
| test_vision_window_positions_are_each_patch_rows[hk_6-wk_42] | ✅ | - | ✅ | - |
| test_vision_window_positions_are_each_patch_rows[hk_65-wk_4] | ✅ | - | ✅ | - |
| test_vision_window_positions_are_each_patch_rows[hk_8-wk_35] | ✅ | - | ✅ | - |

</details>

<details>
<summary>tests/applications/gemma4/reference</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| TestGemma4::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks] | ✅ | - | ✅ | - |
| TestGemma4::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token] | ✅ | - | ✅ | - |
| TestGemma4::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves] | ✅ | - | ✅ | - |
| TestGemma4::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference] | ✅ | - | ✅ | - |
| TestGemma4::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic] | ✅ | - | ✅ | - |
| TestGemma4::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches] | ✅ | - | ✅ | - |
| test_a_placeholder_s_per_layer_inputs_are_the_padding_token_s[test_a_placeholder_s_per_layer_inputs_are_the_padding_token_s] | ✅ | - | ✅ | - |
| test_a_shared_layer_with_no_earlier_layer_of_its_kind_is_refused[test_a_shared_layer_with_no_earlier_layer_of_its_kind_is_refused] | ✅ | - | ✅ | - |
| test_bidirectional_attention_for_images_alone_is_text_s_causal[test_bidirectional_attention_for_images_alone_is_text_s_causal] | ✅ | - | ✅ | - |
| test_what_is_not_built_is_refused[text_{'attention_k_eq_v': True}] | ✅ | - | ✅ | - |
| test_what_is_not_built_is_refused[text_{'attn_logit_softcapping': 50.0}] | ✅ | - | ✅ | - |
| test_what_is_not_built_is_refused[text_{'enable_moe_block': True}] | ✅ | - | ✅ | - |
| test_what_is_not_built_is_refused[text_{'rope_parameters': {'full_attention': {'rope_type': 'default'}}}] | ✅ | - | ✅ | - |
| test_what_is_not_built_is_refused[text_{'use_bidirectional_attention': 'all'}] | ✅ | - | ✅ | - |
| test_what_is_not_built_is_refused[text_{'use_bidirectional_attention': True}] | ✅ | - | ✅ | - |
| test_what_is_not_built_is_refused[text_{'vocab_size_per_layer_input': 512}] | ✅ | - | ✅ | - |

</details>

<details>
<summary>tests/applications/llama</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_llama_3_2[llama_3.2_1b-prompt_13_tokens_1] | ✅ | - | - | - |
| test_llama_3_2[llama_3.2_3b-prompt_13_tokens_1] | ✅ | - | - | - |

</details>

<details>
<summary>tests/applications/llama/reference</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| TestBiasedLlama::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks] | ✅ | - | ✅ | - |
| TestBiasedLlama::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token] | ✅ | - | ✅ | - |
| TestBiasedLlama::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves] | ✅ | - | ✅ | - |
| TestBiasedLlama::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference] | ✅ | - | ✅ | - |
| TestBiasedLlama::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic] | ✅ | - | ✅ | - |
| TestBiasedLlama::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches] | ✅ | - | ✅ | - |

</details>

<details>
<summary>tests/applications/long_context</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_every_decoder_application_is_held_to_its_context[test_every_decoder_application_is_held_to_its_context] | ✅ | - | ✅ | - |
| test_nothing_grows_with_the_context[application_gemma4_e2b-version_decode] | ✅ | - | ✅ | - |
| test_nothing_grows_with_the_context[application_gemma4_e2b-version_prompt] | ✅ | - | ✅ | - |
| test_nothing_grows_with_the_context[application_llama_3.2_1b-version_decode] | ✅ | - | ✅ | - |
| test_nothing_grows_with_the_context[application_llama_3.2_1b-version_prompt] | ✅ | - | ✅ | - |
| test_nothing_grows_with_the_context[application_llama_3.2_3b-version_decode] | ✅ | - | ✅ | - |
| test_nothing_grows_with_the_context[application_llama_3.2_3b-version_prompt] | ✅ | - | ✅ | - |

</details>

