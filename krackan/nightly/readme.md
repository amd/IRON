
# IRON

Tested on `2026_10_30_11_15_59` at commit `ce440fa`.

<details>
<summary>tests/applications/decoders</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_accuracy[gemma4]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_accuracy_across_chunks[gemma4]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_chat_turn[gemma4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_determinism[gemma4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_generation[gemma4-long-40]</td><td>✅ 1/1</td><td>5.85</td><td>5.60</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_generation[gemma4-short-1]</td><td>✅ 1/1</td><td>5.45</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/embedding_gemma2</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestAudio::test_audio_accuracy[name_extended]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_accuracy[name_long]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_accuracy[name_medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_accuracy[name_passage]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_accuracy[name_short]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_features[name_extended]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_features[name_long]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_features[name_medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_features[name_passage]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_features[name_short]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_latency[name_extended]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>356863.00</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_latency[name_long]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>422999.02</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_latency[name_medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>300279.52</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_latency[name_passage]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>347365.12</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestAudio::test_audio_latency[name_short]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>291359.97</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_embeddinggemma_2_each_step_accuracy[past_the_window]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_embeddinggemma_2_each_step_accuracy[query]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_embeddinggemma_2_each_step_multimodal[test_embeddinggemma_2_each_step_multimodal]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(1080, 1920)-tokens_140]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>12908.30</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(17, 23)-tokens_140]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>7678.73</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(2003, 97)-tokens_140]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>12327.22</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(3024, 4032)-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>28186.40</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(333, 517)-tokens_140]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>8273.37</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(4032, 3024)-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>29091.45</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(4096, 3072)-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>29398.83</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(480, 640)-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>9628.28</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(672, 517)-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>10142.69</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_(672, 960)-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>11117.69</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_cats-shape_None-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>10015.52</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_living_room-shape_None-tokens_140]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>9322.55</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor[name_stop_sign-shape_None-tokens_280]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>9773.47</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_image_processor_npu2_only[test_image_processor_npu2_only]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>10019.85</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_vision_accuracy[name_cats]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_vision_accuracy[name_living_room]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_vision_accuracy[name_stop_sign]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_vision_latency[name_cats]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>716384.36</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestVision::test_vision_latency[name_living_room]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>411138.44</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_accuracy[document]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_accuracy[long_document]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_accuracy[near_the_limit]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_accuracy[past_the_window]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_accuracy[query]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_determinism[test_embeddinggemma_2_determinism]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_latency[long_document]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>340206.27</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_latency[past_the_window]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>544537.44</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_latency[query]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>285907.89</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_multimodal[case_audio]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_multimodal[case_both]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_multimodal[case_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_multimodal[case_long_clip_and_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_ranking[test_embeddinggemma_2_ranking]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_truncation[dims_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_truncation[dims_256]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_truncation[dims_512]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_image_processor_refuses[shape_(1, 5000)-tokens_280-refusal_patch columns]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_image_processor_refuses[shape_(5000, 4000)-tokens_280-refusal_does not fit]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_image_processor_refuses[shape_(97, 2003)-tokens_280-refusal_patch columns]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_image_processor_refuses_on_npu1[test_image_processor_refuses_on_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vision_window_positions_are_each_patch_rows[hk_1-wk_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vision_window_positions_are_each_patch_rows[hk_14-wk_19]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vision_window_positions_are_each_patch_rows[hk_16-wk_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vision_window_positions_are_each_patch_rows[hk_200-wk_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vision_window_positions_are_each_patch_rows[hk_6-wk_42]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vision_window_positions_are_each_patch_rows[hk_65-wk_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vision_window_positions_are_each_patch_rows[hk_8-wk_35]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/gemma4</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemma4_multimodal_accuracy[case_both]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.01</td><td>0.00</td></tr>
        <tr><td>test_gemma4_multimodal_accuracy[case_cats]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.01</td><td>1.00</td></tr>
        <tr><td>test_gemma4_multimodal_accuracy[case_medium_clip]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.00</td><td>0.00</td></tr>
        <tr><td>test_gemma4_multimodal_accuracy[case_short_clip]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.01</td><td>0.00</td></tr>
        <tr><td>test_gemma4_multimodal_accuracy[case_stop_sign]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.04</td><td>0.00</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/gemma4/reference</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestGemma4::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGemma4::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGemma4::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGemma4::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGemma4::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGemma4::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_placeholder_s_per_layer_inputs_are_the_padding_token_s[test_a_placeholder_s_per_layer_inputs_are_the_padding_token_s]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_shared_layer_with_no_earlier_layer_of_its_kind_is_refused[test_a_shared_layer_with_no_earlier_layer_of_its_kind_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_bidirectional_attention_for_images_alone_is_text_s_causal[test_bidirectional_attention_for_images_alone_is_text_s_causal]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_is_not_built_is_refused[text_{'attention_k_eq_v': True}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_is_not_built_is_refused[text_{'attn_logit_softcapping': 50.0}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_is_not_built_is_refused[text_{'enable_moe_block': True}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_is_not_built_is_refused[text_{'rope_parameters': {'full_attention': {'rope_type': 'default'}}}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_is_not_built_is_refused[text_{'use_bidirectional_attention': 'all'}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_is_not_built_is_refused[text_{'use_bidirectional_attention': True}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_is_not_built_is_refused[text_{'vocab_size_per_layer_input': 512}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/gemma4_flm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_iron_engine_reload_rebuilds_override_state[test_iron_engine_reload_rebuilds_override_state]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_iron_matches_engine[prompt_long_prompt]</td><td>✅ 1/1</td><td>2.24</td><td>27.90</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_iron_matches_engine[prompt_word_problem]</td><td>✅ 1/1</td><td>0.63</td><td>28.45</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/granite</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestEachStep::test_granite_4_2_3b_each_step[granite_4_2_3b_prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>2.86</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_2_3b_each_step[granite_4_2_3b_prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>2.88</td><td>2.24</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_2_3b_each_step[granite_4_2_3b_prompt_13_tokens_1]</td><td>✅ 1/1</td><td>1.97</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_2_3b_each_step[granite_4_2_3b_prompt_13_tokens_40]</td><td>✅ 1/1</td><td>1.91</td><td>2.26</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_2_3b_each_step_accuracy[test_granite_4_2_3b_each_step_accuracy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.01</td><td>1.00</td></tr>
        <tr><td>TestEachStep::test_granite_4_2_3b_each_step_determinism[test_granite_4_2_3b_each_step_determinism]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b[granite_4_2_3b_prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>1.76</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b[granite_4_2_3b_prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>2.01</td><td>5.60</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b[granite_4_2_3b_prompt_13_tokens_1]</td><td>✅ 1/1</td><td>1.15</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b[granite_4_2_3b_prompt_13_tokens_40]</td><td>✅ 1/1</td><td>1.15</td><td>5.61</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b_accuracy[test_granite_4_2_3b_accuracy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.00</td><td>0.00</td></tr>
        <tr><td>test_granite_4_2_3b_accuracy_across_chunks[test_granite_4_2_3b_accuracy_across_chunks]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b_chat_turn[test_granite_4_2_3b_chat_turn]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b_determinism[test_granite_4_2_3b_determinism]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_2_3b_device_loop[test_granite_4_2_3b_device_loop]</td><td>✅ 1/1</td><td>1.75</td><td>5.59</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/granite/reference</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestGranite::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGranite::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGranite::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGranite::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGranite::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGranite::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/granite_hybrid</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestEachStep::test_granite_4_0_h_1b_each_step[granite_4_0_h_1b_prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>5.35</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_0_h_1b_each_step[granite_4_0_h_1b_prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>5.28</td><td>1.89</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_0_h_1b_each_step[granite_4_0_h_1b_prompt_13_tokens_1]</td><td>✅ 1/1</td><td>4.35</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_0_h_1b_each_step[granite_4_0_h_1b_prompt_13_tokens_40]</td><td>✅ 1/1</td><td>4.26</td><td>1.86</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_granite_4_0_h_1b_each_step_accuracy[test_granite_4_0_h_1b_each_step_accuracy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.00</td><td>2.00</td></tr>
        <tr><td>TestEachStep::test_granite_4_0_h_1b_each_step_determinism[test_granite_4_0_h_1b_each_step_determinism]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_0_h_1b[granite_4_0_h_1b_prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>3.90</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_0_h_1b[granite_4_0_h_1b_prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>4.12</td><td>6.01</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_0_h_1b[granite_4_0_h_1b_prompt_13_tokens_1]</td><td>✅ 1/1</td><td>2.97</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_0_h_1b[granite_4_0_h_1b_prompt_13_tokens_40]</td><td>✅ 1/1</td><td>2.97</td><td>6.02</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_0_h_1b_accuracy[test_granite_4_0_h_1b_accuracy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.01</td><td>2.00</td></tr>
        <tr><td>test_granite_4_0_h_1b_accuracy_across_chunks[test_granite_4_0_h_1b_accuracy_across_chunks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.00</td><td>0.00</td></tr>
        <tr><td>test_granite_4_0_h_1b_chat_turn[test_granite_4_0_h_1b_chat_turn]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_0_h_1b_determinism[test_granite_4_0_h_1b_determinism]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_granite_4_0_h_1b_rate_counts_the_draws_past_eos[test_granite_4_0_h_1b_rate_counts_the_draws_past_eos]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/granite_hybrid/reference</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestGraniteHybridDense::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_forget_restarts_from_a_valid_recurrent_state[position_0-start_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_forget_restarts_from_a_valid_recurrent_state[position_100-start_100]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_forget_restarts_from_a_valid_recurrent_state[position_64-start_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_forget_restarts_from_a_valid_recurrent_state[position_70-start_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestGraniteHybridDense::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_config_with_experts_is_refused[test_a_config_with_experts_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_config_without_rope_reads_back_from_its_json[test_a_config_without_rope_reads_back_from_its_json]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_rope_config_without_rope_theta_takes_transformers_default[test_a_rope_config_without_rope_theta_takes_transformers_default]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_layer_types_short_of_the_layers_are_refused[test_layer_types_short_of_the_layers_are_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_model_cli_help[test_model_cli_help]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/llama</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_1b-prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>0.57</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_1b-prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>0.72</td><td>5.42</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_1b-prompt_13_tokens_1]</td><td>✅ 1/1</td><td>0.53</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_1b-prompt_13_tokens_40]</td><td>✅ 1/1</td><td>0.53</td><td>5.36</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_3b-prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>2.23</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_3b-prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>2.43</td><td>2.75</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_3b-prompt_13_tokens_1]</td><td>✅ 1/1</td><td>1.27</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step[llama_3.2_3b-prompt_13_tokens_40]</td><td>✅ 1/1</td><td>1.22</td><td>2.76</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step_accuracy[llama_3.2_1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.01</td><td>1.00</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step_accuracy[llama_3.2_3b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.04</td><td>0.00</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step_determinism[llama_3.2_1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step_determinism[llama_3.2_3b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step_sampling[llama_3.2_1b]</td><td>✅ 1/1</td><td>0.52</td><td>5.37</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestEachStep::test_llama_3_2_each_step_sampling[llama_3.2_3b]</td><td>✅ 1/1</td><td>1.20</td><td>2.76</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_1b-prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>0.28</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_1b-prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>0.46</td><td>14.54</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_1b-prompt_13_tokens_1]</td><td>✅ 1/1</td><td>0.24</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_1b-prompt_13_tokens_40]</td><td>✅ 1/1</td><td>0.24</td><td>14.65</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_3b-prompt_1024_tokens_1]</td><td>✅ 1/1</td><td>1.34</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_3b-prompt_1024_tokens_40]</td><td>✅ 1/1</td><td>1.56</td><td>6.35</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_3b-prompt_13_tokens_1]</td><td>✅ 1/1</td><td>0.72</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2[llama_3.2_3b-prompt_13_tokens_40]</td><td>✅ 1/1</td><td>0.72</td><td>6.41</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_accuracy[llama_3.2_1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.00</td><td>2.00</td></tr>
        <tr><td>test_llama_3_2_accuracy[llama_3.2_3b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.04</td><td>1.00</td></tr>
        <tr><td>test_llama_3_2_accuracy_across_chunks[llama_3.2_1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.00</td><td>0.00</td></tr>
        <tr><td>test_llama_3_2_accuracy_across_chunks[llama_3.2_3b]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_chat_turn[llama_3.2_1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_chat_turn[llama_3.2_3b]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_determinism[llama_3.2_1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_determinism[llama_3.2_3b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_device_loop[llama_3.2_1b]</td><td>✅ 1/1</td><td>0.28</td><td>14.53</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_device_loop[llama_3.2_3b]</td><td>✅ 1/1</td><td>1.33</td><td>6.35</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_readme_quick_start[test_the_readme_quick_start]</td><td>✅ 1/1</td><td>0.44</td><td>14.55</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/llama/reference</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestBiasedLlama::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestBiasedLlama::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestBiasedLlama::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestBiasedLlama::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestBiasedLlama::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestBiasedLlama::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>tests/applications/long_context</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td><td>Latency (mean)</td><td>MaxKL (mean)</td><td>Top1Mismatches (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_decode_deep_in_the_cache[llama_3.2_1b-16384]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_decode_deep_in_the_cache[llama_3.2_1b-32768]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_decode_deep_in_the_cache[llama_3.2_1b-4096]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_decode_deep_in_the_cache[llama_3.2_1b-65536]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_decode_deep_in_the_cache[llama_3.2_1b-whole]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_decoder_application_is_held_to_its_context[test_every_decoder_application_is_held_to_its_context]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_gemma4_e2b-version_decode]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_gemma4_e2b-version_prompt]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_granite_4.0_h_1b-version_decode]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_granite_4.0_h_1b-version_prompt]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_granite_4.2_3b-version_decode]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_granite_4.2_3b-version_prompt]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_llama_3.2_1b-version_decode]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_llama_3.2_1b-version_prompt]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_llama_3.2_3b-version_decode]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_nothing_grows_with_the_context[application_llama_3.2_3b-version_prompt]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_deep_in_the_cache[llama_3.2_1b-16384]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_deep_in_the_cache[llama_3.2_1b-32768]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_deep_in_the_cache[llama_3.2_1b-4096]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_deep_in_the_cache[llama_3.2_1b-65536]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_time_at_8k[llama_3.2_1b-16384]</td><td>✅ 1/1</td><td>5.28</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_time_at_8k[llama_3.2_1b-32768]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_time_at_8k[llama_3.2_1b-65536]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_time_at_the_whole_context[llama_3.2_1b-16384]</td><td>✅ 1/1</td><td>17.10</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_time_at_the_whole_context[llama_3.2_1b-32768]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_time_at_the_whole_context[llama_3.2_1b-4096]</td><td>✅ 1/1</td><td>1.97</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_time_at_the_whole_context[llama_3.2_1b-65536]</td><td>❌ 0/1</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

