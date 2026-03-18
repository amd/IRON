// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file xdna_runtime_impl.cpp
 * @brief Windows xDNA runtime implementation details
 *
 * This file contains the actual implementation of the XdnaRuntime class.
 * It is separated from the header to reduce compilation dependencies
 * and hide xDNA SDK includes from users.
 *
 * @note This is a stub implementation. Full implementation requires
 *       the AMD xDNA Runtime SDK.
 */

#include <iron/runtime/xdna_runtime.hpp>

#if defined(_WIN32) || defined(_WIN64)

// xDNA SDK includes would go here in production
// #include <xdna/xdna.h>
// #include <xdna/xdna_runtime.h>

namespace iron
{
namespace runtime
{

//==============================================================================
// XdnaBuffer Implementation
//==============================================================================

XdnaBuffer::XdnaBuffer(xdna_detail::BufferHandle handle, size_t size) : handle_(handle), size_(size), valid_(true)
{

    if (!handle_ || size == 0) {
        throw BufferError("Invalid buffer handle or size");
    }
}

XdnaBuffer::~XdnaBuffer()
{
    if (valid_.exchange(false)) {
        // In production: Release xDNA buffer handle
        // xdnaReleaseBuffer(handle_);
        handle_ = nullptr;
    }
}

XdnaBuffer::XdnaBuffer(XdnaBuffer &&other) noexcept
    : handle_(other.handle_), size_(other.size_), valid_(other.valid_.load())
{

    other.handle_ = nullptr;
    other.valid_ = false;
}

XdnaBuffer &XdnaBuffer::operator=(XdnaBuffer &&other) noexcept
{
    if (this != &other) {
        if (valid_.exchange(false)) {
            // Release current buffer
            // xdnaReleaseBuffer(handle_);
        }

        handle_ = other.handle_;
        size_ = other.size_;
        valid_ = other.valid_.load();

        other.handle_ = nullptr;
        other.valid_ = false;
    }
    return *this;
}

size_t XdnaBuffer::size() const
{
    return size_;
}

void XdnaBuffer::write(const void *data, size_t size, size_t offset)
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

    // In production: Use xDNA DMA transfer
    // xdnaBufferWrite(handle_, data, size, offset);

    // Stub: Just copy to temporary storage
    (void)data; // Suppress unused warning
}

void XdnaBuffer::read(void *data, size_t size, size_t offset) const
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

    // In production: Use xDNA DMA transfer
    // xdnaBufferRead(handle_, data, size, offset);

    // Stub: Just copy from temporary storage
    (void)data; // Suppress unused warning
}

void XdnaBuffer::sync(bool to_device)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (!valid_) {
        throw BufferError("Buffer is invalid");
    }

    // In production: Sync buffer with device
    // xdnaBufferSync(handle_, to_device ? XDNA_SYNC_TO_DEVICE : XDNA_SYNC_TO_HOST);
}

void *XdnaBuffer::nativeHandle() const
{
    return handle_;
}

uint64_t XdnaBuffer::address() const
{
    if (!valid_) {
        return 0;
    }

    // In production: Get device address from xDNA
    // return xdnaBufferGetAddress(handle_);

    return reinterpret_cast<uint64_t>(handle_);
}

bool XdnaBuffer::isValid() const
{
    return valid_.load();
}

//==============================================================================
// XdnaKernelHandle Implementation
//==============================================================================

XdnaKernelHandle::XdnaKernelHandle(xdna_detail::KernelHandle handle, const std::string &name, size_t numArgs)
    : handle_(handle), name_(name), numArgs_(numArgs), setArgs_(numArgs)
{

    if (!handle_) {
        throw KernelNotFoundError(name);
    }

    // Initialize argument info (in production, query from kernel metadata)
    argInfo_.resize(numArgs);
    for (size_t i = 0; i < numArgs; ++i) {
        argInfo_[i] = {"arg" + std::to_string(i), "unknown"};
    }
}

XdnaKernelHandle::~XdnaKernelHandle() = default;

