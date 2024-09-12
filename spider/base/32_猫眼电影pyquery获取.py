from fake_useragent import UserAgent
import requests
from pyquery import PyQuery
from time import sleep

def get_html(url):
    headers = {'User-Agent':UserAgent().chrome}
    resp = requests.get(url,headers=headers)
    sleep(2)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        return resp.text
    else:
        return None
def get_list(html):
    pq = PyQuery(html)
    all_a =  pq('div > a[data-act="movies-click"]')
    return [a.get('href') for a in all_a]
def get_index(html):
    pq = PyQuery(html)
    name = pq('h1.name').eq(0).text()
    types = pq('li.ellipsis').eq(0).text()
    actors_m = pq('li.celebrity.actor > div > a')
    actors = format_actors(actors_m)
    return f'电影名：{name}  类型：{types}  演员：{actors}'
def format_actors(a_list):
    actor_set =set()
    for a in a_list:
        actor_set.add(a.text.strip())
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