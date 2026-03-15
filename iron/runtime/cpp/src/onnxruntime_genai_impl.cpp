// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file onnxruntime_genai_impl.cpp
 * @brief Windows ONNX Runtime GenAI backend implementation
 *
 * This file contains the implementation of the ONNX Runtime GenAI
 * wrapper for Windows NPU acceleration via DirectML.
 *
 * @note This is a stub/skeleton implementation. Full implementation
 *       requires ONNX Runtime GenAI library linkage.
 */

#include <iron/runtime/onnxruntime_genai.hpp>

#ifdef _WIN32

// ONNX Runtime GenAI includes
// Note: These would be the actual includes in production
// #include <onnxruntime_genai.h>
// #include <onnxruntime_cxx_api.h>

namespace iron {
namespace runtime {

//==============================================================================
// Helper: Check ONNX Runtime GenAI availability
//==============================================================================

bool OnnxRuntimeGenAiWrapper::isAvailable() {
    // In production: Check if ONNX Runtime GenAI DLL is loadable
    // For now, return true as placeholder
    return true;
}

//==============================================================================
// OnnxBuffer Implementation
//==============================================================================

OnnxBuffer::OnnxBuffer(Ort::Value tensor, size_t size)
    : tensor_(std::move(tensor))
    , size_(size)
    , valid_(true) {
}

OnnxBuffer::OnnxBuffer(const Ort::MemoryInfo& memoryInfo, size_t size)
    : tensor_()
    , size_(size)
    , valid_(false) {

    if (size == 0) {
        throw BufferError("Cannot allocate zero-size buffer");
    }

    // In production: Allocate ONNX tensor
    // tensor_ = Ort::Value::CreateTensor(memoryInfo, ...);
    // valid_ = true;

    // Stub: Mark as valid for testing
    valid_ = true;
}

OnnxBuffer::~OnnxBuffer() {
    if (valid_) {
        // ONNX tensor automatically freed when Ort::Value goes out of scope
        tensor_ = {};
    }
}

OnnxBuffer::OnnxBuffer(OnnxBuffer&& other) noexcept
    : tensor_(std::move(other.tensor_))
    , size_(other.size_)
    , valid_(other.valid_) {

    other.valid_ = false;
}

OnnxBuffer& OnnxBuffer::operator=(OnnxBuffer&& other) noexcept {
    if (this != &other) {
        if (valid_) {
            tensor_ = {};
        }

        tensor_ = std::move(other.tensor_);
        size_ = other.size_;
        valid_ = other.valid_;

        other.valid_ = false;
    }
    return *this;
}

size_t OnnxBuffer::size() const {
    return size_;
}

void OnnxBuffer::write(const void* data, size_t size, size_t offset) {
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

    // In production: Copy data to ONNX tensor
    // void* tensorData = tensor_.GetTensorMutableData<void>();
    // std::memcpy(static_cast<char*>(tensorData) + offset, data, size);

    (void)data;  // Suppress unused warning in stub
}

void OnnxBuffer::read(void* data, size_t size, size_t offset) const {
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

    // In production: Copy data from ONNX tensor
    // const void* tensorData = tensor_.GetTensorData<void>();
    // std::memcpy(data, static_cast<const char*>(tensorData) + offset, size);

    (void)data;  // Suppress unused warning in stub
}

void OnnxBuffer::sync(bool /*to_device*/) {
    std::lock_guard<std::mutex> lock(mutex_);

    if (!valid_) {
        throw BufferError("Buffer is invalid");
    }

    // ONNX Runtime handles sync automatically
    // In production: May need explicit sync for DirectML
}

void* OnnxBuffer::nativeHandle() const {
    // In production: Return ONNX tensor handle
    // return const_cast<Ort::Value*>(&tensor_);
    return nullptr;
}

uint64_t OnnxBuffer::address() const {
    if (!valid_) {
        return 0;
    }

    // In production: Get tensor data pointer
    // auto* data = tensor_.GetTensorData<void>();
    // return reinterpret_cast<uint64_t>(data);

    return 0;
}

bool OnnxBuffer::isValid() const {
    return valid_;
}

Ort::Value& OnnxBuffer::tensor() {
    return tensor_;
}

const Ort::Value& OnnxBuffer::tensor() const {
    return tensor_;
}

//==============================================================================
// OnnxKernelHandle Implementation
//==============================================================================

OnnxKernelHandle::OnnxKernelHandle(std::unique_ptr<Ort::Session> session, const std::string& name)
    : session_(std::move(session))
    , name_(name)
    , setArgs_()
    , argInfo_() {

    if (!session_) {
        throw KernelNotFoundError(name);
    }

    // In production: Get input/output info from session
    // size_t inputCount = session_->GetInputCount();
    // for (size_t i = 0; i < inputCount; ++i) {
    //     auto name = session_->GetInputNameAllocated(i);
    //     argInfo_.push_back({name.get(), "tensor"});
    // }
    // setArgs_.resize(inputCount);
}

OnnxKernelHandle::~OnnxKernelHandle() = default;

std::string OnnxKernelHandle::name() const {
    return name_;
}

void OnnxKernelHandle::setArg(size_t index, const KernelArgument& arg) {
    std::lock_guard<std::mutex> lock(mutex_);

    // Validate index
    if (index >= 64) {  // Stub limit
        throw ArgumentError("Argument index out of range: " + std::to_string(index), index);
    }

    // Ensure setArgs_ is large enough
    if (index >= setArgs_.size()) {
        setArgs_.resize(index + 1);
    }

    setArgs_[index] = arg;
}

bool OnnxKernelHandle::validateArguments() const {
    for (const auto& arg : setArgs_) {
        if (!arg.has_value()) {
            return false;
        }
    }
    return !setArgs_.empty();
}

ExecutionResult OnnxKernelHandle::execute(const ExecutionOptions& options) {
    std::lock_guard<std::mutex> lock(mutex_);

    ExecutionResult result;

    if (!validateArguments()) {
        result.status = 1;
        result.errorMessage = "Not all arguments are set";
        return result;
    }

    // In production: Run ONNX session
    // std::vector<Ort::Value> inputValues;
    // std::vector<const char*> inputNames;
    // std::vector<Ort::Value> outputValues;
    // std::vector<const char*> outputNames;

    // // Prepare inputs
    // for (const auto& arg : setArgs_) {
    //     if (arg.has_value()) {
    //         std::visit([&inputValues](auto&& val) {
    //             if constexpr (std::is_same_v<std::decay_t<decltype(val)>, std::shared_ptr<IBuffer>>) {
    //                 if (val) {
    //                     auto* onnxBuffer = dynamic_cast<OnnxBuffer*>(val.get());
    //                     if (onnxBuffer) {
    //                         inputValues.push_back(onnxBuffer->tensor());
    //                     }
    //                 }
    //             }
    //         }, arg.value());
    //     }
    // }

    // // Execute
    // outputValues = session_->Run(
    //     Ort::RunOptions{nullptr},
    //     inputNames.data(), inputValues.data(), inputValues.size(),
    //     outputNames.data(), outputNames.size()
    // );

    // // Collect outputs
    // for (auto& output : outputValues) {
    //     // Wrap output tensor in buffer
    //     result.outputs.push_back(...);
    // }

    // Stub: Return success
    result.status = 0;

    if (options.profile) {
        // In production: Collect execution time
        result.executionTimeUs = 0;
    }

    return result;
}

void OnnxKernelHandle::reset() {
    std::lock_guard<std::mutex> lock(mutex_);
    std::fill(setArgs_.begin(), setArgs_.end(), std::optional<KernelArgument>{});
}

size_t OnnxKernelHandle::numArguments() const {
    // In production: Return session_->GetInputCount()
    return 2;  // Stub
}

bool OnnxKernelHandle::isReady() const {
    return validateArguments();
}

bool OnnxKernelHandle::isArgumentSet(size_t index) const {
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= setArgs_.size()) {
        return false;
    }
    return setArgs_[index].has_value();
}

std::pair<std::string, std::string> OnnxKernelHandle::getArgumentInfo(size_t index) const {
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= argInfo_.size()) {
        return {"", ""};
    }
    return argInfo_[index];
}

