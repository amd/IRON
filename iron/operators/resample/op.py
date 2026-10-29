# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""torchvision's antialiased bicubic resize of a uint8 image into a vision
tower's bf16 patches, on the device bit for bit as torch computes it on the
CPU.

`ResampleTaps` computes one axis's filter table, `chunks` objects of `words`
int32 as `vision.resample_quantize` writes them, of which a call writes the
first its sizes fill (`ResampleTaps.filled`). `Resample` resizes an image
with two such tables into 16x16 patches of u8 / 255 (`vision.resize`), and
`PatchPositions` says where each of the tower's rows comes from in them
(`datamovement.patch_positions`).
"""

import math

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, ExternalFunction, In, ObjectFifo, Out, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import datamovement, vision
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import param, per_call, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing

HEADER = 4
SIDE = 16  # a patch's pixels on each axis, and the outputs of a taps chunk

# vision.resample_peak's and vision.resample_quantize's entry points in one
# object: the two factory objects each carry the float64 taps code, and
# together overflow a core's 16 KB of program memory.
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
    if (a.support > WMAX)
        return a;
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


def window(in_size: int, out_size: int) -> int:
    """The most input samples one output of a bicubic axis reads."""
    scale = in_size / out_size
    return math.ceil(2.0 * scale if scale >= 1.0 else 2.0) * 2 + 1


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
    `in_samples` samples to `out_samples`.

    Each core takes chunks `k, k + cores, ...` and computes their weights in
    float64 twice, as `vision.resample_peak` and `vision.resample_quantize`
    do: once for the largest weight, which a chain through the cores
    reduces, and once to quantize at the precision it sets.
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
        ],
    )

    in_size: int = param()
    out_size: int = param()
    words: int = param(default=256)
    # The slots of a chunk, or None for as many as the window lets fit.
    slots: int | None = param(default=None, array=True)
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
        return per_chunk(n_in, n_out, self.words, self.slots)

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
                f"{window(self.in_size, self.out_size)}-tap window"
            )

    def ops(self) -> int:
        return 0  # a table, not arithmetic over its words: its figure is latency

    def reference(self, *, in_samples=None, out_samples=None):
        n_in = self.in_size if in_samples is None else int(in_samples)
        n_out = self.out_size if out_samples is None else int(out_samples)
        # The kernels' references as one core writing every chunk: the table
        # does not depend on how the cores deal its chunks.
        filled = self.filled(n_in, n_out)
        kw = dict(words=self.words, cores=1, slots=self.slots)
        peak = vision.resample_peak_ref(n_in, n_out, 0, filled, **kw)
        table = np.zeros((self.chunks, self.words), np.int32)
        table[:filled] = vision.resample_quantize_ref(
            np.tile(peak, (filled, 1)), n_in, n_out, 0, filled, **kw
        )
        return table

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def sequence(self, rt):
        """Chunk `c` from core `c % cores`, the order the cores compute them in."""
        per_call = self.count.per_call
        n, words = self.table.shape
        count = n // self.cores if per_call else self.residents["count"]
        tg = rt.task_group()
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
        rt.finish(tg)

    def build(self) -> Built:
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
            "resample_quantize", [peak_ty, self.table.obj_type] + [np.int32] * 5
        )
        tables = self.table.fifos(self.table.depth)
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
                        tables[k],
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
        return Built(workers, rtps)


class Resample(Operator):
    """An image resized as torchvision's antialiased bicubic resize does it
    on the CPU, written as the vision tower's 16x16 patches of u8 / 255 in
    bf16 (`vision.resize`).

    Every core receives the image in `chunk`-byte chunks; core `k` owns
    patch columns `k, k + cores, ...`, resamples each row across them, then
    each band of 16 rows down them. Patch `(py, px)` is row `py * pad + px`
    of `patches`, `pad` the patch columns padded past the cores with zeros:
    row `pad - 1` is the zero patch padding gathers. The resized sizes are
    whole patches; a call's sizes that are not write zeros.
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
                ).reference(),
                op.taps_h: ResampleTaps(
                    in_size=op.height,
                    out_size=op.out_height,
                    words=op.words,
                    slots=SIDE,
                    chunks=op.height_chunks,
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
        dtype=bfloat16,
        obj_shape=(SIDE * SIDE * 3,),
        per=(num_aie_columns, num_channels),
    )

    src_rows = per_call(derive=lambda op: op.rows)
    src_columns = per_call(derive=lambda op: op.columns)
    dst_rows = per_call(derive=lambda op: op.out_rows)
    dst_columns = per_call(derive=lambda op: op.out_columns)
    image_count = per_call(derive=lambda op: op.rows * -(-3 * op.columns // op.chunk))
    width_count = per_call(derive=lambda op: op.out_columns // SIDE)
    height_count = per_call(derive=lambda op: op.out_rows // SIDE)
    patch_count = per_call(
        derive=lambda op: op.out_rows // SIDE * (op.out_columns // SIDE // op.cores + 1)
    )

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    def default_patch_columns(self) -> int:
        """Patch columns a core holds: `out_width`'s split over the cores and
        a zero one past them.
        """
        dev = self.dev
        cols = self.num_aie_columns or (dev.cols if dev is not None else 8)
        return self.out_width // SIDE // (cols * self.num_channels) + 1

    def padded_rows(self) -> int:
        """Every band's patch columns, padded past the cores."""
        dev = self.dev
        cols = self.num_aie_columns or (dev.cols if dev is not None else 8)
        cores = cols * self.num_channels
        return self.out_height // SIDE * self.default_patch_columns() * cores

    @property
    def window_cap(self) -> int:
        """The widest filter window a chunk of `words` holds 16 of."""
        return 2 * ((self.words - HEADER) // SIDE - 2) - 1

    def held(self, dev) -> int:
        """Core memory a core of `dev` holds at `patch_columns`."""
        cols, win = self.patch_columns, self.window_cap
        plane = (5 * win + 8 + 64 + 63) // 64 * 64
        row = (cols * SIDE * 3 + 31) // 32 * 32  # LINE
        kernel = (
            14 * 4  # resize_setup's own scalars
            + cols * SIDE * 4  # hstart
            + cols * SIDE * 64 * 2  # hweight, two taps vectors a slot
            + 2 * cols * 4  # span0, span
            + cols * 3 * plane  # line
            + win * row  # mid
            + SIDE * row  # hold
            + 2 * 256  # PIXEL
        )
        buffers = (
            2 * self.chunk  # image, depth 2
            + 2 * self.words * 4  # taps, depth 2
            + 2 * SIDE * SIDE * 3 * 2  # patches, depth 2
            + 5 * 4  # counts
        )
        return kernel + buffers + dev.default_core_stack_bytes

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
        return self.replace(num_aie_columns=cols)

    def compatible(self) -> None:
        cap = self.window_cap
        for n_in, n_out in (
            (self.width, self.out_width),
            (self.height, self.out_height),
        ):
            taps_window = window(n_in, n_out)
            if taps_window > cap:
                raise ValueError(
                    f"Resample: {n_in} -> {n_out} samples is a "
                    f"{taps_window}-tap window; {self.words}-word chunks hold {cap}"
                )
        strips, bands = self.out_width // SIDE, self.out_height // SIDE
        nmax = strips // self.cores + 1
        if nmax > self.patch_columns:
            raise ValueError(
                f"Resample: {strips} patch columns over {self.cores} cores is "
                f"{nmax} a core; a core holds {self.patch_columns}"
            )
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
            ("patch_rows", self.patch_rows, bands * nmax * self.cores),
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
        """The kernel's patches (`vision.resize_ref`); given `patches`,
        written over its leading rows, the ones a call writes, the rest kept.
        """
        written = vision.resize_ref(
            np.asarray(image),
            np.asarray(taps_w),
            np.asarray(taps_h),
            self.height if rows is None else int(rows),
            self.width if columns is None else int(columns),
            self.out_height if out_rows is None else int(out_rows),
            self.out_width if out_columns is None else int(out_columns),
            words=self.words,
            chunk=self.chunk,
            patch_columns=self.patch_columns,
            cores=self.cores,
        )
        if patches is None:
            return written
        patches[: len(written)] = written
        return patches

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def sequence(self, rt):
        """The image, then both tables down one stream, and each core's patches."""
        tg = rt.task_group()
        moves = [
            (self.image, None, self.image, "image_count", 0, 1),
            (self.taps_w, None, self.taps_w, "width_count", 0, 1),
            (self.taps_w, None, self.taps_h, "height_count", 0, 1),
        ] + [
            (self.patches, k, self.patches, "patch_count", k, self.cores)
            for k in range(self.cores)
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
        rt.finish(tg)

    def build(self) -> Built:
        cores = self.cores
        resize = vision.resize(
            self.words, chunk=self.chunk, patch_columns=self.patch_columns, cores=cores
        )
        counts_ty = np.ndarray[(5,), np.dtype[np.int32]]
        # image and taps are each one lane broadcast to every core: a fresh
        # cons() per core.
        (image_ends,) = self.image.fifos(self.image.depth, readers=cores)
        (taps_ends,) = self.taps_w.fifos(self.taps_w.depth, readers=cores)
        patches = self.patches.fifos(self.patches.depth)

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
                    image_ends[k],
                    taps_ends[k],
                    patches[k],
                    Buffer(counts_ty),
                    resize.resize_setup,
                    resize.resize_take,
                    resize.resize_band,
                    resize,
                    resize.resize_emit,
                    resize.resize_finish,
                    rtps[k],
                ],
            )
            for k in range(cores)
        ]
        return Built(workers, rtps)


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
        B = self.block
        record = datamovement.patch_positions_ref(
            self.rows // B,
            ho,
            wo,
            block=B,
            side=SIDE,
            pool=self.pool,
            positions=self.positions,
            cores=self.cores,
        )
        xy = record[:, : 2 * B].reshape(-1, 2)
        position_ids = record[:, 2 * B : 4 * B].reshape(-1, 2, B).transpose(1, 0, 2)
        order = record[:, 4 * B :].reshape(-1)
        return xy, position_ids.reshape(2, -1), order

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def sequence(self, rt):
        """`xy` and `order` as the core writes them; `position_ids` a block's
        x into the first half and its y into the second.
        """
        T, B = self.rows, self.block
        tg = rt.task_group()
        self.xy.drain(group=tg, wait=True)
        self.position_ids.drain(
            TensorAccessPattern((2, T), 0, [1, T // B, 2, B], [0, B, T, 1]),
            group=tg,
            wait=True,
        )
        self.order.drain(group=tg, wait=True)
        rt.finish(tg)

    def build(self) -> Built:
        B = self.block
        record_ty = np.ndarray[(5 * B,), np.dtype[np.int32]]
        kernel = datamovement.patch_positions(
            B, side=SIDE, pool=self.pool, positions=self.positions, cores=self.cores
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
