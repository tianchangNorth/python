# 读取文件内容
with open(r'D:\py\人员对比\people.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 解析第一行的人员名单
first_line = lines[0].strip()
# 移除开头的"# "
first_line = first_line[2:] if first_line.startswith('# ') else first_line
# 按分号分割人员名单
first_line_names = set(name.strip() for name in first_line.split(';') if name.strip())

print(f"第一行共有 {len(first_line_names)} 个人员")

# 提取从第三行开始的人员名单
other_names = []
for i in range(2, len(lines)):  # 从第三行开始（索引2）
    line = lines[i].strip()
    if line.startswith('# '):
        name = line[2:].strip()  # 移除"# "前缀
        if name:
            other_names.append(name)

print(f"从第三行开始共有 {len(other_names)} 个人员")

# 找出第一行中不在下面人员中的人
other_names_set = set(other_names)
not_in_other_lines = []
for name in first_line_names:
    if name not in other_names_set:
        not_in_other_lines.append(name)

print(f"\n第一行中不在下面人员中的共有 {len(not_in_other_lines)} 个：")
for i, name in enumerate(sorted(not_in_other_lines), 1):
    print(f"{i}. {name}")