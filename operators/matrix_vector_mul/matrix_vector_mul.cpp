// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "cxxopts.hpp"
#include "golden_reference_reader.h"
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
#include <xrt/xrt_bo.h>
#include <xrt/xrt_device.h>
#include <xrt/xrt_kernel.h>

struct matrix {
    unsigned rows;
    unsigned cols;
    const std::bfloat16_t *data;
};

struct vector {
    unsigned length;
    const std::bfloat16_t *data;
};

void print_vector(const vector v)
{
    for (unsigned i = 0; i < v.length; i++) {
        std::cout << std::setprecision(3) << std::fixed << std::setw(6) << v.data[i] << " ";
    }
    std::cout << std::endl;
}

float epsilon;
float abs_th;

// https://stackoverflow.com/a/32334103
bool nearly_equal(float a, float b)
{
    assert(std::numeric_limits<float>::epsilon() <= epsilon);
    assert(epsilon < 1.f);

    if (a == b)
        return true;

    auto diff = std::abs(a - b);
    auto norm = std::min((std::abs(a) + std::abs(b)), std::numeric_limits<float>::max());
    // or even faster: std::min(std::abs(a + b), std::numeric_limits<float>::max());
    // keeping this commented out until I update figures below
    return diff < std::max(abs_th, epsilon * norm);
}

unsigned vectors_nearly_equal(const vector a, const vector b)
{
    assert(a.length == b.length);
    unsigned n_errors = 0;
    for (unsigned i = 0; i < a.length; i++) {
        if (!nearly_equal(a.data[i], b.data[i])) {
            n_errors += 1;
        }
    }
    return n_errors;
}