std::string XdnaKernelHandle::name() const
{
    return name_;
}

void XdnaKernelHandle::setArg(size_t index, const KernelArgument &arg)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (index >= numArgs_) {
        throw ArgumentError("Argument index out of range: " + std::to_string(index), index);
    }

    // Validate argument type if we have type info
    // In production: Check against kernel argument types

    setArgs_[index] = arg;

    // In production: Set argument in xDNA kernel
    // std::visit([&](auto&& val) {
    //     xdnaKernelSetArg(handle_, static_cast<uint32_t>(index), val);
    // }, arg);
}

ExecutionResult XdnaKernelHandle::execute(const ExecutionOptions &options)
{
    std::lock_guard<std::mutex> lock(mutex_);

    ExecutionResult result;

    if (!isReady()) {
        result.status = 1;
        result.errorMessage = "Kernel not ready: not all arguments are set";
        return result;
    }

    // In production: Execute kernel via xDNA
    // uint64_t startTime = 0;
    // if (options.profile) {
    //     startTime = xdnaGetTimestamp();
    // }

    // int status = xdnaKernelExecute(handle_, options.timeoutMs);

    // if (options.profile) {
    //     result.executionTimeUs = xdnaGetTimestamp() - startTime;
    // }

    // Stub: Return success
    result.status = 0;

    return result;
}

void XdnaKernelHandle::reset()
{
    std::lock_guard<std::mutex> lock(mutex_);
    std::fill(setArgs_.begin(), setArgs_.end(), std::optional<KernelArgument>{});
}

size_t XdnaKernelHandle::numArguments() const
{
    return numArgs_;
}

bool XdnaKernelHandle::isReady() const
{
    std::lock_guard<std::mutex> lock(mutex_);
    for (const auto &arg : setArgs_) {
        if (!arg.has_value()) {
            return false;
        }
    }
    return true;
}

bool XdnaKernelHandle::isArgumentSet(size_t index) const
{
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= setArgs_.size()) {
        return false;
    }
    return setArgs_[index].has_value();
}

std::pair<std::string, std::string> XdnaKernelHandle::getArgumentInfo(size_t index) const
{
    std::lock_guard<std::mutex> lock(mutex_);
    if (index >= argInfo_.size()) {
        return {"", ""};
    }
    return argInfo_[index];
}

std::vector<std::string> XdnaKernelHandle::getArgumentNames() const
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
// XdnaBufferManager Implementation
//==============================================================================

XdnaBufferManager::XdnaBufferManager(size_t maxPoolSize)
    : maxPoolSize_(maxPoolSize), totalMemoryInUse_(0), activeCount_(0)
{
}

XdnaBufferManager::~XdnaBufferManager()
{
    clear();
}

std::shared_ptr<IBuffer> XdnaBufferManager::allocate(size_t size)
{
    std::lock_guard<std::mutex> lock(poolMutex_);

    if (size == 0) {
        throw BufferError("Cannot allocate zero-size buffer");
    }

    // Round up to page size (4KB)
    constexpr size_t pageSize = 4096;
    size_t alignedSize = ((size + pageSize - 1) / pageSize) * pageSize;

    // Try to find a pooled buffer of this size
    auto it = pool_.find(alignedSize);
    if (it != pool_.end() && !it->second.empty()) {
        auto entry = it->second.back();
        it->second.pop_back();
        activeCount_++;
        return entry.buffer;
    }

    // Allocate new buffer
    // In production: Create xDNA buffer
    // xdna_detail::BufferHandle handle = xdnaBufferCreate(size);
    // auto buffer = std::make_shared<XdnaBuffer>(handle, size);

    // Stub: Create with null handle (for testing interface)
    auto buffer = std::make_shared<XdnaBuffer>(nullptr, size);
    totalMemoryInUse_ += size;
    activeCount_++;

    return buffer;
}

