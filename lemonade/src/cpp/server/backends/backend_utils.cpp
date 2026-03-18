// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "lemon/backends/backend_utils.h"

#include "lemon/backends/flm_server.h"
#include "lemon/backends/iron_server.h"
#include "lemon/backends/kokoro_server.h"
#include "lemon/backends/llamacpp_server.h"
#include "lemon/backends/ryzenaiserver.h"
#include "lemon/backends/sd_server.h"
#include "lemon/backends/whisper_server.h"

#include <unordered_map>

namespace lemon::backends
{

/**
 * @brief Map recipe name to backend specification
 *
 * @param recipe Recipe/backend name (e.g., "llamacpp", "ryzenai-llm", "iron")
 * @return Pointer to BackendSpec if found, nullptr otherwise
 */
const BackendSpec *try_get_spec_for_recipe(const std::string &recipe)
{
    static const std::unordered_map<std::string, const BackendSpec *> spec_map = {
        {"llamacpp", &LlamaCppServer::SPEC},
        {"ryzenai-llm", &RyzenAIServer::SPEC},
        {"whispercpp", &WhisperServer::SPEC},
        {"kokoro", &KokoroServer::SPEC},
        {"sd-cpp", &SDServer::SPEC},
        {"flm", &FastFlowLMServer::SPEC},
        {"iron", &IronServer::SPEC},
    };

    auto it = spec_map.find(recipe);
    if (it != spec_map.end()) {
        return it->second;
    }
    return nullptr;
}

/**
 * @brief Check if a recipe/backend is available
 *
 * @param recipe Recipe/backend name
 * @return true if backend is available, false otherwise
 */
bool is_recipe_available(const std::string &recipe)
{
    const BackendSpec *spec = try_get_spec_for_recipe(recipe);
    if (!spec) {
        return false;
    }

    // Check backend-specific availability
    if (recipe == "iron") {
        return IronServer::is_available();
    }

    // For native backends, check if executable exists
    // This is a simplified check - actual implementation may vary
    return true;
}

/**
 * @brief Get list of all available recipes
 *
 * @return Vector of recipe names
 */
std::vector<std::string> get_available_recipes()
{
    return {
        "llamacpp",
        "ryzenai-llm",
        "whispercpp",
        "kokoro",
        "sd-cpp",
        "flm",
        "iron",
    };
}

} // namespace lemon::backends
