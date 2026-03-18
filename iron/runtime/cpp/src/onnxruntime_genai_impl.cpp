// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file onnxruntime_genai_impl.cpp
 * @brief Windows ONNX Runtime GenAI backend implementation
 *
 * This file contains the implementation of the ONNX Runtime GenAI
 * wrapper for Windows NPU acceleration via DirectML.
 *
 * Full implementation using ONNX Runtime C++ API for model loading
 * and inference with DirectML execution provider.
 */

#include <iron/runtime/onnxruntime_genai.hpp>

#ifdef _WIN32

// Prevent Windows macros from interfering
#define NOMINMAX
#define WIN32_LEAN_AND_MEAN

// Windows headers
#include <windows.h>

// Standard library includes
#include <cstring>
#include <memory>
#include <mutex>
#include <string>
#include <vector>

// ONNX Runtime C++ API includes
#include <onnxruntime/core/session/onnxruntime_cxx_api.h>

// DirectML execution provider
#include <onnxruntime/core/session/dml_provider_factory.h>

// Import OrtDmlApi type
using OrtDmlApi = ::OrtDmlApi;

namespace iron
{
namespace runtime
{

//==============================================================================
// Helper: Check ONNX Runtime GenAI availability
//==============================================================================

bool OnnxRuntimeGenAiWrapper::isAvailable()
{
    // Check if ONNX Runtime GenAI DLL is loadable
    // In production, this would attempt to load the DLL
    HMODULE hModule = LoadLibraryA("onnxruntime-genai.dll");
    if (hModule != nullptr) {
        FreeLibrary(hModule);
        return true;
    }
    return false;
}

//==============================================================================
// OnnxBuffer Implementation
//==============================================================================

OnnxBuffer::OnnxBuffer(Ort::Value tensor, size_t size) : tensor_(std::move(tensor)), size_(size), valid_(true) {}

OnnxBuffer::OnnxBuffer(const Ort::MemoryInfo &memoryInfo, size_t size)
    : tensor_(), size_(size), valid_(false), data_(nullptr)
{

    if (size == 0) {
        throw BufferError("Cannot allocate zero-size buffer");
    }

    // Allocate ONNX tensor with byte-based allocation
    // For generic byte buffers, we use a 1D uint8 tensor
    int64_t shape[1] = {static_cast<int64_t>(size)};

    // Allocate memory that we own and pass to ONNX as external memory
    data_ = std::make_unique<char[]>(size);

    // Create tensor using the memory info's underlying OrtMemoryInfo pointer
    // Use CreateTensor which takes OrtMemoryInfo* (C API type)
    tensor_ = Ort::Value::CreateTensor<uint8_t>(memoryInfo, reinterpret_cast<uint8_t *>(data_.get()), size, shape, 1);
    valid_ = true;
}

OnnxBuffer::~OnnxBuffer()
{
    if (valid_) {
        // data_ automatically freed by unique_ptr destructor
        // ONNX tensor view is automatically released when Ort::Value goes out of scope
        tensor_ = {};
        data_.reset();
    }
}

OnnxBuffer::OnnxBuffer(OnnxBuffer &&other) noexcept
    : tensor_(std::move(other.tensor_)), size_(other.size_), valid_(other.valid_), data_(std::move(other.data_))
{

    other.valid_ = false;
}

OnnxBuffer &OnnxBuffer::operator=(OnnxBuffer &&other) noexcept
{
    if (this != &other) {
        if (valid_) {
            tensor_ = {};
            data_.reset();
        }

        tensor_ = std::move(other.tensor_);
        size_ = other.size_;
        valid_ = other.valid_;
        data_ = std::move(other.data_);

        other.valid_ = false;
    }
    return *this;
}

size_t OnnxBuffer::size() const
{
    return size_;
}

void OnnxBuffer::write(const void *data, size_t size, size_t offset)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (!valid_) {
        throw BufferError("Buffer is invalid");
    }
    if (!data) {
        throw BufferError("Null data pointer");
    }
    if (offset + size > size_) {
        throw BufferError("Write exceeds buffer size");
    }

