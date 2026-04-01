# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This file implements a simple Python-based build system. You specify what you
want to compile (*artifacts*) through subclasses of `CompilationArtifact`.
Multiple `CompilationArtifacts` form a `CompilationArtifactGraph`. Each artifact
can have a list (subgraph) of depenencies of other artifacts that it relies on.
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

from abc import ABC, abstractmethod
from collections import deque
from pathlib import Path
import os.path
import shutil
import zlib
import logging
import subprocess
import importlib.util
from contextlib import nullcontext
from aie.extras.context import mlir_mod_ctx
import sys

__all__ = [
    "plan",
    "execute",
    "compile",
    "CompilationArtifactGraph",
    "CompilationArtifact",
    "SourceArtifact",
    "FullElfArtifact",
    "XclbinArtifact",
    "InstsBinArtifact",
    "KernelObjectArtifact",
    "PythonGeneratedMLIRArtifact",
    "CompilationCommand",
    "ShellCompilationCommand",
    "PythonCallbackCompilationCommand",
    "CompilationRule",
    "GenerateMLIRFromPythonCompilationRule",
    "AieccCompilationRule",
    "AieccFullElfCompilationRule",
    "AieccXclbinInstsCompilationRule",
    "PeanoCompilationRule",
]

# Global Functions
# ##########################################################################


def plan(rules, graph, _seen_unavailable=None):
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


def execute(plan_steps):
    for rule, commands in plan_steps:
        logging.debug(f"Applying rule: {rule.__class__.__name__}")
        for command in commands:
            logging.debug(f"  Executing command: {command}")
            success = command.run()
            if not success:
                raise RuntimeError(f"Command failed: {command}")


def compile(rules, artifacts, build_dir="build", dry_run=False):
    if not os.path.exists(build_dir) and not dry_run:
        os.makedirs(build_dir)
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
    def __init__(self, artifacts=None):
        self.artifacts = artifacts if artifacts is not None else []

    def __repr__(self):
        def format_artifact(artifact, indent=0):
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

    def __iter__(self):
        return iter(self.artifacts)

    def __len__(self):
        return len(self.artifacts)

    def __getitem__(self, index):
        return self.artifacts[index]

    def dfs(self):
        return self._traverse(True)

    def bfs(self):
        return self._traverse(False)

    def _traverse(self, dfs):
        visited = set()
        todo = deque(self.artifacts)
        while todo:
            artifact = todo.pop() if dfs else todo.popleft()
            if artifact in visited:
                continue
            visited.add(artifact)
            todo.extend(artifact.dependencies)
            yield artifact

    def replace(self, old_artifact, new_artifact):
        for i, artifact in enumerate(self.artifacts):
            if artifact == old_artifact:
                self.artifacts[i] = new_artifact
            else:
                artifact.dependencies.replace(old_artifact, new_artifact)
        return self

    def populate_availability_from_filesystem(self):
        for artifact in self.artifacts:
            artifact.dependencies.populate_availability_from_filesystem()
            artifact.available = artifact.is_available_in_filesystem()

    def get_worklist(self, kind):
        """Return a list of artifacts of the given kind that can be built in the next step (dependencies available)."""
        return [
            artifact
            for artifact in self.bfs()
            if isinstance(artifact, kind)
            and not artifact.is_available()
            and artifact.dependencies_available()
        ]

    def move_artifacts(self, new_root):
        """Make all artifacts paths point into a build directory"""
        for artifact in self.bfs():
            if not os.path.isabs(artifact.filename):
                artifact.filename = str(Path(new_root) / Path(artifact.filename).name)

    def add(self, artifact):
        self.artifacts.append(artifact)


# Compilation Artifacts
# ##########################################################################


class CompilationArtifact(ABC):
    def __init__(self, filename, dependencies=None, available=False):
        self.filename = str(filename)
        self.dependencies: CompilationArtifactGraph = CompilationArtifactGraph(
            artifacts=dependencies if dependencies is not None else []
        )
        self.available = available

    def __repr__(self):
        return f"{self.__class__.__name__}({self.filename})"

    def is_available(self):
        """'Conceptual' availability: during a dry-run or in the planning stage, available may be True even if the underlying file does not exist yet."""
        # If any of our dependencies' dependencies are outdated, this artifact is also outdated
        return self.available and self.dependencies_available()

    def dependencies_available(self):
        return all(d.is_available() for d in self.dependencies)

    def is_available_in_filesystem(self):
        """'Real' availability: checks if the underlying file exists and is up-to-date with respect to dependencies."""
        if not os.path.exists(self.filename):
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


class FullElfArtifact(CompilationArtifact):
    def __init__(self, filename, mlir_input, dependencies):
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.mlir_input = mlir_input


class XclbinArtifact(CompilationArtifact):
    def __init__(
        self,
        filename,
        mlir_input,
        dependencies,
        kernel_name="MLIR_AIE",
        extra_flags=None,
        xclbin_input=None,
    ):
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.mlir_input = mlir_input
        self.kernel_name = kernel_name
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.xclbin_input = xclbin_input


