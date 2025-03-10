import requests
import re
import csv

pattern = re.compile(r"2025必看热片.*? <ul>(?P<html>.*?)</ul>", re.S)
pattern2 = re.compile(r"<a href='(?P<url>.*?)'", re.S)
pattern3 = re.compile(r'<div class="title_all"><h1>(?P<title>.*?)</h1>.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<url>.*?)"', re.S)
url = 'https://www.dytt8899.com/'
cookies = 'Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1741587400; HMACCOUNT=64BDFD8E1EFABE88; Hm_lvt_8e745928b4c636da693d2c43470f5413=1741587400; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1741587400; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1741587681; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1741587681; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1741587681'
cookie_dict = {}
for cookie in cookies.split('; '):
    key, value = cookie.split('=', 1)
    cookie_dict[key] = value
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

f = open("tiantang.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

response = requests.get(url, headers=headers, cookies=cookie_dict)
response.encoding = 'gb2312'

content = pattern.finditer(response.text)

for item in content:
    html = item.group('html')
    result = pattern2.finditer(html)
    for i in result:
        print(i.group('url'))
        son_url = url + i.group('url')
        response = requests.get(son_url, headers=headers, cookies=cookie_dict)
        response.encoding = 'gb2312'
        content = pattern3.finditer(response.text)
        for item in content:
            dic = item.groupdict()
            csvwriter.writerow(dic.values())
    break
