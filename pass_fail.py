###################################################################################################
#
# Copyright (C) 2020 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
#
###################################################################################################
"""
Check the test results
"""
import configparser
import os

from log_check import not_found_model

# config_path = r'C:\Users\aturhal\Desktop\ai\source\test_config.conf'
config_path = r'/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/test_config.conf'
config = configparser.ConfigParser()
config.read(config_path)
log_path = r'/home/asyaturhal/desktop/ai/log_diff'
# log_path = r'C:\Users\aturhal\Desktop\test_logs'
log_path = log_path + '/' + sorted(os.listdir(log_path))[-1]


def check_top_value(file, threshold):
    """
    Compare Top1 value with threshold
    """
    with open(file, 'r', encoding='utf-8') as f:

        model_name = file.split('/')[-1].split('___')[0]
        # Read all lines in the file
        lines = f.readlines()
        # Extract the last line and convert it to a float
        top1 = lines[-1].split()
        epoch_num = int(top1[0])
        top1_diff = float(top1[1])
        # top5_diff = float(top1[2])

    if top1_diff < threshold:
        print(f"\033[31m\u2718\033[0m Test failed for {model_name} since in"
              f" Top1 value changed {top1_diff} at {epoch_num}th epoch.")
        return False
    print(f"\033[32m\u2714\033[0m Test passed for {model_name} since in"
          f" Top1 value changed {top1_diff} at {epoch_num}th epoch.")
    return True


for item in not_found_model:
    print("\033[93m\u26A0\033[0m " + "Warning: " + item)

for logs in sorted(os.listdir(log_path)):
    log_name = (logs.split("___"))[0]
    if log_name in config:
        threshold_temp = float(config[f'{log_name}']["threshold"])
        # threshold_temp = float(list(config['{log_name}']["threshold"])[0])
    else:
        threshold_temp = 0
    logs = log_path + '/' + str(logs)
    check_top_value(logs, threshold_temp)
