__author__ = "sunraylily"
from selenium import webdriver
import time
# 导入unittest包
import unittest
# 类名可以与文件名不同
class Baidu1(unittest.TestCase):
    # 初始化数据
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
# 测试用例必须以test开头

    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys(u"张杰")
        driver.find_element_by_id("su").click()

    # @unittest.skip("skipping")
    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("hao123").click()
        self.assertEqual(u"hao123_上网从这里开始", driver.title, msg = "hao123")

    # 清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors, msg = u"出错")
if __name__ == "__main__":
     # 执行用例
    #  verbosity参数可以表示测试结果的信息复杂度
    unittest.main()




