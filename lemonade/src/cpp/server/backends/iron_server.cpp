// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "lemon/backends/iron_server.h"

#include "lemon/backend_manager.h"
#include "lemon/backends/backend_utils.h"
#include "lemon/error_types.h"
#include "lemon/utils/process_manager.h"

#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;
using namespace lemon::utils;

namespace lemon
{

/**
 * @brief Get installation parameters for IRON backend
 *
 * For Python-based backend, we rely on system Python + pip package.
 * Returns package information for potential bundling.
 *
 * @param backend Backend name (unused)
 * @param version Version string (unused)
 * @return InstallParams with amd/iron package info
 */
InstallParams IronServer::get_install_params(const std::string & /*backend*/, const std::string & /*version*/)
{
    // For Python-based backend, we rely on system Python + pip package
    // Return package info for potential bundling
    return {"amd/iron", "iron-server.zip"};
}

/**
 * @brief Construct a new Iron Server object
 *
 * @param model_name Name of the model to load
 * @param debug Enable debug logging
 * @param model_manager Pointer to model manager (non-owning)
 * @param backend_manager Pointer to backend manager (non-owning)
 */
IronServer::IronServer(const std::string &model_name,
                       bool debug,
                       ModelManager *model_manager,
                       BackendManager *backend_manager)
    : WrappedServer("IRON-Server", debug ? "debug" : "info", model_manager, backend_manager),
      model_name_(model_name),
      is_loaded_(false)
{
}

/**
 * @brief Destroy the Iron Server object
 *
 * Ensures cleanup by calling unload() if model is loaded.
 * Suppresses exceptions to prevent issues during destruction.
 */
IronServer::~IronServer()
{
    if (is_loaded_) {
        try {
            unload();
        } catch (...) {
            // Suppress exceptions in destructor
        }
    }
}

/**
 * @brief Check if IRON Python package is available
 *
 * Executes: python -c "import iron"
 *
 * @return true if Python and iron package are installed
 * @return false otherwise
 */
bool IronServer::is_available()
{
    // Check if Python and iron package are available
    try {
        auto result = utils::ProcessManager::execute_command("python -c \"import iron\"");
        return result.exit_code == 0;
    } catch (...) {
        return false;
    }
}

/**
 * @brief Load model and start IRON server subprocess
 *
 * Starts the Python subprocess:
 *   python -m iron.api.server --model-path <path> --port <port> [--verbose]
 *
 * Waits for the /health endpoint to respond before returning.
 *
 * @param model_name Name of the model
 * @param model_info Model information including resolved path
 * @param options Recipe options (unused for IRON)
 * @param do_not_upgrade If true, don't upgrade the backend (unused)
 * @throws std::runtime_error if model file not found or server fails to start
 */
void IronServer::load(const std::string &model_name,
                      const ModelInfo &model_info,
                      const RecipeOptions &options,
                      bool do_not_upgrade)
{
    (void)options;        // Unused for IRON backend
    (void)do_not_upgrade; // Unused for IRON backend

    LOG(DEBUG, "IRON") << "Loading model: " << model_name << std::endl;

    // Get model path from model manager
    std::string gguf_path = model_info.resolved_path();
    if (gguf_path.empty()) {
        throw std::runtime_error("Model file not found for checkpoint: " + model_info.checkpoint());
    }

    // Find Python executable
    std::string python_path = "python"; // Could use full path detection

    // Choose port
    port_ = choose_port();

    // Build command line arguments
    std::vector<std::string> args = {
        "-m", "iron.api.server", "--model-path", gguf_path, "--port", std::to_string(port_)};

    // Add debug flag if enabled
    if (is_debug()) {
        args.push_back("--verbose");
    }

    // Set Python environment variables if needed
    std::vector<std::pair<std::string, std::string>> env_vars;
    // Example: env_vars.push_back({"PYTHONPATH", "/path/to/iron"});
    // Example: env_vars.push_back({"IRON_CACHE_DIR", "~/.cache/iron"});

    LOG(DEBUG, "IRON") << "Starting: \"" << python_path << "\"";
    for (const auto &arg : args) {
        LOG(DEBUG, "IRON") << " \"" << arg << "\"";
    }
    LOG(DEBUG, "IRON") << std::endl;

    // Start the process (filter health check spam)
    process_handle_ = utils::ProcessManager::start_process(python_path,
                                                           args,
                                                           "",         // Working directory
                                                           is_debug(), // Inherit output if debug
                                                           true,       // Filter health check spam
                                                           env_vars);

    if (!utils::ProcessManager::is_running(process_handle_)) {
        throw std::runtime_error("Failed to start IRON server process");
    }

    LOG(DEBUG, "ProcessManager") << "Process started successfully, PID: " << process_handle_.pid << std::endl;

    // Wait for server to be ready
    if (!wait_for_ready("/health")) {
        utils::ProcessManager::stop_process(process_handle_);
        process_handle_ = {nullptr, 0}; // Reset to prevent double-stop
        throw std::runtime_error("IRON server failed to start (check logs for details)");
    }

    is_loaded_ = true;
    model_path_ = gguf_path;
    LOG(INFO, "IRON") << "Model loaded on port " << port_ << std::endl;
}

/**
 * @brief Unload model and stop IRON server subprocess
 *
 * Terminates the Python subprocess and resets state:
 * - Calls ProcessManager::stop_process()
 * - Resets process_handle_, port_, model_path_
 * - Sets is_loaded_ to false
 */
void IronServer::unload()
{
    if (!is_loaded_) {
        return;
    }

    LOG(DEBUG, "IRON") << "Unloading model..." << std::endl;

#ifdef _WIN32
    if (process_handle_.handle) {
#else
    if (process_handle_.pid > 0) {
#endif
        utils::ProcessManager::stop_process(process_handle_);
        process_handle_ = {nullptr, 0};
    }

    is_loaded_ = false;
    port_ = 0;
    model_path_.clear();
}

/**
 * @brief Handle OpenAI chat completion request
 *
 * Forwards request to: POST /v1/chat/completions
 *
 * @param request JSON request with model, messages, temperature, etc.
 * @return JSON response with completion
 * @throws ModelNotLoadedException if server is not loaded
 */
json IronServer::chat_completion(const json &request)
{
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }

    // Forward to /v1/chat/completions endpoint
    return forward_request("/v1/chat/completions", request);
}

/**
 * @brief Handle OpenAI legacy completion request
 *
 * Forwards request to: POST /v1/completions
 *
 * @param request JSON request with model, prompt, etc.
 * @return JSON response with completion
 * @throws ModelNotLoadedException if server is not loaded
 */
json IronServer::completion(const json &request)
{
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }

    // Forward to /v1/completions endpoint
    return forward_request("/v1/completions", request);
}

/**
 * @brief Handle OpenAI responses request
 *
 * Forwards request to: POST /v1/responses
 *
 * @param request JSON request
 * @return JSON response
 * @throws ModelNotLoadedException if server is not loaded
 */
json IronServer::responses(const json &request)
{
    if (!is_loaded_) {
        throw ModelNotLoadedException("IRON-Server");
    }

    // Forward to /v1/responses endpoint
    return forward_request("/v1/responses", request);
}

} // namespace lemon
