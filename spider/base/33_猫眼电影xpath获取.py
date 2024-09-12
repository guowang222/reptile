from fake_useragent import UserAgent
import requests
from lxml import etree
from time import sleep

def get_html(url):
    headers = {'User-Agent':UserAgent().chrome}
    resp = requests.get(url,headers=headers)
    sleep(3)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        return resp.text
    else:
        return None
def get_list(html):
    e = etree.HTML(html)
    all_a =  e.xpath('//div/a[@data-act="movies-click"]/@href')
    return all_a
def get_index(html):
    e = etree.HTML(html)
    name = ''.join(e.xpath('//h1[@class="name"]/text()'))
    types = e.xpath('//li[@class="ellipsis"]/a/text()')
    actors_m = e.xpath('//li[@class="celebrity actor"]/div/a/text()')
    actors = format_actors(actors_m)
    return f'电影名：{name}  类型：{types}  演员：{actors}'
def format_actors(a_list):
    actor_set =set()
    for a in a_list:
        actor_set.add(a.strip())
    return actor_set
def start():
    num = int(input('请输入要获取多少页数据：'))
    for i in range(num):
        url = f'https://maoyan.com/films?showType=3&offset={i*30}'
        html = get_html(url)
        all_href = get_list(html)
        for a in all_href:
            url = f'https://maoyan.com{a}'
            index_html = get_html(url)
            info = get_index(index_html)
            print(info)
      
if __name__ == '__main__':
    start()
    # print(get_list())