// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 2D Convolution Kernel for AIE2P (NPU2)
// Enhanced version with larger vector operations and better parallelization

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
// aie_bf16.hpp not required (bfloat16 support is in aie.hpp for this toolchain)
#include <stdint.h>
#include <stdio.h>
#include <type_traits>

extern "C" {

/**
 * 2D Convolution Kernel - AIE2P optimized
 * Uses larger vector factor (16) for AIE2P's enhanced capabilities
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
                        int groups)
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

                    if (bias != NULL) {
                        acc += bias[oc];
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
 * Uses 16-element vectors for better throughput
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
                        int groups)
{
    constexpr int vec_factor = 16; // AIE2P supports larger vectors

    event0();

    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;
    int spatial_size = out_height * out_width;

    for (int n = 0; n < N; n++) {
        for (int oc = 0; oc < out_channels; oc++) {
            int group_id = oc / out_channels_per_group;
            int ic_start = group_id * channels_per_group;

            bfloat16 *output_channel_ptr = output + (n * out_channels + oc) * spatial_size;

            for (int oh = 0; oh < out_height; oh++) {
                for (int ow = 0; ow < out_width; ow++) {
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;

                    bfloat16 acc = bfloat16(0.0f);

                    // Vectorized accumulation over input channels
                    const int V = channels_per_group / vec_factor;
                    for (int v = 0; v < V; v++) {
                        aie::accum<accfloat, vec_factor> acc_vec = aie::zeros<accfloat, vec_factor>();

                        for (int kh = 0; kh < kernel_h; kh++) {
                            for (int kw = 0; kw < kernel_w; kw++) {
                                int ih = ih_start + kh;
                                int iw = iw_start + kw;

                                if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                    // Load vector of input values
                                    aie::vector<bfloat16, vec_factor> in_vec;
                                    aie::vector<bfloat16, vec_factor> w_vec;

                                    for (int i = 0; i < vec_factor; i++) {
                                        int ic = v * vec_factor + i;
                                        int ic_global = ic_start + ic;
                                        int input_idx =
                                            ((n * in_channels + ic_global) * in_height + ih) * in_width + iw;
                                        int weight_idx =
                                            ((oc * channels_per_group + ic) * kernel_h + kh) * kernel_w + kw;

                                        in_vec[i] = input[input_idx];
                                        w_vec[i] = weight[weight_idx];
                                    }

                                    acc_vec = aie::mac(acc_vec, in_vec, w_vec);
                                }
                            }
                        }

                        acc += static_cast<bfloat16>(aie::reduce_add(acc_vec.template to_vector<float>()));
                    }

                    // Handle remainder channels
                    for (int ic = V * vec_factor; ic < channels_per_group; ic++) {
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

                    if (bias != NULL) {
                        acc += bias[oc];
                    }

                    int out_idx = oh * out_width + ow;
                    output_channel_ptr[out_idx] = acc;
                }
            }
        }
    }

    event1();
}

/**
 * Depthwise Convolution Kernel - AIE2P optimized
 * Each output channel depends only on one input channel
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
                                  int pad_w)
{
    constexpr int vec_factor = 16;

    event0();

    int spatial_size = out_height * out_width;

    for (int n = 0; n < N; n++) {
        for (int c = 0; c < channels; c++) {
            bfloat16 *output_channel_ptr = output + (n * channels + c) * spatial_size;

            for (int oh = 0; oh < out_height; oh++) {
                for (int ow = 0; ow < out_width; ow++) {
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;

                    bfloat16 acc = bfloat16(0.0f);

                    // Vectorized kernel accumulation
                    const int V = (kernel_h * kernel_w) / vec_factor;
                    for (int v = 0; v < V; v++) {
                        aie::vector<bfloat16, vec_factor> in_vec, w_vec;

                        for (int i = 0; i < vec_factor; i++) {
                            int kh = (v * vec_factor + i) / kernel_w;
                            int kw = (v * vec_factor + i) % kernel_w;
                            int ih = ih_start + kh;
                            int iw = iw_start + kw;

                            if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                int input_idx = ((n * channels + c) * in_height + ih) * in_width + iw;
                                int weight_idx = (c * kernel_h + kh) * kernel_w + kw;
                                in_vec[i] = input[input_idx];
                                w_vec[i] = weight[weight_idx];
                            } else {
                                in_vec[i] = bfloat16(0.0f);
                                w_vec[i] = bfloat16(0.0f);
                            }
                        }

                        acc += static_cast<bfloat16>(aie::reduce_add(aie::mul(in_vec, w_vec).to_vector<float>()));
                    }

                    // Handle remainder
                    for (int i = V * vec_factor; i < kernel_h * kernel_w; i++) {
                        int kh = i / kernel_w;
                        int kw = i % kernel_w;
                        int ih = ih_start + kh;
                        int iw = iw_start + kw;

                        if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                            int input_idx = ((n * channels + c) * in_height + ih) * in_width + iw;
                            int weight_idx = (c * kernel_h + kh) * kernel_w + kw;
                            acc += input[input_idx] * weight[weight_idx];
                        }
                    }

                    if (bias != NULL) {
                        acc += bias[c];
                    }

                    int out_idx = oh * out_width + ow;
                    output_channel_ptr[out_idx] = acc;
                }
            }
        }
    }

    event1();
}

/**
 * Pointwise (1x1) Convolution Kernel - AIE2P optimized
 * This is essentially a matrix multiplication per spatial location
 * Uses GEMM-like approach for efficiency
 *
 * @param input - Input tensor [N, in_channels, H, W]
 * @param weight - Weight tensor [out_channels, in_channels]
 * @param output - Output tensor [N, out_channels, H, W]
 * @param bias - Optional bias tensor [out_channels]
 */
void pointwise_conv2d_bf16_vector(bfloat16 *input,
                                  bfloat16 *weight,
                                  bfloat16 *output,
                                  bfloat16 *bias,
                                  int N,
                                  int in_channels,
                                  int out_channels,
                                  int height,
                                  int width)
{
    constexpr int vec_factor = 16;

    event0();

    int spatial_size = height * width;

    for (int n = 0; n < N; n++) {
        for (int oc = 0; oc < out_channels; oc++) {
            bfloat16 *output_channel_ptr = output + (n * out_channels + oc) * spatial_size;

            for (int sp = 0; sp < spatial_size; sp++) {
                bfloat16 acc = bfloat16(0.0f);

                // Vectorized dot product
                const int V = in_channels / vec_factor;
                for (int v = 0; v < V; v++) {
                    aie::vector<bfloat16, vec_factor> in_vec, w_vec;

                    for (int i = 0; i < vec_factor; i++) {
                        int ic = v * vec_factor + i;
                        in_vec[i] = input[((n * in_channels + ic) * height * width) + sp];
                        w_vec[i] = weight[oc * in_channels + ic];
                    }

                    acc += static_cast<bfloat16>(aie::reduce_add(aie::mul(in_vec, w_vec).to_vector<float>()));
                }

                // Handle remainder
                for (int ic = V * vec_factor; ic < in_channels; ic++) {
                    acc += input[((n * in_channels + ic) * height * width) + sp] * weight[oc * in_channels + ic];
                }

                if (bias != NULL) {
                    acc += bias[oc];
                }

                output_channel_ptr[sp] = acc;
            }
        }
    }

    event1();
}
} // end extern "C" for C-linkage kernels (fix for symbol resolution in aiecc link, matching reduction.cc fix)
