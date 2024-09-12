from random import betavariate
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

def format_actors(a_list):
    actor_set =set()
    for a in a_list:
        actor_set.add(a.text.strip())
    return actor_set

def start():
    url = 'https://maoyan.com/films/1299372'
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