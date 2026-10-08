# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""ResampleTaps: torchvision's antialiased bicubic filter for one axis,
computed on the device bit for bit as torch computes it on the CPU.

The table is `chunks` objects of `words` int32. Each starts with a header,
`[precision, window, first, outputs]`, and holds `outputs` slots from
output `first` on, a slot being `[start, count]` then the output's
`window` int16 weights, two to a word. A size the table cannot hold
(`per_chunk` below 1, too few chunks, or a size below 1) writes
`[-1, window, 0, 0]` to every header instead.
"""

import dataclasses

import numpy as np
from aie.iron import (
    Buffer,
    ExternalFunction,
    ObjectFifo,
    TaskGroup,
    Worker,
    WorkerRuntimeBarrier,
)
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance

from iron.common import Operator, Out, Value, auto, param
from iron.common.testing import Case, Testing

from .reference import taps, window

HEADER = 4

RESAMPLE = """
#include <stdint.h>

// torch's weights are float64 without contraction: an FMA changes the bits.
#pragma clang fp contract(off)

namespace {
constexpr int HEADER = 4;
constexpr int WMAX = 2 * (WORDS - HEADER - 2);

struct Axis {
    double scale, support, invscale;
    int in, out, window, slot, per;
    bool ok;
};

Axis axis(int32_t in, int32_t out, int32_t chunks) {
    Axis a = {};
    a.in = in;
    a.out = out;
    if (in < 1 || out < 1)
        return a;
    a.scale = (double)in / (double)out;
    a.support = a.scale >= 1.0 ? 2.0 * a.scale : 2.0;
    int s = (int)a.support;
    if ((double)s < a.support)
        s++;
    a.window = s * 2 + 1;
    a.invscale = a.scale >= 1.0 ? 1.0 / a.scale : 1.0;
    a.slot = 2 + (a.window + 1) / 2;
    a.per = (WORDS - HEADER) / a.slot;
    a.ok = a.per >= 1 && a.per * chunks >= out;
    return a;
}

double filter(double x) {
    const double A = -0.5;
    x = __builtin_fabs(x);
    if (x < 1.0)
        return ((A + 2) * x - (A + 3)) * x * x + 1;
    if (x < 2.0)
        return ((A * x - 5 * A) * x + 8 * A) * x - 4 * A;
    return 0.0;
}

double w[WMAX];

// Output i's unnormalized weights in w; returns their sequential sum.
double taps(const Axis &a, int i, int &xmin, int &xsize) {
    double center = a.scale * (i + 0.5);
    int lo = (int)(center - a.support + 0.5);
    xmin = lo > 0 ? lo : 0;
    int hi = (int)(center + a.support + 0.5);
    if (hi > a.in)
        hi = a.in;
    xsize = hi - xmin;
    if (xsize < 0)
        xsize = 0;
    if (xsize > a.window)
        xsize = a.window;
    double total = 0.0;
    for (int j = 0; j < xsize; j++) {
        w[j] = filter(((double)(j + xmin) - center + 0.5) * a.invscale);
        total += w[j];
    }
    return total;
}

double load(const int32_t *p) {
    double v;
    __builtin_memcpy(&v, p, sizeof v);
    return v;
}
} // namespace

// The largest normalized weight of the outputs in chunks core, core + CORES,
// ...: division rounds monotonically, so it is the largest weight over the
// total (the smallest, for a negative total), one division per output.
extern "C" void resample_peak(int32_t *peak, int32_t in, int32_t out,
                              int32_t core, int32_t chunks) {
    Axis a = axis(in, out, chunks * CORES);
    double m = 0.0;
    for (int k = 0; a.ok && k < chunks; k++) {
        int first = (core + k * CORES) * a.per;
        int last = first + a.per < out ? first + a.per : out;
        for (int i = first; i < last; i++) {
            int xmin, xsize;
            double total = taps(a, i, xmin, xsize);
            if (total == 0.0)
                continue;
            double e = w[0];
            for (int j = 1; j < xsize; j++)
                if (total > 0.0 ? e < w[j] : w[j] < e)
                    e = w[j];
            double v = e / total;
            if (m < v)
                m = v;
        }
    }
    __builtin_memcpy(peak, &m, sizeof m);
}

extern "C" void resample_join(int32_t *a, int32_t *b, int32_t *out) {
    double x = load(a), y = load(b);
    double m = x < y ? y : x;
    __builtin_memcpy(out, &m, sizeof m);
}

