# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""torchvision's antialiased bicubic resize of a uint8 image, on the device
bit for bit as torch computes it on the CPU.

`ResampleTaps` computes one axis's filter table. The table is `chunks`
objects of `words` int32. Each starts with a header, `[precision, window,
first, outputs]`, and holds `outputs` slots from output `first` on, a slot
being `[start, count]` then the output's `window` int16 weights, two to a
word. A size the table cannot hold (`per_chunk` below 1, too few chunks, or
a size below 1) writes `[-1, window, 0, 0]` to every header instead.

`Resample` resizes an image with two such tables and writes it as the
vision tower's bf16 patches.
"""

import dataclasses

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
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
from ml_dtypes import bfloat16

from iron.common import Extent, In, Operator, Out, Value, auto, param
from iron.common.testing import Case, Testing

from .reference import resize, taps, window

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
    if (PER)
        a.per = PER <= a.per ? PER : 0;
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


def per_chunk(in_size: int, out_size: int, words: int, slots: int | None = None) -> int:
    """The outputs one chunk of a `words`-word table holds.

    Args:
        in_size: The input samples on the axis.
        out_size: The output samples on the axis.
        words: The int32 words of a chunk.
        slots: The slots a chunk is fixed to, or None for as many as fit.

    Returns:
        The slots after the header, each two words and the window's int16
        weights two to a word; 0 if not one fits, or not `slots`.
    """
    fit = (words - HEADER) // (2 + (window(in_size, out_size) + 1) // 2)
    if slots is None:
        return fit
    return slots if slots <= fit else 0


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
            # A patch's 16 outputs to a chunk, as Resample reads them.
            Case(dict(in_size=3024, out_size=672, words=356, slots=16)),
        ],
        tolerance=Tolerance.exact(),
    )

    in_size: int = param()
    out_size: int = param()
    words: int = param(default=256)
    # The slots of a chunk, or None for as many as the window lets fit.
    slots: int | None = param(default=None, array=True)
    # Enough for out_size, in a multiple of 16 so every core count up to it divides.
    chunks: int = param(
        default=lambda op: 16
        * -(
            -op.out_size
            // (16 * max(1, per_chunk(op.in_size, op.out_size, op.words, op.slots)))
        )
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
        per = per_chunk(self.in_size, self.out_size, self.words, self.slots)
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
        per = per_chunk(n_in, n_out, self.words, self.slots)
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
            compile_flags=[
                f"-DWORDS={self.words}",
                f"-DCORES={cores}",
                f"-DPER={self.slots or 0}",
            ],
            symbol_prefix=f"resample_{self.words}_{cores}_{self.slots or 0}",
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


SIDE = 16  # a patch's pixels on each axis, and the outputs of a taps chunk

# The bf16 bits of u8 / 255 as the image processor rounds them: in float32,
# then to bf16 once.
PIXELS = (np.arange(256, dtype=np.float32) * np.float32(1 / 255)).astype(bfloat16)

RESIZE = """
#include <aie_api/aie.hpp>
#include <stdint.h>

