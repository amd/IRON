// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
//
// Runs every text-path operator of FastFlowLM's Gemma 4 engine on IRON's operators.
// The engine build includes this header.

#ifndef GEMMA4_FLM_OVERRIDES_HPP
#define GEMMA4_FLM_OVERRIDES_HPP

#include "npu_utils/npu_utils.hpp"
#include "utils/utils.hpp"

#include <cstdint>
#include <filesystem>
#include <fstream>
#include <map>
#include <memory>
#include <optional>
#include <stdexcept>
#include <string>
#include <vector>

// Instruction sequence generators that build.py extracts from IRON's dynamic operators.
#include "attn.h"
#include "layer_global.h"
#include "layer_global_skip.h"
#include "layer_swa.h"
#include "layer_swa_skip.h"
#include "swa.h"

namespace iron
{

// ----------------------------------------------------------------------------
// Common helpers
// ----------------------------------------------------------------------------

inline void require(bool ok, const std::string &what)
{
    if (!ok)
        throw std::runtime_error("gemma4_flm overrides: " + what);
}

/// Loads an instruction sequence that build.py wrote to a file.
inline void load_sequence(npu_app &app, const std::string &path)
{
    std::ifstream f(path, std::ios::binary | std::ios::ate);
    require(f.good(), path + " not found");
    std::vector<uint32_t> words(size_t(f.tellg()) / 4);
    f.seekg(0);
    f.read(reinterpret_cast<char *>(words.data()), words.size() * 4);
    app.seq()->from_vector(words);
}

/// An operator whose instruction sequence depends on values known only at
/// dispatch, such as the context length. The generator runs again when they change.
struct dynamic_op {
    npu_app app;
    std::vector<int32_t> params;

