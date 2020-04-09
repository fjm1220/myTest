from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# time.sleep(3)

# driver.find_element_by_id("kw").send_keys("虞书欣")
# time.sleep(5)
# driver.find_element_by_id("kw").clear()

# driver.find_element_by_id("kw").send_keys("谢可寅")
# driver.find_element_by_id("su").submit()

#data = driver.find_element_by_name("tj_trnews").text
#print(data)

driver.find_element_by_id("kw").send_keys("乃万")
driver.find_element_by_id("su").submit()

# time.sleep(10)
#智能等待
driver.implicitly_wait(10)
driver.find_element_by_link_text("乃万_百度百科").click()

time.sleep(5)
driver.quit()
