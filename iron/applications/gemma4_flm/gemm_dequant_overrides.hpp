// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#ifndef GEMMA4_FLM_GEMM_DEQUANT_OVERRIDES_HPP
#define GEMMA4_FLM_GEMM_DEQUANT_OVERRIDES_HPP

#include "modules/gemm.hpp"
#include "npu_utils/npu_utils.hpp"
#include "tensor_utils/safe_tensors.hpp"
#include "utils/utils.hpp"

#include <array>
#include <cstdint>
#include <fstream>
#include <map>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

namespace iron
{

// Common state and helper functions

enum role : size_t { Q, K, V, O, GATE, UP, DOWN, ROLE_COUNT };

inline constexpr std::array<const char *, ROLE_COUNT> role_names = {
    "self_attn.q_proj",
    "self_attn.k_proj",
    "self_attn.v_proj",
    "self_attn.o_proj",
    "mlp.gate_proj",
    "mlp.up_proj",
    "mlp.down_proj",
};

inline void require(bool ok, const std::string &what)
{
    if (!ok)
        throw std::runtime_error("gemma4_flm overrides: " + what);
}

inline void load_sequence(npu_app &app, const std::string &path)
{
    std::ifstream file(path, std::ios::binary | std::ios::ate);
    require(file.good(), path + " not found");
    std::vector<uint32_t> words(size_t(file.tellg()) / 4);
    file.seekg(0);
    file.read(reinterpret_cast<char *>(words.data()), words.size() * 4);
    app.seq()->from_vector(words);
}

struct view {
    flm_rt::bo bo;
    buffer<uint8_t> buf;
    view(bytes &parent, size_t offset) : bo(parent.bo(), parent.size() - offset, offset), buf(bo) {}
};

struct state {
    struct resident_layer {
        std::array<buffer<uint8_t>, ROLE_COUNT> weights;
    };

    struct stock_app {
        npu_app app;
        uint32_t m = 0;
    };

