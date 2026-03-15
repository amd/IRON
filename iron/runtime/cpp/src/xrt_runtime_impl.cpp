// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file xrt_runtime_impl.cpp
 * @brief Linux XRT runtime implementation details
 *
 * This file contains the actual implementation of the XrtRuntimeWrapper class.
 * It is separated from the header to reduce compilation dependencies
 * and hide XRT includes from users.
 *
 * @note This is a stub implementation. Full implementation requires
 *       the AMD/Xilinx XRT library.
 */

#include <iron/runtime/xrt_runtime_wrapper.hpp>

#if defined(__linux__)

// XRT includes would go here in production
// #include <xrt/xrt_device.h>
// #include <xrt/xrt_kernel.h>
// #include <xrt/xrt_bo.h>

namespace iron {
namespace runtime {

//==============================================================================
// XrtBuffer Implementation
//==============================================================================

XrtBuffer::XrtBuffer(xrt::buffer buffer)
    : buffer_(std::move(buffer))
    , size_(0)
    , valid_(false) {

    if (buffer_) {
        // In production: size_ = buffer_.size();
        valid_ = true;
    }
}

XrtBuffer::XrtBuffer(const xrt::device& device, size_t size, bool /*hostAccessible*/)
    : buffer_()
    , size_(size)
    , valid_(false) {

    if (size == 0) {
        throw BufferError("Cannot allocate zero-size buffer");
    }

    // In production: Allocate XRT buffer
    // buffer_ = xrt::bo(device, size, XRT_BO_FLAGS_HOSTABLE);
    // valid_ = true;

    // Stub: Mark as valid for testing
    valid_ = true;
}

XrtBuffer::~XrtBuffer() {
    if (valid_.exchange(false)) {
        // XRT buffer is automatically freed when xrt::bo goes out of scope
        buffer_ = {};
    }
}

XrtBuffer::XrtBuffer(XrtBuffer&& other) noexcept
    : buffer_(std::move(other.buffer_))
    , size_(other.size_)
    , valid_(other.valid_.load()) {

    other.valid_ = false;
}

XrtBuffer& XrtBuffer::operator=(XrtBuffer&& other) noexcept {
    if (this != &other) {
        if (valid_.exchange(false)) {
            buffer_ = {};
        }

        buffer_ = std::move(other.buffer_);
        size_ = other.size_;
        valid_ = other.valid_.load();

        other.valid_ = false;
    }
    return *this;
}

size_t XrtBuffer::size() const {
    return size_;
}

void XrtBuffer::write(const void* data, size_t size, size_t offset) {
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

    // In production: Use XRT buffer write
    // buffer_.write(data, size, offset);

    (void)data;  // Suppress unused warning
}

void XrtBuffer::read(void* data, size_t size, size_t offset) const {
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

    // In production: Use XRT buffer read
    // buffer_.read(data, size, offset);

    (void)data;  // Suppress unused warning
}

void XrtBuffer::sync(bool to_device) {
    std::lock_guard<std::mutex> lock(mutex_);

    if (!valid_) {
        throw BufferError("Buffer is invalid");
    }

    // In production: Sync XRT buffer
    // if (to_device) {
    //     buffer_.sync(XCL_BO_SYNC_BO_TO_DEVICE);
    // } else {
    //     buffer_.sync(XCL_BO_SYNC_BO_FROM_DEVICE);
    // }
}

void* XrtBuffer::nativeHandle() const {
    // In production: Return XRT buffer handle
    // return const_cast<xrt::buffer*>(&buffer_);
    return nullptr;
}

uint64_t XrtBuffer::address() const {
    if (!valid_) {
        return 0;
    }

    // In production: Get XRT buffer address
    // return buffer_.address();

    return 0;
}

bool XrtBuffer::isValid() const {
    return valid_.load();
}

xrt::buffer& XrtBuffer::xrtBuffer() {
    return buffer_;
}

const xrt::buffer& XrtBuffer::xrtBuffer() const {
    return buffer_;
}

//==============================================================================
// XrtKernelHandle Implementation
//==============================================================================

XrtKernelHandle::XrtKernelHandle(xrt::kernel kernel, const std::string& name)
    : kernel_(std::move(kernel))
    , name_(name)
    , setArgs_(0) {

    if (!kernel_) {
        throw KernelNotFoundError(name);
    }

    // In production: Get argument count from kernel
    // numArgs_ = kernel_.arg_count();
    // setArgs_.resize(numArgs_);

    // Initialize argument info
    // In production: Query from kernel metadata
    // for (uint32_t i = 0; i < numArgs_; ++i) {
    //     argInfo_[i] = {kernel_.arg_name(i), kernel_.arg_type(i)};
    // }
}

XrtKernelHandle::~XrtKernelHandle() = default;

std::string XrtKernelHandle::name() const {
    return name_;
}

void XrtKernelHandle::setArg(size_t index, const KernelArgument& arg) {
    std::lock_guard<std::mutex> lock(mutex_);

    // In production: Validate index against numArgs_
    if (index >= 16) {  // Stub limit
        throw ArgumentError("Argument index out of range: " + std::to_string(index), index);
    }

    // Ensure setArgs_ is large enough
    if (index >= setArgs_.size()) {
        setArgs_.resize(index + 1);
    }

    setArgs_[index] = arg;

    // Apply argument to XRT kernel
    applyArgument(index, arg);
}

void XrtKernelHandle::applyArgument(size_t index, const KernelArgument& arg) {
    // In production: Set argument in XRT kernel
    std::visit([this, index](auto&& val) {
        using T = std::decay_t<decltype(val)>;

        if constexpr (std::is_same_v<T, std::shared_ptr<IBuffer>>) {
            // Buffer argument
            if (val) {
                auto* xrtBuffer = dynamic_cast<XrtBuffer*>(val.get());
                if (xrtBuffer) {
                    // kernel_.set_arg(index, xrtBuffer->xrtBuffer());
                }
            }
        } else if constexpr (std::is_integral_v<T>) {
            // Integer argument
            // kernel_.set_arg(index, val);
        } else if constexpr (std::is_floating_point_v<T>) {
            // Float argument
            // kernel_.set_arg(index, val);
        }
    }, arg);
}

ExecutionResult XrtKernelHandle::execute(const ExecutionOptions& options) {
    std::lock_guard<std::mutex> lock(mutex_);

    ExecutionResult result;

    if (!isReady()) {
        result.status = 1;
        result.errorMessage = "Kernel not ready: not all arguments are set";
        return result;
    }

    // In production: Execute XRT kernel
    // auto run = kernel_(/* args */);
    // run.wait2();  // Wait with timeout if specified

    // if (options.profile) {
    //     result.executionTimeUs = run.get_execution_time();
    // }

    // Stub: Return success
    result.status = 0;

    return result;
}

void XrtKernelHandle::reset() {
    std::lock_guard<std::mutex> lock(mutex_);
    std::fill(setArgs_.begin(), setArgs_.end(), std::optional<KernelArgument>{});
}

size_t XrtKernelHandle::numArguments() const {
    // In production: Return kernel_.arg_count()
    return 6;  // Stub
}

bool XrtKernelHandle::isReady() const {
    std::lock_guard<std::mutex> lock(mutex_);
    for (const auto& arg : setArgs_) {
        if (!arg.has_value()) {
            return false;
        }
    }
    return !setArgs_.empty();
}

bool XrtKernelHandle::isArgumentSet(size_t index) const {
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= setArgs_.size()) {
        return false;
    }
    return setArgs_[index].has_value();
}

std::pair<std::string, std::string> XrtKernelHandle::getArgumentInfo(size_t index) const {
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= argInfo_.size()) {
        return {"", ""};
    }
    return argInfo_[index];
}

