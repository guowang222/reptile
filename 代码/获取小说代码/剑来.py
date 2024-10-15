from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


wd = Chrome(service=Service('E:\\tools\\chrome\\chromedriver.exe'))

# 设置访问的URL
url = 'https://www.biqooge.com/1_1010/531479.html'

# 打开网页
wd.get(url)



def content(wd):
    data = {}
    time.sleep(3)
    title = wd.find_element(by=By.TAG_NAME, value='h1')
    data['title'] = title.text
    text = wd.find_element(by=By.ID, value='content')
    data['text'] = text.text
    time.sleep(3)
    link_next = wd.find_elements(by=By.TAG_NAME, value="a")
    link_next[23].click()
    print(data)
    return data

def write_md(data):
    with open(f'I:\python爬虫\\1、基本爬虫\\踏星\\{str(j)}{data.get("title")}.md', 'w', encoding='utf-8') as file:
        file.write(f'# {data.get("title")}\n, {data.get("text")}')


a = True
j = 1
while a:
    data_list = []
    time.sleep(3)
    if wd.find_element(by=By.TAG_NAME, value='h1') == '第一千一百五十四章 签文':
        a = False
    else:
        data = content(wd)
        write_md(data)
        data_list.append(data)
        j += 1

