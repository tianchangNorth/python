a = [1,2,3,4]
b = [1,2,3,4]
print(a[0])

a.append([1,2,3])
print(a)

a.insert(1,100)
print(a)

a.extend(b)
print(a)

a[0] = 100
print(a)

a.pop(3)

print(a)

a.remove(1)
print(a)

c = input('please input any key: ')

if int(c) in a:
  print('yes')
else:
  print('no')

if int(c) not in a:
  print('yes')
else:
  print('no')

