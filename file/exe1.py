fn = "test2.txt"

with open(fn) as file_Obj:
    obj_list = file_Obj.readlines()

str_Obj = ""
space_Obj = "\u0020"
for line in obj_list:
    str_Obj += line.rstrip()
    str_Obj += space_Obj
print(str_Obj)