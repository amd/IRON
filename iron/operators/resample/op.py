# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""torchvision's antialiased bicubic or Lanczos resize of a uint8 image, on
the device bit for bit as torch computes it on the CPU.

`ResampleTaps` computes one axis's filter table. The table is `chunks`
objects of `words` int32, of which a call writes the first its sizes fill
(`ResampleTaps.filled`). Each starts with a header, `[precision, window,
first, outputs]`, and holds `outputs` slots from output `first` on, a slot
being `[start, count]` then the output's `window` int16 weights, two to a
word; the slots past them repeat the last. A size the table cannot hold
(`per_chunk` below 1, too few chunks, or a size below 1) writes
`[-1, window, 0, 0]` to every header instead.

`Resample` resizes an image with two such tables and writes it as the
vision tower's bf16 patches, or as a uint8 image another resize reads, and
`PatchPositions` says where each of the tower's rows comes from in them.
"""

import hashlib
from typing import Any

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, ExternalFunction, In, ObjectFifo, Out, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import param, per_call, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing

from .reference import Interpolation, resize, taps, window

HEADER = 4

RESAMPLE = """
#include <stdint.h>

// torch's weights are float64 without contraction: an FMA changes the bits.
#pragma clang fp contract(off)
// AIE2's 16 KB of program memory holds Lanczos' float64 code only at minsize.
#if __AIE_ARCH__ == 20 && LANCZOS
#pragma clang attribute push(__attribute__((minsize)), apply_to = function)
#endif

