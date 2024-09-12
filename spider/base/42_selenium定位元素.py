from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.keys import Keys

def test01():
    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    chrome.get('http://www.baidu.com')
    sleep(2)

    chrome.find_element_by_id('kw').send_keys('python')
    sleep(2)

    from selenium.webdriver.common.by import By
    chrome.find_element(by = By.ID,value = 'su').click()
    sleep(2)
    chrome.quit()

def test02():
    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    file_path = 'file:///'+os.path.abspath('./html/test01.html')
    chrome.get(file_path)
    # 定位按钮
    chrome.find_element_by_link_text('Link1').click()
    menu = chrome.find_element_by_id('dropdown1').find_element_by_link_text('Action')

    # webdriver.ActionChains(chrome).move_to_element(menu).perform()    # 移动焦点到某个元素

    menu.click()

    sleep(5)
    chrome.quit()

if __name__ == '__main__':
    test02()