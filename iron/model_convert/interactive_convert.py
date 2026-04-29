# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Interactive Model Converter for IRON NPU Framework

A production-grade, interactive command-line tool for converting HuggingFace
model checkpoints to IRON NPU-compatible format. Supports local paths and
HuggingFace Hub models with full safetensors weight loading, mapping, and
export as individual .npy files.

Usage:
    python -m iron.model_convert.interactive_convert <model_path_or_name>
    python -m iron.model_convert.interactive_convert meta-llama/Llama-2-7b-hf -o ./output
    python -m iron.model_convert.interactive_convert ./local_model_dir --batch --force

Phases:
    1. Input Resolution    - Locate or download model, validate files
    2. Architecture Parse  - Load and normalize config via ConfigAdapter
    3. Compatibility Check - Run GapAnalyzer if available
    4. NPU Configuration   - Interactive prompts for AIE columns, tiles, etc.
    5. Weight Loading      - ACTUALLY load safetensors/pytorch weights
    6. Weight Mapping      - Map HF names to IRON names with transforms
    7. Shape Analysis      - Compute padded shapes via ShapeManager
    8. Model Assembly      - Count operators, compute memory requirements
    9. Export              - Save .npy files, config.json, manifests

Author: Jordan Blake, Principal Software Engineer & Technical Lead
"""

import sys
import re
import json
import math
import time
import shutil
import logging
import argparse
import traceback
from pathlib import Path
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# Rich UI (optional -- falls back to plain text if unavailable)
# ---------------------------------------------------------------------------
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.tree import Tree
    from rich.progress import (
        Progress,
        BarColumn,
        TextColumn,
        TimeRemainingColumn,
        SpinnerColumn,
    )

    HAS_RICH = True
except ImportError:
    HAS_RICH = False

# ---------------------------------------------------------------------------
# HuggingFace Hub download (optional)
# ---------------------------------------------------------------------------
try:
    from huggingface_hub import snapshot_download

    HAS_HF_HUB = True
except ImportError:
    HAS_HF_HUB = False
    snapshot_download = None  # type: ignore[misc,assignment]

# ---------------------------------------------------------------------------
# Safetensors (required for actual weight loading)
# ---------------------------------------------------------------------------
try:
    from safetensors import safe_open

    HAS_SAFETENSORS = True
except ImportError:
    HAS_SAFETENSORS = False
    safe_open = None  # type: ignore[misc,assignment]

# ---------------------------------------------------------------------------
# IRON internal modules (relative imports within the package)
# ---------------------------------------------------------------------------
from .config_adapter import (
    ConfigAdapter,
    NormalizedConfig,
    ModelArchitecture,
)
from .weight_mapper import (
    WeightMapper,
    create_weight_mapper,
    MappedWeight,
    WeightTransform,
)
from .shape_manager import ShapeManager, create_shape_manager

# ---------------------------------------------------------------------------
# Optional: GapAnalyzer for compatibility checking
# ---------------------------------------------------------------------------
try:
    from iron.model_analysis.architecture_scanner import (
        ArchitectureScanner,
        ArchitectureRequirements,
    )
    from iron.model_analysis.gap_analyzer import GapAnalyzer

    HAS_GAP_ANALYZER = True
except ImportError:
    HAS_GAP_ANALYZER = False
    ArchitectureScanner = None  # type: ignore[misc,assignment]
    ArchitectureRequirements = None  # type: ignore[misc,assignment]
    GapAnalyzer = None  # type: ignore[misc,assignment]

# ---------------------------------------------------------------------------
# Module logger
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Console helpers
# ---------------------------------------------------------------------------

_console: Optional["Console"] = None


def get_console() -> "Console":
    """Return the Rich console instance, or None if rich is unavailable."""
    global _console
    if _console is None and HAS_RICH:
        _console = Console(force_terminal=True)
    return _console


def print_banner(text: str) -> None:
    """Print a styled banner heading."""
    console = get_console()
    if console:
        console.print(Panel(text, style="bold cyan", border_style="cyan"))
    else:
        width = max(len(text) + 4, 60)
        print(f"\n{'=' * width}")
        print(f"  {text}")
        print(f"{'=' * width}\n")


def print_phase(phase_num: int, total: int, title: str) -> None:
    """Print a phase header."""
    label = f"Phase {phase_num}/{total}: {title}"
    console = get_console()
    if console:
        console.print(f"\n[yellow bold]>> {label}[/yellow bold]")
    else:
        print(f"\n>> {label}")


def print_ok(text: str) -> None:
    """Print a success indicator."""
    console = get_console()
    if console:
        console.print(f"  [green]OK[/green] {text}")
    else:
        print(f"  OK   {text}")


def print_warn(text: str) -> None:
    """Print a warning indicator."""
    console = get_console()
    if console:
        console.print(f"  [yellow]WARN[/yellow] {text}")
    else:
        print(f"  WARN {text}")


def print_err(text: str) -> None:
    """Print an error indicator."""
    console = get_console()
    if console:
        console.print(f"  [red]ERROR[/red] {text}")
    else:
        print(f"  ERR  {text}")


def print_info(text: str) -> None:
    """Print an info line."""
    console = get_console()
    if console:
        console.print(f"  {text}")
    else:
        print(f"  {text}")


def make_progress() -> Optional["Progress"]:
    """Return a Rich Progress instance or None."""
    if not HAS_RICH:
        return None
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        console=get_console(),
    )


def confirm(prompt_text: str, default: bool = True) -> bool:
    """Ask for yes/no confirmation. Returns True for yes."""
    default_str = "Y/n" if default else "y/N"
    try:
        answer = input(f"  {prompt_text} [{default_str}]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    if answer == "":
        return default
    return answer in ("y", "yes")


def ask_value(prompt_text: str, default: Any, cast: type = str) -> Any:
    """Ask for a value with a default. Returns cast value or default."""
    default_str = str(default)
    try:
        answer = input(f"  {prompt_text} [{default_str}]: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return default
    if answer == "":
        return default
    try:
        return cast(answer)
    except (ValueError, TypeError):
        print_err(f"Invalid value '{answer}', using default: {default}")
        return default


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class NPUConfig:
    """NPU hardware and operator configuration.

    Attributes:
        num_aie_columns: Number of AIE columns to utilize (1, 2, 4, or 8)
        tile_m: Row tile size for GEMM operations
        tile_k: Reduction-dimension tile size for GEMM
        tile_n: Column tile size for GEMM
        max_seq_len: Maximum sequence length for KV cache allocation
        batch_size: Batch dimension for shape computation
        use_aie_gemm: Enable AIE GEMM operators
        use_aie_gemv: Enable AIE GEMV operators (decode phase)
        use_aie_norm: Enable AIE RMSNorm operators
        use_aie_attention: Enable fused AIE MHA operator
        use_aie_rope: Enable AIE RoPE operator
        use_aie_ffn: Enable AIE FFN operators

    Example:
        >>> cfg = NPUConfig(num_aie_columns=4, tile_m=32)
        >>> cfg.num_aie_columns
        4
    """

    num_aie_columns: int = 8
    tile_m: int = 64
    tile_k: int = 64
    tile_n: int = 64
    max_seq_len: int = 512
    batch_size: int = 1
    use_aie_gemm: bool = True
    use_aie_gemv: bool = False
    use_aie_norm: bool = True
    use_aie_attention: bool = False
    use_aie_rope: bool = False
    use_aie_ffn: bool = True


@dataclass
class ConversionState:
    """Tracks outputs from each conversion phase.

    This state object is persisted as a JSON checkpoint after each phase
    to support resuming a partially completed conversion.

    Attributes:
        model_path: Resolved local path to the model
        model_name: Human-readable model identifier (HF name or local path)
        is_hub_model: Whether the model was downloaded from HuggingFace Hub
        normalized_config: Dict representation of the NormalizedConfig
        npu_config: Dict representation of NPUConfig
        weight_format: Detected weight format (safetensors, pytorch)
        weight_files: List of weight file paths loaded
        tensor_index: Dict of tensor_name -> file_path (for sharded models)
        tensor_count: Total number of tensors loaded
        total_weight_bytes: Total raw weight data size in bytes
        mapped_weights: Dict of iron_name -> metadata about mapped weights
        mapped_count: Number of successfully mapped weights
        unmapped_names: List of HF weight names that could not be mapped
        shapes: Dict of shape analysis results
        operator_summary: Dict of operator counts and memory info
        output_dir: Final output directory path
        started_at: ISO-8601 timestamp of conversion start
        phase_completed: Highest phase number completed
    """

    model_path: str = ""
    model_name: str = ""
    is_hub_model: bool = False
    normalized_config: Dict[str, Any] = field(default_factory=dict)
    npu_config: Dict[str, Any] = field(default_factory=dict)
    weight_format: str = ""
    weight_files: List[str] = field(default_factory=list)
    tensor_index: Dict[str, str] = field(default_factory=dict)
    tensor_count: int = 0
    total_weight_bytes: int = 0
    mapped_weights: Dict[str, Any] = field(default_factory=dict)
    mapped_count: int = 0
    unmapped_names: List[str] = field(default_factory=list)
    shapes: Dict[str, Any] = field(default_factory=dict)
    operator_summary: Dict[str, Any] = field(default_factory=dict)
    output_dir: str = ""
    started_at: str = ""
    phase_completed: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert state to a serializable dictionary."""
        return {
            "model_path": self.model_path,
            "model_name": self.model_name,
            "is_hub_model": self.is_hub_model,
            "normalized_config": self.normalized_config,
            "npu_config": self.npu_config,
            "weight_format": self.weight_format,
            "weight_files": self.weight_files,
            "tensor_index": self.tensor_index,
            "tensor_count": self.tensor_count,
            "total_weight_bytes": self.total_weight_bytes,
            "mapped_weights": self.mapped_weights,
            "mapped_count": self.mapped_count,
            "unmapped_names": self.unmapped_names,
            "shapes": self.shapes,
            "operator_summary": self.operator_summary,
            "output_dir": self.output_dir,
            "started_at": self.started_at,
            "phase_completed": self.phase_completed,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ConversionState":
        """Reconstruct state from a dictionary."""
        state = cls()
        for key, value in data.items():
            if hasattr(state, key):
                setattr(state, key, value)
        return state


# ---------------------------------------------------------------------------
# DisplayManager -- Rich UI rendering
# ---------------------------------------------------------------------------


class DisplayManager:
    """Manages Rich-based display of conversion results.

    Provides reusable rendering methods for tables, trees, and panels
    that present conversion phase output to the user.

    Usage:
        DisplayManager().show_architecture(config_dict)
        DisplayManager().show_tensor_summary(tensor_index, total_bytes)
    """

    def __init__(self) -> None:
        """Initialize the display manager."""
        self.console = get_console()

    def show_architecture(self, config: Dict[str, Any]) -> None:
        """Display normalized architecture details in a table.

        Args:
            config: Dictionary with architecture parameters.
        """
        table = Table(title="Model Architecture")
        table.add_column("Parameter", style="cyan")
        table.add_column("Value", style="green")

        key_labels = [
            ("architecture", "Architecture"),
            ("model_type", "Model Type"),
            ("hidden_size", "Hidden Size"),
            ("vocab_size", "Vocabulary Size"),
            ("num_hidden_layers", "Num Layers"),
            ("num_attention_heads", "Attention Heads"),
            ("num_kv_heads", "KV Heads"),
            ("head_dim", "Head Dim"),
            ("intermediate_size", "Intermediate Size"),
            ("norm_type", "Norm Type"),
            ("norm_eps", "Norm Epsilon"),
            ("ffn_type", "FFN Type"),
            ("rope_theta", "RoPE Theta"),
            ("max_position_embeddings", "Max Position Embeddings"),
            ("tie_word_embeddings", "Tie Word Embeddings"),
            ("is_gqa", "Is GQA"),
            ("is_mqa", "Is MQA"),
            ("is_mha", "Is MHA"),
        ]
        for key, label in key_labels:
            value = config.get(key, "N/A")
            table.add_row(label, str(value))

        if self.console:
            self.console.print(table)
        else:
            print("  Model Architecture:")
            for key, label in key_labels:
                value = config.get(key, "N/A")
                print(f"    {label}: {value}")

    def show_compatibility(self, report: Dict[str, Any]) -> None:
        """Display compatibility check results.

        Args:
            report: Dictionary from GapAnalyzer or fallback check.
        """
        table = Table(title="Compatibility Report")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        feasibility = report.get("feasibility", "unknown")
        pct = report.get("support_percentage", 0)
        table.add_row("Feasibility", feasibility)
        table.add_row("Support %", f"{pct:.1f}%")
        table.add_row(
            "Supported", str(report.get("supported_components", "N/A"))
        )
        table.add_row(
            "Unsupported", str(report.get("unsupported_components", "N/A"))
        )

        critical = report.get("critical_gaps", [])
        if critical:
            table.add_row("Critical Gaps", str(len(critical)))

        if self.console:
            self.console.print(table)
            if critical:
                print_info("Critical gaps:")
                for gap in critical[:5]:
                    name = gap.get("name", "unknown")
                    reason = gap.get("reason", "")
                    print_info(f"  - {name}: {reason}")
        else:
            print("  Compatibility Report:")
            print(f"    Feasibility: {feasibility}")
            print(f"    Support: {pct:.1f}%")
            print(f"    Critical gaps: {len(critical)}")

    def show_tensor_summary(
        self,
        tensor_index: Dict[str, str],
        total_bytes: int,
    ) -> None:
        """Display tensor inventory summary.

        Args:
            tensor_index: Mapping of tensor names to source files.
            total_bytes: Total raw weight data size.
        """
        table = Table(title="Tensor Inventory")
        table.add_column("Category", style="cyan")
        table.add_column("Count", style="green")

        categories: Dict[str, int] = {
            "Embedding": 0,
            "Attention": 0,
            "FFN": 0,
            "Norm": 0,
            "LM Head": 0,
            "Other": 0,
        }
        for name in tensor_index:
            lower = name.lower()
            if "embed" in lower:
                categories["Embedding"] += 1
            elif any(k in lower for k in ["q_proj", "k_proj", "v_proj", "o_proj", "attn"]):
                categories["Attention"] += 1
            elif any(k in lower for k in ["mlp", "gate", "up", "down", "fc"]):
                categories["FFN"] += 1
            elif any(k in lower for k in ["norm", "ln_"]):
                categories["Norm"] += 1
            elif "lm_head" in lower or "head" in lower:
                categories["LM Head"] += 1
            else:
                categories["Other"] += 1

        for cat, count in categories.items():
            if count > 0:
                table.add_row(cat, str(count))

        table.add_row("Total", str(len(tensor_index)))
        table.add_row("Total Size", _format_bytes(total_bytes))

        if self.console:
            self.console.print(table)
        else:
            print("  Tensor Inventory:")
            for cat, count in categories.items():
                if count > 0:
                    print(f"    {cat}: {count}")
            print(f"    Total: {len(tensor_index)} tensors, {_format_bytes(total_bytes)}")

    def show_mapping_summary(
        self,
        mapped_count: int,
        unmapped: List[str],
        transforms: Dict[str, int],
    ) -> None:
        """Display weight mapping results.

        Args:
            mapped_count: Number of successfully mapped weights.
            unmapped: List of unmapped HF tensor names.
            transforms: Count of each transform type applied.
        """
        table = Table(title="Weight Mapping Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_row("Mapped", str(mapped_count))
        table.add_row("Unmapped", str(len(unmapped)))

        for tname, tcount in transforms.items():
            table.add_row(f"Transform: {tname}", str(tcount))

        if self.console:
            self.console.print(table)
        else:
            print("  Weight Mapping Summary:")
            print(f"    Mapped: {mapped_count}")
            print(f"    Unmapped: {len(unmapped)}")

    def show_shapes(self, shapes: Dict[str, Any]) -> None:
        """Display computed NPU shapes.

        Args:
            shapes: Dictionary of shape analysis results.
        """
        table = Table(title="NPU Padded Shapes")
        table.add_column("Component", style="cyan")
        table.add_column("Original", style="yellow")
        table.add_column("Padded", style="green")
        table.add_column("Padding", style="red")

        for key, shape_info in shapes.items():
            if isinstance(shape_info, dict):
                orig = shape_info.get("original", "N/A")
                padded = shape_info.get("padded", "N/A")
                pad_info = shape_info.get("padding", {})
                pad_str = str(pad_info) if pad_info else "None"
                table.add_row(key, str(orig), str(padded), pad_str)

        if self.console:
            self.console.print(table)
        else:
            print("  NPU Padded Shapes:")
            for key, shape_info in shapes.items():
                if isinstance(shape_info, dict):
                    print(f"    {key}: {shape_info}")

    def show_operators(self, summary: Dict[str, Any]) -> None:
        """Display operator inventory and memory estimates.

        Args:
            summary: Dictionary with operator counts and memory info.
        """
        table = Table(title="Operator Inventory")
        table.add_column("Operator", style="cyan")
        table.add_column("Count", style="green")

        for op_type, count in summary.get("operators", {}).items():
            table.add_row(op_type, str(count))

        table.add_row("Total", str(summary.get("total_operators", 0)))

        if self.console:
            self.console.print(table)
            mem = summary.get("memory", {})
            if mem:
                mem_table = Table(title="Memory Estimates")
                mem_table.add_column("Component", style="cyan")
                mem_table.add_column("Size", style="green")
                for key, val in mem.items():
                    if isinstance(val, (int, float)):
                        mem_table.add_row(key, _format_bytes(int(val)))
                self.console.print(mem_table)
        else:
            print("  Operator Inventory:")
            for op_type, count in summary.get("operators", {}).items():
                print(f"    {op_type}: {count}")
            print(f"    Total: {summary.get('total_operators', 0)}")


def _format_bytes(num_bytes: int) -> str:
    """Format byte count into human-readable string.

    Args:
        num_bytes: Number of bytes.

    Returns:
        Formatted string (e.g., '1.5 GB').

    Example:
        >>> _format_bytes(1500000000)
        '1.40 GB'
    """
    if num_bytes < 1024:
        return f"{num_bytes} B"
    for unit in ("KB", "MB", "GB", "TB"):
        num_bytes /= 1024.0
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}"
    return f"{num_bytes:.2f} PB"


def _safe_name(name: str) -> str:
    """Convert an IRON weight name to a filesystem-safe filename.

    Replaces dots and forward slashes with underscores.

    Args:
        name: IRON internal weight name.

    Returns:
        Filesystem-safe string.

    Example:
        >>> _safe_name("layers.0.attention.wq.weight")
        'layers_0_attention_wq_weight'
    """
    return name.replace(".", "_").replace("/", "_")


# ---------------------------------------------------------------------------
# InteractiveConverter -- main orchestrator
# ---------------------------------------------------------------------------


class InteractiveConverter:
    """Orchestrates the interactive model conversion pipeline.

    Executes 9 phases in sequence, allowing the user to review and confirm
    at each step. State is checkpointed to disk after every phase so that
    a partially completed conversion can be resumed.

    Args:
        model: Model identifier -- either a HuggingFace hub name
            (e.g., ``meta-llama/Llama-2-7b-hf``) or a local directory path.
        output_dir: Directory for converted output files.
        batch: If True, run non-interactively (no prompts).
        force: If True, overwrite existing output without confirmation.
        verbose: Enable debug-level logging.

    Usage:
        converter = InteractiveConverter("meta-llama/Llama-2-7b-hf")
        converter.run()
    """

    TOTAL_PHASES = 9

    def __init__(
        self,
        model: str,
        output_dir: Optional[str] = None,
        batch: bool = False,
        force: bool = False,
        verbose: bool = False,
    ) -> None:
        """Initialize the interactive converter.

        Args:
            model: Model identifier (HF hub name or local path).
            output_dir: Optional output directory.
            batch: Run in non-interactive batch mode.
            force: Overwrite existing output without asking.
            verbose: Enable verbose logging.
        """
        self.model_name = model
        self.batch = batch
        self.force = force
        self.verbose = verbose
        self.state = ConversionState()
        self.state.model_name = model
        self.state.started_at = datetime.now(timezone.utc).isoformat()
        self.display = DisplayManager()

        # Components populated during phases
        self.norm_config: Optional[NormalizedConfig] = None
        self.npu_config: NPUConfig = NPUConfig()
        self.weight_mapper: Optional[WeightMapper] = None
        self.shape_manager: Optional[ShapeManager] = None
        self.loaded_tensors: Dict[str, np.ndarray] = {}
        self._tensor_file_map: Dict[str, str] = {}
        self.transformed_tensors: Dict[str, np.ndarray] = {}

        # Resolve output dir
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            safe = model.replace("/", "_").replace("\\", "_")
            self.output_dir = Path("output") / safe

        self.state.output_dir = str(self.output_dir)

        # Checkpoint file
        self.checkpoint_path = self.output_dir / ".conversion_checkpoint.json"

        # Attempt to resume
        if self.checkpoint_path.exists() and not force:
            self._try_resume()

        # Warnings collected during conversion
        self.warnings: List[str] = []

    # ---- Public API -------------------------------------------------------

    def run(self) -> bool:
        """Execute the full 9-phase conversion pipeline.

        Returns:
            True if all phases completed successfully.
        """
        print_banner("IRON Interactive Model Converter")
        print_info(f"Model: {self.model_name}")
        print_info(f"Output: {self.output_dir}")
        print_info(f"Mode: {'batch' if self.batch else 'interactive'}")
        print_info(f"Started: {self.state.started_at}")

        phases = [
            (1, "Input Resolution", self._phase_1_input_resolution),
            (2, "Architecture Parse", self._phase_2_architecture_parse),
            (3, "Compatibility Check", self._phase_3_compatibility_check),
            (4, "NPU Configuration", self._phase_4_npu_configuration),
            (5, "Weight Loading", self._phase_5_weight_loading),
            (6, "Weight Mapping", self._phase_6_weight_mapping),
            (7, "Shape Analysis", self._phase_7_shape_analysis),
            (8, "Model Assembly Info", self._phase_8_model_assembly),
            (9, "Export", self._phase_9_export),
        ]

        for phase_num, title, phase_fn in phases:
            if self.state.phase_completed >= phase_num and not self.batch:
                # Already completed this phase (from resume)
                print_info(f"Phase {phase_num} already completed (resumed).")
                continue

            print_phase(phase_num, self.TOTAL_PHASES, title)
            try:
                success = phase_fn()
                if not success:
                    print_err(f"Phase {phase_num} failed. Aborting.")
                    return False
                self.state.phase_completed = phase_num
                self._save_checkpoint()
            except Exception as exc:
                print_err(f"Phase {phase_num} raised an exception: {exc}")
                if self.verbose:
                    traceback.print_exc()
                return False

            if not self.batch and phase_num < self.TOTAL_PHASES:
                if not confirm("Continue to next phase?"):
                    print_info("Aborted by user.")
                    return False

        print_banner("Conversion Complete!")
        self._print_summary()
        return True

    # ---- Phase 1: Input Resolution ----------------------------------------

    def _phase_1_input_resolution(self) -> bool:
        """Resolve model location, download if needed, validate files.

        Returns:
            True if a valid model directory with config and weights was found.
        """
        model_path = Path(self.model_name)

        if model_path.exists() and model_path.is_dir():
            # Local directory
            print_info(f"Using local model directory: {model_path.resolve()}")
            self.state.model_path = str(model_path.resolve())
            self.state.is_hub_model = False
        else:
            # Try HuggingFace Hub
            if not HAS_HF_HUB:
                print_err(
                    "Model path not found locally and huggingface_hub is not installed."
                )
                print_info("Install it: pip install huggingface_hub")
                return False

            print_info(f"Model not found locally. Downloading from HuggingFace Hub...")
            print_info(f"  Model: {self.model_name}")

            # Allow user to specify a cache dir in batch mode, otherwise prompt
            cache_dir = None
            if not self.batch:
                cache_input = input(
                    "  Custom cache directory (press Enter for default): "
                ).strip()
                if cache_input:
                    cache_dir = cache_input

            try:
                downloaded = snapshot_download(
                    repo_id=self.model_name,
                    cache_dir=cache_dir,
                    ignore_patterns=["*.msgpack*", "*.onnx*", "*.gguf*"],
                )
                self.state.model_path = downloaded
                self.state.is_hub_model = True
                print_ok(f"Downloaded to: {downloaded}")
            except Exception as exc:
                print_err(f"Failed to download model: {exc}")
                return False

        model_path = Path(self.state.model_path)

        # Validate config.json
        config_path = model_path / "config.json"
        if not config_path.exists():
            print_err(f"No config.json found in {model_path}")
            return False
        print_ok(f"Found config.json")

        # Validate weight files
        weight_files = self._find_weight_files(model_path)
        if not weight_files:
            print_err("No weight files found (expected .safetensors or .bin/.pt)")
            return False
        print_ok(f"Found {len(weight_files)} weight file(s)")
        for wf in weight_files:
            print_info(f"  - {wf}")

        self.state.weight_files = [str(f) for f in weight_files]
        return True

    def _find_weight_files(self, model_path: Path) -> List[Path]:
        """Locate weight files in the model directory.

        Searches for safetensors files first, then pytorch checkpoints.

        Args:
            model_path: Path to the model directory.

        Returns:
            List of weight file paths.
        """
        files: List[Path] = []

        # Safetensors (single or sharded)
        st_file = model_path / "model.safetensors"
        if st_file.exists():
            files.append(st_file)
            return files

        st_index = model_path / "model.safetensors.index.json"
        if st_index.exists():
            # Read index to get shard files
            with open(st_index, "r") as f:
                index = json.load(f)
            seen: set = set()
            for _, filename in index.get("weight_map", {}).items():
                fp = model_path / filename
                if fp.exists() and fp not in seen:
                    files.append(fp)
                    seen.add(fp)
            return files

        # Pytorch checkpoints
        for pattern in ("pytorch_model*.bin", "*.pt"):
            found = sorted(model_path.glob(pattern))
            if found:
                files.extend(found)
                return files

        return files

    # ---- Phase 2: Architecture Parse --------------------------------------

    def _phase_2_architecture_parse(self) -> bool:
        """Load and normalize model configuration via ConfigAdapter.

        Returns:
            True if config was loaded and normalized successfully.
        """
        config_path = Path(self.state.model_path) / "config.json"

        try:
            adapter = ConfigAdapter(str(config_path))
            self.norm_config = adapter.normalize()
        except Exception as exc:
            print_err(f"Failed to parse config: {exc}")
            return False

        config_dict = self.norm_config.to_dict()
        self.state.normalized_config = config_dict
        self.display.show_architecture(config_dict)
        print_ok(f"Architecture: {self.norm_config.architecture.value}")
        print_ok(
            f"Dimensions: hidden={self.norm_config.hidden_size}, "
            f"layers={self.norm_config.num_hidden_layers}, "
            f"heads={self.norm_config.num_attention_heads}"
        )
        return True

    # ---- Phase 3: Compatibility Check -------------------------------------

    def _phase_3_compatibility_check(self) -> bool:
        """Run GapAnalyzer if available, display compatibility report.

        Returns:
            Always True (informational phase).
        """
        if not HAS_GAP_ANALYZER:
            print_warn("GapAnalyzer not available -- skipping compatibility check.")
            print_info("Install IRON model_analysis for full compatibility reporting.")
            return True

        try:
            print_info("Running architecture scanner...")
            scanner = ArchitectureScanner(self.model_name)
            requirements = scanner.scan()

            print_info("Running gap analysis...")
            analyzer = GapAnalyzer()
            report = analyzer.analyze(requirements)

            report_dict = {
                "feasibility": report.conversion_feasibility,
                "support_percentage": report.support_percentage,
                "supported_components": report.supported_components,
                "unsupported_components": report.unsupported_components,
                "critical_gaps": [
                    {
                        "name": g.component_name,
                        "reason": g.reason,
                        "impact": g.impact,
                    }
                    for g in report.critical_gaps
                ],
            }
            self.display.show_compatibility(report_dict)
            print_ok(
                f"Compatibility: {report.support_percentage:.0f}% supported "
                f"({report.conversion_feasibility})"
            )
        except Exception as exc:
            print_warn(f"Compatibility check failed (non-fatal): {exc}")
            if self.verbose:
                traceback.print_exc()

        return True

    # ---- Phase 4: NPU Configuration ---------------------------------------

    def _phase_4_npu_configuration(self) -> bool:
        """Interactively configure NPU parameters.

        Prompts the user for AIE columns, tile sizes, operator flags,
        sequence length, batch size, and output directory.

        Returns:
            True (configuration is always accepted).
        """
        print_info("Configure NPU parameters:")

        if self.batch:
            # Use defaults in batch mode
            self.npu_config = NPUConfig()
        else:
            self.npu_config.num_aie_columns = ask_value(
                "AIE columns (1,2,4,8)", 8, int
            )
            self.npu_config.tile_m = ask_value("Tile M", 64, int)
            self.npu_config.tile_k = ask_value("Tile K", 64, int)
            self.npu_config.tile_n = ask_value("Tile N", 64, int)
            self.npu_config.max_seq_len = ask_value("Max seq len", 512, int)
            self.npu_config.batch_size = ask_value("Batch size", 1, int)
            self.npu_config.use_aie_gemm = ask_value(
                "Use AIE GEMM (y/n)", "y", str
            ) in ("y", "yes")
            self.npu_config.use_aie_gemv = ask_value(
                "Use AIE GEMV (y/n)", "n", str
            ) in ("y", "yes")
            self.npu_config.use_aie_norm = ask_value(
                "Use AIE Norm (y/n)", "y", str
            ) in ("y", "yes")
            self.npu_config.use_aie_attention = ask_value(
                "Use AIE Attention (y/n)", "n", str
            ) in ("y", "yes")
            self.npu_config.use_aie_rope = ask_value(
                "Use AIE RoPE (y/n)", "n", str
            ) in ("y", "yes")
            self.npu_config.use_aie_ffn = ask_value(
                "Use AIE FFN (y/n)", "y", str
            ) in ("y", "yes")

        # Allow output dir override
        if not self.batch:
            new_dir = input(
                f"  Output directory [{self.output_dir}]: "
            ).strip()
            if new_dir:
                self.output_dir = Path(new_dir)
                self.state.output_dir = str(self.output_dir)

        # Clamp AIE columns to valid range
        self.npu_config.num_aie_columns = max(
            1, min(self.npu_config.num_aie_columns, 8)
        )

        npu_dict = {
            "num_aie_columns": self.npu_config.num_aie_columns,
            "tile_m": self.npu_config.tile_m,
            "tile_k": self.npu_config.tile_k,
            "tile_n": self.npu_config.tile_n,
            "max_seq_len": self.npu_config.max_seq_len,
            "batch_size": self.npu_config.batch_size,
            "use_aie_gemm": self.npu_config.use_aie_gemm,
            "use_aie_gemv": self.npu_config.use_aie_gemv,
            "use_aie_norm": self.npu_config.use_aie_norm,
            "use_aie_attention": self.npu_config.use_aie_attention,
            "use_aie_rope": self.npu_config.use_aie_rope,
            "use_aie_ffn": self.npu_config.use_aie_ffn,
        }
        self.state.npu_config = npu_dict
        print_ok(f"NPU config: {self.npu_config.num_aie_columns} columns, "
                  f"tiles={self.npu_config.tile_m}/{self.npu_config.tile_k}/{self.npu_config.tile_n}")
        return True

    # ---- Phase 5: Weight Loading ------------------------------------------

    def _phase_5_weight_loading(self) -> bool:
        """ACTUALLY load weight tensors from safetensors or pytorch files.

        Uses safetensors safe_open with numpy for efficient memory-mapped
        access. Falls back to torch.load for .bin/.pt files.

        Returns:
            True if weights were loaded successfully.
        """
        model_path = Path(self.state.model_path)
        weight_files = [Path(f) for f in self.state.weight_files]

        if not weight_files:
            print_err("No weight files to load.")
            return False

        # Detect format
        first_file = weight_files[0]
        if first_file.suffix == ".safetensors":
            self.state.weight_format = "safetensors"
        elif first_file.suffix in (".bin", ".pt"):
            self.state.weight_format = "pytorch"
        else:
            # Check if there's an index file
            index_path = model_path / "model.safetensors.index.json"
            if index_path.exists():
                self.state.weight_format = "safetensors"
            else:
                print_err(f"Unknown weight file format: {first_file.suffix}")
                return False

        print_info(f"Loading weights (format: {self.state.weight_format})...")

        if self.state.weight_format == "safetensors":
            if not HAS_SAFETENSORS:
                print_err("safetensors is not installed. pip install safetensors")
                return False
            self._load_safetensors(weight_files, model_path)
        else:
            self._load_pytorch(weight_files)

        # Display summary
        total_bytes = sum(
            arr.nbytes for arr in self.loaded_tensors.values()
        )
        self.state.tensor_count = len(self.loaded_tensors)
        self.state.total_weight_bytes = total_bytes
        self.state.tensor_index = {
            name: self._tensor_file_map.get(name, "unknown")
            for name in self.loaded_tensors
        }

        self.display.show_tensor_summary(
            self.state.tensor_index, total_bytes
        )
        print_ok(
            f"Loaded {self.state.tensor_count} tensors "
            f"({_format_bytes(total_bytes)})"
        )
        return True

    def _load_safetensors(
        self, weight_files: List[Path], model_path: Path
    ) -> None:
        """Load weights from safetensors files using numpy.

        Args:
            weight_files: List of .safetensors file paths.
            model_path: Root model directory (for index resolution).
        """
        self._tensor_file_map.clear()

        # Check for sharded index
        index_path = model_path / "model.safetensors.index.json"
        if index_path.exists():
            with open(index_path, "r") as f:
                index = json.load(f)
            weight_map = index.get("weight_map", {})
        else:
            weight_map = {}

        for wf in weight_files:
            file_name = wf.name
            print_info(f"  Loading {file_name}...")

            with safe_open(str(wf), framework="numpy", device="cpu") as f:
                keys = f.keys()
                prog = make_progress()
                if prog:
                    with prog:
                        task = prog.add_task(
                            description=file_name, total=len(keys)
                        )
                        for key in keys:
                            self.loaded_tensors[key] = f.get_tensor(key)
                            self._tensor_file_map[key] = file_name
                            prog.update(task, advance=1)
                else:
                    for i, key in enumerate(keys):
                        self.loaded_tensors[key] = f.get_tensor(key)
                        self._tensor_file_map[key] = file_name
                        if i % 50 == 0:
                            print_info(f"    {i}/{len(keys)} tensors...")

    def _load_pytorch(self, weight_files: List[Path]) -> None:
        """Load weights from PyTorch checkpoint files.

        Args:
            weight_files: List of .bin or .pt file paths.
        """
        try:
            import torch
        except ImportError:
            print_err("PyTorch is required for .bin/.pt weight files.")
            return

        self._tensor_file_map.clear()

        for wf in weight_files:
            file_name = wf.name
            print_info(f"  Loading {file_name}...")

            state_dict = torch.load(str(wf), map_location="cpu", weights_only=True)
            if not isinstance(state_dict, dict):
                print_err(f"Unexpected checkpoint format in {file_name}")
                continue

            for key, tensor in state_dict.items():
                numpy_arr = self._torch_to_numpy(tensor)
                self.loaded_tensors[key] = numpy_arr
                self._tensor_file_map[key] = file_name

    @staticmethod
    def _torch_to_numpy(tensor: Any) -> np.ndarray:
        """Convert a PyTorch tensor to numpy, handling bfloat16.

        Args:
            tensor: PyTorch tensor.

        Returns:
            NumPy array.
        """
        import torch

        t = tensor.detach()
        if t.device.type != "cpu":
            t = t.cpu()
        if not t.is_contiguous():
            t = t.contiguous()
        if t.dtype == torch.bfloat16:
            u16_np = t.view(torch.uint16).numpy()
            return u16_np.view(np.dtype("bfloat16"))
        return t.numpy()

    # ---- Phase 6: Weight Mapping ------------------------------------------

    def _phase_6_weight_mapping(self) -> bool:
        """Map HuggingFace weight names to IRON names with transforms.

        Uses the WeightMapper pattern matching system. Since we loaded
        tensors as numpy (not torch), we handle the transform step
        directly without requiring torch.

        Returns:
            True if at least one weight was successfully mapped.
        """
        if not self.norm_config:
            print_err("No normalized config available. Run phase 2 first.")
            return False

        arch_value = self.norm_config.architecture.value
        print_info(f"Mapping weights for architecture: {arch_value}")

        self.weight_mapper = create_weight_mapper(arch_value)

        patterns = self.weight_mapper.patterns
        mapped: Dict[str, MappedWeight] = {}
        unmapped: List[str] = []
        transform_counts: Dict[str, int] = {}

        prog = make_progress()
        tensor_items = list(self.loaded_tensors.items())

        if prog:
            with prog:
                task = prog.add_task(
                    description="Mapping weights", total=len(tensor_items)
                )
                for hf_name, tensor in tensor_items:
                    result = self._map_single(
                        hf_name, tensor, patterns, self.weight_mapper
                    )
                    if result is not None:
                        mapped[result.name] = result
                        self.transformed_tensors[result.name] = result.tensor
                        tname = result.transform.value
                        transform_counts[tname] = (
                            transform_counts.get(tname, 0) + 1
                        )
                    else:
                        unmapped.append(hf_name)
                    prog.update(task, advance=1)
        else:
            for i, (hf_name, tensor) in enumerate(tensor_items):
                result = self._map_single(
                    hf_name, tensor, patterns, self.weight_mapper
                )
                if result is not None:
                    mapped[result.name] = result
                    self.transformed_tensors[result.name] = result.tensor
                    tname = result.transform.value
                    transform_counts[tname] = (
                        transform_counts.get(tname, 0) + 1
                    )
                else:
                    unmapped.append(hf_name)
                if i % 100 == 0 and i > 0:
                    print_info(f"    {i}/{len(tensor_items)} mapped...")

        self.state.mapped_weights = {
            name: {
                "original_name": mw.original_name,
                "transform": mw.transform.value,
                "shape": list(mw.tensor.shape),
                "dtype": str(mw.tensor.dtype),
            }
            for name, mw in mapped.items()
        }
        self.state.mapped_count = len(mapped)
        self.state.unmapped_names = unmapped

        self.display.show_mapping_summary(
            len(mapped), unmapped, transform_counts
        )

        if unmapped:
            self.warnings.append(
                f"{len(unmapped)} weight(s) could not be mapped"
            )
            print_warn(f"{len(unmapped)} unmapped weight(s)")
            for name in unmapped[:5]:
                print_info(f"  - {name}")
            if len(unmapped) > 5:
                print_info(f"  ... and {len(unmapped) - 5} more")

        if len(mapped) == 0:
            print_err("No weights were mapped. Check architecture detection.")
            return False

        print_ok(f"Mapped {len(mapped)} weights")
        return True

    def _map_single(
        self,
        hf_name: str,
        tensor: np.ndarray,
        patterns: Dict[str, Tuple[str, WeightTransform]],
        mapper: WeightMapper,
    ) -> Optional[MappedWeight]:
        """Map a single weight tensor to IRON format.

        Args:
            hf_name: Original HuggingFace weight name.
            tensor: Weight tensor as numpy array.
            patterns: Architecture-specific regex patterns.
            mapper: The WeightMapper instance (for reference).

        Returns:
            MappedWeight or None if no pattern matched.
        """
        for pattern, (template, transform) in patterns.items():
            match = re.match(pattern, hf_name)
            if match:
                if match.groups():
                    layer_idx = match.group(1)
                    iron_name = template.format(layer_idx)
                else:
                    iron_name = template

                # Apply transform directly on numpy array
                transformed = self._apply_numpy_transform(
                    tensor, transform, hf_name
                )

                return MappedWeight(
                    name=iron_name,
                    original_name=hf_name,
                    tensor=transformed,
                    transform=transform,
                    metadata={
                        "shape": list(tensor.shape),
                        "dtype": str(tensor.dtype),
                    },
                )

        # No pattern matched
        return None

    def _apply_numpy_transform(
        self,
        tensor: np.ndarray,
        transform: WeightTransform,
        hf_name: str,
    ) -> np.ndarray:
        """Apply a weight transform to a numpy array.

        Args:
            tensor: Input numpy array.
            transform: Transform type to apply.
            hf_name: Original weight name (for error messages).

        Returns:
            Transformed numpy array.
        """
        if transform == WeightTransform.NONE:
            return tensor
        elif transform in (WeightTransform.TRANSPOSE, WeightTransform.TRANSPOSE_KV):
            if tensor.ndim == 2:
                return tensor.T
            return tensor
        elif transform == WeightTransform.DEQUANT:
            logger.warning("DEQUANT transform not yet supported for %s", hf_name)
            self.warnings.append(
                f"DEQUANT transform skipped for {hf_name}"
            )
            return tensor
        elif transform == WeightTransform.RESHAPE:
            return tensor
        return tensor

    # ---- Phase 7: Shape Analysis ------------------------------------------

    def _phase_7_shape_analysis(self) -> bool:
        """Compute padded shapes for all model components via ShapeManager.

        Returns:
            True if shapes were computed successfully.
        """
        if not self.norm_config:
            print_err("No normalized config. Run phase 2 first.")
            return False

        cfg = self.norm_config
        npc = self.npu_config

        self.shape_manager = create_shape_manager(
            hidden_size=cfg.hidden_size,
            num_heads=cfg.num_attention_heads,
            num_kv_heads=cfg.num_kv_heads,
            num_aie_columns=npc.num_aie_columns,
        )

        shapes: Dict[str, Any] = {}

        # GEMM shapes for attention projections
        hs = cfg.hidden_size
        nkv = cfg.num_kv_heads or cfg.num_attention_heads
        hd = cfg.head_dim
        kv_dim = nkv * hd
        bs = npc.batch_size
        sl = npc.max_seq_len
        total_tokens = bs * sl

        shapes["q_proj"] = self._padded_shape_to_dict(
            self.shape_manager.calculate_padded_gemm_shape(total_tokens, hs, hs)
        )
        shapes["k_proj"] = self._padded_shape_to_dict(
            self.shape_manager.calculate_padded_gemm_shape(
                total_tokens, hs, kv_dim
            )
        )
        shapes["v_proj"] = self._padded_shape_to_dict(
            self.shape_manager.calculate_padded_gemm_shape(
                total_tokens, hs, kv_dim
            )
        )
        shapes["o_proj"] = self._padded_shape_to_dict(
            self.shape_manager.calculate_padded_gemm_shape(total_tokens, hs, hs)
        )

        # FFN shapes
        intermediate = cfg.intermediate_size
        if intermediate > 0:
            shapes["gate_up_proj"] = self._padded_shape_to_dict(
                self.shape_manager.calculate_padded_gemm_shape(
                    total_tokens, hs, intermediate * 2
                )
            )
            shapes["down_proj"] = self._padded_shape_to_dict(
                self.shape_manager.calculate_padded_gemm_shape(
                    total_tokens, intermediate, hs
                )
            )

        # KV cache
        kv_cache = self.shape_manager.calculate_kv_cache_size(
            max_seq_len=npc.max_seq_len,
            batch_size=npc.batch_size,
        )
        shapes["kv_cache"] = {
            "k_elements": kv_cache["k_cache_elements"],
            "v_elements": kv_cache["v_cache_elements"],
            "k_bytes": kv_cache["k_cache_bytes"],
            "v_bytes": kv_cache["v_cache_bytes"],
            "total_bytes": kv_cache["k_cache_bytes"] + kv_cache["v_cache_bytes"],
        }

        # LM head
        if cfg.vocab_size > 0:
            shapes["lm_head"] = self._padded_shape_to_dict(
                self.shape_manager.calculate_lm_head_shape(
                    bs, sl, cfg.vocab_size
                )
            )

        # Norm shapes
        shapes["norm"] = self._padded_shape_to_dict(
            self.shape_manager.calculate_norm_shape(bs, sl)
        )

        # Embedding
        shapes["embedding"] = self._padded_shape_to_dict(
            self.shape_manager.calculate_embedding_shape(
                cfg.vocab_size, hs
            )
        )

        self.state.shapes = shapes
        self.display.show_shapes(shapes)
        print_ok(f"Computed shapes for {len(shapes)} components")
        return True

    @staticmethod
    def _padded_shape_to_dict(ps: Any) -> Dict[str, Any]:
        """Convert a PaddedShape to a display-friendly dictionary.

        Args:
            ps: PaddedShape instance.

        Returns:
            Dictionary with original, padded, and padding info.
        """
        return {
            "original": list(ps.original_shape),
            "padded": list(ps.padded_shape),
            "padding": ps.padding,
            "is_padded": ps.is_padded,
        }

    # ---- Phase 8: Model Assembly Info -------------------------------------

    def _phase_8_model_assembly(self) -> bool:
        """Count operators needed and compute memory requirements.

        This phase does NOT instantiate AIE operators (which require
        hardware-specific compilation). It only computes the inventory.

        Returns:
            True (informational phase).
        """
        if not self.norm_config:
            print_err("No normalized config. Run phase 2 first.")
            return False

        cfg = self.norm_config
        npc = self.npu_config
        n_layers = cfg.num_hidden_layers

        operators: Dict[str, int] = {}

        # Per-layer operators
        operators["GEMM (Q proj)"] = n_layers if npc.use_aie_gemm else 0
        operators["GEMM (K proj)"] = n_layers if npc.use_aie_gemm else 0
        operators["GEMM (V proj)"] = n_layers if npc.use_aie_gemm else 0
        operators["GEMM (O proj)"] = n_layers if npc.use_aie_gemm else 0
        operators["GEMM (gate proj)"] = n_layers if npc.use_aie_ffn else 0
        operators["GEMM (up proj)"] = n_layers if npc.use_aie_ffn else 0
        operators["GEMM (down proj)"] = n_layers if npc.use_aie_ffn else 0
        operators["RMSNorm (norm1)"] = n_layers if npc.use_aie_norm else 0
        operators["RMSNorm (norm2)"] = n_layers if npc.use_aie_norm else 0
        operators["ElementwiseAdd (residual 1)"] = n_layers
        operators["ElementwiseAdd (residual 2)"] = n_layers

        # Global operators
        operators["RMSNorm (final norm)"] = 1 if npc.use_aie_norm else 0
        operators["GEMM (LM head)"] = 1 if npc.use_aie_gemm else 0

        total = sum(operators.values())

        # Memory requirements
        memory: Dict[str, int] = {}
        if self.shape_manager and cfg.intermediate_size > 0:
            memory = self.shape_manager.get_memory_requirements(
                max_seq_len=npc.max_seq_len,
                batch_size=npc.batch_size,
                intermediate_size=cfg.intermediate_size,
            )

        # Weight memory
        weight_mem = self.state.total_weight_bytes
        memory["weight_data"] = weight_mem

        summary = {
            "operators": operators,
            "total_operators": total,
            "memory": memory,
            "num_layers": n_layers,
            "architecture": cfg.architecture.value,
        }
        self.state.operator_summary = summary

        self.display.show_operators(summary)
        print_ok(f"Total operators: {total} across {n_layers} layers")
        return True

    # ---- Phase 9: Export --------------------------------------------------

    def _phase_9_export(self) -> bool:
        """Save mapped weights as .npy files and write manifest files.

        Exports:
            - weights/*.npy: Individual weight files
            - config.json: Complete IRON configuration
            - model_info.json: Model summary
            - conversion_manifest.json: Full conversion metadata

        Returns:
            True if export completed successfully.
        """
        out = self.output_dir
        weights_dir = out / "weights"

        # Guard: verify tensor data is available before export
        if not self.transformed_tensors:
            if self.state.mapped_count > 0:
                print_err(
                    f"Checkpoint resume detected {self.state.mapped_count} mapped weights, "
                    "but tensor data is not in memory. Re-run from Phase 5 to reload weights."
                )
                return False
            print_err("No transformed tensors available for export.")
            return False

        # Clean or create output directory
        if out.exists():
            if self.force:
                # Only clean weights/ subdirectory to preserve checkpoint
                if weights_dir.exists():
                    shutil.rmtree(weights_dir)
            else:
                if not self.batch:
                    if not confirm(
                        f"Output directory {out} exists. Clean weights and re-export?"
                    ):
                        print_info("Skipping export.")
                        return True
                if weights_dir.exists():
                    shutil.rmtree(weights_dir)

        weights_dir.mkdir(parents=True, exist_ok=True)

        # Save mapped weights as .npy
        print_info(f"Saving {self.state.mapped_count} weights to {weights_dir}...")

        prog = make_progress()
        mapped_items = list(self.transformed_tensors.items())

        if prog:
            with prog:
                task = prog.add_task(
                    description="Saving .npy files", total=len(mapped_items)
                )
                for iron_name, numpy_array in mapped_items:
                    safe = _safe_name(iron_name)
                    np.save(str(weights_dir / f"{safe}.npy"), numpy_array)
                    prog.update(task, advance=1)
        else:
            for i, (iron_name, numpy_array) in enumerate(mapped_items):
                safe = _safe_name(iron_name)
                np.save(str(weights_dir / f"{safe}.npy"), numpy_array)
                if i % 50 == 0 and i > 0:
                    print_info(f"    {i}/{len(mapped_items)} saved...")

        print_ok(f"Saved {len(mapped_items)} .npy files")

        # Save config.json
        config_out = {
            "model_name": self.model_name,
            "architecture": self.norm_config.to_dict()
            if self.norm_config
            else {},
            "npu_config": self.npu_config.__dict__,
            "conversion_date": datetime.now(timezone.utc).isoformat(),
        }
        with open(out / "config.json", "w") as f:
            json.dump(config_out, f, indent=2, default=str)
        print_ok("Saved config.json")

        # Save model_info.json
        model_info = self._build_model_info()
        with open(out / "model_info.json", "w") as f:
            json.dump(model_info, f, indent=2, default=str)
        print_ok("Saved model_info.json")

        # Save conversion_manifest.json
        manifest = self._build_manifest()
        with open(out / "conversion_manifest.json", "w") as f:
            json.dump(manifest, f, indent=2, default=str)
        print_ok("Saved conversion_manifest.json")

        # Save weight manifest for quick lookup
        weight_manifest = []
        for iron_name, numpy_array in mapped_items:
            safe = _safe_name(iron_name)
            meta = self.state.mapped_weights.get(iron_name, {})
            weight_manifest.append({
                "iron_name": iron_name,
                "hf_name": meta.get("original_name", iron_name),
                "file": f"weights/{safe}.npy",
                "shape": list(numpy_array.shape),
                "dtype": str(numpy_array.dtype),
                "transform": meta.get("transform", "identity"),
            })
        with open(out / "weight_manifest.json", "w") as f:
            json.dump(weight_manifest, f, indent=2)
        print_ok("Saved weight_manifest.json")

        return True

    def _build_model_info(self) -> Dict[str, Any]:
        """Build model summary dictionary.

        Returns:
            Dictionary with model architecture, NPU config, and
            conversion statistics.
        """
        info: Dict[str, Any] = {
            "model_name": self.model_name,
            "model_path": self.state.model_path,
            "is_hub_model": self.state.is_hub_model,
            "conversion_date": datetime.now(timezone.utc).isoformat(),
        }

        if self.norm_config:
            info["architecture"] = self.norm_config.to_dict()

        info["npu_config"] = self.npu_config.__dict__
        info["weight_format"] = self.state.weight_format
        info["tensor_count"] = self.state.tensor_count
        info["mapped_count"] = self.state.mapped_count
        info["unmapped_count"] = len(self.state.unmapped_names)
        info["total_weight_size"] = _format_bytes(self.state.total_weight_bytes)

        if self.state.operator_summary:
            info["operator_summary"] = self.state.operator_summary

        if self.state.shapes:
            info["shapes"] = self.state.shapes

        return info

    def _build_manifest(self) -> Dict[str, Any]:
        """Build conversion manifest with timestamps and warnings.

        Returns:
            Dictionary with full conversion metadata.
        """
        return {
            "version": "1.0.0",
            "converter": "iron.model_convert.interactive_convert",
            "model_name": self.model_name,
            "model_path": self.state.model_path,
            "is_hub_model": self.state.is_hub_model,
            "started_at": self.state.started_at,
            "completed_at": datetime.now(timezone.utc).isoformat(),
            "phases_completed": self.state.phase_completed,
            "weight_format": self.state.weight_format,
            "weight_files": self.state.weight_files,
            "tensor_count": self.state.tensor_count,
            "total_weight_bytes": self.state.total_weight_bytes,
            "mapped_count": self.state.mapped_count,
            "unmapped_names": self.state.unmapped_names[:20],
            "unmapped_truncated": len(self.state.unmapped_names) > 20,
            "warnings": self.warnings,
            "npu_config": self.npu_config.__dict__,
            "output_directory": str(self.output_dir),
        }

    # ---- Checkpoint / Resume ----------------------------------------------

    def _save_checkpoint(self) -> None:
        """Persist current state to a JSON checkpoint file.

        The checkpoint enables resuming a partially completed conversion.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        try:
            with open(self.checkpoint_path, "w") as f:
                json.dump(self.state.to_dict(), f, indent=2, default=str)
            logger.debug("Checkpoint saved to %s", self.checkpoint_path)
        except Exception as exc:
            logger.warning("Failed to save checkpoint: %s", exc)

    def _try_resume(self) -> None:
        """Attempt to load state from an existing checkpoint file."""
        try:
            with open(self.checkpoint_path, "r") as f:
                data = json.load(f)
            self.state = ConversionState.from_dict(data)
            phase = self.state.phase_completed
            if phase > 0:
                print_info(
                    f"Found checkpoint from {self.state.started_at} "
                    f"(phase {phase} completed). Resuming..."
                )
                # Restore npu_config from checkpoint if available
                if self.state.npu_config:
                    self.npu_config = NPUConfig(**self.state.npu_config)
        except Exception as exc:
            logger.debug("Could not load checkpoint: %s", exc)

    # ---- Summary ----------------------------------------------------------

    def _print_summary(self) -> None:
        """Print final conversion summary."""
        print_info("")
        print_info("Conversion Summary:")
        print_info(f"  Model: {self.model_name}")
        print_info(f"  Output: {self.output_dir}")
        print_info(f"  Architecture: {self.norm_config.architecture.value if self.norm_config else 'N/A'}")
        print_info(f"  Tensors loaded: {self.state.tensor_count}")
        print_info(f"  Weights mapped: {self.state.mapped_count}")
        print_info(f"  Unmapped: {len(self.state.unmapped_names)}")
        print_info(f"  Weight data: {_format_bytes(self.state.total_weight_bytes)}")

        if self.warnings:
            print_warn(f"Warnings ({len(self.warnings)}):")
            for w in self.warnings[:5]:
                print_info(f"  - {w}")
            if len(self.warnings) > 5:
                print_info(f"  ... and {len(self.warnings) - 5} more")

        print_info("")
        print_info("Files generated:")
        print_info(f"  {self.output_dir}/config.json")
        print_info(f"  {self.output_dir}/model_info.json")
        print_info(f"  {self.output_dir}/conversion_manifest.json")
        print_info(f"  {self.output_dir}/weight_manifest.json")
        print_info(f"  {self.output_dir}/weights/*.npy ({self.state.mapped_count} files)")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> int:
    """CLI entry point for the interactive converter.

    Returns:
        Exit code: 0 for success, 1 for failure.
    """
    parser = argparse.ArgumentParser(
        description="IRON Interactive Model Converter - Convert HuggingFace models to IRON NPU format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode with a local model directory
  python -m iron.model_convert.interactive_convert ./my_model_dir

  # Convert from HuggingFace Hub (downloads automatically)
  python -m iron.model_convert.interactive_convert meta-llama/Llama-2-7b-hf

  # Batch mode with custom output directory
  python -m iron.model_convert.interactive_convert mistralai/Mistral-7B-v0.1 -o ./output --batch

  # Force overwrite existing output
  python -m iron.model_convert.interactive_convert ./model -o ./output --force

  # Verbose mode for debugging
  python -m iron.model_convert.interactive_convert ./model --verbose
        """,
    )

    parser.add_argument(
        "model",
        help="Model name (HuggingFace Hub) or local directory path",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=None,
        help="Output directory for converted files (default: output/<model_name>)",
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Run in non-interactive batch mode (no prompts)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output without confirmation",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose/debug logging",
    )

    args = parser.parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # Run converter
    converter = InteractiveConverter(
        model=args.model,
        output_dir=args.output_dir,
        batch=args.batch,
        force=args.force,
        verbose=args.verbose,
    )

    try:
        success = converter.run()
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        return 130
    except Exception as exc:
        print_err(f"Unhandled exception: {exc}")
        if args.verbose:
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
