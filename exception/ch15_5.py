fn = "test.txt"

try:
    with open(fn) as file_Obj:
        data = file_Obj.read()
except FileNotFoundError:
    print("找不到%s檔案" % fn)
else:
    print(data)
