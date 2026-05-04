# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This file implements a simple Python-based build system. You specify what you
want to compile (*artifacts*) through subclasses of `CompilationArtifact`.
Multiple `CompilationArtifacts` form a `CompilationArtifactGraph`. Each artifact
can have a list (subgraph) of dependencies of other artifacts that it relies on.
Each artifact corresponds to exactly one file.

There is a special artifact for source files that do not need to get generated,
`SourceArtifact`. It is likely that in your compilation dependency graph,
the leaf nodes will be `SourceArtifact`s.

You specify how to generate (compile) an artifact through *rules*, which are
expressed as subclasses of `CompilationRule`. Rules must implement two methods:
`matches` and `compile`. If a rule `matches` to an artifact graph, it can be
applied. Applying a rule is done by calling `compile`; this transforms the
artifact graph (in the simplest case, marks one of the artifacts as available)
and returns a list of compilation commands.

At this point, we can print the compilation commands to the console (dry-run)
or actually run them to generate the artifacts.

Before starting compilation, you may call
`populate_availability_from_filesystem()` -- this will check if any artifacts
are already available at the given file paths (and ensure that dependencies are
as old or older than the artifacts that depend on them). This way, you can avoid
recompiling artifacts that are already up-to-date on disk. If you wish to
regenerate everything, you can skip this step, but will at a minimum want to
mark the `SourceArtifact`s as available -- they cannot be generated.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Iterator, Sequence
from pathlib import Path
import os.path
import shutil
import zlib
import logging
import subprocess
import importlib.util
from dataclasses import dataclass, field
from functools import partial
from typing import Any, Callable
import sys

from iron.common.device_utils import get_kernel_dir

# Global Functions
# ##########################################################################


