
print('\n1 基本数据类型------------------------------')  
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
 
print(counter)
print(miles)
print(name)

print('\n2 多个变量赋值------------------------------')  
a = b = c = 1
a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)

print('\n3 变量所指的对象类型------------------------------')
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))