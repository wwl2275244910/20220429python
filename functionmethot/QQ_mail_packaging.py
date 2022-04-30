from selenium import  webdriver
import  time
import cv2 as cv
import urllib.request
from functionmethot.SlidingValidation import SlidingValidation
class QQmail():
    def __int__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.maximize_window()

    def open_url(self):
        self.__int__()
        self.url = 'https://mail.qq.com/'
        self.driver.get(self.url)
        self.driver.switch_to.frame('login_frame')

    def Login(self,username,password):
        self.open_url()
        #self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        try:
            self.driver.find_element_by_xpath('//*[@class="face"]').click()

        except:
            # 输入账号
            self.driver.find_element_by_id("u").send_keys(username)
            # 输入密码
            self.driver.find_element_by_id("p").send_keys(password)
            # 点击登录
            time.sleep(1)
            self.driver.find_element_by_id("login_button").click()
            time.sleep(3)

    def xiexin(self):
        self.driver.find_element_by_xpath('//*[@id="composebtn"]').click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('2649991429@qq.com')
        self.driver.find_element_by_xpath('//*[@id="subject"]').send_keys('自动化测试')
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//iframe[@class="qmEditorIfrmEditArea"]'))
        self.driver.find_element_by_xpath('/html/body').send_keys('好累呀')
        time.sleep(2)
        # 选择一个默认的框架，再去跳转到 mianFrame，
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/div[1]/a[1]').click()







