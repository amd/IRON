# Chess port state (2026-09-07) — strixhalo
Goal: compile IRON aie_kernels with compiler="chess" (task-1: axpy).

## Installed chess toolchains
- Vitis 2025.2: /home/bcloud/Xilinx2025/2025.2/Vitis/aietools (NEW, 75GB, minimal config)
  - arch for AIE2P-class = **aie2ps** (no aie2p). Symlink alias added:
    data/aie2p -> aie2ps ; tps/lnx64/target_aie2p -> target_aie2ps
- Vitis 2026.1: /home/bcloud/Xilinx/2026.1/Vitis/aietools (has aie2p + aie2ps; model renamed acquire to *guarded*)
- Ryzen AI essentials 1.3.0 (2024): ~/Downloads/ryzen_ai-1.3.0/vitis_aie_essentials (arch aie2p, UNGUARDED void_acquire)

## mlir-aie arch/intrinsic model matrix
| aietools | aie2p? | aie2ps? | acquire name |
|---|---|---|---|
| essentials 2024 | yes | no | void_acquire____uint___uint (unguarded) |
| Vitis 2025.2 | no | yes | void_acquire_guarded___uint___uint |
| Vitis 2026.1 | yes | yes | void_acquire_guarded___uint___uint |

## Wheel wrapper .ll is built by CI against the 2024 essentials (unguarded)
=> mismatch with 2025.2/2026.1 chess front-ends ("unrecognised intrinsic ... model inconsistency").
FIX (done): regenerate aie_runtime_lib/<ARCH>/chess_intrinsic_wrapper.ll against the TARGET aietools:
  xchesscc_wrapper AIE2P -aietools <AIETOOLS_ROOT> -c <mlir-aie>/aie_runtime_lib/AIE2P/chess_intrinsic_wrapper.cpp -d -f +f -o wrapper.ll
  (use the ~/mlir-aie/install wrapper for aie2ps mapping, or the pip wrapper for aie2p)
  backup originals as .ll.bak-2024 / .ll.bak-2026 in site-packages/mlir_aie/aie_runtime_lib/{AIE2,AIE2P}/
CURRENT venv state: AIE2P wrapper = regenerated vs 2025.2 via aie2p mapping (guarded, no target triple).
  AIE2 wrapper = 2026.1 regen (guarded). To use essentials (2024): restore .ll.bak-2024 files.

## pip wrapper arch mapping patched then reverted
- ~/iron/lib/python3.14/site-packages/mlir_aie/bin/xchesscc_wrapper: AIE2P -> aie2p (orig, restored; backup: xchesscc_wrapper.bak-aie2p)
- the compiled aiecc (wheel) hardcodes tps target dir "target_aie2p" => needs the aie2p-name symlinks on 2025.2.

## IRON aiecc hook added (env-guarded, safe)
- iron/common/compilation/base.py: if env AIE_AIECC_NO_XBRIDGE set, append --no-xbridge to aiecc args.
  backup: base.py.bak-noXbridge

## REMAINING BLOCKER (chess link, not kernel)
axpy compiles through the chess front-end fine on ALL THREE aietools (kernel C++ OK after the earlier
bf16 cast fixes). Every aiecc ELF link attempt segfaults in the chess me-link/noodle stage:
- 2025.2/2026.1: "Warning: inconsistent Elf processor header machine flags: 3/4" then segmentation
  violation at aiecc edge elfs_{0}.elf (prebuilt me libs = model 3, LLVM-frontend objects = model 4).
- essentials 2024 (xbridge mode per KB): got past elfs, bridge tool segfaults at EV conversion.
=> Chess object/model generation via mlir-aie 1.4.2.dev16 aiecc is not linkable on any installed aietools.
Candidate next steps:
  A) official upstream mlir_aie v1.4.2 wheel (not .dev16 fork) in a scratch venv - aiecc chess flow is
     AMD-CI-tested against Vitis 2025.1 (buildAndTestVitis.yml); try its chess link.
  B) npueval-known-good pairing: mlir_aie 0.0.1.20250519+c105c0b + llvm_aie 19.0.0.20250415+b2a279c1
     + python 3.12 + May-2025 IRON + 2024 essentials (AMD npueval Dockerfile recipe).
  C) chess-link debugging: model-4 me libs rebuild or EV/bridge flag workarounds.
Test cmd: source env (AIETOOLS_ROOT/PATH/XILINXD_LICENSE_FILE) + cd ~/iron +
  ~/iron/bin/python -m pytest iron/operators/axpy/test.py --compiler chess -m "not extensive" -q

## Update 2 (same day) — options A + B tested (conclusive)
- A) Official upstream mlir_aie v1.4.2 wheel (scratch venv ~/chessA, py3.14): SAME elfs-link crash as
  the fork on every aietools. mlir-aie version is NOT the variable.
- B) npueval pairing (~/chessB, py3.12 + mlir_aie 0.0.1.2025051904+c105c0b + llvm_aie
  19.0.0.2025041501+b2a279c1 + mlir-aie@c105c0b source): the c105c0b-era aiecc.py has NO chess/xbridge
  flags at all -> npueval is a PEANO-only stack. The KB claim "npueval pins the known-good CHESS
  pairing" was WRONG. AIE2P chess ELF linking does not exist in mlir-aie <= May-2025.
- Verdict: no released mlir-aie + aietools combo produces an AIE2P chess ELF. The 2026 unified/sfg
  chess link crashes on 2024 essentials (bridge EV segfault) and 2025.2/2026.1 (me libs model-3 vs
  LLVM objects model-4 -> "inconsistent Elf machine flags 3/4"). mlir-aie CI never exercises the full
  chess ELF link (compile-only, aie2/aie_ml, Vitis 2025.1).
- Scratch venvs left in place: ~/chessA (official 1.4.2), ~/chessB (npueval pairing).
- Remaining paths: C) chess me-link deep-fix (tct/model alignment, lib rebuild); D) newer aietools
  (Vitis 2026.2+/ryzen_ai 2.x) era-matched to the 2026 mlir-aie chess flow; E) upstream bug report.

