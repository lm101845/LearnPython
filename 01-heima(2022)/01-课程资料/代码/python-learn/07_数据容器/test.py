
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        new_list.append(my_list[i])
    i += 1

print(f"偶数形成的新列表：{new_list}")