namespace {
constexpr int HEADER = 4;
constexpr int WMAX = 2 * (WORDS - HEADER - 2);
constexpr double RADIUS = LANCZOS ? 3.0 : 2.0;

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
    a.support = a.scale >= 1.0 ? RADIUS * a.scale : RADIUS;
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

#if LANCZOS
// fdlibm's sin (__kernel_sin, __kernel_cos and __ieee754_rem_pio2's medium
// case, which covers |x| < 2^20 pi / 2), within an ulp of the C library's.
double kernel_sin(double x, double y, bool tail) {
    const double S1 = -1.66666666666666324348e-01, S2 = 8.33333333332248946124e-03,
                 S3 = -1.98412698298579493134e-04, S4 = 2.75573137070700676789e-06,
                 S5 = -2.50507602534068634195e-08, S6 = 1.58969099521155010221e-10;
    double z = x * x, w = z * z, v = z * x;
    double r = S2 + z * (S3 + z * S4) + z * w * (S5 + z * S6);
    if (!tail)
        return x + v * (S1 + z * r);
    return x - ((z * (0.5 * y - v * r) - y) - v * S1);
}

double kernel_cos(double x, double y) {
    const double C1 = 4.16666666666666019037e-02, C2 = -1.38888888888741095749e-03,
                 C3 = 2.48015872894767294178e-05, C4 = -2.75573143513906633035e-07,
                 C5 = 2.08757232129817482790e-09, C6 = -1.13596475577881948265e-11;
    double z = x * x, w = z * z;
    double r = z * (C1 + z * (C2 + z * C3)) + w * w * (C4 + z * (C5 + z * C6));
    double hz = 0.5 * z;
    w = 1.0 - hz;
    return w + (((1.0 - w) - hz) + (z * r - x * y));
}

// The high word of |x|.
uint32_t high(double x) {
    uint64_t bits;
    __builtin_memcpy(&bits, &x, sizeof bits);
    return (uint32_t)(bits >> 32) & 0x7fffffff;
}

int exponent(double x) { return (int)(high(x) >> 20); }

double sine(double x) {
    if (high(x) <= 0x3fe921fb)
        return high(x) < 0x3e500000 ? x : kernel_sin(x, 0.0, false);
    const double invpio2 = 6.36619772367581382433e-01, pio2_1 = 1.57079632673412561417e+00,
                 pio2_1t = 6.07710050650619224932e-11, pio2_2 = 6.07710050630396597660e-11,
                 pio2_2t = 2.02226624879595063154e-21, pio2_3 = 2.02226624871116645580e-21,
                 pio2_3t = 8.47842766036889956997e-32;
    double fn = x * invpio2 + 0x1.8p52;
    fn = fn - 0x1.8p52;
    int n = (int)fn, j = exponent(x);
    double r = x - fn * pio2_1, w = fn * pio2_1t, y0 = r - w, t;
    if (j - exponent(y0) > 16) {
        t = r;
        w = fn * pio2_2;
        r = t - w;
        w = fn * pio2_2t - ((t - r) - w);
        y0 = r - w;
        if (j - exponent(y0) > 49) {
            t = r;
            w = fn * pio2_3;
            r = t - w;
            w = fn * pio2_3t - ((t - r) - w);
            y0 = r - w;
        }
    }
    double y1 = (r - y0) - w;
    switch (n & 3) {
    case 0:
        return kernel_sin(y0, y1, true);
    case 1:
        return kernel_cos(y0, y1);
    case 2:
        return -kernel_sin(y0, y1, true);
    default:
        return -kernel_cos(y0, y1);
    }
}

double sinc(double x) {
    if (x == 0.0)
        return 1.0;
    x *= 3.14159265358979323846;
    return sine(x) / x;
}

// Lanczos-3, as torch's antialiased resize computes it.
double filter(double x) {
    x = __builtin_fabs(x);
    return x < 3.0 ? sinc(x) * sinc(x / 3.0) : 0.0;
}
#else
double filter(double x) {
    const double A = -0.5;
    x = __builtin_fabs(x);
    if (x < 1.0)
        return ((A + 2) * x - (A + 3)) * x * x + 1;
    if (x < 2.0)
        return ((A * x - 5 * A) * x + 8 * A) * x - 4 * A;
    return 0.0;
}
#endif

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
    // Past the axis's end, the last output's slot again.
    for (int s = n; n > 0 && s < a.per; s++)
        for (int i = 0; i < a.slot; i++)
            chunk[HEADER + s * a.slot + i] = chunk[HEADER + (n - 1) * a.slot + i];
}
#if __AIE_ARCH__ == 20 && LANCZOS
#pragma clang attribute pop
#endif
"""


def per_chunk(
    in_size: int,
    out_size: int,
    words: int,
    slots: int | None = None,
    interpolation: Interpolation = Interpolation.BICUBIC,
) -> int:
    """The outputs one chunk of a `words`-word table holds.

    Args:
        in_size: The input samples on the axis.
        out_size: The output samples on the axis.
        words: The int32 words of a chunk.
        slots: The slots a chunk is fixed to, or None for as many as fit.
        interpolation: The filter.

    Returns:
        The slots after the header, each two words and the window's int16
        weights two to a word; 0 if not one fits, or not `slots`.
    """
    taps_window = window(in_size, out_size, interpolation)
    fit = (words - HEADER) // (2 + (taps_window + 1) // 2)
    if slots is None:
        return fit
    return slots if slots <= fit else 0


class ResampleTaps(Operator):
    """The int16 filter table and precision torch resamples one axis with,
    `in_samples` samples to `out_samples`.

    Each core takes chunks `k, k + cores, ...` and computes their weights in
    float64 twice: once for the largest weight, which a chain through the
    cores reduces, and once to quantize at the precision it sets.
    """

    test = Testing(
        [
            # A phone photo's width to the image budget's, on every core.
            Case(dict(in_size=4032, out_size=912), bench=True),
            # Upsampled: the window is 5, 50 outputs to a chunk.
            Case(dict(in_size=17, out_size=1008)),
            Case(dict(in_size=961, out_size=960)),
            # A window of 49, and one core with no chain.
            Case(dict(in_size=8000, out_size=672, num_aie_columns=1, num_channels=1)),
            Case(dict(in_size=1, out_size=48, num_aie_columns=2)),
            # A patch's 16 outputs to a chunk, as Resample reads them.
            Case(dict(in_size=3024, out_size=672, words=356, slots=16)),
            # Lanczos-3: a window of 25 at a scale of 4; a partial last chunk.
            Case(
                dict(
                    in_size=2048,
                    out_size=512,
                    words=244,
                    slots=16,
                    interpolation=Interpolation.LANCZOS,
                )
            ),
            Case(
                dict(
                    in_size=500,
                    out_size=1364,
                    words=244,
                    slots=16,
                    interpolation=Interpolation.LANCZOS,
                )
            ),
            Case(
                dict(in_size=4032, out_size=2048, interpolation=Interpolation.LANCZOS)
            ),
        ],
    )

    in_size: int = param()
    out_size: int = param()
    words: int = param(default=256)
    # The slots of a chunk, or None for as many as the window lets fit.
    slots: int | None = param(default=None, array=True)
    interpolation: Interpolation = param(default=Interpolation.BICUBIC, array=True)
    # A multiple of 16, so every core count up to it divides.
    chunks: int = param(
        default=lambda op: 16
        * -(-op.out_size // (16 * max(1, op.per_chunk(op.in_size, op.out_size))))
    )
    num_aie_columns: int = tunable(domain=widths)
    num_channels: int = tunable(default=2, domain=widths)

    table = Out(
        chunks,
        words,
        dtype=np.int32,
        obj_shape=(words,),
        per=(num_aie_columns, num_channels),
    )
    in_samples = per_call(bounds=in_size)
    out_samples = per_call(bounds=out_size)

    count = per_call(
        derive=lambda op: -(-op.filled(op.in_samples, op.out_samples) // op.cores),
    )
    in_length = per_call(derive=lambda op: op.in_samples)
    out_length = per_call(derive=lambda op: op.out_samples)

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    def per_chunk(self, n_in: int, n_out: int) -> int:
        """The outputs a chunk holds of `n_in` samples to `n_out` (`per_chunk`)."""
        return per_chunk(n_in, n_out, self.words, self.slots, self.interpolation)

    def filled(self, n_in: int, n_out: int) -> int:
        """The chunks a table of `n_in` samples to `n_out` is written in.

        Args:
            n_in: The input samples on the axis.
            n_out: The output samples on the axis.

        Returns:
            Those its outputs fill, in a multiple of 16 as `chunks` is; every
            chunk for sizes the table cannot hold, each header saying so. The
            cores write whole rounds, so up to a round past them.
        """
        per = 0
        if min(n_in, n_out) >= 1:
            per = self.per_chunk(n_in, n_out)
        if not per:
            return self.chunks
        return min(16 * -(-n_out // (16 * per)), self.chunks)

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
        return self.replace(num_aie_columns=cols)

    def compatible(self) -> None:
        if self.chunks % self.cores:
            raise ValueError(
                f"ResampleTaps: chunks ({self.chunks}) must be a multiple of the "
                f"{self.cores} cores"
            )
        per = self.per_chunk(self.in_size, self.out_size)
        if per < 1 or per * self.chunks < self.out_size:
            raise ValueError(
                f"ResampleTaps: {self.chunks} chunks of {self.words} words do not "
                f"hold {self.out_size} outputs of a "
                f"{window(self.in_size, self.out_size, self.interpolation)}-tap window"
            )

    def ops(self) -> int:
        return 0  # a table, not arithmetic over its words: its figure is latency

    def reference(self, *, in_samples=None, out_samples=None):
        n_in = self.in_size if in_samples is None else int(in_samples)
        n_out = self.out_size if out_samples is None else int(out_samples)
        table = np.zeros((self.chunks, self.words), np.int32)
        if n_in < 1 or n_out < 1:
            table[:, 0] = -1
            return table
        taps_window = window(n_in, n_out, self.interpolation)
        per = self.per_chunk(n_in, n_out)
        if per < 1 or per * self.chunks < n_out:
            table[:, 0], table[:, 1] = -1, taps_window
            return table
        t = taps(n_in, n_out, self.interpolation)
        slot = 2 + (taps_window + 1) // 2
        for c in range(self.filled(n_in, n_out)):
            first = c * per
            n = min(max(n_out - first, 0), per)
            table[c, :HEADER] = t.precision, taps_window, first, n
            slots = table[c, HEADER : HEADER + per * slot].reshape(per, slot)
            slots[:n, 0] = t.start[first : first + n]
            slots[:n, 1] = t.count[first : first + n]
            weights = np.zeros((n, 2 * (slot - 2)), np.int16)
            weights[:, :taps_window] = t.weights[first : first + n]
            slots[:n, 2:] = weights.view(np.int32)
            if n:
                slots[n:] = slots[n - 1]
        return table

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def sequence(self, rt):
        """Chunk `c` from core `c % cores`, the order the cores compute them in."""
        per_call = self.count.per_call
        n, words = self.table.shape
        count = n // self.cores if per_call else self.residents["count"]
        tg = TaskGroup()
        for k in range(self.cores):
            tap = TensorAccessPattern(
                (n, words),
                k * words,
                [1, count, 1, words],
                [0, self.cores * words, 0, 1],
            )
            self.table.drain(
                tap,
                lane=k,
                group=tg,
                wait=True,
                length_parameter=self.count if per_call else None,
                length_unit=words,
            )
        tg.finish()

    def build(self) -> Built:
        cores = self.num_aie_columns * self.num_channels
        peak_ty = np.ndarray[(2,), np.dtype[np.int32]]
        peak_k = ExternalFunction(
            "resample_peak",
            source_string=RESAMPLE,
            arg_types=[peak_ty, np.int32, np.int32, np.int32, np.int32],
            compile_flags=[
                f"-DWORDS={self.words}",
                f"-DCORES={cores}",
                f"-DPER={self.slots or 0}",
                f"-DLANCZOS={int(self.interpolation == Interpolation.LANCZOS)}",
            ],
            symbol_prefix=(
                f"resample_{self.words}_{cores}_{self.slots or 0}_{self.interpolation}"
            ),
        )
        join_k = peak_k.object_file.bind("resample_join", [peak_ty] * 3)
        quantize_k = peak_k.object_file.bind(
            "resample_quantize", [peak_ty, self.table.obj_type] + [np.int32] * 5
        )
        of_tables = [ObjectFifo(self.table.obj_type, depth=2) for k in range(cores)]
        # The peak passes core to core; the last broadcasts it from a memtile.
        of_chain = [ObjectFifo(peak_ty, depth=1) for k in range(cores - 1)]
        of_peak = of_all = None
        if cores > 1:
            of_peak = ObjectFifo(peak_ty, depth=1)
            of_all = of_peak.cons().forward(depth=1)
        local = Buffer(peak_ty, initial_value=np.zeros(2, np.int32))

        counts = [self.count, self.in_length, self.out_length]
        rtps = [Rtp(counts) for _ in range(cores)]

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
        ):
            words = rtp.read()
            n, n_in, n_out = (words[v] for v in counts)
            mine = last if passed is None else passed.acquire(1)
            peak_fn(mine, n_in, n_out, core, n)
            if prior is not None:
                before = prior.acquire(1)
                join_fn(before, mine, mine)
                prior.release(1)
            if passed is not None:
                passed.release(1)
                peak = shared.acquire(1)
            else:
                if prior is not None:
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
                    ],
                )
            )
        self.table.bind([f.cons() for f in of_tables])
        return Built(workers, rtps)


SIDE = 16  # a patch's pixels on each axis, and the outputs of a taps chunk

# u8 / 255 as the image processor rounds it: in float32, then to bf16 once.
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
// Whole 64-byte vectors, so a row of mid or hold starts aligned at any COLS.
constexpr int LINE = (COLS * SIDE * 3 + 63) / 64 * 64;

const uint16_t PIXEL[CHANNELS][256] = {@PIXELS@};

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
// the broadcast streams stay in step on any input. A partial patch at the
// edge holds the image's last row and column again.
extern "C" void resize_setup(int32_t *counts, int32_t h, int32_t w, int32_t ho,
                             int32_t wo, int32_t c) {
    rows = h;
    columns = w;
    core = c;
    cpr = w > 0 ? (3 * w + CHUNK - 1) / CHUNK : 0;
    int strips = wo > 0 ? (wo + SIDE - 1) / SIDE : 0;
    owned = c < strips ? (strips - c + CORES - 1) / CORES : 0;
#if OUT8
    // A band's 16 rows, each across the core's COLS patch columns.
    int nmax = SIDE;
    bool fits = (strips + CORES - 1) / CORES <= COLS;
#else
    // A column past the patches at least, so the last of every band is zeros.
    int nmax = strips / CORES + 1;
    bool fits = nmax <= COLS;
#endif
    ok = h >= 1 && w >= 1 && ho >= 1 && wo >= 1 && fits;
    consumed = part = ring = arrived = opened = next = 0;
    counts[0] = strips;
    counts[1] = ho > 0 ? (ho + SIDE - 1) / SIDE : 0;
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
        chunk[3] < 1 || chunk[3] > SIDE) {
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
        vt[2] == opened * SIDE && vt[3] >= 1 && vt[3] <= SIDE) {
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
                w[v / 2] = PIXEL[v % 3 % CHANNELS][c[v % 3] >> 8 * (v / 3) & 255] |
                           (uint32_t)PIXEL[(v + 1) % 3 % CHANNELS]
                                          [c[(v + 1) % 3] >> 8 * ((v + 1) / 3) & 255]
                               << 16;
            __builtin_memcpy(o, w, 24);
        }
    }
}

// Row y of the band across the core's COLS patch columns, core + i * CORES,
// as uint8 pixels, zeros past the image.
extern "C" void resize_emit8(uint8_t *out, int32_t y) {
    if (next < SIDE)
        ok = false;
    // Four pixels, a word of each plane in and three out, as resize_emit reads.
    uint8_t *o = (uint8_t *)__builtin_assume_aligned(out, 4);
    for (int i = 0; i < COLS; i++) {
        const uint8_t *row = hold[y] + 3 * i * SIDE;
        for (int x = 0; x < SIDE; x += 4, o += 12) {
            uint32_t c[3] = {0, 0, 0}, w[3] = {0, 0, 0};
            if (ok && i < owned)
                for (int ch = 0; ch < 3; ch++)
                    __builtin_memcpy(&c[ch], __builtin_assume_aligned(row + ch * SIDE + x, 4),
                                     4);
            for (int v = 0; v < 12; v++)
                w[v / 4] |= (c[v % 3] >> 8 * (v / 3) & 255) << 8 * (v % 4);
            __builtin_memcpy(o, w, 12);
        }
    }
}

extern "C" void resize_finish(int32_t *counts) {
    counts[4] = rows * cpr - consumed;
}
"""