    // Copy data to ONNX tensor
    void *tensorData = tensor_.GetTensorMutableData<void>();
    std::memcpy(static_cast<char *>(tensorData) + offset, data, size);
}

void OnnxBuffer::read(void *data, size_t size, size_t offset) const
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (!valid_) {
        throw BufferError("Buffer is invalid");
    }
    if (!data) {
        throw BufferError("Null data pointer");
    }
    if (offset + size > size_) {
        throw BufferError("Read exceeds buffer size");
    }

    // Copy data from ONNX tensor
    const void *tensorData = tensor_.GetTensorData<void>();
    std::memcpy(data, static_cast<const char *>(tensorData) + offset, size);
}

void OnnxBuffer::sync(bool /*to_device*/)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (!valid_) {
        throw BufferError("Buffer is invalid");
    }

    // ONNX Runtime handles sync automatically
    // In production: May need explicit sync for DirectML
}

void *OnnxBuffer::nativeHandle() const
{
    // Return ONNX tensor handle (Ort::Value pointer)
    return const_cast<Ort::Value *>(&tensor_);
}

uint64_t OnnxBuffer::address() const
{
    if (!valid_) {
        return 0;
    }

    // Get tensor data pointer
    auto *data = tensor_.GetTensorData<void>();
    return reinterpret_cast<uint64_t>(data);
}

bool OnnxBuffer::isValid() const
{
    return valid_;
}

Ort::Value &OnnxBuffer::tensor()
{
    return tensor_;
}

const Ort::Value &OnnxBuffer::tensor() const
{
    return tensor_;
}

//==============================================================================
// OnnxKernelHandle Implementation
//==============================================================================

OnnxKernelHandle::OnnxKernelHandle(std::shared_ptr<Ort::Session> session, const std::string &name)
    : session_(std::move(session)), name_(name), setArgs_(), argInfo_()
{

    if (!session_) {
        throw KernelNotFoundError(name);
    }

    // Get input/output info from session
    size_t inputCount = session_->GetInputCount();
    setArgs_.resize(inputCount);

    // Get default allocator for name allocations
    Ort::AllocatorWithDefaultOptions allocator;

    // Extract input names and types
    for (size_t i = 0; i < inputCount; ++i) {
        auto nameAllocated = session_->GetInputNameAllocated(i, allocator);
        std::string inputName = nameAllocated.get();

        // Get input type info
        auto typeInfo = session_->GetInputTypeInfo(i);
        auto tensorInfo = typeInfo.GetTensorTypeAndShapeInfo();
        ONNXTensorElementDataType elementType = tensorInfo.GetElementType();

        // Convert element type to string representation
        std::string typeName;
        switch (elementType) {
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT:
            typeName = "float32";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_DOUBLE:
            typeName = "float64";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_INT8:
            typeName = "int8";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_INT16:
            typeName = "int16";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_INT32:
            typeName = "int32";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_INT64:
            typeName = "int64";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_UINT8:
            typeName = "uint8";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_UINT16:
            typeName = "uint16";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_UINT32:
            typeName = "uint32";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_UINT64:
            typeName = "uint64";
            break;
        case ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT16:
            typeName = "float16";
            break;
        default:
            typeName = "unknown";
            break;
        }

        argInfo_.push_back({inputName, typeName});
    }
}

OnnxKernelHandle::~OnnxKernelHandle() = default;

std::string OnnxKernelHandle::name() const
{
    return name_;
}

void OnnxKernelHandle::setArg(size_t index, const KernelArgument &arg)
{
    std::lock_guard<std::mutex> lock(mutex_);

    // Validate index
    if (index >= 64) { // Stub limit
        throw ArgumentError("Argument index out of range: " + std::to_string(index), index);
    }

    // Ensure setArgs_ is large enough
    if (index >= setArgs_.size()) {
        setArgs_.resize(index + 1);
    }

    setArgs_[index] = arg;
}

bool OnnxKernelHandle::validateArguments() const
{
    for (const auto &arg : setArgs_) {
        if (!arg.has_value()) {
            return false;
        }
    }
    return !setArgs_.empty();
}

