import re
import requests
import csv

Cookie = r'acw_tc=0b6e703e17413342054608620e9f88b7b3543b814dd60d99c6ea9c4d9123b9; atom_redirect=https%253A%252F%252Fatomgit.com%252F; Hm_lvt_3aae7019e3354d0d43daf0842ea3d4b2=1741231757; ATOMGIT_ID_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2NDlhNzVjNWQzMGIyYjBkM2RlOTA4NmUiLCJhdWQiOiI2MmQ3YTBlYmFmOTViZGFjZjc0ZmM2YjkiLCJpYXQiOjE3NDEzMzQyNDgsImV4cCI6MTc0MjU0Mzg0OCwiaXNzIjoiaHR0cHM6Ly9wYXNzcG9ydC5hdG9tZ2l0LmNvbS9vaWRjIiwibm9uY2UiOiJDOEZCeFNVR2NDIiwibmFtZSI6bnVsbCwiZ2l2ZW5fbmFtZSI6bnVsbCwibWlkZGxlX25hbWUiOm51bGwsImZhbWlseV9uYW1lIjpudWxsLCJuaWNrbmFtZSI6InRpYW5jaGFuZyIsInByZWZlcnJlZF91c2VybmFtZSI6bnVsbCwicHJvZmlsZSI6IuWJjeerr-S5i-iZju-8iOaBqeW4iCBoZXgtY2nvvIlcbiIsInBpY3R1cmUiOiIvL3N0YXRpYy5hdG9tZ2l0LmNvbS9zdGF0aWNzL2F1dGhpbmctY29uc29sZS8vdXBsb2Fkcy91c2VyLzE2OTgxOTc0MDgxNTJfNjcwNi5qcGVnIiwid2Vic2l0ZSI6Imh0dHBzOi8vdGlhbmNoYW5nLmF0b21naXQubmV0L29wZW5hdG9tLVItRC1EZXBhcnRtZW50LWJvb2svIiwiYmlydGhkYXRlIjpudWxsLCJnZW5kZXIiOiJVIiwiem9uZWluZm8iOm51bGwsImxvY2FsZSI6bnVsbCwidXBkYXRlZF9hdCI6IjIwMjUtMDMtMDdUMDc6NTc6MjcuMjI3WiIsImVtYWlsIjoieHVjaGVueWFuZ0BvcGVuYXRvbS5vcmciLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGhvbmVfbnVtYmVyIjoiMTg1MzkxNjI5NzIiLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiOnRydWV9.JjvFlH-_GQNePHlI6qW9tiam-yzYS8-N04D_ghYCHms; ATOMGIT_ACCESS_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlBTRkpTbFhZTGphbFA4RGZpUTZITk53TkFXM0FkT1dscTFKaVpTMmlkbFUifQ.eyJzdWIiOiI2NDlhNzVjNWQzMGIyYjBkM2RlOTA4NmUiLCJhdWQiOiI2MmQ3YTBlYmFmOTViZGFjZjc0ZmM2YjkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBlbWFpbCBwcm9maWxlIHBob25lIiwiaWF0IjoxNzQxMzM0MjQ4LCJleHAiOjE3NDI1NDM4NDgsImp0aSI6IlRWZGFVdGlCYkNVcTR2OUdhd2p0Z3pvbFZSakVXek8wNjV3WUMzTVhFYzUiLCJpc3MiOiJodHRwczovL3Bhc3Nwb3J0LmF0b21naXQuY29tL29pZGMifQ.rVw5vkMmj0DBlcjEnonAjwkihyAHQTTS-f3BNyYqP1-ptf3okH4bsDB8i7j_zcPcSVV1TJ2BmYBGgYu0MqAH6mrVUMYu8rMfG6PO1kbEcc36rFS5cC88p6TgdH6RDtazdwLVlfPuApo-06744k0u2KAorZvYdRbw9-OenaCqUhEFZa-kbeWTfaNLUiuOlbsmNGMKhO63ABj-ONAnLkjaWqOZcgtmqQxOjd1pEax9aAonxlMhsh6xI-oIXd07FGNW4DEzWdeZZ9dlbo1vCJgMnZLU0rdojU4cMBRcbfyW-7KYuDQAAGhN1WvX2jcCEHZG9I5yBIn4Y1TjylA3Jzl5ZQ; ATOMGIT_REFRESH_TOKEN=j6YiUk9nNVCU4qng89dBykCrSUZwrD7T7EXrDAZywzP; ATOMGIT_EXPIRES_IN=1209600; ATOMGIT_EXPIRES_AT=1742543848; DEFAULT_LANG=zh_CN; atom_user={%22id%22:%22649a75c5d30b2b0d3de9086e%22%2C%22username%22:%22tianchang%22%2C%22nickname%22:%22tianchang%22%2C%22photo%22:%22/uploads/user/1698197408152_6706.jpeg%22%2C%22userNameSpace%22:%22tianchang%22%2C%22phone%22:%2218539162972%22%2C%22phoneVerified%22:true%2C%22email%22:%22xuchenyang@openatom.org%22%2C%22emailVerified%22:true%2C%22adminRoleCode%22:null}; ak_user_locale=zh_CN; teambition_lang=zh_CN; Hm_lpvt_3aae7019e3354d0d43daf0842ea3d4b2=1741335223'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36', # 这里添加了逗号
  'content-type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json, text/javascript',
  'x-current-tenant-id':'6350c74b9de1ceb915a7638a'
}

# 将 Cookie 字符串转换为字典
cookie_dict = {}
for cookie in Cookie.split('; '):
    key, value = cookie.split('=', 1)
    cookie_dict[key] = value

f = open("commit.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)
# 添加禁用SSL警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

for j in range(0,10):
  url = f'https://atomgit.com/api/v4/projects/code_reviews/advanced_search_cr?_input_charset=utf-8&page={j}&search=&order_by=updated_at&state=merged&assignee_tb_ids=&author_tb_ids=&label_ids=&project_ids=33381043&per_page=100'
  response = requests.get(url, headers=headers, cookies=cookie_dict, verify=False)
  for i in response.json():
    csvwriter.writerow([i['created_at'],i['title']])  # 将字符串放入列表中
