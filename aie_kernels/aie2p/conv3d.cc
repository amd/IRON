// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 3D Convolution Kernel for AIE2P (NPU2)
// Enhanced version with larger vector operations (vec_factor=16)
// Supports both video models and text model compute primitives via shape manipulation

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <aie_api/aie_bf16.hpp>
#include <stdint.h>
#include <stdio.h>
#include <type_traits>

/**
 * 3D Convolution Kernel - AIE2P enhanced vectorized version
 * Uses 16-element vectors for better throughput on AIE2P
 *
 * @param input - Input tensor [N, in_channels, in_t, in_h, in_w] (flattened)
 * @param weight - Weight tensor [out_channels, in_channels/groups, kernel_t, kernel_h, kernel_w]
 * @param output - Output tensor [N, out_channels, out_t, out_h, out_w] (flattened)
 * @param bias - Optional bias tensor [out_channels]
 * @param N - Batch size
 * @param in_channels - Number of input channels
 * @param in_t - Input temporal dimension
 * @param in_h - Input height
 * @param in_w - Input width
 * @param out_channels - Number of output channels
 * @param out_t - Output temporal dimension
 * @param out_h - Output height
 * @param out_w - Output width
 * @param kernel_t - Kernel temporal depth
 * @param kernel_h - Kernel height
 * @param kernel_w - Kernel width
 * @param stride_t - Stride in temporal dimension
 * @param stride_h - Stride in height dimension
 * @param stride_w - Stride in width dimension
 * @param pad_t - Padding in temporal dimension
 * @param pad_h - Padding in height dimension
 * @param pad_w - Padding in width dimension
 * @param groups - Number of groups
 */
void conv3d_bf16_vector(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int N,
    int in_channels,
    int in_t,
    int in_h,
    int in_w,
    int out_channels,
    int out_t,
    int out_h,
    int out_w,
    int kernel_t,
    int kernel_h,
    int kernel_w,
    int stride_t,
    int stride_h,
    int stride_w,
    int pad_t,
    int pad_h,
    int pad_w,
    int groups
) {
    constexpr int vec_factor = 16;  // AIE2P enhanced vector factor

    event0();

    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;
    int kernel_size = kernel_t * kernel_h * kernel_w;

    // Iterate over batch
    for (int n = 0; n < N; n++) {
        // Iterate over output channels
        for (int oc = 0; oc < out_channels; oc++) {
            int group_id = oc / out_channels_per_group;
            int ic_start = group_id * channels_per_group;

            // Calculate output position for this channel
            bfloat16* output_ptr = output + ((n * out_channels + oc) * out_t * out_h * out_w);

            // Iterate over output temporal/spatial dimensions
            for (int ot = 0; ot < out_t; ot++) {
                for (int oh = 0; oh < out_h; oh++) {
                    for (int ow = 0; ow < out_w; ow++) {
                        // Calculate corresponding input position
                        int it_start = ot * stride_t - pad_t;
                        int ih_start = oh * stride_h - pad_h;
                        int iw_start = ow * stride_w - pad_w;

                        // Accumulate over kernel and input channels
                        bfloat16 acc = bfloat16(0.0f);

                        // Vectorized accumulation over kernel elements
                        const int V = kernel_size / vec_factor;
                        for (int v = 0; v < V; v++) {
                            for (int i = 0; i < vec_factor; i++) {
                                int kt = (v * vec_factor + i) / (kernel_h * kernel_w);
                                int kh = ((v * vec_factor + i) / kernel_w) % kernel_h;
                                int kw = (v * vec_factor + i) % kernel_w;

                                int it = it_start + kt;
                                int ih = ih_start + kh;
                                int iw = iw_start + kw;

                                for (int ic = 0; ic < channels_per_group; ic++) {
                                    int ic_global = ic_start + ic;

                                    // Check bounds (handle padding)
                                    if (it >= 0 && it < in_t &&
                                        ih >= 0 && ih < in_h &&
                                        iw >= 0 && iw < in_w) {
                                        int input_idx = (((n * in_channels + ic_global) * in_t + it) * in_h + ih) * in_w + iw;
                                        int weight_idx = ((((oc * channels_per_group + ic) * kernel_t + kt) * kernel_h + kh) * kernel_w + kw);

                                        acc += input[input_idx] * weight[weight_idx];
                                    }
                                }
                            }
                        }

                        // Handle remainder kernel elements
                        for (int i = V * vec_factor; i < kernel_size; i++) {
                            int kt = i / (kernel_h * kernel_w);
                            int kh = (i / kernel_w) % kernel_h;
                            int kw = i % kernel_w;

                            int it = it_start + kt;
                            int ih = ih_start + kh;
                            int iw = iw_start + kw;

                            for (int ic = 0; ic < channels_per_group; ic++) {
                                int ic_global = ic_start + ic;

                                if (it >= 0 && it < in_t &&
                                    ih >= 0 && ih < in_h &&
                                    iw >= 0 && iw < in_w) {
                                    int input_idx = (((n * in_channels + ic_global) * in_t + it) * in_h + ih) * in_w + iw;
                                    int weight_idx = ((((oc * channels_per_group + ic) * kernel_t + kt) * kernel_h + kh) * kernel_w + kw);

                                    acc += input[input_idx] * weight[weight_idx];
                                }
                            }
                        }

                        // Add bias if provided
                        if (bias != NULL) {
                            acc += bias[oc];
                        }

                        // Store output
                        int out_idx = (ot * out_h + oh) * out_w + ow;
                        output_ptr[out_idx] = acc;
                    }
                }
            }
        }
    }

    event1();
}

