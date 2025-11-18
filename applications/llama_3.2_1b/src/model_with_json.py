# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
import json
from pathlib import Path
from src.block.transformer import TransformerBlock
from src.operator.rope import compute_rope_params
from rich.console import Console
from rich.text import Text


def dtype_from_string(inp):
    if isinstance(inp, torch.dtype):
        return inp
    return {"bfloat16": torch.bfloat16, "float16": torch.float16}.get(
        inp, torch.float32
    )


# fmt: off
# Configuration flag key -> (type function, default value, description)
config_options = {
    "dtype":                        (dtype_from_string, torch.float32, "Data type"),
    "use_kv_cache":                 (bool,              False,         "[Model] KV Cache"),
    "use_aie_gemv":                 (bool,              False,         "[Decode] GEMV"),
    "use_aie_rope":                 (bool,              False,         "[Attention] Rope"),
    "use_aie_attn_projection_gemm": (bool,              False,         "[Attention] QKV GEMM"),
    "use_aie_regular_mha":          (bool,              False,         "[Attention] Regular MHA"),
    "use_aie_fused_mha":            (bool,              False,         "[Attention] Fused MHA"),
    "use_aie_ffn_gemm":             (bool,              False,         "[FFN] GEMM"),
    "use_aie_ffn_mul":              (bool,              False,         "[FFN] Elementwise Mul"),
    "use_aie_ffn_silu":             (bool,              False,         "[FFN] SiLU"),
    "use_aie_residual":             (bool,              False,         "[Transformer] Residual Addition"),
    "use_aie_norm1":                (bool,              False,         "[Transformer] Pre Norm"),
    "use_aie_norm2":                (bool,              False,         "[Transformer] Post Norm"),
    "use_aie_final_norm":           (bool,              False,         "[Transformer] Final Norm"),
    "use_aie_final_gemm":           (bool,              False,         "[Transformer] Final GEMM"),   
}
# fmt: on


def load_llama_config(config_path=None):
    """Load Llama configuration from JSON file"""
    if config_path is None:
        # Default to config.json in the llama directory
        config_path = Path(__file__).parent.parent / "llama32_1b.json"

    with open(config_path, "r") as f:
        config = json.load(f)

    model_config = config["model_config"].copy()
    for key, (type_fn, default_value, description) in config_options.items():
        if key in model_config:
            model_config[key] = type_fn(model_config[key])
        else:
            model_config[key] = default_value

    return model_config


def print_config(cfg, console=Console()):
    def format_option(name, value):
        if isinstance(value, bool):
            checkmark = "[green]✔[/green]" if value else "[red]✘[/red]"
            return f"{name} {checkmark}"
        return f"{name}: {value}"

    dont_print = {"dtype"}
    # The following options are mutually exclusive, e.g. regular and fused MHA
    # cannot be enabled at the same time. But it looks bad to have red Xs,
    # indicating things are running on the CPU when they are not. So, we only
    # print one of these mutually exclusive options.
    if cfg["use_aie_fused_mha"]:
        dont_print |= {"use_aie_regular_mha"}
    else:
        dont_print |= {"use_aie_fused_mha"}

    console.print(
        "AIE Configuration ([green]✔[/green] = AIE NPU / [red]✘[/red] = CPU):",
        style="bold underline",
    )
    for option_key, (option_ty, option_default, option_name) in config_options.items():
        if option_key in dont_print:
            continue
        console.print(format_option(option_name, cfg.get(option_key, option_default)))
    console.print("")


class Llama3ModelWithJSONConfig(nn.Module):
    """Llama3 model that loads configuration from JSON file"""

    def __init__(
        self,
        config_path=None,
        prompt_length=0,
        num_tokens=1,
    ):
        super().__init__()

        # Load configuration from JSON
        self.cfg = load_llama_config(config_path)
        self.prompt_length = prompt_length
        self.num_tokens = num_tokens
        print_config(self.cfg)

        # Main model parameters
        self.tok_emb = nn.Embedding(
            self.cfg["vocab_size"], self.cfg["emb_dim"], dtype=self.cfg["dtype"]
        )

        self.trf_blocks = nn.ModuleList(
            [
                TransformerBlock(
                    self.cfg,
                    prompt_length=prompt_length,
                    num_tokens=num_tokens,
                )
                for i in range(self.cfg["n_layers"])
            ]
        )

        # Create final norm - either AIE or PyTorch
        if self.cfg.get("use_aie_final_norm", False):
            from src.operator.aie_rms_norm import AIERMSNorm

            self.final_norm = AIERMSNorm(
                emb_dim=self.cfg["emb_dim"],
                eps=1e-5,
                num_columns=8,
                num_channels=2,
                tile_size=self.cfg["emb_dim"],
            )
            # TODO: Add logging
        else:
            self.final_norm = nn.RMSNorm(
                self.cfg["emb_dim"], eps=1e-5, dtype=self.cfg["dtype"]
            )

        # Depedns on use_aie_final_gemm
        self.out_head = nn.Linear(
            self.cfg["emb_dim"],
            self.cfg["vocab_size"],
            bias=False,
            dtype=self.cfg["dtype"],
        )

        # Reusable utilities
        cos, sin = compute_rope_params(
            head_dim=self.cfg["emb_dim"] // self.cfg["n_heads"],
            theta_base=self.cfg["rope_base"],
            context_length=self.cfg["context_length"],
            freq_config=self.cfg["rope_freq"],
        )
        angles = torch.cat([torch.empty_like(cos), torch.empty_like(cos)], dim=1)
        angles[:, ::2] = cos
        angles[:, 1::2] = sin
        self.register_buffer("angles", angles, persistent=False)

    def forward(self, in_idx, input_pos=None, use_kv_cache=False):
        # Forward pass
        tok_embeds = self.tok_emb(in_idx)
        x = tok_embeds

        num_tokens = x.shape[1]

        # During generation phase with KV cache, don't create a mask
        # The attention layer will handle masking based on position
        if use_kv_cache and input_pos is not None:
            mask = None
        else:
            # During prefill, create standard causal mask
            mask = torch.triu(
                torch.ones(num_tokens, num_tokens, device=x.device, dtype=torch.bool),
                diagonal=1,
            )

        for block in self.trf_blocks:
            x = block(x, mask, self.angles, input_pos)

        x = self.final_norm(x)

        logits = self.out_head(x.to(self.cfg["dtype"]))

        return logits
