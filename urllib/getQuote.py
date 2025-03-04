import urllib.request
import urllib.parse
path = 'https://www.google.com/search?'

data = {
  'q':'张三',
  'start':'楠'
}
url = urllib.parse.urlencode(data)

print(url)

headers = {
  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}


req = urllib.request.Request(url=url,headers=headers)

res  = urllib.request.urlopen(req)

content = res.read().decode('utf-8')