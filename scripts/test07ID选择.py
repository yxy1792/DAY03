
# 导包
import os
from time import sleep

from appium import webdriver

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 关闭设置app

# 查找搜索按钮并点击
driver.find_element_by_id("com.android.settings:id/search").click()
sleep(3)
# 点击返回按钮
driver.find_element_by_class_name("android.widget.ImageButton").click()

sleep(5)
driver.quit()
