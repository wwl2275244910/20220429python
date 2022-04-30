from  selenium import webdriver
import time
d=webdriver.Chrome()
d.get("https://www.baidu.com")
d.maximize_window()
time.sleep(4)
d.close()