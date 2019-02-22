import requests

url = "http://www.deepstone.com.tw"
try:
    htmlfile = requests.get(url)
    print("download success")
except Exception as err:
    print("download error:%s" % err)

# 儲存網頁內容

fn = "out21_11_1.txt"
with open(fn, "wb") as file_Obj:
    for diskStorage in htmlfile.iter_content(10240):
        size = file_Obj.write(diskStorage)
        print(size)
    print("以%s儲存網頁HTML檔案成功" % fn)
