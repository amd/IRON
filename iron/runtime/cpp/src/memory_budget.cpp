// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file memory_budget.cpp
 * @brief Implementation of memory budget enforcement for IRON runtime
 *
 * This file implements the MemoryBudget class for tracking and enforcing
 * memory limits across different components to prevent OOM conditions.
 *
 * Key features:
 * - Per-component budget tracking (weights, KV cache, activations, misc)
 * - Atomic counters for thread-safe operations
 * - Pre-allocation validation with detailed error messages
 * - Graceful failure handling
 */

#include <cmath>
#include <cstring>
#include <iomanip>
#include <iron/memory_budget.hpp>
#include <sstream>
#include <stdexcept>

namespace iron
{
namespace runtime
{

//==============================================================================
// Construction/Destruction
//==============================================================================

MemoryBudget::MemoryBudget(const Limits &limits) : limits_(limits)
{
    if (!limits.isValid()) {
        throw std::invalid_argument("Invalid MemoryBudget limits: sum of component budgets + headroom "
                                    "must not exceed totalBudget");
    }
}

//==============================================================================
// Validation
//==============================================================================

MemoryBudget::AllocationResult
MemoryBudget::validateModelLoad(size_t requiredWeights, size_t requiredKV, size_t requiredActivations) const
{

    // Check each component budget individually
    if (requiredWeights > limits_.weightBudget) {
        return AllocationResult{false,
                                "Weight memory exceeds budget: " + formatBytes(requiredWeights) + " required, " +
                                    formatBytes(limits_.weightBudget) + " available",
                                requiredWeights,
                                limits_.weightBudget};
    }

    if (requiredKV > limits_.kvCacheBudget) {
        return AllocationResult{false,
                                "KV cache memory exceeds budget: " + formatBytes(requiredKV) + " required, " +
                                    formatBytes(limits_.kvCacheBudget) + " available",
                                requiredKV,
                                limits_.kvCacheBudget};
    }

    if (requiredActivations > limits_.activationBudget) {
        return AllocationResult{false,
                                "Activation memory exceeds budget: " + formatBytes(requiredActivations) +
                                    " required, " + formatBytes(limits_.activationBudget) + " available",
                                requiredActivations,
                                limits_.activationBudget};
    }

    // Check total budget (accounting for headroom)
    size_t totalRequired = requiredWeights + requiredKV + requiredActivations;

    // Account for existing usage
    size_t currentUsage = getTotalUsage();
    size_t remainingTotal = limits_.totalBudget - currentUsage;

    if (totalRequired > remainingTotal) {
        return AllocationResult{false,
                                "Total memory requirement exceeds available budget: " + formatBytes(totalRequired) +
                                    " required, " + formatBytes(remainingTotal) +
                                    " available (current usage: " + formatBytes(currentUsage) + ")",
                                totalRequired,
                                remainingTotal};
    }

    // All checks passed
    return AllocationResult{true, "", requiredWeights, 0};
}

bool MemoryBudget::canAllocateKV(size_t sequenceLength,
                                 size_t batchSize,
                                 size_t numLayers,
                                 size_t numHeads,
                                 size_t headDim,
                                 size_t blockSize) const
{

    size_t required = calculateKVCacheMemory(sequenceLength, batchSize, numLayers, numHeads, headDim, blockSize);

    return required <= getRemainingBudget(Component::KV_CACHE);
}

//==============================================================================
// Budget Queries
//==============================================================================

size_t MemoryBudget::getRemainingBudget(Component component) const
{
    return getBudgetForComponent(component) - getUsageForComponent(component);
}

size_t MemoryBudget::getCurrentUsage(Component component) const
{
    return getUsageForComponent(component);
}

size_t MemoryBudget::getBudgetForComponent(Component component) const
{
    switch (component) {
    case Component::WEIGHTS:
        return limits_.weightBudget;
    case Component::KV_CACHE:
        return limits_.kvCacheBudget;
    case Component::ACTIVATIONS:
        return limits_.activationBudget;
    case Component::MISC:
        // MISC budget is whatever remains after other budgets and headroom
        return limits_.totalBudget - limits_.headroom - limits_.weightBudget - limits_.kvCacheBudget -
               limits_.activationBudget;
    }
    return 0; // Should never reach here
}

size_t MemoryBudget::getUsageForComponent(Component component) const
{
    switch (component) {
    case Component::WEIGHTS:
        return usedWeights_.load(std::memory_order_relaxed);
    case Component::KV_CACHE:
        return usedKVCache_.load(std::memory_order_relaxed);
    case Component::ACTIVATIONS:
        return usedActivations_.load(std::memory_order_relaxed);
    case Component::MISC:
        return usedMisc_.load(std::memory_order_relaxed);
    }
    return 0; // Should never reach here
}

size_t MemoryBudget::getTotalUsage() const
{
    return usedWeights_.load(std::memory_order_relaxed) + usedKVCache_.load(std::memory_order_relaxed) +
           usedActivations_.load(std::memory_order_relaxed) + usedMisc_.load(std::memory_order_relaxed);
}

double MemoryBudget::getUtilizationPercentage() const
{
    return (static_cast<double>(getTotalUsage()) / static_cast<double>(limits_.totalBudget)) * 100.0;
}

//==============================================================================
// Allocation/Deallocation
//==============================================================================

void *MemoryBudget::allocateWithBudget(size_t size, Component component)
{
    if (size == 0) {
        return nullptr;
    }

    if (size > getRemainingBudget(component)) {
        return nullptr; // Budget exceeded
    }

    void *ptr = std::malloc(size);
    if (ptr) {
        addUsage(component, size);
    }
    return ptr;
}

void MemoryBudget::freeWithBudget(void *ptr, size_t size, Component component)
{
    if (ptr) {
        std::free(ptr);
        removeUsage(component, size);
    }
}

bool MemoryBudget::reserveBudget(size_t size, Component component)
{
    if (size == 0) {
        return true;
    }
    if (size > getRemainingBudget(component)) {
        return false;
    }
    // For now, just return success
    // Could implement a reservation system for complex scenarios
    return true;
}

void MemoryBudget::releaseBudget(size_t size, Component component)
{
    // No-op for now - reservations are not tracked separately
    (void)size;
    (void)component;
}

//==============================================================================
// Utility Methods
//==============================================================================

void MemoryBudget::reset()
{
    usedWeights_.store(0, std::memory_order_relaxed);
    usedKVCache_.store(0, std::memory_order_relaxed);
    usedActivations_.store(0, std::memory_order_relaxed);
    usedMisc_.store(0, std::memory_order_relaxed);
}

void MemoryBudget::addUsage(Component component, size_t size)
{
    switch (component) {
    case Component::WEIGHTS:
        usedWeights_.fetch_add(size, std::memory_order_relaxed);
        break;
    case Component::KV_CACHE:
        usedKVCache_.fetch_add(size, std::memory_order_relaxed);
        break;
    case Component::ACTIVATIONS:
        usedActivations_.fetch_add(size, std::memory_order_relaxed);
        break;
    case Component::MISC:
        usedMisc_.fetch_add(size, std::memory_order_relaxed);
        break;
    }
}

void MemoryBudget::removeUsage(Component component, size_t size)
{
    switch (component) {
    case Component::WEIGHTS:
        usedWeights_.fetch_sub(size, std::memory_order_relaxed);
        break;
    case Component::KV_CACHE:
        usedKVCache_.fetch_sub(size, std::memory_order_relaxed);
        break;
    case Component::ACTIVATIONS:
        usedActivations_.fetch_sub(size, std::memory_order_relaxed);
        break;
    case Component::MISC:
        usedMisc_.fetch_sub(size, std::memory_order_relaxed);
        break;
    }
}

std::string MemoryBudget::formatBytes(size_t bytes)
{
    const char *units[] = {"B", "KB", "MB", "GB", "TB"};
    int unitIndex = 0;
    double size = static_cast<double>(bytes);

    while (size >= 1024.0 && unitIndex < 4) {
        size /= 1024.0;
        unitIndex++;
    }

    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2) << size << " " << units[unitIndex];
    return oss.str();
}

} // namespace runtime
} // namespace iron
