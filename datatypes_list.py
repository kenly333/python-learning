

print('\n list------------------------------')

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素

print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

print('\n list元素操作------------------------------')
a = [1, 2, 3, 4, 5, 6]  # [1, 2, 3, 4, 5, 6]
print(a)

a[0] = 9 # [9, 2, 3, 4, 5, 6]
print(a)

a[2:5] = [13, 14, 15] # [9, 2, 13, 14, 15, 6]
print(a)

a[2:5] = []   # 将对应的元素值设置为 []  [9, 2, 6]
print(a)