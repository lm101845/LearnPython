# @Date : 2024/3/18 12:06
# @Author : liming
import requests
import re

domain = "https://dytt89.com"

requests.packages.urllib3.disable_warnings()

resp = requests.get(domain, verify=False)
# verify=False 代表不验证证书
resp.encoding = "gb2312"

obj1 = re.compile(r"2024年必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group("ul")
    # 提取子页面链接
    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面链接
        child_href = domain + itt.group("href").strip("/")
        child_href_list.append(child_href)   # 存储子页面链接

# 提取子页面数据
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = "gb2312"
    print(child_resp.text)

