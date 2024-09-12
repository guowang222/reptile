from selenium import webdriver
from lxml import etree
chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')
chrome.get('https://www.huya.com/g/lol')
chrome.implicitly_wait(10)


'''
num = 1
while True:
    count_num = 8
    num +=1
    if num >= count_num:
        break
'''
i = 0
while True:
    e = etree.HTML(chrome.page_source)
    # 1. 使用浏览器的查找元素获取 标签，再获取里面内容
    # rooms = chrome.find_elements_by_class_name('title') 
    # names = chrome.find_elements_by_class_name('nick')
    # counts = chrome.find_elements_by_class_name('js-num')

    # 2. 直接使用源码，通过源码再用xpath提取  （推荐）
    rooms = e.xpath('//a[@class="title"]/text()')
    names = e.xpath('//i[@class="nick"]/text()')
    counts = e.xpath('//i[@class="js-num"]/text()')
    print(f'=========第{i+1}页数据==========')
    # for r, n ,c in zip(rooms,names,counts):
    #     print(f'{r} : {n} : {c}')
    print(len(rooms))
    print(len(names))
    print(len(counts))
    has_next = chrome.page_source.find('laypage_next')
    if has_next != -1:
        chrome.find_element_by_class_name('laypage_next').click()
    else:
        break
    i += 1
chrome.quit()

'''
sleep()
隐式
显式
'''