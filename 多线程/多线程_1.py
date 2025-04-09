# 启动每一个程序都会默认有一个主线程

# 单线程
# def func():
#   for i in range(10):
#     print('func', i)

# if __name__ == '__main__':
#   func()
#   for i in range(10):
#     print('main', i)

# 多线程
from threading import Thread

def func():
  for i in range(10):
    print('func', i)

if __name__ == '__main__':
  t = Thread(target=func)
  t.start()
  for i in range(10):
    print('main', i)