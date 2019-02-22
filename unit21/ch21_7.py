import requests
import re

url = "http://tw.yahoo.com"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("請輸入欲搜尋的字串:")
    # 使用方法1
    if pattern in htmlfile.text:
        print("搜尋%s成功" % pattern)
    else:
        print("搜尋%s失敗" % pattern)

    # 使用方法2，如果找到放在串列name內
    name = re.findall(pattern, htmlfile.text)
    if name != None:
        print("%s出現%d次" % (pattern, len(name)))
    else:
        print("%s出現0次" % pattern)

else:
    print("網頁下載失敗")