import requests

url = "http://aaa.24ht.com.tw"
htmlfile = requests.get(url)
htmlfile.raise_for_status()