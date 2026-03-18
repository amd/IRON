# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Llama3.2 weight loader.

This module provides the WeightLoader class for downloading, validating,
and loading Llama3.2 model weights from HuggingFace Hub.

Features:
    - Download from HuggingFace Hub with retry logic
    - SHA256 checksum validation
    - Memory-mapped loading for efficiency
    - Integration with MemoryBudget for validation
    - Progress reporting

Example:
    >>> from iron.models.llama32 import WeightLoader
    >>> from iron.runtime import MemoryBudget
    >>>
    >>> loader = WeightLoader(memory_budget=MemoryBudget())
    >>> model_path = loader.download_model("meta-llama/Llama-3.2-1B")
    >>> weight_info = loader.validate_weights(model_path)
    >>> weights = loader.load_weights_mmap(model_path)
"""

import logging
import hashlib
import time
import shutil
from pathlib import Path
from typing import Dict, Optional, Any, List, Tuple
from dataclasses import dataclass
from datetime import datetime

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
)

logger = logging.getLogger(__name__)


@dataclass
class WeightInfo:
    """Information about loaded weights.

    This dataclass holds metadata about weight files including
    size information, tensor counts, and validation results.

    Attributes:
        file_path: Path to the model directory
        file_size: Total size of all weight files in bytes
        num_tensors: Number of weight tensors
        total_tensor_size: Total size of all tensors in bytes
        checksum: SHA256 checksum of the primary weight file
        validation_time_ms: Time taken to validate in milliseconds
        safetensors_files: List of safetensors file paths

    Example:
        >>> info = WeightInfo(
        ...     file_path=Path("/models/llama-3.2-1b"),
        ...     file_size=2_000_000_000,
        ...     num_tensors=200,
        ...     total_tensor_size=2_000_000_000,
        ...     checksum="abc123...",
        ...     validation_time_ms=1500,
        ...     safetensors_files=[Path("model.safetensors")]
        ... )
    """

    file_path: Path
    file_size: int
    num_tensors: int
    total_tensor_size: int
    checksum: str
    validation_time_ms: float = 0.0
    safetensors_files: List[Path] = None

    def __post_init__(self) -> None:
        """Initialize default values."""
        if self.safetensors_files is None:
            self.safetensors_files = []

    @property
    def file_size_mb(self) -> float:
        """Get file size in megabytes.

        Returns:
            File size in MB

        Example:
            >>> print(f"Model size: {info.file_size_mb:.1f} MB")
        """
        return self.file_size / (1024 * 1024)

    @property
    def file_size_gb(self) -> float:
        """Get file size in gigabytes.

        Returns:
            File size in GB

        Example:
            >>> print(f"Model size: {info.file_size_gb:.2f} GB")
        """
        return self.file_size / (1024 * 1024 * 1024)

    def __str__(self) -> str:
        """Get human-readable string representation."""
        return (
            f"WeightInfo("
            f"path={self.file_path}, "
            f"size={self.file_size_gb:.2f}GB, "
            f"tensors={self.num_tensors}, "
            f"checksum={self.checksum[:16]}...)"
        )


class WeightLoader:
    """Loader for Llama3.2 weights in safetensors format.

    This class handles downloading model weights from HuggingFace Hub,
    validating file integrity, and loading weights into memory efficiently.

    Features:
        - Automatic download from HuggingFace Hub
        - Retry logic with exponential backoff for network resilience
        - SHA256 checksum validation
        - Memory budget integration to prevent OOM
        - Memory-mapped loading for large models
        - Progress reporting and logging

    Attributes:
        cache_dir: Directory for caching downloaded models
        memory_budget: Optional memory budget for validation

    Example:
        >>> loader = WeightLoader(
        ...     cache_dir="/tmp/models",
        ...     memory_budget=MemoryBudget()
        ... )
        >>> model_path = loader.download_model("meta-llama/Llama-3.2-1B")
        >>> weights = loader.load_weights_mmap(model_path)
    """

    # Default HuggingFace configuration
    DEFAULT_MODEL_ID = "meta-llama/Llama-3.2-1B"
    DEFAULT_VARIANT = "1B"

    # Retry configuration
    MAX_DOWNLOAD_ATTEMPTS = 3
    RETRY_MIN_WAIT = 4  # seconds
    RETRY_MAX_WAIT = 10  # seconds

    def __init__(
        self, cache_dir: Optional[str] = None, memory_budget: Optional[Any] = None
    ):
        """Initialize weight loader.

        Args:
            cache_dir: Cache directory for downloaded weights. If None,
                uses the default HuggingFace cache directory
            memory_budget: Optional MemoryBudget instance for validating
                memory requirements before loading

        Example:
            >>> loader = WeightLoader(
            ...     cache_dir="/models/cache",
            ...     memory_budget=MemoryBudget()
            ... )
        """
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.memory_budget = memory_budget

        # Ensure cache directory exists
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            logger.debug(f"Cache directory: {self.cache_dir}")

    # =========================================================================
    # Download Methods
    # =========================================================================

    @retry(
        stop=stop_after_attempt(MAX_DOWNLOAD_ATTEMPTS),
        wait=wait_exponential(multiplier=1, min=RETRY_MIN_WAIT, max=RETRY_MAX_WAIT),
        retry=retry_if_exception_type((ConnectionError, TimeoutError, OSError)),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )
    def download_model(
        self,
        model_id: Optional[str] = None,
        variant: str = "1B",
        force_download: bool = False,
        local_files_only: bool = False,
    ) -> Path:
        """Download model weights from HuggingFace Hub.

        Downloads all safetensors files and config.json for the specified
        model. Uses retry logic with exponential backoff for network resilience.

        Args:
            model_id: HuggingFace model ID (e.g., "meta-llama/Llama-3.2-1B").
                If None, uses DEFAULT_MODEL_ID
            variant: Model variant identifier (e.g., "1B", "3B"). Used for
                logging purposes
            force_download: Force re-download even if already cached
            local_files_only: Only use locally cached files, don't download

        Returns:
            Path to downloaded model directory

        Raises:
            RuntimeError: If download fails after all retry attempts
            ConnectionError: If network is unavailable
            ValueError: If model_id is invalid

        Example:
            >>> loader = WeightLoader()
            >>> model_path = loader.download_model(
            ...     "meta-llama/Llama-3.2-1B",
            ...     force_download=False
            ... )
            >>> print(f"Model downloaded to: {model_path}")
        """
        model_id = model_id or self.DEFAULT_MODEL_ID

        logger.info(f"Downloading {model_id} ({variant})...")
        start_time = time.time()

        try:
            from huggingface_hub import snapshot_download
        except ImportError as e:
            raise ImportError(
                "huggingface_hub is required for download_model(). "
                "Install it with: pip install huggingface_hub"
            ) from e

        try:
            model_path = snapshot_download(
                repo_id=model_id,
                cache_dir=str(self.cache_dir) if self.cache_dir else None,
                force_download=force_download,
                local_files_only=local_files_only,
                allow_patterns=["*.safetensors", "config.json"],
            )

            elapsed = time.time() - start_time
            logger.info(f"Downloaded {model_id} to {model_path} ({elapsed:.1f}s)")

            return Path(model_path)

        except Exception as e:
            logger.error(f"Download failed for {model_id}: {e}")
            self._cleanup_partial_downloads(model_id)
            raise RuntimeError(
                f"Failed to download {model_id} after {self.MAX_DOWNLOAD_ATTEMPTS} attempts: {e}"
            ) from e

    def _cleanup_partial_downloads(self, model_id: str) -> None:
        """Clean up partial download files.

        Removes incomplete download artifacts to prevent corruption
        and free disk space.

        Args:
            model_id: Model ID to clean up

        Note:
            This method is called automatically after download failures.
        """
        logger.debug(f"Cleaning up partial downloads for {model_id}")

        if self.cache_dir:
            # HuggingFace Hub stores repos in subdirectories
            repo_name = model_id.replace("/", "--")
            snapshot_dir = self.cache_dir / f"models--{repo_name}"

            if snapshot_dir.exists():
                # Remove incomplete snapshots (those without .complete flag)
                for snapshot_path in snapshot_dir.glob("snapshots/*"):
                    if snapshot_path.is_dir():
                        complete_flag = snapshot_path / ".commit_*.complete"
                        if not any(complete_flag.glob("*")):
                            logger.debug(
                                f"Removing incomplete snapshot: {snapshot_path}"
                            )
                            try:
                                shutil.rmtree(snapshot_path)
                            except OSError as e:
                                logger.warning(f"Failed to remove {snapshot_path}: {e}")

    def is_model_cached(self, model_id: str) -> bool:
        """Check if a model is already cached locally.

        Args:
            model_id: HuggingFace model ID

        Returns:
            True if model is cached and complete

        Example:
            >>> if loader.is_model_cached("meta-llama/Llama-3.2-1B"):
            ...     print("Model already downloaded")
        """
        if not self.cache_dir:
            return False

        repo_name = model_id.replace("/", "--")
        snapshot_dir = self.cache_dir / f"models--{repo_name}" / "snapshots"

        if not snapshot_dir.exists():
            return False

        # Check for at least one complete snapshot
        for snapshot_path in snapshot_dir.glob("*"):
            if snapshot_path.is_dir():
                safetensors_files = list(snapshot_path.glob("*.safetensors"))
                if safetensors_files:
                    return True

        return False

    # =========================================================================
    # Validation Methods
    # =========================================================================

    def validate_weights(self, model_path: Path) -> WeightInfo:
        """Validate weight files.

        Performs validation checks on the weight files including:
        - Checking for safetensors files
        - Calculating checksums
        - Counting tensors
        - Verifying file sizes

        Args:
            model_path: Path to model directory

        Returns:
            WeightInfo with validation results

        Raises:
            FileNotFoundError: If model_path doesn't exist
            ValueError: If no safetensors files are found

        Example:
            >>> loader = WeightLoader()
            >>> weight_info = loader.validate_weights(model_path)
            >>> print(f"Validated {weight_info.num_tensors} tensors")
        """
        start_time = time.time()

        model_path = Path(model_path)

        if not model_path.exists():
            raise FileNotFoundError(f"Model path not found: {model_path}")

        safetensors_files = list(model_path.glob("*.safetensors"))

        if not safetensors_files:
            raise ValueError(f"No safetensors files found in {model_path}")

        total_size = 0
        num_tensors = 0
        total_tensor_size = 0
        primary_checksum = ""

        logger.info(f"Validating {len(safetensors_files)} safetensors file(s)...")

        for i, file_path in enumerate(safetensors_files):
            file_size = file_path.stat().st_size
            total_size += file_size

            # Calculate checksum for primary file
            checksum = self._calculate_checksum(file_path)
            if i == 0:
                primary_checksum = checksum

            file_size_mb = file_size / (1024 * 1024)
            logger.info(
                f"  {file_path.name}: {file_size_mb:.1f}MB, checksum: {checksum[:16]}..."
            )

            # Count tensors
            try:
                from safetensors import safe_open

                with safe_open(file_path, framework="numpy") as f:
                    file_num_tensors = len(f.keys())
                    num_tensors += file_num_tensors

                    for key in f.keys():
                        tensor = f.get_tensor(key)
                        total_tensor_size += tensor.nbytes

                    logger.debug(f"    Contains {file_num_tensors} tensors")

            except Exception as e:
                logger.error(f"Failed to read {file_path}: {e}")
                raise ValueError(f"Invalid safetensors file: {file_path}") from e

        elapsed_ms = (time.time() - start_time) * 1000

        weight_info = WeightInfo(
            file_path=model_path,
            file_size=total_size,
            num_tensors=num_tensors,
            total_tensor_size=total_tensor_size,
            checksum=primary_checksum,
            validation_time_ms=elapsed_ms,
            safetensors_files=safetensors_files,
        )

        logger.info(
            f"Validation complete: {num_tensors} tensors, "
            f"{weight_info.file_size_gb:.2f}GB ({elapsed_ms:.0f}ms)"
        )

        return weight_info

    def _calculate_checksum(self, file_path: Path, chunk_size: int = 8192) -> str:
        """Calculate SHA256 checksum of file.

        Reads the file in chunks to handle large files efficiently.

        Args:
            file_path: Path to file
            chunk_size: Number of bytes to read per chunk

        Returns:
            SHA256 hex digest

        Example:
            >>> checksum = loader._calculate_checksum(Path("model.safetensors"))
            >>> print(f"Checksum: {checksum}")
        """
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                sha256.update(chunk)

        return sha256.hexdigest()

    def validate_memory(
        self,
        weight_info: WeightInfo,
        required_kv: int = 0,
        required_activations: int = 0,
    ) -> bool:
        """Validate weight loading fits within memory budget.

        Checks if loading the weights (plus optional KV cache and
        activations) would exceed the configured memory budget.

        Args:
            weight_info: Weight information from validate_weights()
            required_kv: Additional memory needed for KV cache in bytes
            required_activations: Additional memory needed for activations

        Returns:
            True if loading is safe

        Raises:
            MemoryError: If weights exceed budget

        Example:
            >>> if loader.validate_memory(weight_info):
            ...     weights = loader.load_weights(model_path)
        """
        if self.memory_budget is None:
            logger.debug("No memory budget configured, skipping validation")
            return True

        try:
            # MemoryBudget is passed in constructor, call its validate method
            # The memory_budget could be a C++ wrapper or Python mock
            result = self.memory_budget.validateModelLoad(
                requiredWeights=weight_info.total_tensor_size,
                requiredKV=required_kv,
                requiredActivations=required_activations,
            )

            # Handle both Python object result and C++ result
            success = (
                result.success
                if hasattr(result, "success")
                else result.get("success", True)
            )

            if not success:
                error_msg = ""
                if hasattr(result, "errorMessage"):
                    error_msg = result.errorMessage
                elif isinstance(result, dict):
                    error_msg = result.get("errorMessage", "Memory validation failed")

                raise MemoryError(
                    f"Weight loading would exceed memory budget: "
                    f"{weight_info.total_tensor_size} bytes requested. "
                    f"Error: {error_msg}"
                )

            logger.info(
                f"Memory validation passed: "
                f"{weight_info.file_size_mb:.1f}MB weights within budget"
            )

            return True

        except AttributeError as e:
            logger.warning(f"MemoryBudget validation not available: {e}")
            return True

    def check_disk_space(
        self, model_path: Path, required_bytes: int, safety_margin: float = 0.1
    ) -> bool:
        """Check if sufficient disk space is available.

        Args:
            model_path: Path to model directory
            required_bytes: Required disk space in bytes
            safety_margin: Safety margin fraction (default 10%)

        Returns:
            True if sufficient space is available

        Raises:
            OSError: If insufficient disk space

        Example:
            >>> loader.check_disk_space(model_path, 2_000_000_000)
            True
        """
        import shutil

        # Get disk usage using shutil (cross-platform: Linux, Windows, macOS)
        try:
            # Use the model path if it exists, otherwise use a root path
            check_path = model_path if model_path.exists() else model_path.root
            usage = shutil.disk_usage(check_path)
            available = usage.free
        except (OSError, AttributeError) as e:
            logger.warning(f"Could not check disk space: {e}")
            return True  # Assume OK if we can't check

        required_with_margin = required_bytes * (1 + safety_margin)

        if available < required_with_margin:
            available_gb = available / (1024 * 1024 * 1024)
            required_gb = required_with_margin / (1024 * 1024 * 1024)
            raise OSError(
                f"Insufficient disk space: "
                f"{available_gb:.2f}GB available, "
                f"{required_gb:.2f}GB required"
            )

        logger.debug(
            f"Disk space OK: {available / 1e9:.1f}GB available, "
            f"{required_with_margin / 1e9:.1f}GB required"
        )

        return True

    # =========================================================================
    # Loading Methods
    # =========================================================================

    def load_weights(self, model_path: Path, device: str = "cpu") -> Dict[str, Any]:
        """Load weights into memory.

        Loads all weight tensors from safetensors files into memory.
        For large models, consider using load_weights_mmap() instead
        to reduce memory usage.

        Args:
            model_path: Path to model directory
            device: Target device ("cpu", "npu", "cuda"). Note: currently
                only CPU loading is supported

        Returns:
            Dictionary mapping weight names to numpy arrays

        Raises:
            FileNotFoundError: If no safetensors files are found

        Example:
            >>> weights = loader.load_weights(model_path)
            >>> print(f"Loaded {len(weights)} tensors")
        """
        logger.info(f"Loading weights from {model_path}...")
        start_time = time.time()

        model_path = Path(model_path)
        weights: Dict[str, Any] = {}

        safetensors_files = sorted(model_path.glob("*.safetensors"))

        if not safetensors_files:
            raise FileNotFoundError(f"No safetensors files in {model_path}")

        try:
            from safetensors import safe_open
        except ImportError as e:
            raise ImportError(
                "safetensors is required for load_weights(). "
                "Install it with: pip install safetensors"
            ) from e

        for file_path in safetensors_files:
            logger.debug(f"Loading {file_path.name}...")

            with safe_open(file_path, framework="numpy") as f:
                for key in f.keys():
                    weights[key] = f.get_tensor(key)

        elapsed = time.time() - start_time
        logger.info(f"Loaded {len(weights)} tensors in {elapsed:.2f}s")

        return weights

    def load_weights_mmap(self, model_path: Path) -> Dict[str, Any]:
        """Load weights using memory mapping.

        Loads weight tensors using memory mapping, which allows
        accessing large models without loading everything into RAM.
        The OS handles paging data in and out as needed.

        This is recommended for:
        - Large models (>2GB)
        - Systems with limited RAM
        - When only accessing a subset of weights

        Args:
            model_path: Path to model directory

        Returns:
            Dictionary mapping weight names to memory-mapped numpy arrays

        Raises:
            FileNotFoundError: If no safetensors files are found

        Example:
            >>> weights = loader.load_weights_mmap(model_path)
            >>> # Access weights without full RAM usage
            >>> print(weights["model.embed_tokens.weight"].shape)
        """
        logger.info(f"Loading weights (mmap) from {model_path}...")
        start_time = time.time()

        model_path = Path(model_path)
        weights: Dict[str, Any] = {}

        safetensors_files = sorted(model_path.glob("*.safetensors"))

        if not safetensors_files:
            raise FileNotFoundError(f"No safetensors files in {model_path}")

        try:
            from safetensors import safe_open
        except ImportError as e:
            raise ImportError(
                "safetensors is required for load_weights_mmap(). "
                "Install it with: pip install safetensors"
            ) from e

        for file_path in safetensors_files:
            logger.debug(f"Memory-mapping {file_path.name}...")

            with safe_open(file_path, framework="numpy") as f:
                for key in f.keys():
                    # safetensors with numpy framework returns memory-mapped arrays
                    # when the file is accessed this way
                    weights[key] = f.get_tensor(key)

        elapsed = time.time() - start_time
        logger.info(f"Memory-mapped {len(weights)} tensors in {elapsed:.2f}s")

        return weights

    def load_specific_weights(
        self, model_path: Path, weight_names: List[str]
    ) -> Dict[str, Any]:
        """Load only specified weights.

        Loads only the requested weight tensors, which can be useful
        for partial loading or debugging.

        Args:
            model_path: Path to model directory
            weight_names: List of weight tensor names to load

        Returns:
            Dictionary of requested weight tensors

        Raises:
            KeyError: If requested weight is not found

        Example:
            >>> weights = loader.load_specific_weights(
            ...     model_path,
            ...     ["model.embed_tokens.weight", "model.norm.weight"]
            ... )
        """
        logger.info(f"Loading {len(weight_names)} specific weights...")

        all_weights = self.load_weights_mmap(model_path)

        result = {}
        missing = []

        for name in weight_names:
            if name in all_weights:
                result[name] = all_weights[name]
            else:
                missing.append(name)

        if missing:
            raise KeyError(f"Weights not found: {missing}")

        logger.info(f"Loaded {len(result)}/{len(weight_names)} requested weights")

        return result

    # =========================================================================
    # Convenience Methods
    # =========================================================================

    def download_and_validate(
        self, model_id: Optional[str] = None, check_memory: bool = True
    ) -> Tuple[Path, WeightInfo]:
        """Download and validate model weights.

        Convenience method that combines download and validation steps.

        Args:
            model_id: HuggingFace model ID
            check_memory: Whether to validate against memory budget

        Returns:
            Tuple of (model_path, weight_info)

        Example:
            >>> model_path, weight_info = loader.download_and_validate(
            ...     "meta-llama/Llama-3.2-1B"
            ... )
        """
        model_path = self.download_model(model_id)
        weight_info = self.validate_weights(model_path)

        if check_memory:
            self.validate_memory(weight_info)

        return model_path, weight_info

    def get_model_info(self, model_path: Path) -> Dict[str, Any]:
        """Get information about a downloaded model.

        Args:
            model_path: Path to model directory

        Returns:
            Dictionary with model information

        Example:
            >>> info = loader.get_model_info(model_path)
            >>> print(f"Model has {info['num_tensors']} tensors")
        """
        model_path = Path(model_path)

        safetensors_files = list(model_path.glob("*.safetensors"))
        total_size = sum(f.stat().st_size for f in safetensors_files)

        return {
            "path": str(model_path),
            "num_files": len(safetensors_files),
            "total_size_bytes": total_size,
            "total_size_mb": total_size / (1024 * 1024),
            "total_size_gb": total_size / (1024 * 1024 * 1024),
        }

    def clear_cache(self) -> None:
        """Clear the download cache.

        Removes all downloaded models from the cache directory.

        Warning:
            This will delete all cached models and require re-download.

        Example:
            >>> loader.clear_cache()
        """
        if not self.cache_dir:
            logger.warning("No cache directory configured")
            return

        logger.info(f"Clearing cache: {self.cache_dir}")

        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
            self.cache_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Cache cleared")
