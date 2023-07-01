import time


# account_amount = 0      # 账户余额
# def atm(num, deposit=True):
#     global account_amount
#     if deposit:
#         account_amount += num
#         print(f"存款:+{num}，账户余额:{account_amount}")
#     else:
#         account_amount -= num
#         print(f"取款:-{num}，账户余额:{account_amount}")
#
#
# atm(300)
# atm(300)
# atm(100, False)
#
#
# def account_create(initial_amount=0):
#     def atm(num, deposit=True):
#         nonlocal initial_amount
#         if deposit:
#             initial_amount += num
#             print(f"存款:+{num}，账户余额:{initial_amount}")
#         else:
#             initial_amount -= num
#             print(f"取款:-{num}，账户余额:{initial_amount}")
#
#     return atm
#
#
# fn = account_create()
# fn(300)
# fn(200)
# fn(300, False)
#

# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# fn1 = outer("黑马程序员")
# fn1("大家好呀")
# fn1("学Python就来")
#
# fn2 = outer("传智教育")
# fn2("IT职业教育培训")
# fn2("学Python就来")

# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
#
# fn = outer(10)
# fn(10)
# fn(10)

# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
#
# @outer
# def sleep():
#     import random
#     import time
#     print("睡眠中......")
#     time.sleep(random.randint(1, 5))
#
#
# sleep()




