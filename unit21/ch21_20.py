import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
objTag = objSoup.select("#author")
print("列出串列元素的資料型態=", type(objTag[0]))
print(objTag[0])
print("列出str()轉換過程=", type(str(objTag[0])))
print(objTag[0])