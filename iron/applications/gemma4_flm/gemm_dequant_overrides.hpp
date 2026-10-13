// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#ifndef GEMMA4_FLM_GEMM_DEQUANT_OVERRIDES_HPP
#define GEMMA4_FLM_GEMM_DEQUANT_OVERRIDES_HPP

#include "npu_utils/npu_utils.hpp"
#include "utils/utils.hpp"

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
    std::string dir;
    npu_app_manager *mm = nullptr;
    npu_app_manager *dequant = nullptr;
    std::map<std::string, npu_app> apps;
    std::map<std::pair<void *, size_t>, std::unique_ptr<view>> views;
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

// Operator dispatch functions

inline npu_app &gemm(uint32_t m, uint32_t k, uint32_t n, bool gelu = false)
{
    const std::string file = "gemm_M" + std::to_string(m) + "_K" + std::to_string(k) + "_N" + std::to_string(n) +
                             (gelu ? "_gelu" : "") + ".bin";
    return operator_for(registered.mm, file);
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
    registered.dequant = xclbin("dequant.xclbin");
    header_print("info", "IRON GEMM and dequant from " + registered.dir);
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
    FLM_PP_CAT(FLM_OVERRIDE_, FLM_PP_IS_PROBE(FLM_PP_CAT(FLM_HAS_OVERRIDE_, name)))(name,                              \
                                                                                    expr __VA_OPT__(, ) __VA_ARGS__)
#define FLM_OVERRIDE_0(name, expr, ...) (expr)
#define FLM_OVERRIDE_1(name, expr, ...) FLM_PP_CAT(FLM_OV_, name)(expr __VA_OPT__(, ) __VA_ARGS__)

#define FLM_OV_engine_init(expr, npu, config) ::iron::engine_init(npu, config)
#define FLM_OV_prefill_layer_begin(expr, desc, layer_idx, type, prefill_shape)                                         \
    (::iron::registered.mlp_d = (desc)->weight_desc(type).ffn_gate.shape[0],                                           \
     ::iron::registered.mlp_i = (desc)->weight_desc(type).ffn_gate.shape[1])

#define IRON_DEQUANT(matrix, out, ...)                                                                                 \
    ::iron::dequant(proj_weights, (desc)->weight_desc(type).matrix, out, ##__VA_ARGS__)
#define FLM_OV_dequant_qkv(expr, desc, type) IRON_DEQUANT(attn_qkv, this->qkv_weights)
#define FLM_OV_dequant_o(expr, desc, type) IRON_DEQUANT(attn_output, this->o_weights)
#define FLM_OV_dequant_up(expr, desc, type) IRON_DEQUANT(ffn_up, this->up_weights)
#define FLM_OV_dequant_gate(expr, desc, type)                                                                          \
    IRON_DEQUANT(ffn_gate, this->gate_weights, ::iron::q4nx_bytes((desc)->weight_desc(type).ffn_gate.shape[0], 512))
#define FLM_OV_dequant_down(expr, desc, type) IRON_DEQUANT(ffn_down, this->down_weights)

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

#endif // GEMMA4_FLM_GEMM_DEQUANT_OVERRIDES_HPP
