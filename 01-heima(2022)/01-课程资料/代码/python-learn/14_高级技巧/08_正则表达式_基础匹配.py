"""
演示Python正则表达式re模块的3个基础匹配方法
"""
import re

s = "1python itheima python python"
# match 从头匹配
result = re.match("python", s)
print(result)
# print(result.span())
# print(result.group())
# search 搜索匹配

result = re.search("python2", s)
print(result)
# findall 搜索全部匹配
result = re.findall("python", s)
print(result)

