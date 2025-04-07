import requests

url = 'https://www.zhihu.com/settings/profile'

# 构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://www.zhihu.com',  # 设置防盗链
    'Connection': 'keep-alive'  
}

try:
    # 发送请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功
    
    # 打印响应状态和内容
    print(f"状态码: {response.status_code}")
    print("请求成功！")
    print(f"响应内容: {response.text}")
    
except requests.RequestException as e:
    print(f"请求失败: {e}")
