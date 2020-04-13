from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 键盘事件
# 键盘组合
driver.find_element_by_id("kw").send_keys("毛不易")
driver.find_element_by_id("su").click()
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(5)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)
driver.find_element_by_id("kw").send_keys("无问")
# driver.find_element_by_id("su").click()
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()

