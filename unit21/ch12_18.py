import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
objTag = objSoup.find_all("p")
for data in objTag:
    print(data.text)
print("-----------------------------------------")
print("使用getText()方法列印串列元素")
for i in range(len(objTag)):
    print(objTag[i].getText())