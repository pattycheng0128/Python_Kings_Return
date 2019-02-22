import bs4

htmlfile = open("myhtml.html", encoding="utf-8")
print(type(htmlfile))
objSoup = bs4.BeautifulSoup(htmlfile, "lxml")
print(type(objSoup))
# title
print("物件類型=", type(objSoup.title))
print("列印title=", objSoup.title)

# 去除標籤，傳回文字
print("去除標籤，傳回文字=", objSoup.title.text)

# 傳回所找尋第一個符合的標籤find()
