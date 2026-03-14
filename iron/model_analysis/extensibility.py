# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Extensibility Framework for IRON

This module provides a plugin system for extending IRON with:
- New operator types
- Custom layer implementations
- Architecture-specific handlers
- Dynamic operator discovery and registration

Users can extend IRON to support new models without modifying core code.
"""

import importlib
import inspect
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Type, Union
import logging

from .architecture_scanner import LayerCategory, ArchitectureRequirements
from .capability_registry import (
    register_custom_operator,
    register_architecture_support,
    SupportLevel,
)

logger = logging.getLogger(__name__)


@dataclass
class OperatorTemplate:
    """
    Template for implementing a new NPU operator.

    Provides the structure needed to implement a custom operator.
    """
    name: str
    category: LayerCategory
    description: str = ""

    # Required methods to implement
    required_methods: List[str] = field(default_factory=lambda: [
        "set_up_artifacts",
        "set_up_runtime",
        "forward",
    ])

    # Base class to inherit from
    base_class: str = "AIEOperatorBase"

    # Example implementation
    example_code: str = ""

    # Dependencies
    requires_kernel: bool = True
    kernel_source_template: str = ""


@dataclass
class ArchitectureHandler:
    """
    Handler for a specific model architecture.

    Defines how to convert a specific architecture to IRON.
    """
    architecture_name: str
    model_types: List[str]

    # Layer mappings: HF layer name -> IRON operator
    layer_mappings: Dict[str, str] = field(default_factory=dict)

    # Special handling methods
    custom_handlers: Dict[str, Callable] = field(default_factory=dict)

    # Default configuration
    default_config: Dict[str, Any] = field(default_factory=dict)


class CustomOperatorBase(ABC):
    """
    Abstract base class for custom NPU operators.

    Subclass this to implement new operators for unsupported layers.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Operator name"""
        pass

    @property
    @abstractmethod
    def category(self) -> LayerCategory:
        """Operator category"""
        pass

    @abstractmethod
    def set_up_artifacts(self):
        """Set up compilation artifacts"""
        pass

    @abstractmethod
    def set_up_runtime(self):
        """Set up runtime buffers and kernels"""
        pass

    @abstractmethod
    def forward(self, *args, **kwargs):
        """Forward pass implementation"""
        pass

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)


class OperatorRegistry:
    """
    Registry for custom operators.

    Allows dynamic registration and discovery of operators.
    """

    _instance: Optional["OperatorRegistry"] = None
    _operators: Dict[str, Type[CustomOperatorBase]] = {}
    _templates: Dict[str, OperatorTemplate] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def register(cls, name: str = None):
        """
        Decorator to register a custom operator.

        Usage:
            @OperatorRegistry.register("my_custom_op")
            class MyCustomOp(CustomOperatorBase):
                ...
        """
        def decorator(op_class: Type[CustomOperatorBase]) -> Type[CustomOperatorBase]:
            op_name = name or op_class.__name__
            cls._operators[op_name] = op_class
            logger.info(f"Registered custom operator: {op_name}")
            return op_class
        return decorator

    @classmethod
    def get_operator(cls, name: str) -> Optional[Type[CustomOperatorBase]]:
        """Get a registered operator by name"""
        return cls._operators.get(name)

    @classmethod
    def list_operators(cls) -> List[str]:
        """List all registered operators"""
        return list(cls._operators.keys())

    @classmethod
    def create_operator(cls, name: str, *args, **kwargs) -> Optional[CustomOperatorBase]:
        """Create an instance of a registered operator"""
        op_class = cls.get_operator(name)
        if op_class:
            return op_class(*args, **kwargs)
        return None

    @classmethod
    def register_template(cls, template: OperatorTemplate):
        """Register an operator template"""
        cls._templates[template.name] = template

    @classmethod
    def get_template(cls, name: str) -> Optional[OperatorTemplate]:
        """Get an operator template by name"""
        return cls._templates.get(name)


class ArchitectureRegistry:
    """
    Registry for architecture-specific handlers.
    """

    _instance: Optional["ArchitectureRegistry"] = None
    _handlers: Dict[str, ArchitectureHandler] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def register_handler(cls, handler: ArchitectureHandler):
        """Register an architecture handler"""
        for model_type in handler.model_types:
            cls._handlers[model_type.lower()] = handler
        logger.info(f"Registered architecture handler: {handler.architecture_name}")

    @classmethod
    def get_handler(cls, model_type: str) -> Optional[ArchitectureHandler]:
        """Get handler for a model type"""
        return cls._handlers.get(model_type.lower())

    @classmethod
    def list_handlers(cls) -> List[str]:
        """List all registered architectures"""
        return list(cls._handlers.keys())


class ExtensionLoader:
    """
    Dynamically loads extensions from directories or modules.

    Scans for:
    - Custom operator implementations
    - Architecture handlers
    - Configuration files
    """

    def __init__(self, search_paths: Optional[List[str]] = None):
        """
        Initialize extension loader.

        Args:
            search_paths: Directories to search for extensions
        """
        self.search_paths = search_paths or []
        self._loaded_extensions: List[str] = []

    def add_search_path(self, path: str):
        """Add a search path for extensions"""
        self.search_paths.append(path)

    def load_all(self) -> Dict[str, Any]:
        """
        Load all extensions from search paths.

        Returns:
            Dictionary of loaded extensions
        """
        results = {
            "operators": [],
            "handlers": [],
            "configs": [],
        }

        for search_path in self.search_paths:
            path = Path(search_path)
            if not path.exists():
                continue

            # Load Python modules
            for py_file in path.glob("*.py"):
                if py_file.name.startswith("_"):
                    continue

                loaded = self._load_module(py_file)
                if loaded:
                    results["operators"].extend(loaded.get("operators", []))
                    results["handlers"].extend(loaded.get("handlers", []))

        self._loaded_extensions = list(results.keys())
        return results

    def _load_module(self, path: Path) -> Optional[Dict[str, Any]]:
        """Load a Python module and extract extensions"""
        try:
            spec = importlib.util.spec_from_file_location(
                path.stem, str(path)
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            result = {}

            # Find operator classes
            operators = []
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, CustomOperatorBase) and obj != CustomOperatorBase:
                    operators.append(name)
                    # Auto-register
                    OperatorRegistry._operators[name] = obj

            if operators:
                result["operators"] = operators

            # Find architecture handlers
            for name, obj in inspect.getmembers(module):
                if isinstance(obj, ArchitectureHandler):
                    ArchitectureRegistry.register_handler(obj)
                    if "handlers" not in result:
                        result["handlers"] = []
                    result["handlers"].append(obj.architecture_name)

            return result

        except Exception as e:
            logger.warning(f"Failed to load extension {path}: {e}")
            return None


# === Operator Templates ===
# Pre-defined templates for common custom operators

TEMPLATES = {
    "sliding_window_attention": OperatorTemplate(
        name="AIESlidingWindowAttention",
        category=LayerCategory.ATTENTION,
        description="Sliding window attention for models like Mistral",
        required_methods=[
            "set_up_artifacts",
            "set_up_runtime",
            "forward",
            "_apply_sliding_mask",
        ],
        base_class="AIEOperatorBase",
        example_code="""
