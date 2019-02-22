import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
objTag = objSoup.select("#author")
print(type(objSoup))
print(len(objSoup))
print("元素資料型態:", type(objTag[0]))
print("元素內容:", objTag[0].getText())