// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "cxxopts.hpp"
#include "test_utils.h"

#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdfloat>
#include <string>
#include <vector>
#include <xrt/experimental/xrt_kernel.h>
#include <xrt/xrt_bo.h>
#include <xrt/xrt_device.h>
#include <xrt/xrt_kernel.h>

#define DTYPE std::bfloat16_t
#include "golden_reference_reader.h"
#include "invocation_plan.h"

int main(int argc, const char *argv[])
{
    cxxopts::Options options(argv[0]);
    cxxopts::ParseResult vm;
    options.add_options()("help,h",
                          "produce help message")("xclbin,x", "the input xclbin path", cxxopts::value<std::string>())(
        "insts-mv",
        "path to the instruction binary for the matrix-vector multiplication kernel",
        cxxopts::value<std::string>()->default_value("mv.bin"))(
        "insts-silu",
        "path to the instruction binary for the silu activation kernel",
        cxxopts::value<std::string>()->default_value("silu.bin"))(
        "insts-eltwise-mul",
        "path to the instruction binary for the element-wise multiplication kernel",
        cxxopts::value<std::string>()->default_value("eltwise_mul.bin"))(
        "dim", "embedding dimension", cxxopts::value<unsigned>()->default_value("2048"))(
        "epsilon",
        "relative threshold for floating point comparsion (result must be within this percentage of magnitude of both "
        "results)",
        cxxopts::value<float>()->default_value("0.0202"))(
        "abs_th",
        "absolute threshold for floating point comparison (difference between results must either be less than this "
        "value or less than relative threshold)",
        cxxopts::value<float>()->default_value("0.1"))(
        "ref",
        "path to golden reference file",
        cxxopts::value<std::string>()->default_value("golden_swiglu/golden_reference.bin"));

    vm = options.parse(argc, argv);
    if (vm.count("help")) {
        std::cout << options.help() << std::endl;
        return 1;
    }
    // Check required options
    if (!vm.count("xclbin")) {
        std::cerr << "Error: Required options missing\n\n";
        std::cerr << "Usage:\n" << options.help() << std::endl;
        return 1;
    }

    std::string xclbin_path = vm["xclbin"].as<std::string>();
    std::string ref_path = vm["ref"].as<std::string>();
    float epsilon = vm["epsilon"].as<float>();
    float abs_th = vm["abs_th"].as<float>();
    unsigned dim = vm["dim"].as<unsigned>();

    // Initialize the NPU and load our design
    constexpr unsigned device_index = 0;
    xrt::device device = xrt::device(device_index);
    xrt::xclbin xclbin(xclbin_path);
    device.register_xclbin(xclbin);
    xrt::hw_context context(device, xclbin.get_uuid());

    std::vector<KernelInfo> kernels = {
        {"mv", vm["insts-mv"].as<std::string>(), "swiglu_mv"},
        {"silu", vm["insts-silu"].as<std::string>(), "swiglu_silu"},
        {"eltwise_mul", vm["insts-eltwise-mul"].as<std::string>(), "swiglu_eltwise_mul"}};

    GoldenReference ref = GoldenReference::fromFile(ref_path);

    std::vector<KernelBufferInfo> buffers = {
        {"inp", dim, KernelBufferInfo::Direction::IN, ref.get<std::bfloat16_t>("inp")->data()},
        {"W1", dim * dim, KernelBufferInfo::Direction::IN, ref.get<std::bfloat16_t>("W1")->data()},
        {"W2", dim * dim, KernelBufferInfo::Direction::IN, ref.get<std::bfloat16_t>("W2")->data()},
        {"left", dim, KernelBufferInfo::Direction::OUT, ref.get<std::bfloat16_t>("left")->data()},
        {"right", dim, KernelBufferInfo::Direction::OUT, ref.get<std::bfloat16_t>("right")->data()},
        {"left_swished", dim, KernelBufferInfo::Direction::OUT, ref.get<std::bfloat16_t>("left_swished")->data()},
        {"result", dim, KernelBufferInfo::Direction::OUT, ref.get<std::bfloat16_t>("result")->data()}};

    std::vector<KernelInvocationInfo> runlist = {{"mv", {"W1", "inp", "left"}},
                                                 {"mv", {"W2", "inp", "right"}},
                                                 {"silu", {"left", "left_swished"}},
                                                 {"eltwise_mul", {"left_swished", "right", "result"}}};

    InvocationPlanInfo plan_info = {.xclbin = xclbin_path, .kernels = kernels, .buffers = buffers, .runlist = runlist};

    InvocationPlan plan = InvocationPlan::fromInfo(plan_info, device, xclbin, context);
    auto [success, t_elapsed] = plan.invoke();

    std::cout << "Elapsed time: " << t_elapsed << " μs" << std::endl;

    std::vector<std::pair<std::string, unsigned>> errors = plan.verifyOutputBuffers(epsilon, abs_th);

    if (errors.size()) {
        for (const auto &[buffer_name, i] : errors) {
            const KernelBuffer &buffer = plan.buffers[buffer_name];
            std::cout << buffer_name << ": Mismatch at index " << i << ": " << std::fixed << std::setprecision(3)
                      << std::setw(8) << buffer.buf[i] << " != " << std::setw(8) << buffer.reference[i] << std::endl;
            if ("result" == buffer_name) {
                // result is supposed to be the result left_swished[i] * right[i]
                std::cout << "  Reference: " << std::fixed << std::setprecision(3) << std::setw(8)
                          << plan.buffers["left_swished"].reference[i] << " * " << std::setw(8)
                          << plan.buffers["right"].reference[i] << " = " << std::setw(8) << buffer.reference[i]
                          << std::endl;
                std::cout << "  Computed:  " << std::fixed << std::setprecision(3) << std::setw(8)
                          << plan.buffers["left_swished"].buf[i] << " * " << std::setw(8)
                          << plan.buffers["right"].buf[i] << " = " << std::setw(8) << buffer.buf[i] << std::endl;
            }
        }
        std::cout << "FAIL." << std::endl;
        return 1;
    } else {
        std::cout << "PASS!" << std::endl;
    }

    return 0;
}
