fn = "test.txt"
with open(fn) as file_Obj:
    obj_list = file_Obj.readlines()  # 每次讀取一行

# 列印串列內容
# print(obj_list)

for line in obj_list:
    print(line.rstrip())