class AIESlidingWindowAttention(AIEOperatorBase):
    def __init__(self, window_size, num_heads, head_dim, **kwargs):
        self.window_size = window_size
        self.num_heads = num_heads
        self.head_dim = head_dim
        super().__init__(**kwargs)

    def set_up_artifacts(self):
        # Define MLIR generation and compilation artifacts
        pass

    def set_up_runtime(self):
        # Define buffers and kernel bindings
        pass

    def forward(self, q, k, v):
        # Implement sliding window attention
        pass
""",
    ),

    "moe_layer": OperatorTemplate(
        name="AIEMoELayer",
        category=LayerCategory.LINEAR,
        description="Mixture of Experts layer with routing",
        required_methods=[
            "set_up_artifacts",
            "set_up_runtime",
            "forward",
            "_route_tokens",
            "_combine_expert_outputs",
        ],
        base_class="AIEOperatorBase",
        example_code="""
class AIEMoELayer(AIEOperatorBase):
    def __init__(self, num_experts, top_k, hidden_dim, **kwargs):
        self.num_experts = num_experts
        self.top_k = top_k
        self.hidden_dim = hidden_dim
        super().__init__(**kwargs)

    def set_up_artifacts(self):
        pass

    def set_up_runtime(self):
        pass

    def _route_tokens(self, x):
        # Implement token routing to experts
        pass

    def forward(self, x):
        # Route tokens, process through experts, combine outputs
        pass
