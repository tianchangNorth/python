import urllib.request
import json
url = 'http://www.baidu.com'
res =  urllib.request.urlopen(url)

# print(res.read().decode('utf-8'))
 
# 一个类型 HTTPResponse

print(type(res))

# 一个字节流
# 返回十个字节
# content = res.read(10)

# print(content)

# content = res.readline()
# content = res.readlines()
content =  res.read().decode('utf-8')
status = res.getcode()

url_res = res.geturl()

print(status,url_res)

file = open('./baidu.html','w')

file.write(str(content))