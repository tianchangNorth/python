import requests
from lxml import etree

url = r"https://www.zbj.com/fw/?k=%E5%89%8D%E7%AB%AF"

res = requests.get(url)

tree = etree.HTML(res.text)

doms = tree.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div')

for item in doms:
  print(item.xpath('./div/div[@class="bot-content"]/div[2]/a/span/text()'))