@dataclass
class DesignGenerator:
    """Lazy callable that imports source_path and calls fn_name(*args, **kwargs), returning MLIR as a string."""

    source_path: Path
    fn_name: str
    args: tuple = ()
    kwargs: dict[str, Any] = field(default_factory=dict)

    def __call__(self) -> str:
        spec = importlib.util.spec_from_file_location(
            self.source_path.name, self.source_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return str(getattr(module, self.fn_name)(*self.args, **self.kwargs))


def plan(
    rules: Sequence[CompilationRule],
    graph: CompilationArtifactGraph,
    _seen_unavailable: frozenset[str] | None = None,
) -> list[tuple[CompilationRule, list[CompilationCommand]]]:
    # _seen_unavailable: snapshot of unavailable artifact filenames from the
    # previous recursion.  If a rule fires but the unavailable set is unchanged,
    # we raise RuntimeError to detect rules that make no forward progress
    # (stall detection, not graph-cycle detection).
    if all(artifact.is_available() for artifact in graph):
        return []  # Everything has been compiled
    for rule in rules:
        if rule.matches(graph):
            commands = rule.compile(graph)
            break
    else:
        raise RuntimeError(
            f"No matching rule to compile target(s): {', '.join(artifact.filename for artifact in graph)}"
        )
    unavailable = frozenset(
        artifact.filename for artifact in graph.bfs() if not artifact.is_available()
    )
    if unavailable == _seen_unavailable:
        raise RuntimeError(
            f"Rule {rule.__class__.__name__} fired but made no progress. "
            f"Still unavailable: {sorted(unavailable)}"
        )
    return [(rule, commands)] + plan(rules, graph, _seen_unavailable=unavailable)


def execute(plan_steps: list[tuple[CompilationRule, list[CompilationCommand]]]) -> None:
    for rule, commands in plan_steps:
        logging.debug(f"Applying rule: {rule.__class__.__name__}")
        for command in commands:
            logging.debug(f"  Executing command: {command}")
            success = command.run()
            if not success:
                raise RuntimeError(f"Command failed: {command}")


def compile(
    rules: Sequence[CompilationRule],
    artifacts: CompilationArtifactGraph,
    build_dir: str = "build",
    dry_run: bool = False,
) -> None:
    if not Path(build_dir).exists() and not dry_run:
        Path(build_dir).mkdir(parents=True, exist_ok=True)
    artifacts.move_artifacts(build_dir)
    artifacts.populate_availability_from_filesystem()
    plan_steps = plan(rules, artifacts)
    if not dry_run:
        execute(plan_steps)
    else:
        print("\n".join("\n".join(map(str, cmds)) for _, cmds in plan_steps))


# Compilation Artifact Graph
# ##########################################################################


class CompilationArtifactGraph:
    """DAG of compilation artifacts representing a build dependency graph."""

    def __init__(self, artifacts: list[CompilationArtifact] | None = None) -> None:
        """Initialize the graph.

        Args:
            artifacts: Top-level artifacts to include in the graph.  Each
                artifact may reference further dependencies, forming the DAG.
        """
        self.artifacts: list[CompilationArtifact] = (
            artifacts if artifacts is not None else []
        )

    def __repr__(self) -> str:
        def format_artifact(artifact: CompilationArtifact, indent: int = 0) -> str:
            prefix = "    " * indent
            avail = "[x] " if artifact.is_available() else "[ ] "
            result = f"{prefix}{avail}{artifact.__class__.__name__}({Path(artifact.filename).name})\n"
            for dep in artifact.dependencies:
                result += format_artifact(dep, indent + 1)
            return result

        result = "CompilationArtifactGraph(\n"
        for artifact in self.artifacts:
            result += format_artifact(artifact, indent=1)
        result += ")"
        return result

    def __iter__(self) -> Iterator[CompilationArtifact]:
        return iter(self.artifacts)

    def __len__(self) -> int:
        return len(self.artifacts)

    def __getitem__(self, index: int) -> CompilationArtifact:
        return self.artifacts[index]

    def dfs(self) -> Iterator[CompilationArtifact]:
        return self._traverse(True)

    def bfs(self) -> Iterator[CompilationArtifact]:
        return self._traverse(False)

    def _traverse(self, dfs: bool) -> Iterator[CompilationArtifact]:
        visited: set[CompilationArtifact] = set()
        todo: deque[CompilationArtifact] = deque(self.artifacts)
        while todo:
            artifact = todo.pop() if dfs else todo.popleft()
            if artifact in visited:
                continue
            visited.add(artifact)
            todo.extend(artifact.dependencies)
            yield artifact

    def replace(
        self, old_artifact: CompilationArtifact, new_artifact: CompilationArtifact
    ) -> CompilationArtifactGraph:
        for i, artifact in enumerate(self.artifacts):
            if artifact == old_artifact:
                self.artifacts[i] = new_artifact
            else:
                artifact.dependencies.replace(old_artifact, new_artifact)
        return self

    def populate_availability_from_filesystem(self) -> None:
        for artifact in self.artifacts:
            artifact.dependencies.populate_availability_from_filesystem()
            artifact.available = artifact.is_available_in_filesystem()

    def get_worklist(self, kind: type | tuple[type, ...]) -> list[CompilationArtifact]:
        """Return a list of artifacts of the given kind that can be built in the next step (dependencies available)."""
        return [
            artifact
            for artifact in self.bfs()
            if isinstance(artifact, kind)
            and not artifact.is_available()
            and artifact.dependencies_available()
        ]

    def move_artifacts(self, new_root: str) -> None:
        """Make all artifacts paths point into a build directory"""
        for artifact in self.bfs():
            if not Path(artifact.filename).is_absolute():
                artifact.filename = str(Path(new_root) / Path(artifact.filename).name)

    def add(self, artifact: CompilationArtifact) -> None:
        self.artifacts.append(artifact)


# Compilation Artifacts
# ##########################################################################


class CompilationArtifact(ABC):
    """Abstract base for a single node in a compilation artifact graph.

    Each artifact corresponds to exactly one file on disk.  Subclasses
    represent specific kinds of build products (source files, MLIR modules,
    kernel objects, xclbin packages, etc.).
    """

    def __init__(
        self,
        filename: str | Path,
        dependencies: list[CompilationArtifact] | None = None,
        available: bool = False,
    ) -> None:
        """Initialize the artifact.

        Args:
            filename: Path to the file produced by this artifact.
            dependencies: Artifacts that must be built before this one.
            available: Whether the artifact is already considered built.
        """
        self.filename = str(filename)
        self.dependencies: CompilationArtifactGraph = CompilationArtifactGraph(
            artifacts=dependencies if dependencies is not None else []
        )
        self.available = available

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.filename})"

    def is_available(self) -> bool:
        """'Conceptual' availability: during a dry-run or in the planning stage, available may be True even if the underlying file does not exist yet."""
        # If any of our dependencies' dependencies are outdated, this artifact is also outdated
        return self.available and self.dependencies_available()

    def dependencies_available(self) -> bool:
        """Return True if all direct dependencies are available."""
        return all(d.is_available() for d in self.dependencies)

    def is_available_in_filesystem(self) -> bool:
        """'Real' availability: checks if the underlying file exists and is up-to-date with respect to dependencies."""
        if not Path(self.filename).exists():
            return False
        file_mtime = os.path.getmtime(self.filename)
        for dependency in self.dependencies:
            if (
                not dependency.is_available_in_filesystem()
                or os.path.getmtime(dependency.filename) > file_mtime
            ):
                return False
        return True


