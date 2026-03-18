// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include "lemon/backends/backend_utils.h"
#include "lemon/error_types.h"
#include "lemon/server_capabilities.h"
#include "lemon/wrapped_server.h"

#include <string>

namespace lemon
{

using backends::BackendSpec;
using backends::InstallParams;

/**
 * @class IronServer
 * @brief Backend server wrapper for IRON (AMD Ryzen AI NPU framework)
 *
 * IronServer wraps the IRON Python HTTP server as a subprocess, forwarding
 * OpenAI-compatible API requests to it. The IRON server provides hardware-accelerated
 * LLM inference on AMD Ryzen AI NPUs.
 *
 * Usage pattern:
 * @code
 *   auto server = std::make_unique<IronServer>("model-name", debug, model_mgr, backend_mgr);
 *   server->load(model_name, model_info, options);
 *   auto response = server->chat_completion(request);
 *   server->unload();
 * @endcode
 *
 * Subprocess command:
 *   python -m iron.api.server --model-path <path> --port <port> [--verbose]
 */
class IronServer : public WrappedServer
{
  public:
    /**
     * @brief Get installation parameters for the IRON backend
     * @param backend Backend name (unused for Python-based backend)
     * @param version Version string (unused for Python-based backend)
     * @return InstallParams with package information
     *
     * For Python-based backend, we rely on system Python + pip package.
     */
#ifndef LEMONADE_TRAY
    static InstallParams get_install_params(const std::string &backend, const std::string &version);
#endif

    /**
     * @brief Backend specification for IronServer
     *
     * Defines the backend name and executable. On Windows uses "python",
     * on Linux uses "python3".
     */
    inline static const BackendSpec SPEC = BackendSpec("iron-server",
#ifdef _WIN32
                                                       "python" // Uses system Python
#else
                                                       "python3"
#endif
#ifndef LEMONADE_TRAY
                                                       ,
                                                       get_install_params
#endif
    );

    /**
     * @brief Constructor
     * @param model_name Name of the model to load
     * @param debug Enable debug logging
     * @param model_manager Pointer to model manager (non-owning)
     * @param backend_manager Pointer to backend manager (non-owning)
     */
    IronServer(const std::string &model_name, bool debug, ModelManager *model_manager, BackendManager *backend_manager);

    /**
     * @brief Destructor - ensures cleanup of subprocess
     */
    ~IronServer() override;

    /**
     * @brief Check if IRON Python package is available
     * @return true if Python and iron package are installed, false otherwise
     *
     * Executes: python -c "import iron"
     */
    static bool is_available();

    /**
     * @brief Load model and start IRON server subprocess
     * @param model_name Name of the model
     * @param model_info Model information including path
     * @param options Recipe options for backend configuration
     * @param do_not_upgrade If true, don't upgrade the backend
     * @throws std::runtime_error if model file not found or server fails to start
     *
     * Starts the Python subprocess:
     *   python -m iron.api.server --model-path <path> --port <port> [--verbose]
     */
    void load(const std::string &model_name,
              const ModelInfo &model_info,
              const RecipeOptions &options,
              bool do_not_upgrade = false) override;

    /**
     * @brief Unload model and stop IRON server subprocess
     *
     * Terminates the Python subprocess and resets state.
     */
    void unload() override;

    /**
     * @brief Handle OpenAI chat completion request
     * @param request JSON request with model, messages, etc.
     * @return JSON response with completion
     * @throws ModelNotLoadedException if server is not loaded
     *
     * Forwards request to: POST /v1/chat/completions
     */
    json chat_completion(const json &request) override;

    /**
     * @brief Handle OpenAI legacy completion request
     * @param request JSON request with model, prompt, etc.
     * @return JSON response with completion
     * @throws ModelNotLoadedException if server is not loaded
     *
     * Forwards request to: POST /v1/completions
     */
    json completion(const json &request) override;

    /**
     * @brief Handle OpenAI responses request
     * @param request JSON request
     * @return JSON response
     * @throws ModelNotLoadedException if server is not loaded
     *
     * Forwards request to: POST /v1/responses
     */
    json responses(const json &request) override;

  private:
    std::string model_name_; ///< Name of the loaded model
    std::string model_path_; ///< Path to the model file
    bool is_loaded_;         ///< Whether model is currently loaded
};

} // namespace lemon