class InstsBinArtifact(CompilationArtifact):
    def __init__(self, filename, mlir_input, dependencies, extra_flags=None):
        self.mlir_input = mlir_input
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []


class KernelObjectArtifact(CompilationArtifact):
    def __init__(
        self,
        filename,
        dependencies,
        extra_flags=None,
        rename_symbols=None,
        prefix_symbols=None,
    ):
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.rename_symbols = rename_symbols if rename_symbols is not None else {}
        self.prefix_symbols = prefix_symbols


class PythonGeneratedMLIRArtifact(CompilationArtifact):
    def __init__(
        self,
        filename,
        import_path,
        callback_fn,
        callback_args=None,
        callback_kwargs=None,
        requires_context=False,
    ):
        self.import_path = import_path
        self.callback_fn = callback_fn
        self.callback_args = callback_args if callback_args is not None else []
        self.callback_kwargs = callback_kwargs if callback_kwargs is not None else {}
        self.requires_context = requires_context
        dependencies = [SourceArtifact(import_path)]
        super().__init__(filename, dependencies=dependencies)


# Compilation Command
# ##########################################################################


class CompilationCommand(ABC):
    """An abstraction for anything that can be executed to physically produce artifacts."""

    @abstractmethod
    def run(self) -> bool:
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ShellCompilationCommand(CompilationCommand):
    def __init__(self, command: list[str], cwd=None, env="copy"):
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
        if 0 != result.returncode:
            print("Return code: ", result.returncode)
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
        return 0 == result.returncode

    def __repr__(self):
        return f"Shell({' '.join(self.command)})"


class PythonCallbackCompilationCommand(CompilationCommand):
    def __init__(self, callback):
        self.callback = callback

    def run(self) -> bool:
        result = self.callback()
        return bool(result) if result is not None else True

    def __repr__(self):
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
            # To make Python capture variables in this closure by value, not by reference, use default arguments
            callback = lambda new_artifact=new_artifact, import_path=artifact.import_path, callback_fn=artifact.callback_fn, callback_args=artifact.callback_args, callback_kwargs=artifact.callback_kwargs, requires_context=artifact.requires_context: self.generate_mlir(
                new_artifact,
                import_path,
                callback_fn,
                callback_args,
                callback_kwargs,
                requires_context,
            )
            commands.append(PythonCallbackCompilationCommand(callback))
            new_artifact.available = True
            graph.replace(artifact, new_artifact)
        return commands

    @staticmethod
    def generate_mlir(
        output_artifact,
        import_path,
        callback_fn,
        callback_args=None,
        callback_kwargs=None,
        requires_context=False,
    ):
        # Import the Python source file
        spec = importlib.util.spec_from_file_location(
            Path(import_path).name, import_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # We only initiate an MLIR context if requested; otherwise, it is expected that the callback creates the context
        ctx_callback = lambda: (mlir_mod_ctx() if requires_context else nullcontext())
        with ctx_callback() as ctx:
            callback_function = getattr(module, callback_fn)
            mlir_code = callback_function(*callback_args, **callback_kwargs)
        # Stringify the generated MLIR
        if requires_context:
            mlir_code = str(ctx.module)
        else:
            mlir_code = str(mlir_code)

        with open(output_artifact.filename, "w") as f:
            f.write(mlir_code)


class AieccCompilationRule(CompilationRule, ABC):
    def __init__(self, build_dir, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.build_dir = build_dir
        self.aiecc_path = Path(mlir_aie_dir) / "bin" / "aiecc"
        self.peano_dir = peano_dir
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
                "--no-xchesscc",
                "--no-xbridge",
                "--peano",
                str(self.peano_dir),
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
                "--no-xchesscc",
                "--no-xbridge",
                "--peano",
                str(self.peano_dir),
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


class PeanoCompilationRule(CompilationRule):
    def __init__(self, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        self.mlir_aie_dir = mlir_aie_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(artifacts.get_worklist(KernelObjectArtifact))

    def compile(self, artifacts):
        clang_path = Path(self.peano_dir) / "bin" / "clang++"
        include_path = Path(self.mlir_aie_dir) / "include"
        worklist = artifacts.get_worklist(KernelObjectArtifact)
        commands = []
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
            for extra_dep in list(artifact.dependencies)[1:]:
                if not isinstance(extra_dep, SourceArtifact):
                    raise RuntimeError(
                        "Expected all KernelObject dependencies to be C source files"
                    )

            cmd = (
                [
                    str(clang_path),
                    "-O2",
                    "-std=c++20",
                    "--target=aie2p-none-unknown-elf",
                    "-Wno-parentheses",
                    "-Wno-attributes",
                    "-Wno-macro-redefined",
                    "-Wno-empty-body",
                    "-Wno-missing-template-arg-list-after-template-kw",
                    f"-I{str(include_path)}",
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
        """Locate an LLVM tool by name, trying peano_dir, mlir_aie_dir, then system PATH."""
        candidates = [
            Path(self.peano_dir) / "bin" / name,
            Path(self.mlir_aie_dir) / "bin" / name,
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

    def _rename_symbols(self, artifact):
        objcopy_path = self._find_tool("llvm-objcopy")
        cmd = [
            objcopy_path,
        ]
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
