from selenium import webdriver
import os
from selenium.webdriver import ActionChains
from time import sleep

chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
file = f'file:///{os.path.abspath("./html/scroll.html")}'
chrome.get(file)


div1 = chrome.find_element_by_id('draggable')
div2 = chrome.find_element_by_id('draggable2')
div3 = chrome.find_element_by_id('draggable3')
print(div1)
print(div2)
print(div3)
sleep(2)

ac1 = ActionChains(chrome).drag_and_drop(div1,div2)
ac1.perform()
sleep(2)

ac2 = ActionChains(chrome).drag_and_drop_by_offset(div3,10,10)
for i in range(5):
    ac2.perform()
    sleep(1)

sleep(3)

chrome.quit()