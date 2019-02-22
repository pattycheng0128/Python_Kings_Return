import bs4, requests, os


url = "http://www.grandtech.info/"
html = requests.get(url)
print("網頁下載中....")
html.raise_for_status()   # 驗證網頁是否下載成功
print("確認網頁下載成功")

destDir = "grandtech"  # 設定未來儲存圖片的資料夾
# 判斷當資料夾不存在的話，就新建立一個資料夾
if os.path.exists(destDir) == False:
    os.mkdir(destDir)

# 建立BeautifulSoup物件
objSoup = bs4.BeautifulSoup(html.text, "lxml")

# 搜出所有圖片
imgTag = objSoup.select("img")
print("搜出圖片的數量", len(imgTag))

# 如果有找到圖片則執行裡面的內容
if len(imgTag) > 0:
    for i in range(len(imgTag)):
        # 取得圖片的路徑
        imgUrl = imgTag[i].get("src")
        print("%s圖片下載中" % imgUrl)
        finUrl = url + imgUrl   # 取得圖片在internet上的路徑
        print("%s圖片下載中" % finUrl)
        picture = requests.get(finUrl)  # 下載圖片
        # 驗證圖片是否有下載成功
        picture.raise_for_status()
        print("%s圖片下載成功" % finUrl)

        # 先開啟檔案，在儲存圖片
        pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), "wb")
        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()


else:
    print("無任何圖片")


