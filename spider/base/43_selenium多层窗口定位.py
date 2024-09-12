from selenium import webdriver
import os
from time import sleep

def test01():
    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    file_path = 'file:///'+os.path.abspath('./html/frame.html')
    chrome.get(file_path)

    chrome.switch_to.frame('f1')
    chrome.switch_to.frame('f2')
    
    chrome.find_element_by_id('kw').send_keys('python')
    chrome.find_element_by_id('su').click()
    sleep(2)

if __name__ == '__main__':
    test01() 