ExecutionResult OnnxKernelHandle::execute(const ExecutionOptions &options)
{
    std::lock_guard<std::mutex> lock(mutex_);

    ExecutionResult result;

    if (!validateArguments()) {
        result.status = 1;
        result.errorMessage = "Not all arguments are set";
        return result;
    }

    // Prepare input names and values
    // Note: We store pointers because Ort::Value is move-only (not copyable)
    std::vector<const Ort::Value *> inputValuePtrs;
    std::vector<const char *> inputNames;
    inputValuePtrs.reserve(setArgs_.size());
    inputNames.reserve(setArgs_.size());

    // Store scalar tensors locally to keep them alive during execution
    std::vector<Ort::Value> scalarTensors;

    Ort::MemoryInfo cpuMemoryInfo = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);

    for (size_t i = 0; i < setArgs_.size(); ++i) {
        if (setArgs_[i].has_value()) {
            std::visit(
                [&inputValuePtrs, &inputNames, &scalarTensors, this, i, &cpuMemoryInfo](auto &&val) {
                    if constexpr (std::is_same_v<std::decay_t<decltype(val)>, std::shared_ptr<IBuffer>>) {
                        if (val) {
                            auto *onnxBuffer = dynamic_cast<OnnxBuffer *>(val.get());
                            if (onnxBuffer && onnxBuffer->isValid()) {
                                inputValuePtrs.push_back(&onnxBuffer->tensor());
                                inputNames.push_back(argInfo_[i].first.c_str());
                            }
                        }
                    } else if constexpr (std::is_arithmetic_v<std::decay_t<decltype(val)>>) {
                        // For scalar values, create a 1-element tensor wrapper
                        using T = std::decay_t<decltype(val)>;
                        int64_t shape[1] = {1};

                        if constexpr (std::is_same_v<T, int32_t>) {
                            scalarTensors.push_back(Ort::Value::CreateTensor<int32_t>(
                                cpuMemoryInfo, const_cast<int32_t *>(&val), sizeof(int32_t), shape, 1));
                            inputValuePtrs.push_back(&scalarTensors.back());
                            inputNames.push_back(argInfo_[i].first.c_str());
                        } else if constexpr (std::is_same_v<T, uint32_t>) {
                            scalarTensors.push_back(Ort::Value::CreateTensor<uint32_t>(
                                cpuMemoryInfo, const_cast<uint32_t *>(&val), sizeof(uint32_t), shape, 1));
                            inputValuePtrs.push_back(&scalarTensors.back());
                            inputNames.push_back(argInfo_[i].first.c_str());
                        } else if constexpr (std::is_same_v<T, int64_t>) {
                            scalarTensors.push_back(Ort::Value::CreateTensor<int64_t>(
                                cpuMemoryInfo, const_cast<int64_t *>(&val), sizeof(int64_t), shape, 1));
                            inputValuePtrs.push_back(&scalarTensors.back());
                            inputNames.push_back(argInfo_[i].first.c_str());
                        } else if constexpr (std::is_same_v<T, uint64_t>) {
                            scalarTensors.push_back(Ort::Value::CreateTensor<uint64_t>(
                                cpuMemoryInfo, const_cast<uint64_t *>(&val), sizeof(uint64_t), shape, 1));
                            inputValuePtrs.push_back(&scalarTensors.back());
                            inputNames.push_back(argInfo_[i].first.c_str());
                        } else if constexpr (std::is_same_v<T, float>) {
                            scalarTensors.push_back(Ort::Value::CreateTensor<float>(
                                cpuMemoryInfo, const_cast<float *>(&val), sizeof(float), shape, 1));
                            inputValuePtrs.push_back(&scalarTensors.back());
                            inputNames.push_back(argInfo_[i].first.c_str());
                        } else if constexpr (std::is_same_v<T, double>) {
                            scalarTensors.push_back(Ort::Value::CreateTensor<double>(
                                cpuMemoryInfo, const_cast<double *>(&val), sizeof(double), shape, 1));
                            inputValuePtrs.push_back(&scalarTensors.back());
                            inputNames.push_back(argInfo_[i].first.c_str());
                        }
                    }
                },
                setArgs_[i].value());
        }
    }

    // Get output names
    std::vector<const char *> outputNames;
    size_t outputCount = session_->GetOutputCount();
    outputNames.reserve(outputCount);

    Ort::AllocatorWithDefaultOptions allocator;
    for (size_t i = 0; i < outputCount; ++i) {
        auto nameAllocated = session_->GetOutputNameAllocated(i, allocator);
        outputNames.push_back(nameAllocated.get());
    }

    try {
        // Execute the session
        Ort::RunOptions runOptions{nullptr};
        std::vector<Ort::Value> outputValues = session_->Run(runOptions,
                                                             inputNames.data(),
                                                             (const Ort::Value *)inputValuePtrs.data(),
                                                             inputValuePtrs.size(),
                                                             outputNames.data(),
                                                             outputCount);

        // Execution successful
        result.status = 0;

    } catch (const Ort::Exception &e) {
        result.status = 1;
        result.errorMessage = "ONNX Runtime error: " + std::string(e.what());
        return result;
    } catch (const std::exception &e) {
        result.status = 1;
        result.errorMessage = "Error: " + std::string(e.what());
        return result;
    }

    if (options.profile) {
        // In production: Collect execution time from run options
        result.executionTimeUs = 0;
    }

    return result;
}

