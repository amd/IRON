# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tokenizer utilities for IRON API

Provides tokenizer loading and text processing for various model architectures.
"""

from typing import List, Optional, Tuple
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class TokenizerWrapper:
    """
    Wrapper around HuggingFace tokenizers with caching.

    Supports:
    - Auto-download from HuggingFace Hub
    - Local cache for fast loading
    - Model-specific tokenization settings
    """

    def __init__(self, model_id: Optional[str] = None):
        """
        Initialize tokenizer wrapper.

        Args:
            model_id: Optional HuggingFace model ID for tokenizer
        """
        self.model_id = model_id
        self._tokenizer = None

    def load(self, model_id: Optional[str] = None) -> "TokenizerWrapper":
        """
        Load tokenizer from HF Hub or local path.

        Args:
            model_id: Optional model ID (uses init value if None)

        Returns:
            self for chaining
        """
        try:
            from transformers import AutoTokenizer

            model_id = model_id or self.model_id
            if not model_id:
                raise ValueError("model_id required for tokenizer loading")

            self._tokenizer = AutoTokenizer.from_pretrained(model_id)
            logger.info(f"Loaded tokenizer for {model_id}")
        except ImportError:
            logger.warning("transformers not available, using fallback tokenizer")
            self._tokenizer = None
        except Exception as e:
            logger.warning(f"Could not load tokenizer: {e}")
            self._tokenizer = None

        return self

    @property
    def tokenizer(self):
        """Get underlying tokenizer"""
        return self._tokenizer

    def encode(
        self,
        text: str,
        add_special_tokens: bool = True,
        return_tensors: str = "pt",
    ):
        """
        Encode text to token IDs.

        Args:
            text: Input text
            add_special_tokens: Whether to add special tokens
            return_tensors: Output tensor type ("pt", "np", "list")

        Returns:
            Encoded token IDs
        """
        if self._tokenizer is None:
            return self._fallback_encode(text)

        return self._tokenizer.encode(
            text,
            add_special_tokens=add_special_tokens,
            return_tensors=return_tensors,
        )

    def decode(
        self,
        token_ids: List[int],
        skip_special_tokens: bool = True,
    ) -> str:
        """
        Decode token IDs to text.

        Args:
            token_ids: Token IDs to decode
            skip_special_tokens: Whether to skip special tokens

        Returns:
            Decoded text
        """
        if self._tokenizer is None:
            return self._fallback_decode(token_ids)

        return self._tokenizer.decode(
            token_ids,
            skip_special_tokens=skip_special_tokens,
        )

    def _fallback_encode(self, text: str) -> List[int]:
        """Fallback encoding using simple whitespace tokenization"""
        # Simple whitespace-based tokenization as fallback
        tokens = text.split()
        return [hash(t) % 32000 for t in tokens]  # Dummy token IDs

    def _fallback_decode(self, token_ids: List[int]) -> str:
        """Fallback decoding"""
        return f"[{len(token_ids)} tokens]"


def get_tokenizer(model_id: str) -> TokenizerWrapper:
    """
    Get tokenizer for a model.

    Args:
        model_id: HuggingFace model ID

    Returns:
        TokenizerWrapper instance
    """
    wrapper = TokenizerWrapper(model_id)
    return wrapper.load()


def messages_to_prompt_llama3(messages: List[dict]) -> str:
    """
    Convert chat messages to Llama-3 format.

    Args:
        messages: List of {role, content} dicts

    Returns:
        Formatted prompt string
    """
    prompt = "<|begin_of_text|>"
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        prompt += f"<|start_header_id|>{role}<|end_header_id|>\n\n"
        prompt += f"{content}<|eot_id|>"
    prompt += "<|start_header_id|>assistant<|end_header_id|>\n\n"
    return prompt


def messages_to_prompt_mistral(messages: List[dict]) -> str:
    """
    Convert chat messages to Mistral format.

    Args:
        messages: List of {role, content} dicts

    Returns:
        Formatted prompt string
    """
    prompt = ""
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if role == "user":
            prompt += f"[INST] {content} [/INST]"
        else:
            prompt += f" {content}"
    return prompt


def messages_to_prompt(messages: List[dict], architecture: str = "llama") -> str:
    """
    Convert chat messages to model-specific prompt format.

    Args:
        messages: List of {role, content} dicts
        architecture: Model architecture ("llama", "mistral", "phi", "gemma")

    Returns:
        Formatted prompt string
    """
    architecture = architecture.lower()

    if "llama" in architecture or "llama-3" in architecture.lower():
        return messages_to_prompt_llama3(messages)
    elif "mistral" in architecture:
        return messages_to_prompt_mistral(messages)
    elif "phi" in architecture:
        # Phi uses a simple format
        prompt = ""
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "user":
                prompt += f"User: {content}\n\nAssistant:"
            else:
                prompt += f" {content}\n\n"
        return prompt
    elif "gemma" in architecture:
        # Gemma uses chat template
        prompt = ""
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "user":
                prompt += f"<start_of_turn>user\n{content}<end_of_turn>\n"
                prompt += f"<start_of_turn>model\n"
            else:
                prompt += f"{content}<end_of_turn>\n"
        return prompt
    else:
        # Default to Llama-3 format
        return messages_to_prompt_llama3(messages)


def tokenize(
    text: str,
    tokenizer: Optional[TokenizerWrapper] = None,
    model_id: Optional[str] = None,
) -> Tuple[List[int], int]:
    """
    Tokenize text and return token IDs and count.

    Args:
        text: Input text
        tokenizer: Optional tokenizer wrapper
        model_id: Optional model ID for tokenizer loading

    Returns:
        Tuple of (token_ids, num_tokens)
    """
    if tokenizer is None:
        tokenizer = get_tokenizer(model_id or "meta-llama/Llama-3.2-1B")

    tokens = tokenizer.encode(text, return_tensors="list")
    return tokens, len(tokens)


def detokenize(
    token_ids: List[int],
    tokenizer: Optional[TokenizerWrapper] = None,
) -> str:
    """
    Convert token IDs back to text.

    Args:
        token_ids: Token IDs
        tokenizer: Optional tokenizer wrapper

    Returns:
        Decoded text
    """
    if tokenizer is None:
        tokenizer = TokenizerWrapper()

    return tokenizer.decode(token_ids)
