import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
objTag = objSoup.select("p")

print(len(objTag))
print("----------------------")
for i in range(len(objTag)):
    print(type(objTag[i]))
    print("----------------------")
    print(str(objTag[0]))
    print("----------------------")
    print(objTag[i].getText())
    print("----------------------")
    print(objTag[i].text)
