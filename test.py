"""
一、数据类型
1.  按经验将不同的变量存储不同的类型的数据
2. 验证这些数据到底是什么类型 -- 检测数据类型 -- type(数据)
"""
# int -- 整型
num1 = 1

# float -- 浮点型，就是小数
num2 = 1.1
print(type(num1))
print(type(num2))
# str -- 字符串，特点：数据都要带引号
a = 'hello world'
print(type(a))
# bool -- 布尔型，通常判断使用，布尔型有两个取值 True 和 False
b = True
print(type(b))
# list -- 列表
c = [10, 20, 30]
print(type(c))
# tuple -- 元组
d = (10, 20, 30)
print(type(d))
# set -- 集合
e = {10, 20, 30}
print(type(e))
# dict -- 字典 -- 键值对
f = {'name': 'TOM', 'age': 18}
print(type(f))
"""
二、输出演示
"""
name = 'TOM'
age = 18
weight = 75.5
# 我的名字是x，今年x岁了，体重x公斤
print('我的名字是%s，今年%s岁了，体重%s公斤' % (name, age, weight))

"""
三、格式化输出
1. 准备数据
2. 格式化符号输出数据
"""

age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000
# 1. 今年我的年龄是x岁 -- 整数 %d
print('今年我的年龄是%d岁' % age)
# 2. 我的名字是x -- 字符串 %s
print('我的名字是%s' % name)
# 3. 我的体重是x公斤 -- 浮点数 %f
print('我的体重是%.3f公斤' % weight)
# 4. 我的学号是x -- %d
print('我的学号是%d' % stu_id)
# 4.1 我的学号是001
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)
# 5. 我的名字是x，今年x岁了
print('我的名字是%s，今年%d岁了' % (name, age))
# 5.1 我的名字是x，明年x岁了
print('我的名字是%s，明年%d岁了' % (name, age + 1))
# 6. 我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%06d' % (name, age, weight, stu_id))