""",
    ),

    "multi_token_head": OperatorTemplate(
        name="AIMultiTokenHead",
        category=LayerCategory.LINEAR,
        description="Multi-token prediction head",
        required_methods=[
            "set_up_artifacts",
            "set_up_runtime",
            "forward",
        ],
        base_class="AIEOperatorBase",
    ),
}


# Register built-in templates
for name, template in TEMPLATES.items():
    OperatorRegistry.register_template(template)


def get_operator_template(operator_name: str) -> Optional[OperatorTemplate]:
    """Get a template for implementing an operator"""
    return OperatorRegistry.get_template(operator_name)


def generate_operator_skeleton(
    operator_name: str,
    output_path: str,
    template: Optional[OperatorTemplate] = None,
) -> str:
    """
    Generate a skeleton implementation for a custom operator.

    Args:
        operator_name: Name for the operator
        output_path: Path to write the generated file
        template: Optional template to use

    Returns:
        Path to generated file
    """
    if template is None:
        # Try to find matching template
        for name, tmpl in TEMPLATES.items():
            if name.lower() in operator_name.lower():
                template = tmpl
                break

    if template is None:
        template = OperatorTemplate(
            name=operator_name,
            category=LayerCategory.CUSTOM,
            description=f"Custom NPU operator: {operator_name}",
        )

    # Generate skeleton code
    skeleton = f'''
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
{template.description}

Generated skeleton for: {template.name}
"""

from iron.common import AIEOperatorBase, AIEContext
from iron.common.compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from pathlib import Path


class {template.name}(AIEOperatorBase):
    """
    {template.description}

    TODO: Implement the following methods:
    {chr(10).join(f"    - {m}" for m in template.required_methods)}
    """

    def __init__(
        self,
        # TODO: Add operator-specific parameters
        size: int,
        context=None,
    ):
        self.size = size
        super().__init__(context=context)

    def set_up_artifacts(self):
        """
        Set up compilation artifacts.

        TODO: Define MLIR generation and compilation dependencies.
        """
        operator_dir = Path(__file__).parent

        # Example:
        # mlir_artifact = PythonGeneratedMLIRArtifact.new(
        #     f"{{template.name.lower()}}.mlir",
        #     import_path=operator_dir / "design.py",
        #     callback_fn="generate_mlir",
        #     callback_kwargs={{...}},
        # )
        pass

    def set_up_runtime(self):
        """
        Set up runtime buffers and kernels.

        TODO: Define buffer sizes and kernel bindings.
        """
        # Example:
        # self.add_buffer("input", self.size)
        # self.add_buffer("output", self.size)
        # self.add_kernel("kernel_name", ...)
        # self.add_to_runlist("kernel_name", "input", "output")
        pass

    def forward(self, x):
        """
        Forward pass.

        TODO: Implement the actual computation.

        Args:
            x: Input tensor

        Returns:
            Output tensor
        """
        # Validate input
        applicable = len(x.shape) >= 1 and x.shape[-1] <= self.size
        if not applicable:
            raise ValueError(f"Incompatible input shape: {{x.shape}}")

        # Execute AIE operation
        # self.write_buffer("input", x)
        # self.run_runlist()
        # result = self.read_buffer_as_torch("output", shape=x.shape)
        # return result
        return x


# Design file template (design.py)
"""
Design MLIR generation for {template.name}
"""