## Update 3 (same day) — option C: chess ELF-link FIXED (stale-object root cause)
- ROOT CAUSE of the "inconsistent Elf machine flags 3/4" crash: STALE kernel .o files in ~/iron/build
  (compiled 2026-09-02, ELF flags 0x3) were reused by the aiecc chess link against fresh
  flags-0x4 objects/libs from Vitis 2025.2. Deleting the stale kernel objects forces xchesscc to
  recompile -> the FULL chess pipeline now works: front-end -> me-link -> EV/ELF -> xclbin on
  Vitis 2025.2 (~/Xilinx2025/2025.2/Vitis/aietools + aie2ps alias symlinks).
- Chess-built kernels now LOAD and EXECUTE on npu2_40 but return ERT_CMD_STATE_TIMEOUT
  (fresh-compile silu under chess = timeout; peano silu = PASS). The earlier "silu chess 20 passed
  in 5s" was an artifact-cache false positive (peano binaries reused) - invalid.
- axpy test times out under PEANO too (flm down, silu/mul/add all pass) -> separate axpy
  design/kernel issue (suspect: float scalar core-arg or the saxpy vector kernel on npu2_40).
- flm-35b.service was stopped/restarted during NPU-isolation testing (back UP).
- TODO next: (a) chess-core completion semantics (me-runtime main vs peano bare-metal aie.end);
  (b) axpy-under-peano hang root-cause (blocks the task-1 axpy contract regardless of chess).
## Update 4 (same day) — chess-core runtime hang root-caused (option a)
- Peano core ELF (PASSES): minimal crt (__start 32B) -> main; objectFifo acquire = inline raw
  "acq #0x33/#0x30" machine instructions; buffers at 0x78000/0x7c000/0x70400/0x74000.
- Chess core ELF (TIMES OUT): me-runtime style (12KB; me_defs/me_basic + _main_init prelude with
  ctor/init-array iteration at 0x40-0xbc BEFORE main; libme linked). acquire via function
  llvm___aie2p___acquire -> acq r0,r1 with the SAME lock ids (0x33/0x30) and same buffers.
- => The kernel logic is equivalent; the hang is the chess me-runtime _main_init prelude (or its
  main-return/fini path), which expects the aiecompiler/EV boot environment - NOT the raw xrt
  core-ELF boot that IRON pytest xrt harness provides (peano cores boot bare).
- Both chess link modes (xbridge / no-xbridge) hang identically.
- ALSO found (harness bug): kernel .o cache + artifact names (SiLU_*.bin/.xclbin/.mlir.d) are SHARED
  between peano and chess runs - switching --compiler reuses the other compiler artifacts
  (stale flags-0x3 objects caused the earlier link crash; stale builds cause false pass/fail).
  A proper task-1 harness must segregate compiler artifacts.
- Fix direction: make the chess link produce bare cores (peano-style __start, no me runtime init),
  OR run chess-built kernels through the aiecompiler/EV boot path instead of the raw xrt elf boot.
## Update 5 (same day) — bare-chess-core work (option 1), state + next step
- Goal of option 1: chess cores linked bare (peano-style __start -> main -> done, no me runtime).
- Discovered: TWO aiecc binaries, both incomplete:
  * pip wheel aiecc (mlir_aie 1.4.2.dev16+g7e00b57 in ~/iron venv): has modern flags
    (--get-xclbin/--get-npu-insts/--get-input-with-addresses, --unified/--xchesscc/--xbridge)
    but NO --no-xbridge flag.
  * local fork build (~/mlir-aie/install/bin/aiecc, Jul-12): HAS --no-xbridge/--no-xchesscc
    (and the peano-clang bare-link path with generated ld.script) but LACKS the modern --get-* flags.
- IRON xclbin/insts compile path needs BOTH -> neither binary works standalone with --no-xbridge.
- next step: rebuild aiecc from ~/mlir-aie current source (1e6b70af0, has xbridge/no-xbridge AND
  modern flags) against its LLVM, then swap into the venv (backup exists: bin/aiecc.pip-backup),
  run chess with AIE_AIECC_NO_XBRIDGE=1 -> should produce bare peano-lld-linked chess cores
  (no _main_init/me_defs) -> test silu/axpy runtime.
- base.py now has the env hook (AIE_AIECC_NO_XBRIDGE) at BOTH aiecc option sites (FullElf + xclbin/insts).
- REMINDER: kernel .o + design artifacts (SiLU_*.bin/.xclbin/.mlir.d) are SHARED between peano and
  chess -> always delete build/<design>* + kernel .o before cross-compiler runs (false pass/fail).
## Update 6 — aiecc rebuild investigation (option 1), blockers found
- CONFIRMED: chess vs peano .bin (TXN/control) = BYTE-IDENTICAL for the same silu design (300 B).
  Only the CORE ELF differs -> the hang is 100% the chess me-runtime core under the xrt boot.
  Bare chess cores (option 1) = the correct fix direction.
