import subprocess

def git_commit_with_coauthor(commit_message, co_author_name, co_author_email):
    # Construct the commit message with co-author information
    commit_message += f"\n\nCo-authored-by: {co_author_name} <{co_author_email}>"

    # Stage changes
    subprocess.run(['git', 'add', '.'])

    # Commit with the constructed message
    subprocess.run(['git', 'commit', '-m', commit_message])

# Example usage
commit_msg = "Implement feature X"
author_name = "Freaqke"
author_email = "sembuntjaka2@gmail.com"

git_commit_with_coauthor(commit_msg, author_name, author_email)
