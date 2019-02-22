import os

mydir = "test_patty"
if os.path.exists(mydir):
    print("已經存在")
else:
    os.mkdir(mydir)
    print("建立%s資料夾成功" % dir)