int main(int argc, const char *argv[])
{
    cxxopts::Options options("Matrix-Vector Multiplication Test");
    cxxopts::ParseResult vm;

    options.add_options()("help,h",
                          "produce help message")("xclbin,x", "the input xclbin path", cxxopts::value<std::string>())(
        "kernel,k", "the kernel name in the XCLBIN (for instance PP_PRE_FD)", cxxopts::value<std::string>())(
        "instr,i",
        "path of file containing userspace instructions to be sent to the LX6",
        cxxopts::value<std::string>())("M", "the number of rows of A", cxxopts::value<int>())(
        "K", "the number of columns of A and rows of B", cxxopts::value<int>())(
        "epsilon",
        "relative threshold for floating point comparsion (result must be within this percentage of magnitude of both "
        "results)",
        cxxopts::value<float>()->default_value("0.01"))(
        "abs_th",
        "absolute threshold for floating point comparison (difference between results must either be less than this "
        "value or less than relative threshold)",
        cxxopts::value<float>()->default_value("0.1"))(
        "ref",
        "path to golden reference file",
        cxxopts::value<std::string>()->default_value("golden_matrix_vector_mul/golden_reference.bin"));

    try {
        vm = options.parse(argc, argv);
        if (vm.count("help")) {
            std::cout << options.help() << std::endl;
            return 1;
        }
        // Check required options
        if (!vm.count("xclbin") || !vm.count("kernel") || !vm.count("instr") || !vm.count("M") || !vm.count("K") ||
            !vm.count("ref")) {
            std::cerr << "Error: Required options missing\n\n";
            std::cerr << "Usage:\n" << options.help() << std::endl;
            return 1;
        }
    } catch (const cxxopts::exceptions::parsing &e) {
        std::cerr << e.what() << "\n\n";
        std::cerr << "Usage:\n" << options.help() << std::endl;
        return 1;
    }

    epsilon = vm["epsilon"].as<float>();
    abs_th = vm["abs_th"].as<float>();

    std::string ref_path = vm["ref"].as<std::string>();
    GoldenReference ref = GoldenReference::fromFile(ref_path);

    std::string xclbin_path = vm["xclbin"].as<std::string>();
    std::string insts_path = vm["instr"].as<std::string>();
    std::string kernel_name = vm["kernel"].as<std::string>();
    unsigned M = vm["M"].as<int>();
    unsigned K = vm["K"].as<int>();
    unsigned N = 1; // B is a column vector

    std::vector<uint32_t> insts = test_utils::load_instr_binary(vm["instr"].as<std::string>());

    // Initialize the NPU and load our design
    constexpr unsigned device_index = 0;
    xrt::device device = xrt::device(device_index);
    xrt::xclbin xclbin(xclbin_path);
    device.register_xclbin(xclbin);
    xrt::hw_context context(device, xclbin.get_uuid());
    xrt::kernel kernel = xrt::kernel(context, kernel_name);

    // Initialzie input/output XRT buffers
    unsigned size_a = M * K;
    unsigned size_b = K * N;
    unsigned size_c = M * N;
    xrt::bo bo_insts = xrt::bo(device, insts.size() * sizeof(insts[0]), XCL_BO_FLAGS_CACHEABLE, kernel.group_id(1));
    xrt::bo bo_a = xrt::bo(device, size_a * sizeof(std::bfloat16_t), XRT_BO_FLAGS_HOST_ONLY, kernel.group_id(3));
    xrt::bo bo_b = xrt::bo(device, size_b * sizeof(std::bfloat16_t), XRT_BO_FLAGS_HOST_ONLY, kernel.group_id(4));
    xrt::bo bo_c = xrt::bo(device, size_c * sizeof(std::bfloat16_t), XRT_BO_FLAGS_HOST_ONLY, kernel.group_id(5));
    uint32_t *buf_insts = bo_insts.map<uint32_t *>();
    std::copy(insts.begin(), insts.end(), buf_insts);
    std::bfloat16_t *buf_a = bo_a.map<std::bfloat16_t *>();
    std::bfloat16_t *buf_b = bo_b.map<std::bfloat16_t *>();
    std::bfloat16_t *buf_c = bo_c.map<std::bfloat16_t *>();

    // Prepare input data (initialize random matrices) and sync to NPU
    memcpy(buf_a, ref.get<std::bfloat16_t>("A")->data(), size_a * sizeof(std::bfloat16_t));
    memcpy(buf_b, ref.get<std::bfloat16_t>("B")->data(), size_b * sizeof(std::bfloat16_t));

    bo_insts.sync(XCL_BO_SYNC_BO_TO_DEVICE);
    bo_a.sync(XCL_BO_SYNC_BO_TO_DEVICE);
    bo_b.sync(XCL_BO_SYNC_BO_TO_DEVICE);
    bo_c.sync(XCL_BO_SYNC_BO_TO_DEVICE);

    // Run our design
    auto t_start = std::chrono::system_clock::now();
    constexpr unsigned opcode = 3;
    auto run = kernel(opcode, bo_insts, insts.size(), bo_a, bo_b, bo_c);
    ert_cmd_state r = run.wait();
    auto t_stop = std::chrono::system_clock::now();
    if (r != ERT_CMD_STATE_COMPLETED) {
        std::cout << "Kernel did not complete. Returned status: " << r << std::endl;
        return 1;
    }
    float t_elapsed = std::chrono::duration_cast<std::chrono::microseconds>(t_stop - t_start).count();
    bo_c.sync(XCL_BO_SYNC_BO_FROM_DEVICE);

    // Print elapsed time
    unsigned n_ops = M * K * N * 2;
    float throughput = n_ops / t_elapsed / 1e3;                     // GOP/s
    double total_bytes = (M * K + K + M) * sizeof(std::bfloat16_t); // input and output
    double bandwidth_GBps = total_bytes / (t_elapsed * 1e-6) / 1e9;
    std::cout << "Latency: " << t_elapsed << " us " << std::endl
              << "Effective Bandwidth: " << bandwidth_GBps << " GB/s" << std::endl
              << "Throughput: " << throughput << " GFLOP/s" << std::endl;

    // Validate correctness of output
    auto ref_C = ref.get<std::bfloat16_t>("C");
    struct vector reference = {M, ref_C->data()};
    unsigned n_errors = vectors_nearly_equal(reference, {M, buf_c});

    if (n_errors == 0) {
        std::cout << "PASS!" << std::endl;
    } else {
        std::cout << "Expected: " << std::endl;
        print_vector(reference);
        std::cout << std::endl;
        std::cout << "Actual: " << std::endl;
        print_vector({M, buf_c});
        std::cout << std::endl;
        std::cout << n_errors << "/" << M << " errors" << std::endl;
        std::cout << "FAIL." << std::endl;
        return 1;
    }

    return 0;
}