class Resample(Operator):
    """An image resized as torchvision's antialiased bicubic or Lanczos
    resize does it on the CPU, written as the vision tower's patches, each
    pixel's bf16 from its uint8 level (`levels`), or with `dtype` uint8 as an
    image another resize reads.

    Every core receives the image in `chunk`-byte chunks; core `k` owns
    patch columns `k, k + cores, ...`, resamples each row across them, then
    each band of 16 rows down them; a partial patch at the edge holds the
    image's last row and column again. Patch `(py, px)` is row
    `py * pad + px` of `patches`, `pad` the patch columns padded past the
    cores with zeros: row `pad - 1` is the zero patch padding gathers. A
    uint8 image's rows are `pitch` bytes, `patch_columns` patches of every
    core's, zeros past the image; a core writes it a row at a time.
    """

    test = Testing(
        [
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
            # A uint8 image, Lanczos, partial patches at its edge.
            Case(
                dict(
                    height=37,
                    width=53,
                    out_height=100,
                    out_width=150,
                    words=244,
                    interpolation=Interpolation.LANCZOS,
                    dtype=np.uint8,
                ),
                id="lanczos_image",
                lower=True,
            ),
            # SmolVLM's two resizes: to the longest edge's 2048 as a uint8
            # image, 8 patch columns a core on 16 cores, then to 512x512,
            # normalized, 3 a core, a row of mid not whole vectors.
            Case(
                dict(
                    height=480,
                    width=640,
                    out_height=1536,
                    out_width=2048,
                    words=244,
                    interpolation=Interpolation.LANCZOS,
                    dtype=np.uint8,
                    num_aie_columns=8,
                ),
                id="lanczos_image_landscape",
            ),
            Case(
                dict(
                    height=500,
                    width=333,
                    out_height=2048,
                    out_width=1364,
                    words=244,
                    interpolation=Interpolation.LANCZOS,
                    dtype=np.uint8,
                    num_aie_columns=8,
                ),
                id="lanczos_image_portrait",
            ),
            Case(
                dict(
                    height=1364,
                    width=2048,
                    out_height=512,
                    out_width=512,
                    chunk=6144,
                    words=244,
                    patch_columns=3,
                    interpolation=Interpolation.LANCZOS,
                    mean=(0.5, 0.5, 0.5),
                    std=(0.5, 0.5, 0.5),
                    num_aie_columns=8,
                ),
                id="lanczos_normalized",
                lower=True,
            ),
        ],
        draw=lambda op: dict(
            given={
                op.image: np.random.default_rng(42).integers(
                    0, 256, (op.image_chunks, op.chunk), dtype=np.uint8
                ),
                op.taps_w: ResampleTaps(
                    in_size=op.width,
                    out_size=op.out_width,
                    words=op.words,
                    slots=SIDE,
                    chunks=op.width_chunks,
                    interpolation=op.interpolation,
                ).reference(),
                op.taps_h: ResampleTaps(
                    in_size=op.height,
                    out_size=op.out_height,
                    words=op.words,
                    slots=SIDE,
                    chunks=op.height_chunks,
                    interpolation=op.interpolation,
                ).reference(),
            }
        ),
    )

    height: int = param()
    width: int = param()
    out_height: int = param()
    out_width: int = param()
    # Every chunk is a handshake with every core: few and large ones.
    chunk: int = param(default=4096)
    # A 39-tap window: a scale of up to 9.5.
    words: int = param(default=356)
    # A floor of 8, so two resizes of one image that need no more share an array.
    patch_columns: int = param(
        default=lambda op: max(8, op.default_patch_columns()), array=True
    )
    image_chunks: int = param(
        default=lambda op: op.height * -(-3 * op.width // op.chunk)
    )
    # Multiples of 16, as ResampleTaps's are.
    width_chunks: int = param(default=lambda op: 16 * -(-op.out_width // (16 * SIDE)))
    height_chunks: int = param(default=lambda op: 16 * -(-op.out_height // (16 * SIDE)))
    patch_rows: int = param(default=lambda op: op.padded_rows())
    interpolation: Interpolation = param(default=Interpolation.BICUBIC)
    # bfloat16 patches, or a uint8 image.
    dtype: Any = param(default=bfloat16, repr=False)
    # What a core writes at a time: a patch, or its patch columns of an image row.
    piece: int = param(
        derive=lambda op: (
            op.patch_columns * SIDE * 3 if op.writes_image else SIDE * SIDE * 3
        ),
        init=False,
    )
    # The processor's normalization after its rescale by 1 / 255, per
    # channel, or None for the rescale alone.
    mean: tuple[float, ...] | None = param(default=None, array=True)
    std: tuple[float, ...] | None = param(default=None, array=True)
    num_aie_columns: int = tunable(domain=widths)
    num_channels: int = tunable(default=2, domain=widths)

    rows = per_call(bounds=height)
    columns = per_call(bounds=width)
    out_rows = per_call(bounds=out_height)
    out_columns = per_call(bounds=out_width)

    image = In(image_chunks, chunk, dtype=np.uint8, obj_shape=(chunk,))
    taps_w = In(width_chunks, words, dtype=np.int32, obj_shape=(words,))
    # Through taps_w's stream, after it.
    taps_h = In(height_chunks, words, dtype=np.int32)
    patches = Out(
        patch_rows,
        SIDE * SIDE * 3,
        dtype=dtype,
        obj_shape=(piece,),
        per=(num_aie_columns, num_channels),
    )

    src_rows = per_call(derive=lambda op: op.rows)
    src_columns = per_call(derive=lambda op: op.columns)
    dst_rows = per_call(derive=lambda op: op.out_rows)
    dst_columns = per_call(derive=lambda op: op.out_columns)
    image_count = per_call(derive=lambda op: op.rows * -(-3 * op.columns // op.chunk))
    width_count = per_call(derive=lambda op: -(-op.out_columns // SIDE))
    height_count = per_call(derive=lambda op: -(-op.out_rows // SIDE))
    patch_count = per_call(
        derive=lambda op: -(-op.out_rows // SIDE)
        * (-(-op.out_columns // SIDE) // op.cores + 1)
    )
    # The rows of a uint8 image a call writes, its bands'.
    image_rows = per_call(derive=lambda op: -(-op.out_rows // SIDE) * SIDE)

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    @property
    def writes_image(self) -> bool:
        """It writes a uint8 image, not bf16 patches."""
        return np.dtype(self.dtype) == np.uint8

    @property
    def pitch(self) -> int:
        """The bytes of a row of the uint8 image it writes."""
        return self.patch_columns * self.cores * SIDE * 3

    def default_patch_columns(self) -> int:
        """Patch columns a core holds: `out_width`'s split over the cores,
        and for bf16 patches a zero one past them.
        """
        dev = self.dev
        cols = self.num_aie_columns or (dev.cols if dev is not None else 8)
        cores = cols * self.num_channels
        strips = -(-self.out_width // SIDE)
        return -(-strips // cores) if self.writes_image else strips // cores + 1

    def padded_rows(self) -> int:
        """Every band's patch columns, padded past the cores: a uint8
        image's every core's `patch_columns`.
        """
        dev = self.dev
        cols = self.num_aie_columns or (dev.cols if dev is not None else 8)
        cores = cols * self.num_channels
        per = self.patch_columns if self.writes_image else self.default_patch_columns()
        return -(-self.out_height // SIDE) * per * cores

    def levels(self) -> np.ndarray:
        """Each uint8 level's bf16 bits, a row per channel, or one row if
        they agree: the rescale by 1 / 255, or with `mean` the normalization
        fused with it as Hugging Face's torchvision backend fuses them, in
        float32, rounded once.
        """
        if self.mean is None:
            return PIXELS.view(np.uint16)[None]
        level, scale = np.arange(256, dtype=np.float32), np.float32(255)
        rows = np.stack(
            [
                (level - np.float32(m) * scale) / (np.float32(s) * scale)
                for m, s in zip(self.mean, self.std)
            ]
        )
        rows = rows.astype(bfloat16).view(np.uint16)
        return rows[:1] if (rows == rows[0]).all() else rows

    @property
    def window_cap(self) -> int:
        """The widest filter window a chunk of `words` holds 16 of."""
        return 2 * ((self.words - HEADER) // SIDE - 2) - 1

    def held(self, dev) -> int:
        """Core memory a core of `dev` holds at `patch_columns`."""
        cols, win = self.patch_columns, self.window_cap
        plane = (5 * win + 8 + 64 + 63) // 64 * 64
        row = (cols * SIDE * 3 + 63) // 64 * 64  # LINE
        kernel = (
            14 * 4  # resize_setup's own scalars
            + cols * SIDE * 4  # hstart
            + cols * SIDE * 64 * 2  # hweight, two taps vectors a slot
            + 2 * cols * 4  # span0, span
            + cols * 3 * plane  # line
            + win * row  # mid
            + SIDE * row  # hold
            + 2 * self.levels().size  # PIXEL
        )
        item = np.dtype(self.dtype).itemsize
        buffers = (
            2 * self.chunk  # image, depth 2
            + 2 * self.words * 4  # taps, depth 2
            + 2 * self.piece * item  # patches, depth 2
            + 8 * 4  # counts
        )
        return kernel + buffers + dev.default_core_stack_bytes

    def validate(self) -> None:
        if min(self.height, self.width) < 1 or min(self.out_height, self.out_width) < 1:
            raise ValueError(
                f"Resample: {self.height}x{self.width} -> "
                f"{self.out_height}x{self.out_width}; every size must be at least 1"
            )
        if (self.mean is None) != (self.std is None) or (
            self.mean is not None and (len(self.mean) != 3 or len(self.std) != 3)
        ):
            raise ValueError(
                f"Resample: a mean {self.mean} and std {self.std} are both None or "
                f"one per channel"
            )

    def resolve(self, dev):
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: self.patch_rows % (c * self.num_channels) == 0,
        )
        return self.replace(num_aie_columns=cols)

    def compatible(self) -> None:
        cap = self.window_cap
        for n_in, n_out in (
            (self.width, self.out_width),
            (self.height, self.out_height),
        ):
            taps_window = window(n_in, n_out, self.interpolation)
            if taps_window > cap:
                raise ValueError(
                    f"Resample: {n_in} -> {n_out} samples is a "
                    f"{taps_window}-tap window; {self.words}-word chunks hold {cap}"
                )
        strips, bands = -(-self.out_width // SIDE), -(-self.out_height // SIDE)
        nmax = (
            -(-strips // self.cores) if self.writes_image else strips // self.cores + 1
        )
        if nmax > self.patch_columns:
            raise ValueError(
                f"Resample: {strips} patch columns over {self.cores} cores is "
                f"{nmax} a core; a core holds {self.patch_columns}"
            )
        written = self.patch_columns if self.writes_image else nmax
        if (dev := self.dev) is not None:
            held = self.held(dev)
            if held > dev.core_memory_bytes:
                raise ValueError(
                    f"Resample: {self.patch_columns} patch columns of "
                    f"{self.words}-word chunks and {self.chunk}-byte rows hold "
                    f"{held} bytes a core, past its {dev.core_memory_bytes}"
                )
        for name, have, need in (
            (
                "image_chunks",
                self.image_chunks,
                self.height * -(-3 * self.width // self.chunk),
            ),
            ("width_chunks", self.width_chunks, strips),
            ("height_chunks", self.height_chunks, bands),
            ("patch_rows", self.patch_rows, bands * written * self.cores),
        ):
            if have < need:
                raise ValueError(f"Resample: {name} ({have}) must be at least {need}")

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
        patches=None,
    ):
        """The image's patches, or its uint8 image's rows of `pitch` bytes;
        given `patches`, written over its leading rows, the ones a call
        writes, the rest kept.
        """
        h = self.height if rows is None else int(rows)
        w = self.width if columns is None else int(columns)
        ho = self.out_height if out_rows is None else int(out_rows)
        wo = self.out_width if out_columns is None else int(out_columns)
        line = -(-3 * w // self.chunk) * self.chunk
        pixels = np.asarray(image).reshape(-1)[: h * line].reshape(h, line)
        out = resize(pixels[:, : 3 * w].reshape(h, w, 3), ho, wo, self.interpolation)
        bands, strips = -(-ho // SIDE), -(-wo // SIDE)
        edge = ((0, bands * SIDE - ho), (0, strips * SIDE - wo), (0, 0))
        out = np.pad(out, edge, mode="edge")
        if self.writes_image:
            canvas = np.zeros((bands * SIDE, self.pitch // 3, 3), np.uint8)
            canvas[:, : strips * SIDE] = out
            written = canvas.reshape(-1, SIDE * SIDE * 3)
        else:
            pad = (strips // self.cores + 1) * self.cores
            grid = out.reshape(bands, SIDE, strips, SIDE, 3).transpose(0, 2, 1, 3, 4)
            levels = self.levels()
            # Each channel's pixels through its row of levels; zero past them.
            written = np.zeros((bands, pad, SIDE, SIDE, 3), np.uint16)
            written[:, :strips] = levels[np.arange(3) % len(levels), grid]
            written = written.view(bfloat16).reshape(bands * pad, SIDE * SIDE * 3)
        if patches is None:
            return written
        patches[: len(written)] = written
        return patches

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def sequence(self, rt):
        """The image, then both tables down one stream, and each core's
        patches: into a uint8 image's rows, a band each repeat.
        """
        tg = TaskGroup()
        moves = [
            (self.image, None, self.image, "image_count", 0, 1),
            (self.taps_w, None, self.taps_w, "width_count", 0, 1),
            (self.taps_w, None, self.taps_h, "height_count", 0, 1),
        ] + [
            (self.patches, k, self.patches, "patch_count", k, self.cores)
            for k in range(0 if self.writes_image else self.cores)
        ]
        for operand, lane, buffer, name, first, step in moves:
            per_call = self.value(name).per_call
            n, width = buffer.shape
            count = n // step if per_call else self.residents[name]
            tap = TensorAccessPattern(
                (n, width), first * width, [1, count, 1, width], [0, step * width, 0, 1]
            )
            length = self.value(name) if per_call else None
            if operand.drains:
                operand.drain(
                    tap,
                    lane=lane,
                    group=tg,
                    wait=True,
                    length_parameter=length,
                    length_unit=width,
                )
            else:
                operand.fill(
                    tap,
                    lane=lane,
                    group=tg,
                    source=buffer,
                    length_parameter=length,
                    length_unit=width,
                )
        if self.writes_image:
            rows = self.value("image_rows")
            n, width = self.patches.shape
            count = (
                n * width // self.pitch
                if rows.per_call
                else self.residents["image_rows"]
            )
            run = SIDE * 3
            for k in range(self.cores):
                # Its patch columns of each row; the rows on D2, which has no wrap.
                tap = TensorAccessPattern(
                    (n, width),
                    k * run,
                    [1, count, self.patch_columns, run],
                    [0, self.pitch, self.cores * run, 1],
                )
                self.patches.drain(
                    tap,
                    lane=k,
                    group=tg,
                    wait=True,
                    length_parameter=rows if rows.per_call else None,
                    length_unit=self.piece,
                )
        tg.finish()

    def build(self) -> Built:
        cores = self.num_aie_columns * self.num_channels
        counts_ty = np.ndarray[(8,), np.dtype[np.int32]]
        taps_ty, image_ty, patch_ty = (
            self.taps_w.obj_type,
            self.image.obj_type,
            self.patches.obj_type,
        )
        levels = self.levels()
        setup_k = ExternalFunction(
            "resize_setup",
            source_string=RESIZE.replace(
                "@PIXELS@",
                ", ".join("{" + ", ".join(map(str, row)) + "}" for row in levels),
            ),
            arg_types=[counts_ty] + [np.int32] * 5,
            compile_flags=[
                f"-DWORDS={self.words}",
                f"-DCHUNK={self.chunk}",
                f"-DCOLS={self.patch_columns}",
                f"-DCORES={cores}",
                f"-DCHANNELS={len(levels)}",
                f"-DOUT8={int(self.writes_image)}",
            ],
            symbol_prefix=(
                f"resize_{self.words}_{self.chunk}_{self.patch_columns}_{cores}_"
                f"{'u8' if self.writes_image else 'bf16'}_"
                f"{hashlib.sha256(levels.tobytes()).hexdigest()[:8]}"
            ),
        )
        lib = setup_k.object_file
        take_k = lib.bind("resize_take", [taps_ty, np.int32])
        band_k = lib.bind("resize_band", [taps_ty, counts_ty])
        consume_k = lib.bind("resize_consume", [image_ty, taps_ty])
        emit = "resize_emit8" if self.writes_image else "resize_emit"
        emit_k = lib.bind(emit, [patch_ty, np.int32])
        finish_k = lib.bind("resize_finish", [counts_ty])
        of_image = ObjectFifo(image_ty, depth=2)
        of_taps = ObjectFifo(taps_ty, depth=2)
        of_patches = [ObjectFifo(patch_ty, depth=2) for k in range(cores)]

        sizes = [self.src_rows, self.src_columns, self.dst_rows, self.dst_columns]
        rtps = [Rtp(sizes) for _ in range(cores)]

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
        ):
            words = rtp.read()
            h, w, ho, wo = (words[v] for v in sizes)
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
                    Buffer(counts_ty),
                    setup_k,
                    take_k,
                    band_k,
                    consume_k,
                    emit_k,
                    finish_k,
                    rtps[k],
                ],
            )
            for k in range(cores)
        ]
        self.patches.bind([f.cons() for f in of_patches])
        self.image.bind(of_image.prod())
        self.taps_w.bind(of_taps.prod())
        return Built(workers, rtps)


POSITIONS = """
#include <stdint.h>

namespace {
int n, pad, across, wx, wy, tx, ty;
}

// Block `b` of the patches in pooling-window order: (x, y) side by side in
// xy, x then POSITIONS + y in position, and the patch's row of Resample's
// raster in order. Past the image, or for a size that is not whole windows,
// ids past each table, which a bounded gather never reads, and the raster's
// zero patch.
extern "C" void patch_positions(int32_t *out, int32_t b, int32_t count, int32_t ho,
                                int32_t wo) {
    int32_t *xy = out, *position = out + 2 * BLOCK, *order = out + 4 * BLOCK;
    if (b == 0) {
        unsigned bands = ho > 0 ? (unsigned)ho / SIDE : 0;
        unsigned strips = wo > 0 ? (unsigned)wo / SIDE : 0;
        uint64_t all = (uint64_t)bands * strips;
        bool ok = ho % SIDE == 0 && wo % SIDE == 0 && all > 0 && bands % POOL == 0 &&
                  strips % POOL == 0 && all <= (uint64_t)count * BLOCK;
        n = ok ? (int)all : 0;
        pad = (strips / CORES + 1) * CORES;
        across = strips / POOL;
        wx = wy = tx = ty = 0;
    }
    for (int r = 0, i = b * BLOCK; r < BLOCK; r++, i++) {
        if (i < n) {
            int x = POOL * tx + wx, y = POOL * ty + wy;
            xy[2 * r] = position[r] = x;
            xy[2 * r + 1] = y;
            position[BLOCK + r] = POSITIONS + y;
            order[r] = y * pad + x;
            if (++wx < POOL)
                continue;
            wx = 0;
            if (++wy < POOL)
                continue;
            wy = 0;
            if (++tx < across)
                continue;
            tx = 0;
            ty++;
        } else {
            xy[2 * r] = xy[2 * r + 1] = POSITIONS;
            position[r] = position[BLOCK + r] = 2 * POSITIONS;
            order[r] = pad - 1;
        }
    }
}
"""


class PatchPositions(Operator):
    """Where each of `rows` patch rows of the vision tower comes from, for
    an image resized to `out_rows` by `out_columns` pixels.

    The patches are in pooling-window order; `order` is each one's row of
    `Resample`'s raster. Rows past the image hold `positions`,
    `2 * positions`, past each table, which a gather bounded to the image's
    patches never reads, and the raster's zero patch.
    """

    test = Testing(
        [
            Case(dict(rows=2560, out_height=672, out_width=912), bench=True),
            # Whole: no padding, and 48 patch columns on 16 cores.
            Case(dict(rows=2304, out_height=768, out_width=768)),
            Case(dict(rows=256, out_height=48, out_width=48)),
            Case(dict(rows=2048, out_height=480, out_width=1056, cores=8)),
        ],
    )

    rows: int = param()
    out_height: int = param()
    out_width: int = param()
    pool: int = param(default=3, array=True)
    # The rows of each axis's position-embedding table.
    positions: int = param(default=10240, array=True)
    # Resample's cores, which its raster's columns are padded past.
    cores: int = param(default=16, array=True)
    block: int = param(default=256)

    out_rows = per_call(bounds=out_height)
    out_columns = per_call(bounds=out_width)

    xy = Out(rows, 2, dtype=np.int32, obj_shape=(block, 2))
    position_ids = Out(2, rows, dtype=np.int32, obj_shape=(2, block))
    order = Out(rows, dtype=np.int32, obj_shape=(block,))

    count = per_call(derive=lambda op: op.rows // op.block)
    dst_rows = per_call(derive=lambda op: op.out_rows)
    dst_columns = per_call(derive=lambda op: op.out_columns)

    def validate(self) -> None:
        side = SIDE * self.pool
        if (
            self.out_height % side
            or self.out_width % side
            or not (0 < self.out_height * self.out_width // SIDE**2 <= self.rows)
        ):
            raise ValueError(
                f"PatchPositions: {self.out_height}x{self.out_width} is not whole "
                f"{side}-pixel windows of at most {self.rows} patches"
            )

    def compatible(self) -> None:
        if self.rows % self.block:
            raise ValueError(
                f"PatchPositions: rows ({self.rows}) are not whole "
                f"{self.block}-row blocks"
            )

    def ops(self) -> int:
        return 0  # index arithmetic: its figure is latency

    def reference(self, *, out_rows=None, out_columns=None):
        ho = self.out_height if out_rows is None else int(out_rows)
        wo = self.out_width if out_columns is None else int(out_columns)
        T, P, k = self.rows, self.positions, self.pool
        bands, strips = max(ho, 0) // SIDE, max(wo, 0) // SIDE
        pad = (strips // self.cores + 1) * self.cores
        xy = np.full((T, 2), P, np.int32)
        position_ids = np.full((2, T), 2 * P, np.int32)
        order = np.full(T, pad - 1, np.int32)
        whole = not (ho % SIDE or wo % SIDE or bands % k or strips % k)
        if whole and 0 < bands * strips <= T:
            y, x = np.divmod(np.arange(bands * strips), strips)
            token = x // k + strips // k * (y // k)
            o = np.lexsort((x % k, y % k, token))
            x, y = x[o], y[o]
            xy[: o.size] = np.stack([x, y], axis=-1)
            position_ids[0, : o.size], position_ids[1, : o.size] = x, P + y
            order[: o.size] = y * pad + x
        return xy, position_ids, order

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def sequence(self, rt):
        """`xy` and `order` as the core writes them; `position_ids` a block's
        x into the first half and its y into the second.
        """
        T, B = self.rows, self.block
        tg = TaskGroup()
        self.xy.drain(group=tg, wait=True)
        self.position_ids.drain(
            TensorAccessPattern((2, T), 0, [1, T // B, 2, B], [0, B, T, 1]),
            group=tg,
            wait=True,
        )
        self.order.drain(group=tg, wait=True)
        tg.finish()

    def build(self) -> Built:
        B = self.block
        record_ty = np.ndarray[(5 * B,), np.dtype[np.int32]]
        kernel = ExternalFunction(
            "patch_positions",
            source_string=POSITIONS,
            arg_types=[record_ty] + [np.int32] * 4,
            compile_flags=[
                f"-DSIDE={SIDE}",
                f"-DPOOL={self.pool}",
                f"-DPOSITIONS={self.positions}",
                f"-DCORES={self.cores}",
                f"-DBLOCK={B}",
            ],
            symbol_prefix=(
                f"patch_positions_{self.pool}_{self.positions}_{self.cores}_{B}"
            ),
        )
        outs = (self.xy, self.position_ids, self.order)
        # A core has two output channels: a memtile splits its record into three.
        of_record = ObjectFifo(record_ty, depth=2)
        parts = of_record.cons().split(
            [0, 2 * B, 4 * B],
            obj_types=[out.obj_type for out in outs],
            depths=[2, 2, 2],
        )
        counts = [self.count, self.dst_rows, self.dst_columns]
        rtp = Rtp(counts)

        def core_fn(record, kernel_fn, rtp):
            words = rtp.read()
            n, ho, wo = (words[v] for v in counts)
            for b in range_(n):
                kernel_fn(record.acquire(1), b, n, ho, wo)
                record.release(1)

        worker = Worker(core_fn, [of_record.prod(), kernel, rtp])
        for out, part in zip(outs, parts):
            out.bind(part.cons())
        return Built([worker], [rtp])
