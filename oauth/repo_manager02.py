import json
import requests
import getpass

def create_repo(repo_name: str, username: str, token: str) -> str:
    """
    This will create a repo for your GitHub account.
    """
    repo_data = {"name": repo_name}
    json_data = json.dumps(repo_data)
    headers = {"Authorization": f"token {token}"}
    r = requests.post(f"https://api.github.com/user/repos", data=json_data, headers=headers)
    response_code = r.status_code
    response = r.text
    print(response_code, response)
    return response

def show_repos(username: str, token: str) -> list:
    """
    This will list out all of the repos associated with your GitHub account.
    """
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    resp_headers = r.headers
    print(f"""Rate - \n            Limit: {resp_headers['X-RateLimit-Limit']}
            Used: {resp_headers['X-RateLimit-Used']}
            Remaining: {resp_headers['X-RateLimit-Remaining']}""")
    repos = list(r.json())
    for repo in repos:
        print(repo['name'])
    return repos

def get_credentials() -> tuple:
    # Prompt user for username and API key without displaying them
    username = input("Enter your GitHub username: ")
    token = getpass.getpass("Enter your GitHub API key: ")
    return username, token

if __name__ == "__main__":
    MY_USERNAME, tkn = get_credentials()
    show_repos(MY_USERNAME, tkn)
    create_repo("learning_oauth", MY_USERNAME, tkn)
