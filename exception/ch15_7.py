def wordsNum(fn):
    try:
        with open(fn) as file_obj:
            data = file_obj.read()
    except FileNotFoundError:
        print("找不到 %s 檔案" % fn)
    else:
        wordList = data.split()  # 將文章轉為串列
        print(fn, "文章的字數:", len(wordList))

file = "test.txt"
wordsNum(file)

