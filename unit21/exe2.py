import webbrowser

url = "https://map.baidu.com/"
try:
    address = input("請輸入地址:")
    webbrowser.open(url + address)
except Exception:
    print("您輸入錯誤")