import bs4

# 開啟檔案並定義編碼為utf-8
htmlFile = open("myhtml.html", encoding="utf-8")
# 解析網頁內容
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
# 搜尋img標籤
imgTag = objSoup.select("img")
for i in range(len(imgTag)):
    print(imgTag[i])
    print(imgTag[i].get("src"))
