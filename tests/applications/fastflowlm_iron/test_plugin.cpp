// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: MIT
#include "AutoModel/model_extension.h"
#include "test_support.hpp"

#include <cstring>
#include <string>

namespace
{
flm_backend_create_v1 causal = nullptr;
flm_embedding_create_v1 embedding = nullptr;
flm_span_v1 Span(const char *s)
{
    return {s, std::strlen(s)};
}
int Backend(void *,
            const char *family,
            const char *backend,
            const char *provider,
            const flm_backend_traits_v1 *,
            flm_backend_create_v1 create,
            void *)
{
    TEST_REQUIRE(std::string(family) == "llama3");
    TEST_REQUIRE(std::string(backend) == "iron" && std::string(provider) == "iron");
    causal = create;
    return 0;
}
int Embedding(void *, const char *, const char *, flm_embedding_create_v1 create, void *)
{
    embedding = create;
    return 0;
}
void test_plugin()
{
    const auto *plugin = flm_model_extension_query_v1();
    flm_model_extension_registrar_v1 host{};
    host.struct_size = FLM_MODEL_EXTENSION_REGISTRAR_V1_MIN_SIZE;
    TEST_REQUIRE(plugin->register_extension(&host, nullptr) == FLM_MODEL_EXTENSION_STATUS_UNSUPPORTED);
    host.struct_size = sizeof(host);
    host.register_backend_provider = Backend;
    host.register_embedding_provider = Embedding;
    TEST_REQUIRE(plugin->register_extension(&host, nullptr) == 0);
    flm_backend_create_context_v1 context{};
    context.struct_size = sizeof(context);
    context.model_path = Span("/unused");
    context.model_info_json = Span("{\"iron_model\":\"llama\"}");
    context.context_length = 32;
    flm_backend_instance_v1 lm{};
    lm.struct_size = sizeof(lm);
    TEST_REQUIRE(causal(nullptr, &context, &lm, nullptr) == 0);
    const auto *api = lm.causal_lm;
    flm_bf16_view_v1 out{};
    const int32_t tokens[] = {4, 10};
    TEST_REQUIRE(api->prefill(lm.object, tokens, 2, nullptr, &out, nullptr) == 0);
    TEST_REQUIRE(out.size == 2 && out.data[0] == 10 && out.data[1] == 2);
    const auto *state =
        static_cast<const flm_backend_state_v1 *>(lm.query_capability(lm.object, FLM_BACKEND_CAPABILITY_STATE, 1));
    TEST_REQUIRE(state);
    int32_t length = 0;
    TEST_REQUIRE(state->checkpoint(lm.object, &length, nullptr) == 0 && length == 2);
    TEST_REQUIRE(api->forward(lm.object, 26, &out, nullptr) == 0);
    TEST_REQUIRE(state->restore(lm.object, &length, nullptr) == 0 && length == 2);
    TEST_REQUIRE(api->forward(lm.object, 7, &out, nullptr) == 0);
    TEST_REQUIRE(out.data[0] == 7 && out.data[1] == 3);
    TEST_REQUIRE(api->set_context_length(lm.object, 1, nullptr) == 0);
    TEST_REQUIRE(api->forward(lm.object, 8, &out, nullptr) == 0 && out.data[1] == 2);
    TEST_REQUIRE(api->update_max_length(lm.object, 33, nullptr) != 0);
    TEST_REQUIRE(api->set_context_length(lm.object, 5, nullptr) != 0);
    TEST_REQUIRE(api->clear_context(lm.object, nullptr) == 0);
    TEST_REQUIRE(api->get_current_context_length(lm.object, &length, nullptr) == 0 && length == 0);
    lm.destroy(lm.object);
    flm_embedding_model_v1 emb{};
    emb.struct_size = sizeof(emb);
    TEST_REQUIRE(embedding(nullptr, nullptr, &emb, nullptr) == 0);
    const auto metadata = Span("{\"iron_model\":\"embedding_gemma2\"}");
    TEST_REQUIRE(emb.load(emb.object, Span("/unused"), metadata, 1, nullptr) != 0);
    TEST_REQUIRE(emb.load(emb.object, Span("/unused"), metadata, 0, nullptr) == 0);
    flm_embedding_result_v1 vector{};
    vector.struct_size = sizeof(vector);
    TEST_REQUIRE(emb.embed(emb.object, Span(R"({"input":"hello","task":"unknown"})"), nullptr, &vector, nullptr) ==
                 FLM_MODEL_EXTENSION_STATUS_INVALID_ARGUMENT);
    TEST_REQUIRE(emb.embed(emb.object, Span(R"({"input":"hello"})"), nullptr, &vector, nullptr) == 0);
    TEST_REQUIRE(vector.size == 2 && vector.data[0] == 5 && vector.data[1] == 768);
    TEST_REQUIRE(emb.embed(emb.object,
                           Span(R"({"input":"hello","task":"document","title":"France","dimensions":128})"),
                           nullptr,
                           &vector,
                           nullptr) == 0);
    TEST_REQUIRE(vector.data[1] == 128 && vector.prompt_tokens == 9);
    const flm_cancellation_v1 cancelled{nullptr, [](void *) { return 1; }};
    TEST_REQUIRE(emb.embed(emb.object, Span("{}"), &cancelled, &vector, nullptr) ==
                 FLM_MODEL_EXTENSION_STATUS_CANCELLED);
    emb.destroy(emb.object);
}
} // namespace
int main()
{
    test_plugin();
}
