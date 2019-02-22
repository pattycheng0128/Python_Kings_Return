from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
url = "http://grandtech.info"
browser.get(url)

elebody = browser.find_element_by_tag_name("body")
time.sleep(3)
elebody.send_keys(Keys.PAGE_DOWN)  # 網頁捲動到下一頁
print("PAGE_DOWN")
time.sleep(3)
elebody.send_keys(Keys.END)  # 網頁捲動到最底端
print("END")
time.sleep(3)
elebody.send_keys(Keys.PAGE_UP)  # 網頁捲動到上一頁
print("PAGE_UP")
time.sleep(3)
elebody.send_keys(Keys.HOME)  # 網頁捲動到最上端
print("Home")
time.sleep(3)
browser.quit()