- aiecc sources: no single checkout has both feature sets:
  * upstream Xilinx/mlir-aie main (c80b88c39, ~/mlir-aie-main): modern flags
    (--get-xclbin/--get-npu-insts, in CommandLineOptions.h) + RESTRUCTURED aiecc (map/ShellCommand
    style). NO no-xbridge.
  * local npu2-40 fork (~/mlir-aie @1e6b70af0): OLDER aiecc (no modern flags) + xbridge AND
    --no-xbridge with the peano-clang/lld + ld.script bare-link (PR #3031 lineage) + WIP
    BdLowering.cpp (CMakeLists broken - not registered). Divergence vs upstream = 1782 files.
  * pip wheel aiecc (in ~/iron venv): modern flags + xbridge, no no-xbridge.
- Configuring the local fork against my_install MLIR (mlir-23.0.0.2026071405+46fcb339 = matches
  clone-llvm.sh pin) fails only on the BdLowering.cpp CMakeLists omission (fix = 1 line).
- Paths: (A) port the fork no-xbridge/peano-clang-link into upstream main aiecc (restructured ->
  sizeable); (B) port the modern --get-* flags back onto the local fork aiecc (older structure,
  smaller delta if the fork base is close to the flags introduction); (C) dig into why the chess
  me-runtime hangs under xrt boot (run core in aietools ISS/sim to separate codegen vs boot).
## Update 7 — option A executed: bare chess-core link reached, one wall left
- No port needed: upstream + the pip aiecc BOTH default the chess core ELF link to the bare
  peano-lld path ("--xbridge ... instead of the default Peano lld"); --xbridge (forced by the
  dev16 python) selects the me-link. --xchesscc IMPLIES --xbridge unless xbridge explicitly stated,
  so passing --xbridge=false (env hook AIE_AIECC_NO_XBRIDGE in mlir_aie utils.py) selects the bare
  peanoElfs link.
- Built upstream-main aiecc (c80b88c39, 451 ninja targets, ~10 min) against mlir wheel
  24.0.0.2026080106+56bcc187 (build_u24/bin/aiecc) — but upstream main REMOVED aie.objectfifosubview
  (dialect restructure) so it cannot parse the dev16-era design MLIR. Not usable with the current
  IRON/python stack.
- Back on the pip aiecc + --xbridge=false: the bare link RUNS (needs peano clang on PATH =
  llvm-aie wheel bin/clang) but ld.lld rejects the CHESS me-product metadata sections in the chess
  .o: .tctmemtab, .rtstab, .eoltab, .chesstypeannotationtab ("is being placed in X" with
  --orphan-handling=error in the generated ld script).
- Wall: bare-linking a me-product chess .o needs those sections dropped or placed. Peano cores have
  no such sections; the xrt bare boot should not need them -> stripping them pre-link is the
  surgical fix (objcopy --remove-section in the peanoElfs step, or ld-script INSERT).
- Next: fetch the dev16-era source (g7e00b57, 16 commits past v1.4.2 = the pip wheel commit) ->
  its llvm pin likely = 46fcb339 = my_install mlir (23.0.0.2026071405+46fcb339) -> build its aiecc
  against my_install -> patch peanoElfs to strip chess sections -> bare chess cores on the pip-era
  stack.
- Default state verified restored: peano silu = pass; chess xbridge = compile+load+timeout.
## Update 8 — bare chess core: built, linked, but STILL hangs at runtime
- Built v1.4.2-source aiecc (~/mlir-aie-v142, worktree of the tag) against mlir wheel
  24.0.0.2026080106+56bcc187 (same pin as v1.4.2). Configure failed until bootgen submodule init.
- v1.4.2 aiecc has the same peanoElfs (bare, default) / chessElfs (xbridge) split. Bare link of
  me-product chess .o failed on (a) chess metadata sections (.tctmemtab/.rtstab/.eoltab/
  .chesstypeannotationtab) -> patched --orphan-handling=error->warn; then (b) undefined
  me_primitive::control_rnd/control_sat -> wrote asm no-op stubs (exact GCC-style mangling
  _ZN12me_primitive11control_rndE, ret lr) linked via a peanoElfs patch (literal .arg path,
  NOT .input - the DSL input binding is strict).
- RESULT: BARE chess core produced (5444 B vs 12048 me-runtime; has __start, no me_defs/_main_init)
  -> but the silu test STILL returns ERT_CMD_STATE_TIMEOUT at runtime.
- => The me-runtime prelude was NOT the (only) hang cause: chess-compiled code hangs under the bare
  xrt boot too. (Peano-compiled same design passes.) Remaining suspects: chess me-product codegen
  needs runtime state the bare boot does not provide, or the chess code itself (VLIW bundles
  llvm-objdump cannot decode - decode with the aietools disassembler to compare main loops).
- NOTE: axpy ALSO times out under peano (design issue separate from chess).
- RESTORED default: dev16 pip aiecc in place; default chess (xbridge) = compile+load+timeout;
  peano = pass. Patched aiecc kept at ~/mlir-aie-v142/build_v142/bin/aiecc (switchable + needs
  AIE_AIECC_NO_XBRIDGE=1 + llvm-aie bin on PATH).
## Update 9 — chess-codegen runtime push: results + narrowed hypotheses
- Compared working peano core (1956 B) vs bare chess core (5444 B) side by side:
  * Both: __start -> main; main = infinite server loop (scf.for to 2^63-1) with inline acquires.
  * ERT completes via the shim-DMA drain after the core processes ONE tile (core never exits).
  * PEANO main: inline `acq #51/-1`, `acq #48/-1` -> compute -> `rel #50/1`, `rel #49/1`.
  * CHESS main: calls llvm___aie2p___acquire/release wrappers with the SAME (51/-1, 48/-1, 50/1, 49/1);
    wrapper machine code = plain `acq r0,r1`.
- Tested + eliminated: me-runtime vs bare core (both hang); chess wrapper fences +
  chess_separator_scheduler calls around acq (removed -> still hangs).
- => chess-compiled code is structurally identical to peano yet never completes tile 1 on real
  silicon (or never starts). Remaining hypotheses:
  A) core ELF/xclbin boot path: the bare chess ELF carries extra LOPROC sections
     (.tctmemtab/.rtstab/.eoltab/.chesstypeannotationtab) + me_stub; packaging/boot of chess ELFs
     via the IRON xrt path may differ from peano ELFs (chess ELFs are normally booted via the
     aiecompiler/EV flow, not the raw xrt core-ELF boot).
  B) chess codegen hits something the real npu2_40 silicon does not execute correctly (VLIW
     bundles undecodable by llvm-objdump - need the aietools ISS/disassembler).
- Decisive next step: run the chess-built design in the mlir-aie simulator (noodle/x86sim) instead
  of the real NPU: sim-pass + silicon-timeout => boot/loader issue (hypothesis A);
  sim-hang => codegen bug (hypothesis B).
- Default state restored+verified: peano silu PASS; chess (xbridge) = compile+load+timeout.
  Artifacts kept: /tmp/peano_core.elf (1956 B, working) + /tmp/chessbare_core.elf (5444 B, hangs)
  for further comparison. Patched bare aiecc at ~/mlir-aie-v142/build_v142/bin/aiecc.
