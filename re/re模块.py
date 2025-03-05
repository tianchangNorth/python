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

# print(match.group())

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

str1 = """
<div class='张三'>11111</div>
<div class='里斯'>22222</div>
<div class='王五'>33333</div>
<div class='赵六'>44444</div>
<div class='六七'>55555</div>'
"""

pattern = re.compile(r"<div class='(?P<name>.*?)'>(?P<list>.*?)</div>", re.S)

result = pattern.finditer(str1)

for i in result:
  print(i.group('name'))
  print(i.group('list'))