namespace {
using taps_t = aie::vector<int16_t, 32>;
using sum_t = aie::accum<acc32, 32>;

constexpr int HEADER = 4;
constexpr int SIDE = 16;
constexpr int WIN = 2 * ((WORDS - HEADER) / SIDE - 2) - 1;
static_assert(WIN <= 64, "a window is at most two vectors of taps");
// The input pixels under one patch column's 16 outputs, at any scale a
// WIN-tap window allows, and the 64 a window's vectors read past them.
constexpr int SPAN = 5 * WIN + 8;
constexpr int PLANE = (SPAN + 64 + 63) / 64 * 64;
constexpr int LINE = COLS * SIDE * 3;

const uint16_t PIXEL[256] = {@PIXELS@};

int rows, columns, cpr, owned, core;
// part: the next image chunk's in its row; ring: that row's in mid.
int consumed, part, ring, arrived, opened, next, hp, hwin;
bool ok;
int hstart[COLS][SIDE];
alignas(64) int16_t hweight[COLS][SIDE][64];
int span0[COLS], span[COLS];
// A row's pixels under each patch column, a plane to a channel.
alignas(64) uint8_t line[COLS][3][PLANE];
// The last WIN rows across, row r at r % WIN, and the band's rows down: patch
// column i's channel ch is bytes (3 * i + ch) * SIDE on.
alignas(64) uint8_t mid[WIN][LINE];
alignas(64) uint8_t hold[SIDE][LINE];

taps_t widen(const uint8_t *x) {
    return aie::load_unaligned_v<32>(x).unpack().cast_to<int16_t>();
}

// The sums of outputs o..o+N-1 of patch column i over channel plane x,
// output o + j in lanes j * 32 / N on, which add up to it.
// Inlined whole and branch-free, so the leaves' loads overlap.
template <int N, bool WIDE>
__attribute__((always_inline)) aie::vector<int32_t, 32> tree(const uint8_t *x, int i,
                                                             int o) {
    if constexpr (N == 1) {
        const int16_t *w = hweight[i][o];
        x += hstart[i][o] - span0[i];
        sum_t a = aie::mul<acc32>(widen(x), aie::load_v<32>(w));
        if constexpr (WIDE)
            a = aie::mac(a, widen(x + 32), aie::load_v<32>(w + 32));
        return a.to_vector<int32_t>(0);
    } else {
        auto [even, odd] = aie::interleave_unzip(
            tree<N / 2, WIDE>(x, i, o), tree<N / 2, WIDE>(x, i, o + N / 2), 32 / N);
        return aie::add(even, odd);
    }
}

// (bias + sum) >> p, clipped to [0, 255], as srs gives it.
struct Srs {
    aie::rounding_mode rounding = aie::swap_rounding(aie::rounding_mode::floor);
    aie::saturation_mode saturation = aie::get_saturation();
    Srs() { aie::set_saturation(aie::saturation_mode::saturate); }
    ~Srs() {
        aie::set_rounding(rounding);
        aie::set_saturation(saturation);
    }
};

template <bool WIDE> void across() {
    Srs srs;
    uint8_t *m = mid[ring];
    const auto bias = aie::broadcast<int32_t, 32>(1 << (hp - 1));
    const auto zero = aie::zeros<int32_t, 32>();
    for (int i = 0; i < owned; i++)
        for (int ch = 0; ch < 3; ch++) {
            // A half at a time, so the leaves' vectors fit the registers.
            aie::vector<int32_t, 32> half[2];
#pragma clang loop unroll(disable)
            for (int h = 0; h < 2; h++)
                half[h] = tree<SIDE / 2, WIDE>(line[i][ch], i, h * SIDE / 2);
            auto [lo, hi] = aie::interleave_unzip(half[0], half[1], 32 / SIDE);
            auto [even, odd] = aie::interleave_unzip(aie::add(lo, hi), zero, 1);
            sum_t a(aie::add(aie::add(even, odd), bias));
            aie::store_v(m + (3 * i + ch) * SIDE, a.to_vector<uint8_t>(hp).extract<16>(0));
        }
}

// Peano cannot legalize this loop bounded by a pointer, `src + 3 <= stop`.
// A byte store is a read-modify-write that serializes with the next, so
// whole pixels go four to a word store.
void split(const uint8_t *__restrict src, uint8_t *__restrict red,
           uint8_t *__restrict green, uint8_t *__restrict blue, int n) {
    int k = 0;
    for (; k < n && (uintptr_t)(red + k) % 4; k++) {
        red[k] = src[3 * k];
        green[k] = src[3 * k + 1];
        blue[k] = src[3 * k + 2];
    }
    int words = (n - k) / 4;
    if (words >= 4) {
        const uint8_t *s = src + 3 * k;
        uint8_t *r = (uint8_t *)__builtin_assume_aligned(red + k, 4);
        uint8_t *g = (uint8_t *)__builtin_assume_aligned(green + k, 4);
        uint8_t *b = (uint8_t *)__builtin_assume_aligned(blue + k, 4);
#pragma clang loop min_iteration_count(4)
#pragma clang loop hint(aie-gpr-realloc, 1)
        for (int w = 0; w < words; w++, s += 12) {
            uint32_t x = s[0] | s[3] << 8 | s[6] << 16 | (uint32_t)s[9] << 24;
            uint32_t y = s[1] | s[4] << 8 | s[7] << 16 | (uint32_t)s[10] << 24;
            uint32_t z = s[2] | s[5] << 8 | s[8] << 16 | (uint32_t)s[11] << 24;
            __builtin_memcpy(r + 4 * w, &x, 4);
            __builtin_memcpy(g + 4 * w, &y, 4);
            __builtin_memcpy(b + 4 * w, &z, 4);
        }
        k += 4 * words;
    }
    for (; k < n; k++) {
        red[k] = src[3 * k];
        green[k] = src[3 * k + 1];
        blue[k] = src[3 * k + 2];
    }
}

// The band's output rows whose input rows have all come, in order.
void down(const int32_t *vt) {
    if (!ok)
        return;
    int p = vt[0], slot = 2 + (vt[1] + 1) / 2, n = owned * SIDE * 3;
    Srs srs;
    const auto bias = aie::broadcast<int32_t, 32>(1 << (p - 1));
    const uint8_t *in[WIN];
    for (; next < SIDE; next++) {
        const int32_t *t = vt + HEADER + next * slot;
        int s = t[0], c = t[1];
        if (s + c > arrived)
            break;
        if (s < 0 || s < arrived - WIN || c < 0 || c > WIN) {
            ok = false;
            break;
        }
        const int16_t *w = (const int16_t *)(t + 2);
        // Row s's slot: ring is arrived's, and s is at most WIN rows before it.
        int m = ring - (arrived - s);
        m += m < 0 ? WIN : 0;
        for (int k = 0; k < c; k++, m = m + 1 == WIN ? 0 : m + 1)
            in[k] = mid[m];
        for (int b = 0; b < n; b += 32) {
            sum_t a(bias);
            for (int k = 0; k < c; k++)
                a = aie::mac(a, aie::load_v<32>(in[k] + b).unpack().cast_to<int16_t>(),
                             w[k]);
            aie::store_v(hold[next] + b, a.to_vector<uint8_t>(p));
        }
    }
}
} // namespace

