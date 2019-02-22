import os
import time

class Check_OS():

    def __init__(self):
        self.myfile = "test.py"

    def check_mydir(self):
        if os.path.exists(self.myfile):
            os.mkdir(self.myfile)
        else:
            print("%s資料夾已存在" % self.myfile)

    def check_myfile(self):
        if os.path.exists(self.myfile):
            os.remove("test.py")
            print("%s已刪除成功" % self.myfile)
        else:
            print("%s檔案已不存在" % self.myfile)


if __name__ == '__main__':
    test = Check_OS()
    test.check_mydir()
    time.sleep(3)
    test.check_myfile()

