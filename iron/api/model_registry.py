# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Model Registry for IRON API

Manages converted models and their lifecycle, tracking conversion status,
cache locations, and usage statistics.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)


@dataclass
class ModelEntry:
    """Represents a converted model in the registry"""

    model_id: str  # User-facing ID (e.g., "meta-llama/Llama-3.2-1B")
    iron_name: str  # Internal IRON name
    status: str  # "pending", "converting", "ready", "error"
    architecture: str
    hidden_size: int
    num_layers: int
    vocab_size: int
    converted_at: Optional[datetime] = None
    error_message: Optional[str] = None
    last_used: Optional[datetime] = None
    use_count: int = 0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "model_id": self.model_id,
            "iron_name": self.iron_name,
            "status": self.status,
            "architecture": self.architecture,
            "hidden_size": self.hidden_size,
            "num_layers": self.num_layers,
            "vocab_size": self.vocab_size,
            "converted_at": (
                self.converted_at.isoformat() if self.converted_at else None
            ),
            "error_message": self.error_message,
            "last_used": self.last_used.isoformat() if self.last_used else None,
            "use_count": self.use_count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ModelEntry":
        """Create from dictionary"""
        entry = cls(
            model_id=data["model_id"],
            iron_name=data["iron_name"],
            status=data["status"],
            architecture=data["architecture"],
            hidden_size=data["hidden_size"],
            num_layers=data["num_layers"],
            vocab_size=data["vocab_size"],
            error_message=data.get("error_message"),
            use_count=data.get("use_count", 0),
        )
        if data.get("converted_at"):
            entry.converted_at = datetime.fromisoformat(data["converted_at"])
        if data.get("last_used"):
            entry.last_used = datetime.fromisoformat(data["last_used"])
        return entry


class ModelRegistry:
    """
    Manages converted models and their lifecycle.

    The registry tracks:
    - Model conversion status (pending, converting, ready, error)
    - Cache locations for converted models
    - Usage statistics for cache management
    - Model metadata (architecture, sizes, etc.)
    """

    def __init__(self, cache_dir: str = "~/.cache/iron/models"):
        """
        Initialize the model registry.

        Args:
            cache_dir: Base directory for model cache
        """
        self.cache_dir = Path(cache_dir).expanduser()
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.models: Dict[str, ModelEntry] = {}
        self.registry_file = self.cache_dir / "registry.json"

        # Load existing registry
        self._load_registry()

        logger.info(f"Model registry initialized at {self.cache_dir}")
        logger.info(f"Found {len(self.models)} registered models")

    def _model_id_to_safe_name(self, model_id: str) -> str:
        """Convert model ID to safe directory name"""
        # Replace "/" with "__" for directory naming
        # e.g., "meta-llama/Llama-3.2-1B" -> "meta-llama__Llama-3.2-1B"
        return model_id.replace("/", "__")

    def get_model_path(self, model_id: str) -> Path:
        """
        Get path to converted model cache.

        Args:
            model_id: Model identifier (e.g., "meta-llama/Llama-3.2-1B")

        Returns:
            Path to model cache directory
        """
        safe_name = self._model_id_to_safe_name(model_id)
        return self.cache_dir / safe_name

    def get(self, model_id: str) -> ModelEntry:
        """
        Get model entry from registry.

        Args:
            model_id: Model identifier

        Returns:
            ModelEntry for the model

        Raises:
            KeyError: If model not found
        """
        if model_id not in self.models:
            raise KeyError(f"Model {model_id} not found in registry")
        return self.models[model_id]

    def register_model(
        self,
        model_id: str,
        architecture: str = "unknown",
        hidden_size: int = 0,
        num_layers: int = 0,
        vocab_size: int = 0,
    ) -> ModelEntry:
        """
        Register a new model for conversion.

        Args:
            model_id: Model identifier
            architecture: Model architecture name
            hidden_size: Hidden dimension size
            num_layers: Number of transformer layers
            vocab_size: Vocabulary size

        Returns:
            ModelEntry for the registered model
        """
        entry = ModelEntry(
            model_id=model_id,
            iron_name=model_id,
            status="pending",
            architecture=architecture,
            hidden_size=hidden_size,
            num_layers=num_layers,
            vocab_size=vocab_size,
        )
        self.models[model_id] = entry
        self._save_registry()
        logger.info(f"Registered model: {model_id}")
        return entry

    def update(self, entry: ModelEntry):
        """
        Update model entry in registry.

        Args:
            entry: Updated ModelEntry
        """
        self.models[entry.model_id] = entry
        self._save_registry()

    def update_status(self, model_id: str, status: str, error: Optional[str] = None):
        """
        Update model conversion status.

        Args:
            model_id: Model identifier
            status: New status ("pending", "converting", "ready", "error")
            error: Optional error message if status is "error"
        """
        if model_id in self.models:
            entry = self.models[model_id]
            entry.status = status
            if status == "ready":
                entry.converted_at = datetime.now()
            if error:
                entry.error_message = error
            self.update(entry)
            logger.info(f"Updated model {model_id} status to {status}")

    def update_usage(self, model_id: str):
        """
        Update model usage statistics.

        Args:
            model_id: Model identifier
        """
        if model_id in self.models:
            entry = self.models[model_id]
            entry.last_used = datetime.now()
            entry.use_count += 1
            self.update(entry)

    def list_models(self, status_filter: Optional[str] = None) -> List[ModelEntry]:
        """
        List registered models.

        Args:
            status_filter: Optional status to filter by

        Returns:
            List of ModelEntry objects
        """
        models = list(self.models.values())
        if status_filter:
            models = [m for m in models if m.status == status_filter]
        return models

    def remove(self, model_id: str):
        """
        Remove model from registry.

        Args:
            model_id: Model identifier
        """
        if model_id in self.models:
            del self.models[model_id]
            self._save_registry()
            logger.info(f"Removed model: {model_id}")

    def _load_registry(self):
        """Load registry from disk"""
        if self.registry_file.exists():
            try:
                with open(self.registry_file, "r") as f:
                    data = json.load(f)
                    self.models = {k: ModelEntry.from_dict(v) for k, v in data.items()}
                logger.info(f"Loaded registry with {len(self.models)} models")
            except Exception as e:
                logger.warning(f"Could not load registry: {e}")
                self.models = {}
        else:
            self.models = {}

    def _save_registry(self):
        """Save registry to disk"""
        try:
            with open(self.registry_file, "w") as f:
                data = {k: v.to_dict() for k, v in self.models.items()}
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Could not save registry: {e}")