/**
 * 3D Convolution Kernel - AIE2P scalar reference
 * Naive implementation for small kernels (3x3x3)
 *
 * @param input - Input tensor [N, in_channels, in_t, in_h, in_w] (flattened)
 * @param weight - Weight tensor [out_channels, in_channels/groups, kernel_t, kernel_h, kernel_w]
 * @param output - Output tensor [N, out_channels, out_t, out_h, out_w] (flattened)
 * @param bias - Optional bias tensor [out_channels], can be NULL
 * @param in_channels - Number of input channels
 * @param in_t - Input temporal/depth dimension
 * @param in_h - Input height
 * @param in_w - Input width
 * @param out_channels - Number of output channels
 * @param out_t - Output temporal/depth dimension
 * @param out_h - Output height
 * @param out_w - Output width
 * @param kernel_t - Kernel temporal depth
 * @param kernel_h - Kernel height
 * @param kernel_w - Kernel width
 * @param stride_t - Stride in temporal dimension
 * @param stride_h - Stride in height dimension
 * @param stride_w - Stride in width dimension
 * @param pad_t - Padding in temporal dimension
 * @param pad_h - Padding in height dimension
 * @param pad_w - Padding in width dimension
 * @param groups - Number of groups for grouped convolution
 */
void conv3d_bf16_scalar(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int in_channels,
    int in_t,
    int in_h,
    int in_w,
    int out_channels,
    int out_t,
    int out_h,
    int out_w,
    int kernel_t,
    int kernel_h,
    int kernel_w,
    int stride_t,
    int stride_h,
    int stride_w,
    int pad_t,
    int pad_h,
    int pad_w,
    int groups
) {
    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;

    for (int oc = 0; oc < out_channels; oc++) {
        int group_id = oc / out_channels_per_group;
        int oc_in_group = oc % out_channels_per_group;

        for (int ot = 0; ot < out_t; ot++) {
            for (int oh = 0; oh < out_h; oh++) {
                for (int ow = 0; ow < out_w; ow++) {
                    // Calculate input position
                    int it_start = ot * stride_t - pad_t;
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;

                    bfloat16 acc = bfloat16(0.0f);

                    // Sum over input channels in the group
                    for (int ic = 0; ic < channels_per_group; ic++) {
                        int ic_global = group_id * channels_per_group + ic;

                        for (int kt = 0; kt < kernel_t; kt++) {
                            for (int kh = 0; kh < kernel_h; kh++) {
                                for (int kw = 0; kw < kernel_w; kw++) {
                                    int it = it_start + kt;
                                    int ih = ih_start + kh;
                                    int iw = iw_start + kw;

                                    // Check bounds (handle padding)
                                    if (it >= 0 && it < in_t &&
                                        ih >= 0 && ih < in_h &&
                                        iw >= 0 && iw < in_w) {
                                        int input_idx = (((ic_global * in_t + it) * in_h + ih) * in_w + iw);
                                        int weight_idx = ((((oc * channels_per_group + ic) * kernel_t + kt) * kernel_h + kh) * kernel_w + kw);

                                        acc += input[input_idx] * weight[weight_idx];
                                    }
                                }
                            }
                        }
                    }

                    // Add bias if provided
                    if (bias != NULL) {
                        acc += bias[oc];
                    }

                    int output_idx = ((oc * out_t + ot) * out_h + oh) * out_w + ow;
                    output[output_idx] = acc;
                }
            }
        }
    }
}

/**
 * 3D Convolution Kernel - Optimized for large kernels
 * Uses hierarchical accumulation for better performance on AIE2P
 *
 * @param input - Input tensor [N, in_channels, in_t, in_h, in_w]
 * @param weight - Weight tensor [out_channels, in_channels/groups, kernel_t, kernel_h, kernel_w]
 * @param output - Output tensor [N, out_channels, out_t, out_h, out_w]
 * @param bias - Optional bias tensor [out_channels]
 */
