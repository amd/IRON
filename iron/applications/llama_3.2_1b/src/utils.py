# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import torch
import numpy as np
from ml_dtypes import bfloat16


def model_memory_size(model, input_dtype=torch.float32):
    """
    Calculate the estimated memory size of a PyTorch model in gigabytes.

    This function computes the total memory required for the model's parameters,
    gradients, and buffers based on the input data type.

    Args:
        model (torch.nn.Module): The PyTorch model for which to calculate memory size.
        input_dtype (torch.dtype, optional): The data type of the model's input.
                                              Defaults to torch.float32.

    Returns:
        float: The estimated memory size of the model in gigabytes.
    """

    total_params = 0
    total_grads = 0
    for param in model.parameters():
        # Calculate total number of elements per parameter
        param_size = param.numel()
        total_params += param_size
        # Check if gradients are stored for this parameter
        if param.requires_grad:
            total_grads += param_size

    # Calculate buffer size (non-parameters that require memory)
    total_buffers = sum(buf.numel() for buf in model.buffers())

    # Size in bytes = (Number of elements) * (Size of each element in bytes)
    # We assume parameters and gradients are stored in the same type as input dtype
    element_size = torch.tensor(0, dtype=input_dtype).element_size()
    total_memory_bytes = (total_params + total_grads + total_buffers) * element_size

    # Convert bytes to gigabytes
    total_memory_gb = total_memory_bytes / (1024**3)

    return total_memory_gb


def assign(left, right, tensor_name="unknown"):
    """
    Assigns the value of the right tensor to a new torch.nn.Parameter after validating shape compatibility.

    Parameters:
    left (torch.Tensor or any): The tensor to compare shape with.
    right (torch.Tensor or any): The tensor or value to be assigned.
    tensor_name (str): The name of the tensor for error reporting (default is "unknown").

    Returns:
    torch.nn.Parameter: A new parameter containing the value of right.

    Raises:
    ValueError: If the shapes of left and right do not match.
    """

    if left.shape != right.shape:
        raise ValueError(
            f"Shape mismatch in tensor '{tensor_name}'. Left: {left.shape}, Right: {right.shape}"
        )

    if isinstance(right, torch.Tensor):
        return torch.nn.Parameter(right.clone().detach())
    else:
        return torch.nn.Parameter(torch.tensor(right))


def load_weights_into_llama(model, param_config, params):
    """
    Load weights into the LLaMA model from the provided parameters.

    This function assigns weights from the given parameters to the corresponding
    layers of the LLaMA model. It handles the embedding layer, attention layers,
    feedforward layers, and the output layer. The function also checks for weight
    tying between the output head and the embedding layer.

    Args:
        model: The LLaMA model instance into which weights will be loaded.
        param_config (dict): A configuration dictionary containing model parameters,
                             including the number of layers (`n_layers`).
        params (dict): A dictionary containing the weights to be loaded, with keys
                       corresponding to the model's architecture.
    """
    model.tok_emb.weight = assign(
        model.tok_emb.weight,
        params["model.embed_tokens.weight"],
        "model.embed_tokens.weight",
    )

    for l in range(param_config["n_layers"]):

        # Load attention weights
        model.trf_blocks[l].att.assign_weights(
            l,
            params[f"model.layers.{l}.self_attn.q_proj.weight"],
            params[f"model.layers.{l}.self_attn.k_proj.weight"],
            params[f"model.layers.{l}.self_attn.v_proj.weight"],
            params[f"model.layers.{l}.self_attn.o_proj.weight"],
        )
        # Load FeedForward weights
        model.trf_blocks[l].ff.assign_weights(
            l,
            fc1=params[f"model.layers.{l}.mlp.gate_proj.weight"],
            fc2=params[f"model.layers.{l}.mlp.up_proj.weight"],
            fc3=params[f"model.layers.{l}.mlp.down_proj.weight"],
        )
        # Load RMS norm weights
        model.trf_blocks[l].assign_weights(
            l,
            params[f"model.layers.{l}.input_layernorm.weight"],
            params[f"model.layers.{l}.post_attention_layernorm.weight"],
        )

    # Load output layer weights
    if "lm_head.weight" in params.keys():
        model.assign_weights(
            params["model.norm.weight"], params["lm_head.weight"], "lm_head.weight"
        )
    else:
        model.assign_weights(
            params["model.norm.weight"],
            params["model.embed_tokens.weight"],
            "model.embed_tokens.weight",
        )


def text_to_token_ids(text, tokenizer):
    """
    Convert a given text into token IDs using the specified tokenizer.

    Args:
        text (str): The input text to be tokenized.
        tokenizer: An instance of a tokenizer that has an `encode` method.

    Returns:
        torch.Tensor: A tensor containing the token IDs of the input text,
                      with an added batch dimension.
    """
    encoded = tokenizer.encode(text)
    encoded_tensor = torch.tensor(encoded).unsqueeze(0)  # add batch dimension
    return encoded_tensor


