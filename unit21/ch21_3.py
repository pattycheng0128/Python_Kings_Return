import requests

url = "http://www.google.com"
htmlfile = requests.get(url)
print(type(htmlfile))