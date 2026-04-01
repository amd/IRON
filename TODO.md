# IRON TODOs

## Implement multi-channel weighted RMS Norm

`iron/operators/rms_norm/design_weighted.py` does not accept a `num_channels`
parameter — the weight ObjectFifo is shared across all columns and does not support
per-channel weight routing. `num_channels` was removed from `my_weighted_rms_norm`'s
signature since it was silently ignored. A `ValueError` guard in `AIERMSNorm.__init__`
prevents passing `num_channels != 1` with `weighted=True`.

Implementing `num_channels > 1` for the weighted variant would allow `llama_npu.py`
to use `num_channels=2` for higher throughput. When implemented: add `num_channels`
back to `my_weighted_rms_norm`, pass it from `AIERMSNorm.get_mlir_artifact()`, and
lift the `ValueError` guard.

## Add unit test for GEMM partition_N > 1

`AIEGEMM.partition_B()` splits a large weight matrix into `partition_N` slices for
sequential kernel calls (used in llama's vocab projection with `vocab_partitions=4`).
The operator unit test only ever exercised `partition_N=1` (no partitioning) and the
parameter was removed from the test in this PR. A proper test should call
`partition_B(B, partition_N=4)`, run the operator 4 times into separate output
slices, concatenate, and compare against a single reference GEMM.

## Remove `AIEDeviceManager` in favor of mlir-aie runtime libraries

`iron/common/device_manager.py` provides three things that should be replaced by
upstream mlir-aie (`XRTHostRuntime`) equivalents:

1. **Context/kernel caching** (`get_context_and_kernel`) — the standard operator
   path already uses `aie_utils.DefaultNPURuntime` (i.e., `XRTHostRuntime`), which
   has its own internal caching. The fused ELF path (`iron/common/fusion.py`) still
   uses `AIEDeviceManager.device` (a raw `pyxrt.device`) to create
   `pyxrt.hw_context` directly. `fusion.py` should be refactored to go through
   `XRTHostRuntime` APIs instead of raw pyxrt.

2. **Device type detection** (`device_manager.device_type`) — used by every
   `op.py` to pass NPU1/NPU2 variant to the design function.
   `XRTHostRuntime().device()` already returns the same value; operators should
   obtain it from the runtime directly.

3. **Reset/teardown** (`reset()`) — called by the `aie_context` pytest fixture in
   `conftest.py`. mlir-aie has no equivalent hook today; one would need to be added
   upstream or worked around.

Once `fusion.py` goes through `XRTHostRuntime` and a teardown hook exists,
`device_manager.py` and all `context.device_manager.*` references across
`iron/operators/*/op.py` can be removed.
