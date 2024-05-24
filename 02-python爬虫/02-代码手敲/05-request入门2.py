# @Date : 2024/3/16 11:58
# @Author : liming

import requests

url = "https://fanyi.baidu.com/sug"

s = input("请输入要翻译的单词：")

dat = {
    "kw": s
}

# 发送Post请求,发送的数据必须放在字典中，然后通过data参数传递
resp = requests.post(url,data=dat)

print(resp.text)
print(resp.json())  # 将返回的json字符串转换成字典

