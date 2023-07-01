"""
演示非单例模式的效果
"""

class StrTools:
    pass

s1 = StrTools()
s2 = StrTools()
print(id(s1))
print(id(s2))
