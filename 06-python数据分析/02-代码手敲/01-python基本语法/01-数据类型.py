x = [1,2,3,4,5,1]
print(x)
print(x[:2])
print(x[2:])
print(x[2:-1])
# 2以后所有，但是去掉最后一个

print("早上好"[1])

y = (1,2,3,1)
print(y[2])

print("===============")
z = set(x)
print(z)

print(2 in z)
print(10 not in z)
print("===============")

# 字典和集合一样也是用大括号，但是装的东西不一样(key,value)形式
d = {'a':10,'b':2,'c':x}
print(d)
print(d.get('c'))
print(d['a'])
c = 3
print(d)
# 赋新值，但是没有任何变化——内外完全隔绝
print(d['c'][:2])
# 这种组合写法在python里面是非常常见的