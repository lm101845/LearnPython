# @Date : 2024/3/22 13:30
# @Author : liming

import requests

session = requests.session()

data = {
    "LoginForm[username]": "libai123",
    "LoginForm[password]": "123456aA"
}
url = "https://www.xbiqugu.info/login.php?jumpurl=https://www.xbiqugu.info/"

session.post(url, data=data)

resp = session.get("https://www.xbiqugu.info/modules/article/bookcase.php")

print(resp.json())
