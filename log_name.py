###################################################################################################
#
# Copyright (C) 2020-2022 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
#
###################################################################################################
"""
Changing log names
"""
import os
from create_test_script import log_file_names

log_path = r'/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/logs'

log_list = os.listdir(log_path)

log_list = sorted(log_list)

print(log_list)
print(log_file_names)

for (log, name) in zip(log_list, log_file_names):
    path1 = log_path + '/' + log
    new_path = log_path + '/' + name
    os.rename(path1, new_path)
