// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 2D Convolution Kernel for AIE2P (NPU2)

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <type_traits>

extern "C" {

/**
 * 2D Convolution Kernel - AIE2P optimized
 * Vector factor 16 (AIE2P).
 *
 * @param input - Input tensor [N, in_channels, in_height, in_width] (flattened)
 * @param weight - Weight tensor [out_channels, in_channels, kernel_height, kernel_width]
 * @param output - Output tensor [N, out_channels, out_height, out_width] (flattened)
 * @param bias - Optional bias tensor [out_channels]
 */
void conv2d_bf16_scalar(bfloat16 *input,
                        bfloat16 *weight,
                        bfloat16 *output,
                        bfloat16 *bias,
                        int N, // batch size
                        int in_channels,
                        int in_height,
                        int in_width,
                        int out_channels,
                        int out_height,
                        int out_width,
                        int kernel_h,
                        int kernel_w,
                        int stride_h,
                        int stride_w,
                        int pad_h,
                        int pad_w,
                        int groups,
                        int apply_bias)
{
    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;

    for (int n = 0; n < N; n++) {
        for (int oc = 0; oc < out_channels; oc++) {
            int group_id = oc / out_channels_per_group;
            int ic_start = group_id * channels_per_group;

            for (int oh = 0; oh < out_height; oh++) {
                for (int ow = 0; ow < out_width; ow++) {
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;

                    bfloat16 acc = bfloat16(0.0f);

                    for (int ic = 0; ic < channels_per_group; ic++) {
                        int ic_global = ic_start + ic;

                        for (int kh = 0; kh < kernel_h; kh++) {
                            for (int kw = 0; kw < kernel_w; kw++) {
                                int ih = ih_start + kh;
                                int iw = iw_start + kw;

                                if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                    int input_idx = ((n * in_channels + ic_global) * in_height + ih) * in_width + iw;
                                    int weight_idx = ((oc * channels_per_group + ic) * kernel_h + kh) * kernel_w + kw;

                                    acc += input[input_idx] * weight[weight_idx];
                                }
                            }
                        }
                    }

                    if (apply_bias) {
                        // Packed bias: B_tile follows W_tile in the weight buffer.
                        int w_only = out_channels * channels_per_group * kernel_h * kernel_w;
                        acc += weight[w_only + oc];
                        (void)bias;
                    }

                    int out_idx = ((n * out_channels + oc) * out_height + oh) * out_width + ow;
                    output[out_idx] = acc;
                }
            }
        }
    }
}

/**
 * 2D Convolution Kernel - Vectorized version for AIE2P
 *
 * Pointwise (k=1): vectorize over OW with aie::mac float accum when stride_w==1.
 * k>1 / non-unit stride_w: scalar float path.
 *
 * @param input - Input tensor [N, in_channels, in_height, in_width] (flattened)
 * @param weight - Weight tensor [out_channels, in_channels, kernel_height, kernel_width]
 * @param output - Output tensor [N, out_channels, out_height, out_width] (flattened)
 * @param bias - Optional bias tensor [out_channels]
 */
