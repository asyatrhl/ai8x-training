import os

def joining(list):
    str = ' '.join(list)
    return str

# Folder containing the files to be concatenated
folder_path = r"/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/scripts_test"

# Output file name and path
output_file_path = r"/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/scripts/output_file.sh"

global log_file_names 
log_file_names = []

# Loop through all files in the folder
with open(output_file_path, "w") as output_file:
    for filename in os.listdir(folder_path):
        # Check if the file is a train file
        if filename.startswith("train"):
            with open(os.path.join(folder_path, filename)) as input_file:
                contents = input_file.read()

            temp = contents.split()
            temp.insert(1, "\n")
            i = temp.index('--epochs')
            j = temp.index('--model')
            k = temp.index('--dataset')

            log_name = temp[j+1] + '-' + temp[k+1]
            
            log_file_names.append(filename[:-3])
            
            if '--deterministic' not in temp:
                temp.insert(-2, '--deterministic')
            
            temp.insert(-1, '--name ' + log_name)
            
            #temp[i+1] = str(int(temp[i+1])*10/100) 
            temp[i+1] = str(5)
            temp.append("\n")
            contents = joining(temp)
   
            output_file.write(contents)
    
if "train_test" in log_file_names:
    log_file_names.remove("train_test") 
