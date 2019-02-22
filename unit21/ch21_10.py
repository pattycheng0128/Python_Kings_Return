import requests

url = "http://www.gzaxxc.com/file_not_existed"

try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:
    print("網頁下載失敗:%s" % err)

