import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1;WOW64)\
           AppleWebKit/537.36(KHTML, like Gecko) Chrome/45.0.2454.101Safari/537.36"}

url = "https://www.liontravel.com/"
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器解取網路資料成功")
