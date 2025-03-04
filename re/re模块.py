import re

list = 'my phone number is 13512345678 , you can call me at 135123456178'

# 匹配电话号码
phone = re.findall(r'\d+', list)

print(phone)

# finditer()方法 返回一个迭代器

it = re.finditer(r'\d+', list)

for i in it:
  print(i.group())

# search()方法 返回第一个匹配对象

match = re.search(r'\d+', list)

print(match.group()) 

# match()方法 从头开始匹配

match = re.match(r'\d+', list)

print(match.group())

# compile()方法 编译正则表达式
# 1.提高效率
# 2.可以使用变量

pattern = re.compile(r'\d+')

phone = pattern.findall(list)

print(phone)

# re.S 让 . 可以匹配换行符
# re.I 忽略大小写
# re.M 多行匹配
# re.L 本地化识别