import requests

username = input("Enter a Github username: ")

response = requests.get(f"https://api.github.com/users/{username}/repos")

data = response.json()
print(data)

# for key in data:
#     print(data['name'])
#     print(data['description'])
#     print(data['html_url'])
