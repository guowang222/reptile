from selenium import webdriver
import os
from time import sleep

chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
file_path = 'file:///'+os.path.abspath('./html/drop_down.html')

chrome.get(file_path)

sleep(3)

select = chrome.find_element_by_id('ShippingMethod')
select.find_element_by_xpath('//option[@value="10.69"]').click()

sleep(3)
chrome.quit()