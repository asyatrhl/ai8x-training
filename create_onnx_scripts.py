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
import datetime
import argparse
import os
import subprocess
import yaml

import numpy as np			 


def joining(lst):
    """
    Join list based on the ' ' delimiter
    """
    joined_str = ' '.join(lst)
    return joined_str


def time_stamp():
    """
    Take time stamp as string
    """
    time = str(datetime.datetime.now())
    time = time.replace(' ', '.')
    time = time.replace(':', '.')
    return time


parser = argparse.ArgumentParser()
parser.add_argument('--testconf', help='Enter the config file for the test', required=True)
args = parser.parse_args()
yaml_path = args.testconf

# Open the YAML file
with open(yaml_path, 'r') as file:
    # Load the YAML content into a Python dictionary
    config = yaml.safe_load(file)

if not config["Onnx_Status"]:
    exit(0)

folder_path = r"./logs"
output_file_path = (
    r"./scripts/onnx_scripts.sh"
)
train_path = (
    r"./scripts/output_file.sh"
)
										
logs_list = folder_path + '/' + sorted(os.listdir(folder_path))[-1]

models = []
datasets = []
model_paths = []
bias = []
tar_names = []


with open(output_file_path, "w", encoding='utf-8') as onnx_scripts:
    with open(train_path, "r", encoding='utf-8') as input_file:
        contents = input_file.read()
    lines = contents.split("#!/bin/sh ")
    lines = lines[1:]
    contents_t = contents.split()

    j = [i+1 for i in range(len(contents_t)) if contents_t[i] == '--model']
    for index in j:
        models.append(contents_t[index])

    j = [i+1 for i in range(len(contents_t)) if contents_t[i] == '--dataset']
    for index in j:
        datasets.append(contents_t[index])

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
                tar_names.append(temp_file)

    for i, (model, dataset, bias_value) in enumerate(
        zip(models, datasets, bias)
    ):
        for tar in model_paths:
            element = tar.split('-')
            modelsearch = element[-4][3:]
            datasearch = element[-3].split('_')[0]
            if datasearch == dataset.split('_')[0] and modelsearch == model:
                model_paths.remove(tar)
                tar_path = tar
                timestamp = time_stamp()
                temp = (
                    f"python train.py "
                    f"--model {model} "
                    f"--dataset {dataset} "
                    f"--evaluate "
                    f"--exp-load-weights-from {tar_path} "
                    f"--device MAX78000 "
                    f"--summary onnx "
                    f"--summary-filename {model}_{dataset}_{timestamp}_onnx "
                    f"{bias_value}\n"
                )
                onnx_scripts.write(temp)			

cmd_command = (
												   
    "bash ./scripts/onnx_scripts.sh"
)

subprocess.run(cmd_command, shell=True, check=True)