void conv2d_bf16_vector(bfloat16 *input,
                        bfloat16 *weight,
                        bfloat16 *output,
                        bfloat16 *bias,
                        int N, // batch size
                        int in_channels,
                        int in_height,
                        int in_width,
                        int out_channels,
                        int out_height,
                        int out_width,
                        int kernel_h,
                        int kernel_w,
                        int stride_h,
                        int stride_w,
                        int pad_h,
                        int pad_w,
                        int groups,
                        int apply_bias)
{
    constexpr int vec_factor = 16;

    event0();

    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;
    int spatial_size = out_height * out_width;
    const int w_only = out_channels * channels_per_group * kernel_h * kernel_w;
    const aie::vector<bfloat16, vec_factor> ones =
        aie::broadcast<bfloat16, vec_factor>(bfloat16(1.0f));

    for (int n = 0; n < N; n++) {
        for (int oc = 0; oc < out_channels; oc++) {
            int group_id = oc / out_channels_per_group;
            int ic_start = group_id * channels_per_group;

            bfloat16 *__restrict out_ptr = output + (n * out_channels + oc) * spatial_size;
            const bfloat16 *__restrict w_oc =
                weight + oc * channels_per_group * kernel_h * kernel_w;

            for (int oh = 0; oh < out_height; oh++) {
                int ih_base = oh * stride_h - pad_h;
                int ow = 0;

                // Dense OW tiles: unit stride in W → contiguous input window.
                // Dense OW vector only for k=1; k>1 uses scalar float below.
                if (stride_w == 1 && kernel_h == 1 && kernel_w == 1) {
                    for (; ow + vec_factor <= out_width; ow += vec_factor) {
                        aie::accum<accfloat, vec_factor> acc =
                            aie::zeros<accfloat, vec_factor>();

                        if (apply_bias) {
                            acc = aie::mac(
                                acc,
                                aie::broadcast<bfloat16, vec_factor>(weight[w_only + oc]),
                                ones);
                            (void)bias;
                        }

                        for (int ic = 0; ic < channels_per_group; ic++) {
                            int ic_global = ic_start + ic;
                            const bfloat16 *__restrict in_ch =
                                input + (n * in_channels + ic_global) * in_height * in_width;

                            for (int kh = 0; kh < kernel_h; kh++) {
                                int ih = ih_base + kh;
                                if (ih < 0 || ih >= in_height) {
                                    continue;
                                }
                                const bfloat16 *__restrict in_row = in_ch + ih * in_width;

                                for (int kw = 0; kw < kernel_w; kw++) {
                                    int iw0 = ow - pad_w + kw;
                                    int iw_last = iw0 + vec_factor - 1;
                                    aie::vector<bfloat16, vec_factor> w_vec =
                                        aie::broadcast<bfloat16, vec_factor>(
                                            w_oc[(ic * kernel_h + kh) * kernel_w + kw]);
                                    aie::vector<bfloat16, vec_factor> in_vec;
                                    // Do not write vector lanes via operator[] (not reliable on AIE).
                                    // Interior aligned → load_v; else gather into aligned tmp then load_v.
                                    if (iw0 >= 0 && iw_last < in_width &&
                                        (iw0 & (vec_factor - 1)) == 0) {
                                        in_vec = aie::load_v<vec_factor>(in_row + iw0);
                                    } else {
                                        alignas(32) bfloat16 gather_tmp[vec_factor];
                                        for (int i = 0; i < vec_factor; i++) {
                                            int iw = iw0 + i;
                                            gather_tmp[i] =
                                                (iw >= 0 && iw < in_width) ? in_row[iw]
                                                                          : bfloat16(0.0f);
                                        }
                                        in_vec = aie::load_v<vec_factor>(gather_tmp);
                                    }

                                    acc = aie::mac(acc, in_vec, w_vec);
                                }
                            }
                        }

                        aie::vector<bfloat16, vec_factor> out_vec =
                            acc.template to_vector<bfloat16>();
                        int out_off = oh * out_width + ow;
                        for (int i = 0; i < vec_factor; i++) {
                            out_ptr[out_off + i] = out_vec[i];
                        }
                    }
                }

                // OW tail and non-unit stride_w: scalar float accum.
                for (; ow < out_width; ow++) {
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;
                    float acc = apply_bias ? float(weight[w_only + oc]) : 0.0f;
                    if (apply_bias) {
                        (void)bias;
                    }

                    for (int ic = 0; ic < channels_per_group; ic++) {
                        int ic_global = ic_start + ic;
                        for (int kh = 0; kh < kernel_h; kh++) {
                            for (int kw = 0; kw < kernel_w; kw++) {
                                int ih = ih_start + kh;
                                int iw = iw_start + kw;
                                if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                    int input_idx =
                                        ((n * in_channels + ic_global) * in_height + ih) *
                                            in_width +
                                        iw;
                                    int weight_idx =
                                        ((oc * channels_per_group + ic) * kernel_h + kh) *
                                            kernel_w +
                                        kw;
                                    acc += float(input[input_idx]) * float(weight[weight_idx]);
                                }
                            }
                        }
                    }
                    out_ptr[oh * out_width + ow] = static_cast<bfloat16>(acc);
                }
            }
        }
    }

    event1();
}

