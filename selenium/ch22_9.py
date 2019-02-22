from selenium import webdriver
import time

browser = webdriver.Chrome()
url = "http://grandtech.info"
browser.get(url)

txtBox = browser.find_element_by_id("key")
txtBox.send_keys("Patty")
time.sleep(5)
txtBox.submit()
# browser.quit()