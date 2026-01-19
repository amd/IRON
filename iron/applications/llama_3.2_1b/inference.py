#!/usr/bin/env python3
# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
from pathlib import Path

# Add IRON repository root to Python path
repo_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

import argparse
import time
import torch
from src.model_with_json import Llama3ModelWithJSONConfig

# from src.model import Llama3Model
from src.tokenizer import Tokenizer, ChatFormat
from safetensors.torch import load_file
import os
import shutil
import logging
from collections import deque

from iron.operators.common import AIEOperatorBase
from src.utils import (
    model_memory_size,
    load_weights_into_llama,
    text_to_token_ids,
    token_ids_to_text,
    clean_text,
    generate,
)

# Global logger for profiling
_profile_logger = None


def profile_function_calls(frame, event, arg):
    """
    Profile function that logs start and end times of every function call.

    Args:
        frame: The current stack frame
        event: The event type ('call', 'return', 'c_call', 'c_return', 'c_exception')
        arg: Event-specific argument
    """
    global _profile_logger

    if _profile_logger is None:
        return

    func_name = frame.f_code.co_name
    filename = frame.f_code.co_filename
    line_no = frame.f_lineno

    # Create a readable function identifier
    func_identifier = f"{filename}:{func_name}:{line_no}"

    if event == "call":
        # Function is being called
        timestamp = time.perf_counter()
        _profile_logger.debug(f"[CALL] {func_identifier} started at {timestamp:.9f}")

    elif event == "return":
        # Function is returning
        timestamp = time.perf_counter()
        _profile_logger.debug(f"[RETURN] {func_identifier} ended at {timestamp:.9f}")

    return profile_function_calls


def enable_profiling(logs_dir_name):
    """Enable function call profiling using sys.setprofile."""
    global _profile_logger

    # Create a dedicated logger for profiling
    _profile_logger = logging.getLogger("function_profiler")
    _profile_logger.setLevel(logging.DEBUG)
    # Prevent propagation to root logger to avoid console output
    _profile_logger.propagate = False

    # Create log file for profiling data
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        logs_dir_name,
        f"profile_{timestamp}.log",
    )

    # Add file handler for profiling (only file, no console output)
    profile_handler = logging.FileHandler(log_path)
    profile_handler.setLevel(logging.DEBUG)
    profile_formatter = logging.Formatter("%(asctime)s - %(message)s")
    profile_handler.setFormatter(profile_formatter)
    _profile_logger.addHandler(profile_handler)

    # Set the profile function
    sys.setprofile(profile_function_calls)
    _profile_logger.info("Function profiling enabled")

    # Explicitly call profile_function_calls to log this function's call
    import inspect

    frame = inspect.currentframe()
    profile_function_calls(frame, "call", None)


def disable_profiling():
    """Disable function call profiling."""
    global _profile_logger

    sys.setprofile(None)
    if _profile_logger:
        _profile_logger.info("Function profiling disabled")
        # Close all handlers
        for handler in _profile_logger.handlers[:]:
            handler.close()
            _profile_logger.removeHandler(handler)


_iron_chat = r"""
        /$$$$$$ /$$$$$$$   /$$$$$$  /$$   /$$
       |_  $$_/| $$__  $$ /$$__  $$| $$$ | $$
         | $$  | $$  \ $$| $$  \ $$| $$$$| $$
         | $$  | $$$$$$$/| $$  | $$| $$ $$ $$
         | $$  | $$__  $$| $$  | $$| $$  $$$$
         | $$  | $$  \ $$| $$  | $$| $$\  $$$
        /$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$
       |______/|__/  |__/ \______/ |__/  \__/
                                            
                                            
 /$$       /$$        /$$$$$$  /$$      /$$  /$$$$$$ 
| $$      | $$       /$$__  $$| $$$    /$$$ /$$__  $$
| $$      | $$      | $$  \ $$| $$$$  /$$$$| $$  \ $$
| $$      | $$      | $$$$$$$$| $$ $$/$$ $$| $$$$$$$$
| $$      | $$      | $$__  $$| $$  $$$| $$| $$__  $$
| $$      | $$      | $$  | $$| $$\  $ | $$| $$  | $$
| $$$$$$$$| $$$$$$$$| $$  | $$| $$ \/  | $$| $$  | $$
|________/|________/|__/  |__/|__/     |__/|__/  |__/
"""


