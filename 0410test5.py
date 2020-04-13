from selenium import webdriver
import time
import os
driver = webdriver.Chrome()

# 定位一组元素  find_elements
# file_path='file:///'+os.path.abspath("E:\\java学习\\JAVA学习资料\\测试\\HTML\\checkbox.html")
# driver.get(file_path)
# inputs = driver.find_elements_by_tag_name("input")
# # get_attribute获取属性值
# for input in inputs:
#     if input.get_attribute('type') == "checkbox":
#         input.click()

# 多层框架窗口定位  switch_to.frame()
# 定位内层需从外层一层一层往里定位
# file_path='file:///'+os.path.abspath("E:\\java学习\\JAVA学习资料\\测试\\HTML\\frame.html")
# driver.get(file_path)
# driver.switch_to.frame("f1")
# driver.switch_to.frame("f2")
# driver.find_element_by_id("kw").send_keys("布拉格")
# driver.find_element_by_id("su").click()
# # 从frame中嵌套的页面中跳出，跳回原始的页面
# driver.switch_to.default_content()

# 层级定位
file_path='file:///'+os.path.abspath("E:\\java学习\\JAVA学习资料\\测试\\HTML\\level_locate.html")
driver.get(file_path)
driver.find_element_by_link_text("Link1").click()
driver.implicitly_wait(10)
list = driver.find_element_by_id("dropdown1").find_elements_by_link_text("Action")
# 移动
webdriver.ActionChains(driver).move_to_element(list[0]).perform()
time.sleep(5)
driver.quit()