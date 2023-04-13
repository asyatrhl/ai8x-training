###################################################################################################
#
# Copyright (C) 2020-2022 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
#
###################################################################################################
"""
Compare log files of the pulled code and the last developed
"""
import datetime
import os

from tabulate import tabulate


def compare_logs(old_log, new_log, output_name, output_pth):
    """
    Take diff top1 of log files of the pulled code and the last developed
    """
    header = ["Epoch number", "Top1 Diff", "Top5 Diff"]

    with open(old_log, 'r', encoding='utf-8') as f1, open(new_log, 'r', encoding='utf-8') as f2:
        file1_content = f1.readlines()
        file2_content = f2.readlines()

        log1_list = []
        log2_list = []
        word = 'Best'

        for line in file1_content:
            if word in line:
                lst = line.split()
                log1_list.append(lst[5:])

        for line in file2_content:
            if word in line:
                lst = line.split()
                log2_list.append(lst[5:])

        epoch_num = min(len(log1_list), len(log2_list))

        log1_list = log1_list[:epoch_num]
        log2_list = log2_list[:epoch_num]

        top1 = []

    i = 0
    for (list1, list2) in zip(log1_list, log2_list):
        i = i+1

        top1_diff = ((float(list2[1])-float(list1[1]))/float(list1[1]))*100
        top5_diff = ((float(list2[3])-float(list1[3]))/float(list1[1]))*100

        top1.append([i, top1_diff, top5_diff])

    output_path_2 = output_pth + '/' + output_name + '.txt'
    print(output_path_2)
    with open(output_path_2, "w", encoding='utf-8') as output_file:
        output_file.write(tabulate(top1, headers=header))


def log_path_list(path):
    """
    Create log names
    """
    lst = []
    for file in sorted(os.listdir(path)):
        lst.append(file.split("___")[0])
    return lst


log_new = r'/home/asyaturhal/desktop/ai/test_logs/'
log_old = r'/home/asyaturhal/desktop/ai/last_developed/dev_logs/'

time = str(datetime.datetime.now())
time = time.replace(' ', '.')
time = time.replace(':', '.')
output_path = r"/home/asyaturhal/desktop/ai/log_diff/" + '/' + str(time)
os.mkdir(output_path)

loglist = sorted(os.listdir(log_new))
loglist_old = sorted(os.listdir(log_old))
print(loglist)
old_logs_path = log_old + loglist_old[-1]
new_logs_path = log_new + loglist[-1]

print(old_logs_path)
print(new_logs_path)

new_log_list = log_path_list(new_logs_path)
old_log_list = log_path_list(old_logs_path)

for files_new in sorted(os.listdir(new_logs_path)):
    files_new_temp = files_new.split("___")[0]
    if files_new_temp not in old_log_list:
        print(files_new_temp + " not found in last developed log files.")
    for files_old in sorted(os.listdir(old_logs_path)):
        files_old_temp = files_old.split("___")[0]
        if files_old_temp == files_new_temp:
            print(files_new)
            print('We can break the loop')

            old_path = old_logs_path + '/' + files_old
            new_path = new_logs_path + '/' + files_new

            old_files = sorted(os.listdir(old_path))
            new_files = sorted(os.listdir(new_path))

            old_log_file = [file for file in old_files if file.endswith(".log")][0]
            new_log_file = [file for file in new_files if file.endswith(".log")][0]

            old_path_log = old_path + '/' + old_log_file
            new_path_log = new_path + '/' + new_log_file

            compare_logs(old_path_log, new_path_log, files_new, output_path)
            break
