// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
#pragma once

#include <stdexcept>
#include <string>
#include <string_view>

#define TEST_REQUIRE(condition)                                                                                        \
    do {                                                                                                               \
        if (!(condition))                                                                                              \
            throw std::runtime_error("requirement failed: " #condition);                                               \
    } while (false)

inline void RequireContains(std::string_view text, std::string_view expected)
{
    TEST_REQUIRE(text.find(expected) != std::string_view::npos);
}

template <class F> std::string RequireThrows(F callable)
{
    try {
        callable();
    } catch (const std::exception &error) {
        return error.what();
    }
    throw std::runtime_error("expected exception was not thrown");
}
