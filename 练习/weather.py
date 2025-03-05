import requests
from bs4 import BeautifulSoup

url = 'http://www.weather.com.cn/weather1d/101020100.shtml'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # 提取温度数据（需根据实际网页结构调整选择器）
    temp = soup.find('input', id='hidden_title')
    print(temp)
    print(f'当前温度：{temp}')
except Exception as e:
    print(f'抓取失败：{str(e)}')