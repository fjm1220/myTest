from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
# div对话框处理
# file_path = 'file:///' + os.path.abspath(r"E:\\java学习\\JAVA学习资料\\测试\HTML\\modal.html")
# driver.get(file_path)
# driver.find_element_by_id("show_modal").click()
# time.sleep(4)
# driver.find_element_by_class_name("modal-body").find_element_by_id("click").click()
# time.sleep(4)
# # 如果只有一个button组就可以直接定位，否则要先定位到相应的div
# # but = driver.find_elements_by_tag_name("button")
# # but[0].click()
# buttons=driver.find_element_by_class_name("modal-footer").find_elements_by_tag_name("button")
# buttons[0].click()

# 文件上传操作
file_path = 'file:///' + os.path.abspath(r"E:\\java学习\\JAVA学习资料\\测试\HTML\\upload.html")
driver.get(file_path)
time.sleep(3)
driver.find_element_by_name("file").send_keys(r"E:\\java学习\\JAVA学习资料\\测试\HTML\\alert.html")
time.sleep(4)
driver.quit()

