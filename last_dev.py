import git
import os
import subprocess
import datetime

def log_name(log_file_names):
    log_path = r'/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/logs'

    log_list = os.listdir(log_path)

    log_list = sorted(log_list)

    print(log_list)
    print(log_file_names)

    for (log, name) in zip(log_list, log_file_names) :
        path1 = log_path +  '/' + log
        new_path = log_path +  '/' + name
        os.rename(path1, new_path)

def joining(list):
    # Join based on the ' ' delimiter
    str = ' '.join(list)
    return str

# Folder containing the files to be concatenated
#script_path = r"/home/asyaturhal/desktop/ai/last_developed/ai8x-training/scripts_test"
script_path = r"/home/asyaturhal/desktop/ai/last_developed/scripts_test"

# Output file name and path
output_file_path = r"/home/asyaturhal/desktop/ai/last_developed/dev_scripts/last_dev_train.sh"

global log_file_names 
log_file_names = []

# Loop through all files in the folder
def dev_scripts (script_path, output_file_path ):
    with open(output_file_path, "w") as output_file:
        for filename in sorted(os.listdir(script_path)):
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

def dev_checkout():
    
    repo_url = "https://github.com/MaximIntegratedAI/ai8x-training.git"
    local_path = r'/home/asyaturhal/desktop/ai/last_developed/last_dev_source/'

    try:
        repo = git.Repo(local_path)
    except git.exc.InvalidGitRepositoryError:
        repo = git.Repo.clone_from(repo_url, local_path, branch="develop", recursive=True)

    commit_hash = repo.heads.develop.object.hexsha

    try:
        with open(r"/home/asyaturhal/desktop/ai/last_developed/commit_number.txt", "r") as f:
            saved_commit_hash = f.read().strip()
    except FileNotFoundError:
        saved_commit_hash = ""

    if commit_hash != saved_commit_hash:
        with open(r"/home/asyaturhal/desktop/ai/last_developed/commit_number.txt", "w") as f:
            f.write(commit_hash)
            repo.remotes.origin.pull("develop")
            
            dev_scripts(script_path, output_file_path)
            cmd_command = "bash /home/asyaturhal/desktop/ai/last_developed/dev_scripts/last_dev_train.sh"
            subprocess.run(cmd_command, shell=True, check=True)
            
            log_name(log_file_names)
            
            source_path = "/home/asyaturhal/actions-runner/_work/ai8x-training/ai8x-training/logs/"
            destination_path = "/home/asyaturhal/desktop/ai/last_developed/dev_logs/" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            subprocess.run(['mv', source_path, destination_path], check=True)

dev_checkout()
