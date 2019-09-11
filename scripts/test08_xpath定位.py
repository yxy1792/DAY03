
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
# 业务场景:
# 1.进入设置页面
# 精准定位
driver.find_element_by_xpath("//*[@text,'WLA']").click()
# 模糊定位
driver.find_element_by_xpath("//*[contains(@text,'WLA')]").click()
# driver.find_element_by_xpath("//*[contains(@resource-id,'com.android.settings:id/search')]")
# driver.find_element_by_xpath("//*[contains(@class,'android.widget.ImageButton')]")
# 2.点击WLAN菜单栏



sleep(5)
driver.quit()