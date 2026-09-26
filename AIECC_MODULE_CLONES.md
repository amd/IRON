# aiecc clones the whole module per split item

A note to act on later, in mlir-aie's `tools/aiecc`. Found while building
the Llama 3.2 1B prefill graph as one fused full-ELF image; the same
mechanism bounds every fused build.

## Symptom

The sixteen-layer prefill image (291 steps, 17 designs, 218 cores, one
runtime sequence per design plus the main one) does not build in a 16 GB
container: aiecc reaches 11 GB at the per-sequence split stage
(`(36/47) npu_seq_{0}.mlir`) and is killed. Four layers peak at 5.6 GB. A
one-layer build, sampled per stage in aiecc's own process:

| stage | resident memory |
|---|---|
| input through the control-packet stages (0–11) | 0.1 GB |
| per-core split, `perCore_{0}.mlir` (12) | 2.0 GB |
| per-core compile and link (16–26), peak | 5.2 GB |
| per-sequence split, `npu_seq_{0}.mlir` (36) | 3.3 GB |
| end (47) | 3.6 GB |

The fused module's text is 1.4 MB at sixteen layers. The main runtime
sequence, once materialized (every `aiex.run` inlined) and DMA-lowered,
holds 28,381 DMA tasks (MHA 768 per call, the down projection 320, the
other projections 128, against a whole decode layer's 430).

## Cause

`SplitIRAction` (`tools/aiecc/Actions.h`) walks a module for the key op
and **clones the entire module once per match**; each item is an
`OpInModule{module clone, op}` and the graph keeps every item:

```cpp
// SplitIRAction — walks a ModuleOp for KeyOp instances; clones the module
// once per match. Use `.filter` downstream to skip matches.
for (auto &match : matches) {
  mlir::OwningOpRef<mlir::ModuleOp> clone = srcModule.clone();
  ...
}
```

The call sites, all in `tools/aiecc/aiecc.cpp`:

| split | key op | source module | clones | what the consumer reads |
|---|---|---|---|---|
| `allCores` (`perCore_{0}.mlir`) | `CoreOp` | `physical` | one per core (218) | that core, its device's tiles, buffers, locks and object fifos, the kernels it links |
| `physicalPerDevice` (`perDeviceCompile_{0}.mlir`) | `DeviceOp` | `physical` | one per device (17) | that device |
| `staticPerDevice` (`perDevice_{0}.mlir`) | `DeviceOp` | `npuLowered` under `--expand-load-pdis` | one per device (17) | that device: CDO, PDI |
| `npuLoweredPerDevice` (`perDeviceNPULowered_{0}.mlir`) | `DeviceOp` | `npuLowered` | one per device (17) | that device: the transaction sequence |
| `perSeq` (`npu_seq_{0}.mlir`) | `RuntimeSequenceOp` | `npuLowered` | one per sequence (17) | that sequence and the device it sits in; `buildNpuProgramSubgraph` translates it to the instruction binary |

So memory is (clones) × (module size) at each split, and the module size
after `npu_lowered.mlir` is dominated by the materialized main sequence.
The per-core split multiplies the pre-lowering module 218 times (the 2 GB
step), and the three splits over `npuLowered` multiply the lowered module
51 times. The comment at `perSeq` says why the full module is kept:
"SplitIRAction preserves the complete module for symbol resolution."

## Fix

A draft of this is on mlir-aie's `claude/mlir-aie-iron-upstream` branch
(`pruneSplitClone` in `tools/aiecc/Actions.h`), unbuilt here; the validation
below is what to run once it builds.

Prune each clone to what its consumer reads, keeping symbol resolution
working. Concretely, give `SplitIRAction` an optional prune callback run
on the clone after the matched op is found, and pass one at each call
site:

- **`perSeq`**: erase every other `RuntimeSequenceOp` in the clone. The
  sequences are independent programs; after materialization the main
  sequence no longer calls the designs' sequences (`aiex.run` has been
  inlined), and a design's sequence references only its own device. Each
  of the 16 design-sequence clones then drops the main sequence, and the
  main sequence's clone drops nothing that matters: 17× becomes about 1×.
- **`npuLoweredPerDevice`**, **`staticPerDevice`**: erase the runtime
  sequences of every other device (the transaction, CDO and PDI of a
  device read that device's static configuration, not another device's
  sequence). The main device's expanded sequence is the bulk, so the 16
  design clones shrink to their own device.
- **`allCores`**: erase every runtime sequence, and every other device.
  Core compilation reads the core, its device and the kernels it links,
  never a runtime sequence. This turns the 2 GB base into kilobytes per
  core, and removes the same multiplier from the per-core compile stages.

Erasing an op whose symbol is still referenced would break verification,
so the prune must leave the referenced symbols in place: `aie.device`
symbols referenced by `aiex.configure` / `load_pdi` ops in a kept
sequence, and `func.func` declarations a kept core calls. The safe rule
is to erase runtime sequences and whole devices only, and only when
nothing kept references their symbols (`SymbolTable::symbolKnownUseEmpty`
on the clone after the intended erasures, or erase and run the verifier
in a debug build).

A lighter alternative that also helps: do not retain the source module
of a split once its items exist, and let a consumer release its item once
mapped. The graph keeps every edge's items for the whole run today
(`this->out.items` in `Graph.h`), so the module and all its clones are
live together.

## Validating

1. Build mlir-aie with the change (this needs the LLVM/MLIR build; the
   pip wheel cannot be rebuilt in place).
2. Regenerate the one-layer real-size prefill module from IRON:
   `iron/tests/toolchain/full_elf.py::test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer`
   builds it and leaves `aie.mlir` and the kernel objects in the test's
   `build/prefill_1b_shared.prj`. Then run aiecc on it directly with the
   full-ELF flags (`--peano=<dir> --get-full-elf --full-elf-name=out.elf
   --expand-load-pdis --get-scratchpad-parameters`) and sample its
   resident memory per stage (the stage names are on stdout, separated by
   carriage returns; `tr '\r' '\n'`). The table above is the baseline.
3. The sixteen-layer image is the target: `Llama1B` in
   `iron/tests/common/llama_model.py` at its full depth, through
   `LlamaGraph(cfg, cfg.context_length).trace(cfg, cfg.context_length)`
   and `traced.sequence(...).compile()`. It should build in a few GB, and
   its ELF should be byte-identical to one built without the prune (the
   prune changes what is held, not what is emitted).
4. mlir-aie's own aiecc tests cover the split filters (`--device-name`,
   `--sequence-name`); they must still pass, since filtering happens
   after the split and reads the pruned clones.

## Expected

The per-core split falls from 2 GB to near zero for this module, the
per-core compile peak follows, and the per-sequence split stops scaling
with the number of designs. The sixteen-layer prefill image then costs
about what one lowered module costs, on the order of a gigabyte.
