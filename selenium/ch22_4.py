from selenium import webdriver
import time

browser = webdriver.Ie()
url = "http://tw.yahoo.com"
browser.get(url)

try:
    tag = browser.find_element_by_id("Eyebrow")
    print(tag.text)
    time.sleep(2)
    browser.close()

except Exception:
    print("沒有找到相符的id")