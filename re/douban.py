import re
import requests

findSrc = re.compile(r'<img[^>]*width="100"[^>]*src="([^"]+)"', re.S)
findTitle = re.compile(r'<span class="title">([^<&]+)</span>', re.S)
findRate = re.compile(r'<span class="rating_num" property="v:average">([^<&]+)</span>', re.S)

url = 'https://movie.douban.com/top250'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

res = requests.get(url,headers=headers,verify=False)
data = []

img = findSrc.findall(res.text)
name = findTitle.findall(res.text)
rate = findRate.findall(res.text)
data.append(img)
data.append(name)
data.append(rate)

for img,name,rate in zip(data[0],data[1],data[2]):
    print('序号:',data[0].index(img)+1)
    print('图片：',img)
    print('名称：',name)
    print('评分：',rate)
    print('--------------------')