std::vector<std::string> XrtKernelHandle::getArgumentNames() const {
    std::lock_guard<std::mutex> lock(mutex_);
    std::vector<std::string> names;
    names.reserve(argInfo_.size());
    for (const auto& info : argInfo_) {
        names.push_back(info.first);
    }
    return names;
}

xrt::kernel& XrtKernelHandle::xrtKernel() {
    return kernel_;
}

const xrt::kernel& XrtKernelHandle::xrtKernel() const {
    return kernel_;
}

//==============================================================================
// XrtBufferManager Implementation
//==============================================================================

XrtBufferManager::XrtBufferManager(const xrt::device& device, size_t maxPoolSize)
    : device_(device)
    , maxPoolSize_(maxPoolSize)
    , totalMemoryInUse_(0)
    , activeCount_(0) {
}

XrtBufferManager::~XrtBufferManager() {
    clear();
}

std::shared_ptr<IBuffer> XrtBufferManager::allocate(size_t size) {
    std::lock_guard<std::mutex> lock(poolMutex_);

    if (size == 0) {
        throw BufferError("Cannot allocate zero-size buffer");
    }

    // Round up to page size (4KB)
    constexpr size_t pageSize = 4096;
    size_t alignedSize = roundToBucket(size);

    // Try to find a pooled buffer of this size
    auto it = pool_.find(alignedSize);
    if (it != pool_.end() && !it->second.empty()) {
        auto entry = it->second.back();
        it->second.pop_back();
        activeCount_++;
        return entry.buffer;
    }

    // Allocate new buffer
    // In production: Create XRT buffer
    // xrt::buffer xrtBuf(device_, size, XRT_BO_FLAGS_HOSTABLE);
    // auto buffer = std::make_shared<XrtBuffer>(std::move(xrtBuf));

    // Stub
    xrt::buffer stubBuffer;  // Null buffer for stub
    auto buffer = std::make_shared<XrtBuffer>(stubBuffer);
    totalMemoryInUse_ += size;
    activeCount_++;

    return buffer;
}