def setup_logging(verbosity):
    """Set up logging based on verbosity level."""

    # Ensure the logs directory is created in case of profiling
    logs_dir_name = "logs"
    if not os.path.exists(logs_dir_name):
        os.makedirs(logs_dir_name)

    if verbosity != 0:
        levels = {
            4: logging.DEBUG,
            3: logging.INFO,
            2: logging.WARNING,
            # 1: log everything (DEBUG) to a file
        }

        # Create log file
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        log_file = f"logs/inference_{timestamp}.log"

        handlers = [logging.FileHandler(log_file)]
        if verbosity > 0:
            handlers.append(logging.StreamHandler(sys.stderr))
            handlers[-1].setLevel(levels[verbosity])

        # Configure root logger
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=handlers,
            force=True,  # Override any existing configuration
        )

    return logs_dir_name


def save_layer_data(module, input, output, name, input_data_path, output_data_path):
    for count, i in enumerate(input):
        torch.save(
            i.detach(),
            f"{input_data_path}/{name}_input_{count}_{input[0].size()[1]}_toks.pt",
        )
    torch.save(
        output.detach(), f"{output_data_path}/{name}_output_{output.size()[1]}_toks.pt"
    )


def inference(
    weights_file_path,
    tokenizer_file_path,
    num_tokens,
    prompt,
    use_prompt_template,
    save_outputs,
    chat: bool,
    prompt_len: int = 64,
):
    """
    Main function to load a Llama3 model, process input, and generate output text.
    """
    logging.info("Weights file path: %s", weights_file_path)
    logging.info("Tokenizer file path: %s", tokenizer_file_path)
    logging.info("Number of tokens: %d", num_tokens)
    logging.debug("Prompt: %s", prompt)
    logging.info("Use prompt template: %s", use_prompt_template)
    logging.info("Save outputs: %s", save_outputs)
    torch.manual_seed(1608560892)
    input_data_path = "results/inputs"
    output_data_path = "results/outputs"

    tokenizer = Tokenizer(tokenizer_file_path)

    print(_iron_chat)
    if chat:
        prompt = input("Enter your prompt: ").strip()
    print("")

    logging.info(f"Loading model and tokenizer...")
    token_ids = text_to_token_ids(prompt, tokenizer)[:, :prompt_len]
    truncated_prompt = token_ids_to_text(token_ids, tokenizer)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "configs", "llama32_1b.json")
    model = Llama3ModelWithJSONConfig(
        config_path=config_path,
        prompt_length=prompt_len,
        num_tokens=num_tokens,
    )
    logging.info("Model and tokenizer loaded.")

    # Important: Set the seed again after initialization of the model. Each
    # call that initializes an nn.Linear layer updates the RNG state, because
    # weights are initialized with random values. For different JSON
    # configurations, we initialize a different number of linear layers,
    # so different configurations result in a different RNG state here. Since
    # we use random numbers to sample from the token distribution during
    # inference, it is important to have the same RNG state between runs so we
    # can have reproducible results across configurations.
    torch.manual_seed(1608560892)

    hook_handles = []
    if save_outputs:
        if os.path.exists(output_data_path):
            shutil.rmtree(output_data_path)
        os.makedirs(output_data_path)
        if os.path.exists(input_data_path):
            shutil.rmtree(input_data_path)
        os.makedirs(input_data_path)
        for name, module in model.named_modules():
            handle = module.register_forward_hook(
                lambda module, input, output, name=name, input_data_path=input_data_path, output_data_path=output_data_path: (
                    save_layer_data(
                        module, input, output, name, input_data_path, output_data_path
                    )
                )
            )
            hook_handles.append(handle)

    device = torch.device("cpu")
    model.to(device)
    chat_tokenizer = ChatFormat(tokenizer)

    total_params = sum(p.numel() for p in model.parameters())
    total_params_normalized = total_params - model.tok_emb.weight.numel()
    logging.info(f"Total number of parameters: {total_params:,}")
    logging.info(f"Total number of unique parameters: {total_params_normalized:,}")
    logging.info(
        f"float32 (PyTorch default): {model_memory_size(model, input_dtype=torch.float32):.2f} GB"
    )
    logging.info(
        f"bfloat16: {model_memory_size(model, input_dtype=torch.bfloat16):.2f} GB"
    )

    combined_weights = load_file(weights_file_path)
    # Get parameters from model config
    model_config = {
        "n_layers": model.cfg["n_layers"],
        "emb_dim": model.cfg["emb_dim"],
        "n_heads": model.cfg["n_heads"],
        "n_kv_groups": model.cfg["n_kv_groups"],
        "vocab_size": model.cfg["vocab_size"],
        "context_length": model.cfg["context_length"],
        "hidden_dim": model.cfg["hidden_dim"],
        "rope_base": model.cfg["rope_base"],
        "dtype": model.cfg["dtype"],
        "rope_freq": model.cfg["rope_freq"],
    }
    load_weights_into_llama(model, model_config, combined_weights)
    model.to(device)
    del combined_weights

    logging.info("Preparing AIE operators...")
    # At this point the model is fully described (operators and their dimensions and how to compile them)
    AIEOperatorBase.get_default_context().compile_all()
    AIEOperatorBase.get_default_context().prepare_runtime()
    logging.info("AIE operator preparation completed.")
    print(f"Starting text generation...")
    print(f"Generating {num_tokens} tokens...")
    print("=" * 55)

    prefill_end_time = None

    def set_prefill_time():
        nonlocal prefill_end_time
        prefill_end_time = time.time()

    # Start total wall clock timing
    start = time.time()
    token_ids = generate(
        model=model,
        idx=token_ids.to(device),
        max_new_tokens=num_tokens,
        context_size=model.cfg["context_length"],
        eos_id=tokenizer.special["<|end_of_text|>"],
        hook_handles=hook_handles,
        temperature=0.7,
        top_k=50,
        tokenizer=tokenizer,
        prompt=truncated_prompt,
        prefill_done_callback=set_prefill_time,
    )
    end = time.time()
    prefill_time = prefill_end_time - start
    total_time = end - start
    post_prefill_time = end - prefill_end_time if num_tokens > 0 else 0

    tokens_per_second = (num_tokens - 1) / post_prefill_time if num_tokens > 1 else 0
    time_per_token = total_time / (num_tokens - 1) if num_tokens > 1 else prefill_time

    print("=" * 55)
    print(" TIMING RESULTS:")
    print(f"  Total time: {total_time:.4f} seconds")
    print(f"  Prefill time: {prefill_time:.4f} seconds")
    print(f"  Tokens generated: {num_tokens}")
    print(f"  Tokens per second: {tokens_per_second:.2f}")
    print(
        f"  Time per token: {time_per_token:.4f} seconds"
        if num_tokens > 0
        else "  Time per token: N/A"
    )
    print("=" * 55)

    logging.info(f"Generation time: {total_time:.4f} sec")
    logging.info(f"Total wall clock time: {total_time:.4f} sec")
    logging.info(f"Tokens per second: {tokens_per_second:.2f}")
    logging.info(
        f"Time per token: {time_per_token:.4f} sec"
        if num_tokens > 0
        else "Time per token: N/A"
    )

    output_text = token_ids_to_text(token_ids, tokenizer)
    logging.info("Output text:\n %s", clean_text(output_text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Llama3 model inference.")
    parser.add_argument(
        "weights_file_path",
        type=str,
        help="Path to the weights file: model.safetensors",
    )
    parser.add_argument(
        "tokenizer_file_path",
        type=str,
        help="Path to the tokenizer file: tokenizer.model",
    )
    parser.add_argument(
        "--num_tokens", type=int, default=1, help="Number of tokens to predict."
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="",
        help="Prompt for the model to generate text from.",
    )
    parser.add_argument(
        "--use_prompt_template",
        action="store_true",
        help="Use a prompt template for the model.",
    )
    parser.add_argument(
        "--save_outputs",
        action="store_true",
        help="Enable hooks to save outputs of the layers in the model",
    )
    parser.add_argument(
        "--chat",
        action="store_true",
        help="Enable interactive mode to enter your own prompt.",
    )
    parser.add_argument(
        "--prompt_len",
        type=int,
        default=2048,
        help="Truncate prompt to this many tokens.",
    )
    parser.add_argument(
        "--profile",
        action="store_true",
        help="Use a custom profiler for performance measurements",
    )
    parser.add_argument(
        "-v",
        action="count",
        default=0,
        help="Increase verbosity level (use -v (logs to file), -vv, -vvv, or -vvvv)",
    )
    args = parser.parse_args()

    # Set up logging
    logs_dir_name = setup_logging(args.v)

    # Enable function profiling
    if args.profile:
        enable_profiling(logs_dir_name)

    try:
        prompt = args.prompt
        if not prompt:
            # Default prompt is text from Shakespeare's King Lear: https://shakespeare.mit.edu/lear/lear.1.1.html
            prompt_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "prompt.txt"
            )
            with open(prompt_path, "r", encoding="utf-8") as file:
                prompt = file.read().strip()

        inference(
            args.weights_file_path,
            args.tokenizer_file_path,
            args.num_tokens,
            prompt,
            args.use_prompt_template,
            args.save_outputs,
            args.chat,
            args.prompt_len,
        )
    finally:
        if args.profile:
            # Disable profiling when done
            disable_profiling()
