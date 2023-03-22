import os
from create_test_script import log_file_names

sh_path = r'/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/logs/'

with open(sh_path, "r") as f:
    lines = f.readlines()

log_list = os.listdir(sh_path)

for (log, name) in zip(log_list, log_file_names) :
    path1 = sh_path +  '/' + log
    new_path = sh_path +  '/' + name
    print(path1)
    print(new_path)

    os.rename(path1, new_path)

