import pandas as pd
pd.options.display.max_columns = 10 # 设置最大显示列数

print(pd.__version__)

# 以字典形式按列提供数据
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df1)

print("===============")
# 以list形式按行提供数据
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'])
print(df2)

print("===============")

print(type(df1.get('A')))

# s1中的每一列都是一个Series
s1 = pd.Series(["test","train","test","hot"])
print(s1)

print("================")

s2 = pd.Series(data=[1,2,3,4], name="test")
print(s2)