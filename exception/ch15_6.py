fn = "test.txt"
try:
    with open(fn) as file_Obj:
        data = file_Obj.read()
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    wordList = data.split()  # 將文章轉為串列
    print(data)
    print(fn, "文章的字數是:", len(wordList))
