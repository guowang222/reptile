from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


wd = Chrome(service=Service('E:\\tools\\chrome\\chromedriver.exe'))

# 设置访问的URL
url = 'https://www.beqege.cc/407/542951.html'

# 打开网页
wd.get(url)



def content(wd):
    data = {}
    time.sleep(1)
    title = wd.find_element(by=By.TAG_NAME, value='h1')
    data['title'] = title.text
    text = wd.find_element(by=By.ID, value='content')
    data['text'] = text.text
    time.sleep(1)
    link_next = wd.find_elements(by=By.CSS_SELECTOR, value="div[class='bottem1'] > a")
    link_next[2].click()
    print(data)
    return data

def write_md(data):
    text = data.get('text').replace('\n', '\n       ')
    print(text)
    with open(f'I:\python爬虫\\1、基本爬虫\\最强弃少\\{str(j)}{data.get("title")}.md', 'w', encoding='utf-8') as file:
        file.write(f'# {data.get("title")}\n        {text}')


a = True
j = 951
while a:
    data_list = []
    time.sleep(1)
    if wd.find_element(by=By.TAG_NAME, value='h1') == '第一千一百五十四章 签文':
        a = False
    else:
        data = content(wd)
        write_md(data)
        data_list.append(data)
        j += 1