class SourceArtifact(CompilationArtifact):
    """Artifact representing a source file that does not need to be generated, is assumed to be there."""

    pass


class _MLIRInputMixin:
    """Mixin providing a mlir_input property that finds the MLIR source in dependencies."""

    @property
    def mlir_input(self):
        result = next(
            (
                d
                for d in self.dependencies
                if isinstance(d, (SourceArtifact, PythonGeneratedMLIRArtifact))
            ),
            None,
        )
        if result is None:
            raise ValueError(
                f"No MLIR source artifact found in dependencies of {self.filename}"
            )
        return result


class FullElfArtifact(_MLIRInputMixin, CompilationArtifact):
    def __init__(
        self,
        filename: str,
        mlir_input: CompilationArtifact,
        dependencies: list[CompilationArtifact],
    ) -> None:
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)


class XclbinArtifact(_MLIRInputMixin, CompilationArtifact):
    def __init__(
        self,
        filename: str,
        mlir_input: CompilationArtifact,
        dependencies: list[CompilationArtifact],
        kernel_name: str = "MLIR_AIE",
        extra_flags: list[str] | None = None,
        xclbin_input: XclbinArtifact | None = None,
    ) -> None:
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.kernel_name = kernel_name
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.xclbin_input = xclbin_input


class InstsBinArtifact(_MLIRInputMixin, CompilationArtifact):
    def __init__(
        self,
        filename: str,
        mlir_input: CompilationArtifact,
        dependencies: list[CompilationArtifact],
        extra_flags: list[str] | None = None,
    ) -> None:
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []


class KernelObjectArtifact(CompilationArtifact):
    def __init__(
        self,
        filename: str,
        dependencies: list[CompilationArtifact],
        extra_flags: list[str] | None = None,
        rename_symbols: dict[str, str] | None = None,
        prefix_symbols: str | None = None,
    ) -> None:
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.rename_symbols = rename_symbols if rename_symbols is not None else {}
        self.prefix_symbols = prefix_symbols


class KernelArchiveArtifact(CompilationArtifact):
    """A static archive (.a) bundling one or more KernelObjectArtifacts."""

    pass


class PythonGeneratedMLIRArtifact(CompilationArtifact):
    def __init__(
        self,
        filename: str,
        generator: DesignGenerator,
    ) -> None:
        self.generator = generator
        super().__init__(filename, dependencies=[SourceArtifact(generator.source_path)])


# Compilation Command
# ##########################################################################


class CompilationCommand(ABC):
    """An abstraction for anything that can be executed to physically produce artifacts."""

    @abstractmethod
    def run(self) -> bool:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class ShellCompilationCommand(CompilationCommand):
    def __init__(
        self,
        command: list[str],
        cwd: str | None = None,
        env: dict[str, str] | str = "copy",
    ) -> None:
        self.command = command
        self.cwd = cwd
        if env == "copy":
            env = os.environ.copy()
        self.env = env

    def run(self) -> bool:
        result = subprocess.run(
            self.command,
            capture_output=True,
            text=True,
            cwd=self.cwd,
            env={**self.env, "PYTHONUNBUFFERED": "1"},
        )
        if result.returncode != 0:
            print("Return code: ", result.returncode)
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
        return result.returncode == 0

    def __repr__(self) -> str:
        return f"Shell({' '.join(self.command)})"