std::vector<std::string> OnnxKernelHandle::getArgumentNames() const {
    std::lock_guard<std::mutex> lock(mutex_);
    std::vector<std::string> names;
    names.reserve(argInfo_.size());
    for (const auto& info : argInfo_) {
        names.push_back(info.first);
    }
    return names;
}

//==============================================================================
// OnnxBufferManager Implementation
//==============================================================================

OnnxBufferManager::OnnxBufferManager(const Ort::MemoryInfo& memoryInfo, size_t maxPoolSize)
    : memoryInfo_(nullptr)  // Not used in stub implementation
    , maxPoolSize_(maxPoolSize)
    , totalMemoryInUse_(0)
    , activeCount_(0) {
    (void)memoryInfo;  // Unused in stub
}

OnnxBufferManager::~OnnxBufferManager() {
    clear();
}

std::shared_ptr<IBuffer> OnnxBufferManager::allocate(size_t size) {
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

    // Allocate new buffer
    // In production: Create ONNX tensor
    // Ort::Value tensor = Ort::Value::CreateTensor(memoryInfo_, ...);
    // auto buffer = std::make_shared<OnnxBuffer>(std::move(tensor), size);

    // Stub
    Ort::Value stubTensor;  // Null tensor for stub
    auto buffer = std::make_shared<OnnxBuffer>(std::move(stubTensor), size);
    totalMemoryInUse_ += size;
    activeCount_++;

    return buffer;
}

