import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
objTag = objSoup.select("#author")
print(str(objTag[0].attrs))