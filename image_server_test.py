from selenium import webdriver
import unittest
import time
class imageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://49.235.30.116:8080/image_server/images.html")
        self.driver.maximize_window()
        time.slee(5)
    def tearDown(self):
            self.driver.quit()
    def test_upload(self):
            self.driver.find_element_by_name("upload").send_keys("C:\\Users\\Administrator\\Pictures\\开心.jpg")
            self.driver.find_element_by_xpath("//*[@id='blo g-collapse']/form/div[2]/input").click()
            time.sleep(10)
    def test_delete(self):
            self.driver.find_element_by_xpath("//*[@id='container']/div[3]/button").click()
            time.sleep(10)
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(10)
if __name__=="__main__":
            unittest.main()