void XdnaBufferManager::deallocate(std::shared_ptr<IBuffer> buffer)
{
    if (!buffer)
        return;

    std::lock_guard<std::mutex> lock(poolMutex_);

    auto *xdnaBuffer = dynamic_cast<XdnaBuffer *>(buffer.get());
    if (!xdnaBuffer || !xdnaBuffer->isValid()) {
        return; // Invalid or already freed
    }

    size_t size = xdnaBuffer->size();
    size_t alignedSize = ((size + 4095) / 4096) * 4096;

    // Check if we should pool this buffer
    if (totalMemoryInUse_ <= maxPoolSize_) {
        // Add to pool
        pool_[alignedSize].push_back({std::static_pointer_cast<XdnaBuffer>(buffer), size});
    } else {
        // Pool is full, just decrement active count
        // Buffer will be freed when shared_ptr goes out of scope
    }

    activeCount_--;
}

std::map<size_t, size_t> XdnaBufferManager::getPoolStats() const
{
    std::lock_guard<std::mutex> lock(poolMutex_);

    std::map<size_t, size_t> stats;
    for (const auto &[size, entries] : pool_) {
        stats[size] = entries.size();
    }
    return stats;
}

void XdnaBufferManager::clear()
{
    std::lock_guard<std::mutex> lock(poolMutex_);
    pool_.clear();
    totalMemoryInUse_ = 0;
    activeCount_ = 0;
}

size_t XdnaBufferManager::totalMemoryInUse() const
{
    return totalMemoryInUse_.load();
}

size_t XdnaBufferManager::activeBufferCount() const
{
    return activeCount_.load();
}

size_t XdnaBufferManager::pooledBufferCount() const
{
    std::lock_guard<std::mutex> lock(poolMutex_);
    size_t count = 0;
    for (const auto &[_, entries] : pool_) {
        count += entries.size();
    }
    return count;
}

