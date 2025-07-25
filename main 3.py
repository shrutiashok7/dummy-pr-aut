# main.py

"""
LLM PR Automation Tool using Groq
-----------------------
This script automatically:
- Accepts git diff input directly from user
- Creates a Git branch (UT-gen-<timestamp>)
- Commits changes in `tests/`
- Generates a PR title and description using Groq API
- Pushes the branch
- Raises a Pull Request using GitHub API
"""

import os
import sys
import subprocess
import requests
import datetime
import argparse
import httpx

# ----------- ARGUMENT PARSING -----------
def parse_args():
    parser = argparse.ArgumentParser(description="Automate PR creation for LLM-generated tests.")
    parser.add_argument("--repo", required=True, help="GitHub repository URL (e.g., https://github.com/user/repo)")
    parser.add_argument("--token", required=True, help="GitHub personal access token")
    parser.add_argument("--base-branch", default="main", help="Base branch for the pull request")
    parser.add_argument("--author", required=True, help="Author name")
    parser.add_argument("--groq-api-key", required=True, help="Groq API key")
    parser.add_argument("--groq-model", default="mixtral-8x7b-32768", help="Groq model to use")
    parser.add_argument("--diff", required=True, help="Git diff text to send to the LLM")
    return parser.parse_args()

# ----------- UTILITIES -----------
def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {cmd}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def run_command_safe(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def create_branch(branch_name):
    run_command(f"git checkout -b {branch_name}")

def commit_tests():
    # pass the filename
    run_command("git add tests/ || true")

    # Check if there's anything to commit
    status_output = run_command("git status --porcelain tests/")
    if status_output.strip() == "":
        print("No changes in 'tests/' to commit. Skipping commit step.")
        return False
    
    # Commit Message should be generated by LLM
    run_command("git commit -m 'Add LLM-generated unit tests'")
    diff = run_command("git diff")
    return diff

def push_branch(branch_name):
    run_command(f"git push origin {branch_name}")   

# ----------- GROQ LLM CALL FOR PR TITLE + DESC -----------
def generate_pr_title_desc(author_name, groq_api_key, model, diff_text):
    prompt = (
        f"Given the following git diff, generate a professional GitHub Pull Request title and description.\n\n"
        f"Git diff:\n{diff_text}\n\n"
        f"The title should summarize the change in under 50 characters.\n"
        f"The description should briefly explain:\n"
        f"- What was changed\n"
        f"- What files were added or modified\n"
        f"- Mention if any tests were added or skipped\n"
        f"- Include a placeholder line for test coverage as: Coverage: {{COVERAGE_PLACEHOLDER}}\n\n"
        f"Format your response as:\n"
        f"Title: <title>\n"
        f"Description:\n"
        f"- <points>"
    )

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    body = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    try:
        response = httpx.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
        response.raise_for_status()
        content = response.json()['choices'][0]['message']['content']
        lines = content.strip().split("\n", 1)
        title = lines[0].replace("Title:", "").strip()
        description = lines[1].replace("Description:", "").strip() if len(lines) > 1 else ""
        return title, description
    except Exception as e:
        print(f"Failed to call Groq API: {e}")
        sys.exit(1)

# ----------- GITHUB API TO CREATE PR -----------
def create_pull_request(owner, repo_name, token, base_branch, head_branch, title, body):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "head": head_branch,
        "base": base_branch,
        "body": body
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"Pull request created: {response.json()['html_url']}")
    else:
        print(f"Failed to create PR: {response.status_code} {response.text}")
        sys.exit(1)

# ----------- MAIN FLOW -----------
if __name__ == "__main__":
    args = parse_args()

    # Hardcode the values
    github_repo_url = args.repo
    github_token = args.token
    base_branch = args.base_branch
    author_name = args.author
    groq_api_key = args.groq_api_key
    groq_model = args.groq_model
    diff_text = args.diff

    repo_name = github_repo_url.rstrip("/").split("/")[-1]
    owner = github_repo_url.rstrip("/").split("/")[-2]
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    branch_name = f"UT-gen-{timestamp}"

    print("Starting PR creation for LLM-generated unit tests...")
    create_branch(branch_name)
    changes_committed = commit_tests()
    diff = commit_tests()
    # if not changes_committed:
    #    sys.exit(0)
    push_branch(branch_name)
    pr_title, pr_desc = generate_pr_title_desc(author_name, groq_api_key, groq_model, diff)
    create_pull_request(owner, repo_name, github_token, base_branch, branch_name, pr_title, pr_desc)
