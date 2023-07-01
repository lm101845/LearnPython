"""
演示对函数（方法）进行类型注解
"""

# 对形参进行类型注解
def add(x: int, y: int):
    return x + y

# 对返回值进行类型注解
def func(data: list) -> list:
    return data

print(func(1))
