import requests

url = 'https://www.openatom.cn/api/project/v1/list'

data = {
  'lc': 'zh',
  'status': 2,
}

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
  'Content-Type': 'application/json',
}

res = requests.post(url=url, json=data, headers=headers,verify=False)

info = res.json()['data']

for i in info:
    print('title:',i['title'])
    print('--------------------------')

res.close()