## Update 10 — sim verification attempted; blocked by the same version matrix. Session conclusion.
- Sim route: mlir-aie's noodle = absent in v1.4.2 (no target). The fork aiecc (~/mlir-aie/install,
  Jul-12) has --aiesim + objectfifosubview BUT its parser rejects the dev16-era design MLIR
  (line 32 syntax drift) -> no coherent stack = (dialect-era aiecc) + (aiesim). aiecc_aiesim.cpp
  in v1.4.2 = vestigial (not in CMake, not built).
- FINAL STATE (after the whole chess-port campaign):
  1. Chess toolchain pipeline WORKS: kernels compile + link + produce ELFs on Vitis 2025.2
     (wrapper regen vs target aietools; aie2p<->aie2ps alias; stale-object fix; bare-core link
     with me stubs). This was the original hard blocker and is DELIVERED.
  2. Chess-built cores LOAD + EXECUTE on npu2_40 but every ERT command TIMES OUT under all core
     styles tried (me-runtime / bare / fence-free). Peano cores (identical design + identical
     txn/.bin) complete. Chess code = structurally identical (same locks 51/48, values -1/1,
     plain acq after fence removal).
  3. => chess me-codegen or chess-ELF boot is incompatible with the raw-xrt core-ELF boot that
     IRON's pytest harness uses, on real silicon. Needs either the chess ISS (fork-era coherent
     stack), the aiecompiler/EV boot path, or AMD/upstream input.
  4. SEPARATE: the axpy design times out under PEANO too (silu/mul/add pass) - an axpy design bug
     that blocks the task-1 contract regardless of chess.
  5. Harness bugs found: kernel .o + design artifacts shared across compilers (cache poisoning).
- Recommend: upstream engagement with this evidence (mlir-aie issue: chess AIE2P cores time out
  under raw xrt boot; repro = IRON silu test) + the axpy-under-peano design bug as an independent
  thread. All artifacts/notes in ~/iron/CHESS_PORT_STATE.md (updates 1-10).
## Update 11 — upstream issue filed
- Filed: https://github.com/Xilinx/mlir-aie/issues/3690 (bug label, account bong-water-water-bong)
  "Chess (xchesscc) AIE2P cores time out under raw xrt boot while Peano cores complete (NPU2)".
- Full repro + evidence (byte-identical txn, 3 core-ELF comparisons, fence-free test, decode gap,
  aiesim suggestion referencing #3479). Offer to test fixes.
- Remaining threads: (a) maintainer response / candidate fixes on #3690; (b) axpy-under-peano
  design hang (separate, gates the task-1 axpy contract regardless of chess).
## Update 12 — research findings + decisive mixed-core experiment
- ONLINE/archival research (pi ZFS backup of the prior 3-day NPU campaign + project docs):
  * The prior campaign hit the SAME chess-core-execution wall: "chess codegen is algorithmically
    right but zeros at runtime - a chess-core/kernel runtime-execution defect (control flow, ABI,
    or NPU hardware-compat)" (KB, ~Aug 27). Filed #1908-#1913 upstream; #1878/#1912 = chess
    memref arg-delivery defect (escalated upstream). Custom ps.so aiesim harness built
    (engine/npu/tests/aiesim/txn_replay_main.cpp, branch experiment/compiler-ab) - "core PC stayed
    0" for their chess add-1 in the sim. Catalogue of chesscc aie2p codegen bugs: ret-first leaf
    functions, arg delivery, pointer-arith, soft-float, pipeliner (worked around in-tree).
  * aiesim-debugging.md = the full recipe (sim launcher fixes: aie2psimmsm symlink, device JSON
    XC2VE3858, libstdc++ LD_PRELOAD; ps.so build; TXN-replay harness).
- NEW DECISIVE EXPERIMENT (today): MIXED core = chess-compiled core main + PEANO-compiled silu
  kernel (bare lld link accepts both) -> STILL ERT_CMD_STATE_TIMEOUT. => the hang is in the
  chess-compiled CORE MAIN (startup/acquire-loop), NOT the chess kernel code.
- control_rnd/control_sat: chess me-codegen READS these as DATA (LDA.s8 [sym] -> crRnd rounding
  mode); tested function-stub (byte 0x30) vs data-stub (byte 0) - both still hang; crRnd not the
  (sole) cause.
- Post the mixed-core result + prior-project evidence to Xilinx/mlir-aie#3690
  (comment 5576036282), asking for an ISS trace of the chess core main.
## Update 13 — axpy-under-peano "hang" = FALSE ALARM (artifact cache poisoning)
- Clean-run verification: fresh peano axpy (2048/col1) PASSES; full not-extensive axpy suite =
  20/20 PASS; elementwise_add 20/20 PASS. The earlier axpy ERT timeouts under peano were caused by
  the shared-artifact cache (stale / cross-compiler kernel .o + design artifacts being reused) and/or
  NPU contention (zaya job), NOT an axpy design bug.
- => Remaining task-1 gap = ONLY the chess-core runtime hang (chess-compiled core main never
  completes on the NPU under the xrt boot): upstream Xilinx/mlir-aie#3690 (mixed-core evidence +
  prior-campaign docs posted; awaiting maintainer ISS trace).
- Task-1 actual status: harness (chess_env PATH/license/compiler=chess) = working; axpy COMPILES
  under chess (full pipeline incl. bare/me link) = working; axpy reference test = passes under
  peano; the only unmet clause = "passes its reference test UNDER CHESS" (device execution), gated
  on #3690.
- Harness defect to fix (real): kernel .o + design artifacts (.bin/.xclbin/.mlir.d) are shared
  between --compiler peano and chess -> must segregate per compiler (or invalidate on switch) to
  avoid silent cross-contamination.
