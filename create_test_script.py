import os

def joining(list):
    # Join based on the ' ' delimiter
    str = ' '.join(list)
    return str

# Folder containing the files to be concatenated
folder_path = r"/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/scripts"

# Output file name and path
output_file_path = r"/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/scripts/output_file.sh"

# Regular expression pattern to match the "asya" script with any number

# Loop through all files in the folder
with open(output_file_path, "w") as output_file:
    for filename in os.listdir(folder_path):
        # Check if the file is a text file
        if filename.startswith("train"):
            # Open the file and read its contents
            with open(os.path.join(folder_path, filename)) as input_file:
                contents = input_file.read()

            temp = contents.split()
            temp.insert(1, "\n")
            i = temp.index('--epochs')
            
            #temp[i+1] = str(int(temp[i+1])*10/100) 
            temp[i+1] = str(5)
            temp.append("\n")
            contents = joining(temp)
            # Replace the number in the "--epochs" script

            # Write the contents to the output file
            output_file.write(contents)
