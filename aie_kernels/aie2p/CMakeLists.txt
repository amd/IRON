# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

add_aie_kernel(gelu.o SOURCES gelu.cc)
add_aie_kernel(layer_norm.o SOURCES layer_norm.cc)
add_aie_kernel(leaky_relu.o SOURCES leaky_relu.cc)
add_aie_kernel(relu.o SOURCES relu.cc)
add_aie_kernel(rms_norm.o SOURCES rms_norm.cc)
add_aie_kernel(silu.o SOURCES silu.cc)
add_aie_kernel(softmax.o SOURCES softmax.cc)