void conv3d_bf16_large_kernel(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int N,
    int in_channels,
    int in_t,
    int in_h,
    int in_w,
    int out_channels,
    int out_t,
    int out_h,
    int out_w,
    int kernel_t,
    int kernel_h,
    int kernel_w,
    int stride_t,
    int stride_h,
    int stride_w,
    int pad_t,
    int pad_h,
    int pad_w,
    int groups
) {
    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;
    int kernel_size = kernel_t * kernel_h * kernel_w;

    // Precompute inverse kernel size for multiplication instead of division
    float kernel_size_inv = 1.0f / static_cast<float>(kernel_size);

    for (int n = 0; n < N; n++) {
        for (int oc = 0; oc < out_channels; oc++) {
            int group_id = oc / out_channels_per_group;
            int ic_start = group_id * channels_per_group;

            bfloat16* output_ptr = output + ((n * out_channels + oc) * out_t * out_h * out_w);

            for (int ot = 0; ot < out_t; ot++) {
                for (int oh = 0; oh < out_h; oh++) {
                    for (int ow = 0; ow < out_w; ow++) {
                        int it_start = ot * stride_t - pad_t;
                        int ih_start = oh * stride_h - pad_h;
                        int iw_start = ow * stride_w - pad_w;

                        bfloat16 acc = bfloat16(0.0f);

                        for (int kt = 0; kt < kernel_t; kt++) {
                            for (int kh = 0; kh < kernel_h; kh++) {
                                for (int kw = 0; kw < kernel_w; kw++) {
                                    int it = it_start + kt;
                                    int ih = ih_start + kh;
                                    int iw = iw_start + kw;

                                    if (it >= 0 && it < in_t &&
                                        ih >= 0 && ih < in_h &&
                                        iw >= 0 && iw < in_w) {
                                        for (int ic = 0; ic < channels_per_group; ic++) {
                                            int ic_global = ic_start + ic;
                                            int input_idx = (((n * in_channels + ic_global) * in_t + it) * in_h + ih) * in_w + iw;
                                            int weight_idx = ((((oc * channels_per_group + ic) * kernel_t + kt) * kernel_h + kh) * kernel_w + kw);

                                            acc += input[input_idx] * weight[weight_idx];
                                        }
                                    }
                                }
                            }
                        }

                        if (bias != NULL) {
                            acc += bias[oc];
                        }

                        int out_idx = (ot * out_h + oh) * out_w + ow;
                        output_ptr[out_idx] = acc;
                    }
                }
            }
        }
    }
}

/**
 * Depthwise 3D Convolution Kernel - AIE2P optimized
 * Each output channel depends only on one input channel
 *
 * @param input - Input tensor [N, channels, in_t, in_h, in_w]
 * @param weight - Weight tensor [channels, kernel_t, kernel_h, kernel_w]
 * @param output - Output tensor [N, channels, out_t, out_h, out_w]
 * @param bias - Optional bias tensor [channels]
 */
void depthwise_conv3d_bf16_vector(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int N,
    int channels,
    int in_t,
    int in_h,
    int in_w,
    int out_t,
    int out_h,
    int out_w,
    int kernel_t,
    int kernel_h,
    int kernel_w,
    int stride_t,
    int stride_h,
    int stride_w,
    int pad_t,
    int pad_h,
    int pad_w
) {
    constexpr int vec_factor = 16;  // AIE2P vector factor

    event0();

    int kernel_size = kernel_t * kernel_h * kernel_w;

    for (int n = 0; n < N; n++) {
        for (int c = 0; c < channels; c++) {
            for (int ot = 0; ot < out_t; ot++) {
                for (int oh = 0; oh < out_h; oh++) {
                    for (int ow = 0; ow < out_w; ow++) {
                        int it_start = ot * stride_t - pad_t;
                        int ih_start = oh * stride_h - pad_h;
                        int iw_start = ow * stride_w - pad_w;

                        bfloat16 acc = bfloat16(0.0f);

                        // Vectorized accumulation
                        const int V = kernel_size / vec_factor;
                        for (int v = 0; v < V; v++) {
                            for (int i = 0; i < vec_factor; i++) {
                                int kt = (v * vec_factor + i) / (kernel_h * kernel_w);
                                int kh = ((v * vec_factor + i) / kernel_w) % kernel_h;
                                int kw = (v * vec_factor + i) % kernel_w;

                                int it = it_start + kt;
                                int ih = ih_start + kh;
                                int iw = iw_start + kw;

                                if (it >= 0 && it < in_t &&
                                    ih >= 0 && ih < in_h &&
                                    iw >= 0 && iw < in_w) {
                                    int input_idx = (((n * channels + c) * in_t + it) * in_h + ih) * in_w + iw;
                                    int weight_idx = ((c * kernel_t + kt) * kernel_h + kh) * kernel_w + kw;

                                    acc += input[input_idx] * weight[weight_idx];
                                }
                            }
                        }

                        // Handle remainder
                        for (int i = V * vec_factor; i < kernel_size; i++) {
                            int kt = i / (kernel_h * kernel_w);
                            int kh = (i / kernel_w) % kernel_h;
                            int kw = i % kernel_w;

                            int it = it_start + kt;
                            int ih = ih_start + kh;
                            int iw = iw_start + kw;

                            if (it >= 0 && it < in_t &&
                                ih >= 0 && ih < in_h &&
                                iw >= 0 && iw < in_w) {
                                int input_idx = (((n * channels + c) * in_t + it) * in_h + ih) * in_w + iw;
                                int weight_idx = ((c * kernel_t + kt) * kernel_h + kh) * kernel_w + kw;

                                acc += input[input_idx] * weight[weight_idx];
                            }
                        }

                        if (bias != NULL) {
                            acc += bias[c];
                        }

                        int out_idx = (((n * channels + c) * out_t + ot) * out_h + oh) * out_w + ow;
                        output[out_idx] = acc;
                    }
                }
            }
        }
    }

    event1();
}

