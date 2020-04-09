from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)

# driver.find_element_by_name("wd").send_keys("大虞海棠")
# driver.find_element_by_id("kw").send_keys("赵小棠")
# driver.find_element_by_class_name("s_ipt").send_keys("终南山")
# driver.find_element_by_id("#su").click

# driver.find_element_by_tag_name("input").send_keys("抗击疫情")

# driver.find_element_by_css_selector("#kw").send_keys("终南山")
# driver.find_element_by_id("#su").click

# driver.find_element_by_xpath("//*[@id='kw']").send_keys("青春有你2")
# driver.find_elements_by_xpath("//*[@id='su]").click()

# 文字连接
# driver.find_element_by_link_text("贴吧").click()

# 部分链接定位,链接的部分进行匹配
#driver.find_element_by_partial_link_text("hao").click()

time.sleep(6)
driver.quit()