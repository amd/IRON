# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

add_aie_kernel(lut_based_ops.o SOURCES lut_based_ops.cpp)
add_aie_kernel(gelu_.o SOURCES gelu.cc)
add_aie_archive(gelu.o OBJECT_FILES gelu_.o lut_based_ops.o)
add_aie_kernel(layer_norm.o SOURCES layer_norm.cc)
add_aie_kernel(relu.o SOURCES relu.cc)
add_aie_kernel(rms_norm.o SOURCES rms_norm.cc)
add_aie_kernel(silu_.o SOURCES silu.cc)
add_aie_archive(silu.o OBJECT_FILES silu_.o lut_based_ops.o)
add_aie_kernel(softmax_.o SOURCES softmax.cc)
add_aie_archive(softmax.o OBJECT_FILES softmax_.o lut_based_ops.o)
add_aie_kernel(tanh_.o SOURCES tanh.cc)
add_aie_archive(tanh.o OBJECT_FILES tanh_.o lut_based_ops.o)
