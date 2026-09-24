# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile, rename, prefix, and archive real kernels without opening an NPU."""

from pathlib import Path
import subprocess

import aie.utils.config as config
import pytest

from iron.common import AIEContext
from iron.common.compilation import base as comp


@pytest.mark.parametrize("arch", ["aie2", "aie2p"])
@pytest.mark.parametrize("rename", [False, True])
@pytest.mark.parametrize("prefix", [False, True])
def test_kernel_symbols_and_archive(tmp_path, monkeypatch, arch, rename, prefix):
    monkeypatch.setattr(comp, "get_kernel_dir", lambda: arch)
    source = tmp_path / "kernel.cc"
    source.write_text(
        'extern "C" {\n'
        "int external_fn(int);\n"
        "int helper(int x) { return x + 1; }\n"
        "int entry(int x) { return external_fn(helper(x)); }\n"
        "}\n"
    )
    objects = [
        comp.KernelObjectArtifact(
            f"kernel{i}.o",
            dependencies=[comp.SourceArtifact(source)],
            rename_symbols={"entry": "renamed"} if rename else None,
            prefix_symbols=f"op{i}_" if prefix else None,
        )
        for i in range(2)
    ]
    archive = comp.KernelArchiveArtifact("kernels.a", dependencies=objects)
    context = AIEContext(build_dir=tmp_path / "build with spaces")

    comp.compile(
        context.compilation_rules,
        comp.CompilationArtifactGraph([archive]),
        build_dir=str(context.build_dir),
    )

    for i, obj in enumerate(objects):
        result = subprocess.run(
            [
                config.nm_path(),
                "--defined-only",
                "--extern-only",
                "--format=posix",
                obj.filename,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        symbols = {line.split()[0] for line in result.stdout.splitlines()}
        symbol_prefix = f"op{i}_" if prefix else ""
        entry = "renamed" if rename else "entry"
        assert symbols == {f"{symbol_prefix}{entry}", f"{symbol_prefix}helper"}

        result = subprocess.run(
            [
                config.nm_path(),
                "--undefined-only",
                "--format=posix",
                obj.filename,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        assert {line.split()[0] for line in result.stdout.splitlines()} == {
            "external_fn"
        }
        assert list(Path(obj.filename).parent.glob("*.symbol_map*")) == []
        assert list(Path(obj.filename).parent.glob("aie-symbol-map-*")) == []

    result = subprocess.run(
        [config.ar_path(), "t", archive.filename],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.splitlines() == [Path(obj.filename).name for obj in objects]
