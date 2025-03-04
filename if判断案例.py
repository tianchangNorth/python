a = input('请输入年龄：')

a = int(a)
if(a>=18):
    print('去上网吧')
else:
    print('回家写作业')

if(a>=18):
    print('去上网吧')
elif(a>=16):
    print('去玩游戏')
elif(a>=14):
    print('去看电影')
else:
    print('回家写作业')