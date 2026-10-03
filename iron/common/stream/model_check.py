# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Check stream-dse's estimates of the generated operators against the NPU.

``sweep OUT [--operators mha swiglu] [--trace]`` times stream's choice and every candidate
per point into ``OUT/records.jsonl``; ``report OUT`` compares the choice, latency estimates
and (traced) memory tile traffic with the measurements."""

import argparse
import fcntl
import hashlib
import json
import math
import os
import re
from contextlib import contextmanager
from pathlib import Path

# The NPU2 array clock the cycles stream counts run at.
AIE_CLOCK_HZ = 1.8e9
# Back-to-back dispatches before and during a measurement: the platform clocks down within
# a millisecond of the NPU going idle, so each measurement runs this long without a gap.
WARM_S, TIMED_S, MIN_ITERS = 0.2, 0.5, 8
# Traced runs: one port selection per direction, each watching every channel of a memory
# tile in that direction.
MEMTILE_CHANNELS = 6
TRACE_SIZE = 8 << 20
TRACE_PORTS = tuple(
    ",".join(f"{direction}:{channel}" for channel in range(MEMTILE_CHANNELS))
    for direction in ("S2MM", "MM2S")
)
# Traced builds take fewer heads, so the trace of a long sequence fits its buffer; each trace
# is compared with stream's estimate of the design it traced.
TRACE_HEADS = 2
# What a memory-tile DMA channel moves a traced cycle it runs, measured on an element-wise
# design whose bytes through each memory tile are known.
DMA_BITS_PER_CYCLE = 64
# The memory tile traced: the first column's, which every design of the array uses.
TRACE_TILES = ((0, 1),)
RECORDS = "records.jsonl"
# The smallest one-design operator over every column, as the generated designs are, whose
# latency is what every dispatch costs on top of the cycles stream counts.
DISPATCH = dict(operator="dispatch", point={}, candidate={}, ports=None)


def points(operator):
    """The sweep of one operator, as constructor keyword arguments."""
    if operator == "mha":
        return [
            dict(seq_len=s, d_head=64, heads=32, flash=True)
            for s in (64, 128, 256, 512, 1024, 2048, 4096, 8192)
        ]
    return [
        dict(seq_len=s, embedding_dim=e, hidden_dim=h)
        for e, h in ((1024, 4096), (2048, 8192))
        for s in (256, 512, 1024, 2048, 4096)
    ]


def candidates(operator):
    """Stream's own choice first, then every design it chooses between."""
    if operator == "mha":
        from iron.common.stream.kernel_library import flash_blocks

        return [{}] + [dict(query_block=b) for b in flash_blocks()]
    from iron.operators.swiglu_prefill_stream.stream_design import (
        GEMM_BLOCKS,
        LAYER_BY_LAYER,
    )

    return [{}] + [
        dict(k=k, gemm_block=block)
        for k in (1, LAYER_BY_LAYER)
        for block in GEMM_BLOCKS
    ]


def build(operator, point, candidate, build_dir):
    from iron.common import AIEContext

    context = AIEContext(build_dir=str(build_dir))
    if operator == DISPATCH["operator"]:
        from iron.common.sequence import OperatorSequence
        from iron.common.stream.hardware import array
        from iron.operators.relu.op import ReLU

        columns = array().num_columns
        relu = ReLU(
            size=1024 * columns,
            num_aie_columns=columns,
            num_channels=1,
            tile_size=1024,
            context=context,
        )
        # Dispatched as the generated operators are: a sequence of one design.
        return OperatorSequence(
            name="dispatch_floor",
            runlist=[(relu, "x", "y")],
            input_args=["x"],
            output_args=["y"],
            context=context,
        )
    if operator == "mha":
        from iron.operators.mha_prefill_stream.op import MHAPrefillStream

        return MHAPrefillStream(**point, **candidate, context=context)
    from iron.operators.swiglu_prefill_stream.op import SwiGLUPrefillStream

    return SwiGLUPrefillStream(**point, **candidate, context=context)


