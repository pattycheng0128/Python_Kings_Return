from selenium import webdriver
import time

browser = webdriver.Chrome()
url = "http://aaa.24ht.com.tw"
browser.get(url)

tag1 = browser.find_element_by_tag_name("title")
print("標籤名稱:%s,內容是:%s" % (tag1.tag_name, tag1.text))
print("------------------------------------------------")
tag2 = browser.find_element_by_id("author")
print("標籤名稱:%s,內容是:%s" % (tag2.tag_name, tag2.text))
print("------------------------------------------------")
tag3 = browser.find_elements_by_id("content")
for i in range(len(tag3)):
    print("標籤名稱:%s,內容是:%s" % (tag3[i].tag_name, tag3[i].text))
print("------------------------------------------------")
tag4 = browser.find_elements_by_tag_name("p")
for i in range(len(tag4)):
    print("標籤名稱:%s,內容是:%s" % (tag4[i].tag_name, tag4[i].text))
print("------------------------------------------------")
tag5 = browser.find_elements_by_tag_name("img")
for i in range(len(tag5)):
    print("標籤名稱:%s,內容是:%s" % (tag5[i].tag_name, tag5[i].get_attribute("src")))

time.sleep(2)
browser.quit()