class PythonCallbackCompilationCommand(CompilationCommand):
    def __init__(self, callback: Callable[[], Any]) -> None:
        self.callback = callback

    def run(self) -> bool:
        result = self.callback()
        return bool(result) if result is not None else True

    def __repr__(self) -> str:
        return f"PythonCallback({self.callback})"


# Compilation Rules
# ##########################################################################


class CompilationRule(ABC):
    """A compilation rule is applied to a artifact graph, producing compilation commands and a transformed artifact graph."""

    @abstractmethod
    def matches(self, artifact: CompilationArtifactGraph) -> bool:
        """Return true if this rule can be applied to any artifact in the artifact graph."""
        pass

    @abstractmethod
    def compile(self, artifacts: CompilationArtifactGraph) -> list[CompilationCommand]:
        """Apply this rule to the artifact graph, returning compilation commands. This should modify the artifact graph in-place to reflect the newly generated artifacts."""
        pass


class GenerateMLIRFromPythonCompilationRule(CompilationRule):
    def matches(self, graph):
        return any(graph.get_worklist(PythonGeneratedMLIRArtifact))

    def compile(self, graph):
        """Generate MLIR from a Python callback that uses the MLIR bindings"""
        commands = []
        worklist = graph.get_worklist(PythonGeneratedMLIRArtifact)
        for artifact in worklist:
            new_artifact = SourceArtifact(artifact.filename)
            callback = partial(self.generate_mlir, new_artifact, artifact.generator)
            commands.append(PythonCallbackCompilationCommand(callback))
            new_artifact.available = True
            graph.replace(artifact, new_artifact)
        return commands

    @staticmethod
    def generate_mlir(output_artifact, generator):
        mlir_code = generator()
        with open(output_artifact.filename, "w") as f:
            f.write(mlir_code)


class AieccCompilationRule(CompilationRule):
    def __init__(
        self, build_dir, peano_dir, mlir_aie_dir, use_chess=False, *args, **kwargs
    ):
        self.build_dir = build_dir
        self.aiecc_path = Path(mlir_aie_dir) / "bin" / "aiecc"
        self.peano_dir = peano_dir
        self.use_chess = use_chess
        super().__init__(*args, **kwargs)


class AieccFullElfCompilationRule(AieccCompilationRule):
    def matches(self, graph):
        return any(graph.get_worklist(FullElfArtifact))

    def compile(self, graph):
        worklist = graph.get_worklist(FullElfArtifact)
        commands = []

        for artifact in worklist:
            compile_cmd = [
                str(self.aiecc_path),
                "-v",
                "-j1",
                "--no-compile-host",
            ]
            if self.use_chess:
                compile_cmd += [
                    "--xchesscc",
                    "--xbridge",
                ]
            else:
                compile_cmd += [
                    "--no-xchesscc",
                    "--no-xbridge",
                    "--peano",
                    str(self.peano_dir),
                ]
            compile_cmd += [
                "--expand-load-pdis",
                "--generate-full-elf",
                "--full-elf-name",
                os.path.abspath(artifact.filename),
                os.path.abspath(artifact.mlir_input.filename),
            ]
            commands.append(
                ShellCompilationCommand(compile_cmd, cwd=str(self.build_dir))
            )
            artifact.available = True

        return commands