@contextmanager
def _environment(**values):
    saved = {name: os.environ.get(name) for name in values}
    os.environ.update({name: str(value) for name, value in values.items()})
    try:
        yield
    finally:
        for name, value in saved.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value


def _deploy(op):
    """Compile ``op`` and return its callable, with stream's estimate and its design."""
    from iron.common.stream.runner import ESTIMATE

    op.compile()
    run = op.get_callable()
    root = op.runlist[0][0].design_root()
    designs = sorted(root.glob("group_*/codegen/final.mlir"))
    digest = hashlib.sha256(b"".join(path.read_bytes() for path in designs))
    return run, {
        "estimate": json.loads((root / ESTIMATE).read_text()),
        "design": str(root),
        "digest": digest.hexdigest(),
    }


def measure(run):
    """The fastest and median of back-to-back dispatches of a sequence's callable. Its run on
    the NPU is timed alone: syncing the output back to the host after every dispatch costs
    time stream does not price, which grows with the output, and leaves the NPU idle."""
    from aie.utils.benchmark import run_iters

    run()
    once = run.last_elapsed
    stats = run_iters(
        run._run,
        warmup=math.ceil(WARM_S / once),
        iters=max(MIN_ITERS, math.ceil(TIMED_S / once)),
    ).e2e
    return {"min": stats.min_us, "median": stats.median_us}


def trace(op, out):
    """Per design of ``op``: the groups that run it, and each traced tile's running cycles
    per event and traced span over all their runs."""
    from iron.common.tracing_utils import dump_traces

    run, record = _deploy(op)
    run()
    _, design_of = op.unique_designs()
    design = [design_of[id(child)] for child, *_ in op.runlist]
    designs = []
    for path in dump_traces(run, op.name, out_dir=out / "traces", summary=False):
        events = json.loads(Path(path).read_text())
        events = events["traceEvents"] if isinstance(events, dict) else events
        # A design's trace is named after the runlist step that first runs it.
        first = int(re.search(rf"{re.escape(op.name)}_(\d+)_", Path(path).name)[1])
        tiles = {
            label: _running(e for e in events if e.get("pid") == pid)
            for pid, label in (
                (e["pid"], e["args"]["name"])
                for e in events
                if e.get("name") == "process_name"
            )
        }
        groups = [
            child.group_index
            for (child, *_), shared in zip(op.runlist, design)
            if shared == design[first]
        ]
        designs.append({"groups": groups, "tiles": tiles})
    return record | {"traced": designs}


def _running(events):
    marks = sorted((e["ts"], e["ph"], e["name"]) for e in events if e["ph"] in "BE")
    busy, opened = {}, {}
    for ts, phase, name in marks:
        if phase == "B":
            opened[name] = ts
        elif name in opened:
            busy[name] = busy.get(name, 0) + ts - opened.pop(name)
    return {"busy": busy, "span": marks[-1][0] - marks[0][0] if marks else 0}


def _key(record):
    return json.dumps([record[k] for k in ("operator", "point", "candidate", "ports")])


def _jobs(operators, traced):
    yield dict(DISPATCH)
    for operator in operators:
        for point in points(operator):
            for candidate in candidates(operator):
                # A design is traced as stream builds it, which is what it priced the ports of.
                tracing = TRACE_PORTS if traced and not candidate else ()
                for ports in (None, *tracing):
                    yield dict(
                        operator=operator, point=point, candidate=candidate, ports=ports
                    )


