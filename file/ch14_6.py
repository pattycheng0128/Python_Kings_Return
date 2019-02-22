import os

mydir = "test_patty"
if os.path.exists(mydir):
    os.rmdir(mydir)
    print("刪除%s成功" % mydir)
else:
    print("%s資料夾不存在" % mydir)
