# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Operator Factory for NPU Operations

This module provides a factory pattern for creating IRON NPU operators
based on model configuration. It handles the instantiation of GEMM,
RMSNorm, MHA, RoPE, and other operators with appropriate configurations.
"""

from typing import Any, Dict, List, Optional, Tuple, Type
from dataclasses import dataclass
from enum import Enum

from iron.common import AIEContext


class OperatorType(Enum):
    """Types of NPU operators"""

    GEMM = "gemm"
    GEMV = "gemv"
    RMS_NORM = "rms_norm"
    LAYER_NORM = "layer_norm"
    MHA = "mha"
    GQA = "gqa"
    ROPE = "rope"
    SOFTMAX = "softmax"
    SILU = "silu"
    SWIGLU = "swiglu"
    GELU = "gelu"
    ELEMENTWISE_ADD = "elementwise_add"
    ELEMENTWISE_MUL = "elementwise_mul"
    TRANSPOSE = "transpose"
    COPY = "copy"


@dataclass
class OperatorConfig:
    """Configuration for creating an NPU operator"""

    operator_type: OperatorType
    kwargs: Dict[str, Any]
    name: str = ""
    enabled: bool = True


class OperatorFactory:
    """
    Factory for creating IRON NPU operators.

    Provides a centralized way to instantiate operators with consistent
    configuration and proper NPU resource allocation.

    Example usage:
        factory = OperatorFactory(context=aie_context)
        gemm_op = factory.create_gemm(M=512, K=768, N=768, tile_m=64, ...)
        norm_op = factory.create_rms_norm(size=768, eps=1e-6, ...)
    """

    def __init__(
        self,
        context: Optional[AIEContext] = None,
        num_aie_columns: int = 8,
        default_dtype: str = "bfloat16",
    ):
        """
        Initialize the operator factory.

        Args:
            context: AIE context for operator creation
            num_aie_columns: Number of AIE columns to use
            default_dtype: Default data type for operators
        """
        self.context = context or AIEContext()
        self.num_aie_columns = num_aie_columns
        self.default_dtype = default_dtype

        # Cache for created operators
        self._operator_cache: Dict[str, Any] = {}

        # Default configurations for common operators
        self._default_configs = self._init_default_configs()

    def _init_default_configs(self) -> Dict[OperatorType, Dict[str, Any]]:
        """Initialize default configurations for each operator type"""
        return {
            OperatorType.GEMM: {
                "tile_m": 64,
                "tile_k": 64,
                "tile_n": 64,
                "num_aie_columns": self.num_aie_columns,
                "b_col_maj": True,
                "use_static_weight": False,
            },
            OperatorType.GEMV: {
                "tile_size_input": 4,
                "tile_size_output": 32,
                "num_aie_columns": self.num_aie_columns,
                "is_mv": True,
            },
            OperatorType.RMS_NORM: {
                "num_aie_columns": self.num_aie_columns,
                "num_channels": 2,
                "tile_size": 64,
                "eps": 1e-6,
            },
            OperatorType.LAYER_NORM: {
                "num_aie_columns": self.num_aie_columns,
                "num_channels": 2,
                "tile_size": 64,
                "eps": 1e-6,
            },
            OperatorType.MHA: {
                "num_of_pipelines": 1,
            },
            OperatorType.ROPE: {
                "num_aie_columns": self.num_aie_columns,
            },
            OperatorType.SOFTMAX: {
                "num_aie_columns": self.num_aie_columns,
            },
            OperatorType.SILU: {
                "num_aie_columns": self.num_aie_columns,
            },
            OperatorType.ELEMENTWISE_ADD: {
                "num_aie_columns": self.num_aie_columns,
                "num_channels": 2,
                "tile_size": 64,
            },
        }

    def _get_default_config(self, op_type: OperatorType) -> Dict[str, Any]:
        """Get default configuration for operator type"""
        return self._default_configs.get(op_type, {}).copy()

    def create_operator(
        self,
        operator_type: OperatorType,
        name: Optional[str] = None,
        cache: bool = False,
        **kwargs,
    ) -> Any:
        """
        Create an NPU operator.

        Args:
            operator_type: Type of operator to create
            name: Optional name for the operator
            cache: Whether to cache the created operator
            **kwargs: Operator-specific arguments

        Returns:
            Configured NPU operator instance
        """
        # Merge defaults with provided kwargs
        defaults = self._get_default_config(operator_type)
        defaults.update(kwargs)

        # Create the operator
        if operator_type == OperatorType.GEMM:
            op = self._create_gemm(**defaults)
        elif operator_type == OperatorType.GEMV:
            op = self._create_gemv(**defaults)
        elif operator_type == OperatorType.RMS_NORM:
            op = self._create_rms_norm(**defaults)
        elif operator_type == OperatorType.LAYER_NORM:
            op = self._create_layer_norm(**defaults)
        elif operator_type == OperatorType.MHA:
            op = self._create_mha(**defaults)
        elif operator_type == OperatorType.ROPE:
            op = self._create_rope(**defaults)
        elif operator_type == OperatorType.SOFTMAX:
            op = self._create_softmax(**defaults)
        elif operator_type == OperatorType.SILU:
            op = self._create_silu(**defaults)
        elif operator_type == OperatorType.SWIGLU:
            op = self._create_swiglu(**defaults)
        elif operator_type == OperatorType.ELEMENTWISE_ADD:
            op = self._create_elementwise_add(**defaults)
        elif operator_type == OperatorType.ELEMENTWISE_MUL:
            op = self._create_elementwise_mul(**defaults)
        else:
            raise ValueError(f"Unknown operator type: {operator_type}")

        # Cache if requested
        if cache and name:
            self._operator_cache[name] = op

        return op

    def _create_gemm(
        self,
        M: int,
        K: int,
        N: int,
        tile_m: int = 64,
        tile_k: int = 64,
        tile_n: int = 64,
        num_aie_columns: int = 8,
        partition_N: int = 1,
        use_static_weight: bool = False,
        b_col_maj: bool = True,
        c_col_maj: bool = False,
        dtype_in: str = "bf16",
        dtype_out: str = "bf16",
        **kwargs,
    ):
        """Create a GEMM operator"""
        from iron.operators import AIEGEMM

        return AIEGEMM(
            M=M,
            K=K,
            N=N,
            use_static_weight=use_static_weight,
            tile_m=tile_m,
            tile_k=tile_k,
            tile_n=tile_n,
            num_aie_columns=num_aie_columns,
            partition_N=partition_N,
            b_col_maj=b_col_maj,
            c_col_maj=c_col_maj,
            dtype_in=dtype_in,
            dtype_out=dtype_out,
            context=self.context,
            **kwargs,
        )

    def _create_gemv(
        self,
        M: int,
        K: int,
        tile_size_input: int = 4,
        tile_size_output: int = 32,
        num_aie_columns: int = 8,
        is_mv: bool = True,
        use_static_weight: bool = False,
        **kwargs,
    ):
        """Create a GEMV operator"""
        from iron.operators import AIEGEMV

        return AIEGEMV(
            M=M,
            K=K,
            is_mv=is_mv,
            use_static_weight=use_static_weight,
            num_aie_columns=num_aie_columns,
            tile_size_input=tile_size_input,
            tile_size_output=tile_size_output,
            context=self.context,
            **kwargs,
        )

    def _create_rms_norm(
        self,
        size: int,
        eps: float = 1e-6,
        num_aie_columns: int = 8,
        num_channels: int = 2,
        tile_size: int = 64,
        weighted: bool = True,
        **kwargs,
    ):
        """Create an RMSNorm operator"""
        from iron.operators import AIERMSNorm

        return AIERMSNorm(
            size=size,
            eps=eps,
            num_aie_columns=num_aie_columns,
            num_channels=num_channels,
            tile_size=tile_size,
            weighted=weighted,
            context=self.context,
            **kwargs,
        )

    def _create_layer_norm(
        self,
        size: int,
        eps: float = 1e-6,
        num_aie_columns: int = 8,
        num_channels: int = 2,
        tile_size: int = 64,
        **kwargs,
    ):
        """Create a LayerNorm operator"""
        from iron.operators import AIELayerNorm

        return AIELayerNorm(
            size=size,
            eps=eps,
            num_aie_columns=num_aie_columns,
            num_channels=num_channels,
            tile_size=tile_size,
            context=self.context,
            **kwargs,
        )

    def _create_mha(
        self,
        num_heads: int,
        seq_len: int,
        d: int,
        num_KV_heads: int,
        num_of_pipelines: int = 1,
        **kwargs,
    ):
        """Create a Multi-Head Attention operator"""
        from iron.operators import AIEMHA

        return AIEMHA(
            num_heads=num_heads,
            seq_len=seq_len,
            d=d,
            num_KV_heads=num_KV_heads,
            num_of_pipelines=num_of_pipelines,
            context=self.context,
            **kwargs,
        )

    def _create_rope(
        self,
        seq_len: int,
        head_dim: int,
        theta_base: float = 10000.0,
        num_aie_columns: int = 8,
        **kwargs,
    ):
        """Create a RoPE operator"""
        from iron.operators import AIERoPE

        return AIERoPE(
            seq_len=seq_len,
            head_dim=head_dim,
            theta_base=theta_base,
            num_aie_columns=num_aie_columns,
            context=self.context,
            **kwargs,
        )

    def _create_softmax(
        self,
        size: int,
        num_aie_columns: int = 8,
        **kwargs,
    ):
        """Create a Softmax operator"""
        from iron.operators import AIESoftmax

        return AIESoftmax(
            size=size,
            num_aie_columns=num_aie_columns,
            context=self.context,
            **kwargs,
        )

    def _create_silu(
        self,
        size: int,
        num_aie_columns: int = 8,
        **kwargs,
    ):
        """Create a SiLU operator"""
        from iron.operators import AIESiLU

        return AIESiLU(
            size=size,
            num_aie_columns=num_aie_columns,
            context=self.context,
            **kwargs,
        )

    def _create_swiglu(
        self,
        size: int,
        intermediate_size: int,
        num_aie_columns: int = 8,
        **kwargs,
    ):
        """Create a SwiGLU operator"""
        from iron.operators import AIESwiGLU

        return AIESwiGLU(
            size=size,
            intermediate_size=intermediate_size,
            num_aie_columns=num_aie_columns,
            context=self.context,
            **kwargs,
        )

    def _create_elementwise_add(
        self,
        size: int,
        num_aie_columns: int = 8,
        num_channels: int = 2,
        tile_size: int = 64,
        **kwargs,
    ):
        """Create an ElementwiseAdd operator"""
        from iron.operators import AIEElementwiseAdd

        return AIEElementwiseAdd(
            size=size,
            num_aie_columns=num_aie_columns,
            num_channels=num_channels,
            tile_size=tile_size,
            context=self.context,
            **kwargs,
        )

    def _create_elementwise_mul(
        self,
        size: int,
        num_aie_columns: int = 8,
        **kwargs,
    ):
        """Create an ElementwiseMul operator"""
        from iron.operators import AIEElementwiseMul

        return AIEElementwiseMul(
            size=size,
            num_aie_columns=num_aie_columns,
            context=self.context,
            **kwargs,
        )

    def get_cached_operator(self, name: str) -> Optional[Any]:
        """Get a cached operator by name"""
        return self._operator_cache.get(name)

    def clear_cache(self) -> None:
        """Clear the operator cache"""
        self._operator_cache.clear()

    def create_operator_config(
        self,
        operator_type: OperatorType,
        name: str,
        **kwargs,
    ) -> OperatorConfig:
        """
        Create an operator configuration (without instantiating).

        Useful for deferred operator creation.

        Args:
            operator_type: Type of operator
            name: Operator name
            **kwargs: Operator arguments

        Returns:
            OperatorConfig object
        """
        return OperatorConfig(
            operator_type=operator_type,
            name=name,
            kwargs=kwargs,
            enabled=True,
        )

    def create_from_config(
        self,
        config: OperatorConfig,
    ) -> Any:
        """
        Create an operator from a configuration object.

        Args:
            config: OperatorConfig object

        Returns:
            Configured NPU operator instance
        """
        return self.create_operator(
            operator_type=config.operator_type,
            name=config.name,
            cache=config.enabled,
            **config.kwargs,
        )


class OperatorBuilder:
    """
    Builder pattern for constructing complex operator configurations.

    Provides a fluent interface for chaining operator configuration.
    """

    def __init__(self, factory: OperatorFactory):
        """
        Initialize the builder.

        Args:
            factory: OperatorFactory instance
        """
        self.factory = factory
        self._configs: List[OperatorConfig] = []

    def add_gemm(
        self,
        name: str,
        M: int,
        K: int,
        N: int,
        enabled: bool = True,
        **kwargs,
    ) -> "OperatorBuilder":
        """Add a GEMM operator configuration"""
        self._configs.append(
            OperatorConfig(
                operator_type=OperatorType.GEMM,
                name=name,
                kwargs={"M": M, "K": K, "N": N, **kwargs},
                enabled=enabled,
            )
        )
        return self

    def add_rms_norm(
        self,
        name: str,
        size: int,
        enabled: bool = True,
        **kwargs,
    ) -> "OperatorBuilder":
        """Add an RMSNorm operator configuration"""
        self._configs.append(
            OperatorConfig(
                operator_type=OperatorType.RMS_NORM,
                name=name,
                kwargs={"size": size, **kwargs},
                enabled=enabled,
            )
        )
        return self

    def add_elementwise_add(
        self,
        name: str,
        size: int,
        enabled: bool = True,
        **kwargs,
    ) -> "OperatorBuilder":
        """Add an ElementwiseAdd operator configuration"""
        self._configs.append(
            OperatorConfig(
                operator_type=OperatorType.ELEMENTWISE_ADD,
                name=name,
                kwargs={"size": size, **kwargs},
                enabled=enabled,
            )
        )
        return self

    def build_all(self) -> Dict[str, Any]:
        """
        Build all configured operators.

        Returns:
            Dictionary mapping operator names to instances
        """
        operators = {}
        for config in self._configs:
            if config.enabled:
                operators[config.name] = self.factory.create_from_config(config)
        return operators

    def build_all_and_setup(self) -> Dict[str, Any]:
        """
        Build all operators and set up their artifacts.

        Returns:
            Dictionary mapping operator names to instances
        """
        operators = self.build_all()
        for name, op in operators.items():
            op.set_up_artifacts()
        return operators


def create_operator_factory(
    context: Optional[AIEContext] = None,
    num_aie_columns: int = 8,
    **kwargs,
) -> OperatorFactory:
    """
    Factory function to create an OperatorFactory.

    Args:
        context: AIE context
        num_aie_columns: Number of AIE columns
        **kwargs: Additional arguments

    Returns:
        OperatorFactory instance
    """
    return OperatorFactory(
        context=context,
        num_aie_columns=num_aie_columns,
        **kwargs,
    )
