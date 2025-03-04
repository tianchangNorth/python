# 元组的元素不可修改   

# 创建元组
t = (1, 8, 3, 9, 5)

# 只有一个元素要加,
t1  = (1,)
print(type(t1))

print(t,t[0],t[2:4])

t2 = t + t1
print(t2)

print(len(t))
print(t*4)