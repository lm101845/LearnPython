# @Date : 2024/3/18 15:52
# @Author : liming

import requests
from bs4 import BeautifulSoup

url = "https://www.duitang.com/search/?kw=%E6%B2%BB%E6%84%88&type=feed"

resp = requests.get(url)
resp.encoding = "utf-8"

# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")

alist = main_page.find("ul").find_all("a")   #范围第一次缩小

print(alist)