extern "C" void resample_quantize(int32_t *peak, int32_t *chunk, int32_t in,
                                  int32_t out, int32_t core, int32_t k,
                                  int32_t chunks) {
    Axis a = axis(in, out, chunks * CORES);
    for (int i = 0; i < WORDS; i++)
        chunk[i] = 0;
    if (!a.ok) {
        chunk[0] = -1;
        chunk[1] = a.window;
        return;
    }
    double wt_max = load(peak);
    int p;
    for (p = 0; p < 22; ++p)
        if ((int)(0.5 + wt_max * (1 << (p + 1))) >= (1 << 15))
            break;
    int first = (core + k * CORES) * a.per;
    int n = out - first;
    n = n < 0 ? 0 : n > a.per ? a.per : n;
    chunk[0] = p;
    chunk[1] = a.window;
    chunk[2] = first;
    chunk[3] = n;
    for (int s = 0; s < n; s++) {
        int32_t *slot = chunk + HEADER + s * a.slot;
        int xmin, xsize;
        double total = taps(a, first + s, xmin, xsize);
        slot[0] = xmin;
        slot[1] = xsize;
        int16_t *q = (int16_t *)(slot + 2);
        for (int j = 0; j < xsize; j++) {
            double v = (total != 0.0 ? w[j] / total : w[j]) * (1 << p);
            q[j] = v < 0 ? (int)(-0.5 + v) : (int)(0.5 + v);
        }
    }
}
"""


def per_chunk(in_size: int, out_size: int, words: int) -> int:
    """The outputs one chunk of a `words`-word table holds.

    Args:
        in_size: The input samples on the axis.
        out_size: The output samples on the axis.
        words: The int32 words of a chunk.

    Returns:
        The slots after the header, each two words and the window's int16
        weights two to a word; 0 if not one fits.
    """
    return (words - HEADER) // (2 + (window(in_size, out_size) + 1) // 2)


class ResampleTaps(Operator):
    """The int16 filter table and precision torch resamples one axis with,
    `in_length` samples to `out_length`.

    Each core takes chunks `k, k + cores, ...` and computes its outputs'
    weights in float64 twice: once for the largest normalized weight, which
    a chain through the cores reduces and the last core broadcasts, and once
    to quantize at the precision that weight sets. `in_length` and
    `out_length` are values the cores read, `in_size` and `out_size` unless
    a graph binds them per call, so one build serves every size the table
    holds.
    """

    test = Testing(
        [
            # A phone photo's width to the image budget's, on every core.
            Case(dict(in_size=4032, out_size=912), bench=True),
            Case(dict(in_size=3024, out_size=672)),
            # Upsampled: the window is 5, 50 outputs to a chunk.
            Case(dict(in_size=17, out_size=1008)),
            Case(dict(in_size=961, out_size=960)),
            # A window of 49, and one core with no chain.
            Case(dict(in_size=8000, out_size=672, num_aie_columns=1, num_channels=1)),
            Case(dict(in_size=1, out_size=48, num_aie_columns=2)),
        ],
        tolerance=Tolerance.exact(),
    )

    in_size: int = param()
    out_size: int = param()
    words: int = param(default=256)
    # Enough for out_size, in a multiple of 16 so every core count up to it divides.
    chunks: int = param(
        default=lambda op: 16
        * -(-op.out_size // (16 * max(1, per_chunk(op.in_size, op.out_size, op.words))))
    )
    num_aie_columns: int = auto()
    num_channels: int = auto(2)

    table = Out(
        chunks,
        words,
        dtype=np.int32,
        tile=(words,),
        per=(num_aie_columns, num_channels),
    )
    count = Value(np.int32, derive=lambda op: op.chunks // op.cores)  # chunks per core
    in_length = Value(np.int32, derive=lambda op: op.in_size)
    out_length = Value(np.int32, derive=lambda op: op.out_size)

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    def validate(self) -> None:
        if self.in_size < 1 or self.out_size < 1:
            raise ValueError(
                f"ResampleTaps: {self.in_size} -> {self.out_size} samples; "
                f"both must be at least 1"
            )

    def resolve(self, dev):
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: self.chunks % (c * self.num_channels) == 0,
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    def compatible(self) -> None:
        if self.chunks % self.cores:
            raise ValueError(
                f"ResampleTaps: chunks ({self.chunks}) must be a multiple of the "
                f"{self.cores} cores"
            )
        per = per_chunk(self.in_size, self.out_size, self.words)
        if per < 1 or per * self.chunks < self.out_size:
            raise ValueError(
                f"ResampleTaps: {self.chunks} chunks of {self.words} words do not "
                f"hold {self.out_size} outputs of a "
                f"{window(self.in_size, self.out_size)}-tap window"
            )

    def ops(self) -> int:
        return 0  # a table, not arithmetic over its words: its figure is latency

    def reference(self, *, in_length=None, out_length=None):
        n_in = self.in_size if in_length is None else int(in_length)
        n_out = self.out_size if out_length is None else int(out_length)
        table = np.zeros((self.chunks, self.words), np.int32)
        if n_in < 1 or n_out < 1:
            table[:, 0] = -1
            return table
        taps_window = window(n_in, n_out)
        per = per_chunk(n_in, n_out, self.words)
        if per < 1 or per * self.chunks < n_out:
            table[:, 0], table[:, 1] = -1, taps_window
            return table
        t = taps(n_in, n_out)
        slot = 2 + (taps_window + 1) // 2
        for c in range(self.chunks):
            first = c * per
            n = min(max(n_out - first, 0), per)
            table[c, :HEADER] = t.precision, taps_window, first, n
            slots = table[c, HEADER : HEADER + per * slot].reshape(per, slot)
            slots[:n, 0] = t.start[first : first + n]
            slots[:n, 1] = t.count[first : first + n]
            weights = np.zeros((n, 2 * (slot - 2)), np.int16)
            weights[:, :taps_window] = t.weights[first : first + n]
            slots[:n, 2:] = weights.view(np.int32)
        return table

    def sequence(self, rt):
        """Chunk `c` from core `c % cores`, the round-robin order the cores
        compute them in.
        """
        tg = TaskGroup()
        for lane, tap, _ in rt.round_robin(self.table, 0):
            rt.drain(lane, (self.table, tap), group=tg)
        tg.finish()

    def array(self, target) -> list:
        cores = self.cores
        peak_ty = np.ndarray[(2,), np.dtype[np.int32]]
        peak_k = ExternalFunction(
            "resample_peak",
            source_string=RESAMPLE,
            arg_types=[peak_ty, np.int32, np.int32, np.int32, np.int32],
            compile_flags=[f"-DWORDS={self.words}", f"-DCORES={cores}"],
            symbol_prefix=f"resample_{self.words}_{cores}",
        )
        join_k = peak_k.object_file.bind("resample_join", [peak_ty] * 3)
        quantize_k = peak_k.object_file.bind(
            "resample_quantize", [peak_ty, self.table.tile] + [np.int32] * 5
        )
        of_tables = [
            ObjectFifo(self.table.tile, name=f"table_{k}", depth=2)
            for k in range(cores)
        ]
        # Core k passes the peak so far to core k + 1; the last broadcasts it
        # from a memtile.
        of_chain = [
            ObjectFifo(peak_ty, name=f"peak_{k}", depth=1) for k in range(cores - 1)
        ]
        of_peak = of_all = None
        if cores > 1:
            of_peak = ObjectFifo(peak_ty, name="peak", depth=1)
            of_all = of_peak.cons().forward(name="peak_all", depth=1)
        local = Buffer(peak_ty, initial_value=np.zeros(2, np.int32), name="peak_last")

        elf = target.image == "elf"
        names = ["count", "in_length", "out_length"]
        dynamic = {n: self.uses_value(n) and elf for n in names}
        static = [n for n in names if not dynamic[n]]
        rtps = [
            Buffer(
                np.ndarray[(max(1, len(static)),), np.dtype[np.int32]],
                name=f"rtp_{k}",
                use_write_rtp=True,
            )
            for k in range(cores)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(cores)]
        params = [self.value(n).param for n in names if dynamic[n]]

        def core_fn(
            core,
            table,
            prior,
            passed,
            shared,
            last,
            peak_fn,
            join_fn,
            quantize_fn,
            rtp,
            barrier,
            *words,
        ):
            barrier.wait_for_value(1)
            words = list(words)
            n, n_in, n_out = (
                words.pop(0).read() if dynamic[name] else rtp[static.index(name)]
                for name in names
            )
            if passed is not None:
                mine = passed.acquire(1)
                peak_fn(mine, n_in, n_out, core, n)
                if prior is not None:
                    before = prior.acquire(1)
                    join_fn(before, mine, mine)
                    prior.release(1)
                passed.release(1)
                peak = shared.acquire(1)
            else:
                peak_fn(last, n_in, n_out, core, n)
                if prior is not None:
                    before = prior.acquire(1)
                    join_fn(before, last, last)
                    prior.release(1)
                    out = shared.acquire(1)
                    join_fn(last, last, out)
                    shared.release(1)
                peak = last
            for k in range_(n):
                chunk = table.acquire(1)
                quantize_fn(peak, chunk, n_in, n_out, core, k, n)
                table.release(1)
            if passed is not None:
                shared.release(1)

        workers = []
        for k in range(cores):
            final = k == cores - 1
            shared = None
            if of_peak is not None:
                shared = of_peak.prod() if final else of_all.cons()
            workers.append(
                Worker(
                    core_fn,
                    [
                        k,
                        of_tables[k].prod(),
                        of_chain[k - 1].cons() if k else None,
                        None if final else of_chain[k].prod(),
                        shared,
                        local if final else None,
                        peak_k,
                        join_k,
                        quantize_k,
                        rtps[k],
                        barriers[k],
                    ]
                    + params,
                    stack_size=4096,
                )
            )
            self.table.lane(k).bind(of_tables[k].cons())
        for name in static:
            self.value(name).bind(rtps, static.index(name))
        return workers + barriers