    template <class Generator, class... Params> npu_app &at(Generator generate, Params... p)
    {
        std::vector<int32_t> want{int32_t(p)...};
        if (want != this->params) {
            std::optional<std::vector<uint32_t>> words = generate(p...);
            require(words.has_value(), "the sequence generator failed");
            this->app.seq()->from_vector(*words);
            this->params = want;
        }
        return this->app;
    }
};

/// A device buffer that starts `offset` bytes into another one.
struct view {
    flm_rt::bo bo;
    buffer<uint8_t> buf;
    view(bytes &parent, size_t offset) : bo(parent.bo(), parent.size() - offset, offset), buf(bo) {}
};

struct state {
    std::string dir; ///< the instruction sequences and weights build.py staged
    npu_app_manager *mm = nullptr, *dequant = nullptr;
    npu_app lm_head;
    dynamic_op layer[4]; ///< indexed by the engine's gemma4e_layer_type_t
    dynamic_op attn, swa;
    std::map<std::string, npu_app> static_ops;
    std::map<std::pair<void *, size_t>, std::unique_ptr<view>> views;
    buffer<uint8_t> pli_down, pli_gate, pli_up;
    uint32_t mlp_d = 0, mlp_i = 0; ///< the MLP shape of the layer being prefilled
};

inline state &S()
{
    static state s;
    return s;
}

inline bytes &at_offset(bytes &parent, size_t offset)
{
    auto &v = S().views[{parent.bo().get_handle().get(), offset}];
    if (!v)
        v = std::make_unique<view>(parent, offset);
    return v->buf;
}

inline buffer<uint8_t> load_weights(const std::string &path)
{
    std::ifstream f(path, std::ios::binary | std::ios::ate);
    require(f.good(), path + " not found");
    buffer<uint8_t> b = S().mm->create_bo_buffer<uint8_t>(size_t(f.tellg()));
    f.seekg(0);
    f.read(reinterpret_cast<char *>(b.data()), b.size());
    b.sync_to_device();
    return b;
}

// q4nx stores 5 bits per weight. IRON's GEMM reads bfp16ebs8, 9 bytes per 8 weights.
inline size_t q4nx_bytes(size_t k, size_t n)
{
    return k * n * 5 / 8;
}
inline size_t bfp16_bytes(size_t k, size_t n)
{
    return k * n * 9 / 8;
}

// ----------------------------------------------------------------------------
// Operator functions
// ----------------------------------------------------------------------------

/// The operator `file` holds the instruction sequence of, on the xclbin of `mgr`.
inline npu_app &static_op(npu_app_manager *mgr, const std::string &file)
{
    auto it = S().static_ops.find(file);
    if (it == S().static_ops.end()) {
        npu_app app = mgr->create_app();
        load_sequence(app, S().dir + "/" + file);
        it = S().static_ops.emplace(file, std::move(app)).first;
    }
    return it->second;
}

inline npu_app &gemm(uint32_t m, uint32_t k, uint32_t n, bool gelu = false)
{
    const std::string file = "gemm_M" + std::to_string(m) + "_K" + std::to_string(k) + "_N" + std::to_string(n) +
                             (gelu ? "_gelu" : "") + ".bin";
    require(S().static_ops.count(file) || std::filesystem::exists(S().dir + "/" + file),
            "no GEMM for M=" + std::to_string(m) +
                "; run flm with --prefill-chunk-len 512, or raise CHUNK in build.py");
    return static_op(S().mm, file);
}

/// Dequantizes the (K, N) matrix `w` describes out of a layer's quantized weights.
template <class Weight> ert_cmd_state dequant(bytes &quantized, const Weight &w, bytes &out, size_t extra_offset = 0)
{
    const std::string file = "dequant_K" + std::to_string(w.shape[0]) + "_N" + std::to_string(w.shape[1]) + ".bin";
    return static_op(S().dequant, file)(at_offset(quantized, w.offset + extra_offset), out);
}

// ----------------------------------------------------------------------------
// Overrides
// ----------------------------------------------------------------------------

// The engine wraps each operator dispatch in FLM_OVERRIDE(name, expr, ...). By
// default the macro expands to `expr`, the engine's own dispatch. This header
// redefines FLM_OVERRIDE to paste `name` onto FLM_OV_: FLM_OVERRIDE(lm_head, expr)
// expands to FLM_OV_lm_head(expr). Each FLM_OV_<name> macro below dispatches an
// IRON operator, or expands to `expr` to run the engine's operator. The macros
// expand inside the engine's methods, so they can use the engine's members.
//
// The engine includes this header before it defines its own types. The override
// functions are therefore templates over the types that the call sites pass.

template <class Layer, class Shape, class Bufs>
ert_cmd_state q_proj(const Layer &w, const Shape &s, Bufs &bufs, bytes &qkv)
{
    return gemm(s.L_padded, w.attn_q.shape[0], w.attn_q.shape[1])(bufs->hidden_state_buffer, qkv, bufs->q_buffer);
}

template <class Layer, class Shape, class Bufs> auto k_proj(const Layer &w, const Shape &s, Bufs &bufs, bytes &qkv)
{
    const size_t k_at = bfp16_bytes(w.attn_q.shape[0], w.attn_q.shape[1]);
    return gemm(s.L_padded, w.attn_k.shape[0], w.attn_k.shape[1])
        .create_run(bufs->hidden_state_buffer, at_offset(qkv, k_at), bufs->k_buffer);
}

template <class Layer, class Shape, class Bufs> auto v_proj(const Layer &w, const Shape &s, Bufs &bufs, bytes &qkv)
{
    const size_t v_at = bfp16_bytes(w.attn_q.shape[0], w.attn_q.shape[1] + w.attn_k.shape[1]);
    return gemm(s.L_padded, w.attn_v.shape[0], w.attn_v.shape[1])
        .create_run(bufs->hidden_state_buffer, at_offset(qkv, v_at), bufs->v_buffer);
}

template <class Layer, class Shape, class Bufs>
ert_cmd_state o_proj(const Layer &w, const Shape &s, Bufs &bufs, bytes &o)
{
    return gemm(s.L_padded, w.attn_output.shape[0], w.attn_output.shape[1])(
        bufs->attn_out_buffer, o, bufs->hidden_state_buffer);
}

/// Registers the engine's xclbin paths. build.py stages IRON's xclbins under
/// those names, so the engine and this header share one hardware context per
/// xclbin. The device holds 16.
template <class Npu, class Config> void engine_init(Npu *npu, const Config &config)
{
    state &s = S();
    const auto xclbin = [&](const char *name) {
        return npu->register_xclbin(utils::path_join(config.exec_path, "xclbins", config.model_name, name));
    };
    s.dir = utils::path_join(config.exec_path, "xclbins", config.model_name, "iron");
    for (dynamic_op &op : s.layer)
        op.app = xclbin("layer.xclbin")->create_app();
    s.attn.app = xclbin("attn.xclbin")->create_app();
    s.swa.app = xclbin("swa.xclbin")->create_app();
    s.lm_head = xclbin("lm_head.xclbin")->create_app();
    load_sequence(s.lm_head, s.dir + "/lm_head.bin");
    s.mm = xclbin("mm.xclbin");
    s.dequant = xclbin("dequant.xclbin");
    header_print("info", "IRON operators from " + s.dir);
}

/// Loads the per-layer-input projection weights that build.py repacked for IRON's GEMM.
inline void load_pli_weights()
{
    S().pli_down = load_weights(S().dir + "/pli_down.weights");
    S().pli_gate = load_weights(S().dir + "/pli_gate.weights");
    S().pli_up = load_weights(S().dir + "/pli_up.weights");
}

} // namespace iron

