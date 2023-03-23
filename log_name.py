import os
from create_test_script import log_file_names

log_path = r'/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/logs'

log_list = os.listdir(log_path)

for (log, name) in zip(log_list, log_file_names) :
    path1 = log_path +  '/' + log
    new_path = log_path +  '/' + name
    os.rename(path1, new_path)
