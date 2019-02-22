import keyword

keywordLists = ["as", "while", "if", "hello", "like"]
for x in keywordLists:
    print("%s是否為關鍵字:%s" % (x, keyword.iskeyword(x)))