#define FLM_OVERRIDE(name, expr, ...) FLM_OV_##name(expr __VA_OPT__(, ) __VA_ARGS__)

#define FLM_OV_engine_init(expr, npu, config) ::iron::engine_init(npu, config)
#define FLM_OV_head_weights_loaded(expr, desc) ::iron::load_pli_weights()
#define FLM_OV_layer_weights_loaded(expr, ...) (expr)
#define FLM_OV_prefill_layer_begin(expr, desc, layer_idx, type, s)                                                     \
    (::iron::S().mlp_d = (desc)->weight_desc(type).ffn_gate.shape[0],                                                  \
     ::iron::S().mlp_i = (desc)->weight_desc(type).ffn_gate.shape[1])

// The decode layer, one token through one layer. `_run` builds a run for the
// engine's runlist. The others run at once: on a device with preemption,
// and in the token-by-token prefill of short prompts (`_mv`).
#define IRON_LAYER(gen, type, L, max_l)                                                                                \
    ::iron::S().layer[int(type)].at(::iron::seq::gen::generate_txn_main_sequence, int32_t(L), int32_t(max_l))
#define IRON_LAYER_ARGS(i, kv) this->x, this->proj_weights[i], this->rms_weights[i], this->rope_rms_weights[i], kv
#define IRON_KV_GLOBAL_SKIP this->kv_caches[last_global_kv_cache_layer_idx]
#define IRON_KV_SWA_SKIP this->kv_caches[last_swa_kv_cache_layer_idx]

#define FLM_OV_global_layer_run(expr, type, i, L, max_l)                                                               \
    IRON_LAYER(layer_global, type, L, max_l).create_run(IRON_LAYER_ARGS(i, this->kv_caches[i]))
#define FLM_OV_swa_layer_run(expr, type, i, L, max_l)                                                                  \
    IRON_LAYER(layer_swa, type, L, max_l).create_run(IRON_LAYER_ARGS(i, this->kv_caches[i]))
#define FLM_OV_global_skip_layer_run(expr, type, i, L, max_l)                                                          \
    IRON_LAYER(layer_global_skip, type, L, max_l).create_run(IRON_LAYER_ARGS(i, IRON_KV_GLOBAL_SKIP))
#define FLM_OV_swa_skip_layer_run(expr, type, i, L, max_l)                                                             \
    IRON_LAYER(layer_swa_skip, type, L, max_l).create_run(IRON_LAYER_ARGS(i, IRON_KV_SWA_SKIP))

#define FLM_OV_global_layer(expr, type, i, L, max_l)                                                                   \
    IRON_LAYER(layer_global, type, L, max_l)(IRON_LAYER_ARGS(i, this->kv_caches[i]))
#define FLM_OV_swa_layer(expr, type, i, L, max_l)                                                                      \
    IRON_LAYER(layer_swa, type, L, max_l)(IRON_LAYER_ARGS(i, this->kv_caches[i]))
#define FLM_OV_global_skip_layer(expr, type, i, L, max_l)                                                              \
    IRON_LAYER(layer_global_skip, type, L, max_l)(IRON_LAYER_ARGS(i, IRON_KV_GLOBAL_SKIP))
