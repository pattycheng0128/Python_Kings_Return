from selenium import webdriver
import time

browser = webdriver.Chrome()
url = "http://grandtech.info"
browser.get(url)

# eleLink要點選的元素名稱的變數
eleLink = browser.find_element_by_link_text("認證考試")
print(type(eleLink))
time.sleep(5)
# 連到認證考試
eleLink.click()

browser.quit()
