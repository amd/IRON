# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Validate a candidate profile against a model's stock one, on real
weights: which fusions and packings are live in each compiled version, then
a decoder's own battery (bit identity of greedy logits over a prompt that
crosses a prefill chunk and ends in a partial one, KL against the model's
golden, and TTFT / decode tokens per second, stock and candidate
interleaved) or, for any other graph model (an encoder among them), each
changed version compared on its own tune points (``compare_graphs``): bit
identity within each output's bound, then latency, stock and candidate
interleaved. ``--bisect`` narrows a decoder's bit-identity mismatch to the
candidate's profile entries at fault, one version at a time.

``python -m iron.lm.validate <application> --checkpoint DIR --candidate
PROFILE_DIR``: ``<application>`` is dotted under ``iron.applications``
(``application_model``'s), ``PROFILE_DIR`` holds one ``<device>.json`` the
way a model's own ``profile`` directory does.
"""

import argparse
import dataclasses
import json
import statistics
from collections import Counter
from pathlib import Path
from typing import Any

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron import Profile
from iron.common.declare.profile import Version
from iron.common.graph.coded import CodedWeight
from iron.common.graph.compiled import CompiledGraph, _step_words, apply_profile
from iron.common.graph.fusion import fusions as graph_fusions
from iron.common.graph.record import Recording
from iron.common.image.link import FullELF, PerStep
from iron.common.image.packaging import plan, require_device
from iron.tune.autotune import Timed
from iron.tune.fusions import NotBitIdentical, compare_graphs
from iron.tune.measure import Timing

from .causal import CausalLM
from .generation import Sampler, accuracy, differing_steps, greedy_logits, kl_stats
from .model import Model
from .tune import application_model


def version_labels(model: Model) -> list[str]:
    """A label per ``model.shapes()``'s version, in compile order: ``decode``
    for no input, ``prompt`` for a chunk of ``ids``, ``placed`` for a
    tower's merged ids, else ``version<i>``.
    """
    labels = []
    for i, shape in enumerate(model.shapes()):
        if not shape:
            labels.append("decode")
        elif "placed" in shape:
            labels.append("placed")
        elif "ids" in shape:
            labels.append("prompt")
        else:
            labels.append(f"version{i}")
    return labels


def verify_live(label: str, model: Model) -> dict[str, dict[str, Any]]:
    """For each of ``model``'s compiled versions (``version_labels``): how
    many of its ``sequence.fusions`` are live, by kind, its design and
    fusion-device counts, packed groups and composition identity (a full
    ELF's), and ``images``, what it runs: the full ELF, or each distinct
    xclbin and instruction stream its steps dispatch in turn -- proof a
    profile's fusions and packings matched the live recording, not just
    that the profile file has entries.

    Raises:
        TypeError: A version is packaged neither as a full ELF nor as an
            xclbin per step.
        ValueError: ``model`` holds other than one compiled version per
            ``shapes()``: a caller compiled only some, or two shapes
            collided on one ``Recording.version``.
    """
    out = {}
    labels, versions = version_labels(model), model.versions.values()
    for version_label, version in zip(labels, versions, strict=True):
        fusions = version.sequence.fusions
        packaging = version.sequence.packaging
        if isinstance(packaging, FullELF):
            composition = packaging.composition
            assert (
                composition is not None
            ), "built once the full ELF links (Image.__init__)"
            n_designs, n_fusion_devices = (
                len(composition.designs),
                len(composition.fusions),
            )
            packed = [len(g) for g in composition.packing.groups]
            identity, images = composition.identity, [str(version.image)]
        elif isinstance(packaging, PerStep):
            fused = {f.steps[0] for f in fusions}
            links = sorted(packaging.step_links.items())
            n_designs = len(
                {
                    (l.kernel.xclbin_path, l.design.get_cache_entry().insts)
                    for i, l in links
                    if i not in fused
                }
            )
            n_fusion_devices, packed, identity = len(fusions), [], None
            images = list(
                dict.fromkeys(
                    f"{l.kernel.xclbin_path} {l.design.get_cache_entry().insts}"
                    for _, l in links
                )
            )
        else:
            raise TypeError(f"{version_label}: packaged as {type(packaging).__name__}")
        out[version_label] = {
            "n_fusions": len(fusions),
            "kinds": dict(Counter(f.kind.value for f in fusions)),
            "n_designs": n_designs,
            "n_fusion_devices": n_fusion_devices,
            "packed_groups": packed,
            "composition_identity": identity,
            "images": images,
            "coded_weights": sorted(
                w.name
                for w, _ in version.recording.weights.values()
                if isinstance(w, CodedWeight)
            ),
            "read_plain": dict(version.recording.read_plain),
        }
        print(
            f"[{label}] {version_label}: {len(fusions)} live fusions "
            f"{out[version_label]['kinds']}, {out[version_label]['n_designs']} designs + "
            f"{out[version_label]['n_fusion_devices']} fusion-devices, "
            f"packed groups {out[version_label]['packed_groups']}, "
            f"identity {out[version_label]['composition_identity']}, "
            f"{len(out[version_label]['coded_weights'])} coded weights, "
            f"{len(out[version_label]['read_plain'])} read plain"
        )
    return out


def changed_versions(stock_live: dict, candidate_live: dict) -> list[str]:
    """``version_labels`` whose candidate compile is not stock's image: its
    fusions, packings or tunables changed it.

    Raises:
        AssertionError: A version shares stock's compiled image while its
            live fusions or packed groups are not stock's.
    """
    changed = []
    for label, candidate_v in candidate_live.items():
        stock_v = stock_live[label]
        shared = stock_v["images"] == candidate_v["images"]
        assert not (
            shared
            and any(
                candidate_v[k] != stock_v[k]
                for k in ("n_fusions", "kinds", "packed_groups")
            )
        ), f"{label}: candidate and stock share one compiled image"
        if not shared:
            changed.append(label)
    return changed


def load_model(
    model_class: type[Model], checkpoint: Path, max_seq_len: int | None, profile
) -> Model:
    """``model_class.from_checkpoint(checkpoint)``, under ``profile`` (a
    directory, or None for the model's own), every version compiled as the
    device packages it (``Graph.compile``) and loaded.
    """
    model = model_class.from_checkpoint(checkpoint, max_seq_len=max_seq_len)
    if profile is not None:
        model.profile = profile
    model.load_versions()
    return model


def bit_identity(
    stock: CausalLM, candidate: CausalLM, tokens, num_tokens: int
) -> list[int]:
    """The steps (prompt and decode alike) at which ``candidate``'s greedy
    logits differ bitwise from ``stock``'s, over ``tokens`` and
    ``num_tokens`` decode steps after them.
    """
    stock.session.forget(0)
    candidate.session.forget(0)
    stock_logits = greedy_logits(stock, tokens, num_tokens)
    candidate_logits = greedy_logits(candidate, tokens, num_tokens)
    return differing_steps(candidate_logits, stock_logits)


def run_accuracy(model: CausalLM, tokens, num_tokens: int) -> tuple[dict, int]:
    """``model``'s KL against its own golden (``Model.cpu_reference``),
    teacher-forced over ``num_tokens`` steps from ``tokens``, and its
    top-1 mismatch count.
    """
    model.session.forget(0)
    results = accuracy(model, model.cpu_reference(), tokens, num_tokens)
    stats = kl_stats(results)
    mismatches = sum(not top1 for _, top1 in results)
    return stats, mismatches


def timed_round(model: CausalLM, tokens, num_tokens: int) -> tuple[float, float]:
    model.session.forget(0)
    model.generate(tokens, num_tokens, Sampler(temperature=0))
    assert model.stats is not None, "set once the last token is drawn"
    return model.stats.ttft, model.stats.tokens_per_s


def speed(
    stock: CausalLM, candidate: CausalLM, tokens, num_tokens: int, rounds: int
) -> dict[str, dict[str, float]]:
    """TTFT and decode tokens per second, ``stock`` and ``candidate``
    interleaved over ``rounds`` rounds (so a drifting clock or a warming
    cache costs both alike), each the min and the median.
    """
    stock_ttft, stock_tps, candidate_ttft, candidate_tps = [], [], [], []
    for _ in range(rounds):
        t, s = timed_round(stock, tokens, num_tokens)
        stock_ttft.append(t)
        stock_tps.append(s)
        t, s = timed_round(candidate, tokens, num_tokens)
        candidate_ttft.append(t)
        candidate_tps.append(s)
    return {
        "stock": {
            "ttft_min": min(stock_ttft),
            "ttft_median": statistics.median(stock_ttft),
            "tps_min": min(stock_tps),
            "tps_median": statistics.median(stock_tps),
        },
        "candidate": {
            "ttft_min": min(candidate_ttft),
            "ttft_median": statistics.median(candidate_ttft),
            "tps_min": min(candidate_tps),
            "tps_median": statistics.median(candidate_tps),
        },
    }


def entry_applies(kind: str, entry, recording: Recording) -> bool:
    """Whether a candidate profile's ``entry`` (a fusion's own ``(FusionKind,
    steps, edges, versions)`` where ``kind`` is ``"fusion"``, else a
    ``PackingEntry``) matches anything in ``recording``, either only where
    it applies in the recording's version (``graph_fusions`` checks a
    fusion's own this way already; a packing's own is checked here).
    """
    trial = Profile()
    if kind == "fusion":
        fusion_kind, steps, edges, versions = entry
        trial.add_fusion(fusion_kind, steps, edges, versions)
        return bool(graph_fusions(recording, trial))
    trial.add_packing(entry.members, entry.versions)
    version = recording.version
    return any(
        trial.packings_of(step.op.resolved(), version) for step in recording.steps
    )


def classify_entries(
    candidate: Profile, recordings: dict[str, Recording]
) -> list[tuple[tuple[str, Any], set[str]]]:
    """Each of ``candidate``'s fusion and packing entries, tagged
    ``("fusion"|"packing", entry)``, with the labels of ``recordings``'
    versions it matches (``entry_applies``), in the order ``candidate``
    holds them, fusions first.
    """
    classified = []
    for entry in candidate.fusions():
        matches = {
            l for l, r in recordings.items() if entry_applies("fusion", entry, r)
        }
        classified.append((("fusion", entry), matches))
    for entry in candidate.packings():
        matches = {
            l for l, r in recordings.items() if entry_applies("packing", entry, r)
        }
        classified.append((("packing", entry), matches))
    return classified


def build_variant(stock_path: Path | None, tags) -> Profile:
    """The stock profile at ``stock_path`` (empty with None) plus ``tags``
    (``classify_entries``'s tagged entries): a profile ``save`` can write
    for a bisection trial.
    """
    profile = Profile.load(stock_path) if stock_path is not None else Profile()
    for kind, entry in tags:
        if kind == "fusion":
            profile.add_fusion(*entry)
        else:
            profile.add_packing(entry.members, entry.versions)
    return profile


def bisect(
    model_class: type[CausalLM],
    checkpoint: Path,
    max_seq_len: int | None,
    candidate_path: Path,
    stock_path: Path | None,
    out_dir: Path,
    stock: CausalLM,
    tokens,
    decode_steps: int,
) -> dict:
    """Narrow a bit-identity mismatch to one version's entries, then to a
    prefix of them: classify ``candidate_path``'s fusion and packing entries
    by which version of a fresh recording each matches
    (``classify_entries``), build a profile of the stock plus one version's
    entries at a time, and keep halving a version whose variant still
    mismatches. Saves the smallest failing profile under ``out_dir`` and
    returns a summary; the first version to reproduce the mismatch wins.
    """
    probe = model_class.from_checkpoint(checkpoint, max_seq_len=max_seq_len)
    labels = version_labels(probe)
    recordings = {l: probe.record(**s) for l, s in zip(labels, probe.shapes())}
    dev = require_device()
    candidate = Profile.load(Path(candidate_path) / f"{dev.name}.json")
    classified = classify_entries(candidate, recordings)

    for label in labels:
        tags = [tag for tag, matches in classified if label in matches]
        if not tags:
            continue
        profile_dir = out_dir / f"bisect-{label}"
        profile_dir.mkdir(parents=True, exist_ok=True)
        build_variant(stock_path, tags).save(profile_dir / f"{dev.name}.json")
        variant = load_model(model_class, checkpoint, max_seq_len, profile_dir)
        mismatch = bit_identity(stock, variant, tokens, decode_steps)
        variant.release()
        if not mismatch:
            continue
        print(f"[bisect] {label} alone mismatches at steps {mismatch}; halving")
        lo, hi, best = 1, len(tags), tags
        while hi - lo > 1:
            mid = (lo + hi) // 2
            trial_tags = tags[:mid]
            profile_dir = out_dir / f"bisect-{label}-{mid}"
            profile_dir.mkdir(parents=True, exist_ok=True)
            build_variant(stock_path, trial_tags).save(profile_dir / f"{dev.name}.json")
            variant = load_model(model_class, checkpoint, max_seq_len, profile_dir)
            mismatch = bit_identity(stock, variant, tokens, decode_steps)
            variant.release()
            if mismatch:
                hi, best = mid, trial_tags
            else:
                lo = mid
        profile_dir = out_dir / f"bisect-{label}-minimal"
        profile_dir.mkdir(parents=True, exist_ok=True)
        build_variant(stock_path, best).save(profile_dir / f"{dev.name}.json")
        return {
            "version": label,
            "entry_count": len(best),
            "mismatch_steps": mismatch,
            "profile": str(profile_dir),
        }
    return {
        "version": None,
        "note": "no single version's entries reproduced the mismatch alone",
    }


def model_tune_points(model_class: type[Model], checkpoint: Path) -> list[Timed]:
    """``model_class.tune_calls``'s own calls, over its own tune flags
    (``tune_arguments``) at their defaults save ``--checkpoint``: a
    model-general way to the per-call points and weights a version is tuned
    at (a decoder's context ladder, an encoder's query and longest call),
    not one battery written for a decoder alone.
    """
    tune_parser = argparse.ArgumentParser(add_help=False)
    model_class.tune_arguments(tune_parser)
    tune_args = tune_parser.parse_args(["--checkpoint", str(checkpoint)])
    return model_class.tune_calls(tune_parser, tune_args)


def version_recordings(model) -> dict[Version, Recording]:
    """``model``'s own ``Recording`` of each of ``shapes()``, by
    ``Recording.version``: the identity ``compare_versions`` matches
    ``model_tune_points``'s calls against.
    """
    out = {}
    for shape in model.shapes():
        recording = model.record(**shape)
        out[recording.version] = recording
    return out


def compare_versions(
    model_class: type[Model],
    checkpoint: Path,
    max_seq_len: int | None,
    stock_profile: Profile,
    candidate_profile: Profile,
    labels: list[str],
    label_to_version: dict[str, Version],
    *,
    timing: Timing = Timing(rounds=3, calls=10),
    log=print,
) -> dict[str, dict[str, Any]]:
    """``labels`` (``changed_versions``'s), each compared bit for bit and
    timed, ``stock_profile`` against ``candidate_profile``
    (``compare_graphs``): a fresh real-weight recording of the version
    (``model_class.from_checkpoint``, not the already-loaded ``stock`` or
    ``candidate``, whose states and weights a recording apart from their own
    cannot address), built under each profile (``apply_profile``), at the
    per-call points ``model_tune_points`` gives that version
    (``Recording.version`` matched to ``label_to_version``).

    A build or dispatch failure, and a device timeout propagated from
    ``compare_graphs``, are raised rather than recorded: only a real
    bit-identity mismatch (``compare_graphs``'s own ``NotBitIdentical``) is
    worth a report entry over a traceback, since that is validate's very
    question; anything else is a bug worth seeing in full.

    Raises:
        ValueError: ``label_to_version`` names a version
            ``model_tune_points`` gives no call for: ``model_class``'s
            ``tune_calls`` names shapes other than its own ``shapes()``'s,
            which is always a bug (the two are meant to name one set), never
            an expected state a report should paper over.
        RuntimeError: A version's build or dispatch failed outright (not a
            bit-identity mismatch, ``NotBitIdentical``'s own), or a device
            timeout propagated from ``compare_graphs``.
    """
    dev = require_device()
    probe = model_class.from_checkpoint(checkpoint, max_seq_len=max_seq_len)
    recordings = version_recordings(probe)
    calls = {c.recording.version: c for c in model_tune_points(model_class, checkpoint)}

    out: dict[str, dict[str, Any]] = {}
    for label in labels:
        version = label_to_version[label]
        call_t, recording = calls.get(version), recordings.get(version)
        if call_t is None or recording is None:
            raise ValueError(
                f"{label}: no tune point for this version; "
                f"{model_class.__name__}.tune_calls names other shapes than "
                f"{model_class.__name__}.shapes() does"
            )
        call = dataclasses.replace(call_t, recording=recording)
        graphs = []
        for profile in (stock_profile, candidate_profile):
            patched, fused, packing = apply_profile(call.recording, profile, dev)
            chosen = plan(
                dev,
                patched,
                True,
                False,
                step_words=_step_words(patched),
                fusions=fused,
            )
            graphs.append(
                CompiledGraph(patched, chosen, fusions=fused, packing=packing)
            )
        try:
            delta, noise = compare_graphs(call, *graphs, timing=timing, log=log)
        except NotBitIdentical as e:
            out[label] = {"bit_identical": False, "error": str(e)}
            log(f"[{label}] not bit-identical: {e}")
            continue
        noise_s = "?" if noise is None else f"{noise:.1f}"
        out[label] = {"bit_identical": True, "delta_us": delta, "noise_us": noise}
        log(
            f"[{label}] bit-identical; candidate {delta:+.1f} ± {noise_s} us vs "
            f"stock end to end"
        )
    return out


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "application", help="dotted under iron.applications (e.g. llama)"
    )
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument(
        "--candidate",
        type=Path,
        required=True,
        help="a profile directory (one <device>.json per device) to validate "
        "against the model's stock profile",
    )
    parser.add_argument("--max-seq-len", type=int, default=None)
    parser.add_argument("--prompt-chars", type=int, default=12000)
    parser.add_argument("--decode-steps", type=int, default=32)
    parser.add_argument("--accuracy-tokens", type=int, default=40)
    parser.add_argument("--speed-tokens", type=int, default=32)
    parser.add_argument("--speed-rounds", type=int, default=5)
    parser.add_argument(
        "--bisect",
        action="store_true",
        help="on a bit-identity mismatch, narrow it to the candidate's "
        "profile entries at fault (bisect)",
    )
    parser.add_argument("--out", type=Path, default=Path("validate_report.json"))
    parser.add_argument(
        "--device",
        choices=("npu1", "npu2"),
        default=None,
        help="bind this device explicitly (aie.iron.device.from_name); by "
        "default the runtime's own, where one is already bound",
    )
    args = parser.parse_args(argv)

    if args.device is not None:
        aie_utils.set_current_device(from_name(args.device, n_cols=None))

    model_class = application_model(args.application)
    if args.bisect and not issubclass(model_class, CausalLM):
        parser.error(
            f"{args.application}'s model, {model_class.__name__}, is not a "
            f"CausalLM: --bisect (narrowing a greedy-logits mismatch) is a "
            f"decoder's"
        )

    report: dict[str, Any] = {
        "application": args.application,
        "candidate": str(args.candidate),
    }

    print("loading stock model (real weights)...")
    stock = load_model(model_class, args.checkpoint, args.max_seq_len, None)
    print("loading candidate model...")
    candidate = load_model(
        model_class, args.checkpoint, args.max_seq_len, args.candidate
    )

    report["stock_live"] = verify_live("stock", stock)
    report["candidate_live"] = verify_live("candidate", candidate)
    report["changed_versions"] = changed_versions(
        report["stock_live"], report["candidate_live"]
    )
    if not report["changed_versions"]:
        parser.error(f"{args.candidate}: the candidate profile changes no version")

    if issubclass(model_class, CausalLM):
        tokens = stock.prompt(args.prompt_chars)
        C = stock.config.prefill_chunk
        report["prompt_tokens"], report["prefill_chunk"] = len(tokens), C
        print(f"prompt: {len(tokens)} tokens (prefill_chunk {C})")
        if len(tokens) <= C or not len(tokens) % C:
            parser.error(
                f"--prompt-chars gives {len(tokens)} tokens: the prompt must cross a "
                f"{C}-token chunk and end in a partial one"
            )

        print(
            f"bit identity over {len(tokens)}-token prompt + "
            f"{args.decode_steps} decode steps..."
        )
        mismatch = bit_identity(stock, candidate, tokens, args.decode_steps)
        report["bit_identical"] = not mismatch
        report["mismatch_steps"] = mismatch
        print(
            f"bit identity: {'identical' if not mismatch else f'differs at {mismatch}'}"
        )

        if mismatch and args.bisect:
            print("bisecting...")
            dev = require_device()
            own_profile = model_class.profile
            stock_path = (
                Path(own_profile) / f"{dev.name}.json"
                if isinstance(own_profile, (str, Path))
                else None
            )
            report["bisection"] = bisect(
                model_class,
                args.checkpoint,
                args.max_seq_len,
                args.candidate,
                stock_path,
                args.out.parent,
                stock,
                tokens,
                args.decode_steps,
            )

        print("accuracy against golden...")
        stats, mismatches = run_accuracy(
            candidate, stock.prompt(1024), args.accuracy_tokens
        )
        report["accuracy"] = {
            **stats,
            "top1_mismatches": mismatches,
            "of": args.accuracy_tokens,
        }
        print(
            f"accuracy: mean KL {stats['Mean']:.6f}  p90 {stats['P90']:.6f}  "
            f"max {stats['Max']:.6f}  top-1 mismatches {mismatches}/{args.accuracy_tokens}"
        )

        print(f"speed: {args.speed_rounds} interleaved rounds...")
        report["speed"] = speed(
            stock, candidate, tokens, args.speed_tokens, args.speed_rounds
        )
        for label, s in report["speed"].items():
            print(
                f"[speed:{label}] TTFT min {s['ttft_min']:.4f}s median "
                f"{s['ttft_median']:.4f}s | decode tok/s min {s['tps_min']:.2f} "
                f"median {s['tps_median']:.2f}"
            )
    else:
        dev = require_device()
        own_profile = model_class.profile
        stock_profile = (
            Profile.load(Path(own_profile) / f"{dev.name}.json")
            if isinstance(own_profile, (str, Path))
            else Profile()
        )
        candidate_profile = Profile.load(Path(args.candidate) / f"{dev.name}.json")
        label_to_version = dict(zip(version_labels(stock), stock.versions))
        print(f"comparing {len(report['changed_versions'])} changed version(s)...")
        report["versions"] = compare_versions(
            model_class,
            args.checkpoint,
            args.max_seq_len,
            stock_profile,
            candidate_profile,
            report["changed_versions"],
            label_to_version,
        )
        report["bit_identical"] = all(
            v["bit_identical"] for v in report["versions"].values()
        )
        verdict = "OK" if report["bit_identical"] else "MISMATCH"
        summary = ", ".join(
            (
                f"{label}: {v['delta_us']:+.1f} us"
                if v["bit_identical"]
                else f"{label}: MISMATCH"
            )
            for label, v in report["versions"].items()
        )
        print(f"[{verdict}] {args.application}: {summary}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2))
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
