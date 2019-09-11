# 导包
import os
from time import sleep

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 关闭设置app
# 业务场景:
# 点击搜索按钮
driver.find_element_by_id("com.android.settings:id/search").click()
# 定位到输入框并输入abc
driver.find_element_by_id("android:id/search_src_text").send_keys("你好")

sleep(5)
driver.quit()
WebDriverWait(p)