def _run(job, out):
    build_dir = out / "build" / re.sub(r"\W+", "_", _key(job))
    if job["operator"] == DISPATCH["operator"]:
        op = build(job["operator"], {}, {}, build_dir)
        op.compile()
        return {"measured_us": measure(op.get_callable())}
    if job["ports"] is None:
        op = build(job["operator"], job["point"], job["candidate"], build_dir)
        run, record = _deploy(op)
        return record | {"measured_us": measure(run)}
    point = job["point"] | ({"heads": TRACE_HEADS} if "heads" in job["point"] else {})
    with _environment(
        IRON_TRACE_SIZE=TRACE_SIZE,
        IRON_TRACE_NTILES=len(TRACE_TILES),
        IRON_TRACE_TILES=";".join(f"{c},{r}" for c, r in TRACE_TILES),
        IRON_TRACE_PORTS=job["ports"],
    ):
        op = build(job["operator"], point, job["candidate"], build_dir)
        return trace(op, out)


def sweep(out, operators, traced):
    import aie.utils as aie_utils

    import iron.common.stream.runner as runner

    out.mkdir(parents=True, exist_ok=True)
    runner.OUTPUT_ROOT = str(out / "designs")
    done = {_key(r) for r in load(out)}
    with open(out / RECORDS, "a") as records:
        # A second sweep into the same directory would share its builds and the NPU.
        fcntl.flock(records, fcntl.LOCK_EX | fcntl.LOCK_NB)
        for job in _jobs(operators, traced):
            if _key(job) in done:
                continue
            try:
                job |= _run(job, out)
            except Exception as error:
                job["error"] = f"{type(error).__name__}: {error}"
            finally:
                aie_utils.DefaultNPURuntime.cleanup()
            records.write(json.dumps(job) + "\n")
            records.flush()


def load(out):
    path = out / RECORDS
    return (
        [json.loads(line) for line in path.read_text().splitlines()]
        if path.exists()
        else []
    )


def predicted_us(record, dispatch_us):
    """stream's estimate in microseconds, every group included, on top of what a
    dispatch costs."""
    return record["estimate"]["cycles"] / AIE_CLOCK_HZ * 1e6 + dispatch_us


def _label(candidate):
    return ",".join(f"{k}={v}" for k, v in candidate.items()) or "stream"


def _shape(record):
    point = {k: v for k, v in record["point"].items() if k != "seq_len"}
    return f"{record['operator']} " + ",".join(f"{k}={v}" for k, v in point.items())


def _residual(record):
    measured = record["measured_us"]["min"]
    return (record["predicted_us"] - measured) / measured * 100


def _choices(timed):
    """Per point: stream's own record, the candidate whose design it is, and the fastest one."""
    by_point = {}
    for record in timed:
        by_point.setdefault((_shape(record), record["point"]["seq_len"]), []).append(
            record
        )
    for (shape, seq), records in sorted(by_point.items()):
        own = next((r for r in records if not r["candidate"]), None)
        explicit = [r for r in records if r["candidate"]]
        if own is None or not explicit:
            continue
        fastest = min(explicit, key=lambda r: r["measured_us"]["min"])
        priced = min(explicit, key=lambda r: r["predicted_us"])
        same = next((r for r in explicit if r["digest"] == own["digest"]), None)
        yield shape, seq, own, same, priced, fastest