#define FLM_OV_swa_skip_layer(expr, type, i, L, max_l)                                                                 \
    IRON_LAYER(layer_swa_skip, type, L, max_l)(IRON_LAYER_ARGS(i, IRON_KV_SWA_SKIP))

#define FLM_OV_global_layer_mv(expr, type, i)                                                                          \
    FLM_OV_global_layer(expr, type, i, this->current_context_length, this->MAX_L)
#define FLM_OV_swa_layer_mv(expr, type, i) FLM_OV_swa_layer(expr, type, i, this->current_context_length, this->MAX_L)
#define FLM_OV_global_skip_layer_mv(expr, type, i)                                                                     \
    FLM_OV_global_skip_layer(expr, type, i, this->current_context_length, this->MAX_L)
#define FLM_OV_swa_skip_layer_mv(expr, type, i)                                                                        \
    FLM_OV_swa_skip_layer(expr, type, i, this->current_context_length, this->MAX_L)

// The engine's layer.xclbin runs an empty sequence after each token. It runs
// unchanged on IRON's layer.xclbin.
#define FLM_OV_layer_pre_load(expr) (expr)

#define FLM_OV_lm_head(expr) ::iron::S().lm_head.create_run(this->logits, this->lm_head_weights, this->x)

// Prefill attention over the chunk's rows of the KV cache.
#define IRON_ATTN(op, s, max_l)                                                                                        \
    ::iron::S().op.at(                                                                                                 \
        ::iron::seq::op::generate_txn_main_sequence, (s).L_begin_chunked, (s).L_begin_chunked + (s).L_padded, max_l)
#define FLM_OV_swa_attn_core(expr, type, s, max_l)                                                                     \
    IRON_ATTN(swa, s, max_l)(bufs->attn_out_buffer, bufs->q_buffer, kv_cache_sliding_prefill)
#define FLM_OV_global_attn_core(expr, type, s, max_l)                                                                  \
    IRON_ATTN(attn, s, max_l)(bufs->attn_out_buffer, bufs->q_buffer, kv_cache_global_prefill)

