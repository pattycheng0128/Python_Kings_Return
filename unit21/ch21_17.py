import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
objTag = objSoup.find_all("p")

print("列印objSoup資料型態:", type(objSoup))
print("列印objSoup資料型態:", type(objTag))
print("------------------------------------")
print(objTag)
for tag in objTag:
    print(tag.text)