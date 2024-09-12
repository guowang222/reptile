from selenium import webdriver
from time import sleep

def test01():
    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    url = 'http://www.baidu.com'
    chrome.get(url)
    chrome.maximize_window() # 最大化窗口
    sleep(3)
    chrome.quit()

def test02():
    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    url = 'http://www.baidu.com'
    chrome.get(url)
    chrome.set_window_size(500,600) # 设置浏览器宽与高
    sleep(3)
    chrome.quit()

def test03():
    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    url = 'http://www.baidu.com'
    chrome.get(url)
    sleep(2)
    chrome.get('http://www.bjsxt.com/')
    sleep(3)
    chrome.back()   # 后退
    sleep(2)
    chrome.forward()    # 前进
    sleep(3)
    chrome.quit()
if __name__ == '__main__':
    test03()