// counts: [width chunks, bands, image chunks now, patches a band, image
// chunks left]. Every count is of what all cores share, never of `ok`, so
// the broadcast streams stay in step on any input.
extern "C" void resize_setup(int32_t *counts, int32_t h, int32_t w, int32_t ho,
                             int32_t wo, int32_t c) {
    rows = h;
    columns = w;
    core = c;
    cpr = w > 0 ? (3 * w + CHUNK - 1) / CHUNK : 0;
    int strips = wo > 0 ? wo / SIDE : 0;
    // A column past the patches at least, so the last of every band is zeros.
    int nmax = strips / CORES + 1;
    owned = c < strips ? (strips - c + CORES - 1) / CORES : 0;
    ok = h >= 1 && w >= 1 && ho >= SIDE && wo >= SIDE && ho % SIDE == 0 &&
         wo % SIDE == 0 && nmax <= COLS;
    consumed = part = ring = arrived = opened = next = 0;
    counts[0] = strips;
    counts[1] = ho > 0 ? ho / SIDE : 0;
    counts[2] = 0;
    counts[3] = nmax;
    counts[4] = 0;
}

// Width chunk k is patch column k, this core's when k % CORES == core.
extern "C" void resize_take(int32_t *chunk, int32_t k) {
    if (!ok || k % CORES != core)
        return;
    int i = k / CORES, p = chunk[0], win = chunk[1];
    if (p < 1 || p > 22 || win < 1 || win > WIN || chunk[2] != k * SIDE ||
        chunk[3] != SIDE) {
        ok = false;
        return;
    }
    hp = p;
    hwin = win;
    int slot = 2 + (win + 1) / 2;
    const int32_t *last = chunk + HEADER + (SIDE - 1) * slot;
    int first = chunk[HEADER], end = last[0] + last[1];
    for (int o = 0; o < SIDE; o++) {
        const int32_t *t = chunk + HEADER + o * slot;
        const int16_t *w = (const int16_t *)(t + 2);
        hstart[i][o] = t[0];
        if (t[0] < first || t[1] < 0 || t[1] > win || t[0] + t[1] > end)
            ok = false;
        for (int j = 0; j < 64; j++)
            hweight[i][o][j] = j < t[1] ? w[j] : 0;
    }
    span0[i] = first;
    span[i] = end - first;
    if (first < 0 || end > columns || span[i] > SPAN)
        ok = false;
}

