# requests���԰����ǵ�"��һ���������.py"����Ĵ�����н�һ���ļ�

# requests不是Python自带的库，所以需要进行额外安装

# 安装requests
# pip install requests

# 国内清华源
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests


import requests
query = input("请输入一个你喜欢的明星")

# url = 'https://www.sogou.com/web?query=周杰伦'
url = f'https://www.sogou.com/web?query={query}'

dic = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
resp = requests.get(url, headers=dic)  # 处理了一个小小的反爬

# 浏览器地址栏里的url统一都是用的GET请求。
# requests.get()

print(resp)
print(resp.text)  # 拿到页面源代码
