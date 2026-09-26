# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""DMA descriptor limits, and what a fit says against what the device does.

Each hardware case streams a 64-word buffer through one tile and drains what
that tile's DMA produced, so the output is exactly the access pattern under
test. A fit that says a pattern fits is built from the fit and must
reproduce the pattern on the device; a fit that says it does not is built
naively, as one descriptor holding the pattern as given, to pin what the
toolchain and the device do instead.
"""

from math import prod

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.dialects.aie import get_target_model
from aie.iron.device import from_name
from aie.utils import NPUKernel
from aie.utils.compile import compile_mlir_module
from ml_dtypes import bfloat16

from iron.common.dma import (
    BdLimits,
    Direction,
    DmaFacts,
    Fit,
    Reason,
    TileKind,
    Unfit,
    fit,
)
from iron.common import tiling
from iron.common.tiling import Access

N = 64
READ, WRITE = Direction.READ, Direction.WRITE
SHIM, MEM, CORE = TileKind.SHIM, TileKind.MEM, TileKind.CORE


def _indices(offset: int, dims) -> np.ndarray:
    grids = np.ix_(*(np.arange(n, dtype=np.int64) * s for n, s in dims))
    return (offset + sum(grids)).reshape(-1)


# -- the limits ---------------------------------------------------------------


@pytest.mark.parametrize("name, shims", [("npu1", 4), ("npu2", 8)])
def test_facts_are_the_target_models(name, shims):
    facts = DmaFacts.of(from_name(name, n_cols=None))
    assert facts.shim_tiles == shims
    assert facts.shim_channels(READ) == facts.shim_channels(WRITE) == 2 * shims
    assert facts[SHIM] == BdLimits(
        SHIM, 3, 1023, 1 << 20, (1 << 32) - 1, 64, 255, 16, 16, 2, 2, 4
    )
    assert facts[MEM] == BdLimits(
        MEM, 4, 1023, 1 << 17, (1 << 17) - 1, 64, 255, 48, 24, 6, 6, 4
    )
    assert facts[CORE] == BdLimits(
        CORE, 3, 255, 1 << 13, (1 << 14) - 1, 64, 255, 16, 16, 2, 2, 4
    )


@pytest.mark.parametrize("name", ["npu1", "npu2"])
def test_the_derived_sequence_uses_the_shims_limits(name):
    """tiling's shim constants are the target model's, on both devices."""
    dev = from_name(name, n_cols=None)
    shim = DmaFacts.of(dev)[SHIM]
    assert tiling.DMA_BD_MAX_WRAP == shim.wrap
    assert tiling._ITER_MAX == shim.iteration
    assert 1 << tiling._STRIDE_BITS == shim.step
    tm = get_target_model(dev.resolve())
    assert tiling._ADDR_GRANULE_BYTES * 8 == tm.get_address_gen_granularity()


@pytest.fixture(scope="module")
def facts():
    return DmaFacts.of(from_name("npu2", n_cols=None))


def _fit(dims, kind, direction, facts, dtype=np.int32, offset=0, elements=N):
    return fit(_indices(offset, dims), elements, dtype, kind, direction, facts[kind])


# -- fits, on paper -------------------------------------------------------------

TRANSPOSE = [(16, 1), (4, 16)]  # a 4 x 16 buffer read column by column


@pytest.mark.parametrize("kind", [MEM, CORE])
def test_a_transpose_is_one_tile_descriptor_for_32_bit_words_only(kind, facts):
    got = _fit(TRANSPOSE, kind, READ, facts)
    assert isinstance(got, Fit) and len(got.bds) == 1 and got.repeat == 0
    np.testing.assert_array_equal(got.bds[0].indices(), _indices(0, TRANSPOSE))
    # Two bf16 elements share a granule; no descriptor splits them.
    got = _fit(TRANSPOSE, kind, READ, facts, dtype=bfloat16)
    assert isinstance(got, Unfit) and got.reason is Reason.GRANULE


@pytest.mark.parametrize("kind", [MEM, CORE])
def test_an_outer_reread_is_the_channels_repeat_count(kind, facts):
    got = _fit([(3, 0), (64, 1)], kind, READ, facts)
    assert isinstance(got, Fit) and got.repeat == 2
    np.testing.assert_array_equal(got.bds[0].indices(), np.arange(64))
    got = _fit([(256, 0), (64, 1)], kind, READ, facts)
    assert got == Fit(kind, READ, got.bds, 255)
    got = _fit([(257, 0), (64, 1)], kind, READ, facts)
    assert isinstance(got, Unfit) and got.reason is Reason.REPEAT


@pytest.mark.parametrize("kind", [MEM, CORE])
def test_an_inner_reread_fits_no_tile_descriptor(kind, facts):
    got = _fit([(4, 16), (2, 0), (16, 1)], kind, READ, facts)
    assert isinstance(got, Unfit) and got.reason is Reason.INNER_REPEAT


def test_the_shim_rereads_an_inner_row_by_unrolling(facts):
    dims = [(4, 16), (2, 0), (16, 1)]
    got = _fit(dims, SHIM, READ, facts)
    assert isinstance(got, Fit) and len(got.bds) == 4
    assert all(b.sizes[0] == 2 and b.strides[0] == 0 for b in got.bds)
    np.testing.assert_array_equal(
        np.concatenate([b.indices() for b in got.bds]), _indices(0, dims)
    )
    # Unrolled past the shim's descriptors, it no longer fits.
    got = _fit([(17, 64), (2, 0), (16, 1)], SHIM, READ, facts, elements=17 * 64)
    assert isinstance(got, Unfit) and got.reason is Reason.BDS


@pytest.mark.parametrize("kind", [SHIM, MEM, CORE])
def test_a_write_must_be_injective(kind, facts):
    for dims in ([(2, 0), (64, 1)], [(4, 16), (2, 0), (16, 1)]):
        got = _fit(dims, kind, WRITE, facts)
        assert isinstance(got, Unfit) and got.reason is Reason.NOT_INJECTIVE


def test_tile_kinds_differ_in_dims_and_wrap(facts):
    four = [(2, 64), (2, 24), (2, 10), (8, 1)]  # no two levels nest
    wide = [(2, 1), (257, 2)]  # prime, and over a core's 8-bit wrap
    assert isinstance(_fit(four, MEM, READ, facts, elements=128), Fit)
    got = _fit(four, CORE, READ, facts, elements=128)
    assert isinstance(got, Unfit) and got.reason is Reason.DIMS
    assert isinstance(_fit(wide, MEM, READ, facts, elements=600), Fit)
    got = _fit(wide, CORE, READ, facts, elements=600)
    assert isinstance(got, Unfit) and got.reason is Reason.WRAP
    # A wide dimension that factors takes a free dimension instead.
    got = _fit([(2, 1), (300, 2)], CORE, READ, facts, elements=600)
    assert isinstance(got, Fit)
    assert got.bds[0].sizes[1:] == (2, 2, 150) and got.bds[0].strides[1:] == (1, 300, 2)
    # One contiguous run needs no dimension at all, only a length.
    got = _fit([(4096, 1)], CORE, READ, facts, elements=4096)
    assert isinstance(got, Fit) and got.bds[0].sizes == (1, 1, 1, 4096)


def test_what_no_nest_visits_does_not_fit(facts):
    got = fit(np.array([0, 5, 1]), N, np.int32, MEM, READ, facts[MEM])
    assert isinstance(got, Unfit) and got.reason is Reason.NOT_A_NEST


# -- on the device --------------------------------------------------------------


def _dims_attr(dims) -> str:
    return (
        f" sizes = [{', '.join(str(n) for n, _ in dims)}]"
        f" strides = [{', '.join(str(s) for _, s in dims)}]"
    )


def _access_dims(acc: Access):
    return list(zip(acc.sizes, acc.strides))


def _design(
    tile: TileKind,
    *,
    tile_read=None,
    repeat: int = 0,
    tile_write=None,
    shim_reads=None,
    shim_writes=None,
    in_n: int = N,
    out_n: int = N,
    elem: str = "i32",
) -> str:
    """shim -> tile buffer (N words) -> shim, one flow each way.

    ``tile_read``/``tile_write`` are the tile's MM2S/S2MM descriptor dims;
    ``shim_reads``/``shim_writes`` are per-task shim descriptors.
    """
    coord, dma = {MEM: ("(0, 1)", "aie.memtile_dma"), CORE: ("(0, 2)", "aie.mem")}[tile]
    buf = f"memref<{N}x{elem}>"
    read_len = prod(n for n, _ in tile_read) if tile_read else N
    write_len = prod(n for n, _ in tile_write) if tile_write else N
    streamed_out = read_len * (repeat + 1)
    rd = _dims_attr(tile_read) if tile_read else ""
    wr = _dims_attr(tile_write) if tile_write else ""
    rep = f", repeat_count = {repeat}" if repeat else ""

    def tasks(arg, total, accesses, direction, default_len):
        if accesses is None:
            accesses = [None]
        out = []
        for k, acc in enumerate(accesses):
            last = k == len(accesses) - 1
            bd = (
                f"aie.dma_bd(%{arg} : memref<{total}x{elem}> offset = 0 len = {default_len})"
                if acc is None
                else f"aie.dma_bd(%{arg} : memref<{total}x{elem}> offset = {acc.offset}"
                f" len = {acc.count}{_dims_attr(_access_dims(acc))})"
            )
            token = " {issue_token = true}" if direction == "S2MM" and last else ""
            out.append(
                f"""      %{arg}{k} = aiex.dma_configure_task(%shim, {direction}, 0) {{
        {bd}
        aie.end
      }}{token}
      aiex.dma_start_task(%{arg}{k})"""
            )
        return "\n".join(out), f"%{arg}{len(accesses) - 1}"

    drains, last = tasks("out", out_n, shim_writes, "S2MM", streamed_out)
    fills, _ = tasks("in", in_n, shim_reads, "MM2S", write_len)
    return f"""
