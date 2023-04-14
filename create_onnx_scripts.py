###################################################################################################
#
# Copyright (C) 2020 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
#
###################################################################################################
"""
Create onnx bash scripts for test
"""
import os
import subprocess

import numpy as np


def joining(lst):
    """
    Join list based on the ' ' delimiter
    """
    joined_str = ' '.join(lst)
    return joined_str


folder_path = r"/home/asyaturhal/desktop/ai/test_logs"
output_file_path = (
    r"/home/asyaturhal/actions-runner/_work/"
    r"ai8x-training/ai8x-training/scripts/onnx_scripts.sh"
)
train_path = (
    r"/home/asyaturhal/actions-runner/_work/"
    r"ai8x-training/ai8x-training/scripts/output_file.sh"
)
logs_list = folder_path + '/' + sorted(os.listdir(folder_path))[-1]
# print(logs_list)
models = []
datasets = []
model_paths = []
bias = []

with open(output_file_path, "w", encoding='utf-8') as onnx_scripts:
    with open(train_path, "r", encoding='utf-8') as input_file:
        contents = input_file.read()
    lines = contents.split("#!/bin/sh ")
    lines = lines[1:]
    contents_t = contents.split()
    contents_temp = np.array(contents_t)

    j = [i+1 for i in range(len(contents_temp)) if contents_temp[i] == '--model']
    for index in j:
        models.append(contents_temp[index])

    j = [i+1 for i in range(len(contents_temp)) if contents_temp[i] == '--dataset']
    for index in j:
        datasets.append(contents_temp[index])

    for i, line in enumerate(lines):
        if "--use-bias" in line:
            bias.append("--use-bias")
        else:
            bias.append("")

#     for file in logs_list:
#         temp = './logs/{}/checkpoint.pth.tar'.format(file)
#         model_path.append(temp)

    for file in sorted(os.listdir(logs_list)):
        temp_path = logs_list + "/" + file
        for temp_file in sorted(os.listdir(temp_path)):
            if temp_file.endswith("_checkpoint.pth.tar"):
                temp = f"{temp_path}/{temp_file}"
                model_paths.append(temp)

    for i, (model, dataset, model_path, bias_value) in enumerate(
        zip(models, datasets, model_paths, bias)
    ):
        temp = (
            f"python train.py "
            f"--model {model} "
            f"--dataset {dataset} "
            f"--evaluate "
            f"--exp-load-weights-from {model_path} "
            f"--device MAX78000 "
            f"--summary onnx "
            f"--summary-filename {model}{dataset}onnx "
            f"{bias_value}\n"
        )
        onnx_scripts.write(temp)

cmd_command = (
    "bash /home/asyaturhal/actions-runner/_work/"
    "ai8x-training/ai8x-training/scripts/onnx_scripts.sh"
)
subprocess.run(cmd_command, shell=True, check=True)
