// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "cxxopts.hpp"
#include "golden_reference_reader.h"
#include "test_utils.h"
#include "xrt/xrt_bo.h"
#include "xrt/xrt_device.h"
#include "xrt/xrt_kernel.h"

#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main(int argc, const char *argv[])
{
    // Program arguments parsing
    cxxopts::Options options("Matrix Matrix Multiplication Test");
    cxxopts::ParseResult vm;
    options.add_options()("help,h",
                          "produce help message")("xclbin,x", "the input xclbin path", cxxopts::value<std::string>())(
        "kernel,k", "the kernel name in the XCLBIN (for instance PP_PRE_FD)", cxxopts::value<std::string>())(
        "verbosity,v", "the verbosity of the output", cxxopts::value<int>()->default_value("0"))(
        "instr,i", "path of file containing userspace instructions sent to the NPU", cxxopts::value<std::string>())(
        "rows,M", "Matrix size M", cxxopts::value<int>()->default_value("512"))(
        "inner,K", "Matrix size K", cxxopts::value<int>()->default_value("512"))(
        "columns,N", "Matrix size N", cxxopts::value<int>()->default_value("512"))(
        "trace_sz,t", "trace size", cxxopts::value<int>()->default_value("0"))(
        "trace_file", "where to store trace output", cxxopts::value<std::string>()->default_value("trace.txt"))(
        "b_col_maj", "Is B matrix in colum-major format?", cxxopts::value<int>()->default_value("0"))(
        "c_col_maj", "Is C matrix in colum-major format?", cxxopts::value<int>()->default_value("0"))(
        "ref",
        "path to golden reference file",
        cxxopts::value<std::string>()->default_value("golden_gemm/golden_reference.bin"));

    try {
        vm = options.parse(argc, argv);

        if (vm.count("help")) {
            std::cout << options.help() << std::endl;
            return 1;
        }

        // Check required options
        if (!vm.count("xclbin") || !vm.count("kernel") || !vm.count("instr") || !vm.count("ref")) {
            std::cerr << "Error: Required options missing\n\n";
            std::cerr << "Usage:\n" << options.help() << std::endl;
            return 1;
        }
    } catch (const cxxopts::exceptions::parsing &e) {
        std::cerr << e.what() << "\n\n";
        std::cerr << "Usage:\n" << options.help() << std::endl;
        return 1;
    }

    std::vector<uint32_t> instr_v = test_utils::load_instr_binary(vm["instr"].as<std::string>());

    std::string ref_path = vm["ref"].as<std::string>();
    GoldenReference ref = GoldenReference::fromFile(ref_path);

    int verbosity = vm["verbosity"].as<int>();
    if (verbosity >= 1)
        std::cout << "Sequence instr count: " << instr_v.size() << std::endl;

    int M = vm["M"].as<int>();
    int K = vm["K"].as<int>();
    int N = vm["N"].as<int>();

    if (verbosity >= 1) {
        std::cout << "Matrix size " << M << "x" << K << "x" << N << std::endl;
    }

    int A_VOLUME = M * K;
    int B_VOLUME = N * K;
    int C_VOLUME = M * N;

    size_t A_SIZE = (A_VOLUME * sizeof(std::bfloat16_t));
    size_t B_SIZE = (B_VOLUME * sizeof(std::bfloat16_t));
    size_t C_SIZE = (C_VOLUME * sizeof(std::bfloat16_t));

    // Start the XRT test code
    // Get a device handle
    unsigned int device_index = 0;
    auto device = xrt::device(device_index);

    // Load the xclbin
    if (verbosity >= 1)
        std::cout << "Loading xclbin: " << vm["xclbin"].as<std::string>() << std::endl;
    auto xclbin = xrt::xclbin(vm["xclbin"].as<std::string>());

    if (verbosity >= 1)
        std::cout << "Kernel opcode: " << vm["kernel"].as<std::string>() << std::endl;
    std::string kernelName = vm["kernel"].as<std::string>();

    if (verbosity >= 1)
        std::cout << "Registering xclbin: " << vm["xclbin"].as<std::string>() << "\n";

    device.register_xclbin(xclbin);

    // get a hardware context
    if (verbosity >= 1)
        std::cout << "Getting hardware context." << std::endl;
    xrt::hw_context context(device, xclbin.get_uuid());

    // get a kernel handle
    if (verbosity >= 1)
        std::cout << "Getting handle to kernel:" << kernelName << std::endl;
    auto kernel = xrt::kernel(context, kernelName);

    auto bo_instr = xrt::bo(device, instr_v.size() * sizeof(int), XCL_BO_FLAGS_CACHEABLE, kernel.group_id(1));
    auto bo_a = xrt::bo(device, A_SIZE, XRT_BO_FLAGS_HOST_ONLY, kernel.group_id(3));
    auto bo_b = xrt::bo(device, B_SIZE, XRT_BO_FLAGS_HOST_ONLY, kernel.group_id(4));
    auto bo_out = xrt::bo(device, C_SIZE, XRT_BO_FLAGS_HOST_ONLY, kernel.group_id(5));

    if (verbosity >= 1)
        std::cout << "Writing data into buffer objects." << std::endl;

    std::bfloat16_t *bufA = bo_a.map<std::bfloat16_t *>();
    memcpy(bufA, ref.get<std::bfloat16_t>("A")->data(), A_VOLUME * sizeof(std::bfloat16_t));

    std::bfloat16_t *bufB = bo_b.map<std::bfloat16_t *>();
    memcpy(bufB, ref.get<std::bfloat16_t>("B")->data(), B_VOLUME * sizeof(std::bfloat16_t));

    // Instruction buffer for DMA configuration
    void *bufInstr = bo_instr.map<void *>();
    memcpy(bufInstr, instr_v.data(), instr_v.size() * sizeof(int));

    bo_instr.sync(XCL_BO_SYNC_BO_TO_DEVICE);
    bo_a.sync(XCL_BO_SYNC_BO_TO_DEVICE);
    bo_b.sync(XCL_BO_SYNC_BO_TO_DEVICE);
    bo_out.sync(XCL_BO_SYNC_BO_TO_DEVICE);

    if (verbosity >= 1)
        std::cout << "Running Kernel." << std::endl;
    unsigned int opcode = 3;
    // Setup run to configure
    auto cfg_run = kernel(opcode, bo_instr, instr_v.size(), bo_a, bo_b, bo_out);
    cfg_run.wait();
    auto start = std::chrono::high_resolution_clock::now();
    // Test run
    auto run = kernel(opcode, bo_instr, instr_v.size(), bo_a, bo_b, bo_out);
    ert_cmd_state r = run.wait();
    auto stop = std::chrono::high_resolution_clock::now();
    if (r != ERT_CMD_STATE_COMPLETED) {
        std::cout << "Kernel did not complete. Returned status: " << r << std::endl;
        return 1;
    }
    const float npu_time = std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count();

    bo_out.sync(XCL_BO_SYNC_BO_FROM_DEVICE);
    std::cout << std::endl;
    std::cout << "Latency (us): " << npu_time << std::endl;
    std::cout << std::endl;

    double total_bytes = ((M * K) + (K * N) + (M * N)) * sizeof(std::bfloat16_t); // input and output
    double bandwidth_GBps = (total_bytes / (1024 * 1024 * 1024)) / (npu_time * 1e-6);
    std::cout << "Effective Bandwidth: " << bandwidth_GBps << " GB/s" << std::endl;

    // Need to cast to long long since M/K/N=2048 would give 17*10^9 ops for example
    unsigned long long n_ops = static_cast<unsigned long long>(M) * K * N * 2;
    float throughput = n_ops / npu_time / 1e3; // GOP/s
    std::cout << "Throughput: " << throughput << " GFLOP/s" << std::endl;

    std::bfloat16_t *bufOut1 = bo_out.map<std::bfloat16_t *>();

    // Compare with golden reference
    auto ref_C = ref.get<std::bfloat16_t>("C");
    int errors = 0;
    std::bfloat16_t max_diff = std::bfloat16_t(0.0); // Variable to store the maximum difference
    std::pair<int, std::pair<std::bfloat16_t, std::bfloat16_t>>
        mismatch_values; // To store index and values of mismatches

    for (int i = 0; i < M * N; i++) {
        std::bfloat16_t ref_val = (*ref_C)[i];
        std::bfloat16_t diff = std::abs(*(bufOut1 + i) - ref_val); // Calculate the difference
        if (!test_utils::nearly_equal(*(bufOut1 + i), ref_val, 0.005, 0.005)) {
            errors++;
            // Update max_diff if the current difference is larger
            if (diff > max_diff) {
                max_diff = diff;
                // Store the index and values of the mismatch
                mismatch_values = std::pair<int, std::pair<std::bfloat16_t, std::bfloat16_t>>(
                    i, std::make_pair(ref_val, *(bufOut1 + i)));
            }
            // Print the first 100 mismatches
            if (errors <= 100) {
                std::cout << "Mismatch at index " << i << ": " << "Expected: " << ref_val << ", "
                          << "Got: " << *(bufOut1 + i) << std::endl;
            }
        }
    }
    // Print the largest difference after checking all elements
    // This is to help with comparing the current tolerances with the errors that show
    if (errors > 0) {
        std::cout << "Largest difference: " << max_diff << std::endl;
        std::cout << "Index: " << mismatch_values.first << ", Expected: " << mismatch_values.second.first
                  << ", Got: " << mismatch_values.second.second << std::endl;
    }

    if (!errors) {
        std::cout << std::endl << "PASS!" << std::endl << std::endl;
        return 0;
    } else {
        std::cout << std::endl
                  << errors << " mismatches (" << errors / (float)(M * N) * 100 << "% of output data)." << std::endl
                  << std::endl;
        std::cout << std::endl << "fail." << std::endl << std::endl;
        return 1;
    }
}