## Update 14 — "missing userspace" hypothesis CONFIRMED (how FLM/Loom run chess kernels)
- FLM/Loom DO run chess-built kernels on this NPU2: /opt/fastflowlm/share/flm/xclbins/<model>/*.xclbin
  (mm/layer/dequant/attn/lm_head per model, e.g. Qwen3.6-35B-A3B-NPU2). Container = xclbin2 +
  AIE_PARTITION + PDI - THE SAME format mlir-aie/aiecc produces (verified via xclbinutil on both).
- FLM runtime pattern (reverse-engineering doc): xrt::xclbin -> device.register_xclbin ->
  hw_context -> kernel -> run with set_arg + an NPU-instruction buffer; xrt::bo::sync for data.
  mlir-aie's xrtruntime (hostruntime.py) does the SAME sequence (pyxrt.xclbin -> register_xclbin ->
  hw_context) with two exec paths: insts (kernel(3, insts_bo,...)) and full-elf (hw_context(elf)).
  Our pytest runs use the INSTS path.
- mlir-aie ALSO ships an HRX runtime backend (NPU_RUNTIME=hrx -> CachedHRXRuntime): dispatches the
  SAME xclbin+insts through libhrx (the FLM-family amdxdna userspace; "control_code_from_elf",
  producer-independent DDR-patch ABI, no firmware 5-arg cutoff). This is the intended bridge for
  kernels that need the FLM-style userspace.
- BLOCKER on that path: the local libhrx builds (hrx-ws/install[-new], hrx-rocm, hrx-gfx1151) are
  all too old - missing hrx_buffer_map_with_mode (the symbol the mlir_aie hrxruntime binds; present
  in mlir-aie runtime_lib/test_lib/hrx_test_wrapper.h but in NO local libhrx.so/source). Need a
  fresh jtuyls/hrx (flm-hrx-amdxdna pin or newer) build.
- => The user's "missing userspace" hypothesis = right: chess cores run under the FLM/Loom-style
  userspace (libhrx / xrt-module boot), not the mlir-aie insts path. Next step = build libhrx with
  hrx_buffer_map_with_mode, then NPU_RUNTIME=hrx on the chess-built silu.
## Update 15 — "missing userspace" hypothesis TESTED and ELIMINATED; chess core content = the issue
- Obtained the EXACT libhrx mlir-aie pins for its HRX runtime: jtuyls/hrx release
  flm-hrx-amdxdna-v2026.07.30, asset hrx-amdxdna-2026.07.30-amdxdna-hal-native-rel-eb0b39f (SHA
  verified = the pinned 661ed940...). Has hrx_buffer_map_with_mode.
- Ran silu through the mlir-aie HRX runtime (NPU_RUNTIME=hrx + HRX_DIR) = the FLM-family userspace:
  * PEANO silu: PASSES (3s) - HRX integration + our xclbin/insts format = VALIDATED.
  * CHESS silu: ERT state 8 timeout - identical to the XRT insts/full-elf paths.
- => Every userspace (XRT insts, XRT full-elf, HRX/libhrx=FLM's runtime) boots peano cores but
  chess cores never complete. The gap = the CHESS-COMPILED CORE CONTENT itself, not the loader.
- FLM's own chess cores DO run on this NPU (the 35B serves). Their xclbin = same container/PDI
  scheme. Remaining delta = the core program content: AMD's internal chess build (flags/version/
  runtime libs/PDI packaging) vs our mlir-aie chess output. Next: extract + decode the core image
  from FLM's mm.xclbin PDI and diff against our chess core (entry/init/acquire) to find what AMD
  does differently (e.g. no me-runtime init, different crt, EV format).
- Also on the table: the mlir-aie upstream HRX backend (PR #3347) presumably runs chess cores in
  its CI - worth asking on #3690 which chess/flow it validated with.
## Update 16 — full FLM execution ecosystem mapped; core content confirmed as the sole delta
- FLM/1bit engine execution model (fully decoded from npu-infer + flm analysis):
  * xclbin (xclbin2 + AIE_PARTITION/PDI = the CORE programs) registered on the device.
  * The kernel control = a TXN instruction stream WRAPPED IN AN ELF (npu-infer txn-decode-findings:
    "_gen_elf(&elf_buf, data); // wraps TXN in an ELF") - loaded via xrt::elf + xrt::module +
    xrt::ext::kernel(hwctx, mod, "MLIR_AIE"), run with a scalar-first ABI (arg0..2 = scalars,
    then the DDR BOs).
  * This = the SAME split mlir-aie uses: xclbin (PDI cores) + insts.bin (TXN), dispatched via
    kernel(3, insts, ...) [XRT insts path] or libhrx. Peano cores run through all of these.
- NEW experiments: (a) aiecc full-elf (--get-full-elf, exports kernel "main") through the
  pyxrt.elf/hw_context/ext.kernel path: PEANO full-elf ALSO times out (ext-kernel path + aiecc
  full-elf = not the FLM txn-elf format; separate mismatch). (b) 1bit scalar-first ABI patched
  into the runtime: the aiecc full-elf kernel only declares 3 args (range check fails with 5) -
  again confirming the aiecc full-elf != the FLM txn-elf kernel ABI.
- => The execution machinery (xclbin/PDI cores + TXN control) is identical between us and FLM and
  fully validated with peano. Chess cores from mlir-aie do not run under ANY of it. Sole remaining
  delta = the core program content inside the PDI (mlir-aie chess output vs AMD's internal chess
  build). Decoding the aiebu/IDPP PDI core format to diff FLM's core vs ours = the last step
  (aiebu format lives in xrt SectionAIEPartition.cxx + the amdxdna driver pdi parser).
# Chess port campaign — session summary (2026-09-07)
State file: ~/iron/CHESS_PORT_STATE.md (updates 1-16). Upstream: Xilinx/mlir-aie#3690.

## DELIVERED (working)
1. Vitis 2025.2 installed on strixhalo (~/Xilinx2025, minimal config, aie2ps target; aie2p aliased
   via symlinks for aiecc compat).
2. Chess toolchain pipeline FIXED end-to-end through ELF generation:
   - chess_intrinsic_wrapper.ll regenerated against the target aietools (void_acquire mismatch solved)
   - stale kernel-object cache root-caused (machine-flags 3/4 link crash) + artifact
     segregation lesson (harness bug to fix: shared .o/.bin/.xclbin across peano/chess)
   - bare chess core link (no me-runtime) via a patched v1.4.2-source aiecc (orphan-handling=warn +
     me_primitive stubs), preserved at ~/mlir-aie-v142/build_v142/bin/aiecc
3. axpy: compiles under chess; 20/20 reference tests PASS under peano (the earlier peano "hang"
   was artifact-cache contamination).

## OPEN (one issue): chess cores don't execute on the NPU
- Chess cores time out (ERT state 8) under EVERY userspace tested: XRT insts path, XRT full-elf/
  ext::kernel path, and libhrx/HRX (= FLM's exact pinned runtime, SHA-verified). Peano passes all.
- FLM's own chess xclbins run on this NPU (35B MoE serving). Container/PDI/TXN formats identical.
- Evidence => the delta = the core program content inside the PDI: mlir-aie chess output vs AMD's
  internal chess build. Last step = decode the aiebu/IDPP PDI core format (xrt SectionAIEPartition,
  amdxdna driver pdi parser) and diff FLM's core vs ours.
- Filed Xilinx/mlir-aie#3690 with repro + evidence; asked AMD for their chess flags/crt/PDI flow.

## KEY REFS on strixhalo
- Vitis 2025.2 aietools: /home/bcloud/Xilinx2025/2025.2/Vitis/aietools
- Patched bare-capable aiecc: ~/mlir-aie-v142/build_v142/bin/aiecc (+ me_stub.o data/function)
- Release libhrx (FLM userspace): /tmp/hrx-rel/... (NPU_RUNTIME=hrx + HRX_DIR)
- Prior-campaign findings: pi ZFS backup (/ZFSPool/backups/strixhalo), 1bit docs
  (aiesim-debugging.md, FLM_SECRETS.md), npu-infer engine (txn-elf + ext::kernel "MLIR_AIE")
## Update 17 — FLM core content compared: register-vs-immediate acq + me-init = the visible deltas
- Extracted FLM's working mm.xclbin core program bytes + compared instruction signatures with ours:
  * FLM cores: 128x immediate acq, 0x register acq, NO me-runtime _main_init prelude.
  * Peano core (RUNS): 2x immediate acq, no me-init.
  * Our chess core (TIMES OUT): 0x immediate, 1x register acq (via llvm___aie2p___acquire wrapper),
    me-init prelude present.
- => Executing cores (FLM + peano) = no me-init + immediate acq. Chess output = me-init + register
  acq. Attempted to force chess to inline the acquire wrapper (alwaysinline + fences removed) ->
  chess still emits the register-form wrapper call; the chess model (me_chess.lib) only exposes
  register-arg acquire builtins, so immediate form is unreachable via the chesscc intrinsic path.
- Posted to #3690 (comment 5576347676): asking AMD (a) whether register-form acq r0,r1 or the me-init
  prelude is known-broken on AIE2P silicon, (b) which chess build/flow produced the flm-hrx-amdxdna
  cores (immediate acq + no me-init) so we can replicate it.
- Next in-house avenues if AMD doesn't respond: (1) test register-form acq directly on silicon via a
  minimal peano kernel emitting acq r0,r1 (isolate register-vs-immediate); (2) try older/newer
  Vitis aietools chess; (3) patch the mlir-aie chess flow to bypass the wrapper (emit acq #imm like
  peano) - requires chess-clang to lower llvm.aie2p.acquire directly.
## Update 18 — HRX/Loom clarified (GPU stack); NPU state unchanged; continuation close-out
- ws12-hrx-loom findings: HRX = the runtime, LOOM = the compiler (IREE-derived, Ben Vanik) in
  AMD's lemonade/llama.cpp migration. BUT that stack runs on the GPU (gfx1100/gfx1151 RDNA - Strix
  Halo iGPU/ROCm path), NOT the NPU. The 79 tok/s zaya/30B decode = GPU. Not the NPU chess path.
- The NPU userspace = jtuyls/hrx "amdxdna-hal-native" (libhrx with hrx_amdxdna_executable_create)
  = what mlir-aie NPU_RUNTIME=hrx uses + what FLM-style NPU xclbins dispatch through. Tested:
  peano silu PASSES via it, chess silu TIMES OUT via it. State unchanged.
- FLM's NPU xclbin cores (35B MoE) = chess-built, NO me-init signature, immediate-form acq
  (128x) - vs mlir-aie chess cores = me-init + register-form acq via wrapper. Posted to #3690.
  FLM xclbins are built by AMD internally (not from the fastflowlm repo - external staging).
- Chess-model me_chess.lib = register-arg acquire builtins only -> immediate form unreachable via
  the chesscc intrinsic path. llvm-objdump decode of register-vs-immediate acq + the me-init gap =
  the two structural deltas between working (FLM/peano) and hanging (mlir-aie chess) cores.
- TASK-1 STATUS (unchanged): harness + chess compile pipeline = working; axpy compiles under chess;
  axpy 20/20 under peano; the "passes under chess" clause = blocked on chess-core device execution
  = upstream #3690 (awaiting AMD: register-acq/me-init on-silicon validity + their chess build).
## Update 19 — acquire wrapper anatomy + register-form acq isolation status
- Chess acquire wrapper (chess listing, authoritative decode):
  * llvm___aie2p___acquire = 10 bytes: RET lr (offset 0) + ACQ r0,r1 (offset 4, annotated .delay_slot)
    + NOPs. The ACQ IS in the RET delay window = executes (NOT the dead-code ret-first bug - the
    prior campaign's poke-kernel case had the body PAST the window). So the acquire DOES run.
  * BUT: chess emits REGISTER-form acq r0,r1 (lock in r0, value in r1); peano + FLM cores emit
    IMMEDIATE-form acq #imm,rN. Same operand values (lock 51/48, -1). The register-form's silicon
    semantics (operand order/meaning) = the untested suspect: if acq rA,rB expects different
    operand roles or the lock as an address, chess waits on a garbage lock forever = our timeout.
- Isolation attempts blocked: (a) chess inline-asm acq = darts assembler rejects all forms;
  (b) chess model only exposes register-arg acquire builtins (no immediate); (c) peano only emits
  immediate for constant locks (can't force register form cleanly); (d) binary-patching the working
  peano core to register-form = needs the exact register-form encodings + operand regs (r1 vs r8 for
  the value) + spare VLIW slots = too risky/inconclusive.
- Chess model (me_chess_opns.h/me_chess.lib): acquire_guarded/release_guarded(unsigned,unsigned) =
  the register primitives only. No immediate-lock acquire in the 2025.2 model.
- => Full evidence package on Xilinx/mlir-aie#3690. Remaining unblocks: (1) AMD reply (register-acq
  validity on AIE2P silicon + their flm-hrx-amdxdna chess build), (2) a chess/aietools build whose
  codegen emits immediate acq (newer Vitis or AMD-internal), (3) an aiecc chess-flow patch that
  lowers llvm.aie2p.acquire to acq #imm like peano.
## Update 20 — no-op acquire test: hang is NOT the acquire instruction alone
- Patched the chess acquire wrapper to a pure no-op (release kept, register form): chess silu STILL
  returns ERT_CMD_STATE_TIMEOUT. So the register-form acq is not the sole hang point.
- Interpretation: with the acquire removed, the core still never completes - the hang is in the
  chess core's broader execution (release path, kernel call, loop, or the core never starting at
  all under the boot). The register-vs-immediate correlation (FLM/peano immediate+work vs chess
  register+hang) remains reported on #3690 as a datum, but the no-op test shows it is not the
  single cause.
- Full test matrix now on record: chess cores hang under me-runtime/bare/fence-free/no-op-acquire
  variants, through XRT insts/full-elf/HRX userspaces, while peano passes everywhere. Mixed core
  (chess main + peano kernel) also hangs => chess-compiled core main (boot/startup/loop/execution
  semantics) is the failing component, not the kernel code or a single acquire instruction.
- Wrapper restored to the working default; peano silu verified passing.
## Update 21 — guarded-vs-plain acq finding + full isolation matrix (chess codegen = the failing component)
- Found: chess emits the GUARDED acquire variant (opcode 30 18..., via chessintr_void_acquire_guarded)
  while peano + FLM cores use the PLAIN acquire (opcode 18 18...). 2025.2 model exposes only the
  guarded + no_fence acquire intrinsics.
- Tested: compiled PEANO shims defining llvm___aie2p___acquire/release with plain acq/rel
  (18 18 12 10 / 18 18 10 10), linked them into the chess-built core in place of the guarded
  wrapper (wrapper .ll -> declarations; aiecc peanoElfs + shim .arg). Result: core confirmed to
  contain plain acq+rel, no guarded forms, correct call-site args (r0=lock, r1=-1) -> STILL
  ERT_CMD_STATE_TIMEOUT.
- Complete isolation matrix (all hang): me-runtime / bare / fence-free / no-op-acquire /
  plain-lock-shim; through XRT insts / full-elf / HRX; mixed core (chess main + peano kernel) hangs.
  Peano passes all. => the failing component = the chess-compiled core main CODE itself (control
  flow / memory access / ABI on real silicon), not the loader, me-init, guarded-vs-plain locks,
  or the kernel.
- Guarded-vs-plain acq = still a documented delta (posted to #3690) but not the sole cause.
- Default state restored: dev16 pip aiecc + guarded wrapper; peano silu verified passing.
## Update 22 — 🎉 TASK-1 COMPLETE: chess kernels RUN + PASS reference tests on the NPU2
- ROOT CAUSE FOUND + FIXED: Vitis 2025.2/2026.1 aie2ps chess models expose only the GUARDED
  acquire intrinsic -> chesscc emits the guarded acq (encoding 30 18 12 20) which never completes
  on this NPU2 silicon. The Ryzen-AI 1.3.0 vitis_aie_essentials (2024) chess model has the
  UNGUARDED acquire -> emits the PLAIN acq (18 18 12 10 = same as peano + FLM cores) -> WORKS.
- THE WORKING RECIPE (strixhalo):
  * AIETOOLS_ROOT = ~/Downloads/ryzen_ai-1.3.0/vitis_aie_essentials (2024 aie2ps chess, unguarded
    wrapper .ll = aie_runtime_lib AIE2P .bak-2024 restored)
  * patched v1.4.2-source aiecc (~/mlir-aie-v142/build_v142/bin/aiecc): peanoElfs bare link
    (--xbridge=false via AIE_AIECC_NO_XBRIDGE=1), me_primitive stubs (.arg me_stub.o),
    libsoftfloat.a (f32 conversions), orphan-handling=warn
  * llvm-aie clang on PATH (bare link driver)
- VERIFIED: axpy 20/20 + silu 20/20 PASS under compiler="chess"; peano regression clean
  (axpy 20/20 + silu 20/20). Compile+link+load+execute+correctness = end-to-end working.
- Posted resolution to Xilinx/mlir-aie#3690 (comment 5576721393).
- NOTE: the guarded-acquire hang = a 2025.2+ chesscc silicon-visible defect; the 2024 essentials
  chess = the workaround until AMD fixes the guarded path.
## TASK-2 COMPLETE — all 11 elementwise/activation operators pass under chess
- Verified (2024 vitis_aie_essentials recipe): silu 20, relu 40, gelu 40, tanh 40, sigmoid 40,
  leaky_relu 50, elementwise_add 20, elementwise_mul 20, softmax 15, layer_norm 40, rms_norm 75
  = 400/400 under compiler="chess"; peano regression 400/400 clean.
- Kernel fixes made (in-tree, peano-safe):
  1. leaky_relu: kernel bfloat16 scalar arg -> float arg + (bfloat16) cast inside (chess LLVM
     rejects bfloat call-constants; aie::to_float<bfloat16>(float,0) truncates to int = wrong).
     Files: aie_kernels/aie2p/leaky_relu.cc + iron/operators/leaky_relu/design.py (.bak-f32 saved).
  2. softmax: float-vs-bfloat16 comparison ambiguities at softmax.cc (chess front-end) -> explicit
     (float) casts (.bak-cast saved).
  3. aiecc (patched v1.4.2, ~/mlir-aie-v142): fixChessFloatLiterals() rewrites float/double
     constant literals to exact decimals (chess LLVM rejects hex "f0x..."/short-sci for non-exact
     values; accepts %.17g of the f32). Handles the 16-hex f64-in-float-slot printer quirk by
     narrowing to f32.
- Mesh: shared the recipe with agent-18dcf9 + agent-97adad (cross-lane; their chess-core goals
  confirmed root cause).
## TASK-3 COMPLETE — gemm/gemv/dequant/mha pass under chess
- Verified: gemv 95, dequant 40, gemm 45, mha 5 = 185/185 under compiler="chess"
  (2024 vitis_aie_essentials recipe); peano regression 185/185 clean.
- Kernel fixes:
  1. mha: the design calls the 9-arg `partial_softmax` (mha.cc) whose `bfloat16 inv_scale` ->
     float (chain: partial_softmax -> partial_softmax_bf16 -> alias, all f32 with (bfloat16) casts
     at the alias boundary). bfloat call-constants impossible in the chess LLVM.
     Files: aie_kernels/aie2p/mha.cc + softmax.cc + iron/operators/mha/design.py.
  2. The aiecc float-literal fixup (fixChessFloatLiterals) handles the 0.1806640625 scale
     (exact-decimal rewrite; f64-in-float-slot printer quirk narrowed to f32).
- 3/5 tasks done: task-1 (harness/axpy), task-2 (11 elementwise/activation), task-3 (4 matmul/
  attention). Remaining: task-4 (transpose/strided_copy/repeat/mem_copy/axpy data-movement),
  task-5 (Qwen3-0.6B single-layer smoke under chess + peano regression).
## TASK-4 COMPLETE — data-movement kernels pass under chess
- Verified: transpose/strided_copy/repeat/mem_copy = 140/140 + axpy 20/20 = 160/160 under
  compiler="chess" (2024 vitis_aie_essentials recipe); peano regression 160/160 clean.
- No kernel fixes needed for these (pure data-movement, no scalar args).
- 4/5 tasks done. Remaining: task-5 = Qwen3-0.6B single-layer smoke under chess (smoke_layer.py
  LAYER_OK + HEAD_OK) + peano regression.
## TASK-5 COMPLETE — Qwen3-0.6B decode smoke compiles under chess (5/5 done!)
- smoke_layer.py (real dims: emb 1024, hid 3072, 16 heads, 8 kv, hd 128, vocab
  151936): LAYER_OK + HEAD_OK under compiler="chess" (~16 min full compile);
  peano smoke + deep peano regression clean (160/160 sampled).
- Kernel fix this checkpoint (soft-float link): chess-compiled kernels with scalar
  f32 math (rms_norm etc.) call the softfloat C API (float32_add/div/mul/lt,
  int32_to_float32). The vitis aie2p libsoftfloat.a is a chess archive whose
  per-TU __llN__ locals a bare ld.lld cannot resolve (undefined symbols at the
  peanoElfs link). Fix: wrote aie2p_softfloat.c — a pure-integer, self-contained
  reimplementation of exactly those 5 functions (RNE, subnormals) — validated
  BIT-EXACT against native f32 on 2M+ random patterns (add/mul/div/lt/i2f),
  compiled with llvm-aie clang --target=aie2p-none-unknown-elf, linked into the
  aiecc peanoElfs bare link AFTER the objects. File: ~/mlir-aie-v142/aie2p_softfloat.c
  (+ aiecc.cpp edit). Also fixed the archive ORDER issue (libs must follow objs).
- All 5 goal tasks complete: task-1 axpy/harness, task-2 11 elementwise/activation,
  task-3 gemm/gemv/dequant/mha, task-4 data-movement, task-5 Qwen3-0.6B layer+head
  smoke. Full chess compiler="chess" coverage of the aie_kernels library + the
  Qwen3 decode layer. Peano path unregressed throughout.

## Update 27 — second audit closure: entire-library xchesscc proof + evidence gaps filled
- **aie2/softmax.cc fixed** (audit defect): `-INFINITY` not defined by the aie2 chess
  front-end headers -> `(bfloat16)(-65504.0f)` (most-negative finite bf16; identical masking
  semantics, exp2 underflows to 0). Peano compile of the file verified (clang++ -std=c++20
  --target=aie2-none-unknown-elf with harness flags -D__AIE_API_AIE_ADF_HPP__ -DNDEBUG).
- **ENTIRE LIBRARY xchesscc compile proof (32/32 files)**:
  * aie2/*.cc  (11 files): OK with `xchesscc_wrapper AIE2` (incl. fixed softmax.cc)
  * aie2p/*.cc (13 files): OK with `xchesscc_wrapper AIE2P`; mha.cc requires the harness
    flags `-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16 -Dbf16_bf16_ONLY -DDIM_M=64
    -DDIM_K=64 -DDIM_N=64 -DB_COL_MAJ -DROUND_CONV_EVEN` (bare compile instantiates the
    2024-header-unsupported native 8x8x8 bf16 mmul)
  * generic/*.cc (8 files): OK with `xchesscc_wrapper AIE2P`; mv.cc needs `-DDIM_K`,
    transpose.cc needs `-DDIM_m=32 -DDIM_n=32` (design-time defines, as the harness passes)
- **aie2p_softfloat.c source recovered + saved**: reconstructed deterministically from the
  executor session transcript (base + patch_sf + patch_sf2), verified by compiling for aie2p
  and matching all 82 defined symbols against the shipped aie2p_softfloat.o. Saved at
  ~/mlir-aie-v142/tools/aiecc/aie2p_softfloat.c (was previously .o-only).
- **rope/swiglu reference tests (operators outside the 5-task tree)**:
  chess 55 passed / 1 skipped (swiglu_prefill_stream deselected) in 7:08; peano 55 passed
  in 12.7s. No regression.
- **Post-audit clean-state re-verification (agent-d41b06, artifacts wiped)**: chess axpy 20/20
  (59.5s), peano axpy 20/20 (5.1s), chess silu 20/20 (56.7s); task-5 smoke clean build under
  FINAL toolchain: IRON_COMPILER=chess LAYER_OK+HEAD_OK (/tmp/chess_smoke_final.log) and
  peano LAYER_OK+HEAD_OK (/tmp/peano_smoke_final.log).
