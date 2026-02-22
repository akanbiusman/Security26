import requests


def get_repos():
    github_username = input("Enter a Github username: ")

    response = requests.get(
        f"https://api.github.com/users/{github_username}/repos")

    data = response.json()

    if 'message' in data and data['message'] == 'Not Found':
        print("Username not found!")

        return None

    return data


data = get_repos()

if data is None:
    exit()

for repo in data:
    print(repo['name'])
    print(repo['description'])
    print(repo['html_url'])
    print("\n")
