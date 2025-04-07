import requests

# 会话
session = requests.Session()

# 登录
login_url = 'https://www.zhihu.com/signin?next=%2F'
login_data = {
    'username': 'username',
    'password': 'password'
}
session.post(login_url, data=login_data)

# 访问需要登录的页面
url = 'https://www.zhihu.com/settings/profile'
r = session.get(url)
print(r.text)