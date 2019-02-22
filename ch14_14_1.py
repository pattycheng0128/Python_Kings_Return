import os

print(os.getcwd())
for dirName, sub_dirNames, fileNames in os.walk("D:\\Python課程\\Python_Kings_Return\\"):
    print("目前工作目錄名稱:", dirName)
    print("==========================")
    print("目前子目錄名稱串列", sub_dirNames)
    print("==========================")
    print("目前檔案名稱串列", fileNames, "\n")