void OnnxBufferManager::deallocate(std::shared_ptr<IBuffer> buffer) {
    if (!buffer) return;

    std::lock_guard<std::mutex> lock(poolMutex_);

    auto* onnxBuffer = dynamic_cast<OnnxBuffer*>(buffer.get());
    if (!onnxBuffer || !onnxBuffer->isValid()) {
        return;  // Invalid or already freed
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

std::map<size_t, size_t> OnnxBufferManager::getPoolStats() const {
    std::lock_guard<std::mutex> lock(poolMutex_);

    std::map<size_t, size_t> stats;
    for (const auto& [size, entries] : pool_) {
        stats[size] = entries.size();
    }
    return stats;
}

void OnnxBufferManager::clear() {
    std::lock_guard<std::mutex> lock(poolMutex_);
    pool_.clear();
    totalMemoryInUse_ = 0;
    activeCount_ = 0;
}

size_t OnnxBufferManager::totalMemoryInUse() const {
    return totalMemoryInUse_.load();
}

size_t OnnxBufferManager::activeBufferCount() const {
    return activeCount_.load();
}

size_t OnnxBufferManager::pooledBufferCount() const {
    std::lock_guard<std::mutex> lock(poolMutex_);
    size_t count = 0;
    for (const auto& [_, entries] : pool_) {
        count += entries.size();
    }
    return count;
}

void OnnxBufferManager::setMaxPoolSize(size_t max_bytes) {
    std::lock_guard<std::mutex> lock(poolMutex_);
    maxPoolSize_ = max_bytes;

    // If new limit is lower than current usage, drain pool
    while (totalMemoryInUse_ > maxPoolSize_) {
        size_t largestSize = 0;
        for (const auto& [size, _] : pool_) {
            largestSize = std::max(largestSize, size);
        }
        if (largestSize == 0) break;

        auto it = pool_.find(largestSize);
        if (!it->second.empty()) {
            totalMemoryInUse_ -= it->second.back().size;
            it->second.pop_back();
        }
    }
}

size_t OnnxBufferManager::roundToBucket(size_t size) {
    constexpr size_t bucketSize = 4096;  // 4KB buckets
    return ((size + bucketSize - 1) / bucketSize) * bucketSize;
}

//==============================================================================
// OnnxRuntimeGenAiWrapper Implementation
//==============================================================================

OnnxRuntimeGenAiWrapper::OnnxRuntimeGenAiWrapper(int /*deviceId*/)
    : env_()
    , sessionOptions_()
    , memoryInfo_()
    , bufferManager_()
    , loadedModels_()
    , initialized_(false) {

    initializeSessionOptions();
}

OnnxRuntimeGenAiWrapper::~OnnxRuntimeGenAiWrapper() {
    unload();
}

void OnnxRuntimeGenAiWrapper::initializeSessionOptions() {
    // In production: Initialize ONNX Runtime environment
    // env_ = std::make_unique<Ort::Env>(ORT_LOGGING_LEVEL_WARNING, "IRON");
    // sessionOptions_ = std::make_unique<Ort::SessionOptions>();

    // // Add NPU Execution Provider (DirectML)
    // Ort::AppendExecutionProvider_DirectML(0, sessionOptions_->GetMutableSessionOptions());

    // // Memory info for CPU (host accessible buffers)
    // const char* cpuMemType = "Cpu";
    // int cpuMemId = 0;
    // memoryInfo_ = std::make_unique<Ort::MemoryInfo>(
    //     Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault)
    // );

    // // Create buffer manager
    // bufferManager_ = std::make_shared<OnnxBufferManager>(*memoryInfo_);

    // initialized_ = true;

    // Stub: Mark as initialized
    initialized_ = true;
}

bool OnnxRuntimeGenAiWrapper::loadXclbin(const std::string& path) {
    std::lock_guard<std::mutex> lock(mutex_);

    if (path.empty()) {
        throw XclbinError("Empty path");
    }

    // In production: Load ONNX model
    // auto session = std::make_unique<Ort::Session>(*env_, path.c_str(), *sessionOptions_);

    // // Get input/output names
    // std::vector<std::string> inputNames;
    // std::vector<std::string> outputNames;
    // size_t inputCount = session->GetInputCount();
    // for (size_t i = 0; i < inputCount; ++i) {
    //     inputNames.push_back(session->GetInputNameAllocated(i).get());
    // }

    // loadedModels_.push_back({path, std::move(session), inputNames, outputNames});

    // Stub: Create fake loaded model
    LoadedModel loaded;
    loaded.path = path;
    loaded.session = nullptr;  // Stub - no real session
    loaded.inputNames = {"input"};
    loaded.outputNames = {"output"};

    loadedModels_.push_back(std::move(loaded));
    return true;
}

bool OnnxRuntimeGenAiWrapper::loadXclbinFromMemory(const void* data, size_t size) {
    std::lock_guard<std::mutex> lock(mutex_);

    if (!data || size == 0) {
        throw XclbinError("Invalid data or size");
    }

    // In production: Load ONNX model from memory
    // auto session = std::make_unique<Ort::Session>(
    //     *env_, data, size, *sessionOptions_
    // );

    // Stub
    LoadedModel loaded;
    loaded.path = "<memory>";
    loaded.session = nullptr;  // Stub - no real session
    loaded.inputNames = {"input"};
    loaded.outputNames = {"output"};

    loadedModels_.push_back(std::move(loaded));
    return true;
}

bool OnnxRuntimeGenAiWrapper::unloadXclbin(const std::string& path) {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(loadedModels_.begin(), loadedModels_.end(),
        [&path](const LoadedModel& model) {
            return model.path == path;
        });

    if (it == loadedModels_.end()) {
        return false;
    }

    // ONNX session automatically freed when unique_ptr goes out of scope
    it->session.reset();
    loadedModels_.erase(it);
    return true;
}

std::vector<std::string> OnnxRuntimeGenAiWrapper::getKernelNames() const {
    std::lock_guard<std::mutex> lock(mutex_);

    std::vector<std::string> names;
    for (const auto& model : loadedModels_) {
        // In production: Use model name or derive from path
        names.push_back(model.path);
    }
    return names;
}

std::vector<std::string> OnnxRuntimeGenAiWrapper::getKernelsFromXclbin(
    const std::string& xclbinPath) const {

    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(loadedModels_.begin(), loadedModels_.end(),
        [&xclbinPath](const LoadedModel& model) {
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

bool OnnxRuntimeGenAiWrapper::hasKernel(const std::string& kernelName) const {
    std::lock_guard<std::mutex> lock(mutex_);

    // Check if any loaded model matches the kernel name
    for (const auto& model : loadedModels_) {
        if (model.path == kernelName) {
            return true;
        }
    }
    return false;
}

ExecutionResult OnnxRuntimeGenAiWrapper::execute(
    const std::string& kernelName,
    const std::vector<KernelArgument>& arguments,
    const ExecutionOptions& options) {

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

std::shared_ptr<IKernelHandle> OnnxRuntimeGenAiWrapper::getKernel(const std::string& kernelName) {
    std::lock_guard<std::mutex> lock(mutex_);

    // Find model
    auto* model = findModel(kernelName);
    if (!model) {
        return nullptr;
    }

    // Create kernel handle from session
    // Note: Ort::Session cannot be copied, so we use the existing session
    auto handle = std::make_shared<OnnxKernelHandle>(
        std::move(model->session),  // Use existing session
        kernelName
    );

    return handle;
}

std::shared_ptr<IBuffer> OnnxRuntimeGenAiWrapper::allocateBuffer(size_t size, bool /*hostAccessible*/) {
    if (!bufferManager_) {
        throw BufferError("Runtime not initialized");
    }
    return bufferManager_->allocate(size);
}

std::shared_ptr<IBuffer> OnnxRuntimeGenAiWrapper::allocateBufferFromData(const void* data, size_t size) {
    auto buffer = allocateBuffer(size, true);
    buffer->write(data, size);
    return buffer;
}

std::shared_ptr<IBufferManager> OnnxRuntimeGenAiWrapper::getBufferManager() {
    return bufferManager_;
}

void OnnxRuntimeGenAiWrapper::unload() {
    std::lock_guard<std::mutex> lock(mutex_);

    for (auto& model : loadedModels_) {
        model.session.reset();
    }
    loadedModels_.clear();

    if (bufferManager_) {
        bufferManager_->clear();
    }
}

bool OnnxRuntimeGenAiWrapper::isLoaded() const {
    std::lock_guard<std::mutex> lock(mutex_);
    return !loadedModels_.empty();
}

std::string OnnxRuntimeGenAiWrapper::getPlatformName() const {
    return "ONNX";
}

std::string OnnxRuntimeGenAiWrapper::getVersion() const {
    return "1.0.0";
}

std::string OnnxRuntimeGenAiWrapper::getPlatformVersion() const {
    // In production: Return ONNX Runtime version
    // return Ort::GetVersionString();
    return "0.11.2";  // Stub: Known available version
}

std::string OnnxRuntimeGenAiWrapper::getDeviceInfo() const {
    return R"({"platform": "ONNX Runtime GenAI", "execution_provider": "DirectML"})";
}

OnnxRuntimeGenAiWrapper::LoadedModel* OnnxRuntimeGenAiWrapper::findModel(const std::string& path) {
    for (auto& model : loadedModels_) {
        if (model.path == path) {
            return &model;
        }
    }
    return nullptr;
}

} // namespace runtime
} // namespace iron

#endif // _WIN32
