from multiprocessing import Process
from multiprocessing import Manager
import time
from fake_useragent import UserAgent
import requests
from time import sleep


def spider(url_queue):
    while not url_queue.empty():
        try:
            url = url_queue.get(timeout = 1)
            # headers = {'User-Agent':UserAgent().chrome}
            print(url)
            # resp = requests.get(url,headers = headers)
            # 处理响应结果
            # for d in resp.json().get('data'):
            #     print(f'tid:{d.get("tid")} topic:{d.get("topicName")} content:{d.get("content")}')
            sleep(1)
            # if resp.status_code == 200:
            #     print(f'成功获取第{i}页数据')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    url_queue = Manager().Queue()
    for i in range(1,11):
        url = f'https://www.hupu.com/home/v1/news?pageNo={i}&pageSize=50'
        url_queue.put(url)

    all_process = []
    for i in range(3):
        p1 = Process(target=spider,args=(url_queue,))
        p1.start()
        all_process.append(p1)
    [p.join() for p in all_process]    