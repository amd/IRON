# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import argparse
import numpy as np
import os
import shutil


def torch_to_npy(inp_file_path, outp_file_path):
    # Load the torch file
    data = torch.load(inp_file_path)
    # Convert the tensor to a numpy array of floats
    data_np = data.to(torch.float32).numpy()
    # Compare the values between data and data_np
    if not torch.equal(data, torch.from_numpy(data_np)):
        raise ValueError("Mismatch between original data and converted numpy array.")

    # Save the array to a npy file
    np.save(outp_file_path, data_np)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert torch files to npy files.")
    parser.add_argument(
        "file_path",
        type=str,
        help="Path to the torch file or directory containing torch files",
    )
    args = parser.parse_args()
    file_path = args.file_path

    output_dir = os.path.join("results", f"{os.path.basename(file_path)}_npy")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Check if the file path is a directory
    if os.path.isdir(file_path):
        for file_name in os.listdir(file_path):
            if file_name.endswith(".pt") or file_name.endswith(".pth"):
                full_path = os.path.join(file_path, file_name)
                output_file_path = os.path.join(
                    output_dir, file_name.replace(".pt", ".npy").replace(".pth", ".npy")
                )
                torch_to_npy(full_path, output_file_path)
    else:
        torch_to_npy(file_path)
