// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

using namespace aie;

extern "C" {

void front_fused(
    bfloat16 *restrict input,
    bfloat16 *restrict output
)
{
    event0();

    // TODO

    event1();
}

} // extern "C"
