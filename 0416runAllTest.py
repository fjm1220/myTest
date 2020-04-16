import os
import sys
import unittest
import time

from HTMLTestRunner import HTMLTestRunner

from src2.test import test_baidu1
from src2.test import test_baidu2


# 手工添加案例到套件
def createsuite():
    suite = unittest.TestSuite()
    # 将测试用例添加到测试套件中
    # # 1.addtest 按照添加顺序执行
    # suite.addTest(0416test1.Baidu1("test_hao"))
    # suite.addTest(0416test1.Baidu1("test_baidusearch"))
    # suite.addTest(0416test2.Baidu2("test_baidusearch"))
    # return suite

    # # 2.makeSuite,makeSuite可以将测试用例类中所有测试case组成测试套件
    # suite.addTest(unittest.makeSuite(0416test1.Baidu1))
    # suite.addTest(unittest.makeSuite(0426tes2.Baidu2))
    # return suite

    # #3.TetsLoader用于创建类和模块的测试套件
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(0416test1.Baidu1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(0416test2.Baidu2)
    # suite = unittest.TestSuite([suite1,suite2])
    # return suite

    # #4.discover通过递归方式到其子目录中从指定目录开始，找到所有测试模块并返回一个包含他们对象的TestSuite
    # # 然后进行加载与模式匹配唯一的测试文件
    discover = unittest.defaultTestLoader.discover('../test', pattern='test*.py', top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    # 生成HTML报告
    curpath = sys.path[0]
    # 取当地时间
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))

    if not os.path.exists(curpath + "/resultreport"):
        os.makedirs(curpath + "/resultreport")

    filename = curpath + "/resultreport/" + now + "resultreport.html"
    with open(filename, 'wb') as fp:

        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况", verbosity=2)
        suite = createsuite()
    # runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
