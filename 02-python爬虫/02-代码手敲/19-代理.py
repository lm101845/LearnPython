# @Date : 2024/3/22 20:38
# @Author : liming

import requests

# 118.25.155.223 3128
proxies = {
    "https": "https://118.25.155.223:3128",
}

resp = requests.get("http://www.baidu.com",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