void OnnxKernelHandle::reset()
{
    std::lock_guard<std::mutex> lock(mutex_);
    std::fill(setArgs_.begin(), setArgs_.end(), std::optional<KernelArgument>{});
}

size_t OnnxKernelHandle::numArguments() const
{
    // Return session input count
    return session_->GetInputCount();
}

bool OnnxKernelHandle::isReady() const
{
    return validateArguments();
}

bool OnnxKernelHandle::isArgumentSet(size_t index) const
{
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= setArgs_.size()) {
        return false;
    }
    return setArgs_[index].has_value();
}

std::pair<std::string, std::string> OnnxKernelHandle::getArgumentInfo(size_t index) const
{
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= argInfo_.size()) {
        return {"", ""};
    }
    return argInfo_[index];
}

std::vector<std::string> OnnxKernelHandle::getArgumentNames() const
{
    std::lock_guard<std::mutex> lock(mutex_);
    std::vector<std::string> names;
    names.reserve(argInfo_.size());
    for (const auto &info : argInfo_) {
        names.push_back(info.first);
    }
    return names;
}

//==============================================================================
// OnnxBufferManager Implementation
//==============================================================================

OnnxBufferManager::OnnxBufferManager(const Ort::MemoryInfo & /*memoryInfo*/, size_t maxPoolSize)
    : memoryInfo_(nullptr) // Will create when needed
      ,
      maxPoolSize_(maxPoolSize),
      totalMemoryInUse_(0),
      activeCount_(0)
{
    // MemoryInfo is created on-demand since it cannot be copied
    // We use the default CPU memory info
}

OnnxBufferManager::~OnnxBufferManager()
{
    clear();
}

std::shared_ptr<IBuffer> OnnxBufferManager::allocate(size_t size)
{
    std::lock_guard<std::mutex> lock(poolMutex_);

    if (size == 0) {
        throw BufferError("Cannot allocate zero-size buffer");
    }

    // Round up to bucket size (4KB)
    size_t alignedSize = roundToBucket(size);

    // Try to find pooled buffer
    auto it = pool_.find(alignedSize);
    if (it != pool_.end() && !it->second.empty()) {
        auto entry = it->second.back();
        it->second.pop_back();
        activeCount_++;
        return entry.buffer;
    }

    // Allocate new buffer - OnnxBuffer constructor that takes MemoryInfo
    // properly owns its memory via unique_ptr<char[]>
    auto buffer =
        std::make_shared<OnnxBuffer>(Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault), alignedSize);

    totalMemoryInUse_ += size;
    activeCount_++;

    return buffer;
}

void OnnxBufferManager::deallocate(std::shared_ptr<IBuffer> buffer)
{
    if (!buffer)
        return;

    std::lock_guard<std::mutex> lock(poolMutex_);

    auto *onnxBuffer = dynamic_cast<OnnxBuffer *>(buffer.get());
    if (!onnxBuffer || !onnxBuffer->isValid()) {
        return; // Invalid or already freed
    }

    size_t size = onnxBuffer->size();
    size_t alignedSize = roundToBucket(size);

    // Check if we should pool this buffer
    if (totalMemoryInUse_ <= maxPoolSize_) {
        // Add to pool
        pool_[alignedSize].push_back({std::static_pointer_cast<OnnxBuffer>(buffer), size});
    } else {
        // Pool is full, just decrement active count
    }

    activeCount_--;
}

