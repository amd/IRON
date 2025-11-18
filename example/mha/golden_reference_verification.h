/*
 * SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

//===- golden_reference_verification.h -------------------*- C++ -*-===//
//
// This file is licensed under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.

//

//
//===----------------------------------------------------------------------===//

// This file contains verification functions that use PyTorch-generated golden reference values instead of host-side
// computation

#ifndef GOLDEN_REFERENCE_VERIFICATION_H
#define GOLDEN_REFERENCE_VERIFICATION_H

#include "common.h"
#include "golden_reference_reader.h"

#include <algorithm>
#include <optional>
#include <vector>

namespace golden_reference_verification
{

template <typename Tin, typename Tout, typename Tacc>
int verify_against_golden(GoldenReference &ref,
                          const std::vector<Tout> &actual_O,
                          int verbosity,
                          float abs_tol,
                          float rel_tol,
                          int heads,
                          int S_q,
                          int d)
{

    // Check dimensions match
    if (actual_O.size() != (uint)heads * S_q * d) {
        std::cerr << "Error: Output size mismatch. Expected " << (heads * S_q * d) << " but got " << actual_O.size()
                  << std::endl;
        return -1;
    }

    int n_errors = 0;
    float average_error = 0.0f;
    Tin max_abs_error = 0;
    Tin min_abs_error = std::numeric_limits<Tin>::max();

    std::vector<matmul_common::error<Tout>> errors;
    std::vector<Tout> &golden_ref = *ref.get<Tout>("O");
    // Golden O is stored with sequence padding (S_q_pad). Infer per-head stride from size.
    if (golden_ref.size() % (static_cast<size_t>(heads) * static_cast<size_t>(d)) != 0) {
        std::cerr << "Golden reference size is inconsistent with heads and d." << std::endl;
        return -1;
    }
    int padded_S_q = static_cast<int>(golden_ref.size() / (static_cast<size_t>(heads) * static_cast<size_t>(d)));
    Tout max_rel_error = (Tout)0.0f;

    for (int head = 0; head < heads; head++) {
        for (int row = 0; row < S_q; row++) {
            for (int col = 0; col < d; col++) {

                int idx_actual = (head * S_q * d) + (row * d) + col;
                int idx_golden = (head * padded_S_q * d) + (row * d) + col;

                Tout expected = golden_ref[idx_golden];
                Tout actual = actual_O[idx_actual];

                average_error += std::abs(actual - expected);
                max_abs_error = std::max(max_abs_error, std::abs(actual - expected));
                min_abs_error = std::min(min_abs_error, std::abs(actual - expected));

                std::optional<matmul_common::error<Tout>> error =
                    matmul_common::verify_single(head, row, col, expected, actual, abs_tol, rel_tol);

                if (error.has_value()) {

                    if (n_errors < matmul_common::max_printable_errors) {
                        errors.push_back(*error);
                    }

                    Tout rel_error = std::abs(error->actual - error->expected) /
                                     std::max(std::abs(error->actual), std::abs(error->expected));

                    if (rel_error > max_rel_error) {
                        max_rel_error = rel_error;
                    }
                    n_errors++;
                }
            }
        }
    }
    average_error /= actual_O.size();

    std::cout << "\nAbsolute tolerence: " << abs_tol << std::endl;
    std::cout << "Relative tolerence: " << rel_tol << std::endl;
    std::cout << "Average relative error: " << average_error << std::endl;
    std::cout << "Max absolute error: " << max_abs_error << std::endl;
    std::cout << "Min absolute error: " << min_abs_error << std::endl << std::endl;

    float percentage_of_error_threshold = 0.005f; // 0.5%
    float max_acceptable_errors = std::floor(S_q * d * heads * percentage_of_error_threshold);

    std::cout << "Number of errors: " << n_errors << " out of " << (heads * S_q * d) << " elements." << std::endl;
    std::cout << "Maximum acceptable errors: " << max_acceptable_errors << std::endl;

    if (verbosity >= 1) {
        std::cout << std::endl << "Golden Reference:" << std::endl;
        matmul_common::print_matrix(golden_ref, d, 32, 16);

        std::cout << std::endl << "Actual Output:" << std::endl;
        matmul_common::print_matrix(actual_O, d, 32, 16);

        std::cout << std::endl << "Difference:" << std::endl;
        std::vector<Tout> diff(actual_O.size());

        for (uint i = 0; i < actual_O.size(); i++) {
            diff[i] = golden_ref[i] - actual_O[i];
        }
        matmul_common::print_matrix(diff, d, 32, 16, std::cout, " | ", " ... ", 6);
    }

    if (n_errors > max_acceptable_errors) {
        matmul_common::print_error_summary(std::cout, n_errors, heads * S_q * d, errors, max_rel_error);
    } else {
        n_errors = 0; // reset to 0 if within acceptable range
    }

    return n_errors;
}

// Load input matrices from golden references
template <typename Tin>
void load_golden_inputs(GoldenReference &ref,
                        std::vector<Tin> &Q,
                        std::vector<Tin> &K,
                        std::vector<Tin> &V,
                        int heads,
                        int S_q,
                        int S_kv,
                        int d)
{
    // Golden inputs are stored padded per-head: (heads, S_pad, d).
    // Copy only the valid (unpadded) rows per head into compact buffers.
    std::vector<Tin> &gQ = *ref.get<Tin>("Q");
    std::vector<Tin> &gK = *ref.get<Tin>("K");
    std::vector<Tin> &gV = *ref.get<Tin>("V");

    auto infer_padded_S = [&](const std::vector<Tin> &g, int H, int D) -> int {
        size_t denom = static_cast<size_t>(H) * static_cast<size_t>(D);
        if (g.size() % denom != 0) {
            throw std::invalid_argument("Golden input size inconsistent with heads and d");
        }
        return static_cast<int>(g.size() / denom);
    };

    int S_q_pad = infer_padded_S(gQ, heads, d);
    int S_kv_pad = infer_padded_S(gK, heads, d);

    // Q: (heads, S_q, d) from (heads, S_q_pad, d)
    for (int h = 0; h < heads; ++h) {
        for (int s = 0; s < S_q; ++s) {
            const Tin *src = gQ.data() + (static_cast<size_t>(h) * S_q_pad + s) * d;
            Tin *dst = Q.data() + (static_cast<size_t>(h) * S_q + s) * d;
            std::copy_n(src, d, dst);
        }
    }

    // K and V: (heads, S_kv, d) from (heads, S_kv_pad, d)
    for (int h = 0; h < heads; ++h) {
        for (int s = 0; s < S_kv; ++s) {
            const Tin *srcK = gK.data() + (static_cast<size_t>(h) * S_kv_pad + s) * d;
            Tin *dstK = K.data() + (static_cast<size_t>(h) * S_kv + s) * d;
            std::copy_n(srcK, d, dstK);

            const Tin *srcV = gV.data() + (static_cast<size_t>(h) * S_kv_pad + s) * d;
            Tin *dstV = V.data() + (static_cast<size_t>(h) * S_kv + s) * d;
            std::copy_n(srcV, d, dstV);
        }
    }
}

} // namespace golden_reference_verification

#endif // GOLDEN_REFERENCE_VERIFICATION_H
