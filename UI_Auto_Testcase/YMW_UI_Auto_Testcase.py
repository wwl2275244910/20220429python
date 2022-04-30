from selenium import webdriver
import unittest
import  time
class Ymw_Testcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/EasyBuy')
        self.driver.maximize_window()
        time.sleep(2)
    def test_login(self):
        # 点击右上角登录
        self.driver.find_element_by_link_text('登录').click()
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="loginName"]').send_keys('admin')
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        # 点击登录
        a=self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input')
        a.click()
        self.assertIsNotNone(a)
    def test_search(self):
        # 搜索输入框输入 香水
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/form/input[1]').send_keys('香水')
        # 点击搜索
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/form/input[2]').click()
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()




