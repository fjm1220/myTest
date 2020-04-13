from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://127.0.0.1/biz/user-login-L2Jpei8=.html")
driver.implicitly_wait(10)

# 键盘按键用法
driver.find_element_by_id("account").send_keys("admin")
time.sleep(3)
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(3)
driver.quit()