import git
import os

def dev_checkout():
    # Define the URL of the repository and the local path to clone it to
    # repo_url = "https://github.com/MaximIntegratedAI/ai8x-training.git"
    # local_path = r"C:\Users\aturhal\Desktop\new-ai\source"

    repo_url = "https://github.com/MaximIntegratedAI/ai8x-training.git"
    local_path = r'/home/asyaturhal/desktop/ai/last_developed/last_dev_logs/'

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

dev_checkout()
dev_scripts(script_path, output_file_path)
