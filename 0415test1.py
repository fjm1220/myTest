from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
# 下拉框处理
# file_path = 'file:///' + os.path.abspath(r"E:\\java学习\\JAVA学习资料\\测试\HTML\\drop_down.html")
# driver.get(file_path)
# time.sleep(4)
# # 定位到下拉框
# m1 = driver.find_element_by_id("ShippingMethod")
# # m.find_element_by_xpath("//*[@value='10.69']").click(
# m1.find_element_by_xpath("//option[@value='10.69']").click()
# time.sleep(3)
# m1.find_element_by_xpath("//option[@value='11.61']").click()

# alert处理
# file_path='file:///'+os.path.abspath(r"E:\\java学习\\JAVA学习资料\\测试\HTML\\alert.html")
# driver.get(file_path)
# # 点击链接，弹出alert
# driver.find_element_by_id("tooltip").click()
# time.sleep(2)
# # 跳转到alert
# # 注意：alert= driver.switch_to.alert()是错误的
# alert= driver.switch_to.alert
# # 打印出alert框的内容
# # print (alert.text)
# # 点击确认按钮，接受警告信息
# # alert.accept()
# # 点击取消按钮，也可以取消alert框
# # alert.dismiss()

#send—_keys
file_path='file:///'+os.path.abspath("E:\\java学习\\JAVA学习资料\\测试\\HTML\\send.html")
driver.get(file_path)
driver.find_element_by_tag_name("input").click()
alert = driver.switch_to.alert
alert.send_keys("python")
time.sleep(3)
alert.accept()
time.sleep(5)
driver.quit()
