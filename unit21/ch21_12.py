import requests, bs4

url = "http://www.grandtech.info"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")
print(type(objSoup))