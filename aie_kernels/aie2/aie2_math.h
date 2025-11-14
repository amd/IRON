/*
 * SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

//===- math.h -====//
//
// This file is licensed under the Apache License v2.0 with LLVM Exceptions
// See https://llvm.org/LICENSE.txt for license information.

//
// (c) Copyright 2025 Advanced Micro Devices, Inc.
//
//===----------------------------------------------------------------------===//

#ifndef AIE2_MATH_H
#define AIE2_MATH_H

#include <cstring>
#include <stdint.h>
#include <stdlib.h>

// fast inverse square root implementation from Quake III Arena
inline __attribute__((always_inline)) float invsqrt(float in)
{
    float x2 = in * 0.5f;
    float y = in;
    int32_t i;
    std::memcpy(&i, &y, sizeof(y)); // avoid strict-aliasing
    i = 0x5f3759df - (i >> 1);
    y = *(float *)&i;
    const float threehalfs = 1.5f;
    y = y * (threehalfs - (x2 * y * y));
    return y;
}

#endif // AIE2_MATH_H
