// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: MIT

#include "AutoModel/model_extension.h"

#include "worker.hpp"

#include <algorithm>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

namespace
{
using flm::iron::Worker;
std::string Text(flm_span_v1 s)
{
    return s.size ? std::string(static_cast<const char *>(s.data), s.size) : std::string();
}
template <class F> int Guard(const flm_error_sink_v1 *error, F action) noexcept
{
    try {
        action();
        return FLM_MODEL_EXTENSION_STATUS_OK;
    } catch (const std::exception &e) {
        if (error && error->set_error)
            error->set_error(error->context, e.what(), std::char_traits<char>::length(e.what()));
        if (dynamic_cast<const std::invalid_argument *>(&e))
            return FLM_MODEL_EXTENSION_STATUS_INVALID_ARGUMENT;
    } catch (...) {
        if (error && error->set_error)
            error->set_error(error->context, "IRON provider failed", 20);
    }
    return FLM_MODEL_EXTENSION_STATUS_ERROR;
}
struct Model {
    std::unique_ptr<Worker> worker;
    std::vector<int> tokens, saved;
    std::vector<uint16_t> logits;
    std::vector<float> embedding;
    uint32_t capacity = 0, limit = 0;
    void Run(flm_bf16_view_v1 *out)
    {
        if (tokens.empty() || tokens.size() > limit)
            throw std::out_of_range("IRON token history exceeds context length");
        logits = worker->logits(tokens);
        *out = {logits.data(), logits.size()};
    }
};
Model &Get(void *object)
{
    return *static_cast<Model *>(object);
}
void Destroy(void *object)
{
    delete static_cast<Model *>(object);
}
int Forward(void *object, int32_t token, flm_bf16_view_v1 *out, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        auto &m = Get(object);
        m.tokens.push_back(token);
        m.Run(out);
    });
}
int Prefill(void *object,
            const int32_t *tokens,
            size_t count,
            const flm_prefill_payload_v1 *payload,
            flm_bf16_view_v1 *out,
            const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        if (payload)
            throw std::invalid_argument("IRON extension currently accepts text only");
        auto &m = Get(object);
        if (count)
            m.tokens.insert(m.tokens.end(), tokens, tokens + count);
        m.Run(out);
    });
}
int SetLength(void *object, int32_t length, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        auto &m = Get(object);
        if (length < 0 || static_cast<size_t>(length) > m.tokens.size())
            throw std::out_of_range("Invalid IRON context length");
        m.tokens.resize(length);
    });
}
int SetMaximum(void *object, uint32_t length, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        auto &m = Get(object);
        if (!length || length > m.capacity || length < m.tokens.size())
            throw std::out_of_range("Cannot grow the compiled IRON context");
        m.limit = length;
    });
}
int Clear(void *object, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        auto &m = Get(object);
        m.worker->reset();
        m.tokens.clear();
        m.saved.clear();
    });
}
int Length(void *object, int32_t *length, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] { *length = Get(object).tokens.size(); });
}
int Checkpoint(void *object, int32_t *length, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        auto &m = Get(object);
        m.saved = m.tokens;
        *length = m.saved.size();
    });
}
int Restore(void *object, int32_t *length, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        auto &m = Get(object);
        // Rebuild the saved history on the next logits call. No KV cache copying.
        m.worker->reset();
        m.tokens = m.saved;
        *length = m.tokens.size();
    });
}
int Poisoned(void *object)
{
    return Get(object).worker->poisoned();
}
const void *Capability(void *, uint32_t id, uint32_t version)
{
    static const flm_backend_state_v1 state{sizeof(state), Checkpoint, Restore};
    static const flm_backend_health_v1 health{sizeof(health), Poisoned};
    if (version != 1)
        return nullptr;
    if (id == FLM_BACKEND_CAPABILITY_STATE)
        return &state;
    if (id == FLM_BACKEND_CAPABILITY_HEALTH)
        return &health;
    return nullptr;
}
int CreateCausal(void *,
                 const flm_backend_create_context_v1 *context,
                 flm_backend_instance_v1 *instance,
                 const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        if (instance->struct_size < FLM_BACKEND_INSTANCE_V1_QUERY_CAPABILITY_SIZE || context->enable_preemption ||
            !context->context_length)
            throw std::invalid_argument("IRON requires a positive context and no preemption");
        auto m = std::make_unique<Model>();
        m->capacity = m->limit = context->context_length;
        const auto info = nlohmann::json::parse(Text(context->model_info_json));
        m->worker =
            std::make_unique<Worker>(Text(context->model_path), info.at("iron_model").get<std::string>(), m->capacity);
        static const flm_causal_lm_v1 api{sizeof(api), Forward, Prefill, SetLength, SetMaximum, Clear, Length};
        *instance = {sizeof(*instance), m.release(), Destroy, &api, {"IRON server", 11}, Capability};
    });
}
int LoadEmbedding(void *object, const flm_embedding_load_context_v1 *context, const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        if (!context || context->struct_size < FLM_EMBEDDING_LOAD_CONTEXT_V1_MIN_SIZE)
            throw std::invalid_argument("IRON embedding load context is incomplete");
        if (context->enable_preemption)
            throw std::invalid_argument("IRON embeddings do not support preemption");
        auto &m = Get(object);
        const auto info = nlohmann::json::parse(Text(context->model_info_json));
        m.worker.reset();
        m.worker = std::make_unique<Worker>(Text(context->model_path), info.at("iron_model").get<std::string>());
        if (!m.worker->supports(flm::iron::Capability::EmbeddingRequests))
            throw std::runtime_error("IRON server lacks JSON embedding requests; update IRON");
    });
}
int Embed(void *object,
          flm_span_v1 request,
          const flm_cancellation_v1 *cancellation,
          flm_embedding_result_v1 *out,
          const flm_error_sink_v1 *error)
{
    if (out->struct_size < FLM_EMBEDDING_RESULT_V1_MIN_SIZE)
        return FLM_MODEL_EXTENSION_STATUS_UNSUPPORTED;
    if (cancellation && cancellation->is_cancelled(cancellation->context))
        return FLM_MODEL_EXTENSION_STATUS_CANCELLED;
    return Guard(error, [&] {
        auto &m = Get(object);
        if (!m.worker)
            throw std::runtime_error("IRON embedding model is not loaded");
        uint64_t prompt_tokens = 0;
        m.embedding = m.worker->embed_request(nlohmann::json::parse(Text(request)), prompt_tokens);
        *out = {sizeof(*out), m.embedding.data(), m.embedding.size(), prompt_tokens};
    });
}
int CreateEmbedding(void *,
                    const flm_frontend_create_context_v1 *,
                    flm_embedding_model_v1 *instance,
                    const flm_error_sink_v1 *error)
{
    return Guard(error, [&] {
        if (instance->struct_size < FLM_EMBEDDING_MODEL_V1_MIN_SIZE)
            throw std::invalid_argument("IRON embedding ABI is unavailable");
        *instance = {sizeof(*instance), new Model, Destroy, LoadEmbedding, Embed};
    });
}
int Register(const flm_model_extension_registrar_v1 *host, const flm_error_sink_v1 *)
{
    if (host->struct_size < FLM_MODEL_EXTENSION_REGISTRAR_V1_EMBEDDING_SIZE)
        return FLM_MODEL_EXTENSION_STATUS_UNSUPPORTED;
    const flm_backend_traits_v1 traits{sizeof(traits), 0, 0, 0, 0, 0, nullptr, 0};
    int result =
        host->register_backend_provider(host->host_context, "llama3", "iron", "iron", &traits, CreateCausal, nullptr);
    if (result)
        return result;
    return host->register_embedding_provider(host->host_context, "embeddinggemma-2", "iron", CreateEmbedding, nullptr);
}
} // namespace

extern "C" FLM_MODEL_EXTENSION_EXPORT const flm_model_extension_v1 *flm_model_extension_query_v1()
{
    static const flm_model_extension_v1 extension{sizeof(extension),
                                                  FLM_MODEL_EXTENSION_ABI_V1,
#ifdef FLM_USE_HRX
                                                  FLM_MODEL_EXTENSION_NPU_RUNTIME_HRX,
#else
                                                  FLM_MODEL_EXTENSION_NPU_RUNTIME_XRT,
#endif
                                                  "iron",
                                                  "1",
                                                  Register};
    return &extension;
}
