import urllib.request

url = 'https://www.google.com/'
headers = {
  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url=url,headers=headers)


res = urllib.request.urlopen(req)

content = res.read().decode('utf-8')
print(content)