// The next height chunk opens: the image chunks up to the last input row its
// outputs read.
extern "C" void resize_band(int32_t *vt, int32_t *counts) {
    int win = vt[1], e = rows;
    if (vt[0] >= 1 && vt[0] <= 22 && win >= 1 && win <= WIN &&
        vt[2] == opened * SIDE && vt[3] == SIDE) {
        const int32_t *t = vt + HEADER + (SIDE - 1) * (2 + (win + 1) / 2);
        e = t[0] + t[1];
        e = e < 0 ? 0 : e > rows ? rows : e;
    } else {
        ok = false;
    }
    int need = e * cpr - consumed;
    counts[2] = need > 0 ? need : 0;
    opened++;
    next = 0;
    down(vt);
}

extern "C" void resize_consume(uint8_t *chunk, int32_t *vt) {
    consumed++;
    if (ok) {
        int at = part * CHUNK;
        for (int i = 0; i < owned; i++) {
            int lo = 3 * span0[i], hi = lo + 3 * span[i];
            int from = lo > at ? lo : at;
            int to = hi < at + CHUNK ? hi : at + CHUNK;
            // x * 43691 >> 17 is x / 3 for 0 <= x < 98304, which Peano calls
            // __divsi3 for; past this column's bytes px is not used.
            int px = (unsigned)(from - lo) * 43691u >> 17, ch = from - lo - 3 * px;
            const uint8_t *src = chunk + (from - at), *stop = chunk + (to - at);
            uint8_t *red = line[i][0], *green = line[i][1], *blue = line[i][2];
            // The pixels a chunk boundary splits, then whole ones.
            if (ch == 1 && src < stop)
                green[px] = *src++, ch = 2;
            if (ch == 2 && src < stop)
                blue[px++] = *src++;
            int whole = stop > src ? (stop - src) * 43691 >> 17 : 0;
            split(src, red + px, green + px, blue + px, whole);
            src += 3 * whole;
            px += whole;
            if (src < stop)
                red[px] = *src++;
            if (src < stop)
                green[px] = *src;
        }
    }
    if (++part != cpr)
        return;
    if (ok && hwin > 32)
        across<true>();
    else if (ok)
        across<false>();
    part = 0;
    ring = ring + 1 == WIN ? 0 : ring + 1;
    arrived++;
    down(vt);
}

// Patch column core + i * CORES of the band, zeros past the image.
extern "C" void resize_emit(uint16_t *out, int32_t i) {
    if (next < SIDE)
        ok = false;
    if (!ok || i >= owned) {
        for (int k = 0; k < SIDE * SIDE * 3; k += 32)
            aie::store_v(out + k, aie::zeros<uint16_t, 32>());
        return;
    }
    // Four pixels, a word of each plane in and six out. Byte loads here miscompile:
    // llvm-aie's post-increment combine over a chained pointer reads row for row + SIDE.
    uint16_t *o = (uint16_t *)__builtin_assume_aligned(out, 4);
    for (int y = 0; y < SIDE; y++) {
        const uint8_t *row = hold[y] + 3 * i * SIDE;
        for (int x = 0; x < SIDE; x += 4, o += 12) {
            uint32_t c[3], w[6];
            for (int ch = 0; ch < 3; ch++)
                __builtin_memcpy(&c[ch], __builtin_assume_aligned(row + ch * SIDE + x, 4), 4);
            for (int v = 0; v < 12; v += 2)
                w[v / 2] = PIXEL[c[v % 3] >> 8 * (v / 3) & 255] |
                           (uint32_t)PIXEL[c[(v + 1) % 3] >> 8 * ((v + 1) / 3) & 255] << 16;
            __builtin_memcpy(o, w, 24);
        }
    }
}

