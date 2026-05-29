// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 2D MaxPool Kernel for AIE2P (NPU2)
// Enhanced version with larger vector operations

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <type_traits>

extern "C" {

/**
 * 2D MaxPool Kernel - Vectorized version for AIE2P
 * Uses 16-element vectors for better throughput
 *
 * @param input - Input tensor [N, channels, in_height, in_width] (flattened)
 * @param output - Output tensor [N, channels, out_height, out_width] (flattened)
 */
void max_pool2d_bf16_vector(bfloat16 *input,
                            bfloat16 *output,
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
    constexpr int vec_factor = 16; // AIE2P enhanced vector factor

    event0();

    int spatial_size = out_height * out_width;
    int kernel_size = kernel_h * kernel_w;

    for (int n = 0; n < N; n++) {
        for (int c = 0; c < channels; c++) {
            bfloat16 *output_channel_ptr = output + (n * channels + c) * spatial_size;

            for (int oh = 0; oh < out_height; oh++) {
                for (int ow = 0; ow < out_width; ow++) {
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;

                    bfloat16 max_val = bfloat16(-INFINITY);

                    // Vectorized max over kernel elements
                    const int V = kernel_size / vec_factor;
                    for (int v = 0; v < V; v++) {
                        aie::vector<bfloat16, vec_factor> in_vec;

                        for (int i = 0; i < vec_factor; i++) {
                            int kh = (v * vec_factor + i) / kernel_w;
                            int kw = (v * vec_factor + i) % kernel_w;
                            int ih = ih_start + kh;
                            int iw = iw_start + kw;

                            if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                int input_idx = ((n * channels + c) * in_height + ih) * in_width + iw;
                                in_vec[i] = input[input_idx];
                            } else {
                                in_vec[i] = bfloat16(-INFINITY);
                            }
                        }

                        // Vector max reduction using AIE2P capabilities
                        for (int i = 0; i < vec_factor; i++) {
                            if (in_vec[i] > max_val) {
                                max_val = in_vec[i];
                            }
                        }
                    }

                    // Handle remainder kernel elements
                    for (int i = V * vec_factor; i < kernel_size; i++) {
                        int kh = i / kernel_w;
                        int kw = i % kernel_w;
                        int ih = ih_start + kh;
                        int iw = iw_start + kw;

                        if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                            int input_idx = ((n * channels + c) * in_height + ih) * in_width + iw;
                            bfloat16 input_val = input[input_idx];
                            if (input_val > max_val) {
                                max_val = input_val;
                            }
                        }
                    }

                    int out_idx = oh * out_width + ow;
                    output_channel_ptr[out_idx] = max_val;
                }
            }
        }
    }

    event1();
}
} // end extern "C" for C-linkage kernels (fix for symbol resolution in aiecc link, matching reduction.cc fix)
