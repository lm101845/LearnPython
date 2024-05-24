# @Date : 2024/3/18 11:33
# @Author : liming

import requests
import re
import csv

url = "https://movie.douban.com/top250"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

response = requests.get(url, headers=headers)

# print(response.text)

page_content = response.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*? <span class="title">(?P<name>.*?)'
                        r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                        r'<span>(?P<num>.*?)</span>',   re.S)

# 开始匹配
result = obj.finditer(page_content)
f = open("豆瓣top250.csv", mode="w", encoding="utf-8", newline="")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))  # 电影名字
    # print(it.group("score"))  # 电影评分
    # print(it.group("num"))  # 电影观看人数
    # print(it.group("year").strip())  # 电影年份
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    # 其中年份单独处理一下，去掉空格
    csvwriter.writerow(dic.values())
f.close()
print("over")
