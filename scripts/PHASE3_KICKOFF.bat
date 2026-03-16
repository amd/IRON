@echo off
REM =============================================================================
REM IRON Framework - Phase 3 Kickoff Script
REM =============================================================================
REM Purpose: Display Phase 3 tasks, show critical path, provide quick-start commands
REM Usage:   scripts\PHASE3_KICKOFF.bat
REM =============================================================================

setlocal EnableDelayedExpansion

echo.
echo ================================================================================
echo   IRON Framework - Phase 3 Implementation Kickoff
echo ================================================================================
echo.
echo Phase 1: COMPLETE (4 operators implemented)
echo Phase 2: BASELINE COMPLETE (validation framework ready)
echo Phase 3: IMPLEMENTATION PHASE (15 tasks)
echo.
echo Started: %DATE% %TIME%
echo ================================================================================
echo.

REM =============================================================================
REM ALL 15 PHASE 3 TASKS
REM =============================================================================
echo   ALL PHASE 3 TASKS
echo ================================================================================
echo.
echo  P3-00  | Project Setup & Infrastructure
echo         | Initialize Phase 3 project structure and build system
echo.
echo  P3-01  | KV Cache Operator                    [CRITICAL]
echo         | Implement Key-Value cache management for attention
echo.
echo  P3-02  | RoPE with Cache Integration          [CRITICAL]
echo         | Integrate RoPE with KV cache for efficient attention
echo.
echo  P3-03  | RMSNorm Optimized Kernel
echo         | Optimized RMSNorm with better memory access patterns
echo.
echo  P3-04  | SiLU Gate Fusion                     [CRITICAL]
echo         | Fused SiLU activation for MoE/MLP layers
echo.
echo  P3-05  | Softmax Stable Implementation
echo         | Numerically stable softmax with cache awareness
echo.
echo  P3-06  | Attention Score Computation          [CRITICAL]
echo         | Q @ K^T matrix multiplication kernel
echo.
echo  P3-07  | Attention Output Projection          [CRITICAL]
echo         | Attention weights @ V matrix multiplication
echo.
echo  P3-08  | Layer Fusion: RMSNorm + RoPE
echo         | Fuse consecutive operators for efficiency
echo.
echo  P3-09  | Layer Fusion: SiLU + Linear
echo         | Fused activation + projection
echo.
echo  P3-10  | Memory Pool Manager                  [CRITICAL]
echo         | Unified memory allocation for NPU
echo.
echo  P3-11  | Command Queue Manager
echo         | NPU command submission and synchronization
echo.
echo  P3-12  | Multi-Head Attention Orchestration
echo         | Coordinate all attention components
echo.
echo  P3-13  | Full Decoder Layer Integration       [CRITICAL]
echo         | End-to-end decoder layer pipeline
echo.
echo  P3-14  | Integration Testing & Validation
echo         | System-level testing and benchmarking
echo.
echo  P3-15  | Documentation & Handoff
echo         | Final documentation and QA handoff
echo.

REM =============================================================================
REM CRITICAL PATH (7 Tasks)
REM =============================================================================
echo.
echo ================================================================================
echo   CRITICAL PATH (7 Tasks - Must Complete in Order)
echo ================================================================================
echo.
echo  1. P3-01  | KV Cache Operator
echo           | Foundation for all attention mechanisms
echo           |
echo           v
echo  2. P3-02  | RoPE with Cache Integration
echo           | Positional embedding with cache awareness
echo           |
echo           v
echo  3. P3-06  | Attention Score Computation
echo           | Q @ K^T - core attention calculation
echo           |
echo           v
echo  4. P3-07  | Attention Output Projection
echo           | Attention @ V - produce context vectors
echo           |
echo           v
echo  5. P3-10  | Memory Pool Manager
echo           | Unified memory management for NPU
echo           |
echo           v
echo  6. P3-12  | Multi-Head Attention Orchestration
echo           | Coordinate all attention heads
echo           |
echo           v
echo  7. P3-13  | Full Decoder Layer Integration
echo           | Complete decoder layer pipeline
echo.
echo ================================================================================

REM =============================================================================
REM QUICK START COMMANDS
REM =============================================================================
echo.
echo   QUICK START - Begin Task P3-01 (KV Cache)
echo ================================================================================
echo.
echo  To start working on KV Cache operator, run these commands:
echo.
echo  1. Create task directory:
echo     mkdir iron\src\kv_cache
echo     mkdir iron\test\kv_cache
echo.
echo  2. Create source files:
echo     type nul > iron\src\kv_cache\kv_cache.h
echo     type nul > iron\src\kv_cache\kv_cache.cpp
echo     type nul > iron\src\kv_cache\kv_cache_kernel.cpp
echo.
echo  3. Create test file:
echo     type nul > iron\test\kv_cache\test_kv_cache.cpp
echo.
echo  4. Open VS Code in project:
echo     code .
echo.
echo ================================================================================
echo.
echo   AVAILABLE COMMANDS
echo ================================================================================
echo.
echo  Run validation suite:
echo    python -m iron.benchmarks.validate --generate-charts
echo.
echo  Run specific operator benchmark:
echo    python -m iron.benchmarks.validate --operator rope
echo.
echo  Collect benchmarks with multiple runs:
echo    python scripts\collect_benchmarks.py --runs 5
echo.
echo  Analyze results and generate charts:
echo    python scripts\analyze_results.py --charts all --report full
echo.
echo  Compare against baseline:
echo    python -m iron.benchmarks.verify compare --current results.json --baseline baseline.json
echo.
echo  Verify against targets:
echo    python -m iron.benchmarks.verify verify-targets results.json
echo.
echo ================================================================================
echo.
echo   TASK TRACKING
echo ================================================================================
echo.
echo  Update task status in your project tracker:
echo    - P3-01 [IN PROGRESS] - KV Cache Operator
echo    - All other tasks [PENDING]
echo.
echo  Recommended sprint order:
echo    Sprint 1: P3-01, P3-02, P3-03, P3-04
echo    Sprint 2: P3-05, P3-06, P3-07
echo    Sprint 3: P3-08, P3-09, P3-10
echo    Sprint 4: P3-11, P3-12, P3-13
echo    Sprint 5: P3-14, P3-15
echo.
echo ================================================================================
echo   PHASE 3 KICKOFF COMPLETE
echo ================================================================================
echo.
echo  Ready to begin implementation. Good luck!
echo.
echo  Completed: %DATE% %TIME%
echo ================================================================================
echo.

endlocal
exit /b 0
