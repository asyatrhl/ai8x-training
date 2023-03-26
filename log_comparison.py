from tabulate import tabulate
import os
#from termcolor import colored
import datetime

def compare_logs(old_log, new_log, output_name, output_path ) :

    header = ["Epoch number", "Top1 Diff", "Top5 Diff"]

    with open(old_log, 'r') as f1, open(new_log, 'r') as f2 :
        file1_content = f1.readlines()
        file2_content = f2.readlines()

        log1_list = []
        log2_list = []
        word = 'Best'

        for line in file1_content:
            if word in line :
                list = line.split()
                log1_list.append(list[5:])

        for line in file2_content:
            if word in line :
                list = line.split()
                log2_list.append(list[5:])

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

    output_path_2 = output_path + '/' + output_name + '.txt'
    print(output_path_2)
    with open(output_path_2, "w") as output_file:
        output_file.write(tabulate(top1, headers=header))

log_asya = r'/home/asyaturhal/desktop/ai/test_logs/'

time = str(datetime.datetime.now())

time = time.replace(' ', '.')
time = time.replace(':', '.')
print(time)
output_path = r"/home/asyaturhal/desktop/ai/log_diff/" + '/' + str(time)
os.mkdir(output_path)

loglist = sorted(os.listdir(log_asya))
old_logs_path = log_asya + '/' + loglist[-2]
new_logs_path = log_asya + '/' + loglist[-1]

print(old_logs_path)
print(new_logs_path)

i=0
for files_new in sorted(os.listdir(new_logs_path)) :
    if files_new not in sorted(os.listdir(old_logs_path)):
        print('.. not found')
    for files_old in os.listdir(old_logs_path):
        if (files_old == files_new):
            print(files_new)
            print('We can break the loop')

            old_path = log_asya + '/' + loglist[-2] + '/' + files_old
            new_path = log_asya + '/' + loglist[-1] + '/' + files_new

            old_files = sorted(os.listdir(old_path))
            new_files = sorted(os.listdir(new_path))

            old_log_file = [file for file in old_files if file.endswith(".log")][0]
            new_log_file = [file for file in new_files if file.endswith(".log")][0]

            old_path_log = log_asya + '/' + loglist[-2] + '/' + files_old + '/' + old_log_file
            new_path_log = log_asya + '/' + loglist[-1] + '/' + files_new + '/' + new_log_file

            #print(old_log_file)
            #print(old_path_log)
            #print(new_path_log)
        
            compare_logs(old_path_log, new_path_log, files_new, output_path)
            break
