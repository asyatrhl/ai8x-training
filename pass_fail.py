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

# config_path = r'C:\Users\aturhal\Desktop\ai\source\test_config.conf'
config_path = r'/home/asyaturhal/desktop/ai/test_config.conf'
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

        model_name = file.split('/')[-1].split('.')[0]
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
    print(f"\033[31m\u2718\033[0m Test failed for {model_name} since in"
          f" Top1 value changed {top1_diff} at {epoch_num}th epoch.")
    return True


for logs in sorted(os.listdir(log_path)):
    if logs in config:
        threshold_temp = float(list(config['{logs}']["threshold"])[0])
    else:
        threshold_temp = 0
    logs = log_path + '/' + str(logs)
    check_top_value(logs, threshold_temp)