    std::string dir;
    npu_app_manager *mm = nullptr;
    npu_app_manager *dequant = nullptr;
    std::map<std::string, npu_app> apps;
    std::map<std::tuple<uint32_t, uint32_t, bool>, stock_app> stock_apps;
    std::map<std::pair<void *, size_t>, std::unique_ptr<view>> views;
    std::unique_ptr<Gemm> stock_gemm;
    std::vector<resident_layer> layers;
    size_t layer = 0;
    uint32_t mlp_d = 0;
    uint32_t mlp_i = 0;
};

inline state registered;

inline bytes &at_offset(bytes &parent, size_t offset)
{
    auto &result = registered.views[{parent.bo().get_handle().get(), offset}];
    if (!result)
        result = std::make_unique<view>(parent, offset);
    return result->buf;
}

inline size_t q4nx_bytes(size_t k, size_t n)
{
    return k * n * 5 / 8;
}

inline size_t bfp16_bytes(size_t k, size_t n)
{
    return k * n * 9 / 8;
}

inline npu_app &operator_for(npu_app_manager *manager, const std::string &file)
{
    auto result = registered.apps.find(file);
    if (result == registered.apps.end()) {
        npu_app app = manager->create_app();
        load_sequence(app, registered.dir + "/" + file);
        result = registered.apps.emplace(file, std::move(app)).first;
    }
    return result->second;
}

inline bytes &resident(role matrix)
{
    require(registered.layer < registered.layers.size(), "resident layer is out of range");
    bytes &weight = registered.layers[registered.layer].weights[matrix];
    require(weight.size() != 0, std::string("resident weight is missing: ") + role_names[matrix]);
    return weight;
}

inline void load_resident(npu_app_manager *manager, const std::string &model, bool bfp16)
{
    const std::string mlp_path = model + (bfp16 ? "/model.dq_bfp" : "/model.dq_bf16");
    const std::string attn_path = bfp16 ? model + "/model.dq_bfp_attn" : mlp_path;
    require(std::ifstream(mlp_path).good(), mlp_path + " not found");
    require(std::ifstream(attn_path).good(), attn_path + " not found");
    SafeTensors mlp(mlp_path);
    SafeTensors attn(attn_path);
    const std::string suffix = bfp16 ? ".dq_bfp" : ".dq_bf16";
    size_t total = 0;

    for (size_t layer = 0;; ++layer) {
        const std::string prefix = "model.layers." + std::to_string(layer) + ".";
        if (!attn.has_tensor(prefix + role_names[Q] + ".weight" + suffix))
            break;
        state::resident_layer resident_layer;
        for (size_t matrix = 0; matrix < ROLE_COUNT; ++matrix) {
            SafeTensors &source = matrix <= O ? attn : mlp;
            const std::string name = prefix + role_names[matrix] + ".weight" + suffix;
            if (!source.has_tensor(name))
                continue;
            const size_t bytes = source.get_tensor_metadata(name).byte_size;
            resident_layer.weights[matrix] = manager->create_bo_buffer<uint8_t>(bytes);
            source.load_weights(resident_layer.weights[matrix], name);
            resident_layer.weights[matrix].sync_to_device();
            total += bytes;
        }
        registered.layers.push_back(std::move(resident_layer));
    }
    require(!registered.layers.empty(), "no resident projection weights found");
    header_print("info", "resident projection weights: " + std::to_string(total / (1024 * 1024)) + " MiB");
}

// Operator dispatch functions

inline npu_app &gemm(uint32_t m, uint32_t k, uint32_t n, bool gelu = false)
{
    const std::string file = "gemm_M" + std::to_string(m) + "_K" + std::to_string(k) + "_N" + std::to_string(n) +
                             (gelu ? "_gelu" : "") + ".bin";
    return operator_for(registered.mm, file);
}

inline npu_app &stock_gemm(uint32_t m, uint32_t k, uint32_t n, bool gelu = false)
{
    auto &entry = registered.stock_apps[{k, n, gelu}];
    if (entry.m != m) {
        if (entry.m == 0)
            entry.app = registered.mm->create_app();
        registered.stock_gemm->generate_seq(
            entry.app.seq(), m, k, n, 0, false, gelu ? Gemm::GeLU : Gemm::NO_Activation, 0);
        entry.m = m;
    }
    return entry.app;
}

template <class Weight> ert_cmd_state dequant(bytes &quantized, const Weight &weight, bytes &out, size_t offset = 0)
{
    const std::string file =
        "dequant_K" + std::to_string(weight.shape[0]) + "_N" + std::to_string(weight.shape[1]) + ".bin";
    return operator_for(registered.dequant, file)(at_offset(quantized, weight.offset + offset), out);
}

template <class Layer, class Shape, class Buffers>
ert_cmd_state q_proj(const Layer &weight, const Shape &shape, Buffers &buffers, bytes &qkv)
{
    return gemm(shape.L_padded, weight.attn_q.shape[0], weight.attn_q.shape[1])(
        buffers->hidden_state_buffer, qkv, buffers->q_buffer);
}

template <class Layer, class Shape, class Buffers>
auto k_proj(const Layer &weight, const Shape &shape, Buffers &buffers, bytes &qkv)
{
    const size_t offset = bfp16_bytes(weight.attn_q.shape[0], weight.attn_q.shape[1]);
    return gemm(shape.L_padded, weight.attn_k.shape[0], weight.attn_k.shape[1])
        .create_run(buffers->hidden_state_buffer, at_offset(qkv, offset), buffers->k_buffer);
}

template <class Layer, class Shape, class Buffers>
auto v_proj(const Layer &weight, const Shape &shape, Buffers &buffers, bytes &qkv)
{
    const size_t offset = bfp16_bytes(weight.attn_q.shape[0], weight.attn_q.shape[1] + weight.attn_k.shape[1]);
    return gemm(shape.L_padded, weight.attn_v.shape[0], weight.attn_v.shape[1])
        .create_run(buffers->hidden_state_buffer, at_offset(qkv, offset), buffers->v_buffer);
}

template <class Layer, class Shape, class Buffers>
ert_cmd_state o_proj(const Layer &weight, const Shape &shape, Buffers &buffers, bytes &output)
{
    return gemm(shape.L_padded, weight.attn_output.shape[0], weight.attn_output.shape[1])(
        buffers->attn_out_buffer, output, buffers->hidden_state_buffer);
}

template <class Npu, class Config> void engine_init(Npu *npu, const Config &config)
{
    const auto xclbin = [&](const char *name) {
        return npu->register_xclbin(utils::path_join(config.exec_path, "xclbins", config.model_name, name));
    };
    registered.dir = utils::path_join(config.exec_path, "xclbins", config.model_name, "iron");
    registered.mm = xclbin("mm.xclbin");
#if defined(IRON_OFFLINE_BF16)
    auto stock_config = config;
    registered.stock_gemm = std::make_unique<Gemm>(stock_config);
    load_resident(registered.mm, config.model_path, false);
    header_print("info", "FastFlowLM GEMM with offline BF16 weights");
#elif defined(IRON_OFFLINE_BFP16)
    load_resident(registered.mm, config.model_path, true);
    header_print("info", "IRON GEMM with offline BFP16 weights");
#else
    registered.dequant = xclbin("dequant.xclbin");
    header_print("info", "IRON GEMM and dequant from " + registered.dir);
#endif
}

} // namespace iron

