import requests
import os

url = 'https://www.openatom.cn/api/committee/member/v1/list'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}
data = {
    'committeeType': 4,
    'lc': 'zh'
}

# 创建保存图片的文件夹
save_dir = 'committee_photos_2'
os.makedirs(save_dir, exist_ok=True)

res = requests.post(url=url, headers=headers, json=data)
info = res.json()['data']

for i in info:
    name = i['name'].strip()
    photo_url = i['photo']

    if not photo_url:
        print(f"{name} 没有照片，跳过")
        continue

    try:
        img_res = requests.get(photo_url, stream=True)
        if img_res.status_code == 200:
            ext = os.path.splitext(photo_url)[1] or '.png'  # 获取图片扩展名
            filename = f"{name}{ext}"
            filepath = os.path.join(save_dir, filename)
            with open(filepath, 'wb') as f:
                for chunk in img_res.iter_content(1024):
                    f.write(chunk)
            print(f"已保存: {filepath}")
        else:
            print(f"{name} 照片下载失败，状态码: {img_res.status_code}")
    except Exception as e:
        print(f"{name} 照片下载异常: {e}")
