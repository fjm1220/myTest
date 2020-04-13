from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# 鼠标事件
# ActionChains类
# ActionChains(driver)生成用户行为，将行动存储在ActionChains对象中。
# perfrom()执行所有存储的行为
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("孙燕姿")
su = driver.find_element_by_id("su")
# 右键
ActionChains(driver).context_click(su).perform()
time.sleep(4)
# 双击
ActionChains(driver).double_click(su).perform()
time.sleep(4)
# 拖动
title = driver.find_element_by_link_text("孙燕姿_百度百科")
target = driver.find_element_by_id("su")
ActionChains(driver).drag_and_drop(title, target)
time.sleep(4)
driver.quit()