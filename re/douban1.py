import re
import requests
import csv

url = 'https://movie.douban.com/top250'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
pattern = re.compile(r'<li>.*?<a href="(?P<url>.*?)">.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p>(?P<editor>.*?)<br>(?P<year>.*?)&nbsp'
                     r'.*?<span class="rating_num" property="v:average">(?P<rate>.*?)</span>'
                     r'.*?<p class="quote">.*?<span>(?P<slogan>.*?)</span>', re.S)

response = requests.get(url, headers=headers,verify=True)

result = pattern.finditer(response.text)
f = open("douban.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)
for i in result:
  # print(i.group("name"))
  # print(i.group("url"))
  # print(i.group("editor").strip())
  # print(i.group("year").strip())
  # print(i.group("rate"))
  # print(i.group("slogan"))
  dic = i.groupdict()
  dic["year"] = dic["year"].strip()
  dic["editor"] = dic["editor"].strip()
  csvwriter.writerow(dic.values())
print('运行完成')
