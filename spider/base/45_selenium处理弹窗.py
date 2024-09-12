from selenium import webdriver
import os
from time import sleep

chrome  = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
file = 'file:///'+ os.path.abspath('./html/alter.html')
chrome.get(file)

sleep(3)
# chrome.switch_to_alert().accept() # 过期
chrome.switch_to.alert.accept() # 推荐
sleep(3)

chrome.quit()