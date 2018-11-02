
print('\n算术运算------------------------------')
print((5 + 4))  # 加法 9

print(4.3 - 2) # 减法 2.3
print(3 * 7) # 乘法 21
print(2 / 4)  # 除法，得到一个浮点数 0.5
print(2 // 4) # 除法，得到一个整数 0
print(17 % 3) # 取余  2
print(2 ** 5) # 乘方 32

print('\n数值比较------------------------------')
a = 21
b = 10
c = 0

if (a == b):
    print("1 a 等于 b")
else:
    print("1 a 不等于 b")

if (a != b):
    print("2 a 不等于 b")
else:
    print("2 a 等于 b")

if (a < b):
    print("3 a 小于 b")
else:
    print("3 a 大于等于 b")

if (a > b):
    print("4 a 大于 b")
else:
    print("4 a 小于等于 b")


print('\n赋值运算------------------------------')
c = a + b
print("1 c 的值为：", c)

c += a
print("2 c 的值为：", c)

c *= a
print("3 c 的值为：", c)

c /= a
print("4 c 的值为：", c)

c = 2
c %= a
print("5 c 的值为：", c)

c **= a
print("6 c 的值为：", c)

c //= a
print("7 c 的值为：", c)

print('\n位运算------------------------------')
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2;  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)

print('\n逻辑运算------------------------------')
a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

print('\n成员运算------------------------------')
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")


print('\n身份运算------------------------------')
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