/**
 * Depthwise Convolution Kernel - AIE2P optimized
 *
 * Same OW-dense pipeline as standard conv (stride_w==1 contiguous W loads),
 * one input channel per output channel.
 *
 * @param input - Input tensor [N, channels, in_height, in_width]
 * @param weight - Weight tensor [channels, kernel_h, kernel_w]
 * @param output - Output tensor [N, channels, out_height, out_width]
 * @param bias - Optional bias tensor [channels]
 */
void depthwise_conv2d_bf16_vector(bfloat16 *input,
                                  bfloat16 *weight,
                                  bfloat16 *output,
                                  bfloat16 *bias,
                                  int N,
                                  int channels,
                                  int in_height,
                                  int in_width,
                                  int out_height,
                                  int out_width,
                                  int kernel_h,
                                  int kernel_w,
                                  int stride_h,
                                  int stride_w,
                                  int pad_h,
                                  int pad_w,
                                  int apply_bias)
{
    constexpr int vec_factor = 16;

    event0();

    int spatial_size = out_height * out_width;
    const int w_only = channels * kernel_h * kernel_w;
    const aie::vector<bfloat16, vec_factor> ones =
        aie::broadcast<bfloat16, vec_factor>(bfloat16(1.0f));

    for (int n = 0; n < N; n++) {
        for (int c = 0; c < channels; c++) {
            bfloat16 *__restrict out_ptr = output + (n * channels + c) * spatial_size;
            const bfloat16 *__restrict in_ch =
                input + (n * channels + c) * in_height * in_width;
            const bfloat16 *__restrict w_c = weight + c * kernel_h * kernel_w;

            for (int oh = 0; oh < out_height; oh++) {
                int ih_base = oh * stride_h - pad_h;
                int ow = 0;

                if (stride_w == 1) {
                    for (; ow + vec_factor <= out_width; ow += vec_factor) {
                        aie::accum<accfloat, vec_factor> acc =
                            aie::zeros<accfloat, vec_factor>();

                        if (apply_bias) {
                            acc = aie::mac(
                                acc,
                                aie::broadcast<bfloat16, vec_factor>(weight[w_only + c]),
                                ones);
                            (void)bias;
                        }

                        for (int kh = 0; kh < kernel_h; kh++) {
                            int ih = ih_base + kh;
                            if (ih < 0 || ih >= in_height) {
                                continue;
                            }
                            const bfloat16 *__restrict in_row = in_ch + ih * in_width;

                            for (int kw = 0; kw < kernel_w; kw++) {
                                int iw0 = ow - pad_w + kw;
                                aie::vector<bfloat16, vec_factor> w_vec =
                                    aie::broadcast<bfloat16, vec_factor>(w_c[kh * kernel_w + kw]);
                                aie::vector<bfloat16, vec_factor> in_vec;

                                int iw_last = iw0 + vec_factor - 1;
                                // Avoid vector lane operator[] writes; gather via aligned tmp.
                                if (iw0 >= 0 && iw_last < in_width &&
                                    (iw0 & (vec_factor - 1)) == 0) {
                                    in_vec = aie::load_v<vec_factor>(in_row + iw0);
                                } else {
                                    alignas(32) bfloat16 gather_tmp[vec_factor];
                                    for (int i = 0; i < vec_factor; i++) {
                                        int iw = iw0 + i;
                                        gather_tmp[i] =
                                            (iw >= 0 && iw < in_width) ? in_row[iw]
                                                                      : bfloat16(0.0f);
                                    }
                                    in_vec = aie::load_v<vec_factor>(gather_tmp);
                                }

                                acc = aie::mac(acc, in_vec, w_vec);
                            }
                        }

                        aie::vector<bfloat16, vec_factor> out_vec =
                            acc.template to_vector<bfloat16>();
                        int out_off = oh * out_width + ow;
                        for (int i = 0; i < vec_factor; i++) {
                            out_ptr[out_off + i] = out_vec[i];
                        }
                    }
                }

                for (; ow < out_width; ow++) {
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;
                    float acc = apply_bias ? float(weight[w_only + c]) : 0.0f;
                    if (apply_bias) {
                        (void)bias;
                    }

                    for (int kh = 0; kh < kernel_h; kh++) {
                        for (int kw = 0; kw < kernel_w; kw++) {
                            int ih = ih_start + kh;
                            int iw = iw_start + kw;
                            if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                int input_idx =
                                    ((n * channels + c) * in_height + ih) * in_width + iw;
                                acc += float(input[input_idx]) * float(w_c[kh * kernel_w + kw]);
                            }
                        }
                    }
                    out_ptr[oh * out_width + ow] = static_cast<bfloat16>(acc);
                }
            }
        }
    }

    event1();
}

