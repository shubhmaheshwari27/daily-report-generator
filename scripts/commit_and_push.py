import subprocess

def commit_and_push():
    # Add changes to git
    subprocess.run(["git", "add", "."])  # Stages all files

    # Commit the changes with a message
    subprocess.run(["git", "commit", "-m", "Updated report"])

    # Push changes to the main branch of GitHub
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == '__main__':
    commit_and_push()
