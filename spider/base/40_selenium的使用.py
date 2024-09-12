from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
chrome.get('http://www.baidu.com/')
html =  chrome.page_source
url = chrome.current_url
chrome.save_screenshot('baidu.png')
sleep(2)
chrome.quit()