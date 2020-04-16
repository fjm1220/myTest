from selenium import webdriver
import time
import unittest

class Baidu2(unittest.TestCase):
    # 数据初始化
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
#     测试用例，必须以test开头
    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys(u"谢娜")
        driver.find_element_by_id("su").click()

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verificationErrors, msg = u"出错")

if __name__ == "__main__":
    unittest.main()
