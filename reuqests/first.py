import requests

search = input('Enter the search query: ')

url = f'https://www.google.com/search?q={search}'

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=headers,verify=False)

print(res.text)