extern "C" void resize_finish(int32_t *counts) {
    counts[4] = rows * cpr - consumed;
}
""".replace("@PIXELS@", ", ".join(str(v) for v in PIXELS.view(np.uint16)))


class Resample(Operator):
    """An image resized as torchvision's antialiased bicubic resize does it
    on the CPU, written as the vision tower's patches.

    `image` is the `(height, width, 3)` uint8 image, each row padded to
    whole `chunk`-byte chunks, which every core receives. `taps_w` and
    `taps_h` are `ResampleTaps` tables with a patch's 16 outputs to a
    chunk (`slots=16`), `width -> out_width` and `height -> out_height`.
    Core `k` owns patch columns `k, k + cores, ...`: it takes their width
    chunks, resamples each image row across them, and each band of 16
    output rows down them once its input rows have come. Patch `(py, px)`
    is row `py * pad + px` of `patches`, 16x16 pixels row-major, channels
    last, `u8 / 255` in bf16; `pad` is `(columns // cores + 1) * cores`
    for `columns` patch columns, its extra columns zeros: row `pad - 1` is
    always a zero patch, which padding past the image gathers.

    `rows`, `columns`, `out_rows` and `out_columns` may be bound per call,
    so one build serves every size the buffers hold.
    """

    test = Testing(
        [
            # A phone photo to the image budget's 42x57 patches.
            Case(
                dict(height=3024, width=4032, out_height=672, out_width=912),
                bench=True,
            ),
            # Across only, on 8 cores of 8 patch columns each.
            Case(
                dict(
                    height=480,
                    width=640,
                    out_height=480,
                    out_width=1008,
                    num_aie_columns=4,
                )
            ),
            Case(dict(height=37, width=53, out_height=96, out_width=144)),
            # As many patch columns as cores: a column of zeros past them.
            Case(dict(height=37, width=53, out_height=96, out_width=256)),
            # A 37-tap window down, the most a 356-word chunk holds.
            Case(dict(height=6000, width=500, out_height=672, out_width=432)),
        ],
        draw=lambda op: dict(
            image=np.random.default_rng(42).integers(
                0, 256, (op.image_chunks, op.chunk), dtype=np.uint8
            ),
            taps_w=ResampleTaps(
                in_size=op.width,
                out_size=op.out_width,
                words=op.words,
                slots=SIDE,
                chunks=op.width_chunks,
            ).reference(),
            taps_h=ResampleTaps(
                in_size=op.height,
                out_size=op.out_height,
                words=op.words,
                slots=SIDE,
                chunks=op.height_chunks,
            ).reference(),
        ),
        tolerance=Tolerance.exact(),
    )

    height: int = param()
    width: int = param()
    out_height: int = param()
    out_width: int = param()
    # Every chunk is a buffer handshake with every core: few and large ones.
    chunk: int = param(default=4096, array=True)
    # A 39-tap window: a scale of up to 9.5.
    words: int = param(default=356, array=True)
    # The patch columns a core holds, so cores * patch_columns across.
    patch_columns: int = param(default=8, array=True)
    image_chunks: int = param(
        default=lambda op: op.height * -(-3 * op.width // op.chunk)
    )
    # In multiples of 16, as ResampleTaps's are, so every core count up to it divides.
    width_chunks: int = param(default=lambda op: 16 * -(-op.out_width // (16 * SIDE)))
    height_chunks: int = param(default=lambda op: 16 * -(-op.out_height // (16 * SIDE)))
    patch_rows: int = param(
        default=lambda op: op.out_height
        // SIDE
        * 16
        * (op.out_width // (16 * SIDE) + 1)
    )
    num_aie_columns: int = auto()
    num_channels: int = auto(2)

    rows = Extent(height)
    columns = Extent(width)
    out_rows = Extent(out_height)
    out_columns = Extent(out_width)

    image = In(image_chunks, chunk, dtype=np.uint8, tile=(chunk,), broadcast=True)
    taps_w = In(width_chunks, words, dtype=np.int32, tile=(words,), broadcast=True)
    # Through taps_w's stream, after it.
    taps_h = In(height_chunks, words, dtype=np.int32)
    patches = Out(
        patch_rows,
        SIDE * SIDE * 3,
        dtype=bfloat16,
        tile=(SIDE * SIDE * 3,),
        per=(num_aie_columns, num_channels),
    )

    src_rows = Value(np.int32, derive=lambda op: op.rows)
    src_columns = Value(np.int32, derive=lambda op: op.columns)
    dst_rows = Value(np.int32, derive=lambda op: op.out_rows)
    dst_columns = Value(np.int32, derive=lambda op: op.out_columns)
    image_count = Value(
        np.int32,
        derive=lambda op: op.rows * -(-3 * op.columns // op.chunk),
        optional=True,
    )
    width_count = Value(
        np.int32, derive=lambda op: op.out_columns // SIDE, optional=True
    )
    height_count = Value(np.int32, derive=lambda op: op.out_rows // SIDE, optional=True)
    # Patches per core: every band's, padded past the cores.
    patch_count = Value(
        np.int32,
        derive=lambda op: op.out_rows
        // SIDE
        * (op.out_columns // SIDE // op.cores + 1),
        optional=True,
    )

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    @property
    def window_cap(self) -> int:
        """The widest filter window a chunk of `words` holds 16 of."""
        return 2 * ((self.words - HEADER) // SIDE - 2) - 1

    def validate(self) -> None:
        if min(self.height, self.width) < 1 or min(self.out_height, self.out_width) < 1:
            raise ValueError(
                f"Resample: {self.height}x{self.width} -> "
                f"{self.out_height}x{self.out_width}; every size must be at least 1"
            )
        if self.out_height % SIDE or self.out_width % SIDE:
            raise ValueError(
                f"Resample: {self.out_height}x{self.out_width} is not whole "
                f"{SIDE}-pixel patches"
            )

    def resolve(self, dev):
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: self.patch_rows % (c * self.num_channels) == 0,
        )
        return dataclasses.replace(self, num_aie_columns=cols)

    def compatible(self) -> None:
        cap = self.window_cap
        for n_in, n_out in (
            (self.width, self.out_width),
            (self.height, self.out_height),
        ):
            if window(n_in, n_out) > cap:
                raise ValueError(
                    f"Resample: {n_in} -> {n_out} samples is a "
                    f"{window(n_in, n_out)}-tap window; {self.words}-word chunks "
                    f"hold {cap}"
                )
        strips, bands = self.out_width // SIDE, self.out_height // SIDE
        nmax = strips // self.cores + 1
        if nmax > self.patch_columns:
            raise ValueError(
                f"Resample: {strips} patch columns over {self.cores} cores is "
                f"{nmax} a core; a core holds {self.patch_columns}"
            )
        for name, have, need in (
            (
                "image_chunks",
                self.image_chunks,
                self.height * -(-3 * self.width // self.chunk),
            ),
            ("width_chunks", self.width_chunks, strips),
            ("height_chunks", self.height_chunks, bands),
            ("patch_rows", self.patch_rows, bands * nmax * self.cores),
        ):
            if have < need:
                raise ValueError(f"Resample: {name} is {have}; the image needs {need}")

    def ops(self) -> int:
        return 0  # integer filters, not bf16 arithmetic: its figure is latency

    def reference(
        self,
        image,
        taps_w,
        taps_h,
        *,
        rows=None,
        columns=None,
        out_rows=None,
        out_columns=None,
    ):
        h = self.height if rows is None else int(rows)
        w = self.width if columns is None else int(columns)
        ho = self.out_height if out_rows is None else int(out_rows)
        wo = self.out_width if out_columns is None else int(out_columns)
        line = -(-3 * w // self.chunk) * self.chunk
        pixels = np.asarray(image).reshape(-1)[: h * line].reshape(h, line)
        out = resize(pixels[:, : 3 * w].reshape(h, w, 3), ho, wo)
        bands, strips = ho // SIDE, wo // SIDE
        pad = (strips // self.cores + 1) * self.cores
        grid = np.zeros((bands, pad, SIDE, SIDE, 3), np.uint8)
        grid[:, :strips] = out.reshape(bands, SIDE, strips, SIDE, 3).transpose(
            0, 2, 1, 3, 4
        )
        return PIXELS[grid.reshape(bands * pad, SIDE * SIDE * 3)]

    def sequence(self, rt):
        """The image, then both tables down one stream, and each core's
        patches: every transfer sized at its buffer, shortened per call, or
        at the build's sizes.
        """
        tg = TaskGroup()
        moves = [
            (rt.fill, self.image, self.image, "image_count", 0, 1),
            (rt.fill, self.taps_w, self.taps_w, "width_count", 0, 1),
            (rt.fill, self.taps_w, self.taps_h, "height_count", 0, 1),
        ] + [
            (rt.drain, self.patches.lane(k), self.patches, "patch_count", k, self.cores)
            for k in range(self.cores)
        ]
        for move, stream, buffer, name, first, step in moves:
            per_call = self.uses_value(name)
            n, width = buffer.shape
            count = n // step if per_call else self.residents[name]
            tap = TensorAccessPattern(
                (n, width), first * width, [1, count, 1, width], [0, step * width, 0, 1]
            )
            move(
                stream,
                (buffer, tap),
                group=tg,
                size_by={1: self.value(name)} if per_call else None,
            )
        tg.finish()

    def array(self, target) -> list:
        cores = self.cores
        counts_ty = np.ndarray[(8,), np.dtype[np.int32]]
        taps_ty, image_ty, patch_ty = (
            self.taps_w.tile,
            self.image.tile,
            self.patches.tile,
        )
        setup_k = ExternalFunction(
            "resize_setup",
            source_string=RESIZE,
            arg_types=[counts_ty] + [np.int32] * 5,
            compile_flags=[
                f"-DWORDS={self.words}",
                f"-DCHUNK={self.chunk}",
                f"-DCOLS={self.patch_columns}",
                f"-DCORES={cores}",
            ],
            symbol_prefix=f"resize_{self.words}_{self.chunk}_{self.patch_columns}_{cores}",
        )
        lib = setup_k.object_file
        take_k = lib.bind("resize_take", [taps_ty, np.int32])
        band_k = lib.bind("resize_band", [taps_ty, counts_ty])
        consume_k = lib.bind("resize_consume", [image_ty, taps_ty])
        emit_k = lib.bind("resize_emit", [patch_ty, np.int32])
        finish_k = lib.bind("resize_finish", [counts_ty])
        of_image = ObjectFifo(image_ty, name="image", depth=2)
        of_taps = ObjectFifo(taps_ty, name="taps", depth=2)
        of_patches = [
            ObjectFifo(patch_ty, name=f"patches_{k}", depth=2) for k in range(cores)
        ]

        elf = target.image == "elf"
        names = ["src_rows", "src_columns", "dst_rows", "dst_columns"]
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
            image,
            taps,
            patches,
            counts,
            setup_fn,
            take_fn,
            band_fn,
            consume_fn,
            emit_fn,
            finish_fn,
            rtp,
            barrier,
            *words,
        ):
            barrier.wait_for_value(1)
            words = list(words)
            h, w, ho, wo = (
                words.pop(0).read() if dynamic[name] else rtp[static.index(name)]
                for name in names
            )
            setup_fn(counts, h, w, ho, wo, core)
            for k in range_(counts[0]):
                chunk = taps.acquire(1)
                take_fn(chunk, k)
                taps.release(1)
            for _ in range_(counts[1]):
                vt = taps.acquire(1)
                band_fn(vt, counts)
                for _ in range_(counts[2]):
                    chunk = image.acquire(1)
                    consume_fn(chunk, vt)
                    image.release(1)
                for i in range_(counts[3]):
                    out = patches.acquire(1)
                    emit_fn(out, i)
                    patches.release(1)
                taps.release(1)
            finish_fn(counts)
            for _ in range_(counts[4]):
                image.acquire(1)
                image.release(1)

        workers = [
            Worker(
                core_fn,
                [
                    k,
                    of_image.cons(),
                    of_taps.cons(),
                    of_patches[k].prod(),
                    Buffer(counts_ty, name=f"counts_{k}"),
                    setup_k,
                    take_k,
                    band_k,
                    consume_k,
                    emit_k,
                    finish_k,
                    rtps[k],
                    barriers[k],
                ]
                + params,
            )
            for k in range(cores)
        ]
        for k in range(cores):
            self.patches.lane(k).bind(of_patches[k].cons())
        self.image.lane(0).bind(of_image.prod())
        self.taps_w.lane(0).bind(of_taps.prod())
        for name in static:
            self.value(name).bind(rtps, static.index(name))
        return workers + barriers