// Dispatch override macros

#define FLM_PP_CAT_(a, b) a##b
#define FLM_PP_CAT(a, b) FLM_PP_CAT_(a, b)
#define FLM_PP_SECOND(a, b, ...) b
#define FLM_PP_IS_PROBE(...) FLM_PP_SECOND(__VA_ARGS__, 0)
#define FLM_PP_PROBE() ~, 1

#define FLM_HAS_OVERRIDE_engine_init FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_prefill_layer_begin FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_dequant_qkv FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_dequant_o FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_dequant_up FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_dequant_gate FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_dequant_down FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_q_swa_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_q_global_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_k_swa_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_k_global_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_v_swa_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_v_global_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_o_swa_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_o_global_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_gate_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_up_proj FLM_PP_PROBE()
#define FLM_HAS_OVERRIDE_down_proj FLM_PP_PROBE()

#define FLM_OVERRIDE(name, expr, ...)                                                                                  \
    FLM_PP_CAT(FLM_OVERRIDE_, FLM_PP_IS_PROBE(FLM_PP_CAT(FLM_HAS_OVERRIDE_, name)))                                    \
    (name, expr __VA_OPT__(, ) __VA_ARGS__)
#define FLM_OVERRIDE_0(name, expr, ...) (expr)
#define FLM_OVERRIDE_1(name, expr, ...) FLM_PP_CAT(FLM_OV_, name)(expr __VA_OPT__(, ) __VA_ARGS__)

#define FLM_OV_engine_init(expr, npu, config) ::iron::engine_init(npu, config)
#define FLM_OV_prefill_layer_begin(expr, desc, layer_idx, type, prefill_shape)                                         \
    (::iron::registered.layer = (layer_idx),                                                                           \
     ::iron::registered.mlp_d = (desc)->weight_desc(type).ffn_gate.shape[0],                                           \
     ::iron::registered.mlp_i = (desc)->weight_desc(type).ffn_gate.shape[1])