void XrtBufferManager::deallocate(std::shared_ptr<IBuffer> buffer) {
    if (!buffer) return;

    std::lock_guard<std::mutex> lock(poolMutex_);

    auto* xrtBuffer = dynamic_cast<XrtBuffer*>(buffer.get());
    if (!xrtBuffer || !xrtBuffer->isValid()) {
        return;  // Invalid or already freed
    }

    size_t size = xrtBuffer->size();
    size_t alignedSize = roundToBucket(size);

    // Check if we should pool this buffer
    if (totalMemoryInUse_ <= maxPoolSize_) {
        // Add to pool
        pool_[alignedSize].push_back({std::static_pointer_cast<XrtBuffer>(buffer), size});
    } else {
        // Pool is full, just decrement active count
    }

    activeCount_--;
}

std::map<size_t, size_t> XrtBufferManager::getPoolStats() const {
    std::lock_guard<std::mutex> lock(poolMutex_);

    std::map<size_t, size_t> stats;
    for (const auto& [size, entries] : pool_) {
        stats[size] = entries.size();
    }
    return stats;
}

void XrtBufferManager::clear() {
    std::lock_guard<std::mutex> lock(poolMutex_);
    pool_.clear();
    totalMemoryInUse_ = 0;
    activeCount_ = 0;
}

size_t XrtBufferManager::totalMemoryInUse() const {
    return totalMemoryInUse_.load();
}

size_t XrtBufferManager::activeBufferCount() const {
    return activeCount_.load();
}

size_t XrtBufferManager::pooledBufferCount() const {
    std::lock_guard<std::mutex> lock(poolMutex_);
    size_t count = 0;
    for (const auto& [_, entries] : pool_) {
        count += entries.size();
    }
    return count;
}