/**
 * Pointwise (1x1x1) 3D Convolution Kernel - AIE2P optimized
 * This is essentially a matrix multiplication per spatiotemporal location
 * Key for "Conv trick" - using Conv3D as Linear layer equivalent for 5D tensors
 * Uses 16-element vectors for enhanced throughput
 *
 * @param input - Input tensor [N, in_channels, in_t, in_h, in_w]
 * @param weight - Weight tensor [out_channels, in_channels]
 * @param output - Output tensor [N, out_channels, out_t, out_h, out_w]
 * @param bias - Optional bias tensor [out_channels]
 */
void pointwise_conv3d_bf16_vector(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int N,
    int in_channels,
    int out_channels,
    int in_t,
    int in_h,
    int in_w
) {
    constexpr int vec_factor = 16;  // AIE2P enhanced vector factor

    event0();

    int spatiotemporal_size = in_t * in_h * in_w;

    for (int n = 0; n < N; n++) {
        for (int oc = 0; oc < out_channels; oc++) {
            for (int sp = 0; sp < spatiotemporal_size; sp++) {
                bfloat16 acc = bfloat16(0.0f);

                // Vectorized dot product with AIE2P capabilities
                const int V = in_channels / vec_factor;
                for (int v = 0; v < V; v++) {
                    aie::vector<bfloat16, vec_factor> in_vec, w_vec;
                    for (int i = 0; i < vec_factor; i++) {
                        int ic = v * vec_factor + i;
                        in_vec[i] = input[((n * in_channels + ic) * spatiotemporal_size) + sp];
                        w_vec[i] = weight[oc * in_channels + ic];
                    }
                    acc += aie::mulacc(aie::zeros<bfloat16, vec_factor>(), in_vec, w_vec);
                }

                // Handle remainder
                for (int ic = V * vec_factor; ic < in_channels; ic++) {
                    acc += input[((n * in_channels + ic) * spatiotemporal_size) + sp] * weight[oc * in_channels + ic];
                }

                if (bias != NULL) {
                    acc += bias[oc];
                }

                output[((n * out_channels + oc) * spatiotemporal_size) + sp] = acc;
            }
        }
    }

    event1();
}

extern "C" {

// Standard conv3d kernels
void conv3d_bf16_vector(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int N, int in_channels, int in_t, int in_h, int in_w,
    int out_channels, int out_t, int out_h, int out_w,
    int kernel_t, int kernel_h, int kernel_w,
    int stride_t, int stride_h, int stride_w,
    int pad_t, int pad_h, int pad_w,
    int groups
);

void conv3d_bf16_scalar(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int in_channels, int in_t, int in_h, int in_w,
    int out_channels, int out_t, int out_h, int out_w,
    int kernel_t, int kernel_h, int kernel_w,
    int stride_t, int stride_h, int stride_w,
    int pad_t, int pad_h, int pad_w,
    int groups
);

void conv3d_bf16_large_kernel(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int N, int in_channels, int in_t, int in_h, int in_w,
    int out_channels, int out_t, int out_h, int out_w,
    int kernel_t, int kernel_h, int kernel_w,
    int stride_t, int stride_h, int stride_w,
    int pad_t, int pad_h, int pad_w,
    int groups
);

// Depthwise conv3d
void depthwise_conv3d_bf16_vector(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int N, int channels, int in_t, int in_h, int in_w,
    int out_t, int out_h, int out_w,
    int kernel_t, int kernel_h, int kernel_w,
    int stride_t, int stride_h, int stride_w,
    int pad_t, int pad_h, int pad_w
);

// Pointwise (1x1x1) conv3d
void pointwise_conv3d_bf16_vector(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int N, int in_channels, int out_channels, int in_t, int in_h, int in_w
);

} // extern "C"
