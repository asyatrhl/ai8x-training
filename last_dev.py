import git

# Define the URL of the repository and the local path to clone it to
# repo_url = "https://github.com/MaximIntegratedAI/ai8x-training.git"
# local_path = r"C:\Users\aturhal\Desktop\new-ai\source"

repo_url = "https://github.com/MaximIntegratedAI/ai8x-training.git"
local_path = r'/home/asyaturhal/desktop/ai/last_developed/last_dev_logs/'

# Clone the repository or open it if it already exists
try:
    repo = git.Repo(local_path)
except git.exc.InvalidGitRepositoryError:
    repo = git.Repo.clone_from(repo_url, local_path, branch="develop", recursive=True)

# Get the commit hash of the latest commit on the develop branch
commit_hash = repo.heads.develop.object.hexsha

# Read the commit hash from the text file, or set it to an empty string if the file doesn't exist
try:
    with open(r"/home/asyaturhal/desktop/ai/last_developed/commit_number.txt", "r") as f:
        saved_commit_hash = f.read().strip()
except FileNotFoundError:
    saved_commit_hash = ""

# Compare the commit hashes and write the new commit hash to the text file if they don't match
if commit_hash != saved_commit_hash:
    with open(r"/home/asyaturhal/desktop/ai/last_developed/commit_number.txt", "w") as f:
        f.write(commit_hash)
        repo = git.Repo.clone_from(repo_url, local_path, branch="develop", recursive=True)