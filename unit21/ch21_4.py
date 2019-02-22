import requests

url = "http://www.yahoo.com"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
else:
    print("取的網頁內容失敗")
print("列印內容大小:", len(htmlfile.text))
print(htmlfile.text)