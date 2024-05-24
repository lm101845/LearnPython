# @Date : 2024/3/19 15:34
# @Author : liming

import requests
from lxml import etree

url = "https://www.zbj.com/fw/?k=sass"
resp = requests.get(url)

html = etree.HTML(resp.text)

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div[1]/div')
# print(resp.text)
for div in divs:
    price = div.xpath('./div/div/div')
    company = div.xpath('./div[3]/div[1]/a/span/text()')[0]
    print(price, company)