void XdnaBufferManager::setMaxPoolSize(size_t max_bytes)
{
    std::lock_guard<std::mutex> lock(poolMutex_);
    maxPoolSize_ = max_bytes;

    // If new limit is lower than current usage, drain pool
    while (totalMemoryInUse_ > maxPoolSize_) {
        // Find largest pool entry and remove it
        size_t largestSize = 0;
        for (const auto &[size, _] : pool_) {
            largestSize = std::max(largestSize, size);
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

//==============================================================================
// XdnaRuntime Implementation
//==============================================================================

XdnaRuntime::XdnaRuntime(int deviceId)
    : deviceId_(deviceId), device_(nullptr), bufferManager_(std::make_shared<XdnaBufferManager>()), initialized_(false)
{

    initializeDevice();
}

XdnaRuntime::~XdnaRuntime()
{
    unload();
}

void XdnaRuntime::initializeDevice()
{
    // In production: Initialize xDNA device
    // xdna_device_t* device;
    // xdna_result_t result = xdnaDeviceOpen(&device, deviceId_);
    // if (result != XDNA_SUCCESS) {
    //     throw DeviceNotAvailableError(deviceId_);
    // }
    // device_ = device;

    // Stub: Mark as initialized for testing
    initialized_ = true;
}

bool XdnaRuntime::loadXclbin(const std::string &path)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (path.empty()) {
        throw XclbinError("Empty path");
    }

    // In production: Load xclbin via xDNA
    // auto loadedXclbin = loadXclbinInternal(nullptr, 0, path);

    // Stub: Create fake loaded xclbin
    LoadedXclbin loaded;
    loaded.path = path;
    loaded.kernelNames = {"kernel_stub"}; // Placeholder
    loaded.context = nullptr;

    loadedXclbins_.push_back(std::move(loaded));
    return true;
}

bool XdnaRuntime::loadXclbinFromMemory(const void *data, size_t size)
{
    std::lock_guard<std::mutex> lock(mutex_);

    if (!data || size == 0) {
        throw XclbinError("Invalid data or size");
    }

    // In production: Load xclbin from memory
    // auto loadedXclbin = loadXclbinInternal(data, size, "<memory>");

    // Stub
    LoadedXclbin loaded;
    loaded.path = "<memory>";
    loaded.kernelNames = {"kernel_stub"};
    loaded.context = nullptr;

    loadedXclbins_.push_back(std::move(loaded));
    return true;
}

bool XdnaRuntime::unloadXclbin(const std::string &path)
{
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(loadedXclbins_.begin(), loadedXclbins_.end(), [&path](const LoadedXclbin &xclbin) {
        return xclbin.path == path;
    });

    if (it == loadedXclbins_.end()) {
        return false;
    }

    // In production: Unload xclbin via xDNA
    // xdnaReleaseContext(it->context);

    loadedXclbins_.erase(it);
    return true;
}

std::vector<std::string> XdnaRuntime::getKernelNames() const
{
    std::lock_guard<std::mutex> lock(mutex_);

    std::vector<std::string> names;
    for (const auto &xclbin : loadedXclbins_) {
        names.insert(names.end(), xclbin.kernelNames.begin(), xclbin.kernelNames.end());
    }
    return names;
}

std::vector<std::string> XdnaRuntime::getKernelsFromXclbin(const std::string &xclbinPath) const
{
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = std::find_if(loadedXclbins_.begin(), loadedXclbins_.end(), [&xclbinPath](const LoadedXclbin &xclbin) {
        return xclbin.path == xclbinPath;
    });

    if (it == loadedXclbins_.end()) {
        return {};
    }

    return it->kernelNames;
}

bool XdnaRuntime::hasKernel(const std::string &kernelName) const
{
    std::lock_guard<std::mutex> lock(mutex_);

    for (const auto &xclbin : loadedXclbins_) {
        if (std::find(xclbin.kernelNames.begin(), xclbin.kernelNames.end(), kernelName) != xclbin.kernelNames.end()) {
            return true;
        }
    }
    return false;
}

ExecutionResult XdnaRuntime::execute(const std::string &kernelName,
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

std::shared_ptr<IKernelHandle> XdnaRuntime::getKernel(const std::string &kernelName)
{
    std::lock_guard<std::mutex> lock(mutex_);

    // In production: Get kernel from loaded xclbins
    // auto* handle = getKernelHandleInternal(kernelName);
    // return std::make_shared<XdnaKernelHandle>(handle, kernelName, numArgs);

    // Stub
    auto handle = std::make_shared<XdnaKernelHandle>(reinterpret_cast<xdna_detail::KernelHandle>(0x1),
                                                     kernelName,
                                                     6 // Default arg count
    );
    return handle;
}

std::shared_ptr<IBuffer> XdnaRuntime::allocateBuffer(size_t size, bool /*hostAccessible*/)
{
    return bufferManager_->allocate(size);
}

std::shared_ptr<IBuffer> XdnaRuntime::allocateBufferFromData(const void *data, size_t size)
{
    auto buffer = allocateBuffer(size, true);
    buffer->write(data, size);
    return buffer;
}

std::shared_ptr<IBufferManager> XdnaRuntime::getBufferManager()
{
    return bufferManager_;
}

void XdnaRuntime::unload()
{
    std::lock_guard<std::mutex> lock(mutex_);

    for (auto &xclbin : loadedXclbins_) {
        // In production: xdnaReleaseContext(xclbin.context);
    }
    loadedXclbins_.clear();

    if (bufferManager_) {
        bufferManager_->clear();
    }
}

bool XdnaRuntime::isLoaded() const
{
    std::lock_guard<std::mutex> lock(mutex_);
    return !loadedXclbins_.empty();
}

std::string XdnaRuntime::getPlatformName() const
{
    return "xDNA";
}

std::string XdnaRuntime::getVersion() const
{
    return "1.0.0";
}

std::string XdnaRuntime::getPlatformVersion() const
{
    return getDriverVersion();
}

std::string XdnaRuntime::getDeviceInfo() const
{
    // In production: Query device info from xDNA
    return R"({"device_id":)" + std::to_string(deviceId_) + R"(, "platform": "xDNA"})";
}

} // namespace runtime
} // namespace iron

#endif // _WIN32 || _WIN64
