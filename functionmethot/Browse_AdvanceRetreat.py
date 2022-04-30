from selenium import webdriver
import  time
# 模拟浏览器前进后退操作
class AdvanceRetreat():
    def advance_retreat(self):
        # 使用浏览器选择要使用的浏览器
        driver = webdriver.Chrome()
        # 访问百度
        driver.get("https:www.baidu.com")
        # 窗口最大化
        driver.maximize_window()
        # 强制等待两秒
        time.sleep(2)
        # 访问网易
        driver.get('https://www.163.com')
        # 强制等待两秒
        time.sleep(2)
        # 回退到百度
        driver.back()
        # 强制等待两秒
        time.sleep(2)
        # 前进到网易
        driver.forward()
        # 强制等待一秒
        time.sleep(1)
        # 关闭浏览器
        driver.quit()
call = AdvanceRetreat()
call.advance_retreat()