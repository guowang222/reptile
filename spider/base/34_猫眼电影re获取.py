from fake_useragent import UserAgent
import requests
import re
from time import sleep

def get_html(url):
    headers = {'User-Agent':UserAgent().chrome}
    resp = requests.get(url,headers=headers)
    sleep(5)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        return resp.text
    else:
        return None
def get_list(html):
    all_a =  re.findall('<a href="(.+?)" target="_blank" data-act="movies-click" data-val="{movieId:\d+}">.+?</a>',html)
    return all_a
def get_index(html):

    name = re.findall('<h1 class="name">(.+?)</h1>',html)[0]
    types = re.findall('<ul>\s+?<li class="ellipsis">\s+?([\S\s]+?)</li>',html)[0]
    types = re.findall('<a .+?>\s*(.+)\s*</a>',types)
    actors_m =re.findall('<li class="celebrity actor".+>\s*<a[\d\D]+?</a>\s*<div.+?>\s+<a[\d\D]+?class="name">\s*(.+?)\s*</a>',html)
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