#if defined(IRON_OFFLINE_BF16) || defined(IRON_OFFLINE_BFP16)
#define FLM_OV_dequant_qkv(expr, desc, type) ERT_CMD_STATE_COMPLETED
#define FLM_OV_dequant_o(expr, desc, type) ERT_CMD_STATE_COMPLETED
#define FLM_OV_dequant_up(expr, desc, type) ERT_CMD_STATE_COMPLETED
#define FLM_OV_dequant_gate(expr, desc, type) ERT_CMD_STATE_COMPLETED
#define FLM_OV_dequant_down(expr, desc, type) ERT_CMD_STATE_COMPLETED
#else
#define IRON_DEQUANT(matrix, out, ...)                                                                                 \
    ::iron::dequant(proj_weights, (desc)->weight_desc(type).matrix, out, ##__VA_ARGS__)
#define FLM_OV_dequant_qkv(expr, desc, type) IRON_DEQUANT(attn_qkv, this->qkv_weights)
#define FLM_OV_dequant_o(expr, desc, type) IRON_DEQUANT(attn_output, this->o_weights)
#define FLM_OV_dequant_up(expr, desc, type) IRON_DEQUANT(ffn_up, this->up_weights)
#define FLM_OV_dequant_gate(expr, desc, type)                                                                          \
    IRON_DEQUANT(ffn_gate, this->gate_weights, ::iron::q4nx_bytes((desc)->weight_desc(type).ffn_gate.shape[0], 512))
#define FLM_OV_dequant_down(expr, desc, type) IRON_DEQUANT(ffn_down, this->down_weights)
#endif

#if defined(IRON_OFFLINE_BF16)
#define FLM_OV_q_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::stock_gemm(                                                                                                \
        (prefill).L_padded, (desc)->weight_desc(type).attn_q.shape[0], (desc)->weight_desc(type).attn_q.shape[1])(     \
        bufs->q_buffer, bufs->hidden_state_buffer, ::iron::resident(::iron::Q))
#define FLM_OV_q_global_proj FLM_OV_q_swa_proj
#define FLM_OV_k_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::stock_gemm(                                                                                                \
        (prefill).L_padded, (desc)->weight_desc(type).attn_k.shape[0], (desc)->weight_desc(type).attn_k.shape[1])      \
        .create_run(bufs->k_buffer, bufs->hidden_state_buffer, ::iron::resident(::iron::K))
#define FLM_OV_k_global_proj FLM_OV_k_swa_proj
#define FLM_OV_v_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::stock_gemm(                                                                                                \
        (prefill).L_padded, (desc)->weight_desc(type).attn_v.shape[0], (desc)->weight_desc(type).attn_v.shape[1])      \
        .create_run(bufs->v_buffer, bufs->hidden_state_buffer, ::iron::resident(::iron::V))
#define FLM_OV_v_global_proj FLM_OV_v_swa_proj
#define FLM_OV_o_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::stock_gemm((prefill).L_padded,                                                                             \
                       (desc)->weight_desc(type).attn_output.shape[0],                                                 \
                       (desc)->weight_desc(type).attn_output.shape[1])(                                                \
        bufs->hidden_state_buffer, bufs->attn_out_buffer, ::iron::resident(::iron::O))
#define FLM_OV_o_global_proj FLM_OV_o_swa_proj

#define FLM_OV_gate_proj(expr, desc, double_wide, prefill)                                                             \
    ::iron::stock_gemm((prefill).L_padded, ::iron::registered.mlp_d, ::iron::registered.mlp_i, true)(                  \
        bufs->gate_buffer, bufs->hidden_state_buffer, ::iron::resident(::iron::GATE))
#define FLM_OV_up_proj(expr, desc, double_wide, prefill)                                                               \
    ::iron::stock_gemm((prefill).L_padded, ::iron::registered.mlp_d, ::iron::registered.mlp_i)(                        \
        bufs->up_buffer, bufs->hidden_state_buffer, ::iron::resident(::iron::UP))
#define FLM_OV_down_proj(expr, desc, double_wide, prefill)                                                             \
    ::iron::stock_gemm((prefill).L_padded, ::iron::registered.mlp_i, ::iron::registered.mlp_d)(                        \
        bufs->hidden_state_buffer, bufs->hid_buffer, ::iron::resident(::iron::DOWN))
#elif defined(IRON_OFFLINE_BFP16)
#define FLM_OV_q_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::gemm(                                                                                                      \
        (prefill).L_padded, (desc)->weight_desc(type).attn_q.shape[0], (desc)->weight_desc(type).attn_q.shape[1])(     \
        bufs->hidden_state_buffer, ::iron::resident(::iron::Q), bufs->q_buffer)
#define FLM_OV_q_global_proj FLM_OV_q_swa_proj
#define FLM_OV_k_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::gemm(                                                                                                      \
        (prefill).L_padded, (desc)->weight_desc(type).attn_k.shape[0], (desc)->weight_desc(type).attn_k.shape[1])      \
        .create_run(bufs->hidden_state_buffer, ::iron::resident(::iron::K), bufs->k_buffer)
