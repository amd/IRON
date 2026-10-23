# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every model that is not a decoder records, device-free, at its toy
shape, and every step of every version resolves on the device: none of a
model's call path hides host compute or a shape the device refuses. The
decoders' reference tests check the same (``Decoder``'s
``test_every_step_of_every_version_resolves``).

Each model is built from a toy ``Checkpoint`` of its own tensor names and
shapes, filled with drawn weights (``.tree("random")``) and loaded through
the model's own ``__init__`` and ``load_state_dict`` or ``load_layers``.
"""

import dataclasses

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.embedding_gemma2.model import AudioTower as EGAudioTower
from iron.applications.embedding_gemma2.model import Config as EmbeddingGemmaConfig
from iron.applications.embedding_gemma2.model import EmbeddingGemma
from iron.applications.embedding_gemma2.model import Multimodal as EmbeddingGemma2
from iron.applications.embedding_gemma2.model import VisionTower as EGVisionTower
from iron.applications.gemma4.audio import AudioConfig, AudioTower
from iron.applications.gemma4.vision import VisionConfig, VisionTower
from iron.applications.idefics3.model import (
    SmolVLM,
    SmolVLMConfig,
    SmolVLMTextConfig,
)
from iron.applications.idefics3.vision.model import VisionConfig as SmolVLMVisionConfig
from iron.applications.idefics3.vision.model import VisionTower as SmolVLMVisionTower
from iron.applications.qwen3_embedding.model import Qwen3Embedding, Qwen3EmbeddingConfig
from iron.applications.resnet.model import ResNet, ResNetConfig
from iron.applications.whisper.model import Whisper, WhisperConfig
from iron.applications.yolox.model import YOLOXNano
from iron.common.declare.operator import Operator
from iron.lm import DecoderConfig, Multimodal
from iron.tests.support.llama_model import checkpoint, shapes

pytestmark = pytest.mark.usefixtures("npu2")


def steps(model, calls: list[dict] | None = None) -> list[Operator]:
    """Every step's operator, over every version ``calls`` lists, or
    ``model.shapes()``'s for a ``Model`` with no single shape of its own.
    """
    out = []
    for call in calls if calls is not None else model.shapes():
        out += [step.op for step in model.record(**call).steps]
    return out


def assert_on_npu(model, calls: list[dict] | None = None) -> None:
    """Every step of every version of ``model`` resolves on the bound device."""
    recorded = steps(model, calls)
    assert recorded, f"{type(model).__name__}: no steps recorded"
    dev = aie_utils.get_current_device()
    for op in recorded:
        op.resolved(dev)


QWEN3 = Qwen3EmbeddingConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
)


def names_qwen3(c: DecoderConfig) -> dict[str, tuple[int, ...]]:
    out = shapes(c)
    for i in range(c.num_hidden_layers):
        a = f"model.layers.{i}.self_attn"
        out |= {
            f"{a}.q_norm.weight": (c.head_dim,),
            f"{a}.k_norm.weight": (c.head_dim,),
        }
    return out


# ---------------------------------------------------------------------------
# Encoders with no tower of their own.


def test_qwen3_embedding_is_on_npu():
    named = {k.removeprefix("model."): v for k, v in names_qwen3(QWEN3).items()}
    weights = checkpoint(QWEN3, named).tree("random")
    assert_on_npu(Qwen3Embedding(QWEN3, weights))


RESNET = ResNetConfig(
    embedding_size=64,
    hidden_sizes=(256, 512, 1024, 2048),
    depths=(2, 1, 1, 1),
    image_size=96,
    num_labels=10,
)


def names_resnet(c: ResNetConfig) -> dict[str, tuple[int, ...]]:
    """Each float tensor of a ResNet checkpoint of ``c``'s shape, by name;
    every BatchNorm also holds an int64 ``num_batches_tracked``.
    """
    out = {}

    def conv(path, cin, cout, k=1):
        out[f"{path}.convolution.weight"] = (cout, cin, k, k)
        for name in ("weight", "bias", "running_mean", "running_var"):
            out[f"{path}.normalization.{name}"] = (cout,)

    conv("resnet.embedder.embedder", 3, c.embedding_size, 7)
    widths = (c.embedding_size, *c.hidden_sizes)
    for s, depth in enumerate(c.depths):
        for i in range(depth):
            p = f"resnet.encoder.stages.{s}.layers.{i}"
            cin, cout = widths[s + 1] if i else widths[s], widths[s + 1]
            if cin != cout or (s and not i):
                conv(f"{p}.shortcut", cin, cout)
            conv(f"{p}.layer.0", cin, cout // 4)
            conv(f"{p}.layer.1", cout // 4, cout // 4, 3)
            conv(f"{p}.layer.2", cout // 4, cout)
    out["classifier.1.weight"] = (c.num_labels, c.hidden_sizes[-1])
    out["classifier.1.bias"] = (c.num_labels,)
    return out


def test_resnet_is_on_npu():
    # ResNet is a plain Graph, not a Model: one shape, no shapes().
    named = names_resnet(RESNET)
    weights = checkpoint(RESNET, named).tree("random")
    for name in named:
        if name.endswith("normalization.weight"):
            node = weights
            for part in name.split(".")[:-1]:
                node = node[int(part)] if part.isdigit() else getattr(node, part)
            node.num_batches_tracked = np.zeros((), np.int64)
    model = ResNet(RESNET, weights)
    S = RESNET.image_size // 2 + 3
    assert_on_npu(model, [dict(image=((S, S * 16), bfloat16))])


def _base_conv(path, cin, cout, k=1, groups=1) -> dict[str, tuple[int, ...]]:
    # bn.num_batches_tracked (int64, scalar) is set directly on the loaded
    # tree below: one checkpoint holds one dtype.
    return {
        f"{path}.conv.weight": (cout, cin // groups, k, k),
        f"{path}.bn.weight": (cout,),
        f"{path}.bn.bias": (cout,),
        f"{path}.bn.running_mean": (cout,),
        f"{path}.bn.running_var": (cout,),
    }


def _dwconv(path, cin, cout, k=3) -> dict[str, tuple[int, ...]]:
    return _base_conv(f"{path}.dconv", cin, cin, k, groups=cin) | _base_conv(
        f"{path}.pconv", cin, cout
    )


def _bottleneck(path, channels) -> dict[str, tuple[int, ...]]:
    return _base_conv(f"{path}.conv1", channels, channels) | _dwconv(
        f"{path}.conv2", channels, channels
    )


def _csp_layer(path, cin, cout, depth) -> dict[str, tuple[int, ...]]:
    hidden = cout // 2
    out = (
        _base_conv(f"{path}.conv1", cin, hidden)
        | _base_conv(f"{path}.conv2", cin, hidden)
        | _base_conv(f"{path}.conv3", 2 * hidden, cout)
    )
    for i in range(depth):
        out |= _bottleneck(f"{path}.m.{i}", hidden)
    return out


def _spp(path, channels) -> dict[str, tuple[int, ...]]:
    hidden = channels // 2
    return _base_conv(f"{path}.conv1", channels, hidden) | _base_conv(
        f"{path}.conv2", hidden * 4, channels
    )


def _prediction(path, cin, cout) -> dict[str, tuple[int, ...]]:
    return {f"{path}.weight": (cout, cin, 1, 1), f"{path}.bias": (cout,)}


def names_yolox() -> dict[str, tuple[int, ...]]:
    """Every tensor of YOLOX-Nano's own (fixed, no-config) checkpoint, by
    name: its backbone (``CSPDarknet``), neck (``PAFPN``) and head, mirrored
    from ``applications/yolox/model.py``'s own widths.
    """
    w = 16
    out = _base_conv("model.backbone.backbone.stem.conv", 12, w, 3)
    out |= _dwconv("model.backbone.backbone.dark2.0", w, 2 * w, 3)
    out |= _csp_layer("model.backbone.backbone.dark2.1", 2 * w, 2 * w, 1)
    out |= _dwconv("model.backbone.backbone.dark3.0", 2 * w, 4 * w, 3)
    out |= _csp_layer("model.backbone.backbone.dark3.1", 4 * w, 4 * w, 3)
    out |= _dwconv("model.backbone.backbone.dark4.0", 4 * w, 8 * w, 3)
    out |= _csp_layer("model.backbone.backbone.dark4.1", 8 * w, 8 * w, 3)
    out |= _dwconv("model.backbone.backbone.dark5.0", 8 * w, 16 * w, 3)
    out |= _spp("model.backbone.backbone.dark5.1", 16 * w)
    out |= _csp_layer("model.backbone.backbone.dark5.2", 16 * w, 16 * w, 1)
    n = 64
    out |= _base_conv("model.backbone.lateral_conv0", 4 * n, 2 * n)
    out |= _csp_layer("model.backbone.C3_p4", 4 * n, 2 * n, 1)
    out |= _base_conv("model.backbone.reduce_conv1", 2 * n, n)
    out |= _csp_layer("model.backbone.C3_p3", 2 * n, n, 1)
    out |= _dwconv("model.backbone.bu_conv2", n, n, 3)
    out |= _csp_layer("model.backbone.C3_n3", 2 * n, 2 * n, 1)
    out |= _dwconv("model.backbone.bu_conv1", 2 * n, 2 * n, 3)
    out |= _csp_layer("model.backbone.C3_n4", 4 * n, 4 * n, 1)
    widths, hidden, classes = (n, 2 * n, 4 * n), n, 80
    for i, width in enumerate(widths):
        out |= _base_conv(f"model.head.stems.{i}", width, hidden)
        for branch in ("cls_convs", "reg_convs"):
            for j in range(2):
                out |= _dwconv(f"model.head.{branch}.{i}.{j}", hidden, hidden)
        out |= _prediction(f"model.head.cls_preds.{i}", hidden, classes)
        out |= _prediction(f"model.head.reg_preds.{i}", hidden, 4)
        out |= _prediction(f"model.head.obj_preds.{i}", hidden, 1)
    return out


def test_yolox_is_on_npu():
    # YOLOX has no config: its checkpoint's shape is its own, fixed; the
    # config checkpoint() takes is unused but for named=None's fallback.
    named = names_yolox()
    weights = checkpoint(QWEN3, named).tree("random")
    for name in named:
        if name.endswith("bn.weight"):
            node = weights
            for part in name[: -len(".weight")].split("."):
                node = node[int(part)] if part.isdigit() else getattr(node, part)
            node.num_batches_tracked = np.zeros((), np.int64)
    model = YOLOXNano(weights)
    assert_on_npu(model, [dict(image=((416, 416 * 4), bfloat16))])


# ---------------------------------------------------------------------------
# Towers, standalone.


SMOLVLM_VISION = SmolVLMVisionConfig(
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    intermediate_size=512,
    patch_size=16,
    # side**2 (the patch rows a call takes) is flm.ProjectionGEMM's M, a
    # multiple of 256; the reference test's 128 only runs through reference().
    image_size=256,
    scale_factor=2,
    text_dim=256,
    image_token=511,
)
SMOLVLM_TEXT = SmolVLMTextConfig(
    vocab_size=512,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    num_key_value_heads=2,
    head_dim=64,
    intermediate_size=512,
    rope_theta=1e5,
    max_seq_len=1024,
    prefill_chunk=256,
)


def names_smolvlm_vision(c: SmolVLMVisionConfig) -> dict[str, tuple[int, ...]]:
    E, F = c.hidden_size, c.intermediate_size
    v = "model.vision_model"
    out = {
        f"{v}.embeddings.patch_embedding.weight": (E, 3, c.patch_size, c.patch_size),
        f"{v}.embeddings.patch_embedding.bias": (E,),
        f"{v}.embeddings.position_embedding.weight": (c.side**2, E),
        f"{v}.post_layernorm.weight": (E,),
        f"{v}.post_layernorm.bias": (E,),
        "model.connector.modality_projection.proj.weight": (
            c.text_dim,
            E * c.scale_factor**2,
        ),
    }
    for i in range(c.num_hidden_layers):
        p = f"{v}.encoder.layers.{i}"
        for norm in ("layer_norm1", "layer_norm2"):
            out |= {f"{p}.{norm}.weight": (E,), f"{p}.{norm}.bias": (E,)}
        for proj in ("q_proj", "k_proj", "v_proj", "out_proj"):
            out |= {
                f"{p}.self_attn.{proj}.weight": (E, E),
                f"{p}.self_attn.{proj}.bias": (E,),
            }
        out |= {
            f"{p}.mlp.fc1.weight": (F, E),
            f"{p}.mlp.fc1.bias": (F,),
            f"{p}.mlp.fc2.weight": (E, F),
            f"{p}.mlp.fc2.bias": (E,),
        }
    return out


def names_smolvlm_text(c: SmolVLMTextConfig) -> dict[str, tuple[int, ...]]:
    text = {
        k.replace("model.", "model.text_model.", 1): v for k, v in shapes(c).items()
    }
    return text | {"lm_head.weight": (c.vocab_size, c.hidden_size)}


def test_smolvlm_vision_tower_is_on_npu():
    weights = checkpoint(SMOLVLM_TEXT, names_smolvlm_vision(SMOLVLM_VISION)).tree(
        "random"
    )
    assert_on_npu(SmolVLMVisionTower(SMOLVLM_VISION, weights))


# ---------------------------------------------------------------------------
# Whisper: an EncoderDecoder, its toy the device-free reference test's own
# (``tests/applications/whisper/test.py``), which builds both the encoder's
# and the decoder's tensors in one checkpoint, as Whisper's own __init__
# reads them.


WHISPER = WhisperConfig(
    vocab_size=512,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    num_key_value_heads=4,
    intermediate_size=512,
    max_seq_len=448,
    hidden_act="gelu_pytorch_tanh",
    encoder_layers=2,
    encoder_attention_heads=4,
    encoder_ffn_dim=512,
    num_mel_bins=64,
    max_source_positions=200,
)


def names_whisper(c: WhisperConfig) -> dict[str, tuple[int, ...]]:
    E, V = c.hidden_size, c.vocab_size
    out = {
        "model.encoder.conv1.weight": (E, c.num_mel_bins, 3),
        "model.encoder.conv1.bias": (E,),
        "model.encoder.conv2.weight": (E, E, 3),
        "model.encoder.conv2.bias": (E,),
        "model.encoder.embed_positions.weight": (c.max_source_positions, E),
        "model.encoder.layer_norm.weight": (E,),
        "model.encoder.layer_norm.bias": (E,),
        "model.decoder.embed_tokens.weight": (V, E),
        "model.decoder.embed_positions.weight": (c.max_seq_len, E),
        "model.decoder.layer_norm.weight": (E,),
        "model.decoder.layer_norm.bias": (E,),
    }
    stacks = [
        ("model.encoder", c.encoder_layers, c.encoder_ffn_dim, ["self_attn"]),
        (
            "model.decoder",
            c.num_hidden_layers,
            c.intermediate_size,
            ["self_attn", "encoder_attn"],
        ),
    ]
    for stack, layers, F, attentions in stacks:
        for i in range(layers):
            p = f"{stack}.layers.{i}"
            for a in attentions:
                for proj in ("q_proj", "k_proj", "v_proj", "out_proj"):
                    out[f"{p}.{a}.{proj}.weight"] = (E, E)
                    if proj != "k_proj":
                        out[f"{p}.{a}.{proj}.bias"] = (E,)
                for part in ("weight", "bias"):
                    out[f"{p}.{a}_layer_norm.{part}"] = (E,)
            out |= {
                f"{p}.fc1.weight": (F, E),
                f"{p}.fc1.bias": (F,),
                f"{p}.fc2.weight": (E, F),
                f"{p}.fc2.bias": (E,),
                f"{p}.final_layer_norm.weight": (E,),
                f"{p}.final_layer_norm.bias": (E,),
            }
    return out


def test_whisper_is_on_npu():
    weights = checkpoint(WHISPER, names_whisper(WHISPER)).tree("random")
    assert_on_npu(Whisper(WHISPER, weights))


# ---------------------------------------------------------------------------
# Multimodal: a text model and a tower, as one iron.lm.Multimodal.


def test_smolvlm_is_on_npu():
    named = names_smolvlm_text(SMOLVLM_TEXT) | names_smolvlm_vision(SMOLVLM_VISION)
    weights = checkpoint(SMOLVLM_TEXT, named).tree("random")
    fields = {
        f.name: getattr(SMOLVLM_TEXT, f.name) for f in dataclasses.fields(SMOLVLM_TEXT)
    }
    config = SmolVLMConfig(**fields, vision=SMOLVLM_VISION)
    assert_on_npu(SmolVLM(config, weights))


# ---------------------------------------------------------------------------
# Gemma 4's towers: their real names and shapes, read from the released
# checkpoints' safetensors headers (names and shapes only, no tensor data),
# at a toy config's own scale. Both read a few tensors as plain arrays
# rather than through load_state_dict (see the report alongside this test).


GEMMA4_VISION = VisionConfig(
    # hidden_size is pinned at 768: the patch pixels AXPY.step centres
    # before input_proj's own projection are SIDE * SIDE * 3 wide
    # (operators/resample/op.py's SIDE, 16, fixed, not patch_size),
    # matching the real checkpoint's own hidden_size.
    hidden_size=768,
    num_hidden_layers=2,
    num_attention_heads=12,
    head_dim=64,
    intermediate_size=512,
    patch_size=16,
    pooling_kernel_size=3,
    position_embedding_size=1024,
    text_dim=256,
    patches=512,
    largest=(256, 256),
    rows=256,
    chunk=512,
    patch_columns=8,
    use_clipped_linears=True,
)

GEMMA4_AUDIO = AudioConfig(
    hidden_size=256,
    num_attention_heads=4,
    intermediate_size=512,
    # GEMM's K: the first subsampling conv's banded kernel * mels, the
    # second's 3 * 3 * its in channels (the first's out channels, C0),
    # each a multiple of 64.
    mels=64,
    subsampling_conv_channels=(64, 16),
    window=8,
    band=32,
    conv_kernel_size=5,
    text_dim=256,
    # Deliberately not text_dim: output_proj_dims is the tower's own fixed
    # output width, embed_audio's projection into text_dim is rectangular,
    # not square, a real checkpoint caught square toy shapes missing.
    output_proj_dims=320,
    max_tokens=64,
)


def names_gemma4_vision(c: VisionConfig) -> dict[str, tuple[int, ...]]:
    """``VisionTower``'s own tensors, as the real checkpoint names them
    (``gemma-4-e2b/model.safetensors``'s header): the attention and MLP
    projections ``Clipped``, their clamp bounds read.
    """
    E, F, D = c.hidden_size, c.intermediate_size, c.head_dim
    Q = c.num_attention_heads * D
    out = {
        "vision_tower.patch_embedder.input_proj.weight": (E, E),
        "vision_tower.patch_embedder.position_embedding_table": (
            2,
            c.position_embedding_size,
            E,
        ),
        "embed_vision.embedding_projection.weight": (c.text_dim, E),
    }
    for i in range(c.num_hidden_layers):
        p = f"vision_tower.encoder.layers.{i}"
        out |= {
            f"{p}.input_layernorm.weight": (E,),
            f"{p}.self_attn.q_norm.weight": (D,),
            f"{p}.self_attn.k_norm.weight": (D,),
            f"{p}.post_attention_layernorm.weight": (E,),
            f"{p}.pre_feedforward_layernorm.weight": (E,),
            f"{p}.post_feedforward_layernorm.weight": (E,),
        }
        for name, (cin, cout) in {
            "self_attn.q_proj": (E, Q),
            "self_attn.k_proj": (E, Q),
            "self_attn.v_proj": (E, Q),
            "self_attn.o_proj": (Q, E),
            "mlp.gate_proj": (E, F),
            "mlp.up_proj": (E, F),
            "mlp.down_proj": (F, E),
        }.items():
            out |= _clipped(f"{p}.{name}", cin, cout)
    return out


def test_gemma4_vision_tower_is_on_npu():
    # "unread": q, k and v, and gate and up, clamp their input alike, which
    # bounds drawn at random do not.
    weights = checkpoint(QWEN3, names_gemma4_vision(GEMMA4_VISION)).tree("unread")
    assert_on_npu(VisionTower(GEMMA4_VISION, weights))


def _clipped(path: str, cin: int, cout: int) -> dict[str, tuple[int, ...]]:
    """A ``Clipped`` linear's own tensors: its weight and its four scalar
    clamp bounds, each ``iron.param()``-bound through load_state_dict like
    any other weight.
    """
    return {
        f"{path}.linear.weight": (cout, cin),
        f"{path}.input_min": (),
        f"{path}.input_max": (),
        f"{path}.output_min": (),
        f"{path}.output_max": (),
    }


def names_gemma4_audio(c: AudioConfig) -> dict[str, tuple[int, ...]]:
    """``AudioTower``'s own tensors, as the real checkpoint names them
    (``gemma-4-e2b/model.safetensors``'s header): each conformer layer's two
    feed-forwards, attention and light convolution, their ``Clipped``
    linears' weights and clamp bounds among them. ``subsample_conv_projection``'s
    two ``Conv2d`` kernels, ``output_proj`` and ``embed_audio`` are read as
    plain arrays at construction or call time, not through load_state_dict
    (see the report alongside this test); they still need real shapes here,
    since reading them happens regardless of how they were bound.
    """
    E, M, D = c.hidden_size, c.intermediate_size, c.head_dim
    C0, C1 = c.subsampling_conv_channels
    out = {
        "audio_tower.subsample_conv_projection.layer0.conv.weight": (C0, 1, 3, 3),
        "audio_tower.subsample_conv_projection.layer0.norm.weight": (C0,),
        "audio_tower.subsample_conv_projection.layer1.conv.weight": (C1, C0, 3, 3),
        "audio_tower.subsample_conv_projection.layer1.norm.weight": (C1,),
        "audio_tower.subsample_conv_projection.input_proj_linear.weight": (
            E,
            (c.mels // 4) * C1,
        ),
        "audio_tower.output_proj.weight": (c.output_proj_dims, E),
        "audio_tower.output_proj.bias": (c.output_proj_dims,),
        "embed_audio.embedding_projection.weight": (c.text_dim, c.output_proj_dims),
    }
    for i in range(c.num_hidden_layers):
        p = f"audio_tower.layers.{i}"
        for ff in ("feed_forward1", "feed_forward2"):
            out |= {
                f"{p}.{ff}.pre_layer_norm.weight": (E,),
                f"{p}.{ff}.post_layer_norm.weight": (E,),
            }
            out |= _clipped(f"{p}.{ff}.ffw_layer_1", E, M)
            out |= _clipped(f"{p}.{ff}.ffw_layer_2", M, E)
        out |= {
            f"{p}.norm_pre_attn.weight": (E,),
            f"{p}.norm_post_attn.weight": (E,),
            f"{p}.norm_out.weight": (E,),
            f"{p}.self_attn.relative_k_proj.weight": (E, E),
            f"{p}.self_attn.per_dim_scale": (D,),
        }
        for proj in ("q_proj", "k_proj", "v_proj", "post"):
            out |= _clipped(f"{p}.self_attn.{proj}", E, E)
        out |= {
            f"{p}.lconv1d.pre_layer_norm.weight": (E,),
            f"{p}.lconv1d.depthwise_conv1d.weight": (E, 1, c.conv_kernel_size),
            f"{p}.lconv1d.conv_norm.weight": (E,),
        }
        out |= _clipped(f"{p}.lconv1d.linear_start", E, 2 * E)
        out |= _clipped(f"{p}.lconv1d.linear_end", E, E)
    return out


def test_gemma4_audio_tower_is_on_npu():
    # "unread": q, k and v clamp their input alike, which bounds drawn at
    # random do not.
    weights = checkpoint(QWEN3, names_gemma4_audio(GEMMA4_AUDIO)).tree("unread")
    assert_on_npu(AudioTower(GEMMA4_AUDIO, weights))


# ---------------------------------------------------------------------------
# embedding_gemma2: a text encoder (its own PLE wiring, read as a plain
# array from a shared per-layer projection, not through load_state_dict
# either) with Gemma 4's two towers, as one iron.lm.Multimodal.


EMBEDDING_GEMMA = EmbeddingGemmaConfig(
    vocab_size=1024,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    intermediate_size=512,
    num_key_value_heads=2,
    head_dim=64,
    rope_theta=10000.0,
    layer_types=("sliding_attention", "full_attention"),
    global_kv_groups=1,
    global_head_dim=64,
    global_rope_theta=1000000.0,
    sliding_window=8,
    ple_dim=256,
    embedding_dim=256,
    max_tokens=512,
    block=64,
)


def names_embedding_gemma_text(c: EmbeddingGemmaConfig) -> dict[str, tuple[int, ...]]:
    E, F, P, L = c.hidden_size, c.intermediate_size, c.ple_dim, c.num_hidden_layers
    out = {
        "language_model.embed_tokens.weight": (c.vocab_size, E),
        "language_model.norm.weight": (E,),
        "language_model.embedding_projection.weight": (c.embedding_dim, E),
        "language_model.ple.per_layer_model_projection.weight": (L * P, E),
        "language_model.ple.per_layer_projection_norm.weight": (P,),
    }
    for i in range(L):
        G, D, _ = c.heads(i)
        Q, KV = c.num_attention_heads * D, G * D
        p = f"language_model.layers.{i}"
        out |= {
            f"{p}.input_layernorm.weight": (E,),
            f"{p}.self_attn.q_proj.weight": (Q, E),
            f"{p}.self_attn.k_proj.weight": (KV, E),
            f"{p}.self_attn.v_proj.weight": (KV, E),
            f"{p}.self_attn.o_proj.weight": (E, Q),
            f"{p}.self_attn.q_norm.weight": (D,),
            f"{p}.self_attn.k_norm.weight": (D,),
            f"{p}.post_attention_layernorm.weight": (E,),
            f"{p}.pre_feedforward_layernorm.weight": (E,),
            f"{p}.post_feedforward_layernorm.weight": (E,),
            f"{p}.mlp.gate_proj.weight": (F, E),
            f"{p}.mlp.up_proj.weight": (F, E),
            f"{p}.mlp.down_proj.weight": (E, F),
            f"{p}.per_layer_input_gate.weight": (P, E),
            f"{p}.per_layer_projection.weight": (E, P),
            f"{p}.post_per_layer_input_norm.weight": (E,),
            f"{p}.layer_scalar": (1,),
        }
    return out


def test_embedding_gemma2_is_on_npu():
    named = names_embedding_gemma_text(EMBEDDING_GEMMA)
    weights = checkpoint(QWEN3, named).tree("random")
    assert_on_npu(EmbeddingGemma(EMBEDDING_GEMMA, weights))


def test_embedding_gemma2_multimodal_is_on_npu():
    named = (
        names_embedding_gemma_text(EMBEDDING_GEMMA)
        | names_gemma4_vision(GEMMA4_VISION)
        | names_gemma4_audio(GEMMA4_AUDIO)
    )
    weights = checkpoint(QWEN3, named).tree("unread")
    text = EmbeddingGemma(EMBEDDING_GEMMA, weights)
    audio = EGAudioTower(GEMMA4_AUDIO, weights)
    vision = EGVisionTower(GEMMA4_VISION, weights)

    class _Multimodal(EmbeddingGemma2):
        def __init__(self, text, audio, vision):
            self.config, self.tokenizer = EMBEDDING_GEMMA, None
            Multimodal.__init__(
                self,
                text,
                {
                    EMBEDDING_GEMMA.audio_token: audio,
                    EMBEDDING_GEMMA.image_token: vision,
                },
            )

    assert_on_npu(_Multimodal(text, audio, vision))
