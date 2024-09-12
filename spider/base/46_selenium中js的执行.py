from selenium import webdriver
from time import sleep
chrome  = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
chrome.get('https://search.jd.com/Search?keyword=imac&enc=utf-8&wq=imac')

js = 'document.documentElement.scrollTop=10000'
chrome.execute_script(js)
sleep(2)

info = chrome.find_elements_by_xpath('//div[@class="p-name p-name-type-2"]/a/em')

# for i in info:
#     print(i.text)

print(len(info))
chrome.quit()