/**
 * Pointwise (1x1) Convolution — AIE2P dense path
 *
 * NCHW layout: channel planes are contiguous in H*W, IC is strided by spatial.
 * Dense strategy (no host re-layout): treat each OC as a channel-plane axpy
 * chain — contiguous `aie::load_v` over spatial, broadcast weight[oc, ic],
 * float accum via `aie::mac`, store vector. Tile a few OCs so one input
 * vector is reused (outer-product style), which is the NCHW-friendly dense
 * pipeline.
 *
 * @param input - Input tensor [N, in_channels, H, W]
 * @param weight - Weight tensor [out_channels, in_channels] (+ packed bias)
 * @param output - Output tensor [N, out_channels, H, W]
 * @param bias - Unused when bias is packed after weights
 */
void pointwise_conv2d_bf16_vector(bfloat16 *input,
                                  bfloat16 *weight,
                                  bfloat16 *output,
                                  bfloat16 *bias,
                                  int N,
                                  int in_channels,
                                  int out_channels,
                                  int height,
                                  int width,
                                  int apply_bias)
{
    // AIE2P: 16-lane bf16 vectors for contiguous spatial planes.
    constexpr int vec_factor = 16;
    // How many output channels share one input spatial load.
    constexpr int oc_tile = 4;

    event0();

    const int spatial_size = height * width;
    const int w_only = out_channels * in_channels;
    const aie::vector<bfloat16, vec_factor> ones =
        aie::broadcast<bfloat16, vec_factor>(bfloat16(1.0f));

    for (int n = 0; n < N; n++) {
        bfloat16 *__restrict in_n = input + n * in_channels * spatial_size;
        bfloat16 *__restrict out_n = output + n * out_channels * spatial_size;

        int oc = 0;
        for (; oc + oc_tile <= out_channels; oc += oc_tile) {
            const bfloat16 *__restrict w0 = weight + (oc + 0) * in_channels;
            const bfloat16 *__restrict w1 = weight + (oc + 1) * in_channels;
            const bfloat16 *__restrict w2 = weight + (oc + 2) * in_channels;
            const bfloat16 *__restrict w3 = weight + (oc + 3) * in_channels;
            bfloat16 *__restrict o0 = out_n + (oc + 0) * spatial_size;
            bfloat16 *__restrict o1 = out_n + (oc + 1) * spatial_size;
            bfloat16 *__restrict o2 = out_n + (oc + 2) * spatial_size;
            bfloat16 *__restrict o3 = out_n + (oc + 3) * spatial_size;

            int sp = 0;
            for (; sp + vec_factor <= spatial_size; sp += vec_factor) {
                aie::accum<accfloat, vec_factor> a0 = aie::zeros<accfloat, vec_factor>();
                aie::accum<accfloat, vec_factor> a1 = aie::zeros<accfloat, vec_factor>();
                aie::accum<accfloat, vec_factor> a2 = aie::zeros<accfloat, vec_factor>();
                aie::accum<accfloat, vec_factor> a3 = aie::zeros<accfloat, vec_factor>();

                if (apply_bias) {
                    a0 = aie::mac(a0,
                                  aie::broadcast<bfloat16, vec_factor>(weight[w_only + oc + 0]),
                                  ones);
                    a1 = aie::mac(a1,
                                  aie::broadcast<bfloat16, vec_factor>(weight[w_only + oc + 1]),
                                  ones);
                    a2 = aie::mac(a2,
                                  aie::broadcast<bfloat16, vec_factor>(weight[w_only + oc + 2]),
                                  ones);
                    a3 = aie::mac(a3,
                                  aie::broadcast<bfloat16, vec_factor>(weight[w_only + oc + 3]),
                                  ones);
                    (void)bias;
                }

                for (int ic = 0; ic < in_channels; ic++) {
                    aie::vector<bfloat16, vec_factor> in_vec =
                        aie::load_v<vec_factor>(in_n + ic * spatial_size + sp);
                    a0 = aie::mac(a0, in_vec, aie::broadcast<bfloat16, vec_factor>(w0[ic]));
                    a1 = aie::mac(a1, in_vec, aie::broadcast<bfloat16, vec_factor>(w1[ic]));
                    a2 = aie::mac(a2, in_vec, aie::broadcast<bfloat16, vec_factor>(w2[ic]));
                    a3 = aie::mac(a3, in_vec, aie::broadcast<bfloat16, vec_factor>(w3[ic]));
                }

                aie::store_v(o0 + sp, a0.template to_vector<bfloat16>());
                aie::store_v(o1 + sp, a1.template to_vector<bfloat16>());
                aie::store_v(o2 + sp, a2.template to_vector<bfloat16>());
                aie::store_v(o3 + sp, a3.template to_vector<bfloat16>());
            }

            // Spatial tail (H*W not multiple of vec_factor): scalar float accum.
            for (; sp < spatial_size; sp++) {
                float f0 = 0.0f, f1 = 0.0f, f2 = 0.0f, f3 = 0.0f;
                if (apply_bias) {
                    f0 = weight[w_only + oc + 0];
                    f1 = weight[w_only + oc + 1];
                    f2 = weight[w_only + oc + 2];
                    f3 = weight[w_only + oc + 3];
                    (void)bias;
                }
                for (int ic = 0; ic < in_channels; ic++) {
                    float x = in_n[ic * spatial_size + sp];
                    f0 += x * float(w0[ic]);
                    f1 += x * float(w1[ic]);
                    f2 += x * float(w2[ic]);
                    f3 += x * float(w3[ic]);
                }
                o0[sp] = static_cast<bfloat16>(f0);
                o1[sp] = static_cast<bfloat16>(f1);
                o2[sp] = static_cast<bfloat16>(f2);
                o3[sp] = static_cast<bfloat16>(f3);
            }
        }

        // Remainder OC (not multiple of oc_tile).
        for (; oc < out_channels; oc++) {
            const bfloat16 *__restrict w_row = weight + oc * in_channels;
            bfloat16 *__restrict out_ptr = out_n + oc * spatial_size;

            int sp = 0;
            for (; sp + vec_factor <= spatial_size; sp += vec_factor) {
                aie::accum<accfloat, vec_factor> acc = aie::zeros<accfloat, vec_factor>();
                if (apply_bias) {
                    acc = aie::mac(acc,
                                   aie::broadcast<bfloat16, vec_factor>(weight[w_only + oc]),
                                   ones);
                    (void)bias;
                }
                for (int ic = 0; ic < in_channels; ic++) {
                    aie::vector<bfloat16, vec_factor> in_vec =
                        aie::load_v<vec_factor>(in_n + ic * spatial_size + sp);
                    acc = aie::mac(acc, in_vec, aie::broadcast<bfloat16, vec_factor>(w_row[ic]));
                }
                aie::store_v(out_ptr + sp, acc.template to_vector<bfloat16>());
            }
            for (; sp < spatial_size; sp++) {
                float f = apply_bias ? float(weight[w_only + oc]) : 0.0f;
                if (apply_bias) {
                    (void)bias;
                }
                for (int ic = 0; ic < in_channels; ic++) {
                    f += float(in_n[ic * spatial_size + sp]) * float(w_row[ic]);
                }
                out_ptr[sp] = static_cast<bfloat16>(f);
            }
        }
    }

    event1();
}
} // extern "C"
