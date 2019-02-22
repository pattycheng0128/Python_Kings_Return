import requests, bs4, os

#  1.確認網址下載是否正確
try:
    url = "https://tw.yahoo.com/"
    html = requests.get(url)
    print("網頁下載中....")
    html.raise_for_status()  # 驗證網頁是否下載成功
    print("確認網頁下載成功")
except Exception as err:
    print("網頁下載失敗，請確認網址是否正確", err)

#  2.確認儲存圖片的資料夾是否存在，不存在就新建一個資料夾
destDir = "yahoo"  # 設定未來儲存圖片的資料夾
# 判斷當資料夾不存在的話，就新建立一個資料夾
if os.path.exists(destDir) == False:
    os.mkdir(destDir)

# 建立BeautifulSoup物件
objSoup = bs4.BeautifulSoup(html.text, "lxml")

# 搜出所有圖片
imgTag = objSoup.select("img")
print("搜出圖片的數量", len(imgTag))  # 確認圖片數量

try:
    if len(imgTag) > 0:
        for i in range(len(imgTag)):
            #  取得圖片的路徑
            imgUrl = imgTag[i].get('src')  # 取得圖片路徑
            print("圖片下載中", imgUrl)
            # 驗證圖片是否下載成功
            picture = requests.get(imgUrl)
            picture.raise_for_status()
            print("圖片下載成功", imgUrl)

            # 先開啟檔案，在儲存圖片
            pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), "wb")
            for diskStorage in picture.iter_content(10240):
                pictFile.write(diskStorage)
            pictFile.close()
except Exception as err:
    print("存檔失敗", err)




