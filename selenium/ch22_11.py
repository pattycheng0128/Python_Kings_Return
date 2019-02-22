from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
url = "http://grandtech.info"
browser.get(url)

time.sleep(3)
browser.refresh()  # 更新網頁
time.sleep(3)
browser.quit()  # 關閉網頁
