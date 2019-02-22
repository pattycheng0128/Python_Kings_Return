#
import os

# 列出目前工作的目錄
print (os.getcwd())  # D:\Python課程\Python王者歸來\file
# 列出目前工作目錄的絕對路徑
print(os.path.abspath('.'))  # D:\Python課程\Python王者歸來\file
# 列出上一層工作目錄的絕對路徑
print(os.path.abspath('..'))  # D:\Python課程\Python王者歸來
# 列出目前檔案的絕對路徑
print(os.path.abspath('ch14_1.py'))