import requests

headers = {
  'Authorization': 'Bearer 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'
}
org = input("Enter the organization path: ")

url = f"https://api.atomgit.com/orgs/{org}/repos"

print(url)
response = requests.get(url, headers=headers)

print(response.text)