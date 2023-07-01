"""
演示使用pymysql库进行数据插入的操作
"""
from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名（IP）
    port=3306,          # 端口
    user="root",        # 账户
    password="123456",  # 密码
    autocommit=True     # 自动提交（确认）
)

# print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()      # 获取到游标对象
# 选择数据库
conn.select_db("world")
# 执行sql
cursor.execute("insert into student values(10002, '林俊节', 31, '男')")
# # 通过commit确认
# conn.commit()
# 关闭链接
conn.close()
