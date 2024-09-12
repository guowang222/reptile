from appium import webdriver
from time import sleep

server = 'http://localhost:4723/wd/hub'
desired = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "SM-N976N",
  "appPackage": "com.android.browser",
  "appActivity": "com.android.browser.BrowserActivity"
}
# 创建模拟器
driver = webdriver.Remote(server,desired)
tmp_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView'
tmp = driver.find_element_by_xpath(tmp_xpath)
tmp.click()
# 输入内容
sleep(1)
input_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[3]/android.view.View/android.widget.EditText'
input = driver.find_element_by_xpath(input_xpath)
input.send_keys('音乐')
# 点按钮
sleep(1)
button_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[3]/android.view.View/android.widget.Button'
button = driver.find_element_by_xpath(button_xpath)
button.click()