def token_ids_to_text(token_ids, tokenizer):
    """
    Convert a tensor of token IDs to a human-readable text string.

    Args:
        token_ids (torch.Tensor): A tensor containing token IDs,
                                   typically with a batch dimension.
        tokenizer (Tokenizer): An instance of a tokenizer that has a
                               decode method to convert token IDs to text.

    Returns:
        str: The decoded text string corresponding to the input token IDs.
    """
    flat = token_ids.squeeze(0)  # remove batch dimension
    return tokenizer.decode(flat.tolist())


def generate(
    model,
    idx,
    max_new_tokens,
    context_size,
    eos_id,
    hook_handles,
    temperature=0.0,
    top_k=None,
    tokenizer=None,
    prompt=None,
    do_print=True,
    prefill_done_callback=None,
):
    """
    Generate new tokens using the provided model based on the input sequence.

    Args:
        model: The model used for generating tokens. It should accept input sequences and return logits.
        idx (torch.Tensor): The input sequence of token indices (shape: (batch_size, sequence_length)).
        max_new_tokens (int): The maximum number of new tokens to generate.
        context_size (int): The number of tokens from the input sequence to consider for generation.
        temperature (float, optional): The temperature for scaling logits. Higher values result in more random outputs. Default is 0.0 (no scaling).
        top_k (int, optional): The number of top logits to consider for sampling. If None, all logits are used. Default is None.
        eos_id (int, optional): The end-of-sequence token ID. If specified, generation will stop when this token is produced. Default is None.

    Returns:
        torch.Tensor: The updated sequence of token indices after generation (shape: (batch_size, new_sequence_length)).
    """
    # For-loop is the same as before: Get logits, and only focus on last time step
    finished_prefill = False

    print(f"Starting prefill inference...")

    for i in range(max_new_tokens):
        use_kv_cache = model.cfg["use_kv_cache"]

        if use_kv_cache:
            if i == 0:
                # Prefill phase - process entire sequence
                idx_cond = idx[:, -context_size:]
                input_pos = None
            else:
                # Generation phase with KV cache - single token, need to track position
                # Extract only the last token
                idx_cond = idx[:, -1:]
                input_pos = torch.tensor([idx.shape[1] - 1], device=idx.device)
        else:
            # No KV cache - always process entire sequence (GEMM every time)
            idx_cond = idx[:, -context_size:]
            input_pos = None
        with torch.no_grad():
            logits = model(idx_cond, input_pos=input_pos, use_kv_cache=use_kv_cache)
        logits = logits[:, -1, :]

        # New: Filter logits with top_k sampling
        if top_k is not None:
            # Keep only top_k values
            top_logits, _ = torch.topk(logits, top_k)
            min_val = top_logits[:, -1]
            logits = torch.where(
                logits < min_val, torch.tensor(float("-inf")).to(logits.device), logits
            )

        # New: Apply temperature scaling
        if temperature > 0.0:
            logits = logits / temperature

            # Apply softmax to get probabilities
            probs = torch.softmax(logits, dim=-1)  # (batch_size, context_len)

            # Sample from the distribution
            idx_next = torch.multinomial(probs, num_samples=1)  # (batch_size, 1)

        # Otherwise same as before: get idx of the vocab entry with the highest logits value
        else:
            idx_next = torch.argmax(logits, dim=-1, keepdim=True)  # (batch_size, 1)

        # Only run the forward hook for the prefill stage, remove it afterwards to speed up inference
        if not finished_prefill:
            if hook_handles:
                for handle in hook_handles:
                    handle.remove()
            finished_prefill = True

        if (
            idx_next == eos_id
        ):  # Stop generating early if end-of-sequence token is encountered and eos_id is specified
            break

        # Same as before: append sampled index to the running sequence
        idx = torch.cat((idx, idx_next), dim=1)  # (batch_size, num_tokens+1)

        # End timing the first iteration
        if i == 0:
            if prefill_done_callback is not None:
                prefill_done_callback()
            if do_print:
                print(prompt)

        # print(f"\rGenerating token {i + 1}/{max_new_tokens}...", end="")
        generated_text = token_ids_to_text(idx_next, tokenizer)
        if do_print:
            print(f"{generated_text}", end="", flush=True)

    print("\n\n")
    return idx


def clean_text(text, header_end="assistant<|end_header_id|>\n\n"):
    """
    Cleans the input text by removing the header portion defined by the header_end token.

    Parameters:
    text (str): The input text to be cleaned.
    header_end (str): The token that marks the end of the header. Defaults to "assistant<|end_header_id|>\n\n".

    Returns:
    str: The cleaned text, which is the substring after the header_end token.
         If the token is not found, the original text is returned.
    """

    # Find the index of the first occurrence of "<|end_header_id|>"
    index = text.find(header_end)

    if index != -1:
        # Return the substring starting after "<|end_header_id|>"
        return text[
            index + len(header_end) :
        ].strip()  # Strip removes leading/trailing whitespace
    else:
        # If the token is not found, return the original text
        return text
