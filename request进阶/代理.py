import requests

proxies = {
  "https":"https://86.38.234.176:6630"
}

url = 'https://www.baidu.com'

res = requests.get('https://www.baidu.com',proxies=proxies)
res.encoding = 'utf-8'
print(res.text)