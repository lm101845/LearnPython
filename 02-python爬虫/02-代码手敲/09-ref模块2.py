# @Date : 2024/3/17 13:04
# @Author : liming

import re

s = """
    <div class="jay"><span id='1'>郭麒麟</span></div>
    <div class="jj"><span id='2'>李白</span></div>
    <div class="jolin"><span id='3'>杜甫</span></div>
    <div class="sylar"><span id='4'>白居易</span></div>
    <div class="tory"><span id='5'>王安石</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='\d+'>(.*?)</span></div>",re.S)
# re.S表示让.可以匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group())  # 郭麒麟 李白 杜甫 白居易 王安石