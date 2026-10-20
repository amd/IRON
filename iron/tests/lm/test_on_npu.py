# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every model records, device-free, at its toy shape, every step of every
version a device operator: none of a model's call path hides host compute
behind a step the device never runs. A step that is not one fails with its
class, so a future graph that slips in a bare numpy op is caught here
rather than on hardware.
"""

import dataclasses
from types import SimpleNamespace

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.applications.embedding_gemma2.model import AudioTower as EGAudioTower
from iron.applications.embedding_gemma2.model import Config as EmbeddingGemmaConfig
from iron.applications.embedding_gemma2.model import EmbeddingGemma
from iron.applications.embedding_gemma2.model import Multimodal as EmbeddingGemma2
from iron.applications.embedding_gemma2.model import VisionTower as EGVisionTower
from iron.applications.gemma3.model import Gemma3, Gemma3Config
from iron.applications.gemma4.audio import AudioConfig, AudioTower
from iron.applications.gemma4.model import Gemma4, Gemma4Config
from iron.applications.gemma4.vision import VisionConfig, VisionTower
from iron.applications.granite.model import Granite, GraniteConfig
from iron.applications.granite_hybrid.model import GraniteHybrid, GraniteHybridConfig
from iron.applications.idefics3.model import SmolVLM, SmolVLMText, SmolVLMTextConfig
from iron.applications.idefics3.vision.model import VisionConfig as SmolVLMVisionConfig
from iron.applications.idefics3.vision.model import VisionTower as SmolVLMVisionTower
from iron.applications.lfm2.model import Lfm2, Lfm2Config
from iron.applications.llama.model import Llama, LlamaConfig
from iron.applications.ministral3.model import Ministral3, Ministral3Config
from iron.applications.phi3.model import Phi4, Phi4Config
from iron.applications.qwen2.model import Qwen2, Qwen2Config
from iron.applications.qwen3.model import Qwen3
from iron.applications.qwen3_5.model import Qwen35, Qwen35Config
from iron.applications.qwen3_embedding.model import Qwen3Embedding
from iron.applications.qwen3_moe.model import Qwen3Moe, Qwen3MoeConfig
from iron.applications.resnet.model import ResNet, ResNetConfig
from iron.applications.smollm2.model import SmolLM2
from iron.applications.smollm3.model import SmolLM3, SmolLM3Config
from iron.applications.whisper.model import Whisper, WhisperConfig, WhisperEncoder
from iron.applications.yolox.model import YOLOXNano
from iron.common.declare.operator import Operator
from iron.lm import DecoderConfig, EncoderDecoder, Multimodal
from iron.tests.support.device_free import DeviceFreeWeights, Permissive
from iron.tests.support.llama_model import SMALL

pytestmark = pytest.mark.usefixtures("npu2")

#: ``DecoderConfig``'s own fields, SMALL's values of them: a shape every
#: plain decoder's operators already accept (GEMM's K, ProjectionGEMM's M,
#: MHA's d all multiples their operator needs), reused so every model's toy
#: shape needs no shape rule of its own to be worked out.
_BASE = {f.name: getattr(SMALL, f.name) for f in dataclasses.fields(DecoderConfig)}


def decoder(config_cls, **extra) -> DecoderConfig:
    """``config_cls`` at ``SMALL``'s own shape, ``extra`` its fields beyond
    ``DecoderConfig``'s.
    """
    fields = {f.name for f in dataclasses.fields(config_cls) if f.init}
    kwargs = {k: v for k, v in _BASE.items() if k in fields}
    kwargs.update(extra)
    return config_cls(**kwargs)


def zero(shape, dtype=bfloat16) -> np.ndarray:
    """A ``param``, zero in ``shape``: what a real checkpoint's tensor
    would be read as (``Checkpoint.tree``), for the few leaves a model
    reads as an array directly rather than through ``load_state_dict``.
    """
    return iron.param(np.zeros(shape, dtype))


def free(cls, config, weights=None):
    """``cls(config, weights)`` device-free: every weight its own zero, no
    checkpoint read. ``weights`` is ``Permissive()`` unless a model's
    ``__init__`` reads an array straight from it (Conv1d's kernel): then a
    caller gives the few leaves that need a real shape.
    """

    class _Free(DeviceFreeWeights, cls):
        pass

    return _Free(config, Permissive() if weights is None else weights)


def steps(model, calls: list[dict] | None = None) -> list[Operator]:
    """Every step's operator, over every version ``calls`` lists, or
    ``model.shapes()``'s for a ``Model`` with no single shape of its own.
    """
    out = []
    for shapes in calls if calls is not None else model.shapes():
        out += [step.op for step in model.record(**shapes).steps]
    return out


def assert_on_npu(model, calls: list[dict] | None = None) -> None:
    """Every step of every version of ``model`` is a device ``Operator``."""
    recorded = steps(model, calls)
    assert recorded, f"{type(model).__name__}: no steps recorded"
    not_device = [op for op in recorded if not isinstance(op, Operator)]
    assert not not_device, [
        f"{type(op).__module__}.{type(op).__name__}" for op in not_device
    ]


# ---------------------------------------------------------------------------
# Plain decoders: CausalLM subclasses with no tower or encoder of their own.


DECODERS = [
    (Llama, decoder(LlamaConfig)),
    (Qwen2, decoder(Qwen2Config)),
    (Qwen3, decoder(DecoderConfig)),
    (SmolLM2, decoder(LlamaConfig)),
    (Granite, decoder(GraniteConfig, attention_multiplier=0.1)),
    (Phi4, decoder(Phi4Config)),
    (Ministral3, decoder(Ministral3Config)),
    (
        SmolLM3,
        decoder(
            SmolLM3Config,
            no_rope_layers=tuple([1] * (SMALL.num_hidden_layers - 1) + [0]),
        ),
    ),
    (Gemma3, decoder(Gemma3Config)),
    (
        Gemma4,
        decoder(
            Gemma4Config, layer_types=("full_attention",) * SMALL.num_hidden_layers
        ),
    ),
    (
        Lfm2,
        decoder(
            Lfm2Config,
            full_attn_idxs=(SMALL.num_hidden_layers - 1,),
            block_ff_dim=SMALL.intermediate_size,
        ),
    ),
    (
        Qwen3Moe,
        decoder(
            Qwen3MoeConfig,
            num_experts=64,
            num_experts_per_tok=8,
            moe_intermediate_size=SMALL.intermediate_size,
            norm_topk_prob=True,
        ),
    ),
    (
        Qwen35,
        decoder(
            Qwen35Config,
            layer_types=("full_attention",)
            + ("linear_attention",) * (SMALL.num_hidden_layers - 1),
            linear_conv_kernel_dim=4,
            linear_key_head_dim=SMALL.head_dim,
            linear_value_head_dim=SMALL.head_dim,
            linear_num_key_heads=SMALL.num_key_value_heads,
            linear_num_value_heads=SMALL.num_attention_heads,
            partial_rotary_factor=1.0,
        ),
    ),
    (
        GraniteHybrid,
        decoder(
            GraniteHybridConfig,
            attention_multiplier=0.1,
            layer_types=("attention",) + ("mamba",) * (SMALL.num_hidden_layers - 1),
            shared_intermediate_size=SMALL.intermediate_size,
            mamba_n_heads=64,
            mamba_d_head=64,
            mamba_d_state=64,
        ),
    ),
]


@pytest.mark.parametrize(
    "model_cls,config", DECODERS, ids=[cls.__name__ for cls, _ in DECODERS]
)
def test_decoder_is_on_npu(model_cls, config):
    assert_on_npu(free(model_cls, config))


# ---------------------------------------------------------------------------
# Encoders with no tower of their own.


def test_qwen3_embedding_is_on_npu():
    config = decoder(DecoderConfig)
    weights = Permissive(
        embed_tokens=SimpleNamespace(
            weight=zero((config.vocab_size, config.hidden_size))
        )
    )
    assert_on_npu(free(Qwen3Embedding, config, weights=weights))


def test_resnet_is_on_npu():
    # ResNet is a plain Graph, not a Model: one shape, no shapes().
    config = ResNetConfig(
        embedding_size=64, hidden_sizes=(256,), depths=(1,), image_size=64
    )
    model = free(ResNet, config)
    S = config.image_size // 2 + 3
    assert_on_npu(model, [dict(image=((S, S * 16), bfloat16))])


def test_yolox_is_on_npu():
    # YOLOXNano is a plain Graph taking one positional argument, weights.
    class _Free(DeviceFreeWeights, YOLOXNano):
        pass

    model = _Free(Permissive(model=Permissive()))
    assert_on_npu(model, [dict(image=((416, 416 * 4), bfloat16))])


# ---------------------------------------------------------------------------
# Towers, standalone: each compiles to the NPU on its own, as embedding
# Gemma 2's Multimodal composes them.


@pytest.mark.skip(
    reason="VisionTower.__init__ reads the position table straight from its "
    "checkpoint (table[0][x_ids]), a shape device-free construction has not "
    "worked out yet; the tower's record() path is otherwise exercised by "
    "test_embedding_gemma2_is_on_npu once that is unblocked the same way"
)
def test_gemma4_vision_tower_is_on_npu():
    config = VisionConfig(patches=512, largest=(256, 256), rows=256, chunk=512)
    assert_on_npu(free(VisionTower, config))


@pytest.mark.skip(
    reason="AudioTower.__init__ reads two Conv2d kernels straight from its "
    "checkpoint (subsample_conv_projection.layer{0,1}.conv.weight), a shape "
    "device-free construction has not worked out yet"
)
def test_gemma4_audio_tower_is_on_npu():
    config = AudioConfig()
    assert_on_npu(free(AudioTower, config))


def _smolvlm_vision_config() -> SmolVLMVisionConfig:
    return SmolVLMVisionConfig(
        hidden_size=256,
        num_hidden_layers=2,
        num_attention_heads=4,
        intermediate_size=512,
        patch_size=16,
        image_size=256,
        scale_factor=2,
        text_dim=SMALL.hidden_size,
        image_token=999,
        head_dim=64,
    )


def _smolvlm_vision_weights(c: SmolVLMVisionConfig) -> Permissive:
    """The patch embedding and position table ``VisionTower.front`` reads
    as arrays directly, rather than through ``load_state_dict``.
    """
    embeddings = Permissive(
        patch_embedding=SimpleNamespace(
            weight=zero((c.hidden_size, 3, c.patch_size, c.patch_size)),
            bias=zero((c.hidden_size,)),
        ),
        position_embedding=SimpleNamespace(weight=zero((c.side**2, c.hidden_size))),
    )
    connector = Permissive(
        modality_projection=SimpleNamespace(
            proj=SimpleNamespace(
                weight=zero((c.text_dim, c.hidden_size * c.scale_factor**2))
            )
        )
    )
    return Permissive(
        model=Permissive(
            vision_model=Permissive(embeddings=embeddings), connector=connector
        )
    )


def test_smolvlm_vision_tower_is_on_npu():
    config = _smolvlm_vision_config()
    assert_on_npu(
        free(SmolVLMVisionTower, config, weights=_smolvlm_vision_weights(config))
    )


# ---------------------------------------------------------------------------
# Whisper: an EncoderDecoder, its encoder built and loaded on its own, then
# handed to EncoderDecoder.__init__ directly (Whisper's own __init__ builds
# its encoder inline from the same checkpoint, which a device-free
# checkpoint has no real tensors to split).


def _whisper_config() -> WhisperConfig:
    # head_dim (hidden_size / attention_heads) must be 64 (MHA's d); neither
    # WhisperConfig nor WhisperEncoderConfig takes a head_dim of its own.
    heads, hidden = 4, 256
    return WhisperConfig(
        vocab_size=SMALL.vocab_size,
        hidden_size=hidden,
        num_hidden_layers=SMALL.num_hidden_layers,
        num_attention_heads=heads,
        num_key_value_heads=heads,
        intermediate_size=SMALL.intermediate_size,
        max_seq_len=SMALL.max_seq_len,
        num_mel_bins=128,
        encoder_layers=SMALL.num_hidden_layers,
        encoder_attention_heads=heads,
        encoder_ffn_dim=SMALL.intermediate_size,
        max_source_positions=SMALL.max_seq_len,
        hidden_act="gelu_pytorch_tanh",
    )


def _whisper_encoder_weights(ec) -> Permissive:
    """The few leaves ``WhisperEncoder`` reads as arrays directly, rather
    than through ``load_state_dict``: its two convolutions' kernels and the
    position table, zero in their own shape.
    """
    kernel = 3
    return Permissive(
        model=Permissive(
            encoder=Permissive(
                conv1=SimpleNamespace(
                    weight=np.zeros(
                        (ec.hidden_size, ec.num_mel_bins, kernel), np.float32
                    ),
                    bias=np.zeros(ec.hidden_size, np.float32),
                ),
                conv2=SimpleNamespace(
                    weight=np.zeros(
                        (ec.hidden_size, ec.hidden_size, kernel), np.float32
                    ),
                    bias=np.zeros(ec.hidden_size, np.float32),
                ),
                embed_positions=SimpleNamespace(
                    weight=zero((ec.positions, ec.hidden_size))
                ),
            )
        )
    )


def test_whisper_encoder_is_on_npu():
    ec = _whisper_config().encoder()
    assert_on_npu(free(WhisperEncoder, ec, weights=_whisper_encoder_weights(ec)))


def test_whisper_is_on_npu():
    config = _whisper_config()
    ec = config.encoder()
    encoder = free(WhisperEncoder, ec, weights=_whisper_encoder_weights(ec))

    class _Whisper(DeviceFreeWeights, Whisper):
        pass

    model = _Whisper.__new__(_Whisper)
    EncoderDecoder.__init__(model, config, Permissive(), encoder)
    assert_on_npu(model)


# ---------------------------------------------------------------------------
# Multimodal composites: each sub-model built and loaded on its own (its
# outer class's own __init__ builds them inline from one checkpoint, which
# a device-free one has no real tensors to split either), then composed by
# Multimodal.__init__ directly.


def test_smolvlm_is_on_npu():
    text_config = decoder(SmolVLMTextConfig, tie_word_embeddings=False)
    vision_config = _smolvlm_vision_config()
    text = free(SmolVLMText, text_config)
    tower = free(
        SmolVLMVisionTower,
        vision_config,
        weights=_smolvlm_vision_weights(vision_config),
    )

    class _SmolVLM(DeviceFreeWeights, SmolVLM):
        pass

    model = _SmolVLM.__new__(_SmolVLM)
    Multimodal.__init__(model, text, {vision_config.image_token: tower})
    assert_on_npu(model)


@pytest.mark.skip(
    reason="EmbeddingGemma reads embed_tokens.weight straight from its "
    "checkpoint to prescale it, and its two towers are gemma4's (skipped "
    "above for the same reason): not worked out device-free yet"
)
def test_embedding_gemma2_is_on_npu():
    config = EmbeddingGemmaConfig(
        **{
            k: v
            for k, v in _BASE.items()
            if k in {f.name for f in dataclasses.fields(EmbeddingGemmaConfig)}
        }
    )
    text = free(EmbeddingGemma, config)
    audio_config = AudioConfig()
    vision_config = VisionConfig(patches=512, largest=(256, 256), rows=256, chunk=512)
    audio = free(EGAudioTower, audio_config)
    vision = free(EGVisionTower, vision_config)

    class _Multimodal(DeviceFreeWeights, EmbeddingGemma2):
        pass

    model = _Multimodal.__new__(_Multimodal)
    model.config, model.tokenizer = config, None
    Multimodal.__init__(
        model, text, {config.audio_token: audio, config.image_token: vision}
    )
    assert_on_npu(model)
