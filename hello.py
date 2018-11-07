import keyword
import sys

print("Hello, World!")

print('\n1 keyword------------------------------')
print(keyword.kwlist)

print('\n2 if else------------------------------')

if True:
    print("True")
else:
    print("False")
    
print('\n3 输出字符串两次------------------------------')   
str='Runoob'
print(str * 2)             # 输出字符串两次

print('\n4 连接字符串------------------------------')
print(str + '你好')        # 连接字符串
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print('\n5================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\npython 路径为',sys.path)