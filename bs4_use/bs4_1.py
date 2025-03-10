from bs4 import BeautifulSoup
import requests
import csv

url = 'https://movie.douban.com/top250?start='

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

f = open("douban.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

response = requests.get(url, headers=headers,verify=True)

# 1.页面源代码交给BeautifulSoup进行处理
page = BeautifulSoup(response.text, 'html.parser')
# 2.查找所有的数据 class是python关键字，所以用class_ id也不行要用id_
data = page.find_all('div', class_='item')
# data = page.find_all('div', attrs={'class': 'item'})

for item in data:
  # 3.查找标题
  title = item.find('span', class_='title').text # .text表示拿到的标记内容
  # 4.查找评分
  score = item.find('span', class_='rating_num').text
  # 6.写入csv文件
  csvwriter.writerow([title, score])


