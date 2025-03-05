import csv
from bs4 import BeautifulSoup
import requests

with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['排名', '标题', '评分'])

    for page in range(0, 250, 25):  # 分页处理
        url = f'https://movie.douban.com/top250?start={page}'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        
        for item in soup.select('.item'):
            title = item.select_one('.title').text
            rating = item.select_one('.rating_num').text
            writer.writerow([page//25+1, title, rating])