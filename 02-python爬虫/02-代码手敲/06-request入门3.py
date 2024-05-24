# @Date : 2024/3/17 12:00
# @Author : liming
import requests

# url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=None&start=0&limit=20"
# 这种写法很长
url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "None",
    "start": "0",
    "limit": "20"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/89.0.4389.82 Safari/537.36"
}
# 发送请求
response = requests.get(url, params=params, headers=headers)
print(response.request.url)  # 打印出来的url就是带参数的url
print("==============")
print(response.text)
print("==============")
print(response.json())
print("==============")
print(response.request.headers)  # 打印请求头

response.close()  # 关闭请求