// Dequantizes one layer's projections into the engine's buffers. up and gate
// interleave in runs of 512 out-features; gate's first run follows up's.
#define IRON_DEQUANT(matrix, out, ...)                                                                                 \
    ::iron::dequant(proj_weights, (desc)->weight_desc(type).matrix, out, ##__VA_ARGS__)
#define FLM_OV_dequant_qkv(expr, desc, type) IRON_DEQUANT(attn_qkv, this->qkv_weights)
#define FLM_OV_dequant_o(expr, desc, type) IRON_DEQUANT(attn_output, this->o_weights)
#define FLM_OV_dequant_up(expr, desc, type) IRON_DEQUANT(ffn_up, this->up_weights)
#define FLM_OV_dequant_gate(expr, desc, type)                                                                          \
    IRON_DEQUANT(ffn_gate, this->gate_weights, ::iron::q4nx_bytes((desc)->weight_desc(type).ffn_gate.shape[0], 512))
#define FLM_OV_dequant_down(expr, desc, type) IRON_DEQUANT(ffn_down, this->down_weights)

// The attention projections. M is the chunk's row count. k and v read their
// share of the q|k|v matrix that dequant_qkv wrote.
#define FLM_OV_q_swa_proj(expr, desc, type, s) ::iron::q_proj((desc)->weight_desc(type), s, bufs, qkv_weights)
#define FLM_OV_q_global_proj FLM_OV_q_swa_proj
#define FLM_OV_k_swa_proj(expr, desc, type, s) ::iron::k_proj((desc)->weight_desc(type), s, bufs, qkv_weights)
#define FLM_OV_k_global_proj FLM_OV_k_swa_proj
#define FLM_OV_v_swa_proj(expr, desc, type, s) ::iron::v_proj((desc)->weight_desc(type), s, bufs, qkv_weights)
#define FLM_OV_v_global_proj FLM_OV_v_swa_proj
#define FLM_OV_o_swa_proj(expr, desc, type, s) ::iron::o_proj((desc)->weight_desc(type), s, bufs, o_weights)
#define FLM_OV_o_global_proj FLM_OV_o_swa_proj

// The MLP. Its width differs between layers, so prefill_layer_begin records it.
#define FLM_OV_gate_proj(expr, desc, double_wide, s)                                                                   \
    ::iron::gemm((s).L_padded, ::iron::S().mlp_d, ::iron::S().mlp_i, true)(                                            \
        bufs->hidden_state_buffer, gate_weights, bufs->gate_buffer)
#define FLM_OV_up_proj(expr, desc, double_wide, s)                                                                     \
    ::iron::gemm((s).L_padded, ::iron::S().mlp_d, ::iron::S().mlp_i)(                                                  \
        bufs->hidden_state_buffer, up_weights, bufs->up_buffer)
#define FLM_OV_down_proj(expr, desc, double_wide, s)                                                                   \
    ::iron::gemm((s).L_padded, ::iron::S().mlp_i, ::iron::S().mlp_d)(                                                  \
        bufs->hid_buffer, down_weights, bufs->hidden_state_buffer)

// The per-layer-input projections. M is the chunk's row count rounded up to
// 512. gate and up hold one matrix per layer, one after another.
#define FLM_OV_pli_down_proj(expr, desc, s)                                                                            \
    ::iron::gemm((s).L_padded_512, (desc)->D, (desc)->PLI_D *(desc)->num_hidden_layers)(                               \
        bufs->hidden_state_buffer, ::iron::S().pli_down, bufs->pli_down_buffer)
#define FLM_OV_pli_gate_proj(expr, desc, layer_idx, s)                                                                 \
    ::iron::gemm((s).L_padded_512, (desc)->D, (desc)->PLI_D, true)(                                                    \
        bufs->hidden_state_buffer,                                                                                     \
        ::iron::at_offset(::iron::S().pli_gate, layer_idx * ::iron::bfp16_bytes((desc)->D, (desc)->PLI_D)),            \
        bufs->pli_gate_buffer)
#define FLM_OV_pli_up_proj(expr, desc, layer_idx, s)                                                                   \
    ::iron::gemm((s).L_padded_512, (desc)->PLI_D, (desc)->D)(                                                          \
        bufs->pli_hid_buffer,                                                                                          \
        ::iron::at_offset(::iron::S().pli_up, layer_idx * ::iron::bfp16_bytes((desc)->D, (desc)->PLI_D)),              \
        bufs->hidden_state_buffer)

// The image and audio encoders stay on the engine.
#define FLM_OV_vision_attn_core(expr, ...) (expr)
#define FLM_OV_vision_patch_embed(expr, ...) (expr)
#define FLM_OV_vision_pos_embed_dim0(expr, ...) (expr)
#define FLM_OV_vision_pos_embed_dim1(expr, ...) (expr)
#define FLM_OV_vision_q_proj(expr, ...) (expr)
#define FLM_OV_vision_k_proj(expr, ...) (expr)
#define FLM_OV_vision_v_proj(expr, ...) (expr)
#define FLM_OV_vision_o_proj(expr, ...) (expr)
#define FLM_OV_vision_gate_proj(expr, ...) (expr)
#define FLM_OV_vision_up_proj(expr, ...) (expr)
#define FLM_OV_vision_down_proj(expr, ...) (expr)
#define FLM_OV_vision_to_language_proj(expr, ...) (expr)
#define FLM_OV_audio_conv1d(expr, ...) (expr)
#define FLM_OV_audio_conv1d_start_proj(expr, ...) (expr)
#define FLM_OV_audio_conv1d_end_proj(expr, ...) (expr)
#define FLM_OV_audio_pre_encode_proj(expr, ...) (expr)
#define FLM_OV_audio_sub_sample_proj(expr, ...) (expr)
#define FLM_OV_audio_q_proj(expr, ...) (expr)
#define FLM_OV_audio_k_proj(expr, ...) (expr)
#define FLM_OV_audio_v_proj(expr, ...) (expr)
#define FLM_OV_audio_o_proj(expr, ...) (expr)
#define FLM_OV_audio_ffn_up_proj(expr, ...) (expr)
#define FLM_OV_audio_ffn_down_proj(expr, ...) (expr)
#define FLM_OV_audio_to_language_proj(expr, ...) (expr)

#endif // GEMMA4_FLM_OVERRIDES_HPP
