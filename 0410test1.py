from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 浏览器最大化，设置浏览器的宽高，前进后退
driver.maximize_window()
# driver.find_element_by_link_text("hao123").click()
#
# time.sleep(5)
# driver.set_window_size(400, 800)
# time.sleep(3)
# driver.back()
# time.sleep(4)
# driver.forward()
# time.sleep(5)
# t = driver.title
# print(t)
# url = driver.current_url
# print(url)
# 控制浏览器滚动条
driver.find_element_by_id("kw").send_keys("毛不易")
driver.find_element_by_id("su").click()
time.sleep(4)
# 将滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(4)

# 将滚动条拖到顶部部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(4)
time.sleep(4)
driver.quit()