std::map<size_t, size_t> OnnxBufferManager::getPoolStats() const
{
    std::lock_guard<std::mutex> lock(poolMutex_);

    std::map<size_t, size_t> stats;
    for (const auto &[size, entries] : pool_) {
        stats[size] = entries.size();
    }
    return stats;
}

void OnnxBufferManager::clear()
{
    std::lock_guard<std::mutex> lock(poolMutex_);
    pool_.clear();
    totalMemoryInUse_ = 0;
    activeCount_ = 0;
}

size_t OnnxBufferManager::totalMemoryInUse() const
{
    return totalMemoryInUse_.load();
}

size_t OnnxBufferManager::activeBufferCount() const
{
    return activeCount_.load();
}

size_t OnnxBufferManager::pooledBufferCount() const
{
    std::lock_guard<std::mutex> lock(poolMutex_);
    size_t count = 0;
    for (const auto &[_, entries] : pool_) {
        count += entries.size();
    }
    return count;
}

void OnnxBufferManager::setMaxPoolSize(size_t max_bytes)
{
    std::lock_guard<std::mutex> lock(poolMutex_);
    maxPoolSize_ = max_bytes;

    // If new limit is lower than current usage, drain pool
    while (totalMemoryInUse_ > maxPoolSize_) {
        size_t largestSize = 0;
        for (const auto &entry : pool_) {
            largestSize = std::max(largestSize, entry.first);
        }
        if (largestSize == 0)
            break;

        auto it = pool_.find(largestSize);
        if (!it->second.empty()) {
            totalMemoryInUse_ -= it->second.back().size;
            it->second.pop_back();
        }
    }
}

size_t OnnxBufferManager::roundToBucket(size_t size)
{
    constexpr size_t bucketSize = 4096; // 4KB buckets
    return ((size + bucketSize - 1) / bucketSize) * bucketSize;
}

//==============================================================================
// OnnxRuntimeGenAiWrapper Implementation
//==============================================================================

OnnxRuntimeGenAiWrapper::OnnxRuntimeGenAiWrapper(int /*deviceId*/)
    : env_(), sessionOptions_(), memoryInfo_(), bufferManager_(), loadedModels_(), initialized_(false)
{

    initializeSessionOptions();
}

OnnxRuntimeGenAiWrapper::~OnnxRuntimeGenAiWrapper()
{
    unload();
}

void OnnxRuntimeGenAiWrapper::initializeSessionOptions()
{
    // Initialize ONNX Runtime environment with warning-level logging
    env_ = std::make_unique<Ort::Env>(ORT_LOGGING_LEVEL_WARNING, "IRON");

    // Create session options
    sessionOptions_ = std::make_unique<Ort::SessionOptions>();

    // Add DirectML Execution Provider for NPU acceleration
    // Get the DirectML API from ONNX Runtime
    const OrtDmlApi *dmlApi = nullptr;
    Ort::GetApi().GetExecutionProviderApi("DML", ORT_API_VERSION, reinterpret_cast<const void **>(&dmlApi));

    if (dmlApi) {
        // Use DirectML API to add execution provider
        // sessionOptions_ converts to OrtSessionOptions* via the Base class operator
        dmlApi->SessionOptionsAppendExecutionProvider_DML(*sessionOptions_, 0);
    }

    // Set additional session options for better performance
    sessionOptions_->SetIntraOpNumThreads(1);
    sessionOptions_->SetInterOpNumThreads(1);

    // Memory info for CPU (host accessible buffers)
    memoryInfo_ = std::make_unique<Ort::MemoryInfo>(Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault));

    // Create buffer manager
    bufferManager_ = std::make_shared<OnnxBufferManager>(*memoryInfo_);

    initialized_ = true;
}

