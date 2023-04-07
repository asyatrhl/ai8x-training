import os
import numpy as np
import subprocess

def joining(list):
    # Join based on the ' ' delimiter
    str = ' '.join(list)
    return str

folder_path= r"/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/logs"
output_file_path = r"/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/scripts/onnx_scripts.sh"
train_path = r"/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/scripts/output_file.sh"

logs_list = sorted(os.listdir(folder_path))

models = []
datasets = []
model_path = []
bias = []

with open(output_file_path, "w") as onnx_scripts:
    with open(train_path) as input_file:
        contents = input_file.read()
    lines = contents.split("#!/bin/sh ")
    lines = lines[1:]
    contents = contents.split()
    contents = np.array(contents)

    j = [i+1 for i in range(len(contents)) if contents[i]=='--model']
    for index in j:
        models.append(contents[index])

    j = [i+1 for i in range(len(contents)) if contents[i]=='--dataset']
    for index in j:
        datasets.append(contents[index])

    for i in range(len(lines)):
        if "--use-bias" in lines[i]:
            bias.append("--use-bias")
        else:
            bias.append("")

    for file in logs_list:
        temp = './logs/{}/checkpoint.pth.tar'.format(file)
        model_path.append(temp)

    for i in range(len(models)):
        temp = "python train.py --model --dataset --evaluate --exp-load-weights-from --device MAX78000 --summary onnx "

        temp = temp.split()
        temp.insert(3, models[i] )
        temp.insert(5, datasets[i])
        temp.insert(8, model_path[i])
        temp.append("--summary-filename {}{}onnx".format(models[i],datasets[i]))
        temp.append(bias[i])
        process = joining(temp)
        temp.append("\n")

        onnx_scripts.write(temp)
        subprocess.run(process)
