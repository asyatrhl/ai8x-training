###################################################################################################
#
# Copyright (C) 2020-2022 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
#
###################################################################################################
"""
Create training bash scripts for test
"""
import configparser
import os


def joining(lst):
    """
    Join list based on the ' ' delimiter
    """
    join_str = ' '.join(lst)
    return join_str


config_path = r'/home/asyaturhal/desktop/ai/test_config.conf'
config = configparser.ConfigParser()
config.read(config_path)

# Folder containing the files to be concatenated
folder_path = (
    r"/home/asyaturhal/actions-runner/_work/"
    r"ai8x-training/ai8x-training/scripts_test"
)


# Output file name and path
output_file_path = (
    r"/home/asyaturhal/actions-runner/_work/"
    r"ai8x-training/ai8x-training/scripts/output_file.sh"
)


# global log_file_names
log_file_names = []

# Loop through all files in the folder
with open(output_file_path, "w") as output_file:
    for filename in os.listdir(script_path):
        # Check if the file is a text file
        if filename.startswith("train"):
            # Open the file and read its contents
            with open(os.path.join(script_path, filename)) as input_file:
                contents = input_file.read()

                temp = contents.split()
                temp.insert(1, "\n")
                i = temp.index('--epochs')
                j = temp.index('--model')
                k = temp.index('--dataset')

                log_name = temp[j+1] + '-' + temp[k+1]
                log_file_names.append(filename[:-3])

                # temp[i+1] = str(int(temp[i+1])*10/100) 
                temp[i+1] = config[f'{log_name}']["epoch"]

                if '--deterministic' not in temp:
                    temp.insert(-2, '--deterministic')

                temp.insert(-1, '--name ' + log_name)
                
                data_name = temp[k+1]
                if data_name in config:
                    path_data = config[f'{data_name}']["data_path"]
                    temp.insert(-1, '--data ' + path_data)

                temp.append("\n")
                contents = joining(temp)
                # Replace the number in the "--epochs" script

                # Write the contents to the output file
                output_file.write(contents)

if "train_test" in log_file_names:
    log_file_names.remove("train_test")