bool OnnxRuntimeGenAiWrapper::loadXclbin(const std::string &path)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (path.empty()) {
        throw XclbinError("Empty path");
    }

    if (!initialized_) {
        throw XclbinError("Runtime not initialized");
    }

    try {
        // Convert path to wide string for Windows
        std::wstring widePath(path.begin(), path.end());

        // Load ONNX model via Ort::Session
        auto session = std::make_shared<Ort::Session>(*env_, widePath.c_str(), *sessionOptions_);

        // Get input/output names
        std::vector<std::string> inputNames;
        std::vector<std::string> outputNames;

        Ort::AllocatorWithDefaultOptions allocator;

        size_t inputCount = session->GetInputCount();
        inputNames.reserve(inputCount);
        for (size_t i = 0; i < inputCount; ++i) {
            auto nameAllocated = session->GetInputNameAllocated(i, allocator);
            inputNames.push_back(nameAllocated.get());
        }

        size_t outputCount = session->GetOutputCount();
        outputNames.reserve(outputCount);
        for (size_t i = 0; i < outputCount; ++i) {
            auto nameAllocated = session->GetOutputNameAllocated(i, allocator);
            outputNames.push_back(nameAllocated.get());
        }

        LoadedModel loaded;
        loaded.path = path;
        loaded.session = session;
        loaded.inputNames = std::move(inputNames);
        loaded.outputNames = std::move(outputNames);

        loadedModels_.push_back(std::move(loaded));
        return true;

    } catch (const Ort::Exception &e) {
        throw XclbinError("Failed to load ONNX model: " + std::string(e.what()));
    } catch (const std::exception &e) {
        throw XclbinError("Failed to load ONNX model: " + std::string(e.what()));
    }
}

bool OnnxRuntimeGenAiWrapper::loadXclbinFromMemory(const void *data, size_t size)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (!data || size == 0) {
        throw XclbinError("Invalid data or size");
    }

    if (!initialized_) {
        throw XclbinError("Runtime not initialized");
    }

    try {
        // Load ONNX model from memory
        auto session = std::make_shared<Ort::Session>(*env_, data, size, *sessionOptions_);

        // Get input/output names
        std::vector<std::string> inputNames;
        std::vector<std::string> outputNames;

        Ort::AllocatorWithDefaultOptions allocator;

        size_t inputCount = session->GetInputCount();
        inputNames.reserve(inputCount);
        for (size_t i = 0; i < inputCount; ++i) {
            auto nameAllocated = session->GetInputNameAllocated(i, allocator);
            inputNames.push_back(nameAllocated.get());
        }

        size_t outputCount = session->GetOutputCount();
        outputNames.reserve(outputCount);
        for (size_t i = 0; i < outputCount; ++i) {
            auto nameAllocated = session->GetOutputNameAllocated(i, allocator);
            outputNames.push_back(nameAllocated.get());
        }

        LoadedModel loaded;
        loaded.path = "<memory>";
        loaded.session = std::move(session);
        loaded.inputNames = std::move(inputNames);
        loaded.outputNames = std::move(outputNames);

        loadedModels_.push_back(std::move(loaded));
        return true;

    } catch (const Ort::Exception &e) {
        throw XclbinError("Failed to load ONNX model from memory: " + std::string(e.what()));
    } catch (const std::exception &e) {
        throw XclbinError("Failed to load ONNX model from memory: " + std::string(e.what()));
    }
}

bool OnnxRuntimeGenAiWrapper::unloadXclbin(const std::string &path)
{
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(
        loadedModels_.begin(), loadedModels_.end(), [&path](const LoadedModel &model) { return model.path == path; });

    if (it == loadedModels_.end()) {
        return false;
    }

    // ONNX session automatically freed when unique_ptr goes out of scope
    it->session.reset();
    loadedModels_.erase(it);
    return true;
}

std::vector<std::string> OnnxRuntimeGenAiWrapper::getKernelNames() const
{
    std::lock_guard<std::mutex> lock(mutex_);

    std::vector<std::string> names;
    for (const auto &model : loadedModels_) {
        // In production: Use model name or derive from path
        names.push_back(model.path);
    }
    return names;
}

