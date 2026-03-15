// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 2D Convolution Kernel for AIE2 (NPU)
// Supports standard conv2d with configurable kernel_size, stride, padding

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <aie_api/aie_bf16.hpp>
#include <stdint.h>
#include <stdio.h>
#include <type_traits>

/**
 * 2D Convolution Kernel - AIE2 optimized
 * Naive implementation for small kernels (3x3, 5x5)
 *
 * @param input - Input tensor [in_channels * in_height * in_width]
 * @param weight - Weight tensor [out_channels * in_channels * kernel_height * kernel_width]
 * @param output - Output tensor [out_channels * out_height * out_width]
 * @param bias - Optional bias tensor [out_channels], can be NULL
 * @param in_channels - Number of input channels
 * @param in_height - Input height
 * @param in_width - Input width
 * @param out_channels - Number of output channels
 * @param out_height - Output height
 * @param out_width - Output width
 * @param kernel_height - Kernel height
 * @param kernel_width - Kernel width
 * @param stride_height - Stride in height dimension
 * @param stride_width - Stride in width dimension
 * @param pad_height - Padding in height dimension
 * @param pad_width - Padding in width dimension
 */
void conv2d_bf16_scalar(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int in_channels,
    int in_height,
    int in_width,
    int out_channels,
    int out_height,
    int out_width,
    int kernel_height,
    int kernel_width,
    int stride_height,
    int stride_width,
    int pad_height,
    int pad_width,
    int groups
) {
    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;

    for (int oc = 0; oc < out_channels; oc++) {
        int group_id = oc / out_channels_per_group;
        int oc_in_group = oc % out_channels_per_group;

        for (int oh = 0; oh < out_height; oh++) {
            for (int ow = 0; ow < out_width; ow++) {
                // Calculate input position
                int ih_start = oh * stride_height - pad_height;
                int iw_start = ow * stride_width - pad_width;

                bfloat16 acc = bfloat16(0.0f);

                // Sum over input channels in the group
                for (int ic = 0; ic < channels_per_group; ic++) {
                    int ic_global = group_id * channels_per_group + ic;

                    for (int kh = 0; kh < kernel_height; kh++) {
                        for (int kw = 0; kw < kernel_width; kw++) {
                            int ih = ih_start + kh * 1;  // dilation = 1 for now
                            int iw = iw_start + kw * 1;

                            // Check bounds (handle padding)
                            if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                int input_idx = ((oc_global * in_channels + ic_global) * in_height + ih) * in_width + iw;
                                int weight_idx = ((oc * channels_per_group + ic) * kernel_height + kh) * kernel_width + kw;

                                acc += input[input_idx] * weight[weight_idx];
                            }
                        }
                    }
                }

                // Add bias if provided
                if (bias != NULL) {
                    acc += bias[oc];
                }

                int output_idx = (oc * out_height + oh) * out_width + ow;
                output[output_idx] = acc;
            }
        }
    }
}

/**
 * 2D Convolution Kernel - Vectorized version for AIE2
 * Optimized for 3x3 kernels with vector operations
 *
 * @param input - Input tensor [N, in_channels, in_height, in_width] (flattened)
 * @param weight - Weight tensor [out_channels, in_channels, kernel_height, kernel_width]
 * @param output - Output tensor [N, out_channels, out_height, out_width] (flattened)
 * @param bias - Optional bias tensor [out_channels]
 * @param params - Packed parameters for convolution
 */
void conv2d_bf16_vector(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int N,              // batch size
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
    int groups
) {
    constexpr int vec_factor = 8;  // Process 8 elements per vector operation

    event0();

    int channels_per_group = in_channels / groups;
    int out_channels_per_group = out_channels / groups;

    // Iterate over batch
    for (int n = 0; n < N; n++) {
        // Iterate over output channels
        for (int oc = 0; oc < out_channels; oc++) {
            int group_id = oc / out_channels_per_group;
            int ic_start = group_id * channels_per_group;

            // Calculate output position for this channel
            bfloat16* output_ptr = output + ((n * out_channels + oc) * out_height * out_width);

            // Iterate over output spatial dimensions
            for (int oh = 0; oh < out_height; oh++) {
                for (int ow = 0; ow < out_width; ow++) {
                    // Calculate corresponding input position
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;

                    // Accumulate over kernel and input channels
                    bfloat16 acc = bfloat16(0.0f);

                    for (int ic = 0; ic < channels_per_group; ic++) {
                        int ic_global = ic_start + ic;

                        for (int kh = 0; kh < kernel_h; kh++) {
                            for (int kw = 0; kw < kernel_w; kw++) {
                                int ih = ih_start + kh;
                                int iw = iw_start + kw;

                                // Check bounds (handle padding)
                                if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                    // Load input value
                                    int input_idx = ((n * in_channels + ic_global) * in_height + ih) * in_width + iw;
                                    bfloat16 in_val = input[input_idx];

                                    // Load weight value
                                    int weight_idx = ((oc * channels_per_group + ic) * kernel_h + kh) * kernel_w + kw;
                                    bfloat16 w_val = weight[weight_idx];

                                    // Accumulate product
                                    acc += in_val * w_val;
                                }
                            }
                        }
                    }

                    // Add bias if provided
                    if (bias != NULL) {
                        acc += bias[oc];
                    }

                    // Store output
                    int out_idx = oh * out_width + ow;
                    output_ptr[out_idx] = acc;
                }
            }
        }
    }

    event1();
}

