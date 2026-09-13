#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FullElfArtifact/XclbinArtifact/InstsBinArtifact.is_available_in_filesystem() must be
content-addressed too -- a false "available" here skips calling compile_mlir_module()
entirely, so its own correct internal cache (aie.utils.compile.utils._aiecc_cache_key)
never even runs. Peano only: see _AieccOutputArtifact's docstring for why a Chess build is
left mtime-only rather than checked against a fingerprint nothing here can verify.

Mirrors content_addressed_kernel_objects.py's structure and discipline.
"""

import json
from pathlib import Path
from unittest import mock

from iron.common.cache import content_key
from iron.common.compilation.base import (
    AieccFullElfCompilationRule,
    AieccXclbinInstsCompilationRule,
    CompilationArtifactGraph,
    FullElfArtifact,
    InstsBinArtifact,
    MLIRArtifact,
    SourceArtifact,
    XclbinArtifact,
    _record_aiecc_output_cache_entry,
)


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, bytes):
        path.write_bytes(data)
    else:
        path.write_text(data)


def _with_fixed_toolchain(toolchain):
    return mock.patch(
        "iron.common.compilation.base._peano_toolchain_fingerprint",
        return_value=toolchain,
    )


def _built_full_elf(tmp_path, *, extra_flags=(), trace_size=0):
    mlir = tmp_path / "fused.mlir"
    _write(mlir, "<mlir text>")
    kernel_obj = tmp_path / "kernel.o"
    _write(kernel_obj, "<compiled bytes>")

    mlir_artifact = MLIRArtifact(str(mlir))
    kernel_artifact = SourceArtifact(str(kernel_obj))
    elf = tmp_path / "fused.elf"
    _write(elf, "<full elf bytes>")

    artifact = FullElfArtifact(
        str(elf),
        mlir_input=mlir_artifact,
        dependencies=[mlir_artifact, kernel_artifact],
        extra_flags=list(extra_flags),
        trace_size=trace_size,
    )
    inputs = [d.filename for d in artifact.dependencies]
    flags = artifact._content_flags()
    toolchain = "peano-v1"
    key = content_key(inputs, flags, toolchain)
    _write(
        Path(f"{elf}.contentkey.json"),
        json.dumps(
            {"key": key, "inputs": inputs, "flags": flags, "toolchain": toolchain}
        ),
    )
    return artifact, kernel_obj, key, toolchain


def test_a_freshly_built_full_elf_is_available(tmp_path):
    artifact, _kernel, _key, toolchain = _built_full_elf(tmp_path, extra_flags=["-j1"])
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()


def test_a_flag_only_change_misses_and_is_not_served_stale(tmp_path):
    artifact, _kernel, old_key, toolchain = _built_full_elf(tmp_path, trace_size=0)
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()

        artifact.trace_size = (
            4096  # a traced build is a different graph, not a bigger buffer
        )
        new_key = content_key(
            [d.filename for d in artifact.dependencies],
            artifact._content_flags(),
            toolchain,
        )
        assert new_key != old_key
        assert not artifact.is_available_in_filesystem()
        assert Path(artifact.filename).read_bytes() == b"<full elf bytes>"


def test_a_linked_kernel_objects_bytes_changing_also_misses(tmp_path):
    """The dependency graph, not a hand-picked file list, is where FullElfArtifact's real
    inputs live -- a linked .o changing under an unchanged MLIR text must still miss."""
    artifact, kernel_obj, _old_key, toolchain = _built_full_elf(tmp_path)
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()
        kernel_obj.write_text("<recompiled, different bytes>")
        assert not artifact.is_available_in_filesystem()


def test_a_missing_manifest_is_not_available(tmp_path):
    artifact, *_rest = _built_full_elf(tmp_path)
    Path(f"{artifact.filename}.contentkey.json").unlink()
    assert not artifact.is_available_in_filesystem()


def test_a_toolchain_change_misses_even_with_unchanged_inputs_and_flags(tmp_path):
    artifact, *_rest, toolchain = _built_full_elf(tmp_path)
    with _with_fixed_toolchain(toolchain + "-rebuilt"):
        assert not artifact.is_available_in_filesystem()


def test_xclbin_keys_on_kernel_name_and_its_own_xclbin_input(tmp_path):
    mlir = tmp_path / "op.mlir"
    _write(mlir, "<mlir text>")
    mlir_artifact = MLIRArtifact(str(mlir))
    base = tmp_path / "base.xclbin"
    _write(base, "<base xclbin>")
    base_artifact = XclbinArtifact(
        str(base), mlir_input=mlir_artifact, dependencies=[mlir_artifact]
    )

    xclbin = tmp_path / "op.xclbin"
    _write(xclbin, "<xclbin bytes>")
    artifact = XclbinArtifact(
        str(xclbin),
        mlir_input=mlir_artifact,
        dependencies=[mlir_artifact],
        kernel_name="MY_KERNEL",
        xclbin_input=base_artifact,
    )
    inputs = [d.filename for d in artifact.dependencies]
    flags = artifact._content_flags()
    toolchain = "peano-v1"
    key = content_key(inputs, flags, toolchain)
    _write(
        Path(f"{xclbin}.contentkey.json"),
        json.dumps(
            {"key": key, "inputs": inputs, "flags": flags, "toolchain": toolchain}
        ),
    )
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()
        artifact.kernel_name = "A_DIFFERENT_KERNEL"
        assert not artifact.is_available_in_filesystem()


# --- The real recording path, not just a hand-authored fixture --------------------


def test_record_cache_entry_writes_a_manifest_that_is_then_recognized_available(
    tmp_path,
):
    mlir = tmp_path / "op.mlir"
    _write(mlir, "<mlir text>")
    mlir_artifact = MLIRArtifact(str(mlir))
    insts = tmp_path / "op.bin"
    _write(insts, "<insts bytes>")
    artifact = InstsBinArtifact(
        str(insts), mlir_input=mlir_artifact, dependencies=[mlir_artifact]
    )

    with _with_fixed_toolchain("peano-v1"):
        assert not artifact.is_available_in_filesystem()
        assert _record_aiecc_output_cache_entry(artifact) is True
        assert artifact.is_available_in_filesystem()


def test_chess_builds_are_never_recorded_so_stay_conservatively_unavailable(tmp_path):
    """No call site in this tree threads use_chess through to these artifact classes, so
    there is nothing here to verify a Chess manifest against. Both compilation rules must
    skip recording under use_chess=True rather than record against a Peano fingerprint a
    Chess build did not produce."""
    mlir = tmp_path / "fused.mlir"
    _write(mlir, "<mlir text>")
    mlir_artifact = MLIRArtifact(str(mlir))
    mlir_artifact.available = True
    elf = tmp_path / "fused.elf"

    artifact = FullElfArtifact(
        str(elf), mlir_input=mlir_artifact, dependencies=[mlir_artifact]
    )
    graph = CompilationArtifactGraph([artifact])

    with mock.patch("iron.common.compilation.base.compile_mlir_module") as fake_compile:
        fake_compile.side_effect = lambda *a, **kw: _write(elf, "<full elf bytes>")
        commands = AieccFullElfCompilationRule(use_chess=True).compile(graph)
        for command in commands:
            command.run()

    assert elf.exists()
    assert not Path(
        f"{elf}.contentkey.json"
    ).exists(), (
        "a Chess build must not write a manifest checked against a Peano fingerprint"
    )
    assert not artifact.is_available_in_filesystem()


def test_xclbin_insts_rule_records_both_outputs_from_one_aiecc_call(tmp_path):
    """One compile_mlir_module call can emit both an xclbin and an insts.bin; each of the
    two artifacts must get its OWN correct manifest, not one shared or skipped."""
    mlir = tmp_path / "op.mlir"
    _write(mlir, "<mlir text>")
    mlir_artifact = MLIRArtifact(str(mlir))
    mlir_artifact.available = True
    xclbin = tmp_path / "op.xclbin"
    insts = tmp_path / "op.bin"

    xclbin_artifact = XclbinArtifact(
        str(xclbin), mlir_input=mlir_artifact, dependencies=[mlir_artifact]
    )
    insts_artifact = InstsBinArtifact(
        str(insts), mlir_input=mlir_artifact, dependencies=[mlir_artifact]
    )
    graph = CompilationArtifactGraph([xclbin_artifact, insts_artifact])

    with (
        mock.patch("iron.common.compilation.base.compile_mlir_module") as fake_compile,
        _with_fixed_toolchain("peano-v1"),
    ):
        fake_compile.side_effect = lambda *a, **kw: (
            _write(xclbin, "<xclbin bytes>"),
            _write(insts, "<insts bytes>"),
        )
        commands = AieccXclbinInstsCompilationRule(use_chess=False).compile(graph)
        for command in commands:
            command.run()

        assert xclbin_artifact.is_available_in_filesystem()
        assert insts_artifact.is_available_in_filesystem()


def test_peano_full_elf_rule_records_and_a_second_plan_pass_recognizes_it(tmp_path):
    mlir = tmp_path / "fused.mlir"
    _write(mlir, "<mlir text>")
    mlir_artifact = MLIRArtifact(str(mlir))
    mlir_artifact.available = True
    elf = tmp_path / "fused.elf"

    artifact = FullElfArtifact(
        str(elf), mlir_input=mlir_artifact, dependencies=[mlir_artifact]
    )
    graph = CompilationArtifactGraph([artifact])

    with (
        mock.patch("iron.common.compilation.base.compile_mlir_module") as fake_compile,
        _with_fixed_toolchain("peano-v1"),
    ):
        fake_compile.side_effect = lambda *a, **kw: _write(elf, "<full elf bytes>")
        commands = AieccFullElfCompilationRule(use_chess=False).compile(graph)
        for command in commands:
            command.run()

        assert artifact.is_available_in_filesystem()


# --- Non-vacuity: sabotage the key function and confirm the guard goes red --------


def test_sabotaging_content_key_to_a_constant_makes_the_mutation_guard_go_red(tmp_path):
    artifact, kernel_obj, _old_key, toolchain = _built_full_elf(tmp_path)
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()
        kernel_obj.write_text("<recompiled, different bytes>")

        with mock.patch(
            "iron.common.compilation.base.content_key", return_value="constant-key"
        ):
            manifest_path = Path(f"{artifact.filename}.contentkey.json")
            manifest = json.loads(manifest_path.read_text())
            manifest["key"] = "constant-key"
            manifest_path.write_text(json.dumps(manifest))
            assert artifact.is_available_in_filesystem(), (
                "sabotage did not reproduce the failure -- the guard may already be "
                "vacuous for a different reason, or this test no longer exercises it"
            )
