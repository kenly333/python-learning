

print('\n set------------------------------')

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
print(a) # {'r', 'a', 'b', 'c', 'd'}

b = set('alacazam')
print(b) # {'m', 'z', 'l', 'a', 'c'}

print(a - b)  # a和b的差集 {'d', 'r', 'b'}

print(a | b)  # a和b的并集 {'r', 'm', 'z', 'l', 'a', 'b', 'c', 'd'}

print(a & b)  # a和b的交集 {'a', 'c'}

print(a ^ b)  # a和b中不同时存在的元素 {'r', 'm', 'z', 'b', 'd', 'l'}