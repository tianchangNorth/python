import json

# file = open('./file1.txt','w')

# list = [1,2,3,4]

# file.write(json.dumps(list))

# file.close()

# file = open('./file1.txt','r')

# file_content = file.read()
# print(json.loads(file_content))
# file.close()

# file = open('./file1.txt','w')
# mame_list = ['张三','李四','王五']
# json.dump(mame_list,file)
# file.close() 


file = open('./file1.txt','r')
name_list = json.load(file)
print(name_list)
file.close()