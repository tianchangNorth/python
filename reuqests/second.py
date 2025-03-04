import requests

trans = input('Enter the text to translate: ')

url = 'https://fanyi.baidu.com/sug'

data = {
  "kw": trans
}

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

res = requests.post(url,headers=headers,data=data,verify=False)

print(res.json()['data'][0]['v'])