def _port_rows(traced):
    """Per traced memory tile direction: the bits stream moves through it a run, and the
    bandwidth that is over the run, against the traced ones."""
    import yaml

    from iron.common.stream.runner import ACCELERATOR

    coordinates = yaml.safe_load(Path(ACCELERATOR).read_text())["core_coordinates"]
    core_at = {tuple(xy): core for core, xy in coordinates.items()}
    for record in traced:
        slots = record["ports"].split(",")
        for design in record["traced"]:
            # Every run of the design is an entry of the runlist.
            group, runs = design["groups"][0], len(design["groups"])
            view = record["estimate"]["groups"][f"group_{group}"]
            latency = view["latency"]
            interval = latency["per_iteration"] - latency["overlap_between_iterations"]
            steady = (
                latency["total"] - latency.get("fill", 0) - latency["per_iteration"]
            )
            iterations = 1 + steady / interval
            for label, activity in design["tiles"].items():
                row, col = map(int, re.search(r"tile(\d+),(\d+)", label).groups())
                core = core_at[(col, row)]
                for direction in sorted({slot.split(":")[0] for slot in slots}):
                    modelled = next(
                        r
                        for r in view["port_activity"]
                        if r["kind"] == "memory_port"
                        and r["core_ids"] == [core]
                        and r["port"] == f"dma.{direction.lower()}"
                    )
                    cycles = sum(
                        activity["busy"].get(f"PORT_RUNNING_{i}", 0)
                        for i, slot in enumerate(slots)
                        if slot.startswith(direction)
                    )
                    modelled_bits = modelled["bits_per_iteration"] * iterations
                    traced_bits = cycles * DMA_BITS_PER_CYCLE / runs
                    yield {
                        "shape": _shape(record),
                        "seq": record["point"]["seq_len"],
                        "candidate": _label(record["candidate"]),
                        "group": "+".join(map(str, sorted(set(design["groups"])))),
                        "tile": f"({col},{row}) {direction}",
                        "modelled_bits": modelled_bits,
                        "traced_bits": traced_bits,
                        "modelled_bw": modelled_bits / latency["total"],
                        "traced_bw": traced_bits * runs / activity["span"],
                        "modelled_cycles": latency["total"],
                        "traced_cycles": activity["span"],
                        "runs": runs,
                    }


def _plots(out, timed, ports):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    shapes = sorted({_shape(r) for r in timed})
    figure, axes = plt.subplots(
        2, len(shapes), figsize=(6 * len(shapes), 8), squeeze=False
    )
    for column, shape in enumerate(shapes):
        records = [r for r in timed if _shape(r) == shape]
        for label in sorted({_label(r["candidate"]) for r in records}):
            series = sorted(
                (r for r in records if _label(r["candidate"]) == label),
                key=lambda r: r["point"]["seq_len"],
            )
            seqs = [r["point"]["seq_len"] for r in series]
            line = axes[0][column].plot(
                seqs, [r["measured_us"]["min"] for r in series], "o-", label=label
            )[0]
            axes[0][column].plot(
                seqs, [r["predicted_us"] for r in series], "x--", color=line.get_color()
            )
            axes[1][column].plot(
                seqs, [_residual(r) for r in series], "o-", label=label
            )
        axes[0][column].set(
            title=f"{shape}: measured (o) and stream (x)",
            xscale="log",
            yscale="log",
            ylabel="us",
        )
        axes[1][column].axhspan(-10, 10, color="0.9")
        axes[1][column].set(
            xscale="log", xlabel="seq_len", ylabel="stream - measured (%)"
        )
        axes[0][column].legend(fontsize=7)
    figure.tight_layout()
    figure.savefig(out / "sweep.png", dpi=120)
    if ports:
        figure, axis = plt.subplots(figsize=(6, 6))
        modelled = [p["modelled_bits"] for p in ports]
        traced = [p["traced_bits"] for p in ports]
        axis.loglog(modelled, traced, "o", alpha=0.6)
        bounds = [min(modelled + traced), max(modelled + traced)]
        axis.loglog(bounds, bounds, "k--", linewidth=0.8)
        axis.set(
            xlabel="stream bits per run",
            ylabel="traced bits per run",
            title="memory-tile DMA traffic",
        )
        figure.tight_layout()
        figure.savefig(out / "ports.png", dpi=120)


