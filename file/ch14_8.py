import os

newdir = "python_test"
currentdir = os.getcwd()
print("列出目前工作資料夾:",currentdir)

# 如果newdir資料夾不存在，就新建一個
if os.path.exists(newdir):
    print("%s資料夾已存在" % newdir)
else:
    os.mkdir(newdir)
    print("建立%s資料夾成功" % newdir)

# 將目前的工作資料夾改至newdir
os.chdir(newdir)
print("列出最新工作資料夾:", os.getcwd())

# 將目前工作資料夾返回
os.chdir(currentdir)
print("列出返回工作資料夾", currentdir)