#define FLM_OV_k_global_proj FLM_OV_k_swa_proj
#define FLM_OV_v_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::gemm(                                                                                                      \
        (prefill).L_padded, (desc)->weight_desc(type).attn_v.shape[0], (desc)->weight_desc(type).attn_v.shape[1])      \
        .create_run(bufs->hidden_state_buffer, ::iron::resident(::iron::V), bufs->v_buffer)
#define FLM_OV_v_global_proj FLM_OV_v_swa_proj
#define FLM_OV_o_swa_proj(expr, desc, type, prefill)                                                                   \
    ::iron::gemm((prefill).L_padded,                                                                                   \
                 (desc)->weight_desc(type).attn_output.shape[0],                                                       \
                 (desc)->weight_desc(type).attn_output.shape[1])(                                                      \
        bufs->attn_out_buffer, ::iron::resident(::iron::O), bufs->hidden_state_buffer)
#define FLM_OV_o_global_proj FLM_OV_o_swa_proj

#define FLM_OV_gate_proj(expr, desc, double_wide, prefill)                                                             \
    ::iron::gemm((prefill).L_padded, ::iron::registered.mlp_d, ::iron::registered.mlp_i, true)(                        \
        bufs->hidden_state_buffer, ::iron::resident(::iron::GATE), bufs->gate_buffer)
#define FLM_OV_up_proj(expr, desc, double_wide, prefill)                                                               \
    ::iron::gemm((prefill).L_padded, ::iron::registered.mlp_d, ::iron::registered.mlp_i)(                              \
        bufs->hidden_state_buffer, ::iron::resident(::iron::UP), bufs->up_buffer)
#define FLM_OV_down_proj(expr, desc, double_wide, prefill)                                                             \
    ::iron::gemm((prefill).L_padded, ::iron::registered.mlp_i, ::iron::registered.mlp_d)(                              \
        bufs->hid_buffer, ::iron::resident(::iron::DOWN), bufs->hidden_state_buffer)
#else
#define FLM_OV_q_swa_proj(expr, desc, type, shape) ::iron::q_proj((desc)->weight_desc(type), shape, bufs, qkv_weights)
#define FLM_OV_q_global_proj FLM_OV_q_swa_proj
#define FLM_OV_k_swa_proj(expr, desc, type, shape) ::iron::k_proj((desc)->weight_desc(type), shape, bufs, qkv_weights)
#define FLM_OV_k_global_proj FLM_OV_k_swa_proj
#define FLM_OV_v_swa_proj(expr, desc, type, shape) ::iron::v_proj((desc)->weight_desc(type), shape, bufs, qkv_weights)
#define FLM_OV_v_global_proj FLM_OV_v_swa_proj
#define FLM_OV_o_swa_proj(expr, desc, type, shape) ::iron::o_proj((desc)->weight_desc(type), shape, bufs, o_weights)
#define FLM_OV_o_global_proj FLM_OV_o_swa_proj

#define FLM_OV_gate_proj(expr, desc, double_wide, shape)                                                               \
    ::iron::gemm((shape).L_padded, ::iron::registered.mlp_d, ::iron::registered.mlp_i, true)(                          \
        bufs->hidden_state_buffer, gate_weights, bufs->gate_buffer)
#define FLM_OV_up_proj(expr, desc, double_wide, shape)                                                                 \
    ::iron::gemm((shape).L_padded, ::iron::registered.mlp_d, ::iron::registered.mlp_i)(                                \
        bufs->hidden_state_buffer, up_weights, bufs->up_buffer)
#define FLM_OV_down_proj(expr, desc, double_wide, shape)                                                               \
    ::iron::gemm((shape).L_padded, ::iron::registered.mlp_i, ::iron::registered.mlp_d)(                                \
        bufs->hid_buffer, down_weights, bufs->hidden_state_buffer)
#endif

#endif // GEMMA4_FLM_GEMM_DEQUANT_OVERRIDES_HPP