void XrtBufferManager::setMaxPoolSize(size_t max_bytes) {
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

size_t XrtBufferManager::roundToBucket(size_t size) {
    constexpr size_t bucketSize = 4096;  // 4KB buckets
    return ((size + bucketSize - 1) / bucketSize) * bucketSize;
}

//==============================================================================
// XrtRuntimeWrapper Implementation
//==============================================================================

XrtRuntimeWrapper::XrtRuntimeWrapper(int deviceId)
    : deviceId_(deviceId)
    , device_(nullptr)
    , bufferManager_(nullptr)
    , initialized_(false) {

    initializeDevice();
}

XrtRuntimeWrapper::~XrtRuntimeWrapper() {
    unload();
}

void XrtRuntimeWrapper::initializeDevice() {
    // In production: Initialize XRT device
    // device_ = std::make_unique<xrt::device>(deviceId_);

    // Create buffer manager
    // bufferManager_ = std::make_shared<XrtBufferManager>(*device_);

    // Stub
    device_ = std::make_unique<xrt::device>();
    bufferManager_ = std::make_shared<XrtBufferManager>(*device_);
    initialized_ = true;
}

bool XrtRuntimeWrapper::loadXclbin(const std::string& path) {
    std::lock_guard<std::mutex> lock(mutex_);

    if (path.empty()) {
        throw XclbinError("Empty path");
    }

    // In production: Load xclbin via XRT
    // auto xclbin = xrt::xclbin(path);
    // device_->register_xclbin(xclbin);
    // auto hwContext = xrt::hw_context(device_->get_uuid(xclbin));

    // Stub: Create fake loaded xclbin
    LoadedXclbin loaded;
    loaded.path = path;
    loaded.kernelNames = {"kernel_stub"};
    loaded.hwContext = std::make_unique<xrt::hw_context>();

    loadedXclbins_.push_back(std::move(loaded));
    return true;
}

bool XrtRuntimeWrapper::loadXclbinFromMemory(const void* data, size_t size) {
    std::lock_guard<std::mutex> lock(mutex_);

    if (!data || size == 0) {
        throw XclbinError("Invalid data or size");
    }

    // In production: Load xclbin from memory
    // auto xclbin = xrt::xclbin(data, size);

    // Stub
    LoadedXclbin loaded;
    loaded.path = "<memory>";
    loaded.kernelNames = {"kernel_stub"};
    loaded.hwContext = std::make_unique<xrt::hw_context>();

    loadedXclbins_.push_back(std::move(loaded));
    return true;
}

bool XrtRuntimeWrapper::unloadXclbin(const std::string& path) {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(loadedXclbins_.begin(), loadedXclbins_.end(),
        [&path](const LoadedXclbin& xclbin) {
            return xclbin.path == path;
        });

    if (it == loadedXclbins_.end()) {
        return false;
    }

    // In production: Release hardware context
    it->hwContext.reset();

    loadedXclbins_.erase(it);
    return true;
}

std::vector<std::string> XrtRuntimeWrapper::getKernelNames() const {
    std::lock_guard<std::mutex> lock(mutex_);

    std::vector<std::string> names;
    for (const auto& xclbin : loadedXclbins_) {
        names.insert(names.end(), xclbin.kernelNames.begin(), xclbin.kernelNames.end());
    }
    return names;
}

std::vector<std::string> XrtRuntimeWrapper::getKernelsFromXclbin(const std::string& xclbinPath) const {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(loadedXclbins_.begin(), loadedXclbins_.end(),
        [&xclbinPath](const LoadedXclbin& xclbin) {
            return xclbin.path == xclbinPath;
        });

    if (it == loadedXclbins_.end()) {
        return {};
    }

    return it->kernelNames;
}

bool XrtRuntimeWrapper::hasKernel(const std::string& kernelName) const {
    std::lock_guard<std::mutex> lock(mutex_);

    for (const auto& xclbin : loadedXclbins_) {
        if (std::find(xclbin.kernelNames.begin(), xclbin.kernelNames.end(), kernelName)
            != xclbin.kernelNames.end()) {
            return true;
        }
    }
    return false;
}

ExecutionResult XrtRuntimeWrapper::execute(
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

std::shared_ptr<IKernelHandle> XrtRuntimeWrapper::getKernel(const std::string& kernelName) {
    std::lock_guard<std::mutex> lock(mutex_);

    // In production: Get kernel from hardware context
    // auto* handle = getKernelHandleInternal(kernelName);

    // Stub
    xrt::kernel stubKernel;  // Null kernel
    auto handle = std::make_shared<XrtKernelHandle>(stubKernel, kernelName);
    return handle;
}

std::shared_ptr<IBuffer> XrtRuntimeWrapper::allocateBuffer(size_t size, bool /*hostAccessible*/) {
    if (!bufferManager_) {
        throw BufferError("Runtime not initialized");
    }
    return bufferManager_->allocate(size);
}

std::shared_ptr<IBuffer> XrtRuntimeWrapper::allocateBufferFromData(const void* data, size_t size) {
    auto buffer = allocateBuffer(size, true);
    buffer->write(data, size);
    return buffer;
}

std::shared_ptr<IBufferManager> XrtRuntimeWrapper::getBufferManager() {
    return bufferManager_;
}

void XrtRuntimeWrapper::unload() {
    std::lock_guard<std::mutex> lock(mutex_);

    for (auto& xclbin : loadedXclbins_) {
        xclbin.hwContext.reset();
    }
    loadedXclbins_.clear();

    if (bufferManager_) {
        bufferManager_->clear();
    }
}

bool XrtRuntimeWrapper::isLoaded() const {
    std::lock_guard<std::mutex> lock(mutex_);
    return !loadedXclbins_.empty();
}

std::string XrtRuntimeWrapper::getPlatformName() const {
    return "XRT";
}

std::string XrtRuntimeWrapper::getVersion() const {
    return "1.0.0";
}

std::string XrtRuntimeWrapper::getPlatformVersion() const {
    return getXrtVersion();
}

std::string XrtRuntimeWrapper::getDeviceInfo() const {
    // In production: Query device info from XRT
    return R"({"device_id":)" + std::to_string(deviceId_) + R"(, "platform": "XRT"})";
}

} // namespace runtime
} // namespace iron

#endif // __linux__
