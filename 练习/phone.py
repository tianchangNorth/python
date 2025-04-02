import requests
import re
import pandas as pd
import time

def get_carrier(phone):
    try:
        pattern = re.compile(r'<a href="https://www.haoshudi.com/liantong.htm" target="_blank" rel="nofollow">(?P<type>.*?)</a>', re.S)
        url = f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        result = pattern.search(response.text)
        return result.group('type') if result else "未知"
    except Exception as e:
        return "查询失败"

# 读取Excel文件
try:
    df = pd.read_excel('input.xlsx')  # 确保input.xlsx在同一目录下
    
    # 添加新列用于存储运营商信息
    df['运营商'] = ''
    
    # 遍历每行获取运营商信息
    for index, row in df.iterrows():
        phone = str(row['手机号'])  # 确保手机号转换为字符串
        carrier = get_carrier(phone)
        df.at[index, '运营商'] = carrier
        time.sleep(1)  # 添加延时防止被封
        print(f"正在处理: {row['姓名']} - {phone} - {carrier}")
    
    # 保存结果到新的Excel文件
    df.to_excel('output.xlsx', index=False)
    print("处理完成！结果已保存到 output.xlsx")

except Exception as e:
    print(f"发生错误: {str(e)}")