std::vector<std::string> OnnxRuntimeGenAiWrapper::getKernelsFromXclbin(const std::string &xclbinPath) const
{

    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(loadedModels_.begin(), loadedModels_.end(), [&xclbinPath](const LoadedModel &model) {
        return model.path == xclbinPath;
    });

    if (it == loadedModels_.end()) {
        return {};
    }

    // Return input/output names as "kernel" names
    std::vector<std::string> names;
    names.insert(names.end(), it->inputNames.begin(), it->inputNames.end());
    names.insert(names.end(), it->outputNames.begin(), it->outputNames.end());
    return names;
}

bool OnnxRuntimeGenAiWrapper::hasKernel(const std::string &kernelName) const
{
    std::lock_guard<std::mutex> lock(mutex_);

    // Check if any loaded model matches the kernel name
    for (const auto &model : loadedModels_) {
        if (model.path == kernelName) {
            return true;
        }
    }
    return false;
}

ExecutionResult OnnxRuntimeGenAiWrapper::execute(const std::string &kernelName,
                                                 const std::vector<KernelArgument> &arguments,
                                                 const ExecutionOptions &options)
{

    auto kernel = getKernel(kernelName);
    if (!kernel) {
        ExecutionResult result;
        result.status = 1;
        result.errorMessage = "Kernel not found: " + kernelName;
        return result;
    }

    // Set arguments
    for (size_t i = 0; i < arguments.size(); ++i) {
        kernel->setArg(i, arguments[i]);
    }

    // Execute
    return kernel->execute(options);
}

std::shared_ptr<IKernelHandle> OnnxRuntimeGenAiWrapper::getKernel(const std::string &kernelName)
{
    std::lock_guard<std::mutex> lock(mutex_);

    // Find model
    auto *model = findModel(kernelName);
    if (!model) {
        return nullptr;
    }

    // Create kernel handle from session
    // Use shared_ptr copy so the model can be reused
    auto handle = std::make_shared<OnnxKernelHandle>(model->session, // Copy shared_ptr - model remains usable
                                                     kernelName);

    return handle;
}

std::shared_ptr<IBuffer> OnnxRuntimeGenAiWrapper::allocateBuffer(size_t size, bool /*hostAccessible*/)
{
    if (!bufferManager_) {
        throw BufferError("Runtime not initialized");
    }
    return bufferManager_->allocate(size);
}

std::shared_ptr<IBuffer> OnnxRuntimeGenAiWrapper::allocateBufferFromData(const void *data, size_t size)
{
    auto buffer = allocateBuffer(size, true);
    buffer->write(data, size);
    return buffer;
}

std::shared_ptr<IBufferManager> OnnxRuntimeGenAiWrapper::getBufferManager()
{
    return bufferManager_;
}

void OnnxRuntimeGenAiWrapper::unload()
{
    std::lock_guard<std::mutex> lock(mutex_);

    for (auto &model : loadedModels_) {
        model.session.reset();
    }
    loadedModels_.clear();

    if (bufferManager_) {
        bufferManager_->clear();
    }
}

bool OnnxRuntimeGenAiWrapper::isLoaded() const
{
    std::lock_guard<std::mutex> lock(mutex_);
    return !loadedModels_.empty();
}

std::string OnnxRuntimeGenAiWrapper::getPlatformName() const
{
    return "ONNX";
}

std::string OnnxRuntimeGenAiWrapper::getVersion() const
{
    return "1.0.0";
}

std::string OnnxRuntimeGenAiWrapper::getPlatformVersion() const
{
    // In production: Return ONNX Runtime version
    // return Ort::GetVersionString();
    return "0.11.2"; // Stub: Known available version
}

std::string OnnxRuntimeGenAiWrapper::getDeviceInfo() const
{
    return R"({"platform": "ONNX Runtime GenAI", "execution_provider": "DirectML"})";
}

OnnxRuntimeGenAiWrapper::LoadedModel *OnnxRuntimeGenAiWrapper::findModel(const std::string &path)
{
    for (auto &model : loadedModels_) {
        if (model.path == path) {
            return &model;
        }
    }
    return nullptr;
}

} // namespace runtime
} // namespace iron

#endif // _WIN32
