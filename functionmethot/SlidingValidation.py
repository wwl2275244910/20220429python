from selenium import webdriver
import time
import urllib.request
import cv2 as cv
class SlidingValidation():
    def get_pos(image):
        global x
        blurred = cv.GaussianBlur(image, (5, 5), 0)
        canny = cv.Canny(blurred, 200, 400)
        contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for i, contour in enumerate(contours):
            M = cv.moments(contour)
            if M['m00'] == 0:
                cx = cy = 0
            else:
                cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
            if 6000 < cv.contourArea(contour) < 8000 and 370 < cv.arcLength(contour, True) < 390:
                if cx < 400:
                    continue
                x, y, w, h = cv.boundingRect(contour)  # 外接矩形
                cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv.imshow('image', image)

        return x

# driver.switch_to.frame("tcaptcha_iframe")
# #driver.find_element_by_xpath('//*[@id="slideBg"]').screenshot('123.png')
# url1 = driver.find_element_by_xpath('//*[@id="slideBg"]').get_attribute("src")
# url2 = driver.find_element_by_xpath('//*[@id="slideBlock"]').get_attribute("src")
# urllib.request.urlretrieve(url1, '../20220423UI_AUTO_Test/Bg.jpg')
# urllib.request.urlretrieve(url2, '../20220423UI_AUTO_Test/Block.png')
# '''
# 计算移动距离
# '''
# image = cv.imread('../20220423UI_AUTO_Test/Bg.jpg')
# dis = SlidingValidation.get_pos(image)
# h,w,t = image.shape#(h,w,3)
# #获取移动距离,原始图像是w*h 展示图像是280*163 按比例缩放
# dis = dis*280/w - 31
# print("滑动距离=",dis)
#
# #滑动验证
#
# from selenium.webdriver.common.action_chains import ActionChains
# element = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# #element = driver.find_element_by_id("tcaptcha_drag_thumb")
#
# ActionChains(driver).click_and_hold(element).perform() #点击不放
# ActionChains(driver).move_by_offset(xoffset=dis,yoffset=0).perform() #拖动
# ActionChains(driver).release(element).perform()