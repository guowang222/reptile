from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

def test01():
    chrome  = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    chrome.get('https://search.jd.com/Search?keyword=imac&enc=utf-8&wq=imac')

    js = 'document.documentElement.scrollTop=10000'
    chrome.execute_script(js)
    # sleep(2)
    chrome.implicitly_wait(2)
    info = chrome.find_elements_by_xpath('//div[@class="p-name p-name-type-2"]/a/em')

    # for i in info:
    #     print(i.text) 
    print(len(info))
    chrome.quit()

def test02():
    chrome  = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    chrome.get('http://www.baidu.com/')
    chrome.find_element_by_id('kw').send_keys('离岸金融')
    chrome.find_element_by_id('su').click()
    # sleep(1)
    chrome.implicitly_wait(2)
    chrome.find_element_by_xpath('//div[@id="1"]/h3/a').click()

    sleep(3)
    chrome.quit()

def test03():
    chrome  = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
    chrome.get('http://www.baidu.com/')
    chrome.find_element_by_id('kw').send_keys('离岸金融')
    chrome.find_element_by_id('su').click()
    # sleep(1)
    # chrome.implicitly_wait(2)
    # WebDriverWait(chrome,10,0.5).until(lambda element:chrome.find_element_by_xpath('//div[@id="1"]/h3/a'))
    chrome.find_element_by_xpath('//div[@id="1"]/h3/a').click()

    sleep(3)
    chrome.quit()
if __name__ == '__main__':
    # test01()
    # test02()
    test03()
