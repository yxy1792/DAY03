# 导包
import time
from appium import webdriver

caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': '192.168.56.101:5555',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'

}

#  获取driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

driver.start_activity("com.android.mms","ui.ConversationList")
time.sleep(5)
driver.quit()