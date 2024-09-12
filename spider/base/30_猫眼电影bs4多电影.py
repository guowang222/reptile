from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from time import sleep

def get_list():
    num = int(input('请输入要获取多少页数据：'))
    for i in range(num):
        url = 'https://maoyan.com/films?showType=3&offset={i*30}'
        headers = {'User-Agent':UserAgent().chrome}
        resp = requests.get(url,headers=headers)
        soup = BeautifulSoup(resp.text,'lxml')

        all_a =  soup.select('div > a[data-act="movies-click"]')
        return [a.get('href') for a in all_a]
def format_actors(a_list):
    actor_set =set()
    for a in a_list:
        actor_set.add(a.text.strip())
    return actor_set

def start():
    all_href = get_list()
    for a in all_href:
        sleep(2)
        url = f'https://maoyan.com{a}'
        headers = {'User-Agent':UserAgent().chrome}
        resp = requests.get(url,headers=headers)
        soup = BeautifulSoup(resp.text,'lxml')

        name = soup.select('h1.name')[0].text.strip()
        types = soup.select('li.ellipsis')[0].text.strip()
        actors_m = soup.select('li.celebrity.actor > div > a')
        actors = format_actors(actors_m)
        print(f'电影名：{name}  类型：{types}  演员：{actors}')
if __name__ == '__main__':
    start()
    # print(get_list())