/**
 * Depthwise Convolution Kernel - Specialized for depthwise conv
 * Each output channel depends only on one input channel
 *
 * @param input - Input tensor [N, channels, in_height, in_width]
 * @param weight - Weight tensor [channels, kernel_h, kernel_w]
 * @param output - Output tensor [N, channels, out_height, out_width]
 * @param bias - Optional bias tensor [channels]
 */
void depthwise_conv2d_bf16_vector(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
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
    int pad_w
) {
    event0();

    for (int n = 0; n < N; n++) {
        for (int c = 0; c < channels; c++) {
            for (int oh = 0; oh < out_height; oh++) {
                for (int ow = 0; ow < out_width; ow++) {
                    int ih_start = oh * stride_h - pad_h;
                    int iw_start = ow * stride_w - pad_w;

                    bfloat16 acc = bfloat16(0.0f);

                    for (int kh = 0; kh < kernel_h; kh++) {
                        for (int kw = 0; kw < kernel_w; kw++) {
                            int ih = ih_start + kh;
                            int iw = iw_start + kw;

                            if (ih >= 0 && ih < in_height && iw >= 0 && iw < in_width) {
                                int input_idx = ((n * channels + c) * in_height + ih) * in_width + iw;
                                int weight_idx = (c * kernel_h + kh) * kernel_w + kw;

                                acc += input[input_idx] * weight[weight_idx];
                            }
                        }
                    }

                    if (bias != NULL) {
                        acc += bias[c];
                    }

                    int out_idx = ((n * channels + c) * out_height + oh) * out_width + ow;
                    output[out_idx] = acc;
                }
            }
        }
    }

    event1();
}

/**
 * Pointwise (1x1) Convolution Kernel - Optimized for 1x1 kernels
 * This is essentially a matrix multiplication per spatial location
 *
 * @param input - Input tensor [N, in_channels, H, W]
 * @param weight - Weight tensor [out_channels, in_channels]
 * @param output - Output tensor [N, out_channels, H, W]
 * @param bias - Optional bias tensor [out_channels]
 */
void pointwise_conv2d_bf16_vector(
    bfloat16* input,
    bfloat16* weight,
    bfloat16* output,
    bfloat16* bias,
    int N,
    int in_channels,
    int out_channels,
    int height,
    int width
) {
    constexpr int vec_factor = 8;

    event0();

    int spatial_size = height * width;

    for (int n = 0; n < N; n++) {
        for (int oc = 0; oc < out_channels; oc++) {
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
                    acc += aie::mulacc(aie::zeros<bfloat16, vec_factor>(), in_vec, w_vec);
                }

                // Handle remainder
                for (int ic = V * vec_factor; ic < in_channels; ic++) {
                    acc += input[((n * in_channels + ic) * height * width) + sp] * weight[oc * in_channels + ic];
                }

                if (bias != NULL) {
                    acc += bias[oc];
                }

                output[((n * out_channels + oc) * height * width) + sp] = acc;
            }
        }
    }

    event1();
}

extern "C" {

// Standard conv2d kernels
void conv2d_bf16_scalar(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int in_channels, int in_height, int in_width,
    int out_channels, int out_height, int out_width,
    int kernel_height, int kernel_width,
    int stride_height, int stride_width,
    int pad_height, int pad_width,
    int groups
);

void conv2d_bf16_vector(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int N, int in_channels, int in_height, int in_width,
    int out_channels, int out_height, int out_width,
    int kernel_h, int kernel_w,
    int stride_h, int stride_w,
    int pad_h, int pad_w,
    int groups
);

// Depthwise conv2d
void depthwise_conv2d_bf16_vector(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int N, int channels, int in_height, int in_width,
    int out_height, int out_width,
    int kernel_h, int kernel_w,
    int stride_h, int stride_w,
    int pad_h, int pad_w
);

// Pointwise (1x1) conv2d
void pointwise_conv2d_bf16_vector(
    bfloat16* input, bfloat16* weight, bfloat16* output, bfloat16* bias,
    int N, int in_channels, int out_channels, int height, int width
);

} // extern "C"
