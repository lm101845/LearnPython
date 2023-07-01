from data_define import Record
from pymysql import Connection

f = open("d:/output.json", "w", encoding="UTF-8")
# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 查询
cursor.execute("SELECT * FROM orders")
result = cursor.fetchall()
for r in result:
    record = Record(r[0], r[1], r[2], r[3])
    f.write(record.to_json())
    f.write("\n")

# 关闭MySQL链接对象
conn.close()
f.close()