class AieccXclbinInstsCompilationRule(AieccCompilationRule):
    def matches(self, graph):
        return any(graph.get_worklist((XclbinArtifact, InstsBinArtifact)))

    def compile(self, graph):
        # If there are both xclbin and insts.bin targets based on the same source MLIR code, we can combine them into one single `aiecc.py` invocation.
        mlir_sources = set()
        mlir_sources_to_xclbins = {}
        mlir_sources_to_insts = {}
        worklist = graph.get_worklist((XclbinArtifact, InstsBinArtifact))
        for artifact in worklist:
            mlir_dependency = artifact.mlir_input
            mlir_sources.add(mlir_dependency)
            if isinstance(artifact, XclbinArtifact):
                mlir_sources_to_xclbins.setdefault(mlir_dependency, []).append(artifact)
            elif isinstance(artifact, InstsBinArtifact):
                mlir_sources_to_insts.setdefault(mlir_dependency, []).append(artifact)

        commands = []
        # Now we know for each mlir source if we need to generate an xclbin, an insts.bin or both for it
        for mlir_source in mlir_sources:
            compile_cmd = [
                str(self.aiecc_path),
                "-v",
                "-j1",
                "--no-compile-host",
            ]
            if self.use_chess:
                compile_cmd += [
                    "--xchesscc",
                    "--xbridge",
                ]
            else:
                compile_cmd += [
                    "--no-xchesscc",
                    "--no-xbridge",
                    "--peano",
                    str(self.peano_dir),
                ]
            compile_cmd += [
                "--dynamic-objFifos",
            ]
            do_compile_xclbin = mlir_source in mlir_sources_to_xclbins
            do_compile_insts_bin = mlir_source in mlir_sources_to_insts
            if do_compile_xclbin:
                first_xclbin = mlir_sources_to_xclbins[mlir_source][
                    0
                ]  # TODO: this does not handle the case of multiple xclbins with different kernel names or flags from the same MLIR
                compile_cmd += first_xclbin.extra_flags + [
                    "--aie-generate-xclbin",
                    "--xclbin-name=" + os.path.abspath(first_xclbin.filename),
                    "--xclbin-kernel-name=" + first_xclbin.kernel_name,
                ]
                if first_xclbin.xclbin_input is not None:
                    compile_cmd += [
                        "--xclbin-input="
                        + os.path.abspath(first_xclbin.xclbin_input.filename)
                    ]
            if do_compile_insts_bin:
                first_insts_bin = mlir_sources_to_insts[mlir_source][
                    0
                ]  # TODO: this does not handle the case of multiple insts.bins with different flags from the same MLIR
                if not do_compile_xclbin:
                    compile_cmd += ["--no-compile"]
                compile_cmd += first_insts_bin.extra_flags + [
                    "--aie-generate-npu-insts",
                    "--npu-insts-name=" + os.path.abspath(first_insts_bin.filename),
                ]
            compile_cmd += [os.path.abspath(mlir_source.filename)]

            commands.append(
                ShellCompilationCommand(compile_cmd, cwd=str(self.build_dir))
            )

            # There may be multiple targets that require an xclbin/insts.bin from the same MLIR with different names; copy them
            for sources_to in [mlir_sources_to_xclbins, mlir_sources_to_insts]:
                if sources_to.get(mlir_source, [])[1:]:
                    copy_src = sources_to[mlir_source][0]
                    for copy_dest in sources_to[mlir_source][1:]:
                        commands.append(
                            ShellCompilationCommand(
                                ["cp", copy_src.filename, copy_dest.filename]
                            )
                        )

        # Update graph
        for artifact in worklist:
            artifact.available = True

        return commands