def generate_mlir(**kwargs):
    """
    Generate MLIR for the operator.

    TODO: Implement MLIR generation using AIE Iron API.
    """
    from aie.iron import Kernel, ObjectFifo, Program, Buffer, Runtime
    from aie.iron.placers import SequentialPlacer

    # Build program
    # rt = Runtime()
    # with rt.sequence(...) as (...):
    #     ...

    # program = Program(device_type, rt)
    # module = program.resolve_program(SequentialPlacer())
    # return module
"""
'''

    # Write to file
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w") as f:
        f.write(skeleton)

    logger.info(f"Generated operator skeleton at {output_file}")
    return str(output_file)


# === Extension Points ===

def register_extension_point(
    name: str,
    hook: Callable[[ArchitectureRequirements], Dict[str, Any]],
) -> None:
    """
    Register an extension point hook.

    Extension points allow modifying behavior at key points:
    - before_conversion: Before starting conversion
    - after_weight_load: After weights are loaded
    - before_compile: Before artifact compilation
    - after_convert: After conversion is complete

    Args:
        name: Extension point name
        hook: Callback function
    """
    if not hasattr(register_extension_point, "_hooks"):
        register_extension_point._hooks = {}

    if name not in register_extension_point._hooks:
        register_extension_point._hooks[name] = []

    register_extension_point._hooks[name].append(hook)
    logger.info(f"Registered extension hook: {name}")


def invoke_extension_point(
    name: str,
    requirements: ArchitectureRequirements,
) -> Dict[str, Any]:
    """
    Invoke all hooks for an extension point.

    Args:
        name: Extension point name
        requirements: Architecture requirements

    Returns:
        Combined results from all hooks
    """
    if not hasattr(register_extension_point, "_hooks"):
        return {}

    hooks = register_extension_point._hooks.get(name, [])
    results = {}

    for hook in hooks:
        try:
            result = hook(requirements)
            results.update(result)
        except Exception as e:
            logger.warning(f"Extension hook {name} failed: {e}")

    return results


# === Quick Registration Utilities ===

def quick_register_operator(
    name: str,
    module_patterns: List[str],
    category: str = "linear",
    support_level: str = "full",
) -> None:
    """
    Quickly register operator support via patterns.

    Usage:
        quick_register_operator(
            "MyCustomOp",
            module_patterns=["mymodel.CustomOp"],
            category="attention",
            support_level="partial",
        )
    """
    cat_map = {
        "attention": LayerCategory.ATTENTION,
        "linear": LayerCategory.LINEAR,
        "normalization": LayerCategory.NORMALIZATION,
        "activation": LayerCategory.ACTIVATION,
        "positional": LayerCategory.POSITIONAL,
    }

    level_map = {
        "full": SupportLevel.FULL,
        "partial": SupportLevel.PARTIAL,
        "fallback": SupportLevel.FALLBACK,
        "unsupported": SupportLevel.UNSUPPORTED,
    }

    register_custom_operator(
        name=name,
        category=cat_map.get(category.lower(), LayerCategory.CUSTOM),
        module_patterns=module_patterns,
        support_level=level_map.get(support_level.lower(), SupportLevel.PARTIAL),
    )


def quick_register_architecture(
    name: str,
    model_types: List[str],
    supported_layers: List[str],
) -> None:
    """
    Quickly register architecture support.

    Usage:
        quick_register_architecture(
            "MyModel",
            model_types=["mymodel"],
            supported_layers=["RMSNorm", "GEMM", "Attention"],
        )
    """
    register_architecture_support(
        architecture_name=name,
        model_types=model_types,
        supported_layers=supported_layers,
    )


__all__ = [
    # Base classes
    "CustomOperatorBase",
    "OperatorTemplate",
    "ArchitectureHandler",

    # Registries
    "OperatorRegistry",
    "ArchitectureRegistry",

    # Loader
    "ExtensionLoader",

    # Templates
    "TEMPLATES",
    "get_operator_template",
    "generate_operator_skeleton",

    # Extension points
    "register_extension_point",
    "invoke_extension_point",

    # Quick registration
    "quick_register_operator",
    "quick_register_architecture",
]
