# @Date : 2024/3/18 15:27
# @Author : liming

import requests
from bs4 import BeautifulSoup
url = "www.xinfadi.com.cn/index.html"
response = requests.get(url)

# print(response.text)

# 把网页源码交给bs4处理
page = BeautifulSoup(response.text, "html.parser")   # html.parser是bs4内置的解析器

# table = page.find("div",class_ = "col-item")
table = page.find("div",attrs={"class":"tablebox"})
print(table)
