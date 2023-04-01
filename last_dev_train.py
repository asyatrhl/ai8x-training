import os

def joining(list):
    # Join based on the ' ' delimiter
    str = ' '.join(list)
    return str

# Folder containing the files to be concatenated
script_path = r"/home/asyaturhal/desktop/ai/last_developed/ai8x-training/scripts_test"

# Output file name and path
output_file_path = r"/home/asyaturhal/desktop/ai/last_developed/dev_scripts/last_dev_train.sh"

global log_file_names 
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

                log_file_names.append(filename[:-3])
            
           
                #temp[i+1] = str(int(temp[i+1])*10/100) 
                temp[i+1] = str(5)
                temp.append("\n")
                contents = joining(temp)
                # Replace the number in the "--epochs" script

                # Write the contents to the output file
                output_file.write(contents)
        #log_file_names.remove("train_svhn_tinierssd")