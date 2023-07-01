"""
演示Union联合类型注解
"""
# 使用Union类型，必须先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]

def func(data: Union[int, str]) -> Union[int, str]:
    pass

