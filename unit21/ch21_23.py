import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
imgTag = objSoup.select("img")

print(len(imgTag))
for i in range(len(imgTag)):
    print(imgTag[i])