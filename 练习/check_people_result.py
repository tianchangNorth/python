# 检查people.py中从第三行开始不在第一行的人员名单

# 读取第一行的人员名单
first_line_people = "赵戡;曹海清;曹云菲;常雨莎;程晓明;房莹;范静;付海巍;高飞(胖飞);高源(源);高宇声;韩江;哈悦;何佳雯;侯少斌(冬寒);黄建林;胡骁杰(huxiaojie);胡阳;荆雯;鞠文波;寇雨(Kool);蓝登峰(Quark);兰佳琪;类婷婷;冷佳恒(lengjiaheng);梁克雷;李博;李明宇;林博聪;李少辉;刘博雅;刘少东;刘伟(Vera);刘雅朦(Frances);刘彦飞;刘逸夫;李骁;李雪;李扬(liyang);李永;李志昊(-);罗丽娟;吕强(野狼);马超;马坷;孟宇光;苗慧;缪隆晟;聂世建;蒲天阳;申文奇;孙广毅;唐悦(Amy);王荷舒(Lotus Wang);王宁;吴笑逐;肖景方;辛晓亮(marsxxl);许晨阳(天畅);许磊(Leon);许绍楠(theivanxu);杨泊锐;杨程舒;杨东杰;杨久春;杨力尉;臧秀涛;张建平;张凯;张晓波;张泽帝;张哲;赵畅(Hex);赵海玲;钟雯婷(无);左欣悦;"

# 从第三行开始的人员名单
third_line_onwards = [
    "刘雅朦(Frances)", "李博", "许晨阳(天畅)", "罗丽娟", "张哲", "刘彦飞", "吕强(野狼)", "杨泊锐", "荆雯", "侯少斌(冬寒)",
    "黄建林", "冷佳恒(lengjiaheng)", "胡骁杰(huxiaojie)", "刘逸夫", "胡阳", "寇雨(Kool)", "孙广毅", "李明宇", "张晓波", "肖景方",
    "曹海清", "鞠文波", "高宇声", "聂世建", "杨力尉", "刘博雅", "左欣悦", "钟雯婷(无)", "王宁", "哈悦",
    "李骁", "苗慧", "梁克雷", "杨久春", "韩江", "辛晓亮(marsxxl)", "赵戡", "孟宇光", "缪隆晟", "许绍楠(theivanxu)",
    "唐悦(Amy)", "高飞(胖飞)", "张泽帝", "范静", "赵畅(Hex)", "马坷", "许磊(Leon)", "曹云菲", "李扬(liyang)", "臧秀涛",
    "刘少东", "蒲天阳", "李少辉", "常雨莎", "张凯", "杨程舒", "兰佳琪", "程晓明", "杨东杰", "刘伟(Vera)", "付海巍"
]

# 将第一行的人员名单转换为集合
first_line_set = set(first_line_people.split(';'))
first_line_set.discard('')  # 移除空字符串

# 将从第三行开始的人员名单转换为集合
third_line_set = set(third_line_onwards)

# 检查第一行中哪些人不在从第三行开始的名单中
not_in_third_line = []
for person in first_line_set:
    if person and person not in third_line_set:
        not_in_third_line.append(person)

print("第一行中不在下面人员名单中的人员：")
for person in sorted(not_in_third_line):
    print(f"- {person}")

print(f"\n总共有 {len(not_in_third_line)} 个人在第一行但不在下面的名单中")

# 同时输出第一行中的所有人员以便对比
print("\n第一行的所有人员：")
for person in sorted(first_line_set):
    if person:  # 排除空字符串
        print(f"- {person}")