def _find_tool(name, peano_dir, mlir_aie_dir):
    """Locate an LLVM tool by name, trying peano_dir, mlir_aie_dir, then system PATH."""
    candidates = [
        Path(peano_dir) / "bin" / name,
        Path(mlir_aie_dir) / "bin" / name,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    # Try versioned suffix for distros that install LLVM tools as e.g. llvm-objcopy-18
    for tool_name in [name, f"{name}-18"]:
        found = shutil.which(tool_name)
        if found:
            return found
    raise FileNotFoundError(
        f"{name} not found. Searched in: "
        + ", ".join(str(c) for c in candidates)
        + f", and system PATH (also tried {name}-18)"
    )


class KernelCompilationRule(CompilationRule):
    """Compile KernelObjectArtifacts using Peano (clang++) or xchesscc."""

    def __init__(self, peano_dir, mlir_aie_dir, use_chess=False, *args, **kwargs):
        self.peano_dir = peano_dir
        self.mlir_aie_dir = mlir_aie_dir
        self.use_chess = use_chess
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(artifacts.get_worklist(KernelObjectArtifact))

    def compile(self, artifacts):
        include_path = Path(self.mlir_aie_dir) / "include"
        worklist = artifacts.get_worklist(KernelObjectArtifact)
        commands = []

        kernel_dir = get_kernel_dir()
        runtime_lib_include_path = (
            Path(self.mlir_aie_dir) / "aie_runtime_lib" / kernel_dir.upper()
        )

        for artifact in worklist:
            if len(artifact.dependencies) < 1:
                raise RuntimeError(
                    "Expected at least one dependency (the C source code) for KernelObjectArtifact"
                )
            source_file = artifact.dependencies[0]
            if not isinstance(source_file, SourceArtifact):
                raise RuntimeError(
                    "Expected KernelObject dependency to be a C source file"
                )

            if self.use_chess:
                wrapper_path = Path(self.mlir_aie_dir) / "bin" / "xchesscc_wrapper"
                cmd = (
                    [
                        str(wrapper_path),
                        kernel_dir,  # e.g. "aie2" or "aie2p"
                        f"-I{str(include_path)}",
                        f"-I{str(runtime_lib_include_path)}",
                    ]
                    + artifact.extra_flags
                    + ["-c", source_file.filename, "-o", artifact.filename]
                )
            else:
                clang_path = Path(self.peano_dir) / "bin" / "clang++"
                target = f"{kernel_dir}-none-unknown-elf"
                cmd = (
                    [
                        str(clang_path),
                        "-O2",
                        "-std=c++20",
                        f"--target={target}",
                        "-Wno-parentheses",
                        "-Wno-attributes",
                        "-Wno-macro-redefined",
                        "-Wno-empty-body",
                        "-Wno-missing-template-arg-list-after-template-kw",
                        f"-I{str(include_path)}",
                        f"-I{str(runtime_lib_include_path)}",
                    ]
                    + artifact.extra_flags
                    + ["-c", source_file.filename, "-o", artifact.filename]
                )

            commands.append(ShellCompilationCommand(cmd))
            if artifact.rename_symbols:
                commands.extend(self._rename_symbols(artifact))
            if artifact.prefix_symbols:
                commands.extend(self._prefix_symbols(artifact, artifact.prefix_symbols))
            artifact.available = True

        return commands

    def _find_tool(self, name):
        return _find_tool(name, self.peano_dir, self.mlir_aie_dir)

    def _rename_symbols(self, artifact):
        objcopy_path = self._find_tool("llvm-objcopy")
        cmd = [objcopy_path]
        for old_sym, new_sym in artifact.rename_symbols.items():
            cmd += [
                "--redefine-sym",
                f"{old_sym}={new_sym}",
            ]
        cmd += [artifact.filename]
        return [ShellCompilationCommand(cmd)]

    def _prefix_symbols(self, artifact, prefix):
        objcopy_path = self._find_tool("llvm-objcopy")
        nm_path = self._find_tool("llvm-nm")
        symbol_map_file = artifact.filename + ".symbol_map"

        # Extract defined symbols and create symbol map
        nm_cmd = [
            "sh",
            "-c",
            f"{nm_path} --defined-only --extern-only {artifact.filename} | "
            f"awk '{{print $3 \" {prefix}\" $3}}' > {symbol_map_file}",
        ]

        # Apply the renaming using the symbol map
        objcopy_cmd = [
            objcopy_path,
            "--redefine-syms=" + symbol_map_file,
            artifact.filename,
        ]

        return [ShellCompilationCommand(nm_cmd), ShellCompilationCommand(objcopy_cmd)]


class ArchiveCompilationRule(CompilationRule):
    """Bundle KernelObjectArtifacts into a static archive (.a)."""

    def __init__(self, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        self.mlir_aie_dir = mlir_aie_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(artifacts.get_worklist(KernelArchiveArtifact))

    def compile(self, artifacts):
        ar_path = _find_tool("llvm-ar", self.peano_dir, self.mlir_aie_dir)
        worklist = artifacts.get_worklist(KernelArchiveArtifact)
        commands = []
        for artifact in worklist:
            object_files = [
                dep.filename
                for dep in artifact.dependencies
                if isinstance(dep, KernelObjectArtifact)
            ]
            cmd = [str(ar_path), "rcs", artifact.filename] + object_files
            commands.append(ShellCompilationCommand(cmd))
            artifact.available = True
        return commands
