// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "lemon/router.h"

#include "lemon/backends/flm_server.h"
#include "lemon/backends/iron_server.h"
#include "lemon/backends/kokoro_server.h"
#include "lemon/backends/llamacpp_server.h"
#include "lemon/backends/ryzenaiserver.h"
#include "lemon/backends/sd_server.h"
#include "lemon/backends/whisper_server.h"
#include "lemon/wrapped_server.h"

#include <memory>

namespace lemon
{

/**
 * @brief Create a backend server instance for the given model
 *
 * Factory method that creates the appropriate backend server based on
 * the model's recipe configuration.
 *
 * @param model_info Model information including recipe type
 * @return Unique pointer to WrappedServer instance
 * @throws std::runtime_error if recipe is not supported
 */
std::unique_ptr<WrappedServer> Router::create_backend_server(const ModelInfo &model_info)
{
    std::unique_ptr<WrappedServer> new_server;

    if (model_info.recipe == "whispercpp") {
        LOG(DEBUG, "Router") << "Creating WhisperServer backend" << std::endl;
        new_server = std::make_unique<backends::WhisperServer>(
            model_info.model_name, log_level_ == "debug", model_manager_, backend_manager_);
    } else if (model_info.recipe == "kokoro") {
        LOG(DEBUG, "Router") << "Creating KokoroServer backend" << std::endl;
        new_server = std::make_unique<backends::KokoroServer>(
            model_info.model_name, log_level_ == "debug", model_manager_, backend_manager_);
    } else if (model_info.recipe == "sd-cpp") {
        LOG(DEBUG, "Router") << "Creating SDServer backend" << std::endl;
        new_server = std::make_unique<backends::SDServer>(
            model_info.model_name, log_level_ == "debug", model_manager_, backend_manager_);
    } else if (model_info.recipe == "flm") {
        LOG(DEBUG, "Router") << "Creating FastFlowLMServer backend" << std::endl;
        new_server = std::make_unique<backends::FastFlowLMServer>(
            model_info.model_name, log_level_ == "debug", model_manager_, backend_manager_);
    } else if (model_info.recipe == "ryzenai-llm") {
        LOG(DEBUG, "Router") << "Creating RyzenAIServer backend" << std::endl;
        new_server = std::make_unique<backends::RyzenAIServer>(
            model_info.model_name, log_level_ == "debug", model_manager_, backend_manager_);
    } else if (model_info.recipe == "iron") {
        LOG(DEBUG, "Router") << "Creating IronServer backend" << std::endl;
        new_server = std::make_unique<IronServer>(
            model_info.model_name, log_level_ == "debug", model_manager_, backend_manager_);
    } else {
        // Default to LlamaCppServer for unknown recipes
        LOG(DEBUG, "Router") << "Creating LlamaCppServer backend (default)" << std::endl;
        new_server = std::make_unique<backends::LlamaCppServer>(
            model_info.model_name, log_level_ == "debug", model_manager_, backend_manager_);
    }

    return new_server;
}

} // namespace lemon
