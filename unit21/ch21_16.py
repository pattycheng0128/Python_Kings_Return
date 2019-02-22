import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
objTag = objSoup.find("p")

print("資料型態:", type(objSoup))
print("列印tag:", objTag)
print("列印tag文字:", objTag.text)