def report(out):
    records = load(out)
    good = [r for r in records if "error" not in r]
    dispatch_us = next(
        (
            r["measured_us"]["min"]
            for r in good
            if r["operator"] == DISPATCH["operator"]
        ),
        0.0,
    )
    timed = [
        r | {"predicted_us": predicted_us(r, dispatch_us)}
        for r in good
        if r["ports"] is None and r["operator"] != DISPATCH["operator"]
    ]
    ports = list(_port_rows([r for r in good if r["ports"] is not None]))
    lines = ["# stream estimate against the NPU", "", "## Latency", ""]
    lines += [
        f"Each estimate includes the {dispatch_us:.1f} us one dispatch measured to cost.",
        "",
        "| shape | seq | candidate | stream (us) | measured (us) | residual |",
        "|---|---|---|---|---|---|",
    ]
    for r in sorted(
        timed, key=lambda r: (_shape(r), r["point"]["seq_len"], _label(r["candidate"]))
    ):
        lines.append(
            f"| {_shape(r)} | {r['point']['seq_len']} | {_label(r['candidate'])} | "
            f"{r['predicted_us']:.1f} | {r['measured_us']['min']:.1f} | {_residual(r):+.1f}% |"
        )
    lines += [
        "",
        "## Choice",
        "",
        "| shape | seq | stream built | priced fastest | measured fastest | lost |",
    ]
    lines.append("|---|---|---|---|---|---|")
    for shape, seq, own, same, priced, fastest in _choices(timed):
        lost = (own["measured_us"]["min"] - fastest["measured_us"]["min"]) / fastest[
            "measured_us"
        ]["min"]
        built = _label(same["candidate"]) if same else "a design no candidate built"
        lines.append(
            f"| {shape} | {seq} | {built} | {_label(priced['candidate'])} | "
            f"{_label(fastest['candidate'])} | {lost * 100:+.1f}% |"
        )
    if ports:
        lines += [
            "",
            "## Memory-tile DMA",
            "",
            "| shape | seq | candidate | group | port | stream bits | traced bits | ratio | stream b/cc | traced b/cc |",
        ]
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for p in ports:
            ratio = (
                p["traced_bits"] / p["modelled_bits"]
                if p["modelled_bits"]
                else float("nan")
            )
            lines.append(
                f"| {p['shape']} | {p['seq']} | {p['candidate']} | {p['group']} | {p['tile']} | "
                f"{p['modelled_bits']:.0f} | {p['traced_bits']:.0f} | {ratio:.2f} | "
                f"{p['modelled_bw']:.1f} | {p['traced_bw']:.1f} |"
            )
    if ports:
        lines += [
            "",
            "## Group latency, traced",
            "",
            "| shape | seq | candidate | group | stream (cycles) | traced (cycles) | residual |",
            "|---|---|---|---|---|---|---|",
        ]
        # A traced build dispatches each run on its own, so only a design that runs once
        # spans what the timed build does.
        groups = {
            (p["shape"], p["seq"], p["candidate"], p["group"]): p
            for p in ports
            if p["runs"] == 1
        }
        for (shape, seq, candidate, group), p in groups.items():
            residual = (p["modelled_cycles"] - p["traced_cycles"]) / p["traced_cycles"]
            lines.append(
                f"| {shape} | {seq} | {candidate} | {group} | {p['modelled_cycles']:.0f} | "
                f"{p['traced_cycles']:.0f} | {residual * 100:+.1f}% |"
            )
    failed = [r for r in records if "error" in r]
    if failed:
        lines += ["", "## Not deployed", ""]
        lines += [
            f"- {_shape(r)} seq {r['point'].get('seq_len', '-')} {_label(r['candidate'])}: "
            f"{r['error'].splitlines()[0]}"
            for r in failed
        ]
    (out / "report.md").write_text("\n".join(lines) + "\n")
    _plots(out, timed, ports)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("sweep")
    run.add_argument("out", type=Path)
    run.add_argument(
        "--operators", nargs="+", default=["mha", "swiglu"], choices=["mha", "swiglu"]
    )
    run.add_argument("--trace", action="store_true")
    commands.add_parser("report").add_argument("out", type=Path)
    args = parser.parse_args()
    if args.command == "sweep":
        sweep(args.out, args.operators, args.trace)
    report(args.out)


if __name__ == "__main__":
    main()
