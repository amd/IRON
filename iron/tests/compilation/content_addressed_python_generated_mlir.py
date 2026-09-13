#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""PythonGeneratedMLIRArtifact.is_available_in_filesystem() must key on the DesignGenerator's
full call shape (source_path, fn_name, args, kwargs), not just source_path's mtime -- the same
SCORES_ROWBATCH-shaped defect content_addressed_kernel_objects.py closes for KernelObjectArtifact,
here for the OTHER caller unified-content-addressed-kernel-cache's next: names as still open.

Mirrors that file's structure and discipline (row-4 mutation test, sabotage non-vacuity proof).
"""

import json
from pathlib import Path
from unittest import mock

from iron.common.cache import content_key
from iron.common.compilation.base import (
    DesignGenerator,
    GenerateMLIRFromPythonCompilationRule,
    PythonGeneratedMLIRArtifact,
)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def _built_artifact(tmp_path, *, kwargs=None):
    source = tmp_path / "gen.py"
    _write(source, "def make(rows): return f'mlir for {rows} rows'\n")
    generator = DesignGenerator(source_path=source, fn_name="make", kwargs=kwargs or {})

    mlir = tmp_path / "out.mlir"
    _write(mlir, "<generated mlir>")

    artifact = PythonGeneratedMLIRArtifact(filename=str(mlir), generator=generator)
    inputs = [str(source)]
    flags = _flags(generator)
    toolchain = "python-v1"
    key = content_key(inputs, flags, toolchain)
    _write(
        Path(f"{mlir}.contentkey.json"),
        json.dumps(
            {"key": key, "inputs": inputs, "flags": flags, "toolchain": toolchain}
        ),
    )
    return artifact, source, key, toolchain


def _flags(generator):
    from iron.common.compilation.base import _generator_content_flags

    return _generator_content_flags(generator)


def _with_fixed_toolchain(toolchain):
    return mock.patch("sys.version", toolchain)


def test_a_freshly_built_artifact_is_available(tmp_path):
    artifact, _source, _key, toolchain = _built_artifact(tmp_path, kwargs={"rows": 4})
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()


def test_a_kwarg_only_change_misses_and_is_not_served_stale(tmp_path):
    """Row-4 shape: two calls to the SAME generator function differing only in a kwarg
    (gen_llm_decode.py's scores_rowbatch) must not share one cached "available" file."""
    artifact, _source, old_key, toolchain = _built_artifact(
        tmp_path, kwargs={"rows": 1}
    )
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()

        artifact.generator.kwargs = {"rows": 4}
        new_key = content_key(
            [str(artifact.generator.source_path)], _flags(artifact.generator), toolchain
        )
        assert new_key != old_key, "content key did not change after the kwarg mutation"
        assert (
            not artifact.is_available_in_filesystem()
        ), "a kwarg-only mutation was silently served the pre-mutation MLIR"
        assert Path(artifact.filename).read_bytes() == b"<generated mlir>"


def test_a_changed_source_file_also_misses(tmp_path):
    artifact, source, _key, toolchain = _built_artifact(tmp_path)
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()
        source.write_text("def make(rows): return 'a different body'\n")
        assert not artifact.is_available_in_filesystem()


def test_a_missing_manifest_is_not_available(tmp_path):
    artifact, *_rest = _built_artifact(tmp_path)
    Path(f"{artifact.filename}.contentkey.json").unlink()
    assert not artifact.is_available_in_filesystem()


def test_a_toolchain_change_misses_even_with_unchanged_inputs_and_flags(tmp_path):
    artifact, *_rest, toolchain = _built_artifact(tmp_path)
    with _with_fixed_toolchain(toolchain + "-rebuilt"):
        assert not artifact.is_available_in_filesystem()


def test_args_or_kwargs_holding_a_non_scalar_value_fails_closed(tmp_path):
    """An object with no informative __repr__ is not a stable function of content
    (its default repr embeds a memory address) -- must never enter the key."""
    source = tmp_path / "gen.py"
    _write(source, "def make(obj): return str(obj)\n")
    generator = DesignGenerator(source_path=source, fn_name="make", args=(object(),))
    mlir = tmp_path / "out.mlir"
    _write(mlir, "<generated mlir>")
    artifact = PythonGeneratedMLIRArtifact(filename=str(mlir), generator=generator)
    assert not artifact.is_available_in_filesystem()


def test_record_cache_entry_writes_a_manifest_that_is_then_recognized_available(
    tmp_path,
):
    source = tmp_path / "gen.py"
    _write(source, "def make(rows): return f'mlir for {rows} rows'\n")
    generator = DesignGenerator(source_path=source, fn_name="make", kwargs={"rows": 4})
    mlir = tmp_path / "out.mlir"

    artifact = PythonGeneratedMLIRArtifact(filename=str(mlir), generator=generator)
    GenerateMLIRFromPythonCompilationRule.generate_mlir(artifact, generator)
    assert (
        not artifact.is_available_in_filesystem()
    ), "no manifest exists yet; a fresh generation must not already look available"
    assert GenerateMLIRFromPythonCompilationRule._record_cache_entry(artifact) is True
    assert artifact.is_available_in_filesystem()


def test_sabotaging_content_key_to_a_constant_makes_the_mutation_guard_go_red(tmp_path):
    artifact, source, _old_key, toolchain = _built_artifact(
        tmp_path, kwargs={"rows": 1}
    )
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()
        source.write_text("def make(rows): return 'a different body'\n")

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