module {{
  aie.device(npu2) @empty {{ }}
  aie.device(npu2) @test {{
    %shim = aie.tile(0, 0)
    %t = aie.tile{coord}
    %buf = aie.buffer(%t) {{sym_name = "buf"}} : {buf}
    %full = aie.lock(%t, 0) {{init = 0 : i32, sym_name = "lk_full"}}
    %empty = aie.lock(%t, 1) {{init = 1 : i32, sym_name = "lk_empty"}}
    aie.flow(%shim, DMA : 0, %t, DMA : 0)
    aie.flow(%t, DMA : 0, %shim, DMA : 0)
    %dma = {dma}(%t) {{
      %c1 = arith.constant 1 : i32
      %cr = arith.constant {repeat + 1} : i32
      %0 = aie.dma_start(S2MM, 0, ^fill, ^send_entry)
    ^fill:
      aie.use_lock(%empty, AcquireGreaterEqual, %c1)
      aie.dma_bd(%buf : {buf} offset = 0 len = {write_len}{wr})
      aie.use_lock(%full, Release, %cr)
      aie.next_bd ^end
    ^send_entry:
      %1 = aie.dma_start(MM2S, 0, ^send, ^end{rep})
    ^send:
      aie.use_lock(%full, AcquireGreaterEqual, %c1)
      aie.dma_bd(%buf : {buf} offset = 0 len = {read_len}{rd})
      aie.use_lock(%empty, Release, %c1)
      aie.next_bd ^end
    ^end:
      aie.end
    }}
    aie.runtime_sequence @sequence(%in : memref<{in_n}x{elem}>, %out : memref<{out_n}x{elem}>) {{
      aiex.npu.load_pdi {{ device_ref = @empty }}
      aiex.npu.load_pdi {{ device_ref = @test }}
{drains}
{fills}
      aiex.dma_await_task({last})
    }}
  }}
}}
"""


def _build(tmp_path, mlir: str):
    elf = tmp_path / "aie.elf"
    compile_mlir_module(mlir, full_elf_path=elf, work_dir=tmp_path)
    return NPUKernel(elf_path=elf, kernel_name="test:sequence")


def _run(kernel, data: np.ndarray, out_n: int) -> np.ndarray:
    tin = aie_utils.tensor(data)
    tout = aie_utils.tensor(np.full(out_n, -1, dtype=data.dtype))
    aie_utils.DefaultNPURuntime.load_and_run(kernel, [tin, tout])
    # numpy() maps the buffer object, which is freed with ``tout``.
    return tout.numpy().copy()


def _data(n: int = N) -> np.ndarray:
    return (np.arange(n, dtype=np.int32) * 7 + 1000).astype(np.int32)


TILE_READS = {
    "transpose": TRANSPOSE,
    "outer_reread": [(3, 0), (64, 1)],
    "outer_reread_transposed": [(2, 0), (16, 1), (4, 16)],
    "inner_reread": [(4, 16), (2, 0), (16, 1)],
}


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("kind", [MEM, CORE])
@pytest.mark.parametrize("pattern", sorted(TILE_READS))
def test_a_tile_read_fits_exactly_when_the_device_reproduces_it(
    kind, pattern, facts, tmp_path, npu_runtime
):
    dims = TILE_READS[pattern]
    want = _data()[_indices(0, dims)]
    got = _fit(dims, kind, READ, facts)
    if isinstance(got, Fit):
        (acc,) = got.bds
        dims_fit = [(n, s) for n, s in _access_dims(acc) if n != 1]
        kernel = _build(
            tmp_path,
            _design(kind, tile_read=dims_fit, repeat=got.repeat, out_n=want.size),
        )
        np.testing.assert_array_equal(_run(kernel, _data(), want.size), want)
        return
    # Not fitting is the toolchain's verdict too: no descriptor holds a
    # zero stride, and the verifier says so.
    assert got.reason is Reason.INNER_REPEAT
    with pytest.raises(
        RuntimeError, match="Invalid step size; must be a positive integer"
    ):
        _build(tmp_path, _design(kind, tile_read=dims, out_n=want.size))


@pytest.mark.parametrize("kind", [MEM, CORE])
def test_a_bf16_transpose_is_the_toolchains_granule_error_too(kind, facts, tmp_path):
    got = _fit(TRANSPOSE, kind, READ, facts, dtype=bfloat16)
    assert isinstance(got, Unfit) and got.reason is Reason.GRANULE
    with pytest.raises(RuntimeError, match="inner-most dim stride must be 1"):
        _build(tmp_path, _design(kind, tile_read=TRANSPOSE, elem="bf16"))


SHIM_READS = {  # each 64 elements of a 128-element input
    "outer_reread": [(2, 0), (32, 1)],
    "inner_reread": [(2, 16), (2, 0), (16, 1)],
    "row_halves": [(8, 16), (8, 1)],
}


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("pattern", sorted(SHIM_READS))
def test_a_shim_read_fit_reproduces_on_the_device(
    pattern, facts, tmp_path, npu_runtime
):
    dims = SHIM_READS[pattern]
    idx = _indices(0, dims)
    got = fit(idx, 2 * N, np.int32, SHIM, READ, facts[SHIM])
    assert isinstance(got, Fit)
    kernel = _build(tmp_path, _design(CORE, shim_reads=list(got.bds), in_n=2 * N))
    np.testing.assert_array_equal(_run(kernel, _data(2 * N), N), _data(2 * N)[idx])


@pytest.mark.supported_devices("npu2")
def test_the_toolchain_builds_a_write_that_is_not_injective(
    facts, tmp_path, npu_runtime
):
    """Why the injectivity rule is ours: a shim write that lands two copies
    on one region builds and runs, and the last copy wins."""
    dims = [(2, 0), (64, 1)]
    got = fit(_indices(0, dims), N, np.int32, SHIM, WRITE, facts[SHIM])
    assert isinstance(got, Unfit) and got.reason is Reason.NOT_INJECTIVE
    raw = Access(N, 0, (2, 1, 1, 64), (0, 0, 0, 1))
    kernel = _build(tmp_path, _design(CORE, repeat=1, shim_writes=[raw], out_n=N))
    np.testing.assert_array_equal(_run(kernel, _data(), N), _data())
