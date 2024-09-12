from threading import Thread
from fake_useragent import UserAgent
import requests
from time import sleep
from queue import Queue

def spider():
    while not url_queue.empty():
        url = url_queue.get()
        headers = {'User-Agent':UserAgent().chrome}
        print(url)
        resp = requests.get(url,headers = headers)
        # 处理响应结果
        # for d in resp.json().get('data'):
        #     print(f'tid:{d.get("tid")} topic:{d.get("topicName")} content:{d.get("content")}')
        sleep(3)
        if resp.status_code == 200:
            print(f'成功获取第{i}页数据')


if __name__ == '__main__':
    url_queue = Queue()
    for i in range(1,11):
        url = f'https://www.hupu.com/home/v1/news?pageNo={i}&pageSize=50'
        url_queue.put(url)

    for i in range(3):
        t1 = Thread(target=spider)
        t1.start()
   