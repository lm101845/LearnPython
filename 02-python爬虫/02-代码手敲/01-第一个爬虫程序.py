# -*- coding：utf-8 -*-
# 爬虫：通过编写程序的方式来获取互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容
# python搞定以上需求，特别简单


from urllib.request import urlopen

url = 'http://www.baidu.com'

resp = urlopen(url)

# print(resp.read().decode('utf-8'))

with open('mybaidu.html', mode="w")as f:
    f.write(resp.read().decode('utf-8'))  # 读取到网页的页面源代码
    print("over!")
