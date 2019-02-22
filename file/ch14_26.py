import os

fn = "test2.txt"
string = "Hellp Python test"

with open(fn, 'w') as file_Obj:
    if os.path.exists(fn):
        print("檔案存在")
        file_Obj.write(string)
    else:
        print("檔案不存在")
