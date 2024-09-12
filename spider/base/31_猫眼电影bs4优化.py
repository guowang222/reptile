from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
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
    soup = BeautifulSoup(html,'lxml')
    all_a =  soup.select('div > a[data-act="movies-click"]')
    return [a.get('href') for a in all_a]
def get_index(html):
    soup = BeautifulSoup(html,'lxml')
    name = soup.select('h1.name')[0].text.strip()
    types = soup.select('li.ellipsis')[0].text.strip()
    actors